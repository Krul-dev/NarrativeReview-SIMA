# Bridge Search Session — 2026-09-14

## Objective
Execute the 4 Boolean queries from `bridge_search_queries.md` in WoS + Scopus, screen results, and fill the results table to document that no time-series DL → Rubin bridge paper exists.

## Progress

### Query 1 — Broad: DL imputation + statistical theory (no time-series filter)

**Raw results:**
- Scopus: 325 documents
- Web of Science: 348 documents

**Workflow:**
1. [DONE] Import both exports into Zotero collection "Bridge Search Q1", deduplicate by DOI → **473 unique papers**
2. [ ] Export deduplicated set, upload to NotebookLM
3. [ ] Prompt NotebookLM with screening criteria (classify into formal proof / discusses validity / mentions in passing)
4. [ ] Verify NotebookLM's top-tier classifications manually (positive controls: not-MIWAE, FragmGAN, PSMVAE)
5. [ ] Record final counts: total unique, relevant after screening, any new finds

**Screening result:** (pending)

### Query 2 — Narrow: DL imputation + statistical theory + time series
- Scopus: ___
- Web of Science: ___

### Query 3 — Alternative: DL imputation + missingness mechanism validity
- Scopus: ___
- Web of Science: ___

### Query 4 — Convergence proof: NN imputation + posterior/distribution guarantee
- Scopus: ___
- Web of Science: ___

## NotebookLM Screening Prompt (Q1)

```
You are screening papers from a literature search. The search goal is to find papers that formally connect deep learning imputation methods to Rubin's statistical framework for missing data inference.

For each paper in the uploaded collection, classify it into one of these categories:

- A — Formal bridge: The paper provides a formal proof, theorem, or rigorous mathematical argument that a deep learning imputation architecture produces samples from (or converges to) the posterior predictive distribution P(X_mis | X_obs) under stated missingness conditions (MAR, MNAR, or specific assumptions). Examples: not-MIWAE, FragmGAN, PSMVAE.
- B — Discusses validity: The paper substantively discusses the statistical validity of DL imputation (e.g., proper imputation, congeniality, Rubin's rules, inferential vs. predictive accuracy) but does NOT provide a formal proof.
- C — Mentions in passing: The paper mentions Rubin, MAR/MCAR/MNAR, or multiple imputation but only as background — the paper's main contribution is not about the bridge between DL and statistical validity.
- D — Not relevant: The paper does not address the connection between DL imputation and statistical inference theory.

Additionally, flag whether each paper addresses time series data specifically (YES/NO).

Output a CSV with these columns:
- authors — first author et al.
- year
- title
- category — A, B, C, or D
- time_series — YES or NO
- reasoning — one sentence explaining the classification
- verdict — REVIEW (for A and B), SKIP (for C and D)


Sort the CSV by category (A first, then B, C, D).
```

## Decisions & Notes
- Using Zotero for deduplication (DOI merge) and NotebookLM for bulk abstract screening
- NotebookLM results to be verified manually for anything flagged as having formal proofs
- Positive controls: not-MIWAE, MIWAE, FragmGAN, PSMVAE, Beyond Accuracy should appear in Q1 results
- **NotebookLM hallucinated when given 473 papers at once.** Switching to batches of ~30 papers to reduce hallucination. That's ~16 batches for Q1.
