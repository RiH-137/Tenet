import React from 'react';
import './App.css';

function App() {
  return (
    <><div className="App">
    {/* Video background */}
    <div className="video-background">
      <video autoPlay loop muted>
        <source src="background.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>

    {/* Content over the video */}
    <header className="navigation">
      <nav>
        <ul>
          <li><a href="#home">Home |</a></li>
          <li><a href="#key-benefits">Key Benefits |</a></li>
          <li><a href="#visual-demo">Visual Demo |</a></li>
          <li><a href="#about">About |</a></li>
          <li><a href="#contact">Contact Us</a></li>
        </ul>
      </nav>
    </header>
    <div className="div">
      <h1>Instant Face detection with cutting edge AI</h1>
      <br />
      <h3>"Instant Recognition, Effortless Integration."</h3>
      <br />
      <p id='para'>Experience the future of security with instant face detection powered by cutting-edge AI. Our technology delivers accurate and real-time recognition, ensuring seamless and secure operations. Simplify your processes with effortless integration into any system.</p>
     <br />
     <button class="glow-on-hover" type="button">Try Now</button>
      </div>
   </div>
   <div className="features">
    <h1 id='feat'>Key Features: Deep Face Detection</h1>
    <br />
    <br />
    <div className="div1">
      <div className="text">
        <h2 id='feature'>Accurate Detection</h2>
<p id='featuredescription'> Accurate detection in facial recognition systems refers to the ability to identify and verify facial features with a high degree of precision. This technology uses sophisticated algorithms to analyze facial landmarks, patterns, and unique identifiers, ensuring that each face is recognized correctly, even in complex scenarios such as varying lighting conditions,
   different angles, and partial obstructions. Accurate detection minimizes false positives and negatives, 
   enhancing security, efficiency, and reliability in applications like surveillance, access control, and identity
    verification. It is essential for environments where precision is critical, providing confidence that every face is identified
     with exceptional accuracy.Accurate detection in deep face detection systems is crucial for many applications, from security to user experience enhancements. Here’s how modern deep learning techniques achieve high accuracy in face detection:

Advanced Architectures: State-of-the-art face detection models use advanced neural network architectures like Multi-task Cascaded Convolutional Networks (MTCNN), Single Shot MultiBox Detector (SSD), and YOLO (You Only Look Once). These models are designed to handle complex patterns and variations in face appearance with high precision.

Large and Diverse Datasets: High accuracy is achieved through training on large and diverse datasets that include a wide range of facial images. Datasets like the Wider Face, LFW (Labeled Faces in the Wild), and VGGFace provide extensive and varied samples, helping the model generalize better to different conditions.

</p>  </div>
      <div className="img"><img id='feature1' src="download (1).png" alt="img" /></div>
    </div>


    <div className="div1">
      
      <div className="img"><img id='feature2' src="download.png" alt="" /></div>
      <div className="text">
        <h2 id='feature'>Real Time Processing</h2>
<p id='featuredescription'>Real-time processing in deep face detection focuses on the ability to detect and 
  analyze faces in images or video streams with minimal latency, enabling immediate responses. This capability is crucial for applications
   like live surveillance and interactive user interfaces. Achieving real-time performance involves using efficient algorithms, such as 
   lightweight neural network models (e.g., MobileNet or Tiny-YOLO) designed for speed, and leveraging hardware acceleration with
    GPUs or specialized chips like TPUs and FPGAs. Optimization techniques, including quantization
     and pruning, help reduce computational demands while maintaining accuracy. Software frameworks like TensorFlow Lite and ONNX Runtime are optimized for fast inference on various hardware platforms. Efficient data handling, including batch processing and low-latency data transmission, further ensures that frames are processed promptly. Real-time post-processing techniques, such as object tracking and dynamic adjustment of detection parameters, contribute to maintaining performance. Edge computing allows for on-device processing, eliminating delays associated with data transmission to remote servers. Together, these strategies enable real-time face detection across
   diverse applications, from security and surveillance to augmented reality and interactive systems.</p>  </div>
    </div>


    <div className="div1">
      <div className="text">
        <h2 id='feature'>Robustness To Variability</h2>
<p id='featuredescription'>Robustness to variability in deep face detection models means they can effectively handle a wide range of differences in facial appearance, such as changes in expression, age, and ethnicity. This capability is achieved through diverse training on extensive datasets that capture a variety of faces, including different ages, ethnic backgrounds, and expressions. Data augmentation techniques during training, like rotation and scaling, help simulate these variations. Advanced model architectures, such as CNNs and transformers, are designed to recognize and adapt to subtle differences in facial features. Additionally, multi-scale and multi-angle detection allows models to handle different poses and distances. Regularization techniques prevent overfitting to specific features, while transfer learning from pre-trained models helps adapt to new variations with less additional training. Finally, face landmark detection aids in aligning and normalizing faces, improving recognition across varying conditions. These strategies collectively ensure that deep face detection models remain accurate and reliable despite significant variability in facial appearances.</p>  </div>
      <div className="img"><img id='feature1' src="download (2).png" alt="" /></div>
    </div>



    </div>
    <div className="guide">
    <h1 id='guide1'>Basic Guide: How It Works?</h1>
    <br />
    <br />
    
      <p id='g'>1.Login:

Access the platform and initiate the login process by connecting your MetaMask wallet. Ensure that your wallet is properly configured and contains the necessary funds for transaction fees.</p>
<br />
<p id='g'>2. Validation:

Once connected, the platform will validate your MetaMask wallet. This step ensures secure access and confirms your eligibility to use the services provided.</p>
<br /><p id='g'>3. Upload Video:

After successful validation, you will be prompted to upload a video. Select the video file from your device that you wish to process.</p>
<br /><p id='g'>4. Payment:

To proceed with video processing, a fee is required. Follow the on-screen instructions to make the payment using the supported cryptocurrency. The payment will cover the cost of processing and generating the final output.</p>
<br /><p id='g'>5. View Results:

Upon successful payment, the platform will process your video and generate the final output. You will receive access to view the results once the processing is complete.
</p>
<br />
<br />

<button class="glow-on-hover1" type="button">Upload Here</button>

    </div>
    <div className="foter">

    </div>

   
      
    <footer>
        <div class="footer-container">
            <div class="footer-about">
                <h3>About Us</h3>
                <p>Discover our mission to revolutionize face detection technology with advanced solutions tailored for accuracy and efficiency. Learn more about our team and our commitment to innovation.</p>
            </div>
            <div class="footer-services">
                <h3>Services</h3>
                <ul>
                    <li><a href="#">Face Detection Solutions</a></li>
                    <li><a href="#">Custom Integrations</a></li>
                    <li><a href="#">Consultation & Support</a></li>
                </ul>
            </div>
            <div class="footer-resources">
                <h3>Resources</h3>
                <ul>
                    <li><a href="#">Blog</a></li>
                    <li><a href="#">FAQ</a></li>
                    <li><a href="#">Case Studies</a></li>
                    <li><a href="#">Documentation</a></li>
                </ul>
            </div>
            <div class="footer-contact">
                <h3>Contact Us</h3>
                <p>Email: <a href="mailto:support@facedetection.com">support@facedetection.com</a></p>
                <p>Phone: +1 (123) 456-7890</p>
                <p>Address: 1234 Innovation Drive, Tech City, CA 98765, USA</p>
            </div>
            <div class="footer-social">
                <h3>Connect with Us</h3>
                <ul>
                    <li><a href="#">LinkedIn</a></li>
                    <li><a href="#">Twitter</a></li>
                    <li><a href="#">Facebook</a></li>
                </ul>
            </div>
            <div class="footer-legal">
                <h3>Legal</h3>
                <ul>
                    <li><a href="#">Privacy Policy</a></li>
                    <li><a href="#">Terms of Service</a></li>
                </ul>
            </div>
            
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 Face Detection Inc. All rights reserved.</p>
        </div>
    </footer>
    
  
  
  </>
    
  );
}

export default App;

