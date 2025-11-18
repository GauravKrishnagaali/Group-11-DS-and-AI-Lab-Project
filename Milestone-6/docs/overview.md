# Project Overview – Milestone 6 (Deployment & Documentation)

## 1. Project Title
**Automatic Classification of Steel Microstructures
Using Deep Learning**

## 2. Objective
This project builds an AI system that classifies steel microstructure images into five phases:
- Austenite
- Bainite
- Ferrite
- Martensite
- Pearlite

Using VGG19 and ResNet50 with fine-tuned transfer learning, the model predicts microstructure phases with significant accuracy and deploys through a user-friendly Streamlit interface.

---

## 3. Architecture Summary
Below is the high-level architecture covering data flow, training, and deployment.

       ┌──────────────┐
       │  Input Image  │
       └───────┬──────┘
               │
    ┌──────────▼──────────┐
    │ Preprocessing Layer  │
    │ (resize, normalize)  │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ Trained Model       │
    | Softmax (5 classes) │
    └──────────┬──────────┘
               │
      ┌────────▼────────┐
      │ Probability Dist │
      └────────┬────────┘
               │
       ┌───────▼───────┐
       │ Final Class    │
       └───────────────┘


---

## 4. Deployment Components
App includes:
###  Streamlit App (final deployment)
- Model upload (`.h5`)
- Custom class naming
- Image upload
- Prediction with confidence bar
- CSV result export
- Model summary viewer
---

## 5. Folder Structure (Recommended)
```
Milestone 6/
│
└── app.py # Streamlit deployment
│
├── docs/
│ ├── overview.md
│ ├── technical_doc.md
│ ├── user_guide.md
│ ├── api_doc.md
│ └── licenses.md
│
├── requirements.txt
└── README.md
```


---

## 6. Deliverables Included
 Deployment (Streamlit App)  
 Technical Documentation  
 User Guide  
 Final Project Report-ready content


