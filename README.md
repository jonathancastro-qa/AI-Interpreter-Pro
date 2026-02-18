# AI-Interpreter Pro 🎙️🤖
**Real-Time Bi-directional Translation System for Remote Meetings**

## 📌 Project Overview
AI-Interpreter Pro is a cross-platform desktop application designed to bridge language barriers in professional meetings (Microsoft Teams, Google Meet, Zoom). The system captures system audio and microphone input independently to provide real-time Spanish-to-English and English-to-Spanish translation.

### Key Features
- **Dual-Channel Audio Capture:** Independent processing of user microphone and system loopback (meeting participants).
- **AI-Powered Translation:** Utilizing OpenAI Whisper API for high-accuracy speech-to-text and translation.
- **Virtual Voice Interpretation:** Spanish speech is translated and synthesized into English, then routed back into the meeting as a virtual microphone input.
- **Transparent UI Overlay:** A sleek, "Always on Top" floating window built with Electron/Tauri for live captioning.
- **Low Latency Design:** Optimized audio buffering for near-instant communication.

---

## 🏗️ Technical Architecture
The project follows a **Micro-service/Bridge architecture**:
- **Backend:** Python (Audio processing, VAD, OpenAI API Integration).
- **Frontend:** Electron.js / HTML5 / CSS3 (Transparent UI Overlay).
- **Communication:** Real-time bi-directional data flow via WebSockets (Socket.io).
- **Audio Routing:** Virtual Audio Cable (VAC) integration for system output injection.

---

## 🗺️ Roadmap & Project Management
This project is developed using **Agile/Scrum** methodologies, divided into 4 main Epics:

### Epic 1: Audio Infrastructure (The Ear)
- [ ] Environment Setup (VENV, Git, Directory Structure).
- [ ] System Audio Loopback Implementation (SoundCard).
- [ ] Local Microphone Capture (SpeechRecognition).

### Epic 2: AI Engine (The Brain)
- [ ] OpenAI Whisper Integration (EN -> ES Subtitles).
- [ ] OpenAI Whisper Integration (ES -> EN Translation).
- [ ] Voice Activity Detection (VAD) logic.

### Epic 3: Voice Synthesis & Output (The Mouth)
- [ ] OpenAI TTS Integration (English voice generation).
- [ ] Virtual Audio Cable routing (Output to meeting).

### Epic 4: Floating UI (The View)
- [ ] Frameless & Transparent window setup.
- [ ] WebSocket bridge between Python and JS.
- [ ] Dynamic Styling & High-Contrast Captions.

---

## 🛠️ Tech Stack
- **Languages:** Python, JavaScript, HTML/CSS.
- **AI Models:** OpenAI Whisper (STT), OpenAI TTS-1.
- **Frameworks:** Electron/Tauri, Socket.io.
- **Audio Utils:** VB-CABLE, SoundCard, PyAudio.

---

## 👨‍💻 Author
**Jonathan Castro** *Tester QA*
