# 📊 Synthetic Concept Dataset for Concept-Based XAI

This repository provides a dataset of synthetic visual concepts generated using zero-shot Text-to-Image (T2I) models, designed to support research in concept-based Explainable Artificial Intelligence (XAI).

## 🧠 Motivation

Concept-based XAI methods aim to interpret deep learning models through human-understandable visual concepts (e.g., textures, object parts). However, these approaches typically rely on large, manually curated datasets, which limits scalability.

To address this, we explore the use of synthetic concept datasets generated via T2I models as a scalable alternative.

## 📥 Download

```bash
git clone https://github.com/DataSciencePolimi/ZeroShot-T2I-Concepts.git
cd ZeroShot-T2I-Concepts
```

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

## Project Tree

Below is a visual outline of the dataset’s directory structure.  
The root of the repository is `concepts/`.  
After the helper script `analysis.py`, every *concept* is represented by its own directory.  
Each concept folder follows a consistent naming convention:

| suffix | meaning |
|--------|---------|
| `_flux`  | a *flushed* version (contrast‑adjusted) |
| `_gpti1` | a *Gaussian‑processed* variant (first pass) |
| `_sd35`  | a *size‑downscaled* 35‑pixel version |
| (no suffix) | the original, full‑resolution image |

Below is a representative subset (the full tree contains **~350** concept folders).  
Feel free to expand any of the directories locally – the structure is identical across all concepts.

```text
concept_images_jpg/
├── analysis.py
├── asparagus/
│   ├── asparagus
│   ├── asparagus_flux
│   ├── asparagus_gpti1
│   └── asparagus_sd35
├── bubbly/
│   ├── bubbly
│   ├── bubbly_flux
│   ├── bubbly_gpti1
│   └── bubbly_sd35
├── cast_iron/
│   ├── cast_iron
│   ├── cast_iron_flux
│   ├── cast_iron_gpti1
│   └── cast_iron_sd35
├── crystalline/
│   ├── crystalline
│   ├── crystalline_flux
│   ├── crystalline_gpti1
│   └── crystalline_sd35
├── diced/
│   ├── diced
│   ├── diced_flux
│   ├── diced_gpti1
│   └── diced_sd35
├── fin/
│   ├── fin
│   ├── fin_flux
│   ├── fin_gpti1
│   └── fin_sd35
├── glass/
│   ├── glass
│   ├── glass_flux
│   ├── glass_gpti1
│   └── glass_sd35
├── guitarist/
│   ├── guitarist
│   ├── guitarist_flux
│   ├── guitarist_gpti1
│   └── guitarist_sd35
├── leather/
│   ├── leather
│   ├── leather_flux
│   ├── leather_gpti1
│   └── leather_sd35
├── lichen/
│   ├── lichen
│   ├── lichen_flux
│   ├── lichen_gpti1
│   └── lichen_sd35
│
├── ...  (the remaining 300+ concept folders follow the same pattern)
```

> **Tip:**  
> If you’re only interested in a subset of concepts, you can copy only those directories locally with `rsync`, `scp`, or a simple `cp -r`.  
> The naming convention makes it trivial to filter by variant (`*_flux`, `*_gpti1`, `*_sd35`) using shell globs or a `find` command.

---

### Quick sanity check

After downloading or cloning the repo, you can run the bundled script to confirm that the directory structure is intact:

```bash
python analysis.py --verify
```

It will walk the tree and report any missing or mis‑named files.  

Happy exploring!

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
