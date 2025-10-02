# Pleural-effusion segmentation using AI

This repository contains scripts and notebooks for **Pleural-effusion segmentation** using a modified version of **nnU-Net** from **ce-CT** data. 

The project includes:  

- `nnUNet.py` – Core implementation and training script for nnU-Net model.  
- `prepross.ipynb` – Jupyter notebook for preprocessing the  **ce-CT** data (normalization, resizing, formatting for nnU-Net).  

---

## 📌 Requirements

Make sure you have the following installed:  

- Python 3.8+  
- PyTorch >= 1.10  
- NumPy  
- nibabel (for NIfTI medical images)  
- scikit-learn  
- matplotlib  

Install dependencies:  

```bash
pip install -r requirements.txt
```

*(create a `requirements.txt` with your exact package list if needed)*

---

## ⚙️ Usage

### 1. Preprocessing
Use the notebook `prepross.ipynb` to preprocess medical imaging data before training:  
- Normalization  
- Resampling / resizing  
- Saving in nnU-Net compatible format  

### 2. Training the Model
Run the nnU-Net training script:  

```bash
python nnUNet.py --data_dir <path_to_preprocessed_data> --output_dir <path_to_results>
```

Options:  
- `--epochs` : number of training epochs (default: 100)  
- `--batch_size` : batch size for training (default: 2)  
- `--lr` : learning rate (default: 1e-4)  

### 3. Inference
Once trained, you can run inference on new medical scans:  

```bash
python nnUNet.py --mode predict --input <path_to_image> --model <path_to_trained_model>
```

---

## 📂 Project Structure

```
├── nnUNet.py          # nnU-Net training & inference script
├── prepross.ipynb     # Preprocessing notebook
├── requirements.txt   # (to be created) list of dependencies
└── README.md          # Project documentation
```

---

## References
- [nnU-Net: Self-adapting Framework for U-Net-based Medical Image Segmentation](https://arxiv.org/abs/1809.10486)  

