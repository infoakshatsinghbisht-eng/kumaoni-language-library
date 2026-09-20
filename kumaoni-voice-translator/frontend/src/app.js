// Kumaoni Voice AI - Full-Stack Client App
document.addEventListener("DOMContentLoaded", () => {
  // Navigation Tabs
  const navTabs = document.querySelectorAll(".nav-tab");
  const tabPanes = document.querySelectorAll(".tab-pane");

  navTabs.forEach(tab => {
    tab.addEventListener("click", () => {
      const target = tab.getAttribute("data-tab");
      navTabs.forEach(t => t.classList.remove("active"));
      tabPanes.forEach(p => p.classList.remove("active"));
      tab.classList.add("active");
      const targetPane = document.getElementById(`tab-${target}`);
      if (targetPane) targetPane.classList.add("active");
    });
  });

  // Check Backend Health
  const statusBadge = document.getElementById("backend-status-badge");
  async function checkHealth() {
    try {
      const res = await fetch("/api/health");
      const data = await res.json();
      if (data.status === "healthy") {
        statusBadge.innerHTML = `<span class="pulse-dot"></span> API Online (v${data.version})`;
      }
    } catch (e) {
      statusBadge.innerHTML = `<span class="pulse-dot" style="background:#f43f5e"></span> API Offline`;
      statusBadge.classList.remove("badge-pulse");
      statusBadge.style.borderColor = "rgba(244, 63, 94, 0.4)";
      statusBadge.style.color = "#f43f5e";
    }
  }
  checkHealth();

  // =========================================================
  // 1. SPEECH-TO-SPEECH TRANSLATOR
  // =========================================================
  const btnVoiceMic = document.getElementById("btn-voice-mic");
  const micStatusText = document.getElementById("mic-status-text");
  const voiceSourceLang = document.getElementById("voice-source-lang");
  const toggleAutoSpeak = document.getElementById("toggle-autospeak");
  const voiceInputText = document.getElementById("voice-input-text");
  const speechLangTag = document.getElementById("speech-lang-tag");
  const btnVoiceTranslateManual = document.getElementById("btn-voice-translate-manual");
  const btnVoiceClear = document.getElementById("btn-voice-clear");

  const voiceOutputKumaoni = document.getElementById("voice-output-kumaoni");
  const voiceOutputRoman = document.getElementById("voice-output-roman");
  const voiceSyllableChips = document.getElementById("voice-syllable-chips");
  const btnPlayKumaoniSpeech = document.getElementById("btn-play-kumaoni-speech");
  const btnPlayKumaoniWav = document.getElementById("btn-play-kumaoni-wav");
  const btnCopyVoiceKmy = document.getElementById("btn-copy-voice-kmy");
  const playBtnText = document.getElementById("play-btn-text");

  const canvas = document.getElementById("audio-visualizer-canvas");
  const ctx = canvas ? canvas.getContext("2d") : null;

  let isRecording = false;
  let recognition = null;
  let currentSpeed = 1.0;
  let lastKumaoniText = "पासक अस्पताल कसि छ?";
  let lastRomanText = "Paasak aspataal kasi chha?";
  let visualizerAnimId = null;

  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (SpeechRecognition) {
    recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = true;
    recognition.maxAlternatives = 1;

    recognition.onstart = () => {
      isRecording = true;
      btnVoiceMic.classList.add("recording");
      micStatusText.textContent = "Listening... Speak now";
      micStatusText.className = "mic-status-text recording";
      startVisualizerAnimation(true);
    };

    recognition.onresult = (event) => {
      let interim = "";
      let final = "";

      for (let i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
          final += event.results[i][0].transcript;
        } else {
          interim += event.results[i][0].transcript;
        }
      }

      if (interim) voiceInputText.value = interim;
      if (final) {
        voiceInputText.value = final;
        handleVoiceTranslation(final);
      }
    };

    recognition.onerror = (event) => {
      console.warn("Speech recognition error:", event.error);
      stopRecording();
      micStatusText.textContent = event.error === "not-allowed" 
        ? "Microphone access denied. Type text above."
        : "Click Microphone to Speak";
    };

    recognition.onend = () => {
      stopRecording();
    };
  } else {
    if (micStatusText) micStatusText.textContent = "Speech recognition unavailable in this browser. Type text below.";
  }

  function startRecording() {
    if (!recognition) {
      alert("Speech recognition is not supported in this browser. Please use Chrome, Edge, or Safari.");
      return;
    }
    try {
      recognition.lang = voiceSourceLang.value;
      recognition.start();
    } catch (e) {
      console.error(e);
    }
  }

  function stopRecording() {
    isRecording = false;
    if (btnVoiceMic) btnVoiceMic.classList.remove("recording");
    if (micStatusText) {
      micStatusText.textContent = "Click Microphone to Speak";
      micStatusText.className = "mic-status-text";
    }
    stopVisualizerAnimation();
  }

  if (btnVoiceMic) {
    btnVoiceMic.addEventListener("click", () => {
      if (isRecording) {
        if (recognition) recognition.stop();
        stopRecording();
      } else {
        startRecording();
      }
    });
  }

  if (voiceSourceLang) {
    voiceSourceLang.addEventListener("change", () => {
      if (speechLangTag) speechLangTag.textContent = voiceSourceLang.options[voiceSourceLang.selectedIndex].text;
    });
  }

  async function handleVoiceTranslation(spokenText) {
    const text = (spokenText || voiceInputText.value || "").trim();
    if (!text) return;

    micStatusText.textContent = "Translating speech to Kumaoni...";
    micStatusText.className = "mic-status-text speaking";

    try {
      const resp = await fetch("/api/voice/translate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: text,
          source_lang: voiceSourceLang.value.split("-")[0],
          generate_audio: true
        })
      });

      const data = await resp.json();
      lastKumaoniText = data.translated_text || text;
      lastRomanText = data.romanized || "";

      if (voiceOutputKumaoni) voiceOutputKumaoni.textContent = lastKumaoniText;
      if (voiceOutputRoman) voiceOutputRoman.textContent = lastRomanText;

      renderSyllables(data.syllables || []);
      addToHistory(text, lastKumaoniText, lastRomanText);

      if (toggleAutoSpeak.checked) {
        speakKumaoniSpeech(lastKumaoniText);
      } else {
        micStatusText.textContent = "Translation ready! Click 'Speak Kumaoni' to listen.";
      }
    } catch (err) {
      console.error(err);
      if (voiceOutputKumaoni) voiceOutputKumaoni.textContent = "Translation error. Please check server.";
    }
  }

  if (btnVoiceTranslateManual) {
    btnVoiceTranslateManual.addEventListener("click", () => {
      handleVoiceTranslation(voiceInputText.value);
    });
  }

  if (btnVoiceClear) {
    btnVoiceClear.addEventListener("click", () => {
      voiceInputText.value = "";
      voiceInputText.focus();
    });
  }

  function renderSyllables(syls) {
    if (!voiceSyllableChips) return;
    voiceSyllableChips.innerHTML = "";
    if (!syls || syls.length === 0) {
      voiceSyllableChips.innerHTML = `<span class="syl-chip">${lastKumaoniText}</span>`;
      return;
    }
    syls.forEach((s, idx) => {
      const chip = document.createElement("span");
      chip.className = "syl-chip";
      chip.textContent = s;
      voiceSyllableChips.appendChild(chip);

      if (idx < syls.length - 1) {
        const dot = document.createElement("span");
        dot.className = "syl-dot";
        dot.innerHTML = "&bull;";
        voiceSyllableChips.appendChild(dot);
      }
    });
  }

  // Speed Chips
  document.querySelectorAll(".speed-chip").forEach(chip => {
    chip.addEventListener("click", () => {
      document.querySelectorAll(".speed-chip").forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
      currentSpeed = parseFloat(chip.getAttribute("data-speed")) || 1.0;
    });
  });

  // Native Speech Synthesis Playback
  function speakKumaoniSpeech(textToSpeak) {
    const text = textToSpeak || lastKumaoniText;
    if (!text || !window.speechSynthesis) return;

    window.speechSynthesis.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "hi-IN";
    utterance.rate = 0.92 * currentSpeed;
    utterance.pitch = 1.0;

    if (btnPlayKumaoniSpeech) btnPlayKumaoniSpeech.classList.add("playing");
    if (playBtnText) playBtnText.textContent = "Speaking...";
    startVisualizerAnimation(false);

    utterance.onend = () => {
      if (btnPlayKumaoniSpeech) btnPlayKumaoniSpeech.classList.remove("playing");
      if (playBtnText) playBtnText.textContent = "Speak Kumaoni";
      stopVisualizerAnimation();
    };

    utterance.onerror = () => {
      if (btnPlayKumaoniSpeech) btnPlayKumaoniSpeech.classList.remove("playing");
      if (playBtnText) playBtnText.textContent = "Speak Kumaoni";
      stopVisualizerAnimation();
    };

    window.speechSynthesis.speak(utterance);
  }

  if (btnPlayKumaoniSpeech) {
    btnPlayKumaoniSpeech.addEventListener("click", () => {
      speakKumaoniSpeech(lastKumaoniText);
    });
  }

  if (btnPlayKumaoniWav) {
    btnPlayKumaoniWav.addEventListener("click", () => {
      const audio = new Audio("/api/voice/wav?duration=0.6&freq=480");
      startVisualizerAnimation(false);
      audio.play().catch(e => console.warn(e));
      audio.onended = () => stopVisualizerAnimation();
    });
  }

  if (btnCopyVoiceKmy) {
    btnCopyVoiceKmy.addEventListener("click", () => {
      navigator.clipboard.writeText(`${lastKumaoniText} (${lastRomanText})`).then(() => {
        btnCopyVoiceKmy.textContent = "✓";
        setTimeout(() => btnCopyVoiceKmy.textContent = "📋", 1500);
      });
    });
  }

  // Visualizer Canvas Animation
  function startVisualizerAnimation(isMic) {
    if (!ctx || !canvas) return;
    if (visualizerAnimId) cancelAnimationFrame(visualizerAnimId);
    let step = 0;

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const numBars = 32;
      const barWidth = (canvas.width / numBars) - 2;

      for (let i = 0; i < numBars; i++) {
        const freq = (i / numBars) * Math.PI * 4;
        const wave = Math.sin(freq + step * 0.15) * 0.5 + 0.5;
        const height = (wave * 55 + Math.random() * 25) * (isMic ? 1.0 : 0.85);

        const x = i * (barWidth + 2);
        const y = canvas.height - height;

        const grad = ctx.createLinearGradient(0, y, 0, canvas.height);
        if (isMic) {
          grad.addColorStop(0, "#f43f5e");
          grad.addColorStop(1, "rgba(244, 63, 94, 0.15)");
        } else {
          grad.addColorStop(0, "#10b981");
          grad.addColorStop(0.5, "#f59e0b");
          grad.addColorStop(1, "rgba(16, 185, 129, 0.1)");
        }

        ctx.fillStyle = grad;
        ctx.fillRect(x, y, barWidth, height);
      }

      step++;
      visualizerAnimId = requestAnimationFrame(draw);
    }

    draw();
  }

  function stopVisualizerAnimation() {
    if (!ctx || !canvas) return;
    if (visualizerAnimId) {
      cancelAnimationFrame(visualizerAnimId);
      visualizerAnimId = null;
    }
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = "rgba(245, 158, 11, 0.25)";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(0, canvas.height - 4);
    ctx.lineTo(canvas.width, canvas.height - 4);
    ctx.stroke();
  }

  stopVisualizerAnimation();

  // =========================================================
  // 2. TWO-WAY DIALOGUE MODE
  // =========================================================
  const visitorInput = document.getElementById("dialogue-visitor-input");
  const nativeInput = document.getElementById("dialogue-native-input");
  const btnVisitorSpeak = document.getElementById("btn-dialogue-visitor-speak");
  const btnNativeSpeak = document.getElementById("btn-dialogue-native-speak");
  const dialogueFeed = document.getElementById("dialogue-feed");
  const btnClearDialogue = document.getElementById("btn-clear-dialogue");

  async function postDialogueTurn(speaker, message, lang) {
    if (!message.trim()) return;
    try {
      const resp = await fetch("/api/voice/dialogue", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          speaker: speaker,
          message: message,
          source_lang: lang
        })
      });
      const res = await resp.json();
      renderDialogueBubble(res);
      if (speaker === "person_a") {
        speakKumaoniSpeech(res.translated_kumaoni);
      } else {
        speakKumaoniSpeech(res.translated_kumaoni);
      }
    } catch (e) {
      console.error(e);
    }
  }

  function renderDialogueBubble(res) {
    const isVisitor = res.speaker === "person_a";
    const bubble = document.createElement("div");
    bubble.className = `bubble ${isVisitor ? "bubble-visitor" : "bubble-native"}`;
    bubble.innerHTML = `
      <div class="bubble-speaker">${isVisitor ? "🎒 Visitor (Tourist)" : "🏔️ Local Resident (पहाड़ी)"}</div>
      <div class="bubble-orig">"${res.original}"</div>
      <div class="bubble-trans">➔ ${res.translated_kumaoni || res.translated_english}</div>
      <div class="bubble-roman">${res.romanized || ""}</div>
      <div class="bubble-actions">
        <button class="btn btn-outline btn-sm bubble-play" title="Listen Speech">🔊 Play</button>
      </div>
    `;
    bubble.querySelector(".bubble-play").addEventListener("click", () => {
      speakKumaoniSpeech(res.translated_kumaoni || res.original);
    });
    dialogueFeed.appendChild(bubble);
    dialogueFeed.scrollTop = dialogueFeed.scrollHeight;
  }

  if (btnVisitorSpeak) {
    btnVisitorSpeak.addEventListener("click", () => {
      postDialogueTurn("person_a", visitorInput.value, "en");
    });
  }

  if (btnNativeSpeak) {
    btnNativeSpeak.addEventListener("click", () => {
      postDialogueTurn("person_b", nativeInput.value, "kmy");
    });
  }

  if (btnClearDialogue) {
    btnClearDialogue.addEventListener("click", () => {
      dialogueFeed.innerHTML = "";
    });
  }

  // =========================================================
  // 3. MOUNTAIN PHRASEBOARD
  // =========================================================
  const voicePhraseGrid = document.getElementById("voice-phrase-grid");
  const pcatTabs = document.querySelectorAll(".pcat-tab");

  async function loadVoicePhrases(cat = "all") {
    try {
      const resp = await fetch(`/api/voice/phrases?category=${cat}`);
      const data = await resp.json();
      renderPhraseCards(data.phrases || []);
    } catch (e) {
      console.error(e);
    }
  }

  function renderPhraseCards(phrases) {
    if (!voicePhraseGrid) return;
    voicePhraseGrid.innerHTML = "";
    if (!phrases || phrases.length === 0) {
      voicePhraseGrid.innerHTML = `<div style="grid-column: 1/-1; text-align: center; color: #94a3b8; padding: 2rem;">No phrases found.</div>`;
      return;
    }

    phrases.forEach(p => {
      const card = document.createElement("div");
      card.className = "phrase-card";
      card.innerHTML = `
        <div>
          <div class="phrase-kumaoni">${p.kumaoni}</div>
          <div class="phrase-roman">${p.roman}</div>
          <div class="phrase-english">${p.english}</div>
        </div>
        <div class="phrase-card-footer">
          <span class="phrase-cat-badge">${p.category}</span>
          <button class="phrase-play-btn" title="Speak this phrase">▶</button>
        </div>
      `;

      card.addEventListener("click", () => {
        if (voiceInputText) voiceInputText.value = p.english;
        if (voiceOutputKumaoni) voiceOutputKumaoni.textContent = p.kumaoni;
        if (voiceOutputRoman) voiceOutputRoman.textContent = p.roman;
        lastKumaoniText = p.kumaoni;
        lastRomanText = p.roman;
        speakKumaoniSpeech(p.kumaoni);
        addToHistory(p.english, p.kumaoni, p.roman);
      });

      voicePhraseGrid.appendChild(card);
    });
  }

  loadVoicePhrases("all");

  pcatTabs.forEach(tab => {
    tab.addEventListener("click", () => {
      pcatTabs.forEach(t => t.classList.remove("active"));
      tab.classList.add("active");
      loadVoicePhrases(tab.getAttribute("data-cat"));
    });
  });

  // =========================================================
  // 4. SESSION HISTORY LOGS
  // =========================================================
  const voiceHistoryList = document.getElementById("voice-history-list");
  const btnClearHistory = document.getElementById("btn-clear-history");
  let historyItems = [];

  function addToHistory(src, tgtKmy, tgtRom) {
    if (!src || !tgtKmy) return;
    historyItems.unshift({
      src,
      tgtKmy,
      tgtRom,
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    });
    if (historyItems.length > 30) historyItems.pop();
    renderHistory();
  }

  function renderHistory() {
    if (!voiceHistoryList) return;
    if (historyItems.length === 0) {
      voiceHistoryList.innerHTML = `<div class="history-empty">No voice records yet. Click the microphone to start speaking!</div>`;
      return;
    }
    voiceHistoryList.innerHTML = "";
    historyItems.forEach(item => {
      const row = document.createElement("div");
      row.className = "history-card";
      row.innerHTML = `
        <div class="history-content">
          <div class="history-src">🗣️ "${item.src}" <span style="font-size:0.75rem; color:#64748b;">(${item.time})</span></div>
          <div class="history-tgt">🏔️ ${item.tgtKmy} <span style="font-size:0.85rem; color:#94a3b8; font-weight:normal;">(${item.tgtRom})</span></div>
        </div>
        <button class="btn btn-outline btn-sm history-play-btn" title="Replay Speech">🔊</button>
      `;
      row.querySelector(".history-play-btn").addEventListener("click", () => {
        speakKumaoniSpeech(item.tgtKmy);
      });
      voiceHistoryList.appendChild(row);
    });
  }

  if (btnClearHistory) {
    btnClearHistory.addEventListener("click", () => {
      historyItems = [];
      renderHistory();
    });
  }
});
