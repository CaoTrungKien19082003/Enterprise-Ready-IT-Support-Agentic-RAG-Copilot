# Benchmark report

- Created: 2026-10-14T13:35:37
- Config: `{"mode": "inprocess", "dataset": "dataset.jsonl", "judge": null, "workers": 4, "repeats": 1, "openai_model": "gpt-4o-mini", "embedding_model": "text-embedding-3-small", "top_k": 4, "max_retries": 1, "pinecone_index": "en-ready-rag", "namespace": "roscaelifer-it-kb"}`
- Cases / runs: 5 / 5  (wall time 15.8s)

## Metrics

| metric | value | n |
|---|---:|---:|
| pass_rate | 100.0% | 5 |
| error_rate | 0.0% | 5 |
| route_accuracy | 100.0% | 5 |
| source_strict | 100.0% | 5 |
| source_acceptable | 100.0% | 5 |
| keyword_pass | 100.0% | 5 |
| doc_hit_rate | 100.0% | 5 |
| evidence_hit_rate | 100.0% | 5 |
| mrr_evidence | 0.87 | 5 |
| avg_trace_steps | 4.00 | 5 |
| latency_mean_s | 10.70s | 5 |
| latency_p50_s | 11.84s | 5 |
| latency_p95_s | 13.22s | 5 |
| rewrite_rate | 0.0% | 5 |
| web_fallback_rate | 0.0% | 5 |
| insufficient_rate | 0.0% | 5 |

## By category

| category | runs | pass rate | mean latency |
|---|---:|---:|---:|
| kb_handbook | 5 | 100.0% | 10.70s |

## Failures (0)
