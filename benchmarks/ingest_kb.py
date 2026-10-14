#!/usr/bin/env python3
"""
Index data/sample_kb/* into Pinecone so the benchmark has something to retrieve.
(The repo's ingest_sample_kb.py is currently an empty file.)

Vector ids are deterministic ("<file>-<chunk n>"), so re-running overwrites instead of
creating duplicate chunks, which would otherwise distort retrieval metrics.

  python benchmarks/ingest_kb.py            # upsert all sample docs
  python benchmarks/ingest_kb.py --reset    # wipe the namespace first (removes uploaded docs too!)
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.config import get_settings  # noqa: E402
from app.rag.vectorstore import ensure_index, get_vectorstore  # noqa: E402
from app.services.ingestion import SUPPORTED, chunk_documents, load_file  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reset", action="store_true", help="delete every vector in the namespace first")
    ap.add_argument("--dir", type=Path, default=None, help="folder to index (default: SAMPLE_KB_DIR)")
    a = ap.parse_args()

    s = get_settings()
    kb_dir = a.dir or Path(s.sample_kb_dir)
    files = sorted(p for p in kb_dir.iterdir() if p.suffix.lower() in SUPPORTED)
    if not files:
        sys.exit(f"No supported documents in {kb_dir}")

    if a.reset:
        ensure_index().delete(delete_all=True, namespace=s.pinecone_namespace)
        print(f"Namespace '{s.pinecone_namespace}' cleared.")

    store = get_vectorstore()
    total = 0
    for f in files:
        chunks = chunk_documents(load_file(f))
        ids = [f"{f.stem}-{i:04d}" for i in range(len(chunks))]
        store.add_documents(chunks, ids=ids)
        total += len(chunks)
        print(f"{f.name}: {len(chunks)} chunks")
    print(f"Done: {total} chunks in index '{s.pinecone_index_name}', namespace '{s.pinecone_namespace}'.")


if __name__ == "__main__":
    main()
