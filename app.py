import streamlit as st
import cv2

import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

# Load your trained models
cnn_model = load_model('cnn_model.h5')
lstm_model = load_model('lstm_model.h5')
# capsule_model = load_model(r"C:\\Users\\101ri\\OneDrive\Desktop\deep fake detector\\Notebook\\capsule_model.h5")

# if os.path.exists(r"C:\\Users\\101ri\\OneDrive\Desktop\deep fake detector\\Notebook\\capsule_model.h5" and 'lstm_model.h5' and 'cnn_model.h5'):
#     print("Model file found!")
# else:
#     print("Model file not found! Please check the path.")




# Helper function to extract frames from the uploaded video
def extract_frames(video_path, output_folder, frame_rate=5):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_rate == 0:
            cv2.imwrite(os.path.join(output_folder, f"frame_{frame_count:04d}.jpg"), frame)
        frame_count += 1
    cap.release()

# Helper function to load images and preprocess them
def load_images_from_folder(folder, image_size=(128, 128)):
    images = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        img = load_img(img_path, target_size=image_size)
        img_array = img_to_array(img)
        images.append(img_array)
    return np.array(images)

# Streamlit UI
st.title("Deep Fake Video Detection System")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4"])
if uploaded_file is not None:
    # Save the uploaded video to a temporary file
    video_path = r"C:\\Users\\101ri\\OneDrive\Desktop\deep fake detector\\Notebook\\Celeb-synthesis\\id0_id1_0000.mp4"
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

    # Extract frames from the video
    frame_output_folder = "temp_frames"
    extract_frames(video_path, frame_output_folder)

    # Load and preprocess frames for prediction
    frames_array = load_images_from_folder(frame_output_folder)
    frames_array = frames_array / 255.0  # Normalize the images

    # Make predictions using each model
    cnn_prediction = cnn_model.predict(frames_array)
    lstm_prediction = lstm_model.predict(np.expand_dims(frames_array, axis=0))  # LSTM expects a sequence
    capsule_prediction = capsule_model.predict(frames_array)

    # Aggregate predictions (simple majority voting)
    cnn_result = np.mean(cnn_prediction) > 0.5
    lstm_result = np.mean(lstm_prediction) > 0.5
    capsule_result = np.mean(capsule_prediction) > 0.5

    final_result = (cnn_result + lstm_result + capsule_result) >= 2

    st.write("CNN Prediction:", "Deep Fake" if cnn_result else "Real")
    st.write("LSTM Prediction:", "Deep Fake" if lstm_result else "Real")
    st.write("Capsule Network Prediction:", "Deep Fake" if capsule_result else "Real")

    st.subheader("Final Verdict:")
    st.write("The video is a **Deep Fake**." if final_result else "The video is **Real**.")

    # Clean up temporary files
    os.remove(video_path)
    for filename in os.listdir(frame_output_folder):
        os.remove(os.path.join(frame_output_folder, filename))
    os.rmdir(frame_output_folder)
