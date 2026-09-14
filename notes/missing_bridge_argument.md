# The Missing Bridge: Why This Is a Key Contribution

Personal reference note — not tracked in git.

## The problem

The review claims to trace a path from Rubin's theory (1976) to modern DL imputation (SAITS, CSDI).
But when we searched for the theoretical connection, we found it doesn't exist for time series.

## What we found

The MNAR-aware deep learning papers work on **tabular data**:
- **FragmGAN** (Fang 2023) — proves GAIN's hint mechanism assumes MCAR. Tabular.
- **not-MIWAE** (Ipsen 2021) — VAE that models the missingness mask under MNAR. Tabular.
- **PSMVAE** (Ghalebikesabi 2021) — combines VAE with pattern-mixture models. Tabular.
- **MIWAE** (Mattei 2019) — importance-weighted VAE under MAR. Tabular.

The time-series DL papers (BRITS, SAITS, CSDI) **don't state or verify missingness conditions**:
- They optimize RMSE/MAE.
- They don't prove they produce valid posterior draws.
- They don't connect to Rubin's framework at all.

## The key evidence

1. **Richard & Lippmann (1991)** proved that NN classifiers approximate Bayesian a posteriori
   probabilities. The equivalent theorem for NN *imputation* — proving convergence to
   Rubin-valid posterior predictive distributions P(X_mis | X_obs) — does not exist yet.

2. **Rey del Castillo (2012)** explicitly quotes Rubin (1996) saying RMSE/hit-rate is the
   wrong criterion for evaluating imputation, then shows ML beats MI on exactly that metric.
   This perfectly illustrates the tension: the field optimizes for the wrong thing.

3. **van Buuren (2018, §2.6)** mathematically shows that minimizing RMSE suppresses variance,
   leading to biased standard errors and invalid inference downstream.

## Why this matters

The "Rubin to SAITS" path has a missing bridge. Specifically:

```
Rubin (1976)  →  EM/MI  →  [MNAR theory: selection & pattern-mixture models]
                                          ↓
                              [tabular DL: not-MIWAE, PSMVAE, FragmGAN]
                                          ↓
                                    ??? NO BRIDGE ???
                                          ↓
                              [time-series DL: BRITS, SAITS, CSDI]
```

Nobody has:
- Proven that SAITS produces Rubin-valid imputations under specific missingness conditions
- Extended not-MIWAE or PSMVAE to temporal architectures
- Formally connected Rubin's ignorability conditions to attention-based time-series models

## What to look for in Gap 2 & 3 searches

The **one paper that would change this** would prove something like:
> "Under [specific missingness conditions], [specific time-series DL architecture]
> converges to the posterior predictive distribution P(X_mis | X_obs)."

If you find it → the bridge exists, and the review documents it.
If you don't find it (likely) → the missing bridge IS your key contribution.

**Either way you win.**

## How this shapes the writing

- **§6 (Evaluation):** The RMSE-vs-inference tension is a *symptom* of this missing bridge.
  Models optimize for a metric that Rubin (1996) and van Buuren (2018) explicitly say is wrong
  for imputation. Frame it that way.

- **§8 (Taxonomy):** When classifying methods, include a column or dimension for
  "theoretical validity under stated missingness mechanism." Most DL methods will be blank.

- **§9 (Open challenges):** This becomes a headline finding. Not "future work" — a gap the
  field needs to address. Phrase it as: "The theoretical conditions under which time-series
  DL imputation produces valid statistical inference remain unproven."

- **§1 (Introduction):** The abstract should promise this finding. Something like: "We identify
  a critical disconnect between the statistical theory of valid imputation and the empirical
  success of deep learning architectures for time-series data."
