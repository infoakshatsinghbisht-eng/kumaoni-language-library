# Kumaoni (कुमाऊँनी) Language Library — Complete Documentation Manual

Welcome to the definitive reference manual for the **Kumaoni Python Language Library (`kumaoni`)**.

This document covers everything you need to know about the library: background, architecture, installation, detailed module-by-module API guides with practical examples, and integration patterns.

---

## 📑 Table of Contents

1. [Introduction & Language Overview](#1-introduction--language-overview)
2. [Library Architecture & Philosophy](#2-library-architecture--philosophy)
3. [Installation & Setup](#3-installation--setup)
4. [Quick Start](#4-quick-start)
5. [Module Reference Guide](#5-module-reference-guide)
   - [5.1 Universal Translation Engine (`kumaoni.translate`)](#51-universal-translation-engine)
   - [5.2 Lexicon, Dictionary & 300k+ Morphological Analyzer (`kumaoni.lexicon`)](#52-lexicon-dictionary--300k-morphological-analyzer)
   - [5.3 Grammar & Syntax Engine (`kumaoni.grammar`)](#53-grammar--syntax-engine)
   - [5.4 Numbers, Customary Fractions & Numerals (`kumaoni.numbers`)](#54-numbers-customary-fractions--numerals)
   - [5.5 Script Conversion & Phonetics (`kumaoni.phonetics`)](#55-script-conversion--phonetics)
   - [5.6 Cultural Heritage, Literature & Folklore (`kumaoni.culture`)](#56-cultural-heritage-literature--folklore)
6. [Command-Line Interface (CLI)](#6-command-line-interface-cli)
7. [Interactive Web Playground](#7-interactive-web-playground)
8. [Real-World Application Recipes](#8-real-world-application-recipes)
9. [Primary Literature & Sources Ingested](#9-primary-literature--sources-ingested)
10. [Automated Testing & Verification](#10-automated-testing--verification)

---

## 1. Introduction & Language Overview

### What is Kumaoni?
**Kumaoni (कुमाऊँनी)** is a Central Indo-Aryan language belonging to the Northern Zone (Pahari) subgroup. It is the primary native tongue of the Kumaon division of Uttarakhand, India, spoken across the Himalayan districts of **Almora, Nainital, Pithoragarh, Bageshwar, Champawat, and Udham Singh Nagar**, as well as parts of Western Nepal.

- **ISO 639-3 Code**: `kfy`
- **Native Script**: Devanagari (देवनागरी)
- **Typology**: Subject-Object-Verb (SOV), agglutinative/inflectional postpositional system, split-ergative alignment in past tenses.

---

## 2. Library Architecture & Philosophy

The `kumaoni` library is built to act as a **Python standard-library-grade toolkit** for the language.

### Key Design Principles:
1. **Zero External Dependencies by Default**: Core features (dictionary, 300k+ morphology engine, grammar declensions, numbers, transliteration, local translation, folklore) run with 100% pure Python standard library.
2. **Authenticity First**: Every lemma, proverb, and rule is directly derived from authenticated historical texts, academic grammars, and living folklore. No artificial or hallucinated words.
3. **Sub-Millisecond Performance**: Full-form morphological corpora (300,000+ words) and dictionary searches resolve in under **0.5 milliseconds**.
4. **Universal Interoperability**: Translate between any language in the world and Kumaoni.

```
kumaoni/
├── __init__.py           # Unified top-level public API
├── constants.py          # Enums (Tense, Gender, Dialect), calendar constants
├── phonetics.py          # Devanagari <-> Latin transliteration & normalizer
├── numbers/              # Integer to words, customary fractions, ordinals, numerals
├── lexicon/              # 1,355+ lemmas, 300,500+ full-form corpus, Akhaan, Aana
│   ├── dictionary.py     # Lexicon search & lookup
│   ├── morphology.py     # FullFormCorpus & Morphological Analyzer
│   └── data/             # Curated JSON databases (words, proverbs, phrases, riddles)
├── grammar/              # Verbs, nouns, pronouns, postpositions, SOV syntax, modals
├── translator/           # Rule-based + Universal Pivot bridge + Neural AI adapter
├── culture/              # Epics, Folk Poetry, Canonical Authors, Solar Calendar & Festivals
├── cli.py                # Command-line interface
└── web/                  # Browser developer playground
```

---

## 3. Installation & Setup

### Requirements
- Python 3.8 or higher.

### Installation from PyPI
```bash
pip install kumaoni
```

### Development Installation from Source
Clone the repository and install in editable mode:
```bash
git clone https://github.com/infoakshatsinghbisht-eng/kumaoni-language-library.git
cd kumaoni-language-library
pip install -e .
```

---

## 4. Quick Start

```python
import kumaoni

# 1. Translate
result = kumaoni.translate("Where is the hospital?")
print(result.text)       # 'अस्पताल कहाँ छ?'
print(result.romanized)  # 'Aspataal kahan chha?'

# 2. Lemmatize inflected words (resolves to base dictionary entry)
print(kumaoni.lemmatize("खान्छू"))    # 'खाण' (to eat)
print(kumaoni.lemmatize("घरबटि"))     # 'घर' (house)

# 3. Conjugate verbs
print(kumaoni.conjugate("जाण", tense="past", person=1))  # 'ग्यूँ' (I went)

# 4. Numbers to Kumaoni words
print(kumaoni.num_to_words(108))  # 'एक सौ आठ'

# 5. Access Traditional Proverbs (Akhaan)
prov = kumaoni.proverbs.random()
print(f"{prov['kumaoni']} -> {prov['figurative_meaning']}")
```

---

## 5. Module Reference Guide

### 5.1 Universal Translation Engine

`kumaoni.translate(text, source='auto', target='kfy', method='auto')`

Translates text into Kumaoni using a multi-tiered architecture:
1. **Rule-Based Engine**: Handles direct idiomatic patterns, dialogue, and grammatical alignment.
2. **Pivot Bridge**: Translates from any world language (French, German, Spanish, Russian, Arabic, Japanese, etc.) via intermediate English/Hindi alignment.
3. **LLM Adapter**: Optional neural translation with Google Gemini or OpenAI.

#### Examples:
```python
import kumaoni

# English -> Kumaoni
print(kumaoni.translate("How are you?").text)
# Output: 'कस छू तुम?'

# Hindi -> Kumaoni
print(kumaoni.translate("मुझे पानी चाहिए।", source="hi").text)
# Output: 'मैंकणी पाणि चाही।'

# Spanish -> Kumaoni
print(kumaoni.translate("¿Dónde está el hospital?", source="es").text)
# Output: 'अस्पताल कहाँ छ?'

# French -> Kumaoni
print(kumaoni.translate("Comment vous appelez-vous?", source="fr").text)
# Output: 'तुमार नाम क्या छ?'

# Prohibitive Commands
print(kumaoni.translate("Don't go!").text)
# Output: 'झनि जाया!'
```

---

### 5.2 Lexicon, Dictionary & 300k+ Morphological Analyzer

The lexicon module provides instant lookup across **1,355+ authenticated base lemmas** and synthesizes **300,516+ unique inflected forms**.

#### Functions:
- `kumaoni.lookup(query)`: Exact lookup across Kumaoni (Devanagari), Romanized Latin, English, or Hindi. Resolves both base lemmas and inflected forms.
- `kumaoni.search(query, limit=15)`: Substring fuzzy search across all languages.
- `kumaoni.lemmatize(word)`: Extracts the base dictionary lemma for any inflected noun, verb, or postpositional construction.
- `kumaoni.analyze(word)`: Returns a structured `MorphAnalysis` object containing POS, tense, person, number, gender, case, and voice.
- `kumaoni.total_word_forms()`: Returns the total count of synthesized full-form words.

#### Examples:
```python
import kumaoni

# Total indexed vocabulary
print(kumaoni.total_word_forms())  # 300,516+ words

# Lookup base word
w = kumaoni.lookup("ईजा")
print(f"{w.kumaoni} | Roman: {w.roman} | English: {w.english} | Hindi: {w.hindi}")
# Output: 'ईजा | Roman: ija | English: mother | Hindi: माँ'

# Lookup inflected word (automatic lemmatization)
inflected = kumaoni.lookup("खान्छू")
print(f"Resolved to lemma: {inflected.kumaoni} ({inflected.english})")
# Output: 'Resolved to lemma: खाण (to eat)'

# Morphological analysis
analyses = kumaoni.analyze("खान्छू")
for a in analyses:
    print(f"Lemma: {a.lemma}, POS: {a.pos}, Tense: {a.tense}, Person: {a.person}, Number: {a.number}")
# Output: 'Lemma: खाण, POS: verb_finite, Tense: present, Person: 1, Number: sg'

# Cross-language search
results = kumaoni.search("brother")
for r in results:
    print(f"{r.kumaoni} ({r.roman}): {r.english}")
# Output:
# दाज्यू (dajyu): elder brother
# भै (bhai): younger brother
```

---

### 5.3 Grammar & Syntax Engine

#### 1. Verb Conjugation
`kumaoni.conjugate(verb, tense, person, gender, number, honorific)`

Handles regular and irregular verb roots across all standard tenses:
- **Tenses**: `Tense.PRESENT`, `Tense.PAST`, `Tense.FUTURE`, `Tense.PRESENT_CONTINUOUS`, `Tense.IMPERATIVE`

```python
from kumaoni.constants import Tense, Gender, GrammaticalNumber

# Irregular past tense for 'जाण' (to go)
print(kumaoni.conjugate("जाण", tense=Tense.PAST, person=1, gender=Gender.MASCULINE))  # 'ग्यूँ' (I went)
print(kumaoni.conjugate("जाण", tense=Tense.PAST, person=3, gender=Gender.MASCULINE))  # 'गयो' (He went)
print(kumaoni.conjugate("जाण", tense=Tense.PAST, person=3, gender=Gender.FEMININE))   # 'गै' (She went)

# Substantive Auxiliary 'छ-' (to be)
print(kumaoni.conjugate_to_be(tense=Tense.PRESENT, person=1))  # 'छूँ' (I am)
print(kumaoni.conjugate_to_be(tense=Tense.PRESENT, person=3))  # 'छ' (is)
print(kumaoni.conjugate_to_be(tense=Tense.PAST, person=3))     # 'थो' (was)
```

#### 2. Participles & Verbal Derivatives
```python
# Conjunctive participle (-बेर / -इबेर, equivalent to Hindi -कर)
print(kumaoni.conjunctive_participle("खाण"))  # 'खाईबेर' (having eaten)
print(kumaoni.conjunctive_participle("जाण"))  # 'जाईबेर' (having gone)
print(kumaoni.conjunctive_participle("करण"))  # 'करिबेर' (having done)

# Agentive Nouns (-ण्या, equivalent to Hindi -वाला)
print(kumaoni.agent_noun("गाण"))    # 'गाण्या' (singer)
print(kumaoni.agent_noun("बोलण"))  # 'बोलण्या' (speaker)

# Imperative Requests
print(kumaoni.imperative("खाण", polite=True))  # 'खाया' (Please eat)
print(kumaoni.imperative("औण", polite=True))   # 'आया' (Please come)
```

#### 3. Noun Morphology & Case System
`kumaoni.attach_case(noun, case_type)`

| Case | Marker (Devanagari) | Hindi Equivalent | Example | Meaning |
| :--- | :--- | :--- | :--- | :--- |
| **Ergative / Agentive** | `-ले` | ने | `रामले` | By Ram |
| **Dative / Accusative** | `-कणी`, `-कै`, `-हुणि` | को / के लिए | `ईजा कणी` | To mother |
| **Instrumental** | `-ले`, `-जरियाल` | से / द्वारा | `कलमले` | With a pen |
| **Ablative** | `-बटि`, `-हैं` | से (अलग होना) | `घरबटि` | From home |
| **Genitive** | `-को`, `-की`, `-का`, `-क` | का / की / के | `पहाड़क` | Of the hills |
| **Locative (In/On)** | `-म`, `-पं` | में / पर | `गाँव म` | In the village |
| **Sociative / Comitative**| `-दगड़`, `-दगड़े` | के साथ | `ईजा दगड़` | With mother |
| **Terminative** | `-तक`, `-तलक`, `-सम्म` | तक | `सांझ तक` | Until evening |
| **Superior Locative** | `-मायि`, `-मथि` | के ऊपर | `डाँड़ा मायि` | On top of the ridge |
| **Inferior Locative** | `-मुणि`, `-तलि` | के नीचे | `बोट मुणि` | Under the tree |

#### 4. Advanced Syntactic Constructs
```python
# Relative-Correlative Clauses (जो ... सो / जहाँ ... तहाँ / जब ... तबे)
print(kumaoni.relative_correlative("मेहनत करलो", "फल पालो", marker_type="who"))
# Output: 'जो मेहनत करलो, सो फल पालो।'

# Prohibitive Commands (निषेधात्मक आज्ञा - झनि)
print(kumaoni.prohibitive("जाण", polite=True))  # 'झनि जाया' (Please do not go)
print(kumaoni.prohibitive("रोण", polite=True))  # 'झनि रोया' (Please don't cry)

# Ability Modal (सकण)
print(kumaoni.modal_ability("मैं", "हिंण"))  # 'मैं हिंडि सकन्छू।' (I can walk)

# Obligation Modals (चाही / पडलो)
print(kumaoni.modal_obligation("तुम", "काम करण"))      # 'तुमकणी काम करण चाही।'
print(kumaoni.modal_obligation("मैं", "जाण", strong=True))  # 'मैंकणी जाण पडलो।'

# Desiderative (चाण - want to)
print(kumaoni.modal_desiderative("मैं", "भात खाण"))  # 'मैं भात खाण चान्छू।'

# Causatives Grade 1 & 2
print(kumaoni.causative("करण", degree=1))  # 'करौण' (to cause to do)
print(kumaoni.causative("करण", degree=2))  # 'करवाण' (to have done through someone)

# Passive & Medio-Passive Inability
print(kumaoni.passive("करण"))                        # 'कर्यो जान्छ' (is done)
print(kumaoni.medio_passive_inability("मैं", "हिंण")) # 'मैंबटि हिंड्यो नी जाँछ।'

# SOV Sentence Builder
sent = kumaoni.build_sentence(subject="राम", direct_object="भात", verb="खाण")
print(sent)  # 'राम भात खान्छ।'
```

---

### 5.4 Numbers, Customary Fractions & Numerals

Converts integers up to billions to authentic Kumaoni numbers, ordinals, and fractions.

```python
import kumaoni

# Integers to words
print(kumaoni.num_to_words(42))                     # 'बयालीस'
print(kumaoni.num_to_words(108, script="latin"))     # 'ek sau aath'

# Ordinals
print(kumaoni.ordinal(1))  # 'पैलो' (1st)
print(kumaoni.ordinal(2))  # 'दुसर' (2nd)
print(kumaoni.ordinal(3))  # 'तेसर' (3rd)

# Customary Fractions
print(kumaoni.fraction(1, 2))  # 'आधो' (half)
print(kumaoni.fraction(1, 4))  # 'पाव' (quarter)
print(kumaoni.fraction(3, 4))  # 'पौण' (three-quarters)
print(kumaoni.fraction(1, 1, 4))  # 'सवा' (one and a quarter)
print(kumaoni.fraction(1, 1, 2))  # 'डेढ़' (one and a half)

# Devanagari numerals
print(kumaoni.to_devanagari_numerals(2026))    # '२०२६'
print(kumaoni.from_devanagari_numerals("२०२६"))  # 2026
```

---

### 5.5 Script Conversion & Phonetics

```python
import kumaoni

# Latin to Devanagari
print(kumaoni.transliterate("Jai Dev, dajyu kas chou?", to_script="devanagari"))
# Output: 'जय देव, दाज्यू कस छौ?'

# Devanagari to Latin
print(kumaoni.transliterate("पैलाग भुली", to_script="latin"))
# Output: 'pailag bhuli'

# Devanagari normalizer (nuktas, zero-width joiners)
print(kumaoni.normalize("पढूँछ"))  # 'पढूँछ'
```

---

### 5.6 Cultural Heritage, Literature & Folklore

#### 1. Folk Epics (*Pauwada* / *Bhad* / *Jagar*)
```python
import kumaoni

# List all folk epics
for epic in kumaoni.literature.epics():
    print(f"{epic.title_kumaoni} ({epic.title_english}) - Region: {epic.region}")

# Detailed synopsis of Malushahi-Rajula
malu = kumaoni.literature.get_epic("malushahi")
print(malu.synopsis)
```

#### 2. Traditional Poetry & Ballads (*Nyoli*, *Jhora*, *Chhapeli*)
```python
# Access canonical songs
poems = kumaoni.literature.poems()
bedu_pako = poems[0]
print(bedu_pako.title_kumaoni)        # 'बेड़ू पाको बारह मासा'
print(bedu_pako.verses_kumaoni[0])    # 'बेड़ू पाको बारह मासा, ओ नरण काफल पाको चैत, मेरी छैला!'
print(bedu_pako.english_translation)
```

#### 3. Canonical Authors & Scholars
```python
# Access scholar profiles
for author in kumaoni.literature.authors():
    print(f"{author.name_kumaoni} ({author.name_english}) - Era: {author.era}")
```

#### 4. Proverbs (*Akhaan*) & Riddles (*Aana*)
```python
# Random proverb
akhaan = kumaoni.proverbs.random()
print(f"Proverb: {akhaan['kumaoni']}")
print(f"Meaning: {akhaan['figurative_meaning']}")
print(f"Context: {akhaan['context']}")

# Random riddle
aana = kumaoni.riddles.random()
print(f"Riddle: {aana['riddle']}")
print(f"Answer: {aana['answer_kumaoni']} ({aana['answer_english']})")
```

#### 5. Solar Calendar & Traditional Festivals
```python
# Kumaoni festivals
harela = kumaoni.festivals.get("harela")
print(f"Harela: {harela.description}")

# Months and seasons
print(kumaoni.culture.get_months())
# ['बैसाख', 'जेठ', 'अषाड़', 'सावण', 'भादव', 'असोज', 'कातिक', 'मंगसिर', 'पूस', 'माघ', 'फागुन', 'चैत']
```

---

## 6. Command-Line Interface (CLI)

The library provides a CLI tool `kumaoni`:

```bash
# 1. Translate
kumaoni translate "Where is the hospital?" --source en
kumaoni translate "मुझे पानी चाहिए।" --source hi

# 2. Dictionary lookup
kumaoni lookup "काफल"
kumaoni lookup "dajyu"

# 3. Numbers
kumaoni number 108
kumaoni number 2026 --script devanagari

# 4. Verb Conjugation
kumaoni conjugate "जाण" --tense past --person 1

# 5. Culture
kumaoni proverb
kumaoni riddle
```

---

## 7. Interactive Web Playground

Run a zero-dependency local web interface to test translation and explore vocabulary in your browser:

```bash
python -m kumaoni.web.app 8080
```
Open **[http://localhost:8080](http://localhost:8080)**.

---

## 8. Real-World Application Recipes

### Recipe 1: Building a FastAPI Translation Endpoint
```python
from fastapi import FastAPI
import kumaoni

app = FastAPI(title="Kumaoni Language API")

@app.get("/translate")
def translate_api(text: str, source: str = "en"):
    result = kumaoni.translate(text, source=source)
    return {
        "source_text": text,
        "source_lang": source,
        "kumaoni_devanagari": result.text,
        "kumaoni_romanized": result.romanized,
        "confidence": result.confidence
    }

@app.get("/lookup/{word}")
def lookup_api(word: str):
    res = kumaoni.lookup(word)
    if not res:
        return {"error": "Word not found"}
    return res.to_dict()
```

### Recipe 2: Linguistic Preprocessing & Lemmatizer Pipeline
```python
import kumaoni

def preprocess_kumaoni_corpus(sentence: str):
    tokens = sentence.replace("।", "").replace(",", "").split()
    lemmatized = [kumaoni.lemmatize(tok) for tok in tokens]
    return {
        "tokens": tokens,
        "lemmas": lemmatized,
        "analyses": [kumaoni.analyze(tok) for tok in tokens]
    }
```

---

## 9. Primary Literature & Sources Ingested

Every lexical entry, proverb, grammar rule, and folk narrative in this library is strictly sourced from:
1. **Pt. Ganga Datt Upreti** (1900): *Hill Dialects of the Kumaun Division*, Government Press.
2. **Pt. Ganga Datt Upreti** (1894): *Proverbs & Folklore of Kumaun and Garhwal*, Ludhiana Mission Press.
3. **Badri Datt Pande** (1937): *Kumaun ka Itihas* (कुमाऊँ का इतिहास), Almora.
4. **Dr. Trilochan Pandey** (1977): *Kumaoni Bhasha aur Uska Sahitya* (कुमाऊँनी भाषा और उसका साहित्य) & *Kumaoni Lok-Sahitya ki Prushthbhoomi*.
5. **Dr. Gunanand Juyal** (1967): *Madhya Pahadi Bhasha* (मध्य पहाड़ी भाषा).
6. **Sir George A. Grierson**: *Linguistic Survey of India (Vol. IX, Part IV: Central Pahari - Kumauni)*.
7. **Hem Pant** (2022): *Ghughuti Basuti* (Traditional Nursery Rhymes & Children's Literature).
8. **Dr. D.D. Sharma & Dr. Charu Chandra Pande**: *Linguistic Studies in Central Pahari*.

---

## 10. Automated Testing & Verification

Run the complete test suite:
```bash
python -m unittest discover tests
```
**Results**:
- 37 unit tests covering phonetics, morphology, dictionary lookups, verb conjugation, complex syntax, numerals, translation, and culture modules.
- **Pass rate**: 100% OK.
