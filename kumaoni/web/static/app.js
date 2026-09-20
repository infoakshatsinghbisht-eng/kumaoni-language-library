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

  // 1. Universal Translator
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
      metaConf.textContent = `Confidence: ${Math.round((data.confidence || 0.9) * 100)}%`;
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

  // Copy button
  btnCopyKmy.addEventListener("click", () => {
    const text = outputDev.textContent;
    navigator.clipboard.writeText(text).then(() => {
      btnCopyKmy.textContent = "✓";
      setTimeout(() => btnCopyKmy.textContent = "📋", 1500);
    });
  });

  // 2. Lexicon & Dictionary
  const dictSearchInput = document.getElementById("dict-search-input");
  const btnDictSearch = document.getElementById("btn-dict-search");
  const dictContainer = document.getElementById("dict-results-container");
  const catChips = document.querySelectorAll(".cat-chip");

  const sampleWords = [
    { kumaoni: "पैलाग", roman: "pailag", english: "traditional greeting (touching feet)", hindi: "प्रणाम / चरण स्पर्श", pos: "interjection", category: "greetings" },
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

  // 3. Verb Conjugator
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

  // 4. Numbers & Numerals
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

  // 5. Culture (Proverbs & Riddles)
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

  // Code Copy
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
