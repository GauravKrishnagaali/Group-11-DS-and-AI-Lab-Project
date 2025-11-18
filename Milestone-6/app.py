import streamlit as st
import numpy as np
from PIL import Image
from keras.models import load_model
from keras.layers import Flatten
import tempfile
import os

# Custom Flatten layer
class CustomFlatten(Flatten):
    def call(self, inputs):
        if isinstance(inputs, list):
            inputs = inputs[0]
        return super().call(inputs)
    
    def compute_output_spec(self, inputs):
        if isinstance(inputs, list):
            inputs = inputs[0]
        return super().compute_output_spec(inputs)

# Page configuration
st.set_page_config(
    page_title="Image Classification App",
    page_icon="🖼️",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stAlert {
        margin-top: 1rem;
    }
    .upload-text {
        text-align: center;
        color: #666;
        padding: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🖼️ Image Classification with Deep Learning")
st.markdown("---")

# Initialize session state
if 'model' not in st.session_state:
    st.session_state.model = None
if 'model_loaded' not in st.session_state:
    st.session_state.model_loaded = False
if 'class_names' not in st.session_state:
    st.session_state.class_names = ['Class 0', 'Class 1', 'Class 2', 'Class 3', 'Class 4']

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Model upload section
    st.subheader("1. Upload Model")
    model_file = st.file_uploader(
        "Upload your trained model (.h5 file)",
        type=['h5', 'hdf5'],
        help="Upload your Keras model file"
    )
    
    if model_file is not None:
        if not st.session_state.model_loaded:
            with st.spinner("Loading model..."):
                try:
                    # Save uploaded file temporarily
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.h5') as tmp_file:
                        tmp_file.write(model_file.read())
                        tmp_path = tmp_file.name
                    
                    # Load the model
                    st.session_state.model = load_model(
                        tmp_path,
                        custom_objects={'Flatten': CustomFlatten},
                        compile=False
                    )
                    st.session_state.model_loaded = True
                    
                    # Clean up temp file
                    os.unlink(tmp_path)
                    
                    st.success("✅ Model loaded successfully!")
                    
                    # Display model info
                    st.info(f"""
                    **Model Info:**
                    - Input Shape: {st.session_state.model.input_shape}
                    - Output Shape: {st.session_state.model.output_shape}
                    - Total Params: {st.session_state.model.count_params():,}
                    """)
                    
                    # Display model summary
                    with st.expander("📋 View Model Summary", expanded=False):
                        # Capture model.summary() output
                        from io import StringIO
                        import sys
                        
                        # Redirect stdout to capture summary
                        old_stdout = sys.stdout
                        sys.stdout = StringIO()
                        
                        st.session_state.model.summary()
                        summary_string = sys.stdout.getvalue()
                        
                        # Restore stdout
                        sys.stdout = old_stdout
                        
                        # Display in code block
                        st.code(summary_string, language='text')
                    
                except Exception as e:
                    st.error(f"❌ Error loading model: {str(e)}")
                    st.session_state.model_loaded = False
        else:
            st.success("✅ Model is loaded!")
    
    st.markdown("---")
    
    # Class names configuration
    st.subheader("2. Configure Classes")
    num_classes = st.number_input(
        "Number of classes",
        min_value=2,
        max_value=100,
        value=5,
        help="Enter the number of classes in your model"
    )
    
    # Dynamic class name inputs
    class_names = []
    with st.expander("Edit Class Names", expanded=False):
        for i in range(num_classes):
            class_name = st.text_input(
                f"Class {i}",
                value=st.session_state.class_names[i] if i < len(st.session_state.class_names) else f"Class {i}",
                key=f"class_{i}"
            )
            class_names.append(class_name)
    
    if st.button("Update Class Names"):
        st.session_state.class_names = class_names
        st.success("Class names updated!")
    
    st.markdown("---")
    
    # Model settings
    st.subheader("3. Image Settings")
    img_size = st.selectbox(
        "Input Image Size",
        [128, 224, 256, 299],
        index=0,
        help="Select the input size your model expects"
    )
    
    color_mode = st.selectbox(
        "Color Mode",
        ["Grayscale", "RGB"],
        index=0,
        help="Select the color mode your model expects"
    )

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📤 Upload Image")
    
    if not st.session_state.model_loaded:
        st.warning("⚠️ Please upload a model first in the sidebar!")
    
    uploaded_image = st.file_uploader(
        "Choose an image to classify",
        type=['jpg', 'jpeg', 'png', 'bmp'],
        help="Upload an image file for classification",
        disabled=not st.session_state.model_loaded
    )
    
    if uploaded_image is not None:
        # Display uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Image info
        st.info(f"""
        **Image Info:**
        - Size: {image.size[0]} x {image.size[1]} pixels
        - Mode: {image.mode}
        - Format: {image.format}
        """)

with col2:
    st.subheader("🎯 Prediction Results")
    
    if uploaded_image is not None and st.session_state.model_loaded:
        
        # Preprocess image function
        def preprocess_image(img, target_size, mode):
            # Convert to appropriate color mode
            if mode == "Grayscale":
                img = img.convert('L')
            else:
                img = img.convert('RGB')
            
            # Resize
            img = img.resize((target_size, target_size))
            
            # Convert to array
            img_array = np.array(img)
            
            # Add channel dimension for grayscale
            if mode == "Grayscale" and len(img_array.shape) == 2:
                img_array = np.expand_dims(img_array, axis=-1)
            
            # Add batch dimension
            img_array = np.expand_dims(img_array, axis=0)
            
            # Normalize
            img_array = img_array / 255.0
            
            return img_array
        
        # Make prediction
        try:
            with st.spinner("🔄 Analyzing image..."):
                # Preprocess
                processed_img = preprocess_image(image, img_size, color_mode)
                
                # Predict
                predictions = st.session_state.model.predict(processed_img, verbose=0)
                predicted_class_idx = np.argmax(predictions)
                confidence = predictions[0][predicted_class_idx]
                
                # Display main prediction
                st.success("✅ Prediction Complete!")
                
                st.markdown(f"""
                <div style='text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px; margin: 10px 0;'>
                    <h2 style='color: #1f77b4; margin: 0;'>{st.session_state.class_names[predicted_class_idx]}</h2>
                    <p style='font-size: 24px; color: #666; margin: 10px 0;'>Confidence: {confidence:.2%}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Display all predictions
                st.markdown("### 📊 All Class Probabilities")
                
                # Create dataframe for better visualization
                import pandas as pd
                
                pred_data = []
                for i in range(len(st.session_state.class_names)):
                    pred_data.append({
                        'Class': st.session_state.class_names[i],
                        'Probability': predictions[0][i]
                    })
                
                df = pd.DataFrame(pred_data)
                df = df.sort_values('Probability', ascending=False)
                
                # Display with progress bars
                for idx, row in df.iterrows():
                    col_name, col_bar = st.columns([1, 3])
                    with col_name:
                        st.write(f"**{row['Class']}**")
                    with col_bar:
                        st.progress(float(row['Probability']), text=f"{row['Probability']:.2%}")
                
                # Download predictions
                st.markdown("---")
                st.download_button(
                    label="📥 Download Predictions (CSV)",
                    data=df.to_csv(index=False),
                    file_name="predictions.csv",
                    mime="text/csv"
                )
                
        except Exception as e:
            st.error(f"❌ Error during prediction: {str(e)}")
            st.exception(e)
    
    elif not st.session_state.model_loaded:
        st.info("👈 Upload a model in the sidebar to start!")
    else:
        st.info("👈 Upload an image to get predictions!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>Built with ❤️ from Group 11</p>
    <p style='font-size: 12px;'>Upload your model and images to get started!</p>
</div>
""", unsafe_allow_html=True)

# Help section in expander
with st.expander("ℹ️ How to Use This App"):
    st.markdown("""
    ### Quick Start Guide
    
    1. **Upload Your Model** (Sidebar)
       - Click on "Upload your trained model"
       - Select your `.h5` or `.hdf5` model file
       - Wait for the model to load
    
    2. **Configure Classes** (Sidebar)
       - Set the number of classes
       - Edit class names if needed
       - Click "Update Class Names"
    
    3. **Adjust Settings** (Sidebar)
       - Select the correct input image size
       - Choose the color mode (Grayscale or RGB)
    
    4. **Upload & Classify** (Main Area)
       - Upload an image file
       - View the prediction results
       - Download predictions as CSV
    
    ### Troubleshooting
    
    - **Model won't load?** Make sure it's a valid Keras `.h5` file
    - **Wrong predictions?** Check your image size and color mode settings
    - **Error during inference?** Ensure the image format matches your model's training data
    
    ### Supported Formats
    
    - **Models:** `.h5`, `.hdf5`
    - **Images:** `.jpg`, `.jpeg`, `.png`, `.bmp`
    """)