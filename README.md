🖼️ Design and Development of Image Captioning with Neural Networks using AI & ML
📌 Project Overview

The project aims to develop an AI-powered Image Captioning System that can automatically generate human-like captions for images.
By integrating Convolutional Neural Networks (CNNs) for feature extraction and Recurrent Neural Networks (RNNs) for sequence modeling, the system bridges the gap between computer vision and natural language processing.

🎯 Objectives

To design and implement an end-to-end image captioning model.

To extract meaningful features from images using ResNet CNN encoder.

To generate accurate captions using an LSTM-based decoder.

To evaluate model performance with suitable metrics (e.g., BLEU).

To deploy the system for real-world applications in assistive technologies, search engines, and accessibility tools.


🏗️ Methodology

Dataset Preparation – Images and captions are collected, preprocessed, and stored.

Feature Extraction – A ResNet-50 CNN encoder extracts image features.

Caption Generation – An LSTM-based RNN decoder generates natural language captions.

Training & Evaluation – Model trained on labeled datasets, optimized using loss functions, evaluated with BLEU score.

Deployment – Model integrated for inference and tested with unseen images.

🖥️ System Architecture
          +--------------------+
          |   Input Image      |
          +---------+----------+
                    |
           [ResNet CNN Encoder]
                    |
            Feature Representation
                    |
           [LSTM Decoder Network]
                    |
          +---------v----------+
          | Generated Caption  |
          +--------------------+



⚙️ Technologies Used

Programming Language: Python 3.x

Deep Learning Framework: PyTorch

Image Feature Extraction: ResNet-50

Caption Generator: LSTM-based RNN

Supporting Libraries: Pandas, NumPy, Matplotlib, TorchVision


📊 Results & Discussion

The system successfully generates contextual captions for unseen images.

Demonstrates the potential of AI in bridging visual understanding with natural language.

Can be extended for assistive technologies like tools for visually impaired individuals.


This project is a Streamlit-based web app that generates captions for uploaded images using BLIP (Bootstrapping Language-Image Pretraining) and converts the captions into speech using Google Text-to-Speech (gTTS).


📁 Image-Captioning-AIML
│── 📜 FYP.py                 # Main Streamlit app
│── 📜 README.md              # Project documentation
│── 📜 requirements.txt       # Dependencies
│── 📁 audio/                 # Auto-generated audio captions

🖼️ Example Workflow

Upload an image (.jpg, .jpeg, .png).

Click Generate Caption.

See AI-generated caption on screen.

Download caption text or listen to it as audio.

📊 Future Scope

Add multilingual captions and TTS.

Deploy on Hugging Face Spaces / Streamlit Cloud.

Extend to video captioning.

Use transformer-based models with attention for improved accuracy.




