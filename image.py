import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import cv2

# Set page configuration with title and icon
st.set_page_config(page_title="Deep Fake Detector Tool", page_icon="🕵️‍♂️")

# Add a banner
st.markdown("""
    <style>
        .banner {
            background-color: #f8f9fa;
            padding: 10px;
            text-align: center;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .banner h1 {
            color: #343a40;
            margin: 0;
        }
    </style>
    <div class="banner">
        <h1>Deep Fake Detector Tool</h1>
    </div>
""", unsafe_allow_html=True)

# Load the trained model
model = tf.keras.models.load_model('xception_deepfake_image.h5')

# Function to preprocess the image
def preprocess_image(image):
    image = image.resize((299, 299))  # Resize the image to match the input size expected by the model
    image = np.array(image)
    image = image.astype('float32') / 255.0  # Normalize the image to [0, 1]
    image = np.expand_dims(image, axis=0)  # Add a batch dimension
    return image

# Function to predict if an image is deep fake or real
def predict(image):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    return prediction[0][0]  # Return the probability

# Chatbot functionality with extended topics and guidance
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input:
        return "Hi there! How can I assist you today?"
    
    elif "deep fake" in user_input:
        return "Deep fakes are AI-generated media that can manipulate real video or audio to mislead viewers. I can help you detect them in images or videos."
    
    elif "ethics" in user_input:
        return ("The ethics of AI involve concerns about privacy, fairness, transparency, and accountability. "
                "For example, using deep fake technology to deceive or harm others is unethical and can have serious consequences.")
    
    elif "legal" in user_input:
        return ("The legal use of AI is a complex area. It's essential to ensure AI is used in a way that complies with existing laws, "
                "such as data protection, intellectual property rights, and avoiding harm to individuals or society.")
    
    elif "false information" in user_input or "misinformation" in user_input:
        return ("Deep fake videos can be used to spread false information, leading to significant harm. "
                "It's crucial to develop tools and regulations to combat this misuse of technology.")
    
    elif "how to upload" in user_input:
        return ("To upload an image or video, simply click on the 'Choose an image...' or 'Choose a video...' button depending on your selection. "
                "You can upload images in jpg, jpeg, or png formats, and videos in mp4, avi, or mov formats.")
    
    elif "size of video" in user_input or "size of image" in user_input:
        return ("The recommended image size is under 10MB, and videos should be under 100MB to ensure smooth processing. "
                "Larger files may take longer to process and could result in timeouts.")
    
    elif "how this project works" in user_input or "how does this work" in user_input:
        return ("This project detects deep fake images and videos using a machine learning model trained on the Xception network. "
                "For images, the uploaded image is preprocessed and passed through the model to predict whether it is real or fake. "
                "For videos, the video is split into frames, and each frame is analyzed individually. A summary of the results is provided based on the analysis of all frames.")
    
    elif "goodbye" in user_input or "bye" in user_input:
        return "Goodbye! If you have more questions in the future, feel free to ask."
    
    else:
        return "I'm not sure how to respond to that. Could you ask something else?"

# Streamlit app layout

if st.button('Go to Google'):
    st.write("[Click here to go to Google](https://www.google.com)")

# Sidebar for Chatbot
st.sidebar.title('Chatbot Support')
st.sidebar.write("Ask me anything related to deep fake detection, AI ethics, the legal use of AI, or how this project works!")
user_input = st.sidebar.text_input("You:", key="user_input")
if user_input:
    response = chatbot_response(user_input)
    st.sidebar.text_area("Chatbot:", value=response, height=150)

st.write('Upload an image to check whether it is a deep fake or not.')

# Upload image
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Predict if the image is a deep fake
    prediction = predict(image)
    if prediction > 0.4:
        st.write('The image is a **DEEP FAKE**.', color='red')
    else:
        st.write('The image is a **Real Image**.', color='green')
