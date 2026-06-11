---
title: "AI Explainability: From SHAP to Mechanistic Interpretability"
author: "Your Name"
date: "2026-06-11"
description: "A tour of XAI methods — from black-box attribution to circuit tracing inside LLMs."
fonts:
  heading: "Rubik"
  body: "Poppins"
bibliography: false
footer:
  left: "AI Explainability"
  center: ""
  right: "{n}/{N}"
custom_css: |
  .slide--section-break { background: #1B3A6B; }
  :root { --colloquium-progress-fill: #1B3A6B; }
---

<!-- layout: title-sidebar -->

# AI Explainability

From SHAP to Mechanistic Interpretability

---

<!-- layout: section-break -->

# The Explainability Landscape

---

<!-- columns: 45/55 -->

- **Transparency**
- **XAI (Explainable AI)**
- **Mechanistic Interpretability**

|||

**Transparency** — models designed to be interpretable by construction (decision trees, linear regression).

**XAI** — post-hoc methods that explain black-box models: SHAP, LIME, saliency maps.

**Mechanistic Interpretability** — reverse-engineering learned representations and circuits inside neural networks.

---

## Explainability vs Mechanistic Interpretability

| | Explainability (XAI) | Mechanistic Interpretability |
|---|---|---|
| **Question** | Which inputs drove this output? | What algorithm did the model learn? |
| **Approach** | Attribution / perturbation | Circuit tracing, probing, activation patching |
| **Unit of Analysis** | Feature importance scores | Neurons, attention heads, circuits |
| **Output** | Human-readable explanation | Mechanistic understanding |

---

## The Key Difference

```box
tone: accent
```

XAI tells you *what* the model paid attention to.
Mechanistic interpretability tells you *how* the model computed the answer —
the internal algorithm, not just the input correlation.

```

---

## KernelSHAP on Audio (CLAP)

```python
import shap
import numpy as np

# CLAP: Contrastive Language-Audio Pretraining
def clap_similarity(audio_segments):
    """Return cosine similarity between audio and a text prompt."""
    audio_embeddings = clap_model.get_audio_embedding(audio_segments)
    text_embedding = clap_model.get_text_embedding(["dog barking"])
    return cosine_similarity(audio_embeddings, text_embedding)

# Build a KernelSHAP explainer over audio segments
background = np.zeros((1, n_segments))
explainer = shap.KernelExplainer(clap_similarity, background)

shap_values = explainer.shap_values(audio_mask, nsamples=100)
shap.plots.bar(shap_values)
```

---

<!-- rows: 35/65 -->

> "The goal is not to make AI explainable — it is to make AI *understandable*."

===

<!-- row-columns: 50/50 -->

**Use SHAP when:**
- You need a quick, model-agnostic explanation
- Stakeholders require feature importance scores
- Debugging a production model's single prediction
- Regulatory compliance requires attribution

|||

**Use Mech. Interp when:**
- You want to understand *what* the model learned
- Investigating emergent capabilities or failures
- Safety research: finding deceptive circuits
- Building trust through mechanistic guarantees

---

## Summary

- **XAI methods** like SHAP give fast, actionable explanations — valuable for deployment and compliance, but they describe correlations, not mechanisms.

- **Mechanistic interpretability** opens the black box at the algorithmic level — slower and harder, but the only path to deep trust in AI systems.

- **Both approaches are complementary**: use XAI for day-to-day explanations, mechanistic interpretability for auditing critical systems and frontier models.
