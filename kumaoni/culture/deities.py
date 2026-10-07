"""
Local deities (लोक देवता एवं देवियाँ) of Kumaon.

Includes:
- Golu Devta (God of Justice)
- Nanda Devi & Sunanda Devi (Patron Goddess of Kumaon)
- Bholanath (Defender of the Oppressed)
- Ganganath (Yogi Prince Protector)
- Kalbisht / Kaluwa (Guardian of Cattle & Shepherds)
- Airy Devta (God of the Hunt and Forest Ridges)
- Chaumu Devta (Protector of Domestic Animals)
- Kailpal (Territorial Boundary Guardian)
- Barahi Devi (Goddess of Devidhura & Bagwal)
- Purnagiri (Sacred Shaktipeeth of Tanakpur)
- Kasar Devi (Ancient Cave Shrine of Almora)
- Jhula Devi (Goddess of Bells & Wishes, Chaubattia)
- Lakhia Bhoot (Mahadev's Attendant & Hero of Hillyatra)
- Haru Devta (Brother of Golu & Benevolent Guardian)
- Sem Mukhem / Nagaraja (Divine Serpent Guardian of Waters)
- Kotgari Devi (Supreme Court of Last Resort, Pankhu)
- Chhurmal Devta (Guardian of Trans-Himalayan Alpine Passes)
- Balchan Devta (Youthful Warrior Guardian Spirit)
- Dhannar Devta (Martial Hero of Kali Kumaon)
- Malushahi & Rajula (Deified Folk Heroes)
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict


@dataclass
class KumaoniDeity:
    id: str
    name_kumaoni: str
    name_roman: str
    title: str
    category: str  # "Nyaya Devta", "Kuldevi / Shakti", "Kshetrapal", "Gram Devta", "Jagar Deity"
    primary_shrines: List[str]
    iconography_and_symbols: str
    legend: str
    invocation_or_jagar: str
    cultural_role: str


DEITIES_DATA: Dict[str, KumaoniDeity] = {
    "golu_devta": KumaoniDeity(
        id="golu_devta",
        name_kumaoni="गोलू देवता (गोरिल)",
        name_roman="Golu Devta (Goril)",
        title="न्याय के देवता (Supreme God of Justice & Righteousness)",
        category="Nyaya Devta",
        primary_shrines=["चितई (अल्मोड़ा)", "घोड़ाखाल (नैनीताल)", "चम्पावत", "ताड़ीखेत (रानीखेत)"],
        iconography_and_symbols="Riding a white horse, holding a bow and arrow, adorned with thousands of hanging brass bells and written stamp-paper petitions.",
        legend="Son of King Jhalu Rai and Queen Kalinka of Champawat. His seven jealous stepmothers cast the newborn infant into the river in an iron box. Raised miraculously by a fisherman, the boy later proved his mother's virtue to the king with a wooden horse drinking water at the royal well. He became an avatar of Lord Shiva and sworn protector of the innocent.",
        invocation_or_jagar="जय गोलू देवता चितई वाला, धौला घोड़ा को असवार! न्याय करो महाराज, दुखियारी की पुकार सुणो!",
        cultural_role="Revered throughout Kumaon as the supreme dispenser of rapid cosmic justice. Worshippers submit handwritten legal affidavits and letters on stamp paper to his temple court; when prayers are answered, brass bells of gratitude are tied."
    ),
    "nanda_devi": KumaoniDeity(
        id="nanda_devi",
        name_kumaoni="नंदा देवी एवं सुनंदा देवी",
        name_roman="Nanda Devi & Sunanda Devi",
        title="कूर्मांचल की कुलदेवी एवं इष्टदेवी (Patron Mother Goddess of Kumaon)",
        category="Kuldevi / Shakti",
        primary_shrines=["अल्मोड़ा (नंदा देवी मंदिर)", "नैनीताल", "रणचुलाहाट / कोट भ्रामरी (कत्यूर)", "नंदा देवी पर्वत"],
        iconography_and_symbols="Two sister idols fashioned from banana tree trunks, draped in Rangwali Pichhauda, holding lotus blossoms and tridents.",
        legend="Nanda is the beloved daughter of the Himalayas (Haimavati/Parvati) and sovereign tutelary deity of both the Katyuri and Chand dynasties. She visits her maternal home (Maita) every autumn during the festival of Nanda Ashtami and returns to her consort Shiva on the snow peaks of Mount Nanda Devi (7,816 m).",
        invocation_or_jagar="नमो नंदा दुर्गे, हिमाल की धिया! अल्मोड़ा का कोट म विराजित, सब कणी आशीष दिया माँ!",
        cultural_role="The spiritual mother and emotional anchor of all Kumaoni people. Commemorated through monumental fairs in Almora and Nainital and the twelve-yearly 280-km barefoot trek of Nanda Raj Jaat."
    ),
    "bholanath": KumaoniDeity(
        id="bholanath",
        name_kumaoni="भोलानाथ",
        name_roman="Bholanath",
        title="दीन-दुखियों के रक्षक (Guardian of the Oppressed & Incarnation of Shiva)",
        category="Gram Devta",
        primary_shrines=["अल्मोड़ा (भोलानाथ मंदिर)", "कत्यूर घाटी", "पाली पछाऊँ"],
        iconography_and_symbols="Iron trident (trishul), bronze bell, sacred ash (vibhuti), and iron lamp.",
        legend="Folk history identifies him with an elder prince of the Chand dynasty who was disinherited and assassinated by palace schemers alongside his pregnant wife. Deified as an incarnation of Lord Shiva, his fierce yet benevolent spirit protects villagers from malevolent ghosts and injustice.",
        invocation_or_jagar="जय भोलानाथ बाबा, कष्ट निवारक! गाँव की सीम म रक्षा करा!",
        cultural_role="Venerated in village shrines as a watchful protector against evil spirits, cattle disease, and property disputes."
    ),
    "ganganath": KumaoniDeity(
        id="ganganath",
        name_kumaoni="गंगनाथ देवता",
        name_roman="Ganganath Devta",
        title="नाथ संप्रदाय के सिद्ध देव (Prince Yogi Deity of Justice and Healing)",
        category="Jagar Deity",
        primary_shrines=["कतारमल (अल्मोड़ा)", "डोटी (नेपाल)", "हवालबाग", "द्वाराहाट"],
        iconography_and_symbols="Yogi's ochre robe, khappar (alms bowl), chimta (fire tongs), and damru.",
        legend="A historical prince of Doti (Western Nepal) who renounced royal luxury to become a celibate Nath yogi disciple of Gorakhnath. He journeyed to Katarmal in Kumaon where he formed a spiritual bond with Bhana Joshi. Both were murdered by envious rivals. Their spirits united as powerful guardian deities.",
        invocation_or_jagar="अलख निरंजन! जय बाबा गंगनाथ, डोटी का राजकुमार, कतारमल का सिद्ध देव!",
        cultural_role="Invoked through night-long jagar ceremonies to resolve family feuds, diagnose incurable afflictions, and heal mental distress."
    ),
    "kalbisht": KumaoniDeity(
        id="kalbisht",
        name_kumaoni="कालबिष्ट (कालू देवता)",
        name_roman="Kalbisht (Kalu Devta)",
        title="गौ-पालक एवं ग्वालों के रक्षक (Protector of Cattle, Herdsmen & Pastoralists)",
        category="Gram Devta",
        primary_shrines=["बिनसर (अल्मोड़ा)", "बिष्टखोली", "झाँकर सेम"],
        iconography_and_symbols="Flute (Muruli), wooden shepherd's crook, pastoral horn, and offerings of fresh cow milk.",
        legend="A noble warrior and pastoralist of the Bisht clan in Binsar famed for his extraordinary compassion for cows and his melodious flute that pacified wild tigers. He defended poor shepherds against oppressive feudatories until he was treacherously murdered by poisoned food.",
        invocation_or_jagar="जय कालबिष्ट बाबा, बिनसर का राजा! गौ-बछिया कणी दूध-दही दिया, विपदा दूर करा!",
        cultural_role="The patron saint of milkmen and villagers. Farmers offer the first yield of milk and curd from newly calved cows to his shrine before consuming it."
    ),
    "airy_devta": KumaoniDeity(
        id="airy_devta",
        name_kumaoni="ऐरी देवता",
        name_roman="Airy Devta",
        title="शिकार एवं पर्वत शिखरों के स्वामी (God of the Hunt, Archery & High Ridges)",
        category="Kshetrapal",
        primary_shrines=["बैजनाथ (बागेश्वर)", "धौलादेवी (अल्मोड़ा)", "लोहाघाट (चम्पावत)"],
        iconography_and_symbols="Riding a blue-black horse, armed with a bow and arrow, accompanied by a pack of celestial hunting hounds (Sau).",
        legend="An ancient pre-Vedic deity of the Khas and forest hunters. Airy roams mountain ridges and dark forests at midnight with his ethereal hounds. While dangerous to lone travelers who cross his path disrespectfully, he is deeply protective of shepherds who build stone cairns in his honor.",
        invocation_or_jagar="ऐरी महाराज शिकार खेलन निकला, डाँणा-काँठा म बाजि रई बाँसुरी! दया राख महाराज!",
        cultural_role="Venerated at ridge-top shrines (थान) marked by small stone cairns and iron tridents to protect grazing herds from leopards and wolves."
    ),
    "chaumu_devta": KumaoniDeity(
        id="chaumu_devta",
        name_kumaoni="चौमूँ देवता (चामु)",
        name_roman="Chaumu Devta (Chamu)",
        title="पशुधन के रक्षक देवता (Guardian of Livestock and Village Flocks)",
        category="Gram Devta",
        primary_shrines=["चम्पावत", "चौमेल (पिथौरागढ़)", "रीठा साहिब क्षेत्र"],
        iconography_and_symbols="Brass temple bells, white banners, and vessels filled with fresh churned milk.",
        legend="A revered folk incarnation of Lord Shiva particularly cherished in Kali Kumaon and Champawat. Legend recounts how Chaumu safeguarded cows that had strayed into dense jungles from predators.",
        invocation_or_jagar="जय चौमूँ देवता, चौमेल का राजा! दूध-पूता की रक्षा करा!",
        cultural_role="Invoked whenever cattle fall ill. Milk offerings and miniature bells are dedicated upon recovery."
    ),
    "kailpal": KumaoniDeity(
        id="kailpal",
        name_kumaoni="कैलपाल देवता",
        name_roman="Kailpal Devta",
        title="सीम-सीमाना के रक्षक (Guardian of Boundaries & Village Perimeters)",
        category="Kshetrapal",
        primary_shrines=["अस्कोट (पिथौरागढ़)", "सीरा (डीडीहाट)", "काली कुमाऊँ"],
        iconography_and_symbols="Iron tridents fixed in stone masonry on mountain boundary passes.",
        legend="The supreme boundary guardian of ancient eastern Kumaon and the Indo-Nepal border ridges. Kailpal protects villages against external plagues, locust swarms, and trespassing spirits.",
        invocation_or_jagar="कैलपाल महाराज, गाँव की चारि सीम म चौंकी दिया!",
        cultural_role="Worshipped during village boundary demarcation ceremonies and agricultural sowings."
    ),
    "barahi_devi": KumaoniDeity(
        id="barahi_devi",
        name_kumaoni="माँ बाराही देवी (देवीधुरा)",
        name_roman="Barahi Devi (Devidhura)",
        title="शक्तिस्वरूपा महामाया (Supreme Fierce Goddess of Devidhura & Bagwal)",
        category="Kuldevi / Shakti",
        primary_shrines=["देवीधुरा (चम्पावत)"],
        iconography_and_symbols="Sacred stone idol housed within colossal natural split boulders, copper plates, and wicker shields (Chhatolis).",
        legend="One of the ancient Matrikas. In ancient times, an old woman offered her only grandson as a human sacrifice to the goddess to save the valley from demons. Moved by her grief, the goddess ordained that four clans would instead fight a symbolic stone battle (Bagwal) until blood equal to one man was shed.",
        invocation_or_jagar="जय माँ बाराही, देवीधुरा वासिनी, चारि खामों की रक्षिका!",
        cultural_role="Focal deity of the world-famous Bagwal stone-pelting tournament held every Shravan Purnima."
    ),
    "purnagiri": KumaoniDeity(
        id="purnagiri",
        name_kumaoni="माँ पूर्णागिरी",
        name_roman="Purnagiri Devi",
        title="महाशक्ति पीठ (Sacred Shaktipeeth on the Sharda Mountain)",
        category="Kuldevi / Shakti",
        primary_shrines=["टनकपुर (चम्पावत - पूर्णागिरी पर्वत शिखर)"],
        iconography_and_symbols="Red chunari, silver eyes, coconut offerings, and sacred tridents looking down over the Sharda river.",
        legend="One of the 108 sacred Shaktipeeths of Hindu mythology. According to the Shiva Purana, the naval (Nabhi) of Sati fell upon this high mountain peak as Shiva carried her across the skies in sorrow.",
        invocation_or_jagar="जय माँ पूर्णागिरी, पर्वत वासिनी, मनोकामना पूर्ण करणि!",
        cultural_role="Revered across Kumaon and North India as the fulfiller of all wishes (*Manokamna Siddha Peeth*). Visited by millions during Chaitra Navratri."
    ),
    "kasar_devi": KumaoniDeity(
        id="kasar_devi",
        name_kumaoni="कासार देवी",
        name_roman="Kasar Devi",
        title="कश्यप पर्वत की आदिशक्ति (Ancient Cave Sanctuary of Cosmic Energy)",
        category="Kuldevi / Shakti",
        primary_shrines=["कासार देवी (अल्मोड़ा)"],
        iconography_and_symbols="Cave sanctum, natural rock outcrops, and ancient 2nd century BCE Brahmi inscriptions.",
        legend="A powerful cave shrine dating back over two millennia. Situated on a unique geomagnetic ridge (one of only three such sites in the world alongside Stonehenge and Machu Picchu), celebrated as a sanctuary of deep meditation by Swami Vivekananda (1890) and international spiritual seekers.",
        invocation_or_jagar="कासार पर्वत वासिनी माँ दुर्गा, ध्यान-सिद्धि प्रदायिनी!",
        cultural_role="Spiritual center of cosmic harmony, meditation, and ancient Himalayan asceticism."
    ),
    "jhula_devi": KumaoniDeity(
        id="jhula_devi",
        name_kumaoni="झूला देवी",
        name_roman="Jhula Devi",
        title="घंटियों वाली माता (Goddess of the Wooden Swing & Thousands of Bells)",
        category="Kuldevi / Shakti",
        primary_shrines=["चौबटिया (रानीखेत)"],
        iconography_and_symbols="Goddess seated on an iron/wooden swing surrounded by a labyrinth of thousands of bronze and brass bells tied by devotees.",
        legend="Dating back to the 8th century, the deity manifested in a shepherd's dream asking to be unearthed and placed on a cradle-swing (Jhula) to protect local villagers and their cattle from wild leopards that prowled the dense oak and deodar forests.",
        invocation_or_jagar="जय झूला देवी माता, रानीखेत वासिनी, घंटियों की खनक म रक्षा करा!",
        cultural_role="Devotees tie a bell of faith with a wish; once granted, they return to tie a larger gratitude bell."
    ),
    "lakhia_bhoot": KumaoniDeity(
        id="lakhia_bhoot",
        name_kumaoni="लखिया भूत (वीरभद्र)",
        name_roman="Lakhia Bhoot (Veerabhadra)",
        title="महादेव का उग्र गण एवं हिलजात्रा का महानायक (Chief Attendant of Shiva & Protagonist of Hillyatra)",
        category="Gram Devta",
        primary_shrines=["कुमौड़ (पिथौरागढ़ - सोर घाटी)"],
        iconography_and_symbols="Terrifying dark mask, wild flax hair, black robes, and two long ropes held by attendants.",
        legend="The supreme manifestation of Veerabhadra, created from Shiva's matted lock. In the pastoral folk drama of Hillyatra, Lakhia Bhoot appears with thunderous energy amidst the muddy paddy fields to drive away drought, agricultural pests, and demons, blessing crops and children.",
        invocation_or_jagar="आयो रे लखिया भूत महादेव को गण! सब रोग-दोष भगा, धरती म अन्न उपजा!",
        cultural_role="The climactic deity of the historic Hillyatra festival in Sor Valley, worshipped for abundant harvests and community vitality."
    ),
    "haru_devta": KumaoniDeity(
        id="haru_devta",
        name_kumaoni="हारू देवता (हरिचंद्र)",
        name_roman="Haru Devta (Harishchandra)",
        title="दयालु लोक देवता (Benevolent Brother of Golu Devta & Protector of Champawat)",
        category="Jagar Deity",
        primary_shrines=["चम्पावत", "अल्मोड़ा", "खेतीखान"],
        iconography_and_symbols="Royal insignia, silver umbrella, and sword.",
        legend="Deified as Raja Harishchandra of Champawat and brother of Golu Devta. A benevolent ruler celebrated in Kumaoni balladic epics (*Hurkiya Bol*) for his selflessness and defense of the subjects.",
        invocation_or_jagar="जय राजा हारू, चम्पावत का छत्रपति! गोलू का भाई, प्रजा का रखवाला!",
        cultural_role="Invoked alongside Golu Devta in traditional royal and family jagars to bestow blessings of harmony and domestic peace."
    ),
    "nagaraja": KumaoniDeity(
        id="nagaraja",
        name_kumaoni="नागराज देवता (सेम-मुखेम / भेरुंडा)",
        name_roman="Nagaraja Devta (Sem Mukhem)",
        title="जल-स्रोतों एवं नौलों के रक्षक नाग देव (Divine Serpent Guardian of Springs & Hydrology)",
        category="Kshetrapal",
        primary_shrines=["बेरीनाग (पिथौरागढ़)", "धौलीनाग", "कालीनाग", "फेणिनाग", "सेम-मुखेम"],
        iconography_and_symbols="Carved multi-headed serpent stones (Nag-Shila) placed inside traditional stepped wells (Naulas) and hill streams.",
        legend="Kumaon has an ancient Naga heritage reflected in the iconic shrines of Berinag, Dhaulinag, Kalinag, Feninag, and Pinglenag. The serpent gods are the divine masters of underground springs and groundwater reservoirs.",
        invocation_or_jagar="जय नागराज देवता, नौला-धौड़ा का स्वामी! पाणि का स्रोत हरा-भरा राखो!",
        cultural_role="Worshipped during the excavation and consecration of every traditional hill water spring (Naula) to ensure perennial sweet water."
    ),
    "kotgari_devi": KumaoniDeity(
        id="kotgari_devi",
        name_kumaoni="कोटगाड़ी भगवती",
        name_roman="Kotgari Devi",
        title="न्याय की अंतिम अदालत (Supreme Divine Court of Final Appeal)",
        category="Nyaya Devta",
        primary_shrines=["पांखू (पिथौरागढ़)"],
        iconography_and_symbols="Silver face mask, ancient brass lamps, and written appeals of grievance.",
        legend="Venerated across Uttarakhand as the ultimate divine judiciary where a wronged soul appeals when human laws, courts, and even other remedies have failed. Her justice is believed to be infallible and strictly karmic.",
        invocation_or_jagar="जय कोटगाड़ी माँ, पांखू की देवी! अंतिम न्याय की दाता, निर्दोष की रक्षा करा!",
        cultural_role="Litigants who have suffered grave injustice travel to Pankhu to submit petitions for divine retribution."
    ),
    "chhurmal_devta": KumaoniDeity(
        id="chhurmal_devta",
        name_kumaoni="छुरमल देवता",
        name_roman="Chhurmal Devta",
        title="हिम शिखरों एवं भोटिया व्यापार मार्गों के संरक्षक (Guardian of High Alpine Passes & Shauka Traders)",
        category="Kshetrapal",
        primary_shrines=["जोहार घाटी (मिलम)", "दारमा घाटी", "मुनस्यारी (पिथौरागढ़)"],
        iconography_and_symbols="Tibetan wool banners, mountain yak horns, and stone cairns at trans-Himalayan high passes (Khal).",
        legend="The supreme guardian deity of the Shauka and Bhotia trans-Himalayan trade caravans that crossed the perilous snow passes of Unta Dhura, Kingri-Bingri, and Lipulekh into Tibet. Chhurmal shielded travelers from avalanches and snowstorms.",
        invocation_or_jagar="छुरमल बाबा हिमाल का धनी, जोहार-दारमा का रखवाला! बफिला बाटो म रक्षा करा!",
        cultural_role="Worshipped by high-altitude mountaineers, pastoralists, and borderland communities before embarking on dangerous Himalayan expeditions."
    ),
    "balchan_devta": KumaoniDeity(
        id="balchan_devta",
        name_kumaoni="बालचन देवता",
        name_roman="Balchan Devta",
        title="युवा वीर योद्धा एवं कुल रक्षक (Youthful Warrior Guardian Spirit)",
        category="Jagar Deity",
        primary_shrines=["गंगोलीहाट (पिथौरागढ़)", "सीरा", "अल्मोड़ा"],
        iconography_and_symbols="Iron sword, shield, and red silk pennant.",
        legend="A heroic young warrior deified in village memory after sacrificing his life defending his clan and settlement from marauding forces.",
        invocation_or_jagar="जय वीर बालचन, तलवार का धनी! गाँव म सुख-शांति राख महाराज!",
        cultural_role="Invoked during household jagar rituals to eliminate negative omens and invigorate the youth."
    ),
    "dhannar_devta": KumaoniDeity(
        id="dhannar_devta",
        name_kumaoni="धन्नार देवता",
        name_roman="Dhannar Devta",
        title="काली कुमाऊँ के वीर भड़ (Heroic Ancestral Warrior Deity of Kali Kumaon)",
        category="Jagar Deity",
        primary_shrines=["पाटी (चम्पावत)", "लोहाघाट", "बाराकोट"],
        iconography_and_symbols="Spear (barchha), shield (dhal), and stone altar.",
        legend="Celebrated in epic folk ballads (*Pauwada*) as one of the legendary chivalric warriors (*Bhad*) of the Chand era whose martial valor brought honor to Kumaon.",
        invocation_or_jagar="धन्नार भड़ महाराज की जय! काली कुमाऊँ को सूरवीर!",
        cultural_role="Worshipped by martial families and agricultural communities in Champawat."
    ),
    "malushahi": KumaoniDeity(
        id="malushahi",
        name_kumaoni="मालूशाही एवं राजुला",
        name_roman="Malushahi & Rajula",
        title="अमर प्रेम एवं लोकगाथा के दिव्य स्वरूप (Deified Immortal Folk Heroes of Katyur & Johar)",
        category="Jagar Deity",
        primary_shrines=["बैजनाथ (कत्यूर घाटी, बागेश्वर)", "जोहार (मुनस्यारी)"],
        iconography_and_symbols="Yogi's saffron attire, bronze earrings (kundal), musical hurka drum, and peacock feather.",
        legend="King Malushahi of Bairat (Katyur) and Rajula, the Shauka merchant princess of Johar, whose epic love ballad is sung by hereditary Hurkiya bards over several nights. Malushahi renounced his throne to become a Nath yogi to win Rajula.",
        invocation_or_jagar="धन्य राजा मालूशाही, धन्य राजुला सुवा! कत्यूर का राजा, अमर प्रेम का प्रतीक!",
        cultural_role="Venerated in every village hearth through the most celebrated musical epic (*Pauwada*) of the central Himalayas."
    ),
    "bhumia_devta": KumaoniDeity(
        id="bhumia_devta",
        name_kumaoni="भूमिया देवता (क्षेत्रपाल)",
        name_roman="Bhumia Devta (Kshetrapal)",
        title="भूमि, मिट्टी एवं ग्राम-सीमाना के अधिष्ठाता देव (Lord of Soil, Agricultural Land & Village Settlement)",
        category="Gram Devta",
        primary_shrines=["समस्त कुमाऊँ के गाँव (Every village across Almora, Pithoragarh, Bageshwar, Nainital, Champawat)"],
        iconography_and_symbols="Sacred stone altar placed beneath ancient sacred oak/peepal tree or near village terraced fields, white flag, red vermilion, and unpolished stones.",
        legend="Bhumia is the primordial spirit-lord of the soil and foundational guardian of human settlement in Kumaon. Before ploughing the fields, building a house, or celebrating any lifecycle milestone, the first prayer and grain offering must be offered to Bhumia. Neglecting Bhumia is believed to bring crop failure or distress to cattle.",
        invocation_or_jagar="जय भूमिया महाराज, धरती का धनी! गाँव की सीम म चौंकी दिया, खेत-खलिहान म अन्न उपजा!",
        cultural_role="Invoked first at the start of any agricultural work, house construction, wedding, or religious ceremony. Farmers offer the first grain sheaves of Harela and new harvest."
    ),
    "mosta_devta": KumaoniDeity(
        id="mosta_devta",
        name_kumaoni="मोस्टा देवता (मेघ एवं वर्षा के देव)",
        name_roman="Mosta Devta",
        title="इंद्र के मानस पुत्र एवं मेघ-वर्षा के अधिष्ठाता (Lord of Monsoon Clouds, Rains and Springs)",
        category="Gram Devta",
        primary_shrines=["मोस्टामानु (चांदक, पिथौरागढ़)", "सोर घाटी", "डीडीहाट"],
        iconography_and_symbols="Sacred palanquin (Doli), brass bells, silver umbrellas, and offerings of fresh mountain cucumbers and unboiled milk.",
        legend="Revered as the divine son of Indra sent down to the Himalayas to govern rains and springs. During droughts in the Sor Valley, villagers undertake barefoot processions carrying Mosta Devta's palanquin to Chandak summit, praying for rain, which locals hold unfailingly falls within hours.",
        invocation_or_jagar="जय मोस्टा महाराज, मेघ वर्षा का दाता! सोर घाटी म हरियाली ल्याओ, बादल बरसाओ!",
        cultural_role="The focal rain-deity of eastern Kumaon, celebrated with massive annual melas at Mostamanu on Krishna Ashtami."
    ),
    "jiya_rani": KumaoniDeity(
        id="jiya_rani",
        name_kumaoni="जिया रानी (मौजानी / कत्यूर की वीरांगना रानी)",
        name_roman="Jiya Rani (Mawjani)",
        title="कूर्मांचल की अमर वीरांगना एवं लोकदेवी (Warrior Queen of Katyur & Deified Folk Goddess)",
        category="Jagar Deity",
        primary_shrines=["रानीबाग (चित्रशिला, नैनीताल)", "बैजनाथ", "कत्यूर घाटी"],
        iconography_and_symbols="Chitrashila holy boulders at Ranibagh, royal sword, riding steed, and silk veil.",
        legend="The legendary queen of Katyuri king Pritamdev (Pithorashahi). When Turkish/Rohilla invaders invaded the foothills, Rani Jiya rallied the hill fighters, led her troops into battle at Chitrashila (Ranibagh), and repelled the invaders before disappearing into the sacred subterranean cavern of the river.",
        invocation_or_jagar="धन्य जिया रानी कत्यूर की महारानी! चित्रशिला म अमर ज्योति, कूर्मांचल की लाज बचै!",
        cultural_role="Commemorated through the grand Uttarayani Chitrashila fair at Ranibagh and in stirring Hurkiya ballads that inspire bravery and feminine honor."
    ),
    "saim_devta": KumaoniDeity(
        id="saim_devta",
        name_kumaoni="सैम देवता (हारू-सैम)",
        name_roman="Saim Devta",
        title="हारू के सहयोगी एवं ग्राम-रक्षा के महाबली (Boundary Guardian & Inseparable Partner of Haru Devta)",
        category="Gram Devta",
        primary_shrines=["चम्पावत", "लोहाघाट", "अल्मोड़ा", "झाँकर सेम (जागेश्वर)"],
        iconography_and_symbols="Sacred iron tridents, silver mace, and boundary stone pillars.",
        legend="Always invoked alongside King Haru as 'Haru-Saim'. Saim is the fierce, invincible frontline commander who patrols village frontiers, drives away predatory forest spirits, and enforces moral rectitude.",
        invocation_or_jagar="जय हारू-सैम महाराज की जोड़ी! गाँव का सीम-सीमाना म चौंकी राखो!",
        cultural_role="Paired shrines of Haru-Saim exist in numerous Kumaoni hamlets, propitiated during village boundaries demarcation."
    ),
    "naina_devi": KumaoniDeity(
        id="naina_devi",
        name_kumaoni="माँ नैना देवी",
        name_roman="Naina Devi",
        title="नैनीताल की अधिष्ठात्री शक्ति (Sacred Shaktipeeth of the Divine Eyes)",
        category="Kuldevi / Shakti",
        primary_shrines=["नैनीताल (नैनी झील तट)"],
        iconography_and_symbols="Two divine silver eyes (Nayan) placed upon sacred brass sanctum overlooking the emerald waters of Naini Lake.",
        legend="According to the Shiva Purana, when Lord Shiva carried the charred body of Sati, her divine eyes (Nayan) fell at this Himalayan spot, forming the pristine eye-shaped lake of Naini and the sacred shrine of Naina Devi.",
        invocation_or_jagar="जय माँ नैना देवी, नैनीताल वासिनी! नयनों की ज्योति, सब कष्ट हरणि!",
        cultural_role="The divine patron and spiritual guardian of Nainital, celebrated during Nanda Ashtami and Navratri."
    ),
    "kot_bhramari": KumaoniDeity(
        id="kot_bhramari",
        name_kumaoni="कोट भ्रामरी (कोट की माई)",
        name_roman="Kot Bhramari Devi",
        title="कत्यूरी राजवंश की अधिष्ठात्री कुलदेवी (Sovereign Tutelary Goddess of the Katyuri Kings)",
        category="Kuldevi / Shakti",
        primary_shrines=["रणचुलाहाट / कोट भ्रामरी (गरुड़, बागेश्वर)"],
        iconography_and_symbols="Ancient stone fort sanctum, golden mukut, swarms of divine bees (Bhramar), and red silken parasols.",
        legend="Manifested as Goddess Bhramari (the goddess of hornets and bees) who released millions of stinging black bees from her divine form to annihilate the demon Arunasura. Worshipped as the royal patron of the Katyuri dynasty at their ancient capital.",
        invocation_or_jagar="जय माँ कोट भ्रामरी, कत्यूर की कुलदेवी! रणचुलाहाट की महारानी, आशीष दिया माँ!",
        cultural_role="Revered throughout Baijnath, Garur, and Someshwar valleys with annual fairs on Nanda Ashtami and Chaitra Navratri."
    ),
    "dunagiri_devi": KumaoniDeity(
        id="dunagiri_devi",
        name_kumaoni="माँ दूनागिरी (द्रोणागिरी वैष्णवी)",
        name_roman="Dunagiri Devi",
        title="द्रोणांचल पर्वत की वैष्णवी शक्तिपीठ (Vaishnavi Shakti Sanctuary of Dwarahat)",
        category="Kuldevi / Shakti",
        primary_shrines=["दूनागिरी (द्वाराहाट, अल्मोड़ा)"],
        iconography_and_symbols="Mountain-top sanctum at 8,000 ft, sacred pindis, thousands of brass bells, and ancient oak groves.",
        legend="Legend recounts that when Hanuman carried the Dronagiri mountain with Sanjivani herb for wounded Lakshmana, a fragment fell here, blessed by Goddess Durga as an eternal sanctuary of spiritual meditation.",
        invocation_or_jagar="जय दूनागिरी माता, द्रोणाचल वासिनी! मनोकामना सिद्ध करणि, वैष्णवी रूप नमोस्तुते!",
        cultural_role="One of the most sacred pilgrimage shrines of Almora, visited by childless couples and spiritual aspirants."
    ),
    "syahi_devi": KumaoniDeity(
        id="syahi_devi",
        name_kumaoni="माँ स्याही देवी",
        name_roman="Syahi Devi",
        title="शीतलाखेत पर्वत शिखर की रक्षक देवी (Ancient Peak Sanctuary of Sheetlakhet)",
        category="Kuldevi / Shakti",
        primary_shrines=["शीतलाखेत (अल्मोड़ा)"],
        iconography_and_symbols="Ancient stone idol on high mountain peak surrounded by dense chir and banj forests.",
        legend="Established during the reign of the Chand kings in the 12th century. The goddess manifested to protect the kingdom from southern invasions and epidemic plagues.",
        invocation_or_jagar="जय माँ स्याही देवी, पर्वत शिखर वासिनी! शीतलाखेत की रक्षिका, विपदा दूर करा!",
        cultural_role="A powerful mountain sanctuary where Swami Vivekananda meditated and where locals seek protection against adversity."
    ),
    "gabla_devta": KumaoniDeity(
        id="gabla_devta",
        name_kumaoni="गबला देवता",
        name_roman="Gabla Devta",
        title="व्यापार, समृद्धि एवं हिम शिखरों के स्वामी (Lord of Trans-Himalayan Trade, Caravans & Wealth)",
        category="Gram Devta",
        primary_shrines=["दारमा घाटी", "ब्यांस घाटी", "चौंदास", "मुनस्यारी"],
        iconography_and_symbols="White yak-tail chowrie, silver conch shell, high-altitude incense (Dhup), and ceremonial stone cairns.",
        legend="The supreme guardian deity of the Shauka and Rung trans-Himalayan trading caravans. Gabla bestows fortune in enterprise, shields merchants crossing blizzard-ridden passes, and blesses pastoral flocks.",
        invocation_or_jagar="गबला बाबा दया राख महाराज, जोहार-दारमा का स्वामी! व्यापार म लाभ दिया, घर-परिवार सुखी राखो!",
        cultural_role="Venerated in every Rung and Shauka household with Gabla Puja rituals before the seasonal migration to Tibet or plains."
    ),
    "chipla_kedar": KumaoniDeity(
        id="chipla_kedar",
        name_kumaoni="छिप्ला केदार देवता",
        name_roman="Chipla Kedar",
        title="हिम सरोवर एवं 14,000 फीट की ऊँचाई के शिव स्वरूप (Himalayan Tarn & Alpine Mountain Lord)",
        category="Kshetrapal",
        primary_shrines=["छिप्ला कोट (धारचूला, पिथौरागढ़)"],
        iconography_and_symbols="Glacial lake (Chipla Kund), stone trident, high alpine Brahma Kamal flowers, and white flags.",
        legend="Revered as a manifestation of Lord Shiva residing at the sacred alpine tarn of Chipla Kot at 14,000 ft. Pilgrims undertake the arduous barefoot Chipla Jaat trek every few years through sheer rock cliffs.",
        invocation_or_jagar="जय छिप्ला केदार बाबा, हिमाल का राजा! बर्फिला शिखर म विराजित, सब कणी सुख दिया!",
        cultural_role="Patron deity of pastoralists, shepherds, and mountaineers of the Indo-Nepal-Tibet frontier valleys."
    ),
    "bhairav_devta": KumaoniDeity(
        id="bhairav_devta",
        name_kumaoni="काल भैरव / लाटा भैरव (गोलू के सेनापति)",
        name_roman="Bhairav Devta",
        title="क्षेत्रपाल एवं गोलू देवता के मुख्य सेनापति (Fierce Gatekeeper & Marshal of Divine Justice)",
        category="Kshetrapal",
        primary_shrines=["अल्मोड़ा (लाटा भैरव)", "घोड़ाखाल", "चितई", "बागेश्वर"],
        iconography_and_symbols="Black stone idol, iron club, trishul, and offerings of black cloth, mustard oil, and incense.",
        legend="Bhairav serves as the watchful guardian of temple boundaries and the commander of Golu Devta's spirit army. Devotees seeking Golu Devta's blessing must first pay obeisance to Bhairav.",
        invocation_or_jagar="जय भैरव महाराज, काल भैरव लाटा भैरव! सीम का रखवाला, भूत-पिशाच भगा!",
        cultural_role="Invoked at the entrance of almost every village and shrine across Kumaon to ward off negative spirits and witchcraft."
    ),
    "ainchari": KumaoniDeity(
        id="ainchari",
        name_kumaoni="आँछरी (वनपरियां एवं मातृकाएं)",
        name_roman="Ainchari (Himalayan Fairies)",
        title="पर्वत शिखरों, जल-स्रोतों एवं पुष्प-वाटिकाओं की दिव्य परियां (Celestial Nymphs of Alpine Meadows & Springs)",
        category="Jagar Deity",
        primary_shrines=["बुग्याल (Alpine meadows of Munsyari, Bedni)", "वन-शिखर", "झाँकर"],
        iconography_and_symbols="Fragrant wild flowers, mirrors, multi-colored ribbons, and pure spring water.",
        legend="Ethereal maiden spirits who dwell among high rhododendron blossoms, waterfalls, and alpine meadows. Known to enchant solitary travelers who wear bright colors or whistle near mountain springs.",
        invocation_or_jagar="आँछरी मात, हिमाल की परियाँ! डाँणा-काँठा म वास, सब पर दया राखो माँ!",
        cultural_role="Invoked and placated during nocturnal women's jagar ceremonies (*Ainchari Jagar*) to ensure fertility and emotional peace."
    ),
    "masan_devta": KumaoniDeity(
        id="masan_devta",
        name_kumaoni="मसान देवता (कबरिया मसान)",
        name_roman="Masan Devta",
        title="श्मशान एवं निशीथ के नियामक देव (Lord of Cremation Grounds & Midnight Spirit Realm)",
        category="Jagar Deity",
        primary_shrines=["नदी संगमों के श्मशान घाट (Rameshwar, Pancheshwar, Bageshwar)"],
        iconography_and_symbols="Sacred ashes, iron tongs (chimta), smoldering wood embers, and black sesame seeds.",
        legend="The nocturnal spirit of cremation grounds who commands wandering ethereal entities. When properly appeased through traditional rituals, Masan serves as an impenetrable shield against dark witchcraft and negative afflictions.",
        invocation_or_jagar="जय मसान देव, श्मशान का धनी! रोग-व्याधि और उपद्रव कणी शांत करा!",
        cultural_role="Pacified in specialized shamanic *Masan Jagars* performed by experienced Dangariyas and Hurkiyas."
    ),
    "panchnag": KumaoniDeity(
        id="panchnag",
        name_kumaoni="पंचनाग (धौलीनाग, कालीनाग, फेणिनाग, पिंगलनाग, वासुकिनाग)",
        name_roman="Panchnag (Five Serpent Lords)",
        title="बेरीनाग एवं कूर्मांचल के अधिष्ठाता नाग देव (Sacred Five Serpent Deities of Berinag & Pithoragarh)",
        category="Kshetrapal",
        primary_shrines=["बेरीनाग", "धौलीनाग (विजयपुर)", "कालीनाग", "फेणिनाग", "पिंगलनाग"],
        iconography_and_symbols="Ancient stone carvings of coiled multi-hooded cobras inside sacred cedar groves and stepped spring wells.",
        legend="Ancient Kumaon was deeply steeped in Naga worship. The five Naga brothers took residence on five picturesque ridges of Pithoragarh to watch over human hamlets, weather cycles, and perennial aquifers.",
        invocation_or_jagar="नमो पंचनाग देवता, बेरीनाग-धौलीनाग-फेणिनाग! जल-स्रोत निर्मल राखो, सब की रक्षा करा!",
        cultural_role="Worshipped on Nag Panchami and during the consecration of every new village well or drinking spring."
    ),
    "ghatku_devta": KumaoniDeity(
        id="ghatku_devta",
        name_kumaoni="घटकू देवता",
        name_roman="Ghatku Devta",
        title="काली कुमाऊँ के वीर योद्धा एवं न्यायप्रिय देव (Chivalric Hero Guardian of Champawat)",
        category="Gram Devta",
        primary_shrines=["चम्पावत", "पाटी", "लोहाघाट"],
        iconography_and_symbols="Iron sword, copper shields, and stone boundary altar.",
        legend="A historical martial hero (*Bhad*) celebrated in the chivalric ballads of Kali Kumaon. Deified for defending defenseless peasants from plundering dacoits.",
        invocation_or_jagar="जय घटकू महाराज, तलवार का धनी! निर्दोष की रक्षा करा महाराज!",
        cultural_role="Venerated in village festivals across Champawat for strength, valor, and family welfare."
    ),
    "narsingh_devta": KumaoniDeity(
        id="narsingh_devta",
        name_kumaoni="नरसिंह देवता",
        name_roman="Narsingh Devta",
        title="असुर-विनाशक एवं कुल-रक्षक नृसिंह (Fierce Man-Lion Incarnation & Clan Defender)",
        category="Jagar Deity",
        primary_shrines=["जोशीमठ / कूर्मांचल के पारिवारिक थान"],
        iconography_and_symbols="Lion-faced deity with sharp claws, golden armor, and red pennants.",
        legend="Invoked in traditional Kumaoni Jagars as the ultimate fierce protector of household honor who shatters malevolent curses, black magic, and evil eyes.",
        invocation_or_jagar="जय नरसिंह महाराज, खंभ फाड़ि प्रकट भया! सब दुष्टों का नाश करा, कुल की रक्षा करा!",
        cultural_role="A major deity in domestic Jagars where the medium displays tremendous martial fervor and blesses the family."
    ),
    "ranbhoot": KumaoniDeity(
        id="ranbhoot",
        name_kumaoni="रणभूत (वीर भड़ पूर्वज आत्माएं)",
        name_roman="Ranbhoot (Ancestral Warrior Spirits)",
        title="युद्ध-क्षेत्र में बलिदान हुए पूर्वज योद्धा (Martyred Hero Ancestor Spirits)",
        category="Jagar Deity",
        primary_shrines=["पारिवारिक थान (Household ancestor shrines across Kumaon)"],
        iconography_and_symbols="Iron weapons, miniature swords, shields, and red silken sashes.",
        legend="Spirits of brave clan ancestors who laid down their lives on battlefields defending Kurmanchal. Rather than haunting, their brave souls watch over succeeding generations.",
        invocation_or_jagar="जय रणभूत पूर्वज, युद्ध का वीर! कुल म वंश-वृद्धि दिया, सब कणी बलवान करा!",
        cultural_role="Propitiated during family *Shraddha* and special martial jagars with dynamic ritual dance wielding swords."
    ),
    "khandanath": KumaoniDeity(
        id="khandanath",
        name_kumaoni="खंडानाथ (खंडेराव)",
        name_roman="Khandanath",
        title="प्राचीन शैव क्षेत्रपाल (Ancient Shaivite Guardian Deity of Central Valleys)",
        category="Kshetrapal",
        primary_shrines=["बागेश्वर", "कत्यूर घाटी", "सोमेश्वर"],
        iconography_and_symbols="Trident, sacred damru, and natural rock altar.",
        legend="An ancient Shaivite folk deity closely connected with the Nath yogi heritage that flourished in Kumaon under the Katyuris.",
        invocation_or_jagar="जय खंडानाथ बाबा, पर्वत का स्वामी! घाटी म शांति राख महाराज!",
        cultural_role="Worshipped during village agricultural sowing and seasonal changes."
    ),
    "khatad_singh": KumaoniDeity(
        id="khatad_singh",
        name_kumaoni="खतड़ सिंह (खतड़वा के महानायक)",
        name_roman="Khatad Singh",
        title="चंद सेना के सेनापति एवं खतड़वा के ऐतिहासिक नायक (Historic Chand General of Khatarwa Bonfire)",
        category="Gram Devta",
        primary_shrines=["अल्मोड़ा", "पिथौरागढ़", "चम्पावत"],
        iconography_and_symbols="Flaming pine torch (Bhelo), bonfires, and mountain cucumbers.",
        legend="The legendary general whose battlefield conquest was messaged across the mountains of Kumaon by lighting bonfires on mountain peaks, inaugurating the festival of Khatarwa.",
        invocation_or_jagar="खतड़वा पड़ि ग्यो खात म, गैया आ गई गोठ म! भैलो जी भैलो!",
        cultural_role="Commemorated every autumn during the Khatarwa bonfire celebration to protect cattle from the winter cold."
    ),
    "jhakar_saim": KumaoniDeity(
        id="jhakar_saim",
        name_kumaoni="झाँकर सैम देवता",
        name_roman="Jhakar Saim Devta",
        title="जागेश्वर एवं बिनसर के सघन देवदार वनों के स्वामी (Forest Sanctuary Guardian of Jageshwar & Binsar)",
        category="Kshetrapal",
        primary_shrines=["झाँकर सैम (जागेश्वर धाम, अल्मोड़ा)", "बिनसर"],
        iconography_and_symbols="Sacred deodar grove, iron bells, and natural spring altar.",
        legend="The divine forest guardian of the sacred Jageshwar valley. Pilgrims visiting the Shiva temple complex traditionally first seek the protective permission of Jhakar Saim.",
        invocation_or_jagar="जय झाँकर सैम महाराज, देवदार वन का राजा! जागेश्वर धाम की चौंकी राख महाराज!",
        cultural_role="Protects the sacred cedar forests and wildlife of Jageshwar and Binsar."
    )
}


class DeitiesTreasury:
    """Interface to access, search, and inspect local Kumaoni deities."""

    @staticmethod
    def list(category: Optional[str] = None) -> List[KumaoniDeity]:
        """List all catalogued Kumaoni deities, optionally filtered by category."""
        deities = list(DEITIES_DATA.values())
        if category:
            c_low = category.lower().strip()
            deities = [d for d in deities if c_low in d.category.lower()]
        return deities

    @staticmethod
    def get(name_or_id: str) -> Optional[KumaoniDeity]:
        """Retrieve deity by id (e.g. 'golu_devta') or name."""
        key = name_or_id.lower().replace("-", "_").replace(" ", "_")
        if key in DEITIES_DATA:
            return DEITIES_DATA[key]
        for d in DEITIES_DATA.values():
            if key in d.id or key in d.name_roman.lower() or name_or_id in d.name_kumaoni:
                return d
        return None

    @staticmethod
    def search(query: str) -> List[KumaoniDeity]:
        """Search deities by name, shrine, title, or keywords."""
        q = query.lower().strip()
        return [
            d for d in DEITIES_DATA.values()
            if q in d.name_kumaoni
            or q in d.name_roman.lower()
            or q in d.title.lower()
            or q in d.legend.lower()
            or any(q in s.lower() for s in d.primary_shrines)
        ]

    @staticmethod
    def stats() -> Dict[str, Any]:
        """Summary counts of deities across categories."""
        from collections import Counter
        deities = list(DEITIES_DATA.values())
        cat_counts = Counter(d.category for d in deities)
        return {
            "total_deities": len(deities),
            "categories": dict(cat_counts)
        }
