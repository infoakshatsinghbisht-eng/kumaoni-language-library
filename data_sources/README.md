# Kumaoni Digital Archive & Literary Source Repository

This directory archives historical, grammatical, and folkloric texts written in and about the **Kumaoni language (कुमाऊँनी)**, downloaded directly from the **Internet Archive** and public domain repositories. These primary sources serve as the authenticated foundation for the lexicon, grammar rules, proverbs, folk epics, and idioms in the `kumaoni` Python library.

---

## 📚 Downloaded Primary Source Books

| # | Book Title | Author / Editor | Year | Archive.org ID / Source | Source Size | Extracted Modules |
|---|------------|-----------------|------|----------------|-------------|-------------------|
| 1 | **Proverbs & Folklore of Kumaun and Garhwal** | Pandit Ganga Datt Upreti (Late Extra Asst Commissioner) | 1894 | `cu31924089930774` | 806 KB | Proverbs (`proverbs.json`), Folk Legends |
| 2 | **Linguistic Survey of India (Vol. IX, Part IV: Pahari Languages & Gujuri)** | Sir George Abraham Grierson, K.C.I.E. | 1916 | `in.ernet.dli.2015.32110` | 2.1 MB | Dialects, Postpositions, Auxiliary Verbs, Vocabulary |
| 3 | **Himalayan Folklore: Kumaon and West Nepal** | Rev. E. S. Oakley & Tara Dutt Gairola | 1935 | `in.ernet.dli.2015.532407` | 538 KB | Heroic Epics (*Kalu Bhandari*, *Ganganath*), Bards (*Hurkiyas*) |
| 4 | **Kumaoni Bhasha Aur Sahitya** | Dr. Trilochan Pandey (Foreword by Sumitranandan Pant) | 1977 | `nucr-kumaoni-bhasha-aur-sahitya-by-dr.-trilochan-pandey` | 1.5 MB | Vocabulary, Sensations, Idioms (`phrases.json`), Riddles (`riddles.json`) |
| 5 | **Ghughuti Basuti: Uttarakhand Ke Paramparik Balgeet** | Hem Pant (Samay Sakshya, Dehradun) | 2022 | `nejx_ghughuti-basuti...` | 56 KB | Children's Rhymes, Lullabies (`Ninuri`), Bird Ballads (*Kafal Pako*) |
| 6 | **Hill Dialects of the Kumaun Division** | Pandit Ganga Datt Upreti (Almora) | 1900 | `in.ernet.dli.2015.460831` | 498 KB | Comparative Pahari dialectology, Bhotia & Khas-Parjiya terms |
| 7 | **कुमाउनी भाषा साहित्य (AECC-K-101)** | Uttarakhand Open University, Haldwani | 2020 | UOU Syllabus Text (`AECC-K-101.pdf`) | 1.46 MB PDF / 558 KB text | 100+ Idioms (*Muhavare*), Proverbs, Riddles (*Aan*), Vocabulary |
| 8 | **वीर बालक हरु सिंह हीत** | खीमानन्द | Early 20th C. | Kumauni.in Digital Archives | 4.76 MB PDF | Classical folk epic ballad (*Haru Singh Heet*) |
| 9 | **मानिलै डानि** | हीरा सिंह राणा | 1980s | Kumauni.in Digital Archives | 44.3 MB PDF | Modern folk poetry & lyrical songs |
| 10 | **मन्खौं पड़्यौव मैं** | हीरा सिंह राणा | 1980s | Kumauni.in Digital Archives | 10.1 MB PDF | Modern Kumaoni poetry collection |
| 11 | **Kumaoni Master Bibliography (Verified v1)** | Digital Archives & Scholarly Catalogues | 2026 | Master Excel Dataset (`v1.xlsx`) | 92+ Records | Complete cataloguing of 114+ Kumaoni books (`bibliography.json`) |
| 12 | **Kumaoni Digital Heritage Corpus (v1)** | Digital Archives, Folk Recordings & Heritage Repositories | 2026 | `Kumaoni_Digital_Heritage_Corpus_v1.xlsx` | 33 KB Excel | 20 Folk Songs (`KSN-0001`..`20`), 20 Holi Songs (`KHL-0001`..`20`), 7 Digital Sources (`SRC-001`..`07`), 12 vocabulary terms |

---

## 🔍 Detailed Extraction Breakdown

### 1. Vocabulary & Specialized Lexicon (`kumaoni/lexicon/data/words.json`)
Extracted over **55 new high-precision base lemmas** across core cultural and topographical domains:
- **Mountain Hydrology & Landforms**:
  - `सिमार` (*simaar*): Marshy, fertile river valley wetland.
  - `बगड़` (*bagad*): Sandy/gravelly shore along a Himalayan river.
  - `गधेरा` (*gadhera*): Clear mountain rivulet fordable on foot.
  - `रोड` (*rod*): Swift torrential hill stream.
  - `खाल` (*khaal*): Ridge-top natural pool or meadow pond.
  - `काँठ` (*kaanth*): Lofty mountain crest / skyline ridge.
- **Traditional Hill Implements & Architecture**:
  - `चाख` (*chaakh*): Rotary stone handmill.
  - `जांतर` (*jaantar*): Watermill (*gharat*) powered by mountain brooks.
  - `उखल` (*ukhal*): Heavy stone mortar for paddy pounding.
  - `मुसळ` (*musal*): Iron-ringed wooden pestle.
  - `पाथर` (*paathar*): Mountain slate slabs used for cottage roofs.
  - `दथुड़ो` (*dathudo*): Curved hill sickle.
  - `स्यूँड़` (*syoon*): Large sewing needle for quilts and grain sacks.
  - `गागर` (*gaagar*): Hammered copper spring water vessel.
  - `फुंगइ` (*phungai*): Small brass/copper pitcher.
  - `छयो` (*chhayo*): Long wooden/metal ladle.
- **Traditional Agriculture & Grains**:
  - `पुंगरण` (*pungaran*): Sprouting of seedlings from the soil.
  - `बाखड़` (*baakhad*): Non-lactating dry period of cows or buffaloes.
  - `जुनाल` (*junaal*) / `ध्वाघ` (*dhwaagh*): Himalayan maize / corn cob.
  - `काकुनि` (*kaakuni*): Foxtail millet.
  - `बकौल` (*bakaul*): Uncultivated barren hill terrace.
  - `कणिक` (*kanik*): Broken rice grains / holy ceremonial grains.
  - `फिण` (*phin*) / `मौहट` (*mauhat*) / `मोष्ट` (*mosht*): Woven straw and hemp sitting mats.
  - `चूक` (*chook*): Traditional condensed mountain citrus syrup.
  - `किलमोड़ा` (*kilmoda*): Medicinal Himalayan barberry.
  - `हिसोलू` (*hisolu*): Golden yellow Himalayan raspberry.
- **Medical & Bodily Sensations** (Dr. Trilochan Pandey's classification of itching sensations):
  - `खाज` (*khaaj*): Pruritus from systemic disease or skin ailment.
  - `कन्या` (*kanya*): Itch from insect, flea, or bedbug bite.
  - `चिले` (*chile*): Irritation caused by grain husk dust on sweaty skin.
  - `कीक` (*keek*): Acrid irritation from raw taro/arbi root juice.
  - `खुजे` (*khuje*): Spontaneous tingling itch of unknown cause.
  - `बादुइ` (*baadui*): Hiccups traditionally believed to mean distant loved ones are reminiscing.
- **Folklore, Epics & Alpine Living**:
  - `हुड़किया` (*hurkiya*): Traditional hereditary bard singing epics with the *hurka* drum.
  - `पवाड़ो` (*pawaado*) / `भड़` (*bhad*): Heroic martial epic / chivalric warrior.
  - `डौँर` (*daunr*) & `थाली` (*thaali*): Sacred percussion instruments of spirit jagars.
  - `आंछरी` (*aanchhari*) & `मसाण` (*masaan*): Mountain fairies & cremation ghosts.
  - `शौका` (*shauka*), `हुणिया` (*huniya*), `लाप्चा` (*laapcha*): Johar valley borderland trade culture.
  - `थुलमा` (*thulma*), `चुटका` (*chutka*), `पंखी` (*pankhi*), `दन` (*dan*): High mountain woolen textiles.

---

### 2. Traditional Folk Proverbs (*Akhaan*) (`kumaoni/lexicon/data/proverbs.json`)
Added **20 authenticated proverbs** from Pt. Ganga Datt Upreti (1894) and Dr. Trilochan Pandey (1977), raising the library's total collection to **75 proverbs**:
- `गंगोली को लाटो, पंच बाण्ट खादी एक बाण्ट आटो।` (*The sharp wit of Gangoli: giving five measures of chaff and taking one of pure flour.*)
- `एक गोली का दुइ गोली द्यूँ, अलाई-बलाई शिरा पर ल्यूँ।` (*Why borrow one coin and pay back two, bringing servitude upon oneself?*)
- `सौ की सौ, बियाँ की नता।` (*All spent; not a single grain reserved for tomorrow's seed.*)
- `तीन बोलाया तेरह आया, देखो यांकी रीत। भैरा वाला खाई गया, घरा का गाणी गीत।` (*Uninvited freeloaders feast while the host is left hungry.*)
- `सराद लागा बामण जागा, सराद निमड़ा बामण चिमड़ा।` (*Opportunists flourish during feasts and vanish when work is needed.*)
- `ब्योल मरौ ब्योलि, दक्षिणा लिण म्यर काम।` (*Cold self-interest unconcerned with the client's genuine welfare.*)
- `पोथी न पातड़ी, नाम नरेण पंडित।` (*No book or knowledge, yet claiming the title of grand scholar.*)
- `खसियै की रीस, भैंस की तीस।` (*Fierce mountain anger flares suddenly and cools once justice is met.*)
- `गड़ा जामौ झौ, गौं पैठो सौ।` (*Invasive weeds in a field are as ruinous as a usurer in a hill hamlet.*)
- `जिमदार हुणि विचार ने, भैंस हुणि कच्यार ने।` (*Practical farmers prefer direct labor over theoretical pretense.*)
- `स्यापक जी ख्वार में, बणियक ढेपु में।` (*The snake values its head; the hoarder values his copper coins.*)
- `रणमुखी छत्री, तीरथमुखी बामण।` (*Each craftsperson finds honor in fulfilling their true calling.*)
- `हँसि हँसि ब्वारिल नौ रोटि खाती।` (*Consuming great wealth behind an innocent smile.*)
- `बगर्क देखि साग, स्यैणिक देखि बाघ।` (*Mountain rumors: overestimating forage and fearing imagined leopards.*)
- `धाण कर ब्वारी सगत न्हा, खाण हूँ आ ब्वारी ठूळ थालि कां?` (*Shunning difficult labor but foremost in line for the meal.*)
- `गौं बिगाड़ो राँड़, भात बिगाड़ो माँड़।` (*Slander ruins a village just as excess starch spoils cooked rice.*)
- `सौण भरी सासु, भदौ आए आँसु।` (*Delayed insincere mourning.*)
- `मुट्ठी को धन, मुख कि ज्वे।` (*Only what is directly in hand can be relied upon.*)
- `दाइ हुणि के पेट लुकौण।` (*Futile to hide symptoms from the doctor who must treat you.*)
- `जै बुड़ियाक दुखेल न्यार भे, ऊ म्यर बान आए।` (*Trying to escape a nuisance only to have the entire burden fall back on you.*)

---

### 3. Traditional Folk Riddles (*Aan / Aana*) (`kumaoni/lexicon/data/riddles.json`)
Added **12 authentic riddles** from Dr. Trilochan Pandey (1977) and Hem Pant (2022), raising the collection to **37 traditional riddles**:
- `ठेकि में ठेकि, बीचे में बैठो पिरमू नेगी।` -> **रिखु** (Sugarcane)
- `नान छना हरू छू, जवानी में लाल, बुड़ छना कालो भय, कर पंछी विचार।` -> **काफल** (Himalayan Bayberry)
- `खानू खानू सब कूनी, बीं हुणि धरौ क्वे नि कन।` -> **लूण** (Salt)
- `बारह बैणियाक एक्कै भाई।` -> **नारिङ** (Himalayan Orange)
- `नान नान मिरगा दास, लुकूड़ पेरों सौ पचास।` -> **प्याज** (Onion)
- `कालो बटु भितर पिङलो सुन, जो म्यार आण नि बताल ऊ हिरु डुन।` -> **भट्ट** (Black Soybean)
- `तू हिट मैं औनू।` -> **स्यूँड़ धाग** (Needle and Thread)
- `बणहुँ जाणतक झर-झर रौ, घर हूँ ऊण बखत चुपड़ रौ।` -> **गागर** (Water Pitcher)
- `एक चड़ि बुट्टेदार, जेका प्वाथ नौ हजार।` -> **माछ** (Fish with eggs)
- `एक मैस सवे-ब्याल सरग लखै रौ।` -> **उखल** (Stone Mortar)
- `आहार वाह, पीठ में पुछड़ धर यो तमासा काहाँ?` -> **तराजू** (Weighing Scale)
- `काली नथुली, सुकीली बिन्दी।` -> **तवा रोटी** (Griddle & Bread)

---

### 4. Folk Idioms (*Muhavare*) (`kumaoni/lexicon/data/phrases.json`)
Added **18 expressive folk idioms & traditional blessings** from Dr. Trilochan Pandey (1977):
- `ओली न्योली` (*Humble, courteous demeanor*)
- `अकाशचाणि` (*Gazing helplessly at the sky; destitute*)
- `किरमोली पाँख जामण` (*Ants growing wings; impending downfall of the conceited*)
- `खोरि मे खाइ खनण` (*Courting self-harm with one's own hands*)
- `खोरि फूटण` (*Head cracking; sudden misfortune*)
- `गाइ बगौण` (*Relinquishing all attachment into the river*)
- `घ्यू की अध्याणि` (*Living in luxurious feast*)
- `झट्योल जामण` (*Deserted homestead overgrown with weeds*)
- `ढुंग में धरण` (*Leaving someone stranded on a cold rock*)
- `तड़ि में तराण` (*Physical stamina and energy*)
- `धार में को दिन` (*Setting sun lingering on the ridge; closing years of life*)
- `नटोरी मारण` (*Snapping knuckles in contempt*)
- `फसक मारण` (*Boasting and tall tales*)
- `बकौल फुलण` (*Terraced land lying fallow*)
- `मुख म्बाल हालण` (*Throwing a net over someone's mouth; gagging/silencing*)
- `हाइ खकोलण` (*Washing ancestral bones in holy mountain confluences*)
- `जीरये जागि रये!` (*Traditional elder blessing: May you live long and remain prosperous!*)
- `लागि रौ भाल दिन!` (*May auspicious days shine upon you!*)

---

### 5. Monumental Epics, Poetry & Canonical Authors (`kumaoni/culture/literature.py`)
- **New Folk Epics**:
  - `kalu_bhandari` (*कालू भण्डारी की भड़*): The heroic martial ballad of the champion of Champawat and Kali Kumaon, documented in Oakley-Gairola (1935).
  - `ganganath` (*गंगनाथ जागर*): The sacred narrative of Prince Ganganath of Doti who became an immortal protector deity venerated across Almora and Katarmal.
- **New Folk Poem**:
  - `kafal_pako_geet` (*काफल पाको मिल नी चाखो*): The legendary mountain ritu-geet of the cuckoo and the ripened wild bayberry.
- **New Canonical Authors & Scholars**:
  - `tara_dutt_gairola` (1883 – 1940): Pioneer folklorist and co-author of *Himalayan Folklore* (1935).
  - `e_s_oakley` (1865 – 1944): Principal of Ramsay College Almora, editor of *Proverbs & Folklore of Kumaun* (1894), author of *Holy Himalaya* (1905).
  - `hem_pant` (Contemporary): Dedicated cultural researcher and compiler of *Ghughuti Basuti* (2022).

### 6. Digital Heritage Folklore & Musical Corpus (`kumaoni/culture/folklore.py`)
From `Kumaoni_Digital_Heritage_Corpus_v1.xlsx` and linked verified lyrics repositories:
- **20 Traditional & Recorded Songs (`KSN-0001` to `KSN-0020`)**:
  - Full authentic Devanagari lyrics and verses, Romanized transcription, English translation, and cultural context.
  - Classics include *Bedu Pako Baro Masa*, *Ghughuti Na Basa*, *Kafal Pako Chait*, *Maathu Maathu Hitaili Meri Baana*, *Yo Baato Ka Jaanya*, *Jhan Diya Bojyoon Chhaana Bilori*, *Jai Jai Ho Badri Nath Ke*, and legendary singer Gopal Babu Goswami's classics (*Kaile Baaji Muruli*, *Haay Teri Rumaala*, *Chhooti Ge Nainitaal*, *O Bhina Kasak*).
- **20 Classical Kumaoni Holi Songs (`KHL-0001` to `KHL-0020`)**:
  - Preserved across the 3 historical formats: *Baithaki Holi*, *Khadi Holi*, and *Mahila Holi*.
  - Rigorously mapped to classical Hindustani raags (*Khamaj*, *Kafi*, *Dhrupad/Dhamar*, *Desh/Sorath*, *Bhairavi*, *Pilu*, *Bihag*, *Yaman*, *Jhinjhoti*, *Kalyan*).
- **7 Digital Archival Repositories (`SRC-001` to `SRC-007`)**:
  - Live links and preservation statuses for *Kumauni Archives*, *Kumaoni Holi Archive*, *Kumauni.in*, *Uttarakhand Library Hub*, *Open Library*, *Google Books*, and *Creative Uttarakhand*.
- **12 New Lexical Additions**:
  - Terms added to `kumaoni/lexicon/data/words.json`: `मैता`, `हियो`, `नराई`, `जुन्याली`, `दगड़िया`, `बाना`, `जोबन`, `फाग`, `चीर`, `दमुवां`, `अबीर`, `चुनर`. Base dictionary expanded to **1,681 authenticated lemmas**.

---

## 🚀 Execution & Pipeline

To re-run the extraction and integration pipeline across raw texts, run:

```bash
# Books and textual corpus extraction:
python data_sources/extract_and_integrate.py

# Digital Heritage Excel and lyrics integration:
python data_sources/integrate_digital_heritage.py
```

This validates all JSON schemas, ensures zero lemma duplication, and links new entries into the dictionary lookup and morphological paradigms.
