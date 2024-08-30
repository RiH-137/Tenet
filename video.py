import streamlit as st
import cv2
import tempfile
import os
from PIL import Image
import numpy as np
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model('xception_deepfake_image.h5')

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

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

# Function to detect and crop face from image
def detect_and_crop_face(image):
    # Convert PIL image to OpenCV format
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) == 0:
        return None
    
    # Assume the first detected face is the target
    x, y, w, h = faces[0]
    cropped_face = img[y:y+h, x:x+w]
    
    # Convert back to PIL image
    return Image.fromarray(cropped_face)

# Function to extract frames from video
def extract_frames(video_path, interval=30):
    frames = []
    video = cv2.VideoCapture(video_path)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Initialize the progress bar
    progress_bar = st.progress(0)
    
    for i in range(0, frame_count, interval):
        video.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = video.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(Image.fromarray(frame))
        else:
            break
        # Update progress bar
        progress_bar.progress(int((i / frame_count) * 100))
    
    video.release()
    progress_bar.empty()
    return frames

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

# Sidebar for Chatbot
st.sidebar.title('Chatbot Support')
st.sidebar.write("Ask me anything related to deep fake detection, AI ethics, the legal use of AI, or how this project works!")
user_input = st.sidebar.text_input("You:", key="user_input")
if user_input:
    response = chatbot_response(user_input)
    st.sidebar.text_area("Chatbot:", value=response, height=150)

st.title('Video Deep Fake Detection')

# Upload video
uploaded_video = st.file_uploader("Choose a video...", type=["mp4", "avi", "mov"])

if uploaded_video is not None:
    # Save uploaded video temporarily
    temp_video = tempfile.NamedTemporaryFile(delete=False)
    temp_video.write(uploaded_video.read())
    temp_video.close()
    
    # Extract frames from the video
    st.write("Extracting frames from the video...")
    frames = extract_frames(temp_video.name)

    if frames:
        fake_count = 0
        real_count = 0

        st.write(f"Total frames extracted: {len(frames)}")
        # Display all extracted frames
        for i, frame in enumerate(frames):
            st.image(frame, caption=f'Frame {i+1}', use_column_width=True)
            face_image = detect_and_crop_face(frame)
            if face_image:
                prediction = predict(face_image)
                if prediction > 0.4:
                    fake_count += 1
                    st.write(f'Frame {i+1}: **DEEP FAKE**', color='red')
                else:
                    real_count += 1
                    st.write(f'Frame {i+1}: **Real Image**', color='green')
            else:
                st.write(f'Frame {i+1}: No face detected', color='orange')

        # Summary
        st.write(f"\nSummary:")
        st.write(f"Deep Fake Frames: {fake_count}", color='red')
        st.write(f"Real Frames: {real_count}", color='green')
        if fake_count > real_count:
            st.write("The video is likely to be a **DEEP FAKE**.", color='red')
        else:
            st.write("The video is likely to be a **Real Video**.", color='green')
    
    # Clean up the temporary file
    os.remove(temp_video.name)
