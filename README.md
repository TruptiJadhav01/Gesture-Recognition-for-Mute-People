# Sign Language Recognition with Voice Command

## 📌 Project Overview

Sign Language Recognition with Voice Command is a Python-based project designed to help people with hearing or speech impairments communicate more easily with others.

The system uses computer vision and machine learning techniques to recognize hand gestures through a camera and convert the recognized gestures into text and voice output. It aims to reduce communication barriers and make everyday interactions easier and more accessible.

## 🎯 Objectives

- Recognize hand gestures using a camera.
- Convert recognized gestures into meaningful text.
- Generate voice output using text-to-speech technology.
- Support real-time gesture recognition.
- Improve communication accessibility for people who use sign language.

## ✨ Key Features

- **Hand Gesture Recognition:** Detects and recognizes hand gestures from camera input.
- **Real-Time Processing:** Processes camera input to identify gestures.
- **Text Output:** Displays the recognized gesture as text.
- **Voice Output:** Converts recognized text into speech.
- **Computer Vision:** Uses image-processing techniques to analyze hand gestures.
- **Accessibility:** Supports communication between sign language users and people unfamiliar with sign language.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Computer Vision:** OpenCV
- **Hand Tracking:** MediaPipe
- **Machine Learning / Deep Learning:** TensorFlow and related model tools
- **Model File:** `new_model6.h5`
- **Development Environment:** Visual Studio Code

*Note: Confirm the libraries actually used by your current source code and model before finalizing this list.*

## ⚙️ How It Works

1. **Camera Input:** The camera captures the user's hand gestures.
2. **Hand Detection:** The system detects the hand in the captured frames.
3. **Image Processing:** The input is processed to prepare it for recognition.
4. **Gesture Classification:** The trained machine learning model predicts the corresponding gesture.
5. **Text Generation:** The recognized gesture is displayed as text.
6. **Voice Conversion:** The recognized text is converted into spoken output using text-to-speech functionality.

## 📂 Project Structure

```text
Sign-Language-Recognition/
│
├── Gesture_Recognize_sign.py
├── Dashboard_new.py
├── Image_capturing.py
├── Image_preprocessing.py
├── new_model6.h5
├── dataset/
├── preprocessed/
├── README.md
├── .gitignore
└── LICENSE
```

*The structure above is based on the project files identified in the repository. Additional files or folders may be present.*

## 💻 Installation and Setup

### Prerequisites

- Python installed on your computer
- Git
- A webcam or camera
- Visual Studio Code or another Python editor

### Step 1: Clone the Repository

```bash
git clone https://github.com/TruptiJadhav01/Gesture-Recognition-for-Mute-People.git
```

### Step 2: Open the Project Folder

```bash
cd Gesture-Recognition-for-Mute-People
```

### Step 3: Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

If the repository contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install the dependencies required by the source code. Check the project's imports and model compatibility before choosing package versions.

### Step 5: Run the Project

Open the project in VS Code and run the appropriate entry-point script.

For example, if `Dashboard_new.py` is the main application:

```bash
python Dashboard_new.py
```

If another script starts the application, use that script instead.

## 🧪 Testing

The project report describes testing activities covering:

- Gesture recognition
- Text-to-speech output
- Recognition under different lighting conditions
- Integration of recognition and voice modules
- System functionality and usability

Actual test results depend on the current implementation and testing environment.

## 🌍 Applications

- Assistive communication
- Educational environments
- Healthcare communication
- Customer service
- Accessible human-computer interaction

## ⚠️ Limitations

- Recognition accuracy may vary with lighting, camera quality, and hand position.
- The system can recognize only the gestures supported by its trained model.
- Complex gestures or signs outside the training dataset may not be recognized correctly.
- Recognition performance depends on the available hardware and software environment.
- Sign languages vary by region, so the recognized gestures should not be assumed to represent every sign language.

## 🚀 Future Scope

- Support for additional sign languages and regional variations.
- Improved recognition accuracy using advanced deep learning models.
- Sentence-level translation and contextual understanding.
- Offline operation and improved performance on low-power devices.
- Support for mobile and desktop platforms.
- A more accessible and user-friendly interface.

## 🎓 Project Information

**Project Title:** Sign Language Recognition with Voice Command

**Domain:** Artificial Intelligence, Machine Learning and Computer Vision

**Programming Language:** Python

**GitHub Repository:**  
https://github.com/TruptiJadhav01/Gesture-Recognition-for-Mute-People

## 🤝 Contribution

Suggestions and improvements that enhance recognition accuracy, accessibility, performance, and usability are welcome.

## 📄 License

This project includes a `LICENSE` file. Please refer to that file for the applicable terms of use and distribution.

---

*This project aims to use technology to make communication more accessible and inclusive.*
