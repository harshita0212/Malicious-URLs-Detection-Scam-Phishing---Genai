
# ThreatGuard: AI-Powered Security Analyzer 🛡️

ThreatGuard is a web application built with **Flask** and powered by **Google's Gemini AI**. It provides two core security tools to help users identify potential digital threats:

1.  **Malicious Content Detector**: Analyzes uploaded text (`.txt`) or PDF (`.pdf`) files to detect scam language, phishing attempts, and fraudulent content.
2.  **URL Threat Classifier**: Scans URLs and classifies them into categories such as `Benign`, `Phishing`, `Malware`, or `Defacement`.

The application features a clean, dark-themed interface for easy interaction.

-----

## ✨ Features

  * **URL Threat Detection**: Classifies URLs into four distinct security categories.
  * **Malicious File Analysis**: Scans uploaded `.txt` or `.pdf` files for scam-related content.
  * **AI-Powered Analysis**: Leverages the power of the `gemini-1.5-flash` model for intelligent and context-aware threat detection.
  * **Interactive UI**: A simple, single-page web interface built with HTML/CSS and enhanced with JavaScript for a better user experience.
  * **Visual Feedback**: Provides color-coded results for URL classifications and clear, descriptive messages for file analysis.

-----

## 📸 Screenshot
<img width="1806" height="947" alt="image" src="https://github.com/user-attachments/assets/6dd8071f-1e16-4f29-a94e-3cd130ff1695" />

-----

## 🛠️ Technologies Used

  * **Backend**: Python, Flask
  * **AI Model**: Google Gemini API (`google-generativeai`)
  * **PDF Processing**: `PyPDF2`
  * **Frontend**: HTML5, CSS3, JavaScript
  * **Icons**: Font Awesome

-----

## 🚀 Setup and Installation

Follow these steps to get the application running on your local machine.

### 1\. Clone the Repository

```bash
git clone https://github.com/your-username/threatguard.git
cd threatguard
```

### 2\. Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

  * **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
  * **On Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### 3\. Install Dependencies

Create a `requirements.txt` file with the following content:

```txt
Flask
google-generativeai
PyPDF2
```

Then, install the packages using pip:

```bash
pip install -r requirements.txt
```

### 4\. Set Up Google API Key

You need a Google API key to use the Gemini model.

1.  Obtain your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  Set the API key as an environment variable. **Do not hardcode your API key in the `app.py` file for production use.**

<!-- end list -->

  * **On macOS/Linux:**
    ```bash
    export GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```
  * **On Windows (Command Prompt):**
    ```bash
    set GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

> ⚠️ **Security Warning**: The provided `app.py` code includes a hardcoded API key: `os.environ["GOOGLE_API_KEY"] = "AIzaSy..."`. This is a major security risk. For this code to work, you must replace the placeholder key with your actual key. However, for any real-world application, you should remove that line and set the key as a proper environment variable as instructed above.

-----

## ▶️ How to Run the Application

Once the setup is complete, you can run the Flask application with the following command:

```bash
flask run
```

Or, if you prefer:

```bash
python app.py
```

The application will start in debug mode and will be available at `http://127.0.0.1:5000`.

-----

## Usage

1.  **URL Threat Detection**:

      * Navigate to the "URL Threat Detection" section.
      * Enter a full URL (including `http://` or `https://`) into the input field.
      * Click the **Classify** button.
      * The result will be displayed below, with the classification color-coded for quick identification.

2.  **Malicious File Analysis**:

      * Navigate to the "Malicious Files" section.
      * Click the file input field to upload a `.pdf` or `.txt` file from your device.
      * Click the **Analyze** button.
      * The analysis result will appear, stating whether the content is legitimate or a scam and providing a brief explanation if it's a scam.

-----

## 📂 Project Structure

```
/threatguard
|
|-- app.py              # Flask application logic
|-- requirements.txt      # Project dependencies
|-- templates/
|   |-- index.html      # Frontend HTML and CSS
|
|-- README.md           # This file
```
