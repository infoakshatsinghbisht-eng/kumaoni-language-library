"""
Rule-based linguistic translator for English/Hindi <-> Kumaoni.
Uses phrasebook matching, POS-guided lexicon substitution, case marker adaptation, and SOV ordering.

Authentic Kumaoni grammar notes (sourced from kumauni.in & D.D. Sharma research):
- Copula forms: छ (is), छन (are), छूँ (I am), छौ (you are), थो/थी (was)
- Possessives: मेरो/मेरि (my), तुमारो (your), हमैरो/हमैरि (our), आपणो/आपणि (own)
- Negation: नि (not), used after verb stem
- Common particles: लै (also/too), त (then/emphasis), भौत (very/much)
- Postpositions: बटि (from/ablative), कणी (to/dative), म (in), पं (on), दगड़ (with)
- Progressive: verb-stem + लागूँ/लागी + छ (is happening)
- Dialect: Kumaoni uses SOV word order (Subject-Object-Verb)
"""

import re
from typing import Dict, List, Optional, Tuple
from kumaoni.lexicon.dictionary import get_lexicon, Word
from kumaoni.phonetics import devanagari_to_latin, normalize_devanagari


class RuleBasedTranslator:
    def __init__(self):
        self.lexicon = get_lexicon()
        self._build_phrase_cache()

    def _build_phrase_cache(self):
        self._en_phrases: Dict[str, str] = {}
        self._hi_phrases: Dict[str, str] = {}
        
        for p in self.lexicon.get_phrases():
            en_clean = self._clean_key(p["english"])
            hi_clean = self._clean_key(p["hindi"])
            self._en_phrases[en_clean] = p["kumaoni"]
            self._hi_phrases[hi_clean] = p["kumaoni"]

    @staticmethod
    def _clean_key(text: str) -> str:
        return re.sub(r'[^\w\s]', '', text).strip().lower()

    def translate_en_to_kmy(self, text: str) -> Tuple[str, float]:
        """
        Translates an English sentence into Kumaoni.
        Returns (kumaoni_translation, confidence_score).
        """
        clean_input = self._clean_key(text)
        
        # 1. Exact phrase match (highest priority)
        if clean_input in self._en_phrases:
            return self._en_phrases[clean_input], 1.0

        # 2. High-priority greetings & conversational patterns
        if clean_input in ("hello", "hi", "hey", "greetings", "namaste"):
            return "पैलाग / नमस्कार!", 0.98
        if re.search(r'\bhow\s+are\s+you\b', clean_input):
            return "कस छू तुम?", 0.98
        if re.search(r'\bhow\s+are\s+you\s+\(informal\)', clean_input) or re.search(r'\bhow\s+are\s+you\s+doing\b', clean_input):
            return "कस छे तू?", 0.96
        if re.search(r'\bwhat\s+is\s+your\s+name\b', clean_input):
            return "तुमार नाम क्या छ?", 0.98
        if "good morning" in clean_input:
            return "शुभ बिहान!", 0.98
        if "good night" in clean_input:
            return "शुभ राति!", 0.98
        if "good evening" in clean_input:
            return "शुभ साँझ!", 0.98
        if "thank you" in clean_input or "thanks" in clean_input:
            return "धन्यवाद!", 0.98
        if "welcome" in clean_input:
            return "स्वागत छ!", 0.95
        if re.search(r'\bi\s+am\s+fine\b', clean_input) or re.search(r'\bi\s+am\s+good\b', clean_input) or re.search(r'\bi\s+am\s+okay\b', clean_input):
            return "मैं ठीक छूँ।", 0.98
        if re.search(r'\bi\s+need\s+help\b', clean_input):
            return "मैंकणी मदद चाही।", 0.98
        if "goodbye" in clean_input or "bye" in clean_input or "see you" in clean_input:
            return "फिर मिलुला!", 0.95
        if "take care" in clean_input:
            return "आपणी खैरियत रख्या।", 0.95
        if re.search(r'\bcome\s+inside\b', clean_input) or re.search(r'\bplease\s+come\s+in\b', clean_input):
            return "भितर आ जाओ।", 0.95
        if re.search(r'\bplease\s+sit\b', clean_input) or re.search(r'\bsit\s+down\b', clean_input):
            return "बैठो!", 0.95
        if "drink water" in clean_input:
            return "पाणि पिओ।", 0.95
        if re.search(r'\bdid\s+you\s+eat\b', clean_input) or re.search(r'\bhave\s+you\s+eaten\b', clean_input):
            return "भात खायो?", 0.95
        if re.search(r'\bwhere\s+do\s+you\s+live\b', clean_input) or re.search(r'\bwhere\s+are\s+you\s+from\b', clean_input):
            return "तुम कहाँ रैंछा?", 0.95
        if re.search(r'\bmy\s+name\s+is\b', clean_input):
            name_match = re.search(r'\bmy\s+name\s+is\s+(\w+)', clean_input)
            if name_match:
                return f"मेरो नाम {name_match.group(1)} छ।", 0.95
            return "मेरो नाम... छ।", 0.90
        if re.search(r'\btoday\s+is\s+very\s+cold\b', clean_input):
            return "आज भौत जाड़ छ।", 0.98
        if re.search(r'\bit\s+is\s+raining\b', clean_input) or "raining" in clean_input:
            return "बरखा लागूँ छे।", 0.95
        if re.search(r'\bit\s+is\s+sunny\b', clean_input) or "sunny" in clean_input:
            return "घाम लागूँ छ।", 0.95
        if re.search(r'\bhow\s+are\s+other\s+members\b|\bhow\s+is\s+everyone\s+at\s+home\b', clean_input):
            return "घर पं सब कस छन?", 0.98
        if re.search(r'\beveryone\s+is\s+fine\b|\ball\s+are\s+fine\b', clean_input):
            return "सब ठीक छन।", 0.98
        if re.search(r'\bwhat\s+are\s+you\s+doing\s+these\s+days\b|\bwhat\s+are\s+you\s+doing\s+nowadays\b', clean_input):
            return "तुम अच्याल कि करनो छा?", 0.98
        if re.search(r'\bi\s+am\s+studying\s+in\s+school\b|\bi\s+study\s+in\s+school\b', clean_input):
            return "मैं स्कूल म पडूँ छूँ।", 0.98
        if re.search(r'\bwhere\s+is\s+your\s+village\b', clean_input):
            return "तुमार गाँव कहाँ छ?", 0.98
        if re.search(r'\bmy\s+village\s+is\s+in\s+(?:the\s+)?mountains\b|\bmy\s+village\s+is\s+in\s+pahaad\b', clean_input):
            return "मेरो गाँव पहाड़ म छ।", 0.98
        if re.search(r'\bhow\s+many\s+brothers\s+and\s+sisters\b', clean_input):
            return "तुम कतुक भाई-बैणी छा?", 0.98
        if re.search(r'\bmy\s+father\s+serves\s+in\s+(?:the\s+)?army\b|\bmy\s+father\s+is\s+in\s+army\b', clean_input):
            return "मेर बाबु फौज म नौकरी करैनी।", 0.98
        if re.search(r'\bwhere\s+does\s+this\s+road\s+go\b', clean_input):
            return "यो बाटो कहाँ जाँछ?", 0.98
        if re.search(r'\bhave\s+you\s+ever\s+been\s+to\b', clean_input):
            place_match = re.search(r'been\s+to\s+([\w\s]+?)(?:\?|$)', clean_input)
            place = place_match.group(1).strip() if place_match else "नैनीताल"
            return f"तुम कभै {place.capitalize()} गया छा?", 0.95
        if re.search(r'\bis\s+there\s+electricity\s+in\s+your\s+village\b', clean_input):
            return "तुमार गाँव म बिजली छ?", 0.98
        if re.search(r'\bself[- ]reliance\s+is\b|\bour\s+own\s+hands\b', clean_input):
            return "आपण हाथ जगन्नाथ।", 0.98
        if "our language" in clean_input:
            return "हमैरि बोलि", 0.95
        if "our identity" in clean_input:
            return "हमैरि पछ्याण", 0.95

        # Prohibitive imperative: "don't go" / "do not do" / "don't cry"
        if re.search(r'\b(?:do\s+not|dont|don\s*t)\s+go\b', clean_input):
            return "झनि जाया!", 0.98
        if re.search(r'\b(?:do\s+not|dont|don\s*t)\s+do\b', clean_input):
            return "झनि करा!", 0.98
        if re.search(r'\b(?:do\s+not|dont|don\s*t)\s+cry\b', clean_input):
            return "झनि रोया!", 0.98
        if re.search(r'\b(?:do\s+not|dont|don\s*t)\s+eat\b', clean_input):
            return "झनि खाया!", 0.98
        if re.search(r'\b(?:do\s+not|dont|don\s*t)\s+speak\b', clean_input):
            return "झनि बोला!", 0.98

        # Desiderative: "I want to eat food" / "I want to go" / "I want water"
        if re.search(r'\bi\s+want\s+(?:to\s+)?(?:eat|have)\s+(?:food|rice)\b', clean_input):
            return "मैं भात खाण चाँछू।", 0.98
        if re.search(r'\bi\s+want\s+to\s+go\s+(?:home|village)\b', clean_input):
            return "मैं घर जाण चाँछू।", 0.98
        if re.search(r'\bi\s+want\s+to\s+go\b', clean_input):
            return "मैं जाण चाँछू।", 0.98
        if re.search(r'\bi\s+want\s+water\b', clean_input):
            return "मैंकणी पाणि चाही।", 0.98

        # Ability modal: "I can speak kumaoni" / "can you speak"
        if re.search(r'\bi\s+can\s+speak\s+kumaoni\b', clean_input) or re.search(r'\bi\s+know\s+kumaoni\b', clean_input):
            return "मैं कुमाऊँनी बोलि सकूँछू।", 0.98
        if re.search(r'\bcan\s+you\s+speak\s+kumaoni\b', clean_input):
            return "तुम कुमाऊँनी बोलि सकछा?", 0.98
        if re.search(r'\bi\s+can\s+walk\b', clean_input):
            return "मैं हिंडि सकूँछू।", 0.98

        # Obligation modal: "I have to go" / "you must work"
        if re.search(r'\bi\s+have\s+to\s+go\b|\bi\s+must\s+go\b', clean_input):
            return "मैंकणी जाण पडलो।", 0.98
        if re.search(r'\byou\s+(?:should|must)\s+work\b', clean_input):
            return "तुमकणी काम करण चाही।", 0.98

        # "Where is the X?"
        where_match = re.search(r'where\s+is\s+(?:the\s+)?([\w\s]+?)(?:\?|$)', clean_input)
        if where_match:
            item = where_match.group(1).strip()
            w = self.lexicon.lookup(item.split()[0])
            item_kmy = w.kumaoni if w else item
            return f"{item_kmy} कहाँ छ?", 0.92

        # "How far is X?"
        how_far_match = re.search(r'how\s+far\s+is\s+(?:the\s+)?([\w\s]+?)(?:\?|$)', clean_input)
        if how_far_match:
            item = how_far_match.group(1).strip()
            w = self.lexicon.lookup(item.split()[0])
            item_kmy = w.kumaoni if w else item
            return f"{item_kmy} कतुक दूर छ?", 0.90

        # "How much does X cost?"
        if re.search(r'how\s+much\s+(does|is|costs?)', clean_input):
            return "यिको कतुक पैसा छ?", 0.90

        # 3. Substring phrase search (only if the phrase is long enough)
        for en_key, kmy_val in self._en_phrases.items():
            if len(en_key) > 5 and re.search(rf"\b{re.escape(en_key)}\b", clean_input):
                return kmy_val, 0.9

        # 4. Lexical word-by-word with SOV alignment
        words = re.findall(r'\b\w+\b', text.lower())

        if not words:
            return text, 0.0

        translated_tokens = []
        verbs = []
        matched_count = 0

        # Comprehensive pronouns, auxiliaries & common word map
        gram_map = {
            # Pronouns
            "i": "मैं", "me": "मैंकणी", "my": "मेरो", "mine": "मेरो",
            "we": "हम", "us": "हमकणी", "our": "हमैरो", "ours": "हमैरो",
            "you": "तुम", "your": "तुमारो", "yours": "तुमारो",
            "he": "ऊ", "him": "उकणी", "his": "उको",
            "she": "ऊ", "her": "उकि", "hers": "उकि",
            "they": "ऊँ", "them": "उनकणी", "their": "उनार", "theirs": "उनार",
            "it": "यो",
            # Demonstratives & locatives
            "this": "यो", "that": "त्यो", "these": "यिन", "those": "उन",
            "here": "याँ", "there": "वाँ",
            # Copula
            "is": "छ", "are": "छन", "am": "छूँ", "be": "छ",
            "was": "थो", "were": "था",
            # Particles & postpositions
            "not": "नि", "no": "ना", "yes": "होय",
            "also": "लै", "too": "लै", "even": "लै",
            "very": "भौत", "much": "भौत", "many": "भौत",
            "with": "दगड़",
            "in": "म", "on": "पं", "from": "बटि", "to": "कणी", "for": "कणी",
            # Common nouns
            "water": "पाणि", "food": "भात", "rice": "भात",
            "tea": "चाहा", "bread": "रोटी", "milk": "दूध",
            "mother": "ईजा", "father": "बाबु",
            "brother": "दाज्यू", "sister": "भुली",
            "son": "च्याल", "daughter": "चेलि",
            "grandfather": "बूबू", "grandmother": "आमा",
            "friend": "दगड़ि", "person": "आदिमि",
            "child": "नान्तिन", "children": "नान्तिन",
            "house": "घर", "home": "घर", "village": "गाँव",
            "road": "बाटो", "path": "बाटो",
            "mountain": "पहाड़", "river": "गाड़", "tree": "रुख",
            "sky": "अगास", "sun": "घाम", "snow": "ह्यूँ",
            "water": "पाणि", "rain": "बरखा", "wind": "हवा",
            "language": "बोलि", "culture": "संस्कृति",
            "identity": "पछ्याण", "tradition": "परम्परा",
            "song": "गीत",
            "work": "काम", "money": "पैसा", "school": "स्कूल",
            "hospital": "अस्पताल", "shop": "दुकान",
            "book": "किताब", "pen": "कलम",
            # Adjectives
            "good": "भाल", "bad": "खराब",
            "cold": "जाड़", "hot": "तातो", "warm": "तातो",
            "big": "ठूलो", "small": "छोटो", "little": "नान",
            "new": "नयो", "old": "पुरो",
            "beautiful": "सुन्दर", "clean": "चोखो", "dirty": "मैलो",
            "sweet": "मीठो", "spicy": "चर्को",
            "black": "कालो", "white": "गोरो",
            "red": "रातो", "green": "हरियो", "blue": "नीलो",
            # Common verbs (infinitive-ish mapping)
            "eat": "खाण", "eating": "खाण लागूँ छ",
            "drink": "पिण", "drinking": "पिण लागूँ छ",
            "go": "जाण", "going": "जाण लागूँ छ",
            "come": "औण", "coming": "औण लागूँ छ",
            "do": "करण", "doing": "करण लागूँ छ",
            "speak": "बोलण", "speaking": "बोलण लागूँ छ",
            "listen": "सुणण", "see": "देखण", "look": "देखण",
            "read": "पडण", "write": "लिकण",
            "sleep": "सुतण", "sleeping": "सुतण लागूँ छ",
            "sit": "बैठण", "walk": "हिंण", "run": "धाण",
            "give": "दिण", "take": "लिण",
            "know": "जाणण", "think": "सोचण",
            "stay": "रूण", "live": "रूण", "remain": "रूण",
            "meet": "मिलण", "laugh": "हाँसण", "cry": "रोण",
            "wake": "उठण", "rise": "उठण",
        }

        for w in words:
            if w in gram_map:
                # Check if it's a verb-progressive (contains छ)
                val = gram_map[w]
                if "छ" in val and " " in val:
                    # Progressive form — keep as is
                    verbs.append(val)
                elif w in ("eat", "drink", "go", "come", "do", "speak", "listen",
                           "see", "look", "read", "write", "sleep", "sit", "walk",
                           "run", "give", "take", "know", "think", "stay", "live",
                           "remain", "meet", "laugh", "cry", "wake", "rise"):
                    verbs.append(val)
                else:
                    translated_tokens.append(val)
                matched_count += 1
                continue
            lookup_res = self.lexicon.lookup(w)
            if lookup_res:
                if lookup_res.pos == "verb":
                    verbs.append(lookup_res.kumaoni)
                else:
                    translated_tokens.append(lookup_res.kumaoni)
                matched_count += 1
            else:
                translated_tokens.append(w)

        # Place verbs at end for SOV order
        translated_tokens.extend(verbs)
        confidence = matched_count / max(1, len(words))
        return " ".join(translated_tokens), min(0.85, confidence)

    def translate_hi_to_kmy(self, text: str) -> Tuple[str, float]:
        """
        Translates a Hindi sentence into Kumaoni.
        Authentic Kumaoni forms based on linguistic research.
        """
        clean_input = self._clean_key(text)
        
        # 1. Exact phrase match
        if clean_input in self._hi_phrases:
            return self._hi_phrases[clean_input], 1.0

        for hi_key, kmy_val in self._hi_phrases.items():
            if hi_key in clean_input or clean_input in hi_key:
                return kmy_val, 0.9

        # 2. Morphological, lexical, and postposition substitutions
        # Ordered from most specific (longer patterns) to least specific
        res = text
        substitutions = [
            # Greetings
            (r'नमस्ते|प्रणाम|नमस्कार', 'पैलाग'),
            # Questions
            (r'आप कैसे हैं|तुम कैसे हो', 'कस छू तुम?'),
            (r'तू कैसा है|तू कैसी है', 'कस छे तू?'),
            (r'आपका नाम क्या है|तुम्हारा नाम क्या है|आपका नाम क्या छ', 'तुमार नाम क्या छ?'),
            (r'मैं ठीक हूँ', 'मैं ठीक छूँ।'),
            (r'हमारी भाषा|हमारी बोली', 'हमैरि बोलि'),
            # Modals & Desires & Needs
            (r'मुझे पानी चाहिए|मुझे जल चाहिए', 'मैंकणी पाणि चाही।'),
            (r'मुझे खाना चाहिए|मुझे भोजन चाहिए', 'मैंकणी भात चाही।'),
            (r'मुझे मदद चाहिए|मेरी सहायता करो', 'मैंकणी मदद चाही।'),
            (r'मत जाओ|मत जाइए', 'झनि जाया!'),
            (r'मत करो|मत करिए', 'झनि करा!'),
            (r'मत रोओ|मत रोइए', 'झनि रोया!'),
            (r'मैं जा रहा हूँ|मैं जा रही हूँ', 'मैं जाण लागूँ छूँ।'),
            (r'कहाँ जा रहे हो|कहाँ जा रहे हैं', 'कहाँ जाणा छा?'),
            # Common words (long first to avoid partial matches)
            (r'\bमेरा नाम\b', 'मेरो नाम'),
            (r'\bहमारा\b|\bहमारी\b', 'हमैरो'),
            (r'\bअपना\b|\bअपनी\b', 'आपणो'),
            (r'\bकहाँ है\b|\bकहाँ हैं\b', 'कहाँ छ?'),
            # Kinship terms
            (r'\bमाताजी\b|\bमाँ\b|\bअम्मा\b', 'ईजा'),
            (r'\bपिताजी\b|\bपापा\b|\bबाप\b', 'बाबु'),
            (r'\bबड़े भाई\b|\bभैया\b', 'दाज्यू'),
            (r'\bछोटे भाई\b|\bछोटा भाई\b', 'भै'),
            (r'\bबड़ी बहन\b|\bदीदी\b', 'दीदी'),
            (r'\bछोटी बहन\b', 'भुली'),
            (r'\bदादाजी\b|\bनाना\b', 'बूबू'),
            (r'\bदादीजी\b|\bनानी\b', 'आमा'),
            (r'\bबेटा\b|\bपुत्र\b', 'च्याल'),
            (r'\bबेटी\b|\bपुत्री\b', 'चेलि'),
            (r'\bबच्चे\b|\bबच्चों\b', 'नान्तिन'),
            (r'\bचाचा\b|\bकाका\b', 'काका'),
            (r'\bदोस्त\b|\bसाथी\b|\bमित्र\b', 'दगड़ि'),
            # Nature / food
            (r'\bपानी\b|\bजल\b', 'पाणि'),
            (r'\bखाना\b|\bभोजन\b|\bचावल\b|\bभात\b', 'भात'),
            (r'\bचाय\b|\bचाहा\b', 'चाहा'),
            (r'\bघोड़ा\b', 'घ्वड़ो'),
            (r'\bधूप\b|\bसूरज की रोशनी\b', 'घाम'),
            (r'\bसर्दी\b|\bठंड\b|\bठंडक\b', 'जाड़'),
            (r'\bबरसात\b|\bबारिश\b|\bवर्षा\b', 'बरखा'),
            (r'\bपेड़\b|\bवृक्ष\b', 'रुख'),
            (r'\bआकाश\b|\bआसमान\b', 'अगास'),
            (r'\bबर्फ\b|\bहिम\b', 'ह्यूँ'),
            (r'\bरोशनी\b|\bउजाला\b', 'उज्याव'),
            (r'\bभाषा\b|\bबोली\b', 'बोलि'),
            (r'\bपहचान\b', 'पछ्याण'),
            (r'\bसंस्कृति\b', 'संस्कृति'),
            (r'\bपरम्परा\b|\bपरंपरा\b', 'परम्परा'),
            (r'\bगाना\b|\bगीत\b', 'गीत'),
            (r'\bबाजार\b', 'बजार'),
            (r'\bरास्ता\b|\bराह\b', 'बाटो'),
            # Postpositions (must come after noun replacements)
            (r'\bघर से\b', 'घरबटि'),
            (r'\bसे\b', 'बटि'),
            (r'\bको\b', 'कणी'),
            (r'\bके साथ\b|\bके संग\b', 'दगड़'),
            (r'\bमें\b', 'म'),
            (r'\bपर\b', 'पं'),
            (r'\bके लिए\b', 'कणी'),
            # Copula / verb forms
            (r'\bहै\b', 'छ'),
            (r'\bहैं\b', 'छन'),
            (r'\bथा\b', 'थो'),
            (r'\bथी\b', 'थी'),
            (r'\bथे\b', 'था'),
            (r'\bहूँ\b', 'छूँ'),
            (r'\bहो\b', 'छौ'),
            # Common verb replacements
            (r'\bजाता है\b|\bजाती है\b', 'जाँछ'),
            (r'\bखाता है\b|\bखाती है\b', 'खान्छ'),
            (r'\bआता है\b|\bआती है\b', 'औंछ'),
            (r'\bरहता है\b|\bरहती है\b', 'रूंछ'),
            (r'\bबोलता है\b|\bबोलती है\b', 'बोलण्छ'),
            # Adverbs & particles
            (r'\bबहुत\b', 'भौत'),
            (r'\bभी\b', 'लै'),
            (r'\bअब\b', 'आब'),
            (r'\bतब\b', 'ताब'),
            (r'\bआज\b', 'आज'),
            (r'\bकल\b', 'ब्याल'),
            (r'\bनहीं\b|\bनही\b', 'नि'),
            (r'\bहाँ\b|\bजी\b', 'होय'),
            (r'\bकब\b', 'कब'),
            (r'\bकहाँ\b', 'कहाँ'),
            (r'\bकैसे\b|\bकैसा\b', 'कस'),
            (r'\bकितना\b|\bकितने\b', 'कतुक'),
            (r'\bक्यों\b', 'किलै'),
            (r'\bकौन\b', 'को'),
            (r'\bक्या\b', 'कि'),
        ]

        changed = False
        for pat, rep in substitutions:
            if re.search(pat, res):
                res = re.sub(pat, rep, res)
                changed = True

        res = re.sub(r'[।\.]+\s*[।\.]+', '।', res)
        res = re.sub(r'!\s*[।\.]', '!', res)
        res = re.sub(r'\?\s*[।\.]', '?', res)

        return res.strip(), 0.85 if changed else 0.5
