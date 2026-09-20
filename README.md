# Kumaoni (कुमाऊँनी) Language Library for Python

[![Author & Creator](https://img.shields.io/badge/Author%20%26%20Creator-Akshat%20Singh%20Bisht-orange.svg?style=for-the-badge&logo=person)](https://akshatsinghbisht.com/)
[![Website](https://img.shields.io/badge/Official%20Website-akshatsinghbisht.com-blue?style=for-the-badge&logo=googlechrome&logoColor=white)](https://akshatsinghbisht.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/akshat-singh-bisht-digital-performance-marketing-specialist/)
[![ResearchGate](https://img.shields.io/badge/ResearchGate-Publications-00CCBB?style=for-the-badge&logo=researchgate&logoColor=white)](https://www.researchgate.net/profile/Akshat-Bisht-8)
[![Amazon Author](https://img.shields.io/badge/Amazon-Author%20Page-FF9900?style=for-the-badge&logo=amazon&logoColor=white)](https://www.amazon.com/stores/Akshat-Singh-Bisht/author/B0D5TYDT28?ref=sr_ntt_srch_lnk_1&qid=1789906571&sr=8-1&shoppingPortalEnabled=true)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/infoakshatsinghbisht-eng)
[![Lexicon Forms](https://img.shields.io/badge/Lexicon%20Forms-300%2C516%2B-success.svg?style=for-the-badge)](https://github.com/infoakshatsinghbisht-eng/kumaoni-language-library)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

A standard-library-style Python package for the **Kumaoni language** (कुमाऊँनी / Central Pahari). Designed to be as simple, fast, and comprehensive for Kumaoni as Python's built-in `math` library is for mathematics.

This library empowers developers to build **web applications, mobile apps, educational tools, chatbots**, and perform **universal translation from any language of the world into Kumaoni**.

> 📖 **Full Reference Manual**: Check out [DOCUMENTATION.md](file:///c:/Users/digit_lgfi273/OneDrive/Desktop/kumaoni%20language%20library/DOCUMENTATION.md) for the exhaustive guide, complete API references, grammatical rules, and application recipes.

---

## 🌟 Key Features

1. **Universal Multi-Language Translator**
   - Translate from **any world language** (English, French, Spanish, German, Japanese, Russian, Arabic, Hindi, Bengali, etc.) into Kumaoni.
   - Multi-tiered architecture: Offline rule-based engine + Zero-key universal world language bridge + Neural AI adapter (Gemini / OpenAI).

2. **Morphological Verb Conjugation Engine**
   - Automatically conjugates regular and irregular Kumaoni verbs (e.g., `खाण` to eat, `जाण` to go, `करन` to do).
   - Handles tenses (Present, Past, Future, Continuous), person (1st, 2nd, 3rd), gender (Masculine/Feminine), and honorific forms.
   - Auxiliary substantive verb (`छ-` / to be) conjugation.

3. **Kumaoni Numbers & Numerals**
   - Converts any integer (0 to 1,000,000,000+) to Kumaoni words in Devanagari or Romanized script.
   - Converts Kumaoni words back to numbers.
   - Supports ordinals (1st `पैलो`, 2nd `दुसर`, 3rd `तेसर`...), customary fractions (`आधो`, `पाव`, `पौण`, `सवा`, `डेढ़`), and Devanagari numerals (`०१२३४५६७८९`).

4. **100,000+ Words Morphological Paradigm Engine & Lemmatizer**
   - Synthesizes and indexes **300,000+ unique authenticated Kumaoni word forms** across verbal paradigms (Present, Past, Future, Continuous, Imperatives, Causatives, Participles, Agentives), nominal declensions (Direct, Plural, Oblique, Case postpositions bound/spaced, Diminutives, Echo words), and adjectival agreements.
   - Sub-millisecond `kumaoni.lemmatize()` and `kumaoni.analyze()` for inflected surface forms.
   - Seamless dictionary lookups: querying inflected forms like `खान्छू`, `ग्यूँ`, `ईजा कणी`, or `घरबटि` resolves directly to their base lemmas and definitions.

5. **Rich Lexicon & Dictionary (1,355+ Authenticated Base Lemmas)**
   - Search across Kumaoni, English, and Hindi.
   - Comprehensive vocabulary sourced from Grierson's *Linguistic Survey of India (Vol. IX, Part IV)*, Badri Datt Pande's *Kumaun ka Itihas (1937)*, Edwin T. Atkinson's *Himalayan Gazetteer*, Pt. Ganga Datt Upreti's *Hill Dialects of the Kumaun Division (1900)* & *Proverbs & Folklore of Kumaun (1894)*, Dr. Trilochan Pandey's *Kumaoni Bhasha Aur Sahitya (1977)* & *Kumaoni Lok-Sahitya ki Prushthbhoomi*, Dr. Gunanand Juyal's *Madhya Pahadi Bhasha (1967)*, and Hem Pant's *Ghughuti Basuti (2022)*.
   - Categorized by historical governance & land tenure (`बूढ़ा`, `स्याणा`, `कामीन`, `थोकदार`, `थातवान`, `खायकर`, `सिरतान`, `गूठ`, `रौत`, `सिरती`, `बैकर`, `कटक`), shamanic & sacred rituals (`जागरिया`, `डांगरिया`, `थात`, `डौँर`, `हुड़का`, `आंछरी`, `मसाण`), alpine pastoralism & high valleys (`छानि`, `खर्क`, `बुग्याल`, `शौका`, `रंग-भंग`, `झूलाघाट`, `लाप्चा`, `हुणिया`, `पिरुल`, `लिसो`), seasonal dynamics & climate (`ह्यूंद`, `रूड़ि`, `चौमास`, `बशगाल`, `शरद`, `ब्वार`, `तुसार`, `कुइड़ो`), traditional cuisine, handicrafts & textiles (`थुलमा`, `चुटका`, `पंखी`, `दन`), and traditional measurements.
   - Phonetic Latin transliteration and Devanagari script normalization.

6. **Cultural Treasury (अखाण, आणा, लोकगीत, महागाथा & साहित्य)**
   - **45+ Authentic Proverbs (*Akhaan*)**: Sourced from Pt. Ganga Datt Upreti's foundational compilation, Badri Datt Pande, Dr. Trilochan Pandey, and living hill tradition with literal, figurative, and parallel interpretations.
   - **75+ Authentic Conversational & Folk Phrases**: Traditional greetings, blessings (`जीरये जागि रये`), lullabies, travel advice, and everyday idioms.
   - **20+ Traditional Riddles (*Aan / Aana*)**: Engaging folk puzzles with hints and cultural context.
   - **6 Monumental Folk Epics & Ballads**: *Malushahi-Rajula*, *Ajuva Bafaul ki Bhad*, *Golu Devta Jagar*, *Jiya Rani ki Gatha* (The Warrior Queen of Katyur), *Veer Balak Haru Singh Heet*, and *Amar Gopichand Yogi*.
   - **6 Canonical Folk Poems & Songs**: *Bedu Pako Baro Masa*, *Malushahi Geet*, *Nyoli Lokgeet*, *Kalyug Varnan*, *Bajyaani Ka Dhur*, and *Ghughuti Basuti* (Traditional Lullaby & Nursery Rhymes).
   - **15+ Canonical Authors & Scholars**: Profiles and canonical works for Badri Datt Pande (*Kumaun ka Itihas*), Gumani Pant, Gaurda, Krishna Pandey (*Kalyug Varnan*), Pt. Ganga Datt Upreti (*Proverbs & Folklore*, *Hill Dialects*), Dr. Trilochan Pandey (*Kumaoni Bhasha aur Uska Sahitya*), Dr. Gunanand Juyal (*Madhya Pahadi Bhasha*), Thakur Dewan Singh Bisht (*Deewani Vinod*), Chintamani Paliwal (*Kumaun ke Samrat*), Dr. Pramila Joshi (*Bajyaani Ka Dhur*), Girish Tiwari 'Girda', Heera Singh Rana, Kabootari Devi, Mohan Upreti, and Dr. Charu Chandra Pande.
   - **Festivals & Almanac**: Traditional festivals (*Harela*, *Phool Dei*, *Ghughutiya*, *Olgia*, *Nanda Devi*, *Saatu-Aathu*, *Bhitauli*, *Khataduva*, *Bagwal*) and Kumaoni solar calendar months and seasons.

7. **Interactive Developer Playground & CLI**
   - Built-in command line interface (`kumaoni translate`, `kumaoni lookup`, `kumaoni number`).
   - Modern glassmorphism web playground running locally with zero dependencies.

---

## 🚀 Installation

Install via pip directly from PyPI:

```bash
pip install kumaoni
```

Or install from GitHub source in development mode:

```bash
git clone https://github.com/infoakshatsinghbisht-eng/kumaoni-language-library.git
cd kumaoni-language-library
pip install -e .
```

---

## 📖 Quickstart Guide

### 1. Universal Translation

```python
import kumaoni

# Translate from English to Kumaoni
result = kumaoni.translate("Where is the hospital?", source="en")
print(result)            # Output: अस्पताल कतुक दूर छ?
print(result.romanized)  # Output: Aspataal katuk door chha?

# Translate from any world language (e.g., French, Spanish, Hindi)
fr_result = kumaoni.translate("Comment allez-vous?", source="fr")
print(fr_result)         # Output: कस छू तुम?

hi_result = kumaoni.translate("मुझे पानी चाहिए।", source="hi")
print(hi_result)         # Output: मैंकणी पाणि चाही।
```

### 2. Verb Conjugator

```python
import kumaoni
from kumaoni.constants import Tense, Gender

# Conjugate 'जाण' (to go) in the past tense for 1st person
past_form = kumaoni.conjugate("जाण", tense=Tense.PAST, person=1, gender=Gender.MASCULINE)
print(past_form)  # Output: 'ग्यूँ' (I went)

# Conjugate 'खाण' (to eat) in the future tense
future_form = kumaoni.conjugate("खाण", tense=Tense.FUTURE, person=1)
print(future_form)  # Output: 'खालूँ' (I will eat)

# Auxiliary verb 'to be' (छ-)
is_form = kumaoni.conjugate_to_be(tense=Tense.PRESENT, person=3)
print(is_form)  # Output: 'छ' (is)

# Morphological Participles & Agent Nouns
print(kumaoni.conjunctive_participle("खाण"))  # 'खाईबेर' (having eaten)
print(kumaoni.agent_noun("गाण"))              # 'गाण्या' (singer)
print(kumaoni.imperative("औण", polite=True))  # 'आया' (please come)

# Causatives & Compound Verbs
print(kumaoni.causative("करण", degree=1))     # 'करौण' (to make someone do)
print(kumaoni.causative("खाण", degree=1))     # 'खिलाण' (to feed)
print(kumaoni.compound_verb("खाण", "हाल्ण"))  # 'खाईहाल्ण' (to eat up completely)

# Passive & Medio-Passive (Inability with -बटि)
print(kumaoni.passive("करण"))                 # 'कर्यो जान्छ' (is done)
print(kumaoni.medio_passive_inability("मैं", "हिंण")) # 'मैंबटि हिंड्यो नी जाँछ।'

# SOV Sentence Builder & Conditionals
sent = kumaoni.build_sentence(subject="राम", direct_object="भात", verb="खाण")
print(sent)  # 'राम भात खान्छ।'

cond = kumaoni.conditional("बरखा होली", "हम घर म रौला")
print(cond)  # 'जै बरखा होली, त हम घर म रौला।'

# Relative-Correlative Clauses (सम्बन्धवाचक रचना)
print(kumaoni.relative_correlative("मेहनत करलो", "फल पालो", marker_type="who"))
# Output: 'जो मेहनत करलो, सो फल पालो।'

# Prohibitive Commands (निषेधात्मक आज्ञा - झनि)
print(kumaoni.prohibitive("जाण", polite=True))  # 'झनि जाया' (Please do not go)
print(kumaoni.prohibitive("रोण", polite=True))  # 'झनि रोया' (Please don't cry)

# Modals: Ability, Obligation, and Desideratives
print(kumaoni.modal_ability("मैं", "हिंण"))           # 'मैं हिंडि सकन्छू।' (I can walk)
print(kumaoni.modal_obligation("तुम", "काम करण"))     # 'तुमकणी काम करण चाही।' (You should work)
print(kumaoni.modal_obligation("मैं", "जाण", strong=True)) # 'मैंकणी जाण पडलो।' (I will have to go)
print(kumaoni.modal_desiderative("मैं", "भात खाण"))  # 'मैं भात खाण चान्छू।' (I want to eat food)

# Interrogative Questions (प्रश्नवाचक रचना)
print(kumaoni.interrogative_sentence("कहाँ", subject="अस्पताल"))  # 'अस्पताल कहाँ छ?'
print(kumaoni.interrogative_sentence("क्या", subject="तुमार नाम")) # 'तुमार नाम क्या छ?'
```


### 3. Numbers & Devanagari Numerals

```python
import kumaoni

# Integer to Kumaoni words
print(kumaoni.num_to_words(42))                     # 'बयालीस'
print(kumaoni.num_to_words(108, script="latin"))     # 'ek sau aath'

# Ordinals & fractions
print(kumaoni.ordinal(1))                           # 'पैलो' (1st)
print(kumaoni.ordinal(2))                           # 'दुसर' (2nd)
print(kumaoni.fraction(1, 2))                       # 'आधो' (half)

# Devanagari numerals
print(kumaoni.to_devanagari_numerals(2026))         # '२०२६'
print(kumaoni.from_devanagari_numerals("२०२६"))       # 2026

# Words back to numbers
print(kumaoni.words_to_num("बयालीस"))                 # 42
```

### 4. Dictionary & Lexicon Search

```python
import kumaoni

# Exact lookup
word = kumaoni.lookup("ईजा")
print(f"{word.kumaoni} -> {word.english} ({word.hindi})")
# Output: 'ईजा -> mother (माँ)'

# Cross-language search
results = kumaoni.search("water")
for w in results:
    print(f"{w.kumaoni} ({w.roman}): {w.english}")
# Output: 'पाणि (paani): water'
```

### 5. Morphological Lemmatizer & Analyzer (200,000+ Words)

```python
import kumaoni

# Check total synthesized and indexed full-form vocabulary
print(kumaoni.total_word_forms())  # Output: 300,516+ words

# Lemmatize inflected verb forms, case-marked nouns, or postpositions
print(kumaoni.lemmatize("खान्छू"))    # 'खाण' (to eat)
print(kumaoni.lemmatize("जाँला"))     # 'जाण' (to go)
print(kumaoni.lemmatize("घरबटि"))     # 'घर' (house)
print(kumaoni.lemmatize("ईजा कणी"))   # 'ईजा' (mother)

# Deep morphological analysis (extracts tense, person, case, number, lemma)
analyses = kumaoni.analyze("खान्छू")
for a in analyses:
    print(f"Lemma: {a.lemma}, POS: {a.pos}, Tense: {a.tense}, Person: {a.person}, Number: {a.number}")
# Output: Lemma: खाण, POS: verb_finite, Tense: present, Person: 1, Number: sg

# Seamless dictionary lookup on inflected words
w = kumaoni.lookup("खान्छू")
print(f"Resolved to: {w.kumaoni} -> {w.english}")  # Resolved to: खाण -> to eat
```

### 6. Script & Phonetics

```python
import kumaoni

# Transliterate English phonetics to Devanagari
print(kumaoni.transliterate("Jai Dev, dajyu kas chou?", to_script="devanagari"))
# Output: 'जय देव, दाज्यू कस छौ?'

# Transliterate Devanagari to Romanized
print(kumaoni.transliterate("पैलाग भुली", to_script="latin"))
# Output: 'pailag bhuli'
```

### 7. Cultural Heritage, Literature & Folklore

```python
import kumaoni

# Access Folk Epics (Pauwada / Bhad)
malushahi = kumaoni.literature.get_epic("malushahi")
print(malushahi.title_kumaoni)        # 'राजुला मालूशाही'
print(malushahi.synopsis)

# Explore Traditional Valley Poetry (Nyoli / Jhora)
bedu_pako = kumaoni.literature.poems()[0]
print(bedu_pako.title_kumaoni)        # 'बेड़ू पाको बारह मासा'
print(bedu_pako.verses_kumaoni[0])    # 'बेड़ू पाको बारह मासा, ओ नरण काफल पाको चैत, मेरी छैला!'

# Canonical Kumaoni Authors & Poets (Gumani Pant, Gaurda, Dr. Charu Chandra Pande)
gumani = kumaoni.literature.get_author("gumani_pant")
print(f"{gumani.name_kumaoni} ({gumani.era}): {gumani.significance}")

# Random proverb (Akhaan) & riddle (Aana)
proverb = kumaoni.proverbs.random()
print("Akhaan:", proverb["kumaoni"], "->", proverb["figurative_meaning"])

riddle = kumaoni.riddles.random()
print("Aana:", riddle["riddle"], "-> Answer:", riddle["answer_kumaoni"])

# Traditional Kumaoni festival information
harela = kumaoni.festivals.get("harela")
print(harela.description)
```

---

## 📋 Comprehensive API Function Reference

All key functions are directly accessible via `import kumaoni`:

| Category | Function / Property | Description |
|---|---|---|
| **Translation** | `kumaoni.translate(text, source='en', target='kumaoni')` | Translate from 100+ world languages into Kumaoni. |
| **Voice & Speech** | `kumaoni.voice_translate(text, ...)` | Voice translation pipeline (text + IPA phonetic script + audio). |
| | `kumaoni.voice.phrases()` | Get categorized authentic conversational phrases. |
| **Dictionary & Search** | `kumaoni.lookup(word)` | Search base dictionary definitions (Kumaoni, Hindi, English). |
| | `kumaoni.search(query)` | Multi-result search in vocabulary database. |
| **Morphology (300k+ Forms)** | `kumaoni.lemmatize(word)` | Reduces inflected forms (`खान्छू`, `घरबटि`) to base dictionary lemma. |
| | `kumaoni.analyze(word)` | Deep grammatical analysis (POS, tense, case, gender, person). |
| | `kumaoni.total_word_forms()` | Count of indexed morphological forms (300,000+). |
| **Verb Conjugation** | `kumaoni.conjugate(verb, tense, person, ...)` | Conjugates verbs across Present, Past, Future, Continuous. |
| | `kumaoni.conjugate_to_be(tense, person, ...)`| Conjugates auxiliary substantive verb (`छ-` / to be). |
| | `kumaoni.imperative(verb, honorific=...)` | Forms imperative commands (`खा`, `खाओ`, `खाइये`). |
| | `kumaoni.causative(verb, degree=1)` | Forms 1st and 2nd degree causative verbs (`खवाण`, `खववाण`). |
| | `kumaoni.passive(verb, tense=...)` | Forms passive voice constructions. |
| | `kumaoni.conjunctive_participle(verb)` | Conjunctive participle 'having done' (`खाईकन`, `जाईकन`). |
| | `kumaoni.agent_noun(verb)` | Agentive noun 'the one who does' (`खन्या`, `जन्या`). |
| | `kumaoni.compound_verb(main, vector, ...)` | Aspectual compound verbs (`खा ल्हियो`). |
| | `kumaoni.prohibitive(verb, honorific=...)` | Negative prohibitive commands (`झन् खा`). |
| | `kumaoni.modal_ability(verb, subject=...)` | Modal ability 'can do' (`सकण`). |
| | `kumaoni.modal_obligation(verb, subject=...)`| Modal obligation 'must / should do' (`पड़ण`). |
| | `kumaoni.modal_desiderative(verb, ...)` | Modal desiderative 'wants to do' (`चाण`). |
| **Grammar & Syntax** | `kumaoni.build_sentence(sub, verb, obj, ...)`| Generates grammatically aligned SOV sentences. |
| | `kumaoni.conditional(cond, conseq)` | Conditional sentences (`अगर... तब...`). |
| | `kumaoni.relative_correlative(rel, corr)` | Relative-correlative clauses (`जो... सो...`). |
| | `kumaoni.interrogative_sentence(sub, ...)` | Question sentences (`कहाँ`, `कबे`, `क्योँ`, `को`). |
| | `kumaoni.echo_word(word)` | Reduplicative echo words (`भात-व़ात`, `किताब-सिताब`). |
| **Nouns & Declension** | `kumaoni.pluralize(noun, gender=...)` | Pluralizes nouns by declension class. |
| | `kumaoni.decline_noun(noun, case, ...)` | Declines nouns into grammatical cases. |
| | `kumaoni.to_oblique(noun, ...)` | Oblique stem for postpositions. |
| | `kumaoni.attach_case(noun, case, ...)` | Attaches vibhakti case markers to noun. |
| | `kumaoni.get_marker(case)` | Returns case marker postposition (`-ले`, `-कणी`, `-बटि`, `-म`). |
| | `kumaoni.get_pronoun(person, case, ...)` | Resolves personal pronouns across cases. |
| | `kumaoni.to_feminine(word)` / `to_masculine` | Converts gender forms of nouns/adjectives. |
| | `kumaoni.make_diminutive(noun)` | Diminutive affection forms (`गाड़` ➔ `गड्यूल`). |
| **Numbers & Fractions** | `kumaoni.num_to_words(number)` | Integer to Kumaoni words (`108` ➔ `'एक सौ आठ'`). |
| | `kumaoni.words_to_num(words)` | Kumaoni number words to integer. |
| | `kumaoni.to_devanagari_numerals(n)` | Converts number to Devanagari numerals (`२०२६`). |
| | `kumaoni.from_devanagari_numerals(s)` | Devanagari numerals back to integer. |
| | `kumaoni.ordinal(n)` | Ordinals (`पैलो`, `दुसर`, `तेसर`, `चौथ`). |
| | `kumaoni.fraction(val)` | Fractions (`आधो`, `पाव`, `सवा`, `डेढ़`, `ढाई`). |
| **Phonetics & Script** | `kumaoni.transliterate(text, to_script=...)`| Two-way Devanagari ↔ Latin/Roman transliteration. |
| | `kumaoni.devanagari_to_latin(text)` | Transliterates Devanagari into Latin phonetic script. |
| | `kumaoni.latin_to_devanagari(text)` | Converts Romanized Kumaoni input to Devanagari. |
| | `kumaoni.normalize(text)` | Normalizes Devanagari diacritics and nuktas. |
| | `kumaoni.detect_script(text)` | Detects `'devanagari'`, `'latin'`, or `'mixed'`. |
| | `kumaoni.tokenize(text)` / `syllables(text)`| Tokenizes words and splits phonetic syllables. |
| **Culture & Literature** | `kumaoni.proverbs.all()` / `.random()` | 45+ Proverbs (*Akhaan*) with literal & cultural meanings. |
| | `kumaoni.riddles.all()` / `.random()` | 20+ Traditional Riddles (*Aana*) with hints & answers. |
| | `kumaoni.phrases.all()` / `.random()` | 75+ Conversational phrases, idioms & blessings. |
| | `kumaoni.festivals.list()` / `.get(name)` | Festivals (*Harela*, *Phool Dei*, *Ghughutiya*, *Nanda Devi*). |
| | `kumaoni.literature.epics()` / `.get_epic(id)`| 6 Folk Epics (*Malushahi-Rajula*, *Jiya Rani*, *Golu Devta*). |
| | `kumaoni.literature.poems()` | Canonical Kumaoni poems & folk songs. |
| | `kumaoni.literature.authors()` / `.get_author(id)` | Biographies of 15+ canonical scholars & poets. |
| | `kumaoni.get_months()` / `get_seasons()` | Kumaoni solar calendar months & 6 traditional seasons. |
| | `kumaoni.get_current_season()` | Calculates active season for today's date. |

For exhaustive explanations and parameter details, see [DOCUMENTATION.md](file:///c:/Users/digit_lgfi273/OneDrive/Desktop/kumaoni%20language%20library/DOCUMENTATION.md).

---

## 💻 Command-Line Interface (CLI)

The library provides a CLI tool `kumaoni`:

```bash
# Translate text
kumaoni translate "Where does this road go?" --source en

# Dictionary lookup
kumaoni lookup "काफल"
kumaoni lookup "पिछौड़ा"

# Number to words
kumaoni number 108

# Verb conjugation
kumaoni conjugate "जाण" --tense past --person 1

# Random proverb / riddle
kumaoni proverb
kumaoni riddle
```

---

## 🖥️ Interactive Web Playground

Launch the interactive local web playground to test translation and explore the language in a browser:

```bash
python -m kumaoni.web.app 8080
```
Open [http://localhost:8080](http://localhost:8080) in your browser.

---

## 📂 Project Architecture

```
kumaoni/
├── __init__.py           # Unified top-level namespace (kumaoni.translate, literature, etc.)
├── constants.py          # Dialects, grammatical constants, solar calendar
├── phonetics.py          # Script transliteration, Devanagari normalizer
├── grammar/
│   ├── verbs.py          # Verb root extraction & conjugation engine
│   ├── nouns.py          # Noun morphology, pluralization, case declensions
│   ├── pronouns.py       # Pronoun tables across person, number, and case
│   └── postpositions.py  # Karaka markers (-ले, -कणी, -बटि, -म, etc.)
├── numbers/
│   └── converter.py      # Integer to words, ordinals, fractions, numerals
├── lexicon/
│   ├── dictionary.py     # Fast search across Devanagari, English, and Hindi
│   └── data/             # Curated JSON datasets (370+ words, phrases, Akhaan, Aana)
├── translator/
│   ├── engine.py         # Unified translation orchestrator
│   ├── rule_based.py     # Rule-based linguistic transfer & dialogue patterns
│   ├── pivot.py          # Universal multi-language bridge (Any Language -> Kumaoni)
│   └── llm_adapter.py    # Native Gemini/OpenAI neural integration
├── culture/
│   ├── festivals.py      # Cultural documentation (Harela, Phooldei, etc.)
│   ├── calendar.py       # Kumaoni solar months & seasons
│   └── literature.py     # Folk Epics (Malushahi, Bafaul), Nyoli, Jhora, Authors
├── cli.py                # Command-line interface
└── web/                  # Interactive developer playground
```

---

## 📚 Data Sources & Acknowledgments

This library synthesizes datasets and oral cultural heritage from:
- **eUttaranchal** (*Learn Kumaoni* linguistic lessons 1–3)
- **SpeakKumaoni** & **PahadiLingo** (Himalayan vocabulary & phonetic guides)
- **Kumauni Archives** & **Kumauni Culture** (Oral literature, e-books, e-magazines)
- **Linguistic Research**: Works of Dr. D.D. Sharma (*Linguistic Geography of Kumaun Himalayas*), Dr. Charu Chandra Pande, G.A. Grierson (*LSI*), Saraswati Kohli (*Kumaoni Kahavatein*), Gumani Pant, and Gaurda.

---

## 📜 License

MIT License &copy; 2026 Kumaoni Language Initiative. Open-source and free for all developers, linguists, and researchers.

---

## 👤 Author & Creator Profile

* **Creator & Author**: **Akshat Singh Bisht**
* **Official Website**: [https://akshatsinghbisht.com/](https://akshatsinghbisht.com/)
* **Email**: [infoakshatsinghbisht@gmail.com](mailto:infoakshatsinghbisht@gmail.com)
* **LinkedIn**: [Akshat Singh Bisht on LinkedIn](https://www.linkedin.com/in/akshat-singh-bisht-digital-performance-marketing-specialist/)
* **Amazon Author Profile**: [Akshat Singh Bisht on Amazon](https://www.amazon.com/stores/Akshat-Singh-Bisht/author/B0D5TYDT28?ref=sr_ntt_srch_lnk_1&qid=1789906571&sr=8-1&shoppingPortalEnabled=true)
* **ResearchGate**: [Akshat Bisht on ResearchGate](https://www.researchgate.net/profile/Akshat-Bisht-8)
* **GitHub**: [@infoakshatsinghbisht-eng](https://github.com/infoakshatsinghbisht-eng)
* **Kumaoni Repository**: [https://github.com/infoakshatsinghbisht-eng/kumaoni-language-library](https://github.com/infoakshatsinghbisht-eng/kumaoni-language-library)
* **Garhwali Repository**: [https://github.com/infoakshatsinghbisht-eng/garhwali-language-library](https://github.com/infoakshatsinghbisht-eng/garhwali-language-library)
* **Garhwali PyPI**: [https://pypi.org/project/garhwali/](https://pypi.org/project/garhwali/)

---

## 📄 License
This project is licensed under the **MIT License** — dedicated to the computational preservation, linguistic research, and cultural advancement of the Himalayan languages of Uttarakhand.
