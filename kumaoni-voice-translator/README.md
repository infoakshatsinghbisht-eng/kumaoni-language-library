# 🎙️ Kumaoni Voice Translator (कुमाऊँनी आवाज अनुवादक)

A modern, full-stack Voice Translation application powered by the [`kumaoni`](https://github.com/infoakshatsinghbisht-eng/kumaoni-language-library) language library.

Features real-time multilingual Speech-to-Speech translation into authentic Central Pahari Kumaoni with live 60fps audio waveform visualization, two-way conversational dialogue mode, and mountain dialect phrasebooks.

---

## 🌟 Key Features

1. **🎙️ Real-Time Speech-to-Speech (STT $\to$ Translation $\to$ Spoken TTS)**:
   - Speak in English, Hindi, Nepali, French, Spanish, German, etc.
   - Converts speech into authentic Kumaoni with Central Pahari phonetic cadences and retroflex timing.
2. **⚡ Auto-Speak & Audio Controls**:
   - Hands-free continuous translation mode.
   - Adjust playback speed (`0.8x`, `1.0x`, `1.2x`) with syllabic stress breakdown.
3. **📊 Live 60fps Audio Waveform Visualizer**:
   - Animated Web Audio API canvas visualizer pulsing in real time with microphone and speech playback.
4. **💬 Two-Way Dialogue Mode**:
   - Split-screen conversation studio for **Tourist / Visitor** $\leftrightarrow$ **Local Mountain Resident**.
5. **🏔️ Mountain Phraseboard**:
   - Instant one-tap spoken dialogues across Greetings, Mountain Trails & Roads, Food & Hospitality, Health & Emergency, and Market.
6. **📜 Session History**:
   - Live session timeline with instant one-click audio replay.

---

## 🚀 Quickstart

### 1. Run the Full App with Python (One Command)
```bash
python run_app.py
```
Open **`http://localhost:8000`** in your browser.

---

### 2. Or Run Backend & Frontend Separately (Developer Mode)

#### Start Backend (FastAPI):
```bash
cd backend
pip install -r requirements.txt
python server.py 8000
```

#### Start Frontend (Vite):
```bash
cd frontend
npm install
npm run dev
```
Open **`http://localhost:3000`**.

---

## 🏗️ Architecture

```
kumaoni-voice-translator/
├── backend/
│   ├── server.py             # FastAPI REST & Streaming Backend
│   └── requirements.txt      # Backend dependencies
├── frontend/
│   ├── src/
│   │   ├── app.js            # Client-side Speech & Visualizer Engine
│   │   └── style.css         # Modern Glassmorphism & Neon Design System
│   ├── index.html            # Main UI Shell
│   ├── package.json          # Node & Vite configuration
│   └── vite.config.js        # Vite dev-server config with API proxy
├── run_app.py                # Single-command application launcher
└── README.md
```

---

## 📜 API Documentation

When the backend is running, interactive Swagger API docs are available at **`http://localhost:8000/docs`**.

- `POST /api/voice/translate`: Universal voice translation with syllables and SSML.
- `POST /api/voice/dialogue`: Two-way conversation helper.
- `GET /api/voice/phrases`: Curated mountain dialogue phrasebook.
- `GET /api/voice/wav`: Synthesized uncompressed PCM WAV audio stream.
- `GET /api/health`: Service status and word count stats.
