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
2. [DONE] Export deduplicated set, upload to NotebookLM
3. [DONE] Prompt NotebookLM with screening criteria in 16 batches of ~30 papers each
4. [IN PROGRESS] Verify NotebookLM's top-tier classifications manually (positive controls: not-MIWAE, FragmGAN, PSMVAE)
5. [ ] Record final counts: total unique, relevant after screening, any new finds

**Screening result:** 16 batches completed → 472 papers screened. Merged into `Q1_all_batches.csv` (2026-09-15).

**Papers to review:** 67 total — 21 category A (formal bridge), 46 category B (discusses validity). Manual verification in progress (2026-09-18).

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

## Q1 Full-Text Verification (2026-09-18)

**Goal:** Verify the 67 A/B papers using full text in NotebookLM. The abstract-only screening may have over-classified papers; full text lets us confirm or downgrade.

**Batching:** 5–7 papers per batch (full text is much larger than abstracts — smaller batches to avoid hallucination).

**Important distinction — imputation vs. training with missing data:**
Some papers discuss missing data only in the context of *training* a model (e.g., handling incomplete inputs during supervised learning, or training a classifier when some features are absent). These are NOT about imputation. Our review is about papers where imputation itself is the goal — generating plausible replacements for missing values. Papers that only address missing data as a training nuisance should be downgraded to C/D.

### A papers verification — DONE (2026-09-18)

Ran 21 papers through NotebookLM in batches of 4–5. **5 confirmed as A:**

1. Multiple Imputation via Generative Adversarial Network for High-dimensional Blockwise Missing Value Problems
2. Multiple Imputation with Neural Network Gaussian Process for High-dimensional Incomplete Data
3. Missing Data Imputation with Uncertainty-Driven Network
4. GAIN: Missing Data Imputation using Generative Adversarial Nets
5. Generative Conditional Missing Imputation Networks

Remaining 16 downgraded. Full reading of the 5 confirmed-A papers pending.

**Note:** Positive controls (not-MIWAE, FragmGAN, PSMVAE) did not appear in the confirmed list — need to check whether they were in the original Q1 search results at all or were filtered out earlier.

### Prompt used for A papers

```
You have the full text of N papers. For each one, answer these questions exactly:

1. **Is this about imputation?** Does the paper treat imputation (filling in missing values) as its primary goal? Or does it only address missing data as a nuisance during model training (e.g., training a classifier with incomplete features)? If the latter, mark as NOT-IMPUTATION.

2. **Formal result?** Does the paper contain a theorem, proposition, lemma, or proof that a deep learning architecture's imputations converge to or sample from the posterior predictive distribution P(X_mis | X_obs)? If yes, quote the theorem statement or the key sentence. If no, say NO.

3. **Missingness assumption?** What missingness mechanism does the formal result require? (MAR, MNAR, MCAR, or specific assumptions). If no formal result, what does the paper assume without proving?

4. **Architecture?** What DL architecture is covered? (VAE, GAN, transformer, RNN, diffusion, etc.)

5. **Data type?** Is the formal result about tabular data, time series, or both? If time series, is it multivariate?

6. **Verdict:**
   - CONFIRMED-A — formal proof exists, paper is about imputation
   - DOWNGRADE-B — discusses validity but no proof
   - DOWNGRADE-C/D — not relevant or not about imputation

Output a table with columns: authors, year, title, is_imputation (YES/NOT-IMPUTATION), formal_result (YES + quote / NO), missingness_assumption, architecture, data_type, verdict.
```

### B papers verification — DONE (2026-09-19)

Ran 46 papers through NotebookLM in batches of 4–5. **0 upgraded to A. No hidden formal proofs found.**

**Papers not uploaded (access issues):**
- "A Novel Approach for Ultra-High Performance Concrete Data Augmentation..." — only available in Chinese, no English full text found
- "Accounting for Imputation Uncertainty During Neural Network Training" — no free full text available
- "Context-Aware Imputation for Parkinson's Disease Trajectories..." — no free full text available
- "Handling Missing Data" — this is a book, not uploaded to NotebookLM
- "Improvements Achieved by Multiple Imputation for Single-Cell RNA-Seq Data in Clustering Analysis and Differential Expression Analysis" — not found

**Papers not uploaded but flagged for manual review:**
- **KAI: A Scalable Kalman-Attention Imputation Method for Robust Inference in Probabilistic Data** — no free full text found, but abstract is highly relevant. Claims a hybrid Kalman-attention model for multivariate time series that tests under MCAR/MAR/MNAR and reports interval coverage under multiple imputation. If it validates Rubin-style inference (not just RMSE), this could be the closest paper to the time-series bridge. **Must find and read this paper.**

### Prompt used for B papers

```
You have the full text of N papers. These were initially classified as "discusses statistical validity of DL imputation but without a formal proof." For each one, answer:

1. **Is this about imputation?** Does the paper treat imputation (filling in missing values) as its primary goal? Or does it only address missing data as a nuisance during model training (e.g., training a classifier with incomplete features)? If the latter, mark as NOT-IMPUTATION.

2. **Hidden formal result?** Check the appendix, supplementary material, and proofs section. Does the paper contain a theorem or proof about convergence to posterior predictive distributions that was missed in abstract screening? If yes, quote it.

3. **What validity discussion?** In 1–2 sentences, what specifically does the paper say about statistical validity, Rubin's framework, proper imputation, or inferential correctness? Quote the key passage.

4. **Data type?** Tabular, time series, or both?

5. **Verdict:**
   - UPGRADE-A — found a formal proof, paper is about imputation
   - CONFIRMED-B — substantive validity discussion, paper is about imputation
   - DOWNGRADE-C/D — only mentions MAR/MCAR in passing, not substantive, or not about imputation

Output a table with columns: authors, year, title, is_imputation (YES/NOT-IMPUTATION), hidden_formal_result (YES + quote / NO), validity_discussion, data_type, verdict.
```

## Decisions & Notes
- Using Zotero for deduplication (DOI merge) and NotebookLM for bulk abstract screening
- NotebookLM results to be verified manually for anything flagged as having formal proofs
- Positive controls: not-MIWAE, MIWAE, FragmGAN, PSMVAE, Beyond Accuracy should appear in Q1 results
- **NotebookLM hallucinated when given 473 papers at once.** Switching to batches of ~30 papers to reduce hallucination. That's ~16 batches for Q1.
- **Training vs. imputation confusion:** Some papers in the results discuss missing data only in the context of training ML models, not as an imputation problem. These should be downgraded during verification.
