"""
Kumaoni temple implements, sacred vessels, hawan paraphernalia, and ritual objects.
Catalogues sacred objects used in Kumaoni temples (Dewaal), village hearth shrines (Thaan),
shamanic jagars, and daily household pujas.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict


@dataclass
class KumaoniRitualItem:
    id: str
    name_kumaoni: str
    name_roman: str
    name_hindi: str
    category: str  # "Sacred Mark & Thread", "Vessel & Offering Implement", "Hawan & Fire Sacrifice", "Temple Insignia & Votive Offering", "Jagar & Oracle Implement", "Sacred Attire & Ornaments", "Sacred Water & Sanctum Feature"
    traditional_material: str
    sacred_purpose: str
    cultural_context: str
    associated_deities_or_shrines: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


RITUAL_ITEMS_DATA: Dict[str, KumaoniRitualItem] = {
    # ==================== SACRED MARKS & THREADS ====================
    "pithyan": KumaoniRitualItem(
        id="pithyan",
        name_kumaoni="पिथ्याँ / पिथौं",
        name_roman="Pithyan",
        name_hindi="पिथ्याँ (रोली-हल्दी का तिलक)",
        category="Sacred Mark & Thread",
        traditional_material="Pure Himalayan turmeric powder, lime water, and camphor, creating brilliant red-orange vermilion.",
        sacred_purpose="Vertical sacred tilak drawn with the right ring finger extending from the bridge of the nose upwards to the forehead.",
        cultural_context="Quintessential mark of Kumaoni identity. No puja, temple visit, marriage (Dhuli-argh), or festival begins without elders applying Pithyan. Unmarried girls apply yellow; married women and men receive vibrant red.",
        associated_deities_or_shrines=["Universal across all Kumaoni temples", "Golu Devta", "Nanda Devi", "Bhumia Devta"]
    ),
    "akshat": KumaoniRitualItem(
        id="akshat",
        name_kumaoni="अक्षत",
        name_roman="Akshat",
        name_hindi="अक्षत (अखंडित चावल)",
        category="Sacred Mark & Thread",
        traditional_material="Whole unbroken raw white rice grains.",
        sacred_purpose="Placed firmly over the wet Pithyan mark on the forehead; offered directly to idols during puja.",
        cultural_context="Literally means 'unbroken / undamaged'. Symbolizes wholeness, fertility, and cosmic abundance. Also cast by the Jagariya during 'Akshat-Parkh' to divine the cause of disease or misfortune.",
        associated_deities_or_shrines=["Universal across all temples", "Jagar séances", "Harela sowing"]
    ),
    "kalawa": KumaoniRitualItem(
        id="kalawa",
        name_kumaoni="कलावा / मौली / रक्षासूत्र",
        name_roman="Kalawa / Mauli / Rakshasutra",
        name_hindi="कलावा (मौली)",
        category="Sacred Mark & Thread",
        traditional_material="Unspun spun cotton thread dyed in bright red and golden yellow.",
        sacred_purpose="Consecrated protective thread tied around the right wrist of men and left wrist of women by the temple priest.",
        cultural_context="Known as 'Raksha Sutra' (thread of divine protection). Chanted with the Sanskrit sloka 'Yena baddho Bali raja...'. Protects the bearer from negative vibrations and preserves the merit of the temple visit.",
        associated_deities_or_shrines=["Universal across all Kumaoni temples", "Navratri pujas"]
    ),
    "janeu": KumaoniRitualItem(
        id="janeu",
        name_kumaoni="जनेऊ / जनेव / यज्ञोपवीत",
        name_roman="Janeu / Yajnopavita",
        name_hindi="जनेऊ",
        category="Sacred Mark & Thread",
        traditional_material="Three strands of pure hand-twisted cotton thread representing Brahma, Vishnu, and Shiva (and the three debts).",
        sacred_purpose="Worn over the left shoulder across the chest to the right hip; marker of spiritual initiation and daily Vedic discipline.",
        cultural_context="Conferred during the 'Janeu Sanskar' (Upanayana ceremony), a major family milestone in Kumaon. Renewed annually on 'Janopunyu' (Shravani Purnima / Raksha Bandhan) at sacred river confluences (Bagnath, Rameshwar).",
        associated_deities_or_shrines=["Bagnath Temple", "Jageshwar Dham", "Pancheshwar Sangam"]
    ),
    "roli": KumaoniRitualItem(
        id="roli",
        name_kumaoni="रोली",
        name_roman="Roli",
        name_hindi="रोली (कुमकुम)",
        category="Sacred Mark & Thread",
        traditional_material="Fine red ceremonial powder made of turmeric treated with slaked lime.",
        sacred_purpose="Consecration of temple idols, sacred stones, kalash, and threshold lintels.",
        cultural_context="Used alongside chandan to adorn Shivalingas and Devi icons.",
        associated_deities_or_shrines=["Dunagiri Devi", "Kotgari Devi", "Barahi Devi"]
    ),
    "chandan": KumaoniRitualItem(
        id="chandan",
        name_kumaoni="चन्दन",
        name_roman="Chandan",
        name_hindi="चंदन",
        category="Sacred Mark & Thread",
        traditional_material="Fragrant white or red sandalwood stick rubbed with water on a smooth stone slab (Sil / Batta).",
        sacred_purpose="Cooling fragrant paste applied to Shivalingas, Vishnu idols, and across the brow of devotees.",
        cultural_context="Brings mental peace and serene detachment in high mountain weather.",
        associated_deities_or_shrines=["Jageshwar Dham", "Katarmal Sun Temple", "Binsar Mahadev"]
    ),
    "bhabhoot": KumaoniRitualItem(
        id="bhabhoot",
        name_kumaoni="भभूत / भस्म",
        name_roman="Bhabhoot / Bhasma",
        name_hindi="भभूत (पवित्र राख)",
        category="Sacred Mark & Thread",
        traditional_material="Sacred white ash gathered from the perpetual fire (Dhooni) of Nath yogis, temple hawankunds, or sacred herbal fires.",
        sacred_purpose="Applied as three horizontal lines (Tripundra) across the forehead representing Shiva.",
        cultural_context="Considered a potent shield against evil eye (Nazar) and malevolent spirits (Masan). Blessed bhabhoot from the temple of Golu Devta or Gorakhnath is reverently preserved in homes.",
        associated_deities_or_shrines=["Bholanath", "Kalbisht", "Golu Devta", "Ganganath"]
    ),

    # ==================== VESSELS & OFFERING IMPLEMENTS ====================
    "panchapatra": KumaoniRitualItem(
        id="panchapatra",
        name_kumaoni="पंचपात्र",
        name_roman="Panchapatra",
        name_hindi="पंचपात्र",
        category="Vessel & Offering Implement",
        traditional_material="Hammered copper (Tamra) or heavy brass.",
        sacred_purpose="Tumbler holding consecrated water used for personal purification and offering libations to deities.",
        cultural_context="Represents the five great elements (Pancha Mahabhutas). Placed on the priest's right side during every temple ritual.",
        associated_deities_or_shrines=["Universal across all temple sanctums"]
    ),
    "aachmani": KumaoniRitualItem(
        id="aachmani",
        name_kumaoni="आचमनी",
        name_roman="Aachmani",
        name_hindi="आचमनी (छोटी तांबे की चम्मच)",
        category="Vessel & Offering Implement",
        traditional_material="Engraved copper or brass with hooded snake or peacock handle.",
        sacred_purpose="Scoops three drops of holy water into the palm for ritual sipping (Aachaman) before chanting mantras.",
        cultural_context="Purifies internal speech, breath, and intellect.",
        associated_deities_or_shrines=["Universal across temple sanctums"]
    ),
    "argha": KumaoniRitualItem(
        id="argha",
        name_kumaoni="अरघा",
        name_roman="Argha",
        name_hindi="अरघा (जलाभिषेक पात्र)",
        category="Vessel & Offering Implement",
        traditional_material="Pure spun copper shaped like a small boat or yoni with a drainage spout.",
        sacred_purpose="Suspended above the Shivalinga with a tiny perforation at the base for continuous water dripping (Jaladhara).",
        cultural_context="Maintains perpetual cool abhisheka upon the fiery lingam of Lord Shiva day and night.",
        associated_deities_or_shrines=["Jageshwar Mahadev", "Bagnath", "Mukteshwar", "Baijnath"]
    ),
    "kalash": KumaoniRitualItem(
        id="kalash",
        name_kumaoni="कलश / लोटा",
        name_roman="Kalash / Lota",
        name_hindi="मंगल कलश",
        category="Vessel & Offering Implement",
        traditional_material="Embossed brass or copper filled with Ganga water, coins, betel nut, topped with five mango/panya leaves and a coconut wrapped in red cloth.",
        sacred_purpose="Embodies the universe, all holy tirthas, and Lord Varuna; consecrated at the start of every ceremony.",
        cultural_context="Centerpiece of Navratri Ghatasthapana, wedding Mandap, and temple Pran Pratishtha in Kumaon.",
        associated_deities_or_shrines=["Universal across all temples", "Navratri shrines"]
    ),
    "aarti_thali": KumaoniRitualItem(
        id="aarti_thali",
        name_kumaoni="आरती की थाली",
        name_roman="Aarti ki Thali",
        name_hindi="आरती की थाली",
        category="Vessel & Offering Implement",
        traditional_material="Carved brass or bell-metal featuring five-wick oil lamp (Pancha-pradeep), camphor cup, and flower holders.",
        sacred_purpose="Rotated clockwise in circular motions before the deity during morning and evening sandhya aarti.",
        cultural_context="Devotees pass their hands over the holy flame after aarti and touch their eyes to receive divine grace.",
        associated_deities_or_shrines=["Universal across temples"]
    ),
    "dhoopdani": KumaoniRitualItem(
        id="dhoopdani",
        name_kumaoni="धूपदानी",
        name_roman="Dhoopdani",
        name_hindi="धूपदानी",
        category="Vessel & Offering Implement",
        traditional_material="Heavy cast brass burner with an extended insulated wooden handle.",
        sacred_purpose="Holds burning hardwood charcoal onto which alpine jatamansi, guggul, and incense are showered.",
        cultural_context="Carried by the priest through every corner of the temple to purify the atmosphere with fragrant smoke.",
        associated_deities_or_shrines=["Universal across temples", "Jagar rituals"]
    ),
    "rot": KumaoniRitualItem(
        id="rot",
        name_kumaoni="रोट",
        name_roman="Rot",
        name_hindi="रोट (मीठा मोटा रोट)",
        category="Vessel & Offering Implement",
        traditional_material="Whole wheat flour kneaded with pure cow ghee and thick organic jaggery, slowly baked over hardwood coals.",
        sacred_purpose="The supreme traditional non-cereal sweet offering (Prasad) to village protectors and heroic deities.",
        cultural_context="Mandatory offering to Bhumia Devta, Golu Devta, and Kalbisht at village thans. Cooked with great purity exclusively by men or elderly women on open wood fires.",
        associated_deities_or_shrines=["Bhumia Devta", "Golu Devta", "Kalbisht (Binsar)", "Kailpal Devta"]
    ),
    "panchamrit": KumaoniRitualItem(
        id="panchamrit",
        name_kumaoni="पंचामृत",
        name_roman="Panchamrit",
        name_hindi="पंचामृत",
        category="Vessel & Offering Implement",
        traditional_material="A blend of five holy Himalayan elixirs: raw cow milk, fresh curd, pure desi ghee, mountain honey, and jaggery/sugar.",
        sacred_purpose="Used to bathe the deity's idol during Abhisheka; distributed to devotees as divine sweet nectar.",
        cultural_context="Represents spiritual nourishment, purity, and sweetness in life.",
        associated_deities_or_shrines=["Universal across temples"]
    ),
    "batasha": KumaoniRitualItem(
        id="batasha",
        name_kumaoni="बताशा",
        name_roman="Batasha",
        name_hindi="बताशा",
        category="Vessel & Offering Implement",
        traditional_material="Pure crystallised sugar droplets shaped like airy white domes.",
        sacred_purpose="Everyday temple sweet offering distributed alongside black roasted grams (Chana).",
        cultural_context="Light and imperishable sweet offered at small wayside roadside shrines (Thans) across hill paths.",
        associated_deities_or_shrines=["Village wayside Thans", "Hanuman temples"]
    ),

    # ==================== HAWAN & FIRE SACRIFICE ====================
    "hawankund": KumaoniRitualItem(
        id="hawankund",
        name_kumaoni="हवनकुंड",
        name_roman="Hawankund",
        name_hindi="हवनकुंड",
        category="Hawan & Fire Sacrifice",
        traditional_material="Tiered copper pyramid or baked stone-brick masonry altar smeared with red clay and cow dung.",
        sacred_purpose="Sacred fire vessel in which Agni (the divine messenger) receives oblations of ghee, herbs, and grains.",
        cultural_context="Center of all major Vedic ceremonies in Kumaon, including Shravani Mela at Jageshwar, Navratri, and housewarming (Griha Pravesh).",
        associated_deities_or_shrines=["Jageshwar Dham", "Dunagiri", "Devidhura"]
    ),
    "samidha": KumaoniRitualItem(
        id="samidha",
        name_kumaoni="समिधा",
        name_roman="Samidha",
        name_hindi="समिधा (हवन की पवित्र लकड़ी)",
        category="Hawan & Fire Sacrifice",
        traditional_material="Dry slender twigs cut exclusively from sacred trees: Panya (wild cherry), Pipal, Banjh, Shami, and Mango.",
        sacred_purpose="Fuel for the sacred sacrificial fire, fed systematically into Agni accompanied by Swaha mantras.",
        cultural_context="Never gathered from green living limbs; harvested respectfully from naturally dried branches in sacred groves.",
        associated_deities_or_shrines=["All Hawan rituals across Kumaon"]
    ),
    "sruwa": KumaoniRitualItem(
        id="sruwa",
        name_kumaoni="स्रुवा",
        name_roman="Sruwa",
        name_hindi="स्रुवा (हवन का बड़ा काष्ठ चम्मच)",
        category="Hawan & Fire Sacrifice",
        traditional_material="Carved single piece of sacred wood (Khair or Panya) with a deep oval bowl and long straight handle.",
        sacred_purpose="Used by the chief officiating Brahmin priest to pour continuous streams of clarified ghee into the fire during Purnahuti.",
        cultural_context="Traditional Vedic implement preserved across generations of priest families in Almora and Gangolihat.",
        associated_deities_or_shrines=["Jageshwar Dham", "Vedic Hawans"]
    ),
    "sruch": KumaoniRitualItem(
        id="sruch",
        name_kumaoni="स्रुच",
        name_roman="Sruch",
        name_hindi="स्रुच (हवन का चपटा चम्मच)",
        category="Hawan & Fire Sacrifice",
        traditional_material="Flat carved sacred wooden spoon companion to the Sruwa.",
        sacred_purpose="Holds herbal Hawan Samagri (sesame, barley, jatamansi, camphor) before consigning to the flames.",
        cultural_context="Complements Sruwa to ensure fire is fed without scattering.",
        associated_deities_or_shrines=["Temple Hawans"]
    ),
    "kapoor": KumaoniRitualItem(
        id="kapoor",
        name_kumaoni="कपूर",
        name_roman="Kapoor",
        name_hindi="कपूर",
        category="Hawan & Fire Sacrifice",
        traditional_material="Natural aromatic white crystalline camphor from Himalayan Cinnamomum camphora.",
        sacred_purpose="Burned during aarti in a small brass cup; burns completely without leaving ash or residue.",
        cultural_context="Symbolizes the total burning away of individual ego (Ahamkara) in the light of supreme consciousness.",
        associated_deities_or_shrines=["Universal across temples"]
    ),

    # ==================== TEMPLE INSIGNIA & VOTIVE OFFERINGS ====================
    "ghant": KumaoniRitualItem(
        id="ghant",
        name_kumaoni="घंट / घंटी / डांगर",
        name_roman="Ghant / Ghanti",
        name_hindi="घंट (मंदिर की घंटी)",
        category="Temple Insignia & Votive Offering",
        traditional_material="Resonant bell-metal bronze (Kansa) and cast brass, ranging from handheld bells to massive temple bells weighing hundreds of kilograms.",
        sacred_purpose="Rung by devotees on entering the temple to awaken spiritual vigilance; hung as votive thanksgiving offerings upon fulfillment of prayers.",
        cultural_context="Chitai Golu Devta temple near Almora is world-famous as the 'Temple of Bells' where thousands of brass bells of all sizes are tied along railings by grateful seekers of justice.",
        associated_deities_or_shrines=["Chitai Golu Devta", "Ghorakhal Golu Devta", "Jhula Devi (Ranikhet)"]
    ),
    "shankha": KumaoniRitualItem(
        id="shankha",
        name_kumaoni="शंख",
        name_roman="Shankha",
        name_hindi="शंख",
        category="Temple Insignia & Votive Offering",
        traditional_material="Natural ocean conch shell (Dakshinavarti or Vamavarti) mounted on a brass stand.",
        sacred_purpose="Blown at dawn and sunset during temple aartis; also used to pour consecrated holy water over deity idols.",
        cultural_context="Its deep primordial resonance ('Omkara') purifies mountain valleys and signals the opening of temple portals.",
        associated_deities_or_shrines=["Bagnath", "Jageshwar", "Naina Devi"]
    ),
    "trishul": KumaoniRitualItem(
        id="trishul",
        name_kumaoni="त्रिशूल",
        name_roman="Trishul",
        name_hindi="त्रिशूल",
        category="Temple Insignia & Votive Offering",
        traditional_material="Wrought iron or forged brass with sharp prongs, often bound with red cloth and holy thread.",
        sacred_purpose="Planted upright in open-air stone altars (Thans) and temple yards as the emblem of divine authority and protection.",
        cultural_context="Represents victory over the three pains (Adhyatmika, Adhidaivika, Adhibhautika) and the three Gunas. Planted at shrines of Shiva, Golu Devta, and Bhairav.",
        associated_deities_or_shrines=["Chitai Golu Devta", "Patal Bhuvaneshwar", "Kalbisht", "Kotgari Devi"]
    ),
    "bana_nishan": KumaoniRitualItem(
        id="bana_nishan",
        name_kumaoni="बाना / निशान",
        name_roman="Bana / Nishan",
        name_hindi="निशान (धार्मिक ध्वज)",
        category="Temple Insignia & Votive Offering",
        traditional_material="Saffron, red, or white triangular silk pennant embroidered with trident, sun, or om, mounted on a tall bamboo/panya pole.",
        sacred_purpose="Temple standard and holy herald carried at the head of religious processions, fairs (Melas), and pilgrimage Yatras.",
        cultural_context="Hoisted atop temple spires (Shikhara) to declare the sovereign domain of the deity over the valley.",
        associated_deities_or_shrines=["Nanda Devi Mela", "Chhipla Jaat", "Somnath Mela"]
    ),
    "paati": KumaoniRitualItem(
        id="paati",
        name_kumaoni="पाती",
        name_roman="Paati",
        name_hindi="पाती (न्याय की अर्जी)",
        category="Temple Insignia & Votive Offering",
        traditional_material="Handwritten letter, affidavit on stamp paper, or written legal prayer on paper, tied with red sacred string.",
        sacred_purpose="Formal petition submitted by aggrieved persons directly to Golu Devta (God of Justice) seeking divine arbitration and truth.",
        cultural_context="Unique legal-spiritual tradition of Kumaon. Thousands of personal letters in Kumaoni, Hindi, and English hang on temple cords at Chitai and Ghorakhal.",
        associated_deities_or_shrines=["Chitai Golu Devta", "Ghorakhal Golu Devta", "Chamarkhan Golu Devta"]
    ),
    "chanwar": KumaoniRitualItem(
        id="chanwar",
        name_kumaoni="चँवर / चामर",
        name_roman="Chanwar / Chamar",
        name_hindi="चंवर",
        category="Temple Insignia & Votive Offering",
        traditional_material="Pure white hair from the tail of Himalayan yak, mounted in an intricately chased silver handle.",
        sacred_purpose="Gently waved in rhythmic arcs before deities during royal aarti to symbolize royal divinity and ward off flies.",
        cultural_context="Historically presented by high Himalayan Shauka traders from Johar to the royal temples of Almora and Champawat.",
        associated_deities_or_shrines=["Almora Nanda Devi", "Jageshwar Dham", "Bagnath"]
    ),
    "chhatra": KumaoniRitualItem(
        id="chhatra",
        name_kumaoni="छत्र",
        name_roman="Chhatra",
        name_hindi="छत्र (मुकुट छत्र)",
        category="Temple Insignia & Votive Offering",
        traditional_material="Domed canopy crafted from solid silver, gold foil, or spun brass, embossed with floral and solar motifs.",
        sacred_purpose="Suspended directly over the sanctum idol or Shivalinga signifying celestial sovereignty.",
        cultural_context="Donated as prestigious votive offerings by kings, commanders, and wealthy patrons upon miraculous escapes or prosperity.",
        associated_deities_or_shrines=["Maa Purnagiri", "Barahi Devi", "Naina Devi"]
    ),
    "doli": KumaoniRitualItem(
        id="doli",
        name_kumaoni="डोलि / डोला",
        name_roman="Doli / Dola",
        name_hindi="देव डोली",
        category="Temple Insignia & Votive Offering",
        traditional_material="Carved seasoned deodar wood framed with brass finials, draped in rich silk, brocade, and red velvet.",
        sacred_purpose="Ceremonial palanquin carrying the deity's consecrated bronze mask (Mukhavata) during pilgrimages and village visits.",
        cultural_context="Carried on the shoulders of nominated village devotees; sways rhythmically as the divine presence manifests during Himalayan processions.",
        associated_deities_or_shrines=["Nanda Raj Jaat", "Chhipla Kedar Jaat", "Village dev-kautuk"]
    ),

    # ==================== JAGAR & ORACLE IMPLEMENTS ====================
    "hurka": KumaoniRitualItem(
        id="hurka",
        name_kumaoni="हुड़का",
        name_roman="Hurka",
        name_hindi="हुड़का",
        category="Jagar & Oracle Implement",
        traditional_material="Carved hollow hardwood shell, goatskin membranes tightened with woven cotton cord shoulder-strap.",
        sacred_purpose="Rhythmically played by the chief bard (Jagariya) to recite oral genealogies and awaken local deities during all-night Jagars.",
        cultural_context="Venerated instrument of Kumaon. Treated with puja and Pithyan before any performance; never placed carelessly on the floor.",
        associated_deities_or_shrines=["Golu Devta Jagar", "Bholanath Jagar", "Ganganath Jagar"]
    ),
    "daur": KumaoniRitualItem(
        id="daur",
        name_kumaoni="डौंर",
        name_roman="Daur",
        name_hindi="डौंर (छोटा तांत्रिक डमरू)",
        category="Jagar & Oracle Implement",
        traditional_material="Small heavy wooden barrel drum with leather faces and strike cords.",
        sacred_purpose="Played alongside bell-metal thali in esoteric tantric and guardian invocations (Ghatku, Masan, Airy).",
        cultural_context="Creates urgent driving tempo to facilitate the descent of the spiritual energy into the oracle.",
        associated_deities_or_shrines=["Airy Devta", "Chaumu Devta", "Masan thans"]
    ),
    "kansi_thali": KumaoniRitualItem(
        id="kansi_thali",
        name_kumaoni="कांसी की थाली",
        name_roman="Kansi ki Thali",
        name_hindi="कांसी की थाली (कांस्य थाल)",
        category="Jagar & Oracle Implement",
        traditional_material="High-resonance bell-metal bronze (78% copper, 22% tin) beaten to precise thickness.",
        sacred_purpose="Placed on a wooden support and rapidly struck with a slender split-bamboo or hardwood stick (Kutiya).",
        cultural_context="Its sharp, piercing metallic vibration acts as a psychoacoustic catalyst that induces divine trance (Awat/Bhav) in the Dangariya.",
        associated_deities_or_shrines=["Universal across all Kumaoni Jagar ceremonies"]
    ),
    "bagambar": KumaoniRitualItem(
        id="bagambar",
        name_kumaoni="बगंबर",
        name_roman="Bagambar",
        name_hindi="मृगछाला / बगंबर आसन",
        category="Jagar & Oracle Implement",
        traditional_material="Traditionally deer or leopard skin representation, now woven coarse highland sheep wool rug.",
        sacred_purpose="Seat of meditation and spiritual invocation on which the priest and oracle sit during sacred ceremonies.",
        cultural_context="Insulates the practitioner from earthly currents; symbol of Shiva's ascetic majesty.",
        associated_deities_or_shrines=["All dev-sthan Jagars", "Sadhu dhunis"]
    ),
    "saangal": KumaoniRitualItem(
        id="saangal",
        name_kumaoni="सांगल",
        name_roman="Saangal",
        name_hindi="सांगल (पवित्र लोहे की जंजीर)",
        category="Jagar & Oracle Implement",
        traditional_material="Heavy forged iron chains with thick links, often ending in rings.",
        sacred_purpose="Kept at shrines of wrathful or justice deities; brandished by the Dangariya in trance to demonstrate immunity from pain.",
        cultural_context="Signifies unyielding divine power and absolute fearlessness in the presence of truth.",
        associated_deities_or_shrines=["Chitai Golu Devta", "Kalbisht", "Bhairav thans"]
    ),

    # ==================== SACRED ATTIRE & ORNAMENTS ====================
    "rangwali_pichhaura": KumaoniRitualItem(
        id="rangwali_pichhaura",
        name_kumaoni="रंग्वाली पिछौड़ा",
        name_roman="Rangwali Pichhaura",
        name_hindi="रंग्वाली पिछौड़ा (पारंपरिक दुपट्टा)",
        category="Sacred Attire & Ornaments",
        traditional_material="Fine cotton or silk dyed in saffron-yellow (representing turmeric and sun) and hand-printed with red dots and motifs.",
        sacred_purpose="Worn by all married women during temple pujas, Hawans, weddings, and naming ceremonies.",
        cultural_context="Central motif features a central circle containing the Om, Sun, Moon, Conch, and Swastika, encircled by 28 red auspicious dots (representing lunar mansions / Nakshatras). Embodiment of marital auspiciousness (Suhag).",
        associated_deities_or_shrines=["All temple pilgrimages", "Nanda Devi Mela", "Marriage pujas"]
    ),
    "aanchal": KumaoniRitualItem(
        id="aanchal",
        name_kumaoni="अंचल / गाँठ",
        name_roman="Aanchal",
        name_hindi="अंचल (पवित्र पीत वस्त्र)",
        category="Sacred Attire & Ornaments",
        traditional_material="Unstitched yellow or saffron cloth containing sacred betel nut, turmeric piece, and silver coin.",
        sacred_purpose="Used to tie the sacred nuptial knot (Gathbandhan) between bride and groom or offered as shawl to goddesses.",
        cultural_context="Binding bond of karma, duty, and spiritual partnership.",
        associated_deities_or_shrines=["Marriage rituals", "Goddess shrines"]
    ),

    # ==================== SACRED WATER & SANCTUM FEATURES ====================
    "gangajal": KumaoniRitualItem(
        id="gangajal",
        name_kumaoni="गंगाजल",
        name_roman="Gangajal",
        name_hindi="गंगाजल",
        category="Sacred Water & Sanctum Feature",
        traditional_material="Primal sacred water collected from the Ganges, Bhagirathi, Alaknanda, or holy Kumaoni rivers (Saryu, Kali, Gori Ganga).",
        sacred_purpose="Used for idol purification (Shuddhi), sprinkling across devotees, and dying rites.",
        cultural_context="Stored in copper vessels for years without spoiling; fundamental to all rituals.",
        associated_deities_or_shrines=["Universal across temples"]
    ),
    "naula": KumaoniRitualItem(
        id="naula",
        name_kumaoni="नौला",
        name_roman="Naula",
        name_hindi="नौला (प्राकृतिक बावड़ी)",
        category="Sacred Water & Sanctum Feature",
        traditional_material="Fine hand-carved stone masonry pavilion enclosing a closed subterranean aquifer spring, with steps leading down to clear water.",
        sacred_purpose="Ancient architectural sacred stepwell treated with the exact sanctity of an inner temple sanctum.",
        cultural_context="Every Naula has a carved stone relief of the serpent god (Sheshnaga) guarding the source. Shoes are strictly removed before approaching; women visit with brass water vessels after puja.",
        associated_deities_or_shrines=["Syunarkot Naula", "Ekhathiya Naula (Champawat)", "Jahnavi Naula (Gangolihat)"]
    ),
    "dhaara": KumaoniRitualItem(
        id="dhaara",
        name_kumaoni="धारा / मणिकर्णिका",
        name_roman="Dhaara",
        name_hindi="धारा (पत्थर का जल-स्रोत)",
        category="Sacred Water & Sanctum Feature",
        traditional_material="Chiseled stone waterspout, traditionally carved as a cow's face (Gaumukh), tiger head, or lotus spout.",
        sacred_purpose="Perpetually flowing mountain aquifer stream channeled for bathing before entering temple grounds.",
        cultural_context="Water is revered as living divine ambrosia; holy ablutions performed at dawn.",
        associated_deities_or_shrines=["Panchdhara of Almora", "Bageshwar confluences"]
    ),
    "dhooni": KumaoniRitualItem(
        id="dhooni",
        name_kumaoni="धूणी",
        name_roman="Dhooni",
        name_hindi="धूणी (निरंतर प्रज्वलित अग्नि)",
        category="Sacred Water & Sanctum Feature",
        traditional_material="Sunken circular firepit filled with glowing logs of oak and deodar, generating constant sacred ash.",
        sacred_purpose="Perpetual sacred fire kept burning continuously day and night by yogis, ascetics, and shrine keepers.",
        cultural_context="Symbol of non-dual consciousness and constant tapasya; devotees sit around it in silent communion.",
        associated_deities_or_shrines=["Gorakhnath ashrams", "Haat Kalika Gangolihat", "Devidhura"]
    ),
    "pindi": KumaoniRitualItem(
        id="pindi",
        name_kumaoni="पिंडी",
        name_roman="Pindi",
        name_hindi="पिंडी (स्वयंभू शिला)",
        category="Sacred Water & Sanctum Feature",
        traditional_material="Naturally water-smoothed monolithic rock or subterranean stalagmite/stalactite formation (Svayambhu).",
        sacred_purpose="Primary manifestation of goddess or deity worshipped without anthropomorphic carving.",
        cultural_context="The innermost shrines of Maa Purnagiri, Barahi Devi, and Patal Bhuvaneshwar consist of venerated stone pindis covered in pithyan, flowers, and silver umbrellas.",
        associated_deities_or_shrines=["Maa Purnagiri", "Barahi Devi (Devidhura)", "Patal Bhuvaneshwar", "Kotgari Devi"]
    ),
    "thaan": KumaoniRitualItem(
        id="thaan",
        name_kumaoni="थान / द्यो-थान",
        name_roman="Thaan / Dyo-Thaan",
        name_hindi="थान (ग्रामीण देवस्थल)",
        category="Sacred Water & Sanctum Feature",
        traditional_material="Open-air dry-stone raised platform located under a sacred Banjh or Pipal tree, atop a ridge, or beside a field.",
        sacred_purpose="Local sanctum and seat of Gram Devtas, Kshetrapals, and forest spirits (Bhumia, Kalbisht, Airy).",
        cultural_context="The heart of community faith. Villagers offer the first harvest sheaves, sweet rot, and milk directly at the village Thaan.",
        associated_deities_or_shrines=["Bhumia Devta", "Kalbisht", "Saim Devta", "Airy Devta"]
    ),
    "dewaal": KumaoniRitualItem(
        id="dewaal",
        name_kumaoni="देवाल / मन्दिरा",
        name_roman="Dewaal / Mandira",
        name_hindi="देवाल (पत्थर का भव्य मंदिर)",
        category="Sacred Water & Sanctum Feature",
        traditional_material="Dressed stone blocks assembled with mortise-and-tenon joints, featuring towering curvi-linear shikhara and amalaka.",
        sacred_purpose="Sacred temple complex housing the consecrated deity in the garbhagriha.",
        cultural_context="Exemplified by the classical Katyuri and Chand stone architecture of Jageshwar, Baijnath, and Katarmal.",
        associated_deities_or_shrines=["Jageshwar Dham", "Baijnath", "Bagnath", "Katarmal"]
    ),
}


class RitualsTreasury:
    """Query, inspect, and explore Kumaoni temple items, sacred vessels, and ritual objects."""

    @classmethod
    def list(cls, category: Optional[str] = None) -> List[KumaoniRitualItem]:
        if category:
            cat_lower = category.strip().lower()
            return [r for r in RITUAL_ITEMS_DATA.values() if cat_lower in r.category.lower()]
        return list(RITUAL_ITEMS_DATA.values())

    @classmethod
    def get(cls, id_or_name: str) -> Optional[KumaoniRitualItem]:
        if not id_or_name:
            return None
        key = id_or_name.strip().lower().replace(" ", "_")
        if key in RITUAL_ITEMS_DATA:
            return RITUAL_ITEMS_DATA[key]
        for r in RITUAL_ITEMS_DATA.values():
            if (id_or_name in r.name_kumaoni or
                key == r.name_roman.lower() or
                key == r.name_hindi.lower()):
                return r
        return None

    @classmethod
    def search(cls, query: str) -> List[KumaoniRitualItem]:
        if not query:
            return cls.list()
        q = query.strip().lower()
        results = []
        for r in RITUAL_ITEMS_DATA.values():
            if (q in r.name_kumaoni.lower() or
                q in r.name_roman.lower() or
                q in r.name_hindi.lower() or
                q in r.category.lower() or
                q in r.traditional_material.lower() or
                q in r.sacred_purpose.lower() or
                q in r.cultural_context.lower() or
                any(q in shrine.lower() for shrine in r.associated_deities_or_shrines)):
                results.append(r)
        return results

    @classmethod
    def stats(cls) -> Dict[str, Any]:
        categories: Dict[str, int] = {}
        for r in RITUAL_ITEMS_DATA.values():
            categories[r.category] = categories.get(r.category, 0) + 1
        return {
            "total_ritual_items": len(RITUAL_ITEMS_DATA),
            "categories": categories,
        }
