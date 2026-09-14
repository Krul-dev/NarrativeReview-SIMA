# Formal Search: Missing Bridge Between DL Imputation and Statistical Validity

Objective: Document whether a paper exists that formally proves time-series DL imputation
produces Rubin-valid inference under stated missingness conditions. Professors Raúl and
Blanca Rosa agreed this claim requires a traceable, reported search (2026-09-09).

Databases: Web of Science, Scopus
Date searched: ____

---

## Boolean Queries

### Query 1 — Broad: DL imputation + statistical theory (no time-series filter)

**Web of Science (Topic field = title, abstract, keywords):**
```
TS=( ("deep learning" OR "neural network*" OR "generative adversarial" OR "variational autoencoder" OR "transformer" OR "diffusion model")
AND ("imputation" OR "missing data" OR "missing values")
AND ("Rubin" OR "ignorab*" OR "posterior distribut*" OR "multiple imputation" OR "inferential valid*" OR "statistical valid*" OR "proper imputation" OR "congeniality") )
```

**Scopus (TITLE-ABS-KEY):**
```
TITLE-ABS-KEY( ("deep learning" OR "neural network*" OR "generative adversarial" OR "variational autoencoder" OR "transformer" OR "diffusion model")
AND ("imputation" OR "missing data" OR "missing values")
AND ("Rubin" OR "ignorab*" OR "posterior distribut*" OR "multiple imputation" OR "inferential valid*" OR "statistical valid*" OR "proper imputation" OR "congeniality") )
```

**What this finds:** Any paper that combines DL imputation with Rubin's framework, regardless of data type. Expect: a handful of tabular papers (not-MIWAE, MIWAE, FragmGAN, etc.) but likely nothing for time series.

### Query 2 — Narrow: DL imputation + statistical theory + time series

**Web of Science:**
```
TS=( ("deep learning" OR "neural network*" OR "generative adversarial" OR "variational autoencoder" OR "transformer" OR "diffusion model")
AND ("imputation" OR "missing data" OR "missing values")
AND ("Rubin" OR "ignorab*" OR "posterior distribut*" OR "inferential valid*" OR "statistical valid*" OR "proper imputation")
AND ("time series" OR "temporal" OR "sequential" OR "longitudinal") )
```

**Scopus:**
```
TITLE-ABS-KEY( ("deep learning" OR "neural network*" OR "generative adversarial" OR "variational autoencoder" OR "transformer" OR "diffusion model")
AND ("imputation" OR "missing data" OR "missing values")
AND ("Rubin" OR "ignorab*" OR "posterior distribut*" OR "inferential valid*" OR "statistical valid*" OR "proper imputation")
AND ("time series" OR "temporal" OR "sequential" OR "longitudinal") )
```

**What this finds:** The exact bridge paper, if it exists. Expect: zero or near-zero results.

### Query 3 — Alternative framing: DL imputation + missingness mechanism validity

**Web of Science:**
```
TS=( ("deep learning" OR "neural network*" OR "recurrent neural" OR "self-attention" OR "BRITS" OR "SAITS" OR "CSDI" OR "GAIN")
AND ("imputation")
AND ("missing at random" OR "MCAR" OR "MNAR" OR "missing not at random" OR "missingness mechanism" OR "ignorab*" OR "selection model" OR "pattern mixture") )
```

**Scopus:**
```
TITLE-ABS-KEY( ("deep learning" OR "neural network*" OR "recurrent neural" OR "self-attention" OR "BRITS" OR "SAITS" OR "CSDI" OR "GAIN")
AND ("imputation")
AND ("missing at random" OR "MCAR" OR "MNAR" OR "missing not at random" OR "missingness mechanism" OR "ignorab*" OR "selection model" OR "pattern mixture") )
```

**What this finds:** Papers that at least discuss which missingness mechanism their DL model assumes. Broader than Query 1 — may find papers that discuss mechanisms without citing Rubin. Check if any provide formal proofs vs. just mentioning assumptions.

### Query 4 — Convergence proof: NN imputation + posterior/distribution guarantee

**Web of Science:**
```
TS=( ("neural network*" OR "deep learning")
AND ("imputation" OR "missing value*" OR "missing data")
AND ("convergence" OR "posterior predictive" OR "distributional guarantee" OR "consistent estimat*" OR "asymptotic" OR "Bayesian posterior")
AND ("proof" OR "theorem" OR "proposition" OR "lemma") )
```

**Scopus:**
```
TITLE-ABS-KEY( ("neural network*" OR "deep learning")
AND ("imputation" OR "missing value*" OR "missing data")
AND ("convergence" OR "posterior predictive" OR "distributional guarantee" OR "consistent estimat*" OR "asymptotic" OR "Bayesian posterior")
AND ("proof" OR "theorem" OR "proposition" OR "lemma") )
```

**What this finds:** Papers that provide formal mathematical proofs about NN imputation convergence. This is the most specific query — looks for the Richard & Lippmann (1991) equivalent for imputation.

---

## How to Log Results

For each query, record in the table below:

| Query | Database | Date | Results | Relevant after screening | Notes |
|-------|----------|------|---------|--------------------------|-------|
| Q1    | WoS      |      |         |                          |       |
| Q1    | Scopus   |      |         |                          |       |
| Q2    | WoS      |      |         |                          |       |
| Q2    | Scopus   |      |         |                          |       |
| Q3    | WoS      |      |         |                          |       |
| Q3    | Scopus   |      |         |                          |       |
| Q4    | WoS      |      |         |                          |       |
| Q4    | Scopus   |      |         |                          |       |

For "Relevant after screening": read titles/abstracts of all results. Mark how many actually
address the bridge (formal proof that DL imputation → valid statistical inference). If any do,
note the citation.

**What counts as "the bridge paper":** A paper that proves or formally argues that a specific
DL imputation architecture produces samples from (or converges to) the posterior predictive
distribution P(X_mis | X_obs) under stated missingness conditions (MAR, MNAR, or specific
assumptions).

**What does NOT count:** Papers that merely mention "MAR" in passing, or evaluate under
synthetic MCAR without proving validity, or use "multiple imputation" to mean "impute
several times and average" without Rubin's pooling rules.

---

## Reporting in §2

In the Review Methodology section, describe this search briefly:

> To support our finding that no formal theoretical bridge exists between time-series
> deep learning imputation and Rubin's inferential framework, we conducted targeted
> Boolean searches in Web of Science and Scopus on [date]. Queries combined deep
> learning architecture terms with statistical validity concepts (ignorability, posterior
> distributions, Rubin's framework) and time-series terms. Query details and results
> are available in [supplementary / appendix]. [Q1] returned N results in WoS and M
> in Scopus; after title/abstract screening, K addressed the bridge for tabular data
> (notably not-MIWAE, FragmGAN, PSMVAE) but none for time-series architectures.
> [Q2], restricted to time series, returned N results with zero relevant after screening.
