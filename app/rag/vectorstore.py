import time
from pinecone import Pinecone, ServerlessSpec
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from app.core.config import get_settings

settings = get_settings()


_embeddings = None
_vectorstore = None



EMBEDDING_DIMENSION = {
    "text-embedding-3-small": 1536,
    "text-embedding-3-large": 3072,
    "text-embedding-3-xl": 6144,
    "text-embedding-ada-002": 1536,
    "all-minilm-l6-v2": 384
    #you can add more embedding models and their dimensions here as needed
}

def get_embeddings_dimension(model_name: str | None = None) -> int:
    name = (model_name or settings.embedding_model or "").strip()
    if not name:
        raise ValueError("Model name must be provided to get its embedding dimension.")
    
    normalized = name.lower()
    if normalized in EMBEDDING_DIMENSION:
        return EMBEDDING_DIMENSION[normalized]
    if "text-embedding-3-small" in normalized:
        return 1536
    if "text-embedding-3-large" in normalized:
        return 3072
    if "text-embedding-3-xl" in normalized:
        return 6144
    if "text-embedding-ada-002" in normalized:    
        return 1536
    if "all-minilm-l6-v2" in normalized:
        return 384

    raise ValueError(
        f"Unknown embedding model: '{model_name or settings.embedding_model}'. Please provide a valid model name and add the matching dimension to EMBEDDING_DIMENSION."
    )

def get_embeddings():
    global _embeddings
    if _embeddings is None:
        if not settings.openai_api_key:
            raise ValueError("OpenAI API key is not set. Please set it in the environment or .env file.")
        _embeddings = OpenAIEmbeddings(
            model=settings.embedding_model,
            openai_api_key=settings.openai_api_key
        )
    return _embeddings


def ensure_index():
    if not settings.pinecone_api_key:
        raise ValueError("Pinecone API key is not set. Please set it in the environment or .env file.")

    desired_dimension = get_embeddings_dimension()
    pc = Pinecone(api_key=settings.pinecone_api_key)
    names = [x["name"] for x in pc.list_indexes()]

    if settings.pinecone_index_name in names:
        index_info = pc.describe_index(settings.pinecone_index_name)
        current_dimension = getattr(index_info, "dimension", None)
        if current_dimension is None and isinstance(index_info, dict):
            current_dimension = index_info.get("dimension")
            
        if current_dimension is None and current_dimension != desired_dimension:
            pc.delete_index(name=settings.pinecone_index_name)
            while settings.pinecone_index_name in [x["name"] for x in pc.list_indexes()]:
                time.sleep(1)
    
    if settings.pinecone_index_name not in [x["name"] for x in pc.list_indexes()]:
        pc.create_index(
            name=settings.pinecone_index_name,
            dimension=desired_dimension,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
        while not pc.describe_index(settings.pinecone_index_name).status["ready"]:
            time.sleep(1)

    return pc.Index(name=settings.pinecone_index_name)

def get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        index = ensure_index()
        _vectorstore = PineconeVectorStore(
            index=index, 
            embedding=get_embeddings(),
            namespace=settings.pinecone_namespace
        )
    return _vectorstore

def get_retriever():
    return get_vectorstore().as_retriever(search_kwargs={"k": settings.top_k})

def add_documents(chunks):
    store = get_vectorstore()
    return store.add_documents(chunks)