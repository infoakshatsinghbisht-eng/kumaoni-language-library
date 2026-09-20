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

  // =========================================================
  // 0. VOICE TRANSLATOR & SPEECH ENGINE
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
  const ctx = canvas.getContext("2d");

  let isRecording = false;
  let recognition = null;
  let currentSpeed = 1.0;
  let lastKumaoniText = "कस छू तुम?";
  let lastRomanText = "Kas chou tum?";
  let audioCtx = null;
  let visualizerAnimId = null;

  // Initialize Web Speech Recognition
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
      let interimTranscript = "";
      let finalTranscript = "";

      for (let i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
          finalTranscript += event.results[i][0].transcript;
        } else {
          interimTranscript += event.results[i][0].transcript;
        }
      }

      if (interimTranscript) {
        voiceInputText.value = interimTranscript;
      }
      if (finalTranscript) {
        voiceInputText.value = finalTranscript;
        handleVoiceTranslation(finalTranscript);
      }
    };

    recognition.onerror = (event) => {
      console.warn("Speech recognition error:", event.error);
      stopRecording();
      if (event.error === "not-allowed") {
        micStatusText.textContent = "Microphone permission denied. Type above instead.";
      } else {
        micStatusText.textContent = "Click Microphone to Speak";
      }
    };

    recognition.onend = () => {
      stopRecording();
    };
  } else {
    micStatusText.textContent = "Speech recognition unavailable in this browser. Type below.";
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

  voiceSourceLang.addEventListener("change", () => {
    speechLangTag.textContent = voiceSourceLang.options[voiceSourceLang.selectedIndex].text;
  });

  // Perform Voice Translation
  async function handleVoiceTranslation(spokenText) {
    const text = (spokenText || voiceInputText.value || "").trim();
    if (!text) return;

    micStatusText.textContent = "Translating speech...";
    micStatusText.className = "mic-status-text speaking";

    try {
      const resp = await fetch("/api/voice/translate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: text,
          source: voiceSourceLang.value.split("-")[0],
          generate_audio: true
        })
      });

      const data = await resp.json();
      lastKumaoniText = data.translated_text || text;
      lastRomanText = data.romanized || "";

      voiceOutputKumaoni.textContent = lastKumaoniText;
      voiceOutputRoman.textContent = lastRomanText;

      // Render syllables
      renderSyllables(data.syllables || []);

      // Add to session log
      addToHistory(text, lastKumaoniText, lastRomanText);

      // Auto-speak if enabled
      if (toggleAutoSpeak.checked) {
        speakKumaoniSpeech(lastKumaoniText);
      } else {
        micStatusText.textContent = "Translation ready! Click 'Speak Kumaoni' to listen.";
      }
    } catch (err) {
      console.error(err);
      voiceOutputKumaoni.textContent = "Translation error. Please check server.";
    }
  }

  btnVoiceTranslateManual.addEventListener("click", () => {
    handleVoiceTranslation(voiceInputText.value);
  });

  btnVoiceClear.addEventListener("click", () => {
    voiceInputText.value = "";
    voiceInputText.focus();
  });

  function renderSyllables(syls) {
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

  // Speed controls
  document.querySelectorAll(".speed-chip").forEach(chip => {
    chip.addEventListener("click", () => {
      document.querySelectorAll(".speed-chip").forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
      currentSpeed = parseFloat(chip.getAttribute("data-speed")) || 1.0;
    });
  });

  // Speak Kumaoni using SpeechSynthesis
  function speakKumaoniSpeech(textToSpeak) {
    const text = textToSpeak || lastKumaoniText;
    if (!text || !window.speechSynthesis) return;

    window.speechSynthesis.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "hi-IN"; // Indic cadence articulates Central Pahari phonetics accurately
    utterance.rate = 0.92 * currentSpeed;
    utterance.pitch = 1.0;

    btnPlayKumaoniSpeech.classList.add("playing");
    playBtnText.textContent = "Speaking...";
    startVisualizerAnimation(false);

    utterance.onend = () => {
      btnPlayKumaoniSpeech.classList.remove("playing");
      playBtnText.textContent = "Speak Kumaoni";
      stopVisualizerAnimation();
    };

    utterance.onerror = () => {
      btnPlayKumaoniSpeech.classList.remove("playing");
      playBtnText.textContent = "Speak Kumaoni";
      stopVisualizerAnimation();
    };

    window.speechSynthesis.speak(utterance);
  }

  btnPlayKumaoniSpeech.addEventListener("click", () => {
    speakKumaoniSpeech(lastKumaoniText);
  });

  // Play Synthesized WAV Audio Tone
  btnPlayKumaoniWav.addEventListener("click", () => {
    const audio = new Audio("/api/voice/wav?duration=0.6&freq=480");
    startVisualizerAnimation(false);
    audio.play().catch(e => console.warn(e));
    audio.onended = () => stopVisualizerAnimation();
  });

  btnCopyVoiceKmy.addEventListener("click", () => {
    navigator.clipboard.writeText(`${lastKumaoniText} (${lastRomanText})`).then(() => {
      btnCopyVoiceKmy.textContent = "✓";
      setTimeout(() => btnCopyVoiceKmy.textContent = "📋", 1500);
    });
  });

  // Waveform Visualizer Canvas Animation
  function startVisualizerAnimation(isMic) {
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

        // Gradient
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
    if (visualizerAnimId) {
      cancelAnimationFrame(visualizerAnimId);
      visualizerAnimId = null;
    }
    // Clear & draw quiescent line
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = "rgba(245, 158, 11, 0.25)";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(0, canvas.height - 4);
    ctx.lineTo(canvas.width, canvas.height - 4);
    ctx.stroke();
  }

  stopVisualizerAnimation();

  // Spoken Mountain Phrases Quick-Board
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
        voiceInputText.value = p.english;
        voiceOutputKumaoni.textContent = p.kumaoni;
        voiceOutputRoman.textContent = p.roman;
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

  // Voice Session History
  const voiceHistoryList = document.getElementById("voice-history-list");
  const btnClearHistory = document.getElementById("btn-clear-history");
  let historyItems = [];

  function addToHistory(src, tgtKmy, tgtRom) {
    if (!src || !tgtKmy) return;
    historyItems.unshift({ src, tgtKmy, tgtRom, time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) });
    if (historyItems.length > 20) historyItems.pop();
    renderHistory();
  }

  function renderHistory() {
    if (historyItems.length === 0) {
      voiceHistoryList.innerHTML = `<div class="history-empty">No voice translations yet. Click the microphone above to start speaking!</div>`;
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

  btnClearHistory.addEventListener("click", () => {
    historyItems = [];
    renderHistory();
  });

  // =========================================================
  // 1. UNIVERSAL TEXT TRANSLATOR
  // =========================================================
  const btnTranslate = document.getElementById("btn-translate");
  const transInput = document.getElementById("translate-input");
  const sourceLangSelect = document.getElementById("source-lang-select");
  const selectMethod = document.getElementById("select-method");
  const outputDev = document.getElementById("translate-output-dev");
  const outputRoman = document.getElementById("translate-output-roman");
  const metaMethod = document.getElementById("output-meta-method");
  const metaConf = document.getElementById("output-meta-conf");
  const btnCopyKmy = document.getElementById("btn-copy-kmy");

  async function performTranslation() {
    const text = transInput.value.trim();
    if (!text) return;

    btnTranslate.disabled = true;
    btnTranslate.innerHTML = "<span>⏳ Translating...</span>";

    try {
      const resp = await fetch("/api/translate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: text,
          source: sourceLangSelect.value,
          method: selectMethod.value
        })
      });
      const data = await resp.json();
      outputDev.textContent = data.translated_text || text;
      outputRoman.textContent = data.romanized || "";
      metaMethod.textContent = `Method: ${data.method || "auto"}`;
      metaConf.textContent = `Confidence: ${Math.round((data.confidence || 0.95) * 100)}%`;
    } catch (err) {
      console.error(err);
      outputDev.textContent = "Translation error. Please check server.";
    } finally {
      btnTranslate.disabled = false;
      btnTranslate.innerHTML = "<span>✨ Translate to Kumaoni</span>";
    }
  }

  btnTranslate.addEventListener("click", performTranslation);

  // Quick pills
  document.querySelectorAll(".pill-sample").forEach(pill => {
    pill.addEventListener("click", () => {
      transInput.value = pill.getAttribute("data-text");
      sourceLangSelect.value = pill.getAttribute("data-lang");
      performTranslation();
    });
  });

  btnCopyKmy.addEventListener("click", () => {
    const text = outputDev.textContent;
    navigator.clipboard.writeText(text).then(() => {
      btnCopyKmy.textContent = "✓";
      setTimeout(() => btnCopyKmy.textContent = "📋", 1500);
    });
  });

  // =========================================================
  // 2. LEXICON & DICTIONARY
  // =========================================================
  const dictSearchInput = document.getElementById("dict-search-input");
  const btnDictSearch = document.getElementById("btn-dict-search");
  const dictContainer = document.getElementById("dict-results-container");
  const catChips = document.querySelectorAll(".cat-chip");

  const sampleWords = [
    { kumaoni: "पैलाग", roman: "pailag", english: "traditional respectful greeting (touching feet)", hindi: "प्रणाम / चरण स्पर्श", pos: "interjection", category: "greetings" },
    { kumaoni: "ईजा", roman: "ija", english: "mother", hindi: "माँ", pos: "noun", category: "kinship" },
    { kumaoni: "बाबु", roman: "babu", english: "father", hindi: "पिताजी", pos: "noun", category: "kinship" },
    { kumaoni: "दाज्यू", roman: "dajyu", english: "elder brother", hindi: "बड़ा भाई", pos: "noun", category: "kinship" },
    { kumaoni: "भुली", roman: "bhuli", english: "younger sister", hindi: "छोटी बहन", pos: "noun", category: "kinship" },
    { kumaoni: "पाणि", roman: "paani", english: "water", hindi: "पानी", pos: "noun", category: "food" },
    { kumaoni: "भात", roman: "bhaat", english: "cooked rice / food", hindi: "चावल / भात", pos: "noun", category: "food" },
    { kumaoni: "घाम", roman: "ghaam", english: "sunlight / sunshine", hindi: "धूप", pos: "noun", category: "nature" },
    { kumaoni: "जाड़", roman: "jaad", english: "cold / winter", hindi: "सर्दी", pos: "noun", category: "nature" },
    { kumaoni: "खाण", roman: "khaan", english: "to eat", hindi: "खाना", pos: "verb", category: "verbs" },
    { kumaoni: "जाण", roman: "jaan", english: "to go", hindi: "जाना", pos: "verb", category: "verbs" },
    { kumaoni: "घ्वड़ो", roman: "ghwado", english: "horse", hindi: "घोड़ा", pos: "noun", category: "animals" }
  ];

  function renderDictionary(words) {
    dictContainer.innerHTML = "";
    if (!words || words.length === 0) {
      dictContainer.innerHTML = `<div style="grid-column: 1/-1; text-align: center; color: #94a3b8; padding: 2rem;">No matching words found.</div>`;
      return;
    }
    words.forEach(w => {
      const card = document.createElement("div");
      card.className = "dict-card";
      card.innerHTML = `
        <div class="dict-word-kmy">${w.kumaoni}</div>
        <div class="dict-word-roman">${w.roman}</div>
        <div class="dict-meaning-en"><strong>EN:</strong> ${w.english}</div>
        <div class="dict-meaning-hi"><strong>HI:</strong> ${w.hindi}</div>
        <div class="dict-meta">${w.pos || "word"} &bull; ${w.category || "general"}</div>
      `;
      dictContainer.appendChild(card);
    });
  }

  renderDictionary(sampleWords);

  async function searchDict() {
    const q = dictSearchInput.value.trim();
    if (!q) {
      renderDictionary(sampleWords);
      return;
    }
    try {
      const resp = await fetch(`/api/lookup?q=${encodeURIComponent(q)}`);
      const data = await resp.json();
      const list = [];
      if (data.result) list.push(data.result);
      if (data.matches) list.push(...data.matches);
      renderDictionary(list);
    } catch (e) {
      console.error(e);
    }
  }

  btnDictSearch.addEventListener("click", searchDict);
  dictSearchInput.addEventListener("keyup", (e) => {
    if (e.key === "Enter") searchDict();
  });

  catChips.forEach(chip => {
    chip.addEventListener("click", () => {
      catChips.forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
      const cat = chip.getAttribute("data-cat");
      if (cat === "all") {
        renderDictionary(sampleWords);
      } else {
        renderDictionary(sampleWords.filter(w => w.category === cat));
      }
    });
  });

  // =========================================================
  // 3. VERB CONJUGATOR
  // =========================================================
  const btnConjugate = document.getElementById("btn-conjugate");
  const conjVerbSelect = document.getElementById("conj-verb-select");
  const conjTenseSelect = document.getElementById("conj-tense-select");
  const conjPersonSelect = document.getElementById("conj-person-select");
  const conjGenderSelect = document.getElementById("conj-gender-select");
  const conjOutputText = document.getElementById("conj-output-text");
  const conjExampleSentence = document.getElementById("conj-example-sentence");

  async function performConjugation() {
    const verb = conjVerbSelect.value;
    const tense = conjTenseSelect.value;
    const person = conjPersonSelect.value;
    const gender = conjGenderSelect.value;

    try {
      const resp = await fetch(`/api/conjugate?verb=${encodeURIComponent(verb)}&tense=${tense}&person=${person}&gender=${gender}`);
      const data = await resp.json();
      conjOutputText.textContent = data.result || "खान्छ";
      conjExampleSentence.textContent = `Conjugated form for ${verb} (${tense}, person ${person}, ${gender === "m" ? "masculine" : "feminine"})`;
    } catch (e) {
      console.error(e);
    }
  }

  btnConjugate.addEventListener("click", performConjugation);

  // =========================================================
  // 4. NUMBERS & NUMERALS
  // =========================================================
  const numInput = document.getElementById("num-input");
  const btnConvertNum = document.getElementById("btn-convert-num");
  const numResDevDigits = document.getElementById("num-res-dev-digits");
  const numResWords = document.getElementById("num-res-words");
  const numResRoman = document.getElementById("num-res-roman");
  const numResOrdinal = document.getElementById("num-res-ordinal");

  async function convertNumber() {
    const n = numInput.value || 0;
    try {
      const resp = await fetch(`/api/number?n=${n}`);
      const data = await resp.json();
      numResDevDigits.textContent = data.devanagari_numerals;
      numResWords.textContent = data.devanagari_words;
      numResRoman.textContent = data.romanized_words;
      numResOrdinal.textContent = data.ordinal;
    } catch (e) {
      console.error(e);
    }
  }

  btnConvertNum.addEventListener("click", convertNumber);
  numInput.addEventListener("keyup", (e) => {
    if (e.key === "Enter") convertNumber();
  });

  // =========================================================
  // 5. CULTURE & AKHAAN
  // =========================================================
  const btnNextProverb = document.getElementById("btn-next-proverb");
  const proverbText = document.getElementById("proverb-text");
  const proverbRoman = document.getElementById("proverb-roman");
  const proverbMeaning = document.getElementById("proverb-meaning");
  const proverbHindi = document.getElementById("proverb-hindi");
  const proverbEnglish = document.getElementById("proverb-english");

  async function loadRandomProverb() {
    try {
      const resp = await fetch("/api/proverb/random");
      const data = await resp.json();
      const p = data.proverb;
      if (p) {
        proverbText.textContent = p.kumaoni;
        proverbRoman.textContent = p.roman;
        proverbMeaning.textContent = p.figurative_meaning;
        proverbHindi.textContent = p.hindi_equivalent;
        proverbEnglish.textContent = p.english_equivalent;
      }
    } catch (e) {
      console.error(e);
    }
  }

  btnNextProverb.addEventListener("click", loadRandomProverb);

  // Riddles
  const btnNextRiddle = document.getElementById("btn-next-riddle");
  const btnRevealRiddle = document.getElementById("btn-reveal-riddle");
  const riddleText = document.getElementById("riddle-text");
  const riddleTranslation = document.getElementById("riddle-translation");
  const riddleAnswerBox = document.getElementById("riddle-answer-box");
  const riddleAnswer = document.getElementById("riddle-answer");

  async function loadRandomRiddle() {
    riddleAnswerBox.classList.add("hidden");
    try {
      const resp = await fetch("/api/riddle/random");
      const data = await resp.json();
      const r = data.riddle;
      if (r) {
        riddleText.textContent = r.riddle;
        riddleTranslation.textContent = r.english_translation;
        riddleAnswer.textContent = `${r.answer_kumaoni} (${r.answer_english})`;
      }
    } catch (e) {
      console.error(e);
    }
  }

  btnNextRiddle.addEventListener("click", loadRandomRiddle);
  btnRevealRiddle.addEventListener("click", () => {
    riddleAnswerBox.classList.toggle("hidden");
  });

  // Code Snippet Copy
  document.querySelectorAll(".btn-copy-code").forEach(btn => {
    btn.addEventListener("click", () => {
      const targetId = btn.getAttribute("data-target");
      const el = document.getElementById(targetId);
      if (el) {
        navigator.clipboard.writeText(el.innerText).then(() => {
          btn.textContent = "Copied!";
          setTimeout(() => btn.textContent = "Copy", 1500);
        });
      }
    });
  });
});
