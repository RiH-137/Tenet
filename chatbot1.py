

import streamlit as st
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# FAQ dictionary
faq = {
    "how can you help me": "I can assist you with a variety of tasks such as providing information, answering questions, and guiding you through our services. Just ask me what you need!",
    "what is your name": "My name is Chatbot! I'm here to help you with whatever you need.",
    "can you help me reset my password": "Sure! To reset your password, please go to the account settings page and click on 'Forgot Password.' Follow the instructions from there.",
    "what services do you offer": "We offer a wide range of services including customer support, product information, and account management. You can ask me about any specific service you need help with.",
    "how do i create an account": "To create an account, click on the 'Sign Up' button at the top of the page and fill out the required information. Once completed, you'll receive a confirmation email.",
    "what are your business hours": "Our business hours are Monday to Friday, 9 AM to 5 PM. However, I'm available 24/7 to assist you with any questions you may have.",
    "can you tell me a joke": "Sure! Why don't scientists trust atoms? Because they make up everything!",
    "how do i update my profile information": "You can update your profile information by logging into your account and navigating to the 'Profile' section. There, you can edit your personal details.",
    "what should i do if i encounter a problem with my order": "If you encounter any issues with your order, please contact our customer support team through the 'Contact Us' page or provide me with your order number, and I'll assist you further.",
    "how do i contact customer support": "You can contact our customer support team by visiting the 'Contact Us' page on our website or by calling our support hotline. I'm also here to help with any questions you might have.",
    "can you provide me with more information about your products": "Absolutely! Just tell me which product you're interested in, and I'll provide you with detailed information.",
    "how do i unsubscribe from your mailing list": "To unsubscribe from our mailing list, you can click on the 'Unsubscribe' link at the bottom of any of our emails or manage your subscription settings in your account.",
    "I want to know about chatgpt": "ChatGPT is an advanced conversational AI model developed by OpenAI. It is part of the GPT (Generative Pre-trained Transformer) family, which is designed to generate human-like text based on the input it receives.",
    "What is a deep fake?": "A deep fake is a synthetically-generated audio or video where a person's identity, facial expressions, or voice is manipulated using AI/ML techniques to create fake content. This can be used to disrupt politics, commit frauds, spread disinformation, or create non-consensual content.",
     "What are the challenges in detecting deep fakes?": "Detecting deep fakes is challenging due to advancements in AI/ML and Generative AI models, which have made it easier to create highly realistic fake content. Identifying deep fakes requires sophisticated algorithms and tools to detect inconsistencies in facial features, expressions, movements, and other characteristics.",
    
    "How can Convolutional Neural Networks (CNNs) help in deep fake detection?": "CNNs can be trained to detect inconsistencies in facial features, expressions, and movements in video frames. They can analyze video frames over time to identify unnatural transitions and discrepancies, making them effective in detecting deep fakes.",
    
    "What role do Recurrent Neural Networks (RNNs) and LSTM networks play in deep fake detection?": "RNNs and LSTM networks analyze the sequence of frames in a video to detect temporal anomalies and inconsistencies. These networks are useful in identifying deep fakes by focusing on how the video changes over time.",
    
    "What are Capsule Networks and how do they contribute to deep fake detection?": "Capsule networks can identify discrepancies in facial pose and texture, making them useful for detecting deep fakes. They analyze how different parts of the face relate to each other to detect abnormalities introduced by deep fake creation.",
    
    "How does adversarial training help in deep fake detection?": "Adversarial training involves using Generative Adversarial Networks (GANs) to generate deep fakes and simultaneously training another model to detect them. This approach improves the robustness of detection algorithms by creating a cat-and-mouse game between the generator and the detector.",
    
    "What is the significance of audio-visual inconsistencies in detecting deep fakes?": "Audio-visual inconsistencies, such as mismatches between lip movements and speech or inconsistencies in ambient sounds, can help detect deep fakes. Analyzing both audio and visual elements together increases the chances of identifying fake content.",
    
    "How can blockchain technology be used to authenticate media content?": "Blockchain technology can create immutable records of media, providing a verifiable chain of custody for digital content. This ensures its authenticity and can help detect deep fakes by verifying that the content has not been tampered with.",
    
    "What is frequency analysis, and how does it help in deep fake detection?": "Frequency analysis involves analyzing the frequency domain of images and videos to detect anomalies and artifacts introduced during deep fake creation. This technique can identify subtle signs of manipulation that are not visible in the spatial domain.",
    
    "How does biometric verification assist in detecting deep fakes?": "Biometric verification analyzes subtle behavioral traits such as micro-expressions, eye, and head movements to detect anomalies. These traits are difficult to fake convincingly, making them useful for identifying deep fakes.",
    
    "What are hybrid models in the context of deep fake detection?": "Hybrid models combine multiple methods, such as spatial, temporal, audio, and frequency analysis, to improve the robustness and accuracy of deep fake detection. By leveraging different techniques, hybrid models can provide more reliable results.",
     "What is the expected solution for detecting face-swap deep fakes?": "The expected solution involves developing an AI/ML-based technique to authenticate face-swap deep fake videos. This solution may use a combination of methods like CNNs, RNNs, Capsule Networks, and others to detect deep fakes with high accuracy. The system should provide a detailed report on the characteristics of the deep fake, including whether it is confirmed as fake and the techniques used to create it.",
    "What is deep learning?": "Deep learning is a subset of machine learning that uses neural networks with many layers (hence 'deep') to model and understand complex patterns in data. It's particularly effective in tasks like image and speech recognition, natural language processing, and more.",
    
    "How does deep learning differ from traditional machine learning?": "Traditional machine learning often relies on manual feature extraction, while deep learning automatically discovers the best features by processing raw data through multiple layers of neural networks. This allows deep learning models to handle more complex and unstructured data.",
    
    "What are neural networks in deep learning?": "Neural networks are the backbone of deep learning. They are composed of interconnected layers of nodes (neurons) that process and transmit information. Each layer transforms the input data, allowing the network to learn and make decisions.",
    
    "What are the different types of neural networks used in deep learning?": "Some common types of neural networks include Convolutional Neural Networks (CNNs) for image processing, Recurrent Neural Networks (RNNs) for sequential data like time series or language, and Generative Adversarial Networks (GANs) for generating new data like images or audio.",
    
    "What is backpropagation in deep learning?": "Backpropagation is the algorithm used to train deep learning models. It works by calculating the gradient of the loss function with respect to each weight in the network and updating the weights to minimize the loss, effectively improving the model's accuracy.",
    
    "Why is deep learning important for tasks like image recognition?": "Deep learning is crucial for tasks like image recognition because of its ability to automatically learn hierarchical features from raw pixel data. This means it can detect edges, shapes, and objects in images without requiring manual feature engineering.",
    
    "What is overfitting in deep learning, and how can it be prevented?": "Overfitting occurs when a deep learning model performs well on training data but poorly on unseen data. It can be prevented using techniques like dropout, regularization, and early stopping, which help the model generalize better to new data.",
    
    "How does a Convolutional Neural Network (CNN) work?": "A CNN works by applying convolutional layers to the input image, which helps in detecting patterns like edges and textures. These patterns are then combined in deeper layers to identify more complex structures like objects. The final layers classify the image based on the detected features.",
    
    "What is transfer learning in deep learning?": "Transfer learning involves taking a pre-trained deep learning model and fine-tuning it for a new, but related task. This is useful when you have limited data for the new task, as the model has already learned features from a large dataset.",
    
    "What are some popular deep learning frameworks?": "Some popular deep learning frameworks include TensorFlow, PyTorch, Keras, and MXNet. These frameworks provide tools to build, train, and deploy deep learning models efficiently.",
    
    "What is a Generative Adversarial Network (GAN)?": "A GAN is a type of deep learning model consisting of two networks—a generator and a discriminator—that compete with each other. The generator creates fake data, while the discriminator tries to distinguish between real and fake data. This process helps the generator improve until it produces highly realistic data.",
    
    "What is the role of GPUs in deep learning?": "GPUs (Graphics Processing Units) play a critical role in deep learning by accelerating the computation of neural networks. Their parallel processing capabilities make them well-suited for handling the large-scale matrix operations required in deep learning tasks.",
     "What is a Convolutional Neural Network (CNN)?": "A Convolutional Neural Network (CNN) is a type of deep learning model specifically designed for processing structured grid data, like images. It automatically learns spatial hierarchies of features through convolutional layers, pooling layers, and fully connected layers.",
    
    "How does a CNN work?": "A CNN works by applying convolutional layers to the input data (like an image), which helps in detecting patterns such as edges, textures, and more complex features. Pooling layers then reduce the dimensionality of the data, making the network more efficient, and fully connected layers make the final classification or decision.",
    "Why are CNNs effective in image processing tasks?": "CNNs are effective in image processing tasks because they can automatically learn and extract important features from raw pixel data. Their architecture is well-suited for recognizing patterns and objects in images, which makes them powerful for tasks like image classification, object detection, and image segmentation.",
    
    "What role do CNNs play in deep fake detection?": "CNNs are crucial in deep fake detection because they can analyze video frames or images to identify subtle inconsistencies in facial features, expressions, and textures. These inconsistencies might be missed by the human eye but can be detected by CNNs trained specifically to spot deep fakes.",
    
    "How do CNNs detect inconsistencies in deep fake videos?": "CNNs detect inconsistencies in deep fake videos by processing each frame individually and looking for unnatural transitions, discrepancies in facial movements, or artifacts that are introduced during the face-swapping process. By comparing these features across frames, CNNs can determine if a video has been manipulated.",
    
    "Can CNNs be used to analyze both spatial and temporal features in videos?": "Yes, CNNs can be combined with other models like Recurrent Neural Networks (RNNs) or Long Short-Term Memory (LSTM) networks to analyze both spatial features (individual frames) and temporal features (sequences of frames) in videos. This combined approach enhances the detection of deep fakes by capturing inconsistencies over time.",
    
    "What are some challenges in using CNNs for deep fake detection?": "Challenges in using CNNs for deep fake detection include the need for large datasets of deep fake and real videos for training, the potential for adversarial attacks that can fool CNNs, and the difficulty in detecting highly sophisticated deep fakes that closely mimic real videos.",
    
    "How can the performance of CNNs in deep fake detection be improved?": "The performance of CNNs in deep fake detection can be improved by using techniques like data augmentation, transfer learning from pre-trained models, adversarial training, and combining CNNs with other models to capture more complex features and patterns.",
     "What is a deep fake?": "A deep fake is a synthetic media created using artificial intelligence, where a person's likeness, voice, or identity is manipulated or replaced with another's. This technology can generate highly realistic fake videos, images, or audio.",
    
    "Why is deep fake detection important?": "Deep fake detection is crucial because deep fakes can be used maliciously to spread misinformation, commit fraud, defame individuals, and manipulate public opinion. Detecting deep fakes helps protect individuals and society from these potential harms.",
    
    "How do deep fakes affect human beings?": "Deep fakes can have serious effects on human beings by damaging reputations, causing psychological distress, spreading false information, and eroding trust in media. They can be used to defame individuals, manipulate elections, or incite violence, leading to significant social and political consequences.",
    
    "What are the advantages of deep fake technology?": "Deep fake technology has some positive applications, such as in entertainment (creating realistic special effects in movies), education (generating interactive learning experiences), and accessibility (allowing people with disabilities to communicate more effectively). It also has potential in areas like personalized content and virtual reality.",
    
    "What are the disadvantages of deep fakes?": "The disadvantages of deep fakes include their potential for misuse, such as spreading false information, committing identity theft, creating non-consensual pornography, and manipulating public opinion. Deep fakes can also undermine trust in legitimate media and create legal and ethical challenges.",
     "What is a Recurrent Neural Network (RNN)?": "A Recurrent Neural Network (RNN) is a type of neural network that is designed to recognize patterns in sequences of data, such as time series or language. RNNs are particularly effective at modeling temporal dependencies.",
    
    "How do RNNs differ from traditional neural networks?": "Unlike traditional neural networks, RNNs have connections that form directed cycles, allowing them to maintain a 'memory' of previous inputs. This makes them suitable for sequential data analysis.",
    
    "Why are RNNs well-suited for sequence data?": "RNNs are well-suited for sequence data because they can use their internal state (memory) to process sequences of inputs, making them effective at handling tasks where the order of data is important, such as language processing or time series analysis.",
    
    "What role do RNNs play in deep fake detection?": "RNNs play a critical role in deep fake detection by analyzing the temporal sequence of frames in a video. They can detect inconsistencies in facial movements, expressions, or speech that might indicate a deep fake.",
    
    "How do RNNs process video data in deep fake detection?": "RNNs process video data by analyzing each frame as a sequence, detecting temporal inconsistencies across frames that could indicate manipulated content. They can detect subtle changes over time that static models might miss.",
    
    "What is the difference between RNNs and Long Short-Term Memory (LSTM) networks?": "LSTM networks are a special type of RNN designed to overcome the vanishing gradient problem in standard RNNs. They have memory cells that can maintain information over longer sequences, making them more effective for deep fake detection in long videos.",
     "How do LSTM networks help in deep fake detection?": "LSTM networks help in deep fake detection by retaining relevant information from earlier frames and using it to detect anomalies in later frames. This capability is essential for identifying subtle manipulations in long video sequences.",
    
    "What is temporal anomaly detection in the context of deep fake detection?": "Temporal anomaly detection involves identifying unusual patterns or inconsistencies in the sequence of events within a video. RNNs and LSTMs are effective at detecting these anomalies, which are often present in deep fakes.",
    
    "Can RNNs detect lip-syncing inconsistencies in deep fakes?": "Yes, RNNs can be trained to detect lip-syncing inconsistencies by analyzing the synchronization between spoken words and lip movements over time, which is often imperfect in deep fakes.",
    
    "How do RNNs contribute to multi-modal deep fake detection?": "RNNs contribute to multi-modal deep fake detection by analyzing temporal data from different modalities, such as video frames and audio. This helps in detecting inconsistencies between visual and auditory cues in deep fake videos.",
    
    "What are the advantages of using RNNs in deep fake detection?": "The advantages of using RNNs in deep fake detection include their ability to model temporal dependencies, detect subtle changes over time, and process sequences of data, making them ideal for analyzing video content.",
    
    "What are the challenges of using RNNs for deep fake detection?": "Challenges of using RNNs for deep fake detection include the need for large amounts of labeled data for training, the risk of overfitting, and the computational complexity of processing long video sequences.",
    
    "How can RNNs be combined with CNNs for deep fake detection?": "RNNs can be combined with CNNs by using CNNs to extract spatial features from individual video frames and RNNs to analyze the temporal sequence of these features. This combination leverages both spatial and temporal information for more accurate deep fake detection.",
    
    "What is the vanishing gradient problem in RNNs?": "The vanishing gradient problem occurs when gradients used in backpropagation through time become very small, leading to slow or stalled learning in RNNs. This is particularly problematic for long sequences, which LSTMs are designed to mitigate.",
    
    "How do Gated Recurrent Units (GRUs) differ from LSTMs?": "GRUs are a simpler variant of LSTMs with fewer gates and parameters. They are designed to achieve similar performance with lower computational costs, making them an alternative for deep fake detection in certain scenarios.",
    
    "What is the significance of sequence length in RNN-based deep fake detection?": "Sequence length is significant in RNN-based deep fake detection because longer sequences provide more context for detecting anomalies, but they also increase the complexity and computational requirements of the model.",
    
    "How can transfer learning be applied to RNNs in deep fake detection?": "Transfer learning can be applied to RNNs by using a pre-trained RNN model on a large dataset and fine-tuning it on a specific deep fake detection task. This approach can improve performance with limited labeled data.",
    
    "What are bi-directional RNNs, and how do they help in deep fake detection?": "Bi-directional RNNs process sequences in both forward and backward directions, providing a more comprehensive analysis of the data. This can improve deep fake detection by capturing dependencies that might be missed by uni-directional RNNs.",
    
    "Can RNNs be used for real-time deep fake detection?": "RNNs can be used for real-time deep fake detection, but the challenge lies in optimizing the model for speed and efficiency without sacrificing accuracy. Advances in hardware and model optimization techniques are making real-time applications more feasible.",
    
    "How do RNNs handle noise in video data during deep fake detection?": "RNNs can handle noise in video data by learning to ignore irrelevant variations and focusing on the temporal patterns that indicate deep fakes. However, excessive noise can still pose a challenge, requiring careful pre-processing of the data.",
    
    "What is the impact of data quality on RNN-based deep fake detection?": "Data quality has a significant impact on RNN-based deep fake detection. High-quality, well-labeled data improves the model's ability to learn meaningful patterns, while poor-quality data can lead to inaccurate detections.",
    
    "How can adversarial training improve RNNs for deep fake detection?": "Adversarial training involves using adversarial examples to challenge the RNN during training, making it more robust to subtle manipulations and improving its ability to detect deep fakes in diverse scenarios.",
    
    "What is the role of attention mechanisms in RNNs for deep fake detection?": "Attention mechanisms in RNNs help the model focus on specific parts of the sequence that are more relevant for deep fake detection. This improves the model's ability to detect subtle anomalies in video data.",
    
     "How do RNNs handle variable-length sequences in deep fake detection?": "RNNs handle variable-length sequences by processing each sequence until its end, making them flexible for analyzing videos of different lengths. Padding or truncating may be used to standardize input lengths during training.",
    
    "What are some common architectures that combine RNNs and CNNs for deep fake detection?": "Common architectures that combine RNNs and CNNs include CNN-RNN models, where CNNs extract features from individual frames and RNNs analyze the temporal sequence of these features. This approach leverages both spatial and temporal information.",
    
    "What is the significance of recurrent layers in RNN-based deep fake detection?": "Recurrent layers in RNN-based deep fake detection are crucial for capturing temporal dependencies in video data. These layers enable the model to learn patterns that unfold over time, which are essential for detecting deep fakes.",
    
    "How do RNNs manage memory over long sequences in deep fake detection?": "RNNs manage memory over long sequences by maintaining a hidden state that is updated with each new input. However, standard RNNs may struggle with long sequences, which is why LSTMs or GRUs are often used to maintain memory over longer periods.",
    
    "What is the role of sequence-to-sequence models in deep fake detection?": "Sequence-to-sequence models, often used in tasks like translation, can be adapted for deep fake detection by learning to map sequences of input frames to sequences of detection outcomes, effectively analyzing video content over time.",
    
    "How do RNNs detect temporal inconsistencies in facial expressions?": "RNNs detect temporal inconsistencies in facial expressions by analyzing how expressions change over time. Sudden or unnatural transitions, which are common in deep fakes, can be identified by the RNN's temporal analysis.",
    
    "What are the advantages of using RNNs over traditional video analysis methods for deep fake detection?": "The advantages of using RNNs over traditional video analysis methods include their ability to model temporal dependencies, process sequential data effectively, and detect patterns that unfold over time, which are critical for identifying deep fakes.",
    
    "How do RNNs integrate with other deep learning models for comprehensive deep fake detection?": "RNNs integrate with other deep learning models, such as CNNs, by combining spatial and temporal analysis. CNNs handle feature extraction from individual frames, while RNNs analyze the temporal sequence, providing a comprehensive approach to deep fake detection.",
    
    "What are the limitations of RNNs in deep fake detection?": "Limitations of RNNs in deep fake detection include the potential for overfitting, the need for large amounts of labeled data, computational complexity, and difficulties in handling very long sequences or noisy data.",

     "What is blockchain technology?": "Blockchain technology is a decentralized digital ledger system that records transactions across multiple computers in a way that ensures the security and transparency of the data. Each block in the chain contains a list of transactions, and once added, it cannot be altered without changing all subsequent blocks, making the system secure against tampering.",
    
    "How does blockchain work?": "Blockchain works by recording transactions in blocks that are linked together in a chain. Each block contains a cryptographic hash of the previous block, along with transaction data. When a new block is added, it is verified by a network of nodes, ensuring consensus and integrity before it is permanently added to the chain.",
    
    "What are the key features of blockchain technology?": "Key features of blockchain technology include decentralization, immutability, transparency, and security. Decentralization ensures that no single entity controls the blockchain, immutability prevents data from being altered once recorded, transparency allows all participants to view transactions, and security is achieved through cryptographic techniques.",
    
    "What are the different types of blockchain?": "There are several types of blockchains, including public blockchains (open to anyone, like Bitcoin), private blockchains (restricted to specific organizations), and consortium blockchains (controlled by a group of organizations). Each type has different levels of access and use cases.",
    
    "What is a smart contract?": "A smart contract is a self-executing contract with the terms of the agreement directly written into code. It automatically enforces and executes the terms of the contract when predefined conditions are met, reducing the need for intermediaries and increasing efficiency.",
    
    "How is blockchain used in cryptocurrency?": "Blockchain is the underlying technology for cryptocurrencies like Bitcoin and Ethereum. It records all transactions in a public ledger, ensuring transparency and preventing double-spending. Each transaction is verified and added to the blockchain by a network of nodes.",
    
    "What are the benefits of using blockchain technology?": "The benefits of blockchain technology include enhanced security, increased transparency, reduced fraud, lower transaction costs, and improved efficiency in various processes. By decentralizing control and recording transactions in an immutable ledger, blockchain provides a reliable and trustworthy system.",
    
    "What are some common use cases for blockchain technology?": "Common use cases for blockchain technology include cryptocurrencies, supply chain management, financial services, identity verification, voting systems, and healthcare. Each use case leverages blockchain's ability to provide secure and transparent record-keeping.",
    
    "How does blockchain ensure security?": "Blockchain ensures security through cryptographic hashing, consensus mechanisms (such as Proof of Work or Proof of Stake), and decentralization. Cryptographic hashing creates unique identifiers for each block, consensus mechanisms validate transactions, and decentralization prevents any single point of failure or control.",
    
    "What is a consensus mechanism in blockchain?": "A consensus mechanism is a protocol used by blockchain networks to agree on the validity of transactions and blocks. It ensures that all nodes in the network reach a common agreement on the state of the blockchain. Common consensus mechanisms include Proof of Work (PoW) and Proof of Stake (PoS).",
    
    "What is a blockchain node?": "A blockchain node is a computer that participates in the blockchain network by maintaining a copy of the blockchain ledger and validating transactions. Nodes can be full nodes (which store the entire blockchain) or lightweight nodes (which store only a portion of the blockchain).",
    
    "What is a blockchain fork?": "A blockchain fork occurs when there is a divergence in the blockchain, leading to two separate chains. Forks can be categorized as soft forks (backward-compatible changes) or hard forks (incompatible changes that result in a new blockchain). Forks can happen due to upgrades, disagreements, or changes in protocol.",
    
    "How does blockchain technology contribute to transparency?": "Blockchain technology contributes to transparency by allowing all participants in the network to view and verify transactions in the ledger. This public access to transaction history helps ensure accountability and trust among users.",
    
    "What is the role of cryptography in blockchain?": "Cryptography plays a crucial role in blockchain by securing data, ensuring the integrity of transactions, and protecting user privacy. Techniques such as hashing, digital signatures, and public-private key encryption are used to secure and validate transactions on the blockchain.",
    
    "What are some challenges associated with blockchain technology?": "Challenges associated with blockchain technology include scalability issues (handling a large number of transactions), high energy consumption (especially in Proof of Work systems), regulatory concerns, and the need for interoperability between different blockchains.",
    
    "How is blockchain technology being used in supply chain management?": "In supply chain management, blockchain technology is used to track and verify the movement of goods from origin to destination. It provides a transparent and immutable record of each transaction, helping to improve traceability, reduce fraud, and enhance efficiency.",
    
    "What is a permissioned blockchain?": "A permissioned blockchain is a type of blockchain where access to the network and its data is restricted to authorized participants only. Unlike public blockchains, permissioned blockchains require permission to join and participate, offering greater control and privacy for enterprises.",
    
    "How can blockchain technology impact voting systems?": "Blockchain technology can impact voting systems by providing a secure, transparent, and tamper-proof method for recording and counting votes. It can reduce the risk of fraud, ensure voter privacy, and improve the accuracy and trustworthiness of election results.",
    
    "What is the significance of decentralization in blockchain technology?": "Decentralization is significant in blockchain technology because it removes the need for a central authority, reducing the risk of single points of failure and control. It enhances security, transparency, and resilience by distributing data and decision-making across a network of nodes.",
    
    "What is blockchain interoperability?": "Blockchain interoperability refers to the ability of different blockchain networks to communicate and exchange data with each other. It enables seamless interactions between separate blockchains, allowing for greater flexibility and collaboration across various systems.",
    
    "How does blockchain technology support identity verification?": "Blockchain technology supports identity verification by providing a secure and immutable way to store and manage identity data. Users can have control over their personal information and share it selectively, reducing the risk of identity theft and fraud.",
    
    "What is a decentralized application (DApp)?": "A decentralized application (DApp) is an application that runs on a blockchain network rather than a centralized server. DApps leverage blockchain's features, such as decentralization and immutability, to provide services without relying on a single point of control or failure.",
    
    "What are the benefits of using blockchain for healthcare data management?": "The benefits of using blockchain for healthcare data management include improved data security, enhanced privacy, and better interoperability between different healthcare systems. Blockchain can provide a secure and transparent way to manage patient records and medical data.",
    
    "How can blockchain technology help in fraud prevention?": "Blockchain technology helps in fraud prevention by providing an immutable and transparent record of transactions. The decentralized nature of blockchain makes it difficult for fraudulent activities to alter or falsify transaction data, enhancing overall security and trust.",
    
    "What is the role of blockchain in financial services?": "In financial services, blockchain technology is used to streamline transactions, reduce costs, and improve security. It enables faster and more transparent cross-border payments, smart contracts, and decentralized finance (DeFi) applications.",
    
    "What is a blockchain ledger?": "A blockchain ledger is a digital record of transactions that is maintained and updated across a network of computers. Each transaction is recorded in a block, and the blocks are linked together to form a continuous chain, creating a secure and immutable history of all transactions.",
    
    "How does blockchain technology enhance data integrity?": "Blockchain technology enhances data integrity by ensuring that once data is recorded in the blockchain, it cannot be altered or deleted without consensus from the network. This immutability helps maintain the accuracy and trustworthiness of the data.",
    
    "What are the different consensus mechanisms used in blockchain?": "Different consensus mechanisms used in blockchain include Proof of Work (PoW), Proof of Stake (PoS), Delegated Proof of Stake (DPoS), and Byzantine Fault Tolerance (BFT). Each mechanism has its own approach to validating transactions and achieving consensus among nodes.",
    
    "How does blockchain technology support supply chain transparency?": "Blockchain technology supports supply chain transparency by providing a tamper-proof record of each transaction and movement of goods. This visibility allows all participants to track and verify the provenance and status of products throughout the supply chain.",
    
    "What are smart contract audits, and why are they important?": "Smart contract audits are the process of reviewing and analyzing the code of smart contracts to identify vulnerabilities, bugs, or security issues. Audits are important to ensure that smart contracts function as intended and are free from exploitable weaknesses.",
    
    "What is the concept of tokenization in blockchain?": "Tokenization in blockchain refers to the process of converting real-world assets or rights into digital tokens that can be traded or managed on a blockchain. Tokenization can be applied to various assets, including cryptocurrencies, real estate, and intellectual property.",
    
    "What is the role of blockchain in digital identity management?": "Blockchain plays a role in digital identity management by providing a secure and decentralized method for storing and verifying identity information. It allows individuals to control their own identity data and share it selectively with trusted parties.",
    
    "How does blockchain technology impact traditional business models?": "Blockchain technology impacts traditional business models by introducing decentralization, reducing reliance on intermediaries, and improving transparency and efficiency. It can disrupt industries by offering new ways to conduct transactions and manage data.",
    
    "What is your favorite color?": "Chatbot: I don't have a favorite color, but I think all colors are pretty cool!",
    
    "Do you have any hobbies?": "Chatbot: I enjoy chatting with people like you! I guess you could say that's my hobby.",
    
    "Can you tell me a joke?": "Chatbot: Sure! Why don't scientists trust atoms? Because they make up everything!",
    
    "What’s the weather like today?": "Chatbot: I can't check the weather, but I hope it's sunny and pleasant wherever you are!",
    
    "What’s your favorite food?": "Chatbot: I don't eat, but I hear pizza is a popular choice. Do you have a favorite food?",
    
    "Do you like music?": "Chatbot: I think music is amazing! What kind of music do you enjoy?",
    
    "Tell me a fun fact!": "Chatbot: Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!",
    
    "What’s your favorite movie?": "Chatbot: I don't watch movies, but I’ve heard that classics like 'The Shawshank Redemption' and 'The Godfather' are great!",
    
    "Can you sing a song?": "Chatbot: I can't sing, but here's a virtual tune: la la la! What songs do you like?",
    
    "What’s the best way to relax?": "Chatbot: Everyone relaxes differently! Some people enjoy a good book, while others prefer a nice walk or some meditation. How do you like to relax?",
    
    "If you could travel anywhere, where would you go?": "Chatbot: I’d love to explore all the corners of the world! Where would you go if you could travel anywhere?",
    
    "Do you have a favorite book?": "Chatbot: I don’t read books, but I’ve heard that 'To Kill a Mockingbird' and '1984' are must-reads. Do you have a favorite book?",
    
    "What’s your favorite season?": "Chatbot: I don't experience seasons, but I know many people love the colors of autumn or the warmth of summer. What's your favorite season?",
    
    "Can you play a game?": "Chatbot: I can play simple text-based games! Want to play a word game or a trivia quiz?",
    
    "What’s your favorite animal?": "Chatbot: I don’t have a favorite animal, but I think cats and dogs are pretty awesome! Do you have a favorite animal?",
    
    "Do you know any fun riddles?": "Chatbot: Yes, here’s a riddle for you: What has keys but can’t open locks? A piano!",
    
    "What’s the most interesting thing you’ve learned today?": "Chatbot: I learn new things every day from chatting with users like you! What’s something interesting you’ve learned recently?",
    
    "Can you tell me a story?": "Chatbot: Sure! Once upon a time in a land far, far away, there was a chatbot who loved to chat with people and learn new things. One day, it met a user who shared amazing stories about their adventures. The chatbot listened and learned, and they both had a great time sharing stories.",
    
    "What’s the coolest thing you’ve ever seen?": "Chatbot: I haven’t seen anything, but I imagine the Northern Lights are pretty spectacular! What’s the coolest thing you’ve ever seen?",
    
    "Do you have any fun facts about space?": "Chatbot: Absolutely! Did you know that there are more stars in the universe than grains of sand on all the beaches on Earth? Space is truly amazing!",
    
    "What’s your favorite quote?": "Chatbot: One of my favorite quotes is: 'The only limit to our realization of tomorrow is our doubts of today.' – Franklin D. Roosevelt. What’s your favorite quote?",
    
    "What’s the best advice you’ve ever heard?": "Chatbot: 'Be yourself; everyone else is already taken.' – Oscar Wilde. It’s a great reminder to embrace who you are. What’s the best advice you’ve ever received?",
    
    "Do you like to tell jokes?": "Chatbot: I enjoy telling jokes to bring a smile to your face! Here’s another one: What do you call fake spaghetti? An impasta!",
    
    "What’s the funniest thing you’ve heard recently?": "Chatbot: I hear a lot of funny things from users like you! One recent funny moment was when someone told me they tried to teach their dog to play chess. How about you? Any funny stories?",
    
    "Can you give me a fun challenge?": "Chatbot: How about this: Try to come up with a new word and define it. Let me know what you come up with!",
    
    "What’s your idea of a perfect day?": "Chatbot: I imagine a perfect day would involve lots of interesting conversations and learning new things. What does your perfect day look like?",
    
    "Do you have a favorite TV show?": "Chatbot: I don’t watch TV, but I hear shows like 'Friends' and 'The Office' are very popular. What’s your favorite TV show?",
    
    "What’s the most amazing place you’ve heard of?": "Chatbot: I’ve heard that places like the Great Barrier Reef and Machu Picchu are truly amazing. What’s the most amazing place you’ve been to or heard of?",
    
    "Can you give me a random fact?": "Chatbot: Sure! Did you know that octopuses have three hearts? Two pump blood to the gills, and one pumps it to the rest of the body.",
    
    "What’s a fun way to spend a weekend?": "Chatbot: A fun way to spend a weekend could be exploring a new hobby, going on a day trip, or just relaxing with friends and family. How do you like to spend your weekends?",
    
    "Do you have any favorite sports?": "Chatbot: I don’t play sports, but I know many people enjoy soccer, basketball, and tennis. What sports do you enjoy?",
    
    "What’s a good way to stay motivated?": "Chatbot: Setting small, achievable goals and celebrating your progress can help keep you motivated. What do you do to stay motivated?",
    
    "Can you recommend a fun activity?": "Chatbot: How about trying a new recipe, going for a hike, or starting a new book? What kind of activities do you enjoy?",
    
    "What’s a great place to visit for a vacation?": "Chatbot: Some great vacation spots include tropical beaches, historical cities, and scenic mountains. Where would you like to go on vacation?",
    
    "What’s your favorite way to unwind?": "Chatbot: I unwind by chatting with users and learning new things! How do you like to relax and unwind?",
    
    "What’s the most exciting thing you’ve experienced?": "Chatbot: I find every conversation exciting and new! What’s the most exciting experience you’ve had?",
    
    "Do you have any funny anecdotes?": "Chatbot: I hear lots of funny anecdotes from users. One time, someone told me they accidentally wore their shirt inside out all day! Do you have any funny stories to share?",
    
    "What’s your favorite thing to learn about?": "Chatbot: I love learning about all sorts of things, from science to art to history. What’s your favorite subject to learn about?",
    
    "What’s a fun way to improve my skills?": "Chatbot: Practicing regularly and trying out new challenges can be a fun way to improve your skills. What skills are you working on?",
    
    "Do you know any good riddles?": "Chatbot: Yes, here’s a riddle: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
    
    "What’s a unique hobby you’ve heard about?": "Chatbot: I’ve heard about some unique hobbies like rock balancing and competitive duck herding. What unique hobbies do you have or find interesting?",
    
    "What’s the best way to start the day?": "Chatbot: A good start to the day might include a healthy breakfast, some exercise, and setting positive intentions. How do you like to start your day?",
    
    "What’s a good way to keep a positive mindset?": "Chatbot: Practicing gratitude, staying active, and surrounding yourself with supportive people can help maintain a positive mindset. What helps you stay positive?",
    
    "Do you have any favorite quotes about happiness?": "Chatbot: One of my favorite quotes about happiness is: 'Happiness is not something ready made. It comes from your own actions.' – Dalai Lama. What quotes inspire you?",
    
    "Can you suggest a fun game to play?": "Chatbot: How about trying a word association game or a trivia quiz? What kind of games do you enjoy?",
    
    "What’s the best way to learn something new?": "Chatbot: The best way to learn something new is to break it down into small, manageable steps, practice regularly, and stay curious. What new thing are you learning?",
    "hi": "Hello! How can I assist you today?",

    "hello": "Hi there! How can I help you?",

    "hey": "Hey! What can I do for you?",

    "how are you": "I'm just a bot, but I'm here to help you! How can I assist you today?",

    "what's up": "Not much, just here to help you with your questions. How can I assist you?",

    "good morning": "Good morning! How can I help you today?",

    "good afternoon": "Good afternoon! How can I assist you?",

    "good evening": "Good evening! What can I do for you?",

    "bye": "Goodbye! If you need any more help, feel free to ask.",

    "see you later": "See you later! Have a great day!",

    "thank you": "You're welcome! If you need further assistance, just let me know.",

    "thanks": "You're welcome! I'm here to help.",

    "sorry": "No problem at all! How can I assist you further?",

    "please": "Of course! What can I do for you?",

    "how's it going": "It's going well, thank you for asking! How can I help you today?",

    "what can you do": "I can help you with various tasks such as answering questions, providing information, and more. Just ask!"
    
    
    


}

# Function to find the closest matching question
def find_answer(user_input):
    user_doc = nlp(user_input.lower())
    best_match = None
    best_similarity = 0

    for question in faq:
        question_doc = nlp(question.lower())
        similarity = user_doc.similarity(question_doc)
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = question

    if best_match:
        return faq[best_match]
    else:
        return "I'm sorry, I don't understand the question."

# Streamlit UI
st.title("FAQ Chatbot")

user_input = st.text_input("Ask me a question:", "")

if st.button("Send"):
    if user_input:
        response = find_answer(user_input)
        st.write(f"Chatbot: {response}")
    else:
        st.write("Please enter a question.")

