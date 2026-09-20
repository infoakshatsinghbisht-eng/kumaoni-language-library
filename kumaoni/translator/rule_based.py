"""
Rule-based linguistic translator for English/Hindi <-> Kumaoni.
Uses phrasebook matching, POS-guided lexicon substitution, case marker adaptation, and SOV ordering.

Authentic Kumaoni grammar notes (sourced from kumauni.in & D.D. Sharma research):
- Copula forms: छ (is), छन (are), छूँ (I am), छा/छौ (you are), थो/थी (was)
- Possessives: मेरो/मेरि (my), तुमारो/तुमार (your), हमैरो/हमैरि (our), आपणो/आपणि (own)
- Negation: नि (not), used after verb stem or before copula; झनि (prohibitive imperative)
- Common particles: लै (also/too), त (then/emphasis), भौत (very/much)
- Postpositions: बटि (from/ablative), कणी (to/dative), म (in), पं (on), दगड़ (with)
- Progressive: verb-stem + लागूँ/लागी + copula
- Word order: Kumaoni uses SOV word order (Subject-Object-Verb)
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
            en_raw = p.get("english", "")
            en_clean = self._clean_key(en_raw)
            en_base = re.sub(r'\(.*?\)', '', en_raw).strip()
            en_base_clean = self._clean_key(en_base)
            
            hi_raw = p.get("hindi", "")
            hi_clean = self._clean_key(hi_raw)
            hi_base = re.sub(r'\(.*?\)', '', hi_raw).strip()
            hi_base_clean = self._clean_key(hi_base)
            
            kmy = p.get("kumaoni", "")
            if en_clean and en_clean not in self._en_phrases:
                self._en_phrases[en_clean] = kmy
            if en_base_clean and en_base_clean not in self._en_phrases:
                self._en_phrases[en_base_clean] = kmy
            if hi_clean and hi_clean not in self._hi_phrases:
                self._hi_phrases[hi_clean] = kmy
            if hi_base_clean and hi_base_clean not in self._hi_phrases:
                self._hi_phrases[hi_base_clean] = kmy

    @staticmethod
    def _clean_key(text: str) -> str:
        text = re.sub(r'[-_]', ' ', text)
        return re.sub(r'[^\w\s]', '', text).strip().lower()

    def translate_en_to_kmy(self, text: str) -> Tuple[str, float]:
        """
        Translates an English word or sentence into Kumaoni.
        Returns (kumaoni_translation, confidence_score).
        """
        clean_input = self._clean_key(text)
        if not clean_input:
            return text, 0.0
        
        # 1. Exact phrase match (highest priority)
        if clean_input in self._en_phrases:
            return self._en_phrases[clean_input], 1.0

        # 2. Exact dictionary lookup (including multi-word lexical entries like "paternal grandfather")
        w = self.lexicon.lookup(clean_input)
        if w:
            return w.kumaoni, 1.0

        # 3. High-priority greetings, Hinglish & conversational patterns
        if re.search(r'\b(?:hello|hi|hey|namaste)?\s*(?:aap|tum|tu)?\s*(?:kaise|kaisa|kaisi|kas|kasa)\s*(?:ho|hain|hai|chha|chho)\b', clean_input):
            return "कस छू तुम?", 0.98
        if re.search(r'\b(?:hello|hi|hey)\s+how\s+are\s+you\b', clean_input):
            return "पैलाग! कस छू तुम?", 0.98
        if re.search(r'\bhow\s+are\s+you\b', clean_input):
            return "कस छू तुम?", 0.98
        if clean_input in ("hello", "hi", "hey", "greetings", "namaste", "pailag", "pailaag"):
            return "पैलाग!", 0.98
        if re.search(r'\b(?:aapka|tumhara|tera)?\s*naam\s*kya\s*(?:hai|chha)\b', clean_input):
            return "तुमार नाम क्या छ?", 0.98
        if re.search(r'\b(?:kahan|kaha)\s*(?:ja\s*rahe|ho)\b', clean_input):
            return "कहाँ जाणा छा?", 0.98
        if re.search(r'\b(?:kya\s*kar\s*rahe)\b', clean_input):
            return "क्या करण लागी रया छा?", 0.98
        if re.search(r'\b(?:khana|bhaat)\s*(?:kha\s*liya|khaya)\b', clean_input):
            return "तुमले भात खै ल्ही?", 0.98
        if re.search(r'\b(?:main\s*theek|theek\s*hoon|sab\s*theek)\b', clean_input):
            return "मैं ठीक छूँ।", 0.98
        if re.search(r'\bhow\s+are\s+you\s+\(informal\)', clean_input) or re.search(r'\bhow\s+are\s+you\s+doing\b', clean_input):
            return "कस छे तू?", 0.96
        if re.search(r'\bwhat\s+is\s+your\s+name\b', clean_input):
            return "तुमार नाम क्या छ?", 0.98
        if re.search(r'\bwhat\s+is\s+this\b', clean_input):
            return "यो क्या छ?", 0.98
        if re.search(r'\bwhat\s+is\s+that\b', clean_input):
            return "त्यो क्या छ?", 0.98
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
        if re.search(r'\bwhat\s+(?:did\s+you|have\s+you)\s+eat(?:en)?\b', clean_input):
            return "तुमल क्या खायो?", 0.98
        if re.search(r'\bdid\s+you\s+eat\b', clean_input) or re.search(r'\bhave\s+you\s+eaten\b', clean_input):
            return "भात खायो?", 0.95
        if re.search(r'\bnice\s+to\s+meet\s+you\b', clean_input):
            return "तुज भेटक बढ़िया लागो।", 0.98
        if re.search(r'\bwhere\s+are\s+you\s+from\b', clean_input):
            return "तु कहाँ का छे?", 0.98
        if re.search(r'\bi\s+am\s+from\s+(.+)$', clean_input):
            p_match = re.search(r'from\s+(.+)$', clean_input)
            place = p_match.group(1).strip() if p_match else ""
            w_p = self.lexicon.lookup(place)
            p_kmy = w_p.kumaoni if w_p else place.capitalize()
            return f"मैं {p_kmy} सौं छुं।", 0.95
        if re.search(r'\bwhere\s+is\s+this\s+place\b', clean_input):
            return "यो ठाऊँ कहाँ छे?", 0.98
        if re.search(r'\bhow\s+far\s+is\s+this\s+place\b', clean_input):
            return "यो ठाऊँ कति दूर छे?", 0.98
        if re.search(r'\bwhich\s+way\s+should\s+i\s+go\b', clean_input):
            return "मैं कुन बाट जालुं?", 0.98
        if re.search(r'\bcome\s+here\b|\bcome\s+this\s+way\b', clean_input):
            return "एथर आ।", 0.98
        if re.search(r'\bgo\s+there\b|\bgo\s+that\s+way\b', clean_input):
            return "उथर जा।", 0.98
        if re.search(r'\bstand\s+up\b|\bget\s+up\b', clean_input):
            return "उठ जा।", 0.98
        if re.search(r'\bspeak\s+slowly\b', clean_input):
            return "धीरे बोल।", 0.98
        if re.search(r'\bwait\s+(?:for\s+)?(?:a\s+)?(?:while|minute|second)\b', clean_input):
            return "थोड़ी देर रूकी।", 0.98
        if re.search(r'\blet\s*s\s+go\b|\blets\s+go\b', clean_input):
            return "चाल, जालुं।", 0.98
        if re.search(r'\bi\s+love\s+you\b', clean_input):
            return "मैं तुझै प्रेम करनु छुं।", 0.98
        if re.search(r'\bi\s+miss\s+you\s+a\s+lot\b|\bi\s+miss\s+you\s+so\s+much\b', clean_input):
            return "मैं तुझै बहुत याद करनु छुं।", 0.98
        if re.search(r'\bi\s+miss\s+you\b', clean_input):
            return "मैं तुझै याद करनु छुं।", 0.98
        if re.search(r'\bi\s+am\s+happy\b', clean_input):
            return "मैं खुश छुं।", 0.98
        if re.search(r'\bi\s+am\s+sad\b|\bi\s+am\s+unhappy\b', clean_input):
            return "मैं दुखी छुं।", 0.98
        if re.search(r'\bi\s+am\s+hungry\b', clean_input):
            return "मैं भूखो छुं।", 0.98
        if re.search(r'\bi\s+am\s+thirsty\b', clean_input):
            return "मैं प्यासी छुं।", 0.98
        if re.search(r'\bi\s+am\s+tired\b', clean_input):
            return "मैं थक ग्ये छुं।", 0.98
        if re.search(r'\bi\s+am\s+scared\b|\bi\s+am\s+afraid\b', clean_input):
            return "मैं डर ग्ये छुं।", 0.98
        if re.search(r'\bi\s+am\s+angry\b', clean_input):
            return "मैं गुस्से मा छुं।", 0.98
        if re.search(r'\bi\s+am\s+busy\b', clean_input):
            return "मैं ब्यस्त छुं।", 0.98
        if re.search(r'\bi\s+(?:don\s*t|do\s+not)\s+understand\b', clean_input):
            return "मैं बुझ ना।", 0.98
        if re.search(r'\bi\s+(?:don\s*t|do\s+not)\s+know\b', clean_input):
            return "मैंकणी नी पत्त।", 0.98
        if re.search(r'\bwhat\s+(?:did\s+you|have\s+you)\s+eat(?:en)?\b', clean_input):
            return "तुमल क्या खायो?", 0.98
        if re.search(r'\bgive\s+me\s+food\b', clean_input):
            return "मणि खानो दे।", 0.98
        if re.search(r'\b(?:the\s+)?food\s+is\s+(?:tasty|delicious|good)\b', clean_input):
            return "खानो मिठो छु।", 0.98
        if re.search(r'\byou\s+are\s+(?:very\s+)?beautiful\b', clean_input):
            return "तू बढ़िया लागे।", 0.98
        if re.search(r'\byou\s+are\s+my\s+everything\b', clean_input):
            return "तू मेरु सब कुछ छुं।", 0.98
        if re.search(r'\byou\s+are\s+my\s+best\s+friend\b', clean_input):
            return "तू मेरु सबसे बढ़िया संगि छुं।", 0.98
        if re.search(r'\bour\s+friendship\s+is\s+forever\b', clean_input):
            return "हमारो दोस्ती हमेसा रैछ।", 0.98
        if re.search(r'\bhappy\s+birthday\b', clean_input):
            return "जन्मदिन को बहुत-बहुत शुभकामना!", 0.98
        if re.search(r'\bhappy\s+new\s+year\b', clean_input):
            return "नव बर्स की बधाइ छे!", 0.98
        if re.search(r'\bhappy\s+diwali\b|\bhappy\s+deepavali\b', clean_input):
            return "दीपावली की बधाइ छे!", 0.98
        if re.search(r'\bhappy\s+holi\b', clean_input):
            return "होली की शुभकामना!", 0.98
        if re.search(r'\bmay\s+your\s+life\s+be\s+filled\s+with\s+light\b', clean_input):
            return "तेरु जिंदगि रोशनी और खुशियों सौं भरि जै।", 0.98
        if re.search(r'\bmay\s+all\s+your\s+dreams\s+come\s+true\b', clean_input):
            return "तेरि सब सपना साचि हों।", 0.98
        if re.search(r'\bmay\s+you\s+have\s+a\s+long\s+and\s+happy\s+life\b', clean_input):
            return "तेरि उम्र लम्बी और खुशी रहै।", 0.98
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

        # Desiderative: "I want to eat food" / "I want to sleep" / "I want water"
        if re.search(r'\bi\s+want\s+water\b', clean_input):
            return "मैंकणी पाणि चाही।", 0.98
        if re.search(r'\bi\s+want\s+(?:food|rice|tea|money|help)\b', clean_input):
            obj_match = re.search(r'want\s+(\w+)', clean_input)
            obj = obj_match.group(1) if obj_match else "भात"
            w_obj = self.lexicon.lookup(obj)
            obj_kmy = w_obj.kumaoni if w_obj else obj
            return f"मैंकणी {obj_kmy} चाही।", 0.95
        if re.search(r'\bi\s+want\s+to\s+sleep\b', clean_input):
            return "मैं सुतण चाँछू।", 0.98
        if re.search(r'\bi\s+want\s+(?:to\s+)?(?:eat|have)\s+(?:food|rice)\b', clean_input):
            return "मैं भात खाण चाँछू।", 0.98
        if re.search(r'\bi\s+want\s+to\s+go\s+(?:home|village)\b', clean_input):
            return "मैं घर जाण चाँछू।", 0.98
        if re.search(r'\bi\s+want\s+to\s+go\b', clean_input):
            return "मैं जाण चाँछू।", 0.98
        if re.search(r'\bi\s+want\s+to\s+(\w+)', clean_input):
            v_match = re.search(r'want\s+to\s+(\w+)', clean_input)
            if v_match:
                v_stem = v_match.group(1)
                w_v = self.lexicon.lookup(v_stem)
                v_kmy = w_v.kumaoni if w_v else v_stem
                if not v_kmy.endswith("ण") and not v_kmy.endswith("न"):
                    v_kmy += "ण"
                return f"मैं {v_kmy} चाँछू।", 0.92

        # Ability / knowledge modal: "I can speak kumaoni" / "do you speak kumaoni"
        if re.search(r'\bi\s+(?:can\s+speak|know)\s+kumaoni\b', clean_input):
            return "मैं कुमाऊँनी बोलि सकूँछू।", 0.98
        if re.search(r'\b(?:do|can)\s+you\s+speak\s+kumaoni\b', clean_input):
            return "के तुम कुमाऊँनी बोलछा?", 0.98
        if re.search(r'\bi\s+can\s+walk\b', clean_input):
            return "मैं हिंडि सकूँछू।", 0.98

        # Obligation modal: "I have to go" / "you must work"
        if re.search(r'\bi\s+have\s+to\s+go\b|\bi\s+must\s+go\b', clean_input):
            return "मैंकणी जाण पडलो।", 0.98
        if re.search(r'\byou\s+(?:should|must)\s+work\b', clean_input):
            return "तुमकणी काम करण चाही।", 0.98

        # "Where is [item]?" / "Where is the [item]?" / "Where is my [item]?"
        where_match = re.search(r'where\s+is\s+(?:the\s+)?(.+?)(?:\?|$)', clean_input)
        if where_match:
            raw_item = where_match.group(1).strip()
            item_tokens = raw_item.split()
            translated_item_tokens = []
            for it in item_tokens:
                if it in ("my", "mine"):
                    translated_item_tokens.append("मेरो")
                elif it in ("your", "yours"):
                    translated_item_tokens.append("तुमार")
                elif it in ("our", "ours"):
                    translated_item_tokens.append("हमैरो")
                elif it in ("his", "her", "its"):
                    translated_item_tokens.append("उको")
                elif it in ("their", "theirs"):
                    translated_item_tokens.append("उनार")
                else:
                    w = self.lexicon.lookup(it)
                    translated_item_tokens.append(w.kumaoni if w else it)
            item_kmy = " ".join(translated_item_tokens)
            return f"{item_kmy} कहाँ छ?", 0.92

        # "How far is X?"
        how_far_match = re.search(r'how\s+far\s+is\s+(?:the\s+)?(.+?)(?:\?|$)', clean_input)
        if how_far_match:
            raw_place = how_far_match.group(1).strip()
            w = self.lexicon.lookup(raw_place)
            place_kmy = w.kumaoni if w else raw_place
            return f"{place_kmy} कतुक दूर छ?", 0.90

        # "How much does X cost?"
        if re.search(r'how\s+much\s+(does|is|costs?)', clean_input):
            return "यिको कतुक पैसा छ?", 0.90

        # Continuous / Progressive aspect patterns:
        # "I am going to school", "She is eating food", "They are playing"
        prog_match = re.search(r'\b(i|you|he|she|they|we)\s+(?:am|are|is)\s+(\w+ing)(?:\s+(.+))?$', clean_input)
        if prog_match:
            subj = prog_match.group(1)
            verb_ing = prog_match.group(2)
            remainder = prog_match.group(3) or ""
            
            # Subject map
            subj_map = {"i": "मैं", "you": "तुम", "he": "ऊ", "she": "ऊ", "they": "ऊँ", "we": "हम"}
            subj_kmy = subj_map.get(subj, "ऊ")
            
            # Copula ending for progressive
            cop_map = {"i": "छूँ", "you": "छा", "he": "छ", "she": "छे", "they": "छन", "we": "छूँ"}
            cop_kmy = cop_map.get(subj, "छ")
            
            # Base verb stem mapping
            base_verb = re.sub(r'ing$', '', verb_ing)
            verb_map = {
                "go": "जाण", "eat": "खाण", "drink": "पिण", "sleep": "सुतण", "speak": "बोलण",
                "read": "पडण", "write": "लिकण", "walk": "हिंण", "run": "धाण", "play": "खेलण",
                "sing": "गाण", "dance": "नाचण", "come": "औण", "do": "करण", "look": "देखण",
                "see": "देखण", "listen": "सुणण", "study": "पडण", "work": "काम करण", "liv": "रूण"
            }
            v_kmy = verb_map.get(base_verb)
            if not v_kmy:
                w_v = self.lexicon.lookup(base_verb)
                v_kmy = w_v.kumaoni if w_v else f"{base_verb}ण"
            
            # Remainder (objects, prepositional phrases)
            rem_words = [w for w in remainder.split() if w not in ("a", "an", "the", "to")]
            rem_kmy = []
            for rw in rem_words:
                w_r = self.lexicon.lookup(rw)
                rem_kmy.append(w_r.kumaoni if w_r else rw)
            
            rem_str = f" {' '.join(rem_kmy)}" if rem_kmy else ""
            return f"{subj_kmy}{rem_str} {v_kmy} लागूँ {cop_kmy}।", 0.92

        # Copular equatives: "This is my house", "The water is cold", "That is a tree"
        cop_match = re.search(r'\b(this|that|these|those|it)\s+is\s+(.+)$', clean_input)
        if cop_match:
            dem = cop_match.group(1)
            rest = cop_match.group(2).strip()
            dem_map = {"this": "यो", "that": "त्यो", "these": "यिन", "those": "उन", "it": "यो"}
            dem_kmy = dem_map.get(dem, "यो")
            
            rest_words = [w for w in rest.split() if w not in ("a", "an", "the")]
            rest_kmy = []
            for rw in rest_words:
                if rw in ("my", "mine"):
                    rest_kmy.append("मेरो")
                elif rw in ("your", "yours"):
                    rest_kmy.append("तुमार")
                elif rw in ("our", "ours"):
                    rest_kmy.append("हमैरो")
                elif rw in ("his", "her", "its"):
                    rest_kmy.append("उको")
                elif rw in ("their", "theirs"):
                    rest_kmy.append("उनार")
                else:
                    w = self.lexicon.lookup(rw)
                    rest_kmy.append(w.kumaoni if w else rw)
            return f"{dem_kmy} {' '.join(rest_kmy)} छ।", 0.90

        # Imperative commands: "give me water", "give me food"
        give_match = re.search(r'\bgive\s+me\s+(?:the\s+|a\s+|some\s+)?(.+?)$', clean_input)
        if give_match:
            item = give_match.group(1).strip()
            w_item = self.lexicon.lookup(item)
            item_kmy = w_item.kumaoni if w_item else item
            return f"मैंकणी {item_kmy} दिया।", 0.95

        # Habitual / Present tense: "we live in village", "i live in mountains"
        live_match = re.search(r'\b(i|we|they|he|she)\s+live\s+in\s+(?:the\s+)?(.+?)$', clean_input)
        if live_match:
            subj = live_match.group(1)
            place = live_match.group(2).strip()
            subj_map = {"i": "मैं", "we": "हम", "they": "ऊँ", "he": "ऊ", "she": "ऊ"}
            subj_kmy = subj_map.get(subj, "हम")
            verb_ending = "रूँछूँ" if subj in ("i", "we") else ("रूँछन" if subj == "they" else "रूँछ")
            w_place = self.lexicon.lookup(place)
            place_kmy = w_place.kumaoni if w_place else place
            return f"{subj_kmy} {place_kmy} म {verb_ending}।", 0.94

        # Substring phrase search (only if the phrase is long enough)
        for en_key, kmy_val in self._en_phrases.items():
            if len(en_key) > 5 and re.search(rf"\b{re.escape(en_key)}\b", clean_input):
                return kmy_val, 0.9

        # 4. Lexical word-by-word with SOV alignment
        raw_words = re.findall(r'\b\w+\b', text.lower())
        if not raw_words:
            return text, 0.0

        # Filter articles
        words = [w for w in raw_words if w not in ("a", "an", "the")]
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
            "you": "तुम", "your": "तुमार", "yours": "तुमार",
            "he": "ऊ", "him": "उकणी", "his": "उको",
            "she": "ऊ", "her": "उकि", "hers": "उकि",
            "they": "ऊँ", "them": "उनकणी", "their": "उनार", "theirs": "उनार",
            "it": "यो",
            # Demonstratives & locatives
            "this": "यो", "that": "त्यो", "these": "यिन", "those": "उन",
            "here": "याँ", "there": "वाँ",
            # Conjunctions
            "and": "र", "or": "या", "but": "पर", "because": "किलैकि",
            # Particles & postpositions
            "not": "नि", "no": "ना", "yes": "होय",
            "also": "लै", "too": "लै", "even": "लै",
            "very": "भौत", "much": "भौत", "many": "भौत",
            "with": "दगड़",
            "in": "म", "on": "पं", "from": "बटि", "to": "कणी", "for": "कणी",
            # Common verbs
            "eat": "खाण", "drink": "पिण", "go": "जाण", "come": "औण", "do": "करण",
            "speak": "बोलण", "listen": "सुणण", "see": "देखण", "look": "देखण",
            "read": "पडण", "write": "लिकण", "sleep": "सुतण", "sit": "बैठण",
            "walk": "हिंण", "run": "धाण", "give": "दिण", "take": "लिण",
            "know": "जाणण", "think": "सोचण", "stay": "रूण", "live": "रूण",
            "remain": "रूण", "meet": "मिलण", "laugh": "हाँसण", "cry": "रोण",
            "wake": "उठण", "rise": "उठण", "sing": "गाण", "play": "खेलण",
        }

        verb_set = {
            "eat", "drink", "go", "come", "do", "speak", "listen", "see", "look",
            "read", "write", "sleep", "sit", "walk", "run", "give", "take", "know",
            "think", "stay", "live", "remain", "meet", "laugh", "cry", "wake",
            "rise", "sing", "play"
        }

        prep_map = {
            "in": "म", "on": "पं", "from": "बटि", "with": "दगड़", "for": "कणी", "to": "कणी"
        }

        has_copula = False
        copula_val = "छ"

        i = 0
        n = len(words)
        while i < n:
            w = words[i]

            # Check for preposition + noun inversion (e.g. "in village" -> "गाँव म")
            if w in prep_map and i + 1 < n and words[i + 1] not in prep_map and words[i + 1] not in verb_set and words[i + 1] not in ("is", "are", "am", "was", "were"):
                prep_kmy = prep_map[w]
                next_w = words[i + 1]
                w_lookup = self.lexicon.lookup(next_w)
                next_kmy = w_lookup.kumaoni if w_lookup else gram_map.get(next_w, next_w)
                translated_tokens.append(next_kmy)
                translated_tokens.append(prep_kmy)
                matched_count += 2
                i += 2
                continue

            if w in ("is", "are", "am", "was", "were", "be"):
                has_copula = True
                if w == "am":
                    copula_val = "छूँ"
                elif w == "are":
                    copula_val = "छन"
                elif w == "was":
                    copula_val = "थो"
                elif w == "were":
                    copula_val = "था"
                else:
                    copula_val = "छ"
                matched_count += 1
                i += 1
                continue

            if w in gram_map:
                val = gram_map[w]
                if w in verb_set:
                    verbs.append(val)
                else:
                    translated_tokens.append(val)
                matched_count += 1
                i += 1
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
            i += 1

        # Place verbs & copula at end for SOV order
        translated_tokens.extend(verbs)
        if has_copula and not verbs:
            translated_tokens.append(copula_val)

        confidence = matched_count / max(1, len(words))
        return " ".join(translated_tokens), min(0.85, confidence)

    def translate_hi_to_kmy(self, text: str) -> Tuple[str, float]:
        """
        Translates a Hindi sentence into Kumaoni.
        Authentic Kumaoni forms based on linguistic research.
        """
        clean_input = self._clean_key(text)
        if not clean_input:
            return text, 0.0
        
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
