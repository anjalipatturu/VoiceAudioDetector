# 🎙️ Voice Activity Detector

A simple **Voice Activity Detection (VAD)** application that identifies speech and silence regions in an audio file using **RMS energy-based signal processing**.

The project provides an interactive **Streamlit interface** for uploading audio, visualizing speech activity, analyzing RMS energy, and viewing detected speech segments.

---

## ✨ Features

* 🎵 Upload WAV, MP3, and OGG audio files
* 🔊 Built-in audio playback
* 🗣️ Detect speech and silence regions
* 📊 Calculate speech and silence percentages
* 〰️ Visualize the audio waveform
* 🟢 Highlight detected speech regions
* 📈 Display RMS energy over time
* 🚦 Show the detection threshold
* ⏱️ Extract speech segment timestamps
* 🔍 Display technical audio information
* ⚡ Simple and lightweight signal-processing approach

---

## 🧠 How It Works

The application uses an **energy-based Voice Activity Detection** approach.

```text
Audio File
    ↓
Convert to Mono
    ↓
Resample to 16 kHz
    ↓
Divide Audio into Frames
    ↓
Calculate RMS Energy
    ↓
Convert Energy to dB
    ↓
Compare with Threshold
    ↓
Speech / Silence
    ↓
Display Results
```

### Detection Process

1. The uploaded audio is converted to **mono**.
2. The audio is resampled to **16 kHz**.
3. The signal is divided into small frames.
4. **RMS (Root Mean Square) energy** is calculated for every frame.
5. RMS energy is converted into decibels.
6. Each frame is compared against an energy threshold.
7. Frames above the threshold are classified as **speech**.
8. Consecutive speech frames are grouped into speech segments.

---

## 📊 Visualizations

The application provides:

### Speech Activity Timeline

Shows which parts of the audio are classified as speech or silence.

### Waveform with Speech Regions

Displays the original waveform and highlights the detected speech regions.

### RMS Energy

Shows the energy level of the audio over time along with the detection threshold.

---

## 🛠️ Tech Stack

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Core programming language |
| Streamlit  | Interactive web interface |
| Librosa    | Audio processing          |
| NumPy      | Numerical calculations    |
| Matplotlib | Data visualization        |
| SoundFile  | Audio file handling       |

---

## 📁 Project Structure

```text
VoiceActivityDetector/
│
├── app.py
├── requirements.txt
├── .gitignore
└── .venv/
```

> `.venv/` is excluded from GitHub using `.gitignore`.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/voice-activity-detector.git
```

### 2. Open the project

```bash
cd voice-activity-detector
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually it will be available at:

```text
http://localhost:8501
```

---

## ⚙️ Configuration

The current implementation uses:

```python
Sample Rate = 16000 Hz
Frame Length = 512 samples
Hop Length = 256 samples
RMS Threshold = -35 dB
```

The threshold can be adjusted in `app.py` depending on the audio recording and background noise.

---

## 🧪 Example Output

The application provides information such as:

```text
Detection Summary

Speech      64.2%
Silence     35.8%
Duration    8.42 sec
Sample Rate 16000 Hz
```

Detected speech segments are displayed as:

```text
Segment 1 → 0.42s - 2.18s
Segment 2 → 3.01s - 5.47s
Segment 3 → 6.12s - 8.02s
```

---

## ⚠️ Limitations

This project uses a simple **energy-based rule** rather than a machine-learning model.

Therefore:

* Loud background noise may be detected as speech.
* Very quiet speech may not be detected.
* The threshold may need adjustment for different recordings.
* It is not designed to distinguish speech from all types of non-speech sounds.

This project is primarily intended for **learning, experimentation, and demonstrating fundamental audio signal-processing concepts**.

---

## 🔮 Future Improvements

Possible improvements include:

* [ ] Adaptive energy threshold
* [ ] Zero-Crossing Rate based detection
* [ ] Minimum speech duration filtering
* [ ] Noise reduction before detection
* [ ] Real-time microphone input
* [ ] Machine-learning based VAD
* [ ] Integration with speech recognition
* [ ] Integration with audio noise suppression

---

## 🎯 Learning Outcomes

Through this project, I explored:

* Audio preprocessing
* Sampling rate and mono audio
* Audio framing
* RMS energy
* Decibel representation
* Threshold-based classification
* Speech segmentation
* Audio visualization
* Python audio-processing libraries
* Streamlit application development

---

## 🔗 Project Architecture

This VAD can also be used as an initial stage in a larger speech-processing system:

```text
Audio Input
     ↓
Voice Activity Detection
     ↓
Speech Region Detection
     ↓
Noise Suppression
     ↓
Clean Speech
     ↓
Speech Recognition / AI Processing
```


