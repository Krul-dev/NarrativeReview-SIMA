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

**Raw results:**
- Combined (WoS + Scopus): 13 documents (1 retracted)

**Screening:** Single-batch NotebookLM screening (13 papers fits in one pass).

### Prompt used for Q2 screening

```
You are screening 13 papers from a targeted literature search. The search goal is to find papers that formally prove time-series deep learning imputation produces statistically valid inference under Rubin's framework.

First: if any paper is marked as RETRACTED, classify it as R — Retracted and skip further analysis.

For each remaining paper, answer:

1. **Is this about imputation?** Is filling in missing values the paper's primary goal? If it only handles missing data as a nuisance during model training, mark NOT-IMPUTATION.

2. **Formal result?** Does the paper contain a theorem, proposition, or proof that a DL architecture's imputations converge to or sample from the posterior predictive distribution P(X_mis | X_obs)? If yes, quote the key statement. If no, say NO.

3. **Time series?** Does the formal result (or the method) specifically address temporal/sequential/longitudinal data? Or is it tabular-only?

4. **Missingness assumption?** What mechanism does the paper assume or prove validity under? (MCAR, MAR, MNAR, specific conditions)

Classify into:
- A — Formal bridge: proof/theorem that DL imputation → valid posterior draws. Time series = strongest signal.
- B — Discusses validity: substantive discussion of statistical validity of DL imputation but no proof.
- C — Mentions in passing: MAR/MCAR/Rubin as background only.
- D — Not relevant: not about imputation or the DL–statistics bridge.
- R — Retracted.

Output a CSV with columns:
authors, year, title, category, is_imputation, formal_result, time_series, missingness_assumption, reasoning, verdict (REVIEW for A/B, SKIP for C/D/R)
```

**Screening result:** 6 papers confirmed as imputation-related. 1 retracted, rest not relevant. Proceeding to full-text verification of the 6.

### Q2 full-text verification (2026-09-22)

**Goal:** Verify the 6 imputation papers using full text. Single batch.

### Prompt used for Q2 full-text verification

```
You have the full text of 6 papers. These were identified by a literature search for papers that combine deep learning imputation with statistical validity theory specifically for time series data. The goal is to determine whether any of them contains a formal proof that a DL imputation architecture produces Rubin-valid posterior draws for time series.

For each paper, answer:

1. **Is this about imputation of time series?** Confirm the paper treats imputation of temporal/sequential/longitudinal data as its primary goal. If it is tabular-only or only handles missing data during training, note that.

2. **Formal result?** Check the main text, appendix, and supplementary material. Does the paper contain a theorem, proposition, lemma, or proof that the model's imputations converge to or sample from the posterior predictive distribution P(X_mis | X_obs) under stated missingness conditions? If yes, quote the exact theorem statement. If no, say NO.

3. **What does it claim?** In 1–2 sentences, what is the paper's actual contribution regarding missing data? Does it just optimize RMSE/MAE, or does it discuss inferential validity, uncertainty calibration, Rubin's pooling rules, or proper imputation?

4. **Missingness assumption?** What mechanism does the paper assume (MCAR, MAR, MNAR)? Is this stated formally or just mentioned?

5. **Verdict:**
   - CONFIRMED-A — formal proof exists, paper is about time-series imputation
   - DOWNGRADE-B — discusses validity but no proof
   - DOWNGRADE-C/D — no substantive bridge content, or not actually about time-series imputation

Output a table with columns: authors, year, title, is_ts_imputation (YES/NO), formal_result (YES + quote / NO), contribution_summary, missingness_assumption, verdict
```

**Verification result:** 0 confirmed-A. No formal proofs found. All 6 papers optimize point accuracy (RMSE/MAE) without proving convergence to Rubin-valid posterior draws for time series.

### Query 3 — Alternative: DL imputation + missingness mechanism validity

**Raw results:**
- Combined (WoS + Scopus): 177 documents

**Workflow:**
1. [ ] Screen in NotebookLM in batches of ~30 (6 batches), abstracts + metadata
2. [ ] Collect A/B papers for full-text verification
3. [ ] Full-text verification of A/B papers
4. [ ] Record final counts

### Prompt used for Q3 screening

```
You are screening papers from a literature search. You have metadata and abstracts but NOT full text. The search goal is to find papers where a deep learning imputation method formally addresses which missingness mechanism (MCAR, MAR, MNAR) it is valid under.

For each paper, based on the title, keywords, and abstract, classify:

- A — Formal bridge: the abstract describes a proof, theorem, or formal analysis that a DL imputation method produces valid inference under specific missingness conditions. Look for: "proof," "theorem," "guarantee," "posterior," "Rubin," "ignorability," "proper imputation," "convergence" combined with a DL architecture.
- B — Discusses validity: the abstract substantively engages with missingness mechanisms AND the statistical validity of DL/ML imputation (e.g., "MNAR-aware," "mechanism-agnostic," "sensitivity analysis for neural imputation," discusses when a method breaks under mechanism shift). More than just testing under MCAR/MAR as experimental conditions.
- C — Mentions mechanism as assumption only: the abstract mentions MCAR/MAR/MNAR but only as experimental settings or background assumptions. Most DL imputation papers that "evaluate under different missing rates and mechanisms" fall here.
- D — Not relevant: not about imputation (e.g., classification, detection, prediction with missing inputs), or not related to the DL–statistics bridge at all.

Additionally note whether the paper addresses time series (YES/NO/UNCLEAR).

Important: with abstracts only, err on the side of inclusion — if uncertain between B and C, choose B. We will verify with full text later.

Output a CSV with columns:
authors, year, title, category, time_series, reasoning, verdict (REVIEW for A/B, SKIP for C/D)
```

**Screening result:** 177 papers screened in 6 batches. Merged into `Notebooklm/Q_3/Q3_all_batches.csv`.
- A (formal bridge): 6
- B (discusses validity): 36
- C (mentions in passing): 60
- D (not relevant): 75

**Papers to verify:** 42 total (6 A + 36 B). Full-text verification in batches of 6 (~7 batches).

### Prompt used for Q3 full-text verification

```
You have the full text of 6 papers. These were identified by a literature search for papers where a deep learning imputation method formally addresses which missingness mechanism (MCAR, MAR, MNAR) it is valid under. The goal is to determine whether any of them contains a formal proof that a DL imputation architecture produces Rubin-valid posterior draws.

For each paper, answer:

1. **Is this about imputation?** Is filling in missing values the paper's primary goal? If it only handles missing data during model training or is about classification/prediction, mark NOT-IMPUTATION.

2. **Formal result?** Check the main text, appendix, and supplementary material. Does the paper contain a theorem, proposition, lemma, or proof that the model's imputations converge to or sample from the posterior predictive distribution P(X_mis | X_obs) under stated missingness conditions? If yes, quote the exact theorem statement. If no, say NO.

3. **What does it claim about missingness mechanisms?** Does the paper formally prove validity under a specific mechanism, or does it just test empirically under MCAR/MAR/MNAR as experimental conditions? Be precise — "evaluated under MNAR" is not the same as "proven valid under MNAR."

4. **Data type?** Tabular, time series, or both? If time series, is it multivariate?

5. **Verdict:**
   - CONFIRMED-A — formal proof exists, paper is about imputation
   - DOWNGRADE-B — discusses validity but no proof
   - DOWNGRADE-C/D — no substantive bridge content, only mentions mechanisms as experimental settings, or not about imputation

Output a table with columns: authors, year, title, is_imputation (YES/NOT-IMPUTATION), formal_result (YES + quote / NO), mechanism_claim (FORMAL PROOF / EMPIRICAL ONLY / MENTIONS ONLY), data_type, verdict
```

**Papers not found (no free full text, 2026-09-22):**
- A Hybrid Self-Supervised Framework for Intelligent Data Imputation Using Causal Graphs, Diffusion Models, and Generative World Learning
- A Hybrid Self-supervised Learning Framework for Missing Data Imputation in Cloud-Based Data Mining Systems
- A Modular Framework for Multimorbidity Prediction with MNAR-Aware Imputation and Label-Enhanced Transformers
- Clustering-Informed Shared-Structure Variational Autoencoder for Missing Data Imputation in Large-Scale Healthcare Data
- Comparing the Performance of Recurrent Neural Network and Some Well-Known Statistical Methods in the Case of Missing Multivariate Time Series Data
- **KAI: A Scalable Kalman-Attention Imputation Method for Robust Inference in Probabilistic Data** — also flagged in Q1 B verification. Still no full text. Remains the most promising lead for a time-series bridge.
- MiCaST: Missingness-Aware Causal Attention and Missing-Conditioned Phase Alignment for Time Series
- Physics-guided conditional generative imputation of gappy GNSS coordinate measurements under mixed missingness
- Siamese Autoencoder-Based Approach for Missing Data Imputation

**Verification result (2026-09-22):** 33 papers verified in 6 batches (9 not found, see above). Merged into `Notebooklm/Q_3/Review_AB/Q3_review_all.csv`.
- CONFIRMED-A: 1 — Dai, Bu & Long (2021) "Multiple Imputation via Generative Adversarial Network for High-dimensional Blockwise Missing Value Problems." Formal theorems proving GAN convergence to true conditional distribution under MAR. **Tabular only, not time series.**
- DOWNGRADE-B: 6
- DOWNGRADE-C/D: 26

**Q3 conclusion:** No formal proof found for time-series DL imputation. The one confirmed-A paper (Dai et al. 2021) is tabular, consistent with Q1 and Q2 findings.

### Query 4 — Convergence proof: NN imputation + posterior/distribution guarantee

**Raw results:**
- Combined (WoS + Scopus): 3 documents

**Screening:** None of the 3 papers are about imputation. All are false positives from keyword overlap:
1. Qaffas (2026) — blockchain + IoT data transfer
2. Linda & Griffin (2026) — blockchain + credit card fraud detection with zeroing neural network
3. Cai et al. (2026) — matrix completion (low-rank recovery, not missing-data imputation in Rubin's sense)

**Q4 conclusion:** 0 relevant papers. No convergence proofs for NN imputation exist in WoS/Scopus under this query. Data saved in `Notebooklm/Q_4/Q4_all.csv`.

## Summary of Findings (all queries complete, 2026-09-23)

Four Boolean queries were run across Web of Science and Scopus to search for a paper that formally proves time-series deep learning imputation produces Rubin-valid statistical inference. A total of 666 papers were retrieved, deduplicated, screened by abstract, and verified by full text where applicable.

| Query | Scope | Papers | Confirmed-A | Time series? |
|-------|-------|--------|-------------|--------------|
| Q1 | DL imputation + statistical theory (broad) | 473 | 5 | No — all tabular |
| Q2 | DL imputation + statistical theory + time series | 13 | 0 | — |
| Q3 | DL imputation + missingness mechanism validity | 177 | 1 (Dai et al. 2021) | No — tabular |
| Q4 | NN imputation + convergence/posterior proof | 3 | 0 | — |

**Conclusion:** No paper in the literature formally proves that a time-series DL imputation architecture (BRITS, SAITS, CSDI, or similar) produces samples from the posterior predictive distribution P(X_mis | X_obs) under stated missingness conditions. The few confirmed formal results (6 total across Q1 and Q3) are all for tabular data. The missing bridge between Rubin's framework and time-series deep learning imputation remains unproven — this is a key contribution of the review.

**Caveats:**
- 9 papers in Q3 could not be accessed for full-text verification, including KAI (Kalman-attention for time series), which remains the most promising unfound lead.
- Positive controls (not-MIWAE, FragmGAN, PSMVAE) from our existing collection did not appear in Q1 confirmed results — needs verification of whether they were captured by the search queries.

---

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
