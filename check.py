import os

if os.path.exists('capsule_model.h5'):
    print("Model file found!")
    
else:
    print("Model file not found! Please check the path.")
