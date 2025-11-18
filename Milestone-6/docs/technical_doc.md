#  Technical Documentation – Milestone 6

## 1. Environment Setup

### Python Version
Python **3.10+**

### Install Requirements

pip install -r requirements.txt


### Dependencies
``` tensorflow
keras
numpy
pandas
scikit-learn
pillow
streamlit
pickle5
matplotlib
```


---

## 2. Data Pipeline

### Dataset Classes
- Austenite
- Bainite
- Ferrite
- Martensite
- Pearlite

### Preprocessing
- Resize → 224×224
- Normalize → `/255.0`
- Augmentation:
  - flips
  - zoom
  - brightness jitter
  - shifts

### Split
train: 80%
test: 20%


---

## 3. Model Architecture

### Base Models
- **VGG19**
- **ResNet50**
Both loaded with ImageNet pretrained weights (`include_top=False`).

### Custom Classifier Head
Flatten
Dense(256, ReLU)
Dropout(p)
Dense(5, softmax)


---

## 4. Training Summary

- Loss: `categorical_crossentropy`
- Regularization :  L2 kernel regularization
- Best Hyperparameters:
  - LR: 0.001
  - Dropout: 0.1
- Early stopping applied : with a patience of 10 epochs
- Best validation: **~0.85 accuracy** 

---

## 5. Evaluation Summary (Milestone 5)

### Metrics 

<img width="782" height="241" alt="image" src="https://github.com/user-attachments/assets/fc969d07-fd43-43b7-b3f4-b83877ad0cfb" />

---

## 6. Inference Pipeline
Deployed Streamlit app uses the following steps:
```
Upload model (.h5)
↓
Load with custom Flatten layer
↓
Upload image → preprocess → resize + normalize
↓
model.predict()
↓
Softmax → probability distribution
↓
Display predicted class + bars
```

Pseudo-code:

```python
img = load_image(path)
img = preprocess(img)
pred = model.predict(img)
class_id = np.argmax(pred)
```

## 7. Deployment Details
Deployment Platform — Streamlit App

File:

```app.py```

Features:

- Upload any .h5 model

- Custom class names

- Image preprocessing controls

- Probability bar chart

- Download prediction results

- Model summary viewer

- Run the app
``` streamlit run app.py```

## 8. System Design Considerations

Modular → model, preprocessing, prediction split

Reproducible →  logs, saved weights

Extensible → supports any image classifier

Robust → handles grayscale, RGB, errors gracefully

## 9. Error Handling & Monitoring

App handles:

- Wrong file type

- Invalid model structure

- Empty class list

- Prediction failures
