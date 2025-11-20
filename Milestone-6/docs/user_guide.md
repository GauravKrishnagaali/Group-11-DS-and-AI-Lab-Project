
#  User Guide – Microstructure Classifier App

## 1. What the App Does
This app classifies steel microstructure images into:
Austenite, Bainite, Ferrite, Martensite, Pearlite.

It uses a deep-learning model trained using VGG19/ResNet50.

---

## 2. How to Use the App

### Step 1 — Launch the App
``` streamlit run app.py ```

### Step 2 — Upload the Model

- Use the sidebar to upload your trained `.h5` model:

- You will see a success message: Model loaded successfully! 

### Step 3 — Configure Class Names (Optional)

- Enter the five class names:

``` Austenite, Bainite, Ferrite, Martensite, Pearlite ```

- Click **Update Class Names**.

### Step 4 — Upload Image
- Upload a JPG/PNG micrograph image.

### Step 5 — Get Prediction
The app shows:
- Predicted Phase  
- Confidence score  
- Probability bar chart  
- Optional CSV download  

---

## 3. Troubleshooting

| Problem | Solution |
|--------|----------|
| Wrong prediction | Check correct input size (224×224) |
| Cannot load model | Ensure `.h5` is compatible with TensorFlow |
| Black/white images predicted wrongly | Switch “Color Mode” to RGB |
| App freezes | Restart Streamlit session |

---

## 4. Example Interaction
1. User uploads model  
2. User uploads micrograph  
3. App returns:  
Predicted Phase: Pearlite
Confidence: 0.84


---

## 5. Screenshots 
- Upload screen
  <img width="1908" height="876" alt="image" src="https://github.com/user-attachments/assets/6f1d3349-27ea-4228-a1a1-199fda13cf18" />
 
- Prediction screen & Probability chart
  <img width="1910" height="2062" alt="screencapture-group-11-ds-ai-project-streamlit-app-2025-11-18-18_02_01" src="https://github.com/user-attachments/assets/ae313683-1141-45ca-b9bb-8295228b3284" />
