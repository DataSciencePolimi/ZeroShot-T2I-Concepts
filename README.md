# 📊 Synthetic Concept Dataset for Concept-Based XAI

This repository provides a dataset of synthetic visual concepts generated using zero-shot Text-to-Image (T2I) models, designed to support research in concept-based Explainable Artificial Intelligence (XAI).

## 🧠 Motivation

Concept-based XAI methods aim to interpret deep learning models through human-understandable visual concepts (e.g., textures, object parts). However, these approaches typically rely on large, manually curated datasets, which limits scalability.

To address this, we explore the use of synthetic concept datasets generated via T2I models as a scalable alternative.

## 🗂️ Dataset Overview

The dataset contains:

- 🎨 Synthetic concept images generated from predefined textual prompts
- 🏷️ Concept-level organization (one folder per concept)
- 🔁 Multiple samples per concept to enable variability analysis
- ⚙️ Configurations reflecting different prompt and generation settings

Each concept is designed to approximate a human-interpretable visual feature, such as:

- textures (e.g., striped, dotted)
- object parts (e.g., wings, wheels)
- materials or patterns

## 🔬 Use Cases

This dataset is intended for:

- Evaluating concept-based XAI methods
- Studying representation similarity between synthetic and real concepts
- Testing intra-concept consistency across generated samples
- Supporting downstream explanation tasks
- Analyzing the effect of concept removal on model explanations

## 📈 Evaluation Protocols (from the paper)

The dataset supports four key analyses:

1. **Concept Representation Similarity** - Compare embeddings of synthetic vs. real concept images
2. **Intra-Concept Similarity** - Measure consistency across subsets of the same concept
3. **Downstream Explanation Performance** - Evaluate usefulness in explaining class predictions
4. **Concept Removal Impact** - Assess how removing a concept affects explanation behavior

### ⚠️ Limitations

While synthetic data offers scalability, this dataset highlights some challenges:

- ❗ Potential mismatch between synthetic and real-world concepts
- 🎭 Limited faithfulness of generated visual features
- 📉 Variability in usefulness for downstream XAI tasks
- 🤖 Biases introduced by the generative model

These limitations should be carefully considered when using synthetic data for interpretability.

## 🚀 Getting Started
```bash
git clone https://github.com/DataSciencePolimi/ZeroShot-T2I-Concepts.git
cd ZeroShot-T2I-Concepts
```

Explore the dataset structure and integrate it into your XAI pipelines.

## 📄 Citation

If you use this dataset, please cite:

```bibtex
@article{yourpaper202X,
  title={Synthetic Concepts for Concept-Based Explainable AI: Opportunities and Limitations},
  author={Author Names},
  journal={Conference/Journal Name},
  year={202X}
}
```

**Full author list (equal contribution noted):**  
Giacomo Astolfi*, Matteo Bianchi*, Riccardo Campi*, Antonio De Santis, Marco Brambilla

## 🤝 Contributions

Contributions, issues, and discussions are welcome!
Feel free to open a PR or start a discussion.
