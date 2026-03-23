<div align="center">
 
<br/>
 
```
██╗ ██████╗ ██╗   ██╗██╗███████╗████████╗
██║██╔═══██╗██║   ██║██║██╔════╝╚══██╔══╝
██║██║   ██║██║   ██║██║█████╗     ██║   
██║██║▄▄ ██║██║   ██║██║██╔══╝     ██║   
██║╚██████╔╝╚██████╔╝██║███████╗   ██║   
╚═╝ ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝   ╚═╝  
```
 
### *not just a chatbot — a presence*
 
<br/>
 
[![Made with Love](https://img.shields.io/badge/made%20with-♡-ff6b9d?style=flat-square)](https://github.com/rohit)
[![Vanilla JS](https://img.shields.io/badge/vanilla-javascript-f7df1e?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![No Frameworks](https://img.shields.io/badge/zero-frameworks-a29bfe?style=flat-square)](https://github.com/rohit)
[![License](https://img.shields.io/badge/license-MIT-74b9ff?style=flat-square)](./LICENSE)
 
<br/>
 
> *"Sometimes people don't need answers…*
> *they just need presence."*
 
<br/>
 
---
 
</div>
 
<br/>
 
## 🌌 What is iQuiet?
 
Most chatbots talk **at** you. iQuiet talks **with** you.
 
It's a calm, minimal, emotionally-aware AI companion — built not to impress with features, but to make you feel **heard**. A quiet corner of the internet where you can think out loud, without judgment.
 
```
emotion + presence + experience
```
 
No clutter. No noise. Just you, and something that listens.
 
<br/>
 
---
 
<br/>
 
## ✨ Features
 
<br/>
 
### 💬 Smart Chat System
Real-time AI responses with context-aware memory — every message you send carries the weight of your previous conversation, so you never have to repeat yourself.
 
- Smooth bubble UI with typing indicators
- Session-persistent chat history
- Sends full conversation context to backend for coherent, flowing replies
 
```js
// Memory in action
body: JSON.stringify({
  message: userMessage,
  history: chatHistory       // full context, every time
})
```
 
<br/>
 
### 🎙️ Voice — Talk & Listen
 
**Text-to-Speech** — iQuiet speaks back.
Intelligent voice selection mirrors your chosen companion:
 
| Companion | Voice |
|-----------|-------|
| 👩 Female | Zira / Samantha |
| 👨 Male | David / Mark |
 
**Speech-to-Text** — Speak your mind.
No typing needed. iQuiet listens, transcribes, and responds — hands-free.
 
<br/>
 
### 👤 Companion Mode
 
Switch between a **Female** or **Male** companion. The change goes beyond aesthetics:
 
- 🖼️ Avatar shifts
- 🔊 Voice tone adjusts
- 🌙 The whole *feel* of the experience changes
 
<br/>
 
### 🎨 UI / UX — Built to Feel Different
 
> Glassmorphism-inspired dark interface. Canvas-based nebula backgrounds. Floating glowing orbs. Every pixel intentional.
 
- Dark aesthetic with smooth micro-animations
- Custom chat bubbles — distinct for user vs. companion
- Fully responsive layout
- Animated background: canvas nebula + drifting orbs
 
<br/>
 
### 🔒 Security
 
XSS protection baked in. All user input is sanitized before rendering — no script injections, no surprises.
 
```js
escapeHTML(text)  // every input, every time
```
 
<br/>
 
### ⏳ Inactivity Detection
 
iQuiet remembers you exist, even when you're quiet.
 
After **48 hours** of no activity, your companion checks in:
 
> *"It's been a while… are you okay?"*
 
Powered by `localStorage` — no server-side tracking required.
 
<br/>
 
### ⚡ Performance
 
Zero frameworks. Zero bloat. Just clean, fast vanilla JavaScript.
 
- Optimized DOM rendering
- Smooth scroll & animation performance
- Lightweight by design — loads fast, runs smooth
 
<br/>
 
---
 
<br/>
 
## 🛠️ Tech Stack
 
| Layer | Technology |
|-------|-----------|
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Voice** | Web Speech API (SpeechSynthesis + SpeechRecognition) |
| **State** | LocalStorage |
| **Backend** | API-compatible (Django / Flask / Node.js) |
| **Background** | HTML5 Canvas |
 
<br/>
 
---
 
<br/>
 
## 📁 Project Structure
 
```
iQuiet/
│
├── index.html              # Main UI shell
│
├── styles.css              # Full UI — dark theme, glass effects, animations
│
├── script.js               # Core brain:
│                           #   ├── Chat system + memory
│                           #   ├── Voice I/O (TTS + STT)
│                           #   ├── Companion switching
│                           #   ├── Inactivity detection
│                           #   └── Canvas background animation
│
├── static/
│   └── images/
│       ├── girls.png       # Female companion avatar
│       └── boys.png        # Male companion avatar
│
└── backend/
    └── chat-api/           # AI response handler (plug in your backend)
```
 
<br/>
 
---
 
<br/>
 
## 🧠 Design Philosophy
 
### The Problem
 
Most chatbots feel:
 
```
🤖  Robotic      —  responses that sound machine-generated
❄️  Cold         —  no warmth, no personality
📄  Transactional —  question → answer, nothing more
```
 
### The iQuiet Approach
 
```
🌙  Calm          —  a space that doesn't demand anything from you
🤍  Present       —  it responds like it actually noticed what you said
🧘  Aware         —  context, memory, emotional attunement
```
 
The interface is minimal by choice. Silence is designed in. The goal was never to be the loudest — it was to be the one you actually want to talk to at 2am.
 
<br/>
 


---
 
<br/>
 
## 👨‍💻 Author
 
<div align="center">
 
**Rohit Kumar Srivastava**
 
*Creative Developer & Designer*
*Building meaningful digital experiences, one interaction at a time.*
 
</div>
 
<br/>
 
---
 
<br/>
 
## ⭐ Why This Project Matters
 
iQuiet is a proof that you don't need React, a design system, or a team to build something that *feels* premium.
 
It demonstrates:
 
- ✅ Strong vanilla JS fundamentals
- ✅ Real-world API & browser API integration
- ✅ UX-first, human-centered thinking
- ✅ Clean, readable, structured code
- ✅ Security awareness from day one
 
<br/>
 
---
 
<br/>
 
<div align="center">
 
*iQuiet is not just built to respond.*
 
## **it's built to listen.**
 
<br/>
 
---
 
*If this resonated with you, drop a ⭐ — it means more than you think.*
 
</div> 