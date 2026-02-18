# AI-Interpreter Pro 🎙️🤖

**Real-Time Bi-directional Translation System for Remote Meetings**

## 📌 Project Overview
AI-Interpreter Pro is a professional-grade desktop application designed to bridge language barriers in remote meetings (Microsoft Teams, Google Meet, Zoom). The system captures microphone input and meeting audio independently to provide high-accuracy real-time translation and future voice synthesis.

## ✨ Key Features
* **AI-Powered Transcription:** Integration with **OpenAI Whisper** for robust Speech-to-Text (STT) that handles technical jargon and diverse accents.
* **Dual-Channel Audio Capture:** Independent processing of user microphone (for personal dictation) and system loopback (for participants).
* **Vibrant Feedback UI:** Interactive "Click-to-Toggle" buttons with **Vibrant Red (`#FF0000`)** active states for unmistakable status awareness.
* **Transparent Overlay:** "Always on Top" semi-transparent window built with `CustomTkinter` for non-intrusive use during calls.
* **Traceability Logs:** Real-time console within the UI to monitor active audio devices (Virtual Cables) and processing status.

## 🏗️ Technical Architecture
The project follows a modular AI pipeline:
* **Inference Engine:** `OpenAI Whisper` (Local/API) for high-fidelity transcription.
* **Frontend:** `CustomTkinter` (Python) for a modern, hardware-accelerated interface.
* **Translation:** `Deep-Translator` API integration.
* **Audio Routing:** `VB-Audio Virtual Cable` integration to inject translated audio into meeting platforms.

## 🗺️ Roadmap & Project Management
This project is developed using **Agile/Scrum** methodologies, divided into 4 main Epics:

### Epic 1: Audio Infrastructure (The Ear) 🟢
- [x] Environment Setup (VENV, Git, VS Code).
- [x] Local Microphone Capture & Device Index Mapping.
- [x] Virtual Cable routing logic.

### Epic 2: AI Engine (The Brain) 🟡
- [x] Spanish-to-English Translation Logic.
- [x] **OpenAI Whisper Integration** (STT).
- [ ] OpenAI Whisper Integration (EN -> ES Subtitles for Meeting).
- [ ] Voice Activity Detection (VAD) optimization.

### Epic 3: Voice Synthesis & Output (The Mouth) 🔴
- [ ] OpenAI TTS / pyttsx3 Integration (English voice generation).
- [ ] Virtual Audio Cable routing (Direct output to meeting).

### Epic 4: Floating UI & UX (The View) 🟢
- [x] Frameless & Transparent window setup.
- [x] High-Contrast Vibrant Red state indicators.
- [x] Dynamic log console for QA traceability.

## 🛠️ Tech Stack
* **Languages:** Python 3.10+
* **AI Models:** OpenAI Whisper (Base/Small).
* **UI Framework:** CustomTkinter.
* **Libraries:** torch, openai-whisper, SoundDevice, SpeechRecognition.
* **Audio Utils:** VB-CABLE Virtual Audio Device, **FFmpeg**.

## ⚙️ Installation & Setup

### 1. Audio Virtualization
* Install [VB-CABLE Virtual Audio Device](https://vb-audio.com/Cable/). Required to route AI voice to meetings.

### 2. System Dependencies
* **FFmpeg** is mandatory. 
    * **Windows:** Install via [Chocolatey](https://chocolatey.org/) (`choco install ffmpeg`) or download from [ffmpeg.org](https://ffmpeg.org/) and add the `\bin` folder to your **System PATH**.
    * **Verify:** Run `ffmpeg -version` in terminal.

### 3. Python Environment
1. Clone the repository.
2. Create and activate a Virtual Environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate

## 👨‍💻 Author
**Jonathan Castro** - *Tester QA*
