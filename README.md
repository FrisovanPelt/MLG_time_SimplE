# Temporal Analysis of SimplE on ICEWS14

## Summary

This repository contains an experimental study of the **SimplE** knowledge graph embedding model applied to the **ICEWS14** dataset under different temporal assumptions.

The project reproduces the original SimplE model in a **static setting** and evaluates a **minimal temporal extension** that conditions on timestamps **without allowing entity representations to evolve over time**.

The goal of this work is **not** to propose a new model, but to analyze how different temporal modeling choices affect performance, and to contrast these findings with the published results of **DE-SimplE**, a temporal extension of SimplE that introduces diachronic entity embeddings.

This codebase is largely based on the official SimplE implementation and retains the original training and evaluation pipeline with minimal modifications.

---

## Dependencies

The dependencies and setup closely follow the original SimplE implementation:

- **Python** 3.6+
- **NumPy** 1.15+
- **PyTorch** 1.0+

The code has been tested with more recent versions of PyTorch, though behavior may differ slightly due to changes in default serialization and optimization settings.

### Installation

A minimal setup using `pip`:

```bash
pip install numpy torch
```

Using a virtual environment is recommended.

---

## Project Structure and Datasets

The project supports two variants of the ICEWS14 dataset:

- **`ICEWS14_static`**  
  A static version of ICEWS14 obtained by removing the temporal component from all quadruples and deduplicating resulting triples.  
  This dataset is used to reproduce SimplE in its original static formulation.

- **`ICEWS14`**  
  The original temporal dataset, used for evaluating a minimal temporal extension of SimplE that conditions on timestamps while keeping entity and relation embeddings static.

All datasets are expected to be placed in the `datasets/` directory.

> **Note:** Dataset files are expected to follow the same format as in the original SimplE repository. ICEWS14 must be obtained separately and is not redistributed here.

---

## Temporal Modeling Assumptions

The minimal temporal extension evaluated in this repository:

- conditions scoring on timestamps
- **does not** introduce time-dependent entity embeddings
- **does not** modify the SimplE scoring function beyond timestamp conditioning

This design isolates the effect of temporal conditioning alone and allows direct comparison with DE-SimplE, which introduces diachronic entity representations.

---

## Usage

To run SimplE or its minimal temporal variant, the following parameters can be specified:

- `ne`: number of training epochs  
- `lr`: learning rate  
- `reg`: L2 regularization parameter  
- `dataset`: dataset name  
- `emb_dim`: embedding dimension  
- `neg_ratio`: number of negative samples per positive example  
- `batch_size`: batch size  
- `save_each`: validation frequency (in epochs)

Example usage:

```bash
python main.py \
  -ne <ne> \
  -lr <lr> \
  -reg <reg> \
  -dataset <dataset> \
  -emb_dim <emb_dim> \
  -neg_ratio <neg_ratio> \
  -batch_size <batch_size> \
  -save_each <save_each>
```

---

## Evaluation and Results

Models are evaluated using the same metrics and evaluation protocol as the original SimplE implementation.  
Validation and test results are logged during training and saved according to the specified validation frequency.

Published DE-SimplE results are used for comparison and are **not** reproduced in this repository.

---

## Relation to Prior Work

This project is based on and inspired by the following works:

### SimplE
Kazemi and Poole introduced **SimplE** as a simple yet expressive model for static knowledge graph completion.

- **Official repository:**  
  https://github.com/Mehran-k/SimplE

### DE-SimplE
Goel et al. proposed **DE-SimplE**, a temporal extension of SimplE that models diachronic entity embeddings.

- **Official repository:**  
  https://github.com/BorealisAI/de-simple

This repository does **not** reimplement DE-SimplE. Instead, published DE-SimplE results are used for comparison in order to analyze which temporal inductive biases are necessary for strong performance on **ICEWS14**.

---

## Limitations

- This work does not explore alternative temporal embedding schemes beyond timestamp conditioning.
- Results depend on the original SimplE training pipeline and hyperparameter choices.
- Differences from published DE-SimplE results may arise due to dataset preprocessing and evaluation protocol differences.

---

## Citation

If you use this code or analysis in academic work, please cite the original SimplE and DE-SimplE papers.

---

## License

This repository follows the license of the original SimplE implementation unless stated otherwise.
