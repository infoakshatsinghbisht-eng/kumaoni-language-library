"""
Sacred temples, historic shrines, holy rivers, Himalayan peaks, and cultural places of Kumaon.
Covering 50 major temples, dhams, sangams, valleys, alpine peaks, and historic centers of Uttarakhand.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict


@dataclass
class KumaoniPlace:
    id: str
    name_kumaoni: str
    name_roman: str
    title: str
    category: str  # "Temple & Sacred Dham", "River & Confluence", "Alpine Peak & Glacier", "Valley, Pass & Town"
    district: str  # "Almora", "Nainital", "Pithoragarh", "Bageshwar", "Champawat", "Udham Singh Nagar"
    altitude_or_location: str
    spiritual_or_historical_significance: str
    description: str
    associated_deities_or_fairs: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


PLACES_DATA: Dict[str, KumaoniPlace] = {
    # ==================== TEMPLES & SACRED DHAMS ====================
    "jageshwar_dham": KumaoniPlace(
        id="jageshwar_dham",
        name_kumaoni="जागेश्वर धाम",
        name_roman="Jageshwar Dham",
        title="Ancient Valley of 124 Stone Temples & 8th Jyotirlinga Sanctuary",
        category="Temple & Sacred Dham",
        district="Almora",
        altitude_or_location="1,870 m (36 km northeast of Almora in Jataganga valley)",
        spiritual_or_historical_significance="Revered as Nagesh Darukavane (the 8th among the twelve holy Jyotirlingas of Lord Shiva) and seat of Lakulisha Shaivism.",
        description="A magnificent forest complex of over 124 stone temples dating from the 7th to 14th century CE built by the Katyuri and Chand dynasties amidst towering deodars. Features Maha Mrityunjaya temple, Dandeshwar, and Jageshwar Mahadev.",
        associated_deities_or_fairs=["Lord Shiva (Maha Mrityunjaya)", "Jhakar Saim", "Pushti Devi", "Jageshwar Shravani Mela"]
    ),
    "baijnath_temple": KumaoniPlace(
        id="baijnath_temple",
        name_kumaoni="बैजनाथ मन्दिर",
        name_roman="Baijnath Temple",
        title="Capital Sanctuary of Katyuri Kings on the Banks of River Gomti",
        category="Temple & Sacred Dham",
        district="Bageshwar",
        altitude_or_location="1,126 m (Katyur Valley, 17 km from Kausani)",
        spiritual_or_historical_significance="Ancient royal religious seat of the Katyuri Empire (Kartikeyapura); renowned for its flawless black chlorite stone murti of Goddess Parvati.",
        description="A 12th-century stone temple cluster situated along the emerald Gomti river. The principal sanctum houses Shiva and a breathtaking 1.5-meter standing statue of Goddess Parvati carved with exquisite ornaments.",
        associated_deities_or_fairs=["Vaidyanath Shiva", "Maa Parvati", "Kot Bhramari", "Mahashivratri Mela"]
    ),
    "bagnath_temple": KumaoniPlace(
        id="bagnath_temple",
        name_kumaoni="बागनाथ मन्दिर (बागेश्वर)",
        name_roman="Bagnath Temple (Bageshwar)",
        title="Ancient Tiger-Form Shiva Shrine at the Saryu-Gomti Sangam",
        category="Temple & Sacred Dham",
        district="Bageshwar",
        altitude_or_location="960 m (Confluence of Saryu and Gomti rivers)",
        spiritual_or_historical_significance="Where sage Markandeya worshipped Lord Shiva; Shiva manifested in the form of a tiger (Vaghrasvara / Bagnath) to bless sage Vashishta.",
        description="A monumental Nagar-style stone temple with towering spires built in 1602 CE by Chand ruler Laxmi Chand. Centered at the sacred confluence, it is the epicenter of the historic Uttarayani fair.",
        associated_deities_or_fairs=["Bagnath Shiva", "Bhairav", "Ganesh", "Uttarayani Mela"]
    ),
    "patal_bhuvaneshwar": KumaoniPlace(
        id="patal_bhuvaneshwar",
        name_kumaoni="पाताल भुवनेश्वर",
        name_roman="Patal Bhuvaneshwar",
        title="Subterranean Cave Temple of 33 Crore Divine Mysteries",
        category="Temple & Sacred Dham",
        district="Pithoragarh",
        altitude_or_location="1,350 m (14 km from Gangolihat)",
        spiritual_or_historical_significance="Described in Skanda Purana (Manaskhanda); an underground limestone cave 160m long and 90ft deep holding stalactite and stalagmite representations of cosmic creation.",
        description="Entered through a steep narrow iron chain tunnel, this mystical cavern reveals natural mineral formations of Sheshnag's hood, Kamadhenu's udders, Ganesha's severed head, and the Kalpvriksha tree.",
        associated_deities_or_fairs=["Lord Shiva", "Sheshnag", "Ganesha", "Mahashivratri Pilgrimage"]
    ),
    "chitai_golu": KumaoniPlace(
        id="chitai_golu",
        name_kumaoni="चितई गोलू देवता मन्दिर",
        name_roman="Chitai Golu Devta Temple",
        title="Supreme Temple of Justice & Thousand Brass Bells",
        category="Temple & Sacred Dham",
        district="Almora",
        altitude_or_location="1,700 m (8 km from Almora on Pithoragarh highway)",
        spiritual_or_historical_significance="Supreme divine court where devotees submit stamp-paper petitions; every answered prayer is commemorated with a dedicated brass temple bell.",
        description="Perched amidst fragrant chir pine ridges, the entire temple sanctuary is draped in hundreds of thousands of ringing brass bells and written legal appeals addressed directly to Goril Devta.",
        associated_deities_or_fairs=["Golu Devta (Goril)", "Kalbisht", "Bhairav", "Chitai Golu Mela"]
    ),
    "katarmal_sun_temple": KumaoniPlace(
        id="katarmal_sun_temple",
        name_kumaoni="कटारमल सूर्य मन्दिर (बड़ा आदित्य)",
        name_roman="Katarmal Sun Temple (Bara Aditya)",
        title="9th-Century Himalayan Solar Sanctuary of Sun God Aditya",
        category="Temple & Sacred Dham",
        district="Almora",
        altitude_or_location="2,116 m (17 km from Almora)",
        spiritual_or_historical_significance="The second most significant Sun Temple in India after Konark, built by Katyuri ruler Katarmalla in the 9th century CE.",
        description="A grand stone temple complex comprising 45 smaller subsidiary shrines clustered around the magnificent central spire of Bara Aditya, capturing the first dawn rays of sunlight.",
        associated_deities_or_fairs=["Surya Dev (Aditya)", "Shiva", "Vishnu", "Rishi Katarmal"]
    ),
    "kasar_devi_temple": KumaoniPlace(
        id="kasar_devi_temple",
        name_kumaoni="कसार देवी मन्दिर",
        name_roman="Kasar Devi Temple",
        title="2nd-Century BCE Cave Sanctuary on the Cosmic Van Allen Belt",
        category="Temple & Sacred Dham",
        district="Almora",
        altitude_or_location="2,116 m (8 km from Almora on Crank's Ridge)",
        spiritual_or_historical_significance="Positioned on a rare geomagnetic anomaly recognized by NASA (shared with Stonehenge and Machu Picchu); sanctuary of Swami Vivekananda, Lama Govinda, and Bob Dylan.",
        description="An ancient rock-cut cave temple dedicated to Goddess Durga slaying Mahishasura. Sits atop Crank's Ridge offering panoramic vistas from Bandarpunch to Panchachuli.",
        associated_deities_or_fairs=["Kasar Devi (Durga)", "Lord Shiva", "Kasar Devi Mela (Kartik Purnima)"]
    ),
    "haat_kalika": KumaoniPlace(
        id="haat_kalika",
        name_kumaoni="हाट कालिका (गंगोलीहाट)",
        name_roman="Haat Kalika (Gangolihat)",
        title="Fierce Mahakali Shaktipeeth & Patron Guardian of Kumaon Regiment",
        category="Temple & Sacred Dham",
        district="Pithoragarh",
        altitude_or_location="1,760 m (Gangolihat town)",
        spiritual_or_historical_significance="Chosen by Adi Shankaracharya to quell the terrifying Kali energy with a Sri Yantra; soldiers of the Kumaon Regiment never depart for battle without Her blessings.",
        description="Set deep within an ancient deodar grove, the temple radiates immense spiritual power. Soldiers and villagers offer red flags, silver tridents, and drums in gratitude.",
        associated_deities_or_fairs=["Maa Mahakali", "Bhairav", "Navratri Mela", "Chaitra Ashtami"]
    ),
    "maa_barahi_devidhura": KumaoniPlace(
        id="maa_barahi_devidhura",
        name_kumaoni="माँ बाराही मन्दिर (देवीधुरा)",
        name_roman="Maa Barahi Temple (Devidhura)",
        title="Mystic Cave Grotto of the Epic Bagwal Stone Battle",
        category="Temple & Sacred Dham",
        district="Champawat",
        altitude_or_location="1,980 m (45 km from Lohaghat)",
        spiritual_or_historical_significance="Ancient cave shrine between colossal megalithic granite boulders; legendary site where the four warrior clans (Khams) offer blood through stones during Bagwal.",
        description="The deity is enshrined inside a concealed copper basket within a granite fissure, opened only by blindfolded priests during the annual Shravani Purnima festival.",
        associated_deities_or_fairs=["Maa Barahi", "Bhumia Devta", "Bagwal Mela", "Navratri Fairs"]
    ),
    "maa_purnagiri": KumaoniPlace(
        id="maa_purnagiri",
        name_kumaoni="माँ पूर्णागिरि धाम",
        name_roman="Maa Purnagiri Dham",
        title="Sacred Naval Shaktipeeth Overlooking River Sharda",
        category="Temple & Sacred Dham",
        district="Champawat",
        altitude_or_location="1,710 m (20 km from Tanakpur on Indo-Nepal border)",
        spiritual_or_historical_significance="One of the 108 supreme Shaktipeeths where Sati's naval (nabhi) fell as Shiva carried Her body across the heavens.",
        description="Perched upon a jagged, wind-swept limestone ridge looking across the plains of Terai and the Sharda river into Nepal. Attracts millions of pilgrims during Chaitra Navratri.",
        associated_deities_or_fairs=["Maa Purnagiri", "Bhairav Devta", "Purnagiri Mela (Chaitra)"]
    ),
    "kainchi_dham": KumaoniPlace(
        id="kainchi_dham",
        name_kumaoni="कैंची धाम",
        name_roman="Kainchi Dham",
        title="Himalayan Spiritual Ashram of Neem Karoli Baba",
        category="Temple & Sacred Dham",
        district="Nainital",
        altitude_or_location="1,400 m (17 km from Nainital on Almora highway)",
        spiritual_or_historical_significance="Founded in 1964 by the saint Neem Karoli Baba (Maharaj-ji); renowned worldwide as a center of devotion, peace, and selfless service.",
        description="Tucked inside a scissor-like mountain pass ('Kainchi'), this serene riverfront temple is dedicated to Lord Hanuman. Renowned for its massive annual June 15 Bhandara festival.",
        associated_deities_or_fairs=["Neem Karoli Baba", "Lord Hanuman", "Kainchi Dham Foundation Mela (15 June)"]
    ),
    "dunagiri_temple": KumaoniPlace(
        id="dunagiri_temple",
        name_kumaoni="दूनागिरि मन्दिर (द्रोणागिरि)",
        name_roman="Dunagiri Temple (Dronagiri)",
        title="Vaishnavi Shaktipeeth & Vedic Herbal Sanctuary of Sage Garg",
        category="Temple & Sacred Dham",
        district="Almora",
        altitude_or_location="2,438 m (14 km from Dwarahat)",
        spiritual_or_historical_significance="According to Ramayana lore, a piece of the medicinal Sanjeevani hill fell here as Hanuman flew north to Lanka; hermitage of sage Garg.",
        description="Reached via 500 stone stairs climbing through oak woods to a breezy summit temple with panoramic views of the Trishul and Nanda Devi peaks.",
        associated_deities_or_fairs=["Dunagiri Devi (Vaishnavi)", "Sage Garg", "Dunagiri Navratri Mela"]
    ),
    "binsar_mahadev": KumaoniPlace(
        id="binsar_mahadev",
        name_kumaoni="बिनसर महादेव",
        name_roman="Binsar Mahadev",
        title="10th-Century Forest Sanctuary of Lord Shiva",
        category="Temple & Sacred Dham",
        district="Almora",
        altitude_or_location="2,480 m (Near Ranikhet & Sony village)",
        spiritual_or_historical_significance="Built by King Pithu Chand in the 10th century CE in memory of his father Bindu; sanctified by natural water springs flowing into stone kunds.",
        description="Set inside a fairy-tale clearing surrounded by towering deodars and pines, this peaceful temple houses unique idols of Har Gauri, Maheshmardini, and a central Shivalinga.",
        associated_deities_or_fairs=["Lord Shiva (Bindeshwar)", "Maa Gauri", "Vaikunth Chaturdashi Mela"]
    ),
    "someshwar_temple": KumaoniPlace(
        id="someshwar_temple",
        name_kumaoni="सोमेश्वर महादेव",
        name_roman="Someshwar Mahadev",
        title="Ancient Royal Shivalinga Shrine of Chand Dynasty Founder",
        category="Temple & Sacred Dham",
        district="Almora",
        altitude_or_location="1,450 m (Kosi river valley)",
        spiritual_or_historical_significance="Consecrated by King Som Chand, the founder of the Chand Dynasty of Kumaon, merging his name with Lord Shiva.",
        description="Lies in the center of the lush Someshwar paddy valley along the Kosi river. Dedicated to Lord Shiva with ancient stone inscriptions and brass tridents.",
        associated_deities_or_fairs=["Someshwar Shiva", "Someshwar Mela", "Mahashivratri"]
    ),
    "mukteshwar_dham": KumaoniPlace(
        id="mukteshwar_dham",
        name_kumaoni="मुक्तेश्वर महादेव मन्दिर",
        name_roman="Mukteshwar Mahadev Temple",
        title="350-Year-Old Shiva Sanctuary Overlooking Chauli ki Jali Cliffs",
        category="Temple & Sacred Dham",
        district="Nainital",
        altitude_or_location="2,286 m (Highest point of Mukteshwar ridge)",
        spiritual_or_historical_significance="Believed to be where Lord Shiva granted liberation ('Mukti') to a slain demon; surrounded by ancient rock-climbing cliffs of Chauli ki Jali.",
        description="A white stone temple crowning the highest ridge of Mukteshwar. Offers stunning unobstructed vistas of the complete Nanda Devi, Trishul, and Panchachuli ranges.",
        associated_deities_or_fairs=["Lord Shiva", "Bhairav", "Chauli ki Jali Legends", "Mahashivratri"]
    ),
    "naina_devi_temple": KumaoniPlace(
        id="naina_devi_temple",
        name_kumaoni="नैना देवी मन्दिर",
        name_roman="Naina Devi Temple",
        title="Sacred Eye Shaktipeeth on the Shore of Naini Lake",
        category="Temple & Sacred Dham",
        district="Nainital",
        altitude_or_location="1,938 m (Northern bank of Naini Lake / Mallital)",
        spiritual_or_historical_significance="Revered spot where Goddess Sati's eyes (Nayan) fell, giving the lake and town its name Nainital.",
        description="Rebuilt after the catastrophic 1880 landslide. Houses two divine eyes representing Goddess Naina Devi alongside Goddess Kali and Lord Ganesha.",
        associated_deities_or_fairs=["Maa Naina Devi", "Maa Kali", "Nanda Devi Mela", "Navratri"]
    ),
    "kot_bhramari": KumaoniPlace(
        id="kot_bhramari",
        name_kumaoni="कोट भ्रामरी मन्दिर (कोट की माई)",
        name_roman="Kot Bhramari Temple (Kot ki Mai)",
        title="Fortress Citadel Shrine of the Katyuri Dynasty",
        category="Temple & Sacred Dham",
        district="Bageshwar",
        altitude_or_location="1,250 m (Ridge above Baijnath)",
        spiritual_or_historical_significance="Ancient fortress and guardian goddess of the Katyuri kings who ruled Kumaon for centuries from Kartikeyapura.",
        description="Stands upon a defensive hill overlooking Baijnath and the entire Katyur valley. Revered during Nanda Ashtami when devotees climb the ridge in massive processions.",
        associated_deities_or_fairs=["Goddess Bhramari", "Nanda Devi", "Kot Bhramari Mela"]
    ),
    "chaiti_mandir": KumaoniPlace(
        id="chaiti_mandir",
        name_kumaoni="चैती मन्दिर (माँ बालसुन्दरी)",
        name_roman="Chaiti Temple (Maa Balasundari)",
        title="Ancient Terai-Foothill Shakti Shrine of Kashipur",
        category="Temple & Sacred Dham",
        district="Udham Singh Nagar",
        altitude_or_location="218 m (Kashipur town)",
        spiritual_or_historical_significance="Ancient shrine of the Chand and Harsha eras; hosts the immense Chaiti Mela drawing devotees from across the plains and hills.",
        description="Dedicated to Maa Balasundari, an incarnation of Goddess Durga. Connected to the ancient archaeological mound of Drona Sagar.",
        associated_deities_or_fairs=["Maa Balasundari", "Chaiti Mela", "Drona Sagar"]
    ),
    "mostamanu_temple": KumaoniPlace(
        id="mostamanu_temple",
        name_kumaoni="मोस्टामानु मन्दिर (चंडक)",
        name_roman="Mostamanu Temple (Chandak)",
        title="Hilltop Rain God Sanctuary of Sor Valley",
        category="Temple & Sacred Dham",
        district="Pithoragarh",
        altitude_or_location="1,950 m (6 km from Pithoragarh town atop Chandak)",
        spiritual_or_historical_significance="Dedicated to Mosta Devta, the sovereign god of rainfall, bountiful crops, and pastoral security in eastern Kumaon.",
        description="A serene hilltop temple amidst whispering pines overlooking the vast expanse of Pithoragarh town and the Himalayan snow peaks.",
        associated_deities_or_fairs=["Mosta Devta", "Mostamanu Mela (August-September)"]
    ),
    "ghorakhal_golu": KumaoniPlace(
        id="ghorakhal_golu",
        name_kumaoni="घोड़ाखाल गोलू देवता",
        name_roman="Ghorakhal Golu Devta",
        title="Lake District Sanctuary of Justice Overlooking Bhimtal",
        category="Temple & Sacred Dham",
        district="Nainital",
        altitude_or_location="1,800 m (Near Bhowali & Sainik School Ghorakhal)",
        spiritual_or_historical_significance="One of the principal shrines of Golu Devta, surrounded by prayer bells and legal petitions.",
        description="Perched upon a tranquil mountain slope surrounded by oak forests, offering panoramic views of Bhimtal lake below.",
        associated_deities_or_fairs=["Golu Devta", "Bhairav", "Ghorakhal Fairs"]
    ),
    "syahi_devi_temple": KumaoniPlace(
        id="syahi_devi_temple",
        name_kumaoni="स्याही देवी मन्दिर (शीतलाखेत)",
        name_roman="Syahi Devi Temple (Shitlakhet)",
        title="Crest Mountain Sanctuary of Meditation & Herbal Forests",
        category="Temple & Sacred Dham",
        district="Almora",
        altitude_or_location="2,200 m (Summit above Shitlakhet village)",
        spiritual_or_historical_significance="Where Swami Vivekananda meditated on his Himalayan journey; patron hilltop goddess protecting the Syahi hills.",
        description="Surrounded by dense oak, pine, and rhododendron forests, this peaceful ridge temple provides panoramic 360-degree views of the Greater Himalayas.",
        associated_deities_or_fairs=["Syahi Devi", "Lord Shiva", "Navratri Celebrations"]
    ),
    "jhula_devi_temple": KumaoniPlace(
        id="jhula_devi_temple",
        name_kumaoni="झूला देवी मन्दिर (चौबटिया)",
        name_roman="Jhula Devi Temple (Chaubattia)",
        title="8th-Century Goddess of the Wooden Cradle & Countless Bells",
        category="Temple & Sacred Dham",
        district="Almora",
        altitude_or_location="1,950 m (7 km from Ranikhet near apple orchards of Chaubattia)",
        spiritual_or_historical_significance="Legend holds that the deity requested a swing (jhula) to rest; devotees whose wishes are granted tie a brass bell to her compound.",
        description="A forest sanctuary draped in tens of thousands of ringing bells, with idols resting gracefully in a decorated wooden cradle.",
        associated_deities_or_fairs=["Goddess Durga (Jhula Devi)", "Lord Rama", "Navratri Fairs"]
    ),

    # ==================== RIVERS & SACRED CONFLUENCES ====================
    "saryu_river": KumaoniPlace(
        id="saryu_river",
        name_kumaoni="सरयू नदी",
        name_roman="Saryu River",
        title="Sacred Lifeline River of Kumaon Originating at Sarmul",
        category="River & Confluence",
        district="Bageshwar",
        altitude_or_location="Originates at 3,500 m near Nanda Kot; flows through Bageshwar to Pancheshwar",
        spiritual_or_historical_significance="The holiest river of central Kumaon; mentioned in Manaskhanda as carrying the spiritual merit of Ganga.",
        description="Flows through rugged canyons, nurturing fertile valleys of Kapkot, Bageshwar, Seraghat, and Rameshwar before merging into the Kali at Pancheshwar.",
        associated_deities_or_fairs=["Bagnath Shiva", "Uttarayani Mela", "Pancheshwar Sangam"]
    ),
    "gomti_river": KumaoniPlace(
        id="gomti_river",
        name_kumaoni="गोमती नदी (कुमाऊँ)",
        name_roman="Gomti River (Kumaon)",
        title="Katyuri Valley River Nurturing Ancient Rice Terraces",
        category="River & Confluence",
        district="Bageshwar",
        altitude_or_location="Originates in Bhatkot ranges; flows through Baijnath to Bageshwar",
        spiritual_or_historical_significance="The holy river that watered the royal paddies of Kartikeyapura; forms the sacred Sangam at Bageshwar.",
        description="Meanders gently through the broad, emerald Katyur valley past the ancient stone temples of Baijnath before meeting the Saryu at Bagnath.",
        associated_deities_or_fairs=["Baijnath Shiva", "Bagnath", "Uttarayani"]
    ),
    "kali_river": KumaoniPlace(
        id="kali_river",
        name_kumaoni="काली / शारदा नदी",
        name_roman="Kali / Sharda River",
        title="Mighty Himalayan Boundary River of Indo-Nepal Frontier",
        category="River & Confluence",
        district="Pithoragarh",
        altitude_or_location="Originates at Kalapani (3,600 m); flows through Dharchula, Jhulaghat, to Tanakpur",
        spiritual_or_historical_significance="Named after Goddess Kali at her high shrine in Kalapani; acts as the international border between India and Nepal.",
        description="A thunderous, turquoise torrent carving dramatic deep gorges through the trans-Himalayan crags of Vyas and Byans before broadening into the Sharda at Tanakpur.",
        associated_deities_or_fairs=["Goddess Kali at Kalapani", "Purnagiri Devi", "Jauljibi Mela", "Pancheshwar"]
    ),
    "gori_ganga": KumaoniPlace(
        id="gori_ganga",
        name_kumaoni="गोरी गंगा नदी",
        name_roman="Gori Ganga River",
        title="Glacial Torrent of the Johar Valley Emerging from Milam Glacier",
        category="River & Confluence",
        district="Pithoragarh",
        altitude_or_location="Originates at Milam Glacier (3,600 m); joins Kali at Jauljibi",
        spiritual_or_historical_significance="The glacial lifeblood of the Shauka community and trans-Himalayan traders.",
        description="Rushes with milky-white glacial silt through the breathtaking gorges of Munsyari, Madkot, and Baram before joining the dark Kali river at Jauljibi.",
        associated_deities_or_fairs=["Milam Shrine", "Jauljibi Mela", "Hot sulphur springs of Madkot"]
    ),
    "ramganga_east": KumaoniPlace(
        id="ramganga_east",
        name_kumaoni="पूर्वी रामगंगा नदी",
        name_roman="Eastern Ramganga River",
        title="Glacial River Born from Namik Glacier & Saryu Tributary",
        category="River & Confluence",
        district="Pithoragarh",
        altitude_or_location="Originates at Namik Glacier (3,600 m); meets Saryu at Rameshwar",
        spiritual_or_historical_significance="Consecrated by sage Rama at Rameshwar Sangam in Gangolihat.",
        description="Carves through the high gorges of Munsyari, Tejam, Thal, and Nachni before its scenic meeting with the Saryu at Rameshwar.",
        associated_deities_or_fairs=["Rameshwar Mahadev", "Thal Mela", "Namik Glacier"]
    ),
    "kosi_river": KumaoniPlace(
        id="kosi_river",
        name_kumaoni="कोसी नदी (कौशिकी)",
        name_roman="Kosi River (Kaushiki)",
        title="Sacred River of Sage Kaushika Nurturing Almora & Corbett Foothills",
        category="River & Confluence",
        district="Almora",
        altitude_or_location="Originates at Kausani / Bhatkot; flows past Someshwar and Almora to Ramnagar",
        spiritual_or_historical_significance="Revered in Hindu epics as River Kaushiki, associated with sage Vishwamitra.",
        description="Waters the fertile valley of Someshwar, flows around the base of Almora ridge, and cuts through deep granite ravines into Corbett National Park.",
        associated_deities_or_fairs=["Someshwar Mahadev", "Katarmal Sun Temple", "Garjiya Devi (Ramnagar)"]
    ),
    "gaula_river": KumaoniPlace(
        id="gaula_river",
        name_kumaoni="गौला नदी",
        name_roman="Gaula River",
        title="Foothill River of the Katyuri Queen & Gateway to the Hills",
        category="River & Confluence",
        district="Nainital",
        altitude_or_location="Originates in Sattal / Mornaula hills; flows past Ranibagh and Kathgodam",
        spiritual_or_historical_significance="Sacred site where Katyuri Queen Jiya Rani fought and attained immortal folk deity status at Chitrashila (Ranibagh).",
        description="The primary water source for Haldwani and the Bhabar plain, emerging from rocky hill canyons into wide gravel beds.",
        associated_deities_or_fairs=["Jiya Rani", "Chitrashila Ghat", "Ranibagh Uttarayani Mela"]
    ),
    "bageshwar_sangam": KumaoniPlace(
        id="bageshwar_sangam",
        name_kumaoni="बागेश्वर संगम (सरयू-गोमती संगम)",
        name_roman="Bageshwar Sangam (Saryu-Gomti)",
        title="The Kashi of Kumaon & Epicenter of Makar Sankranti",
        category="River & Confluence",
        district="Bageshwar",
        altitude_or_location="Confluence in Bageshwar town",
        spiritual_or_historical_significance="The most sacred river junction in Kumaon, compared in sanctity to Varanasi; location of the historic 1921 Coolie-Begar movement ledger immersion.",
        description="Flanked by the temples of Bagnath and Chandika, thousands take ritual holy dips during Uttarayani.",
        associated_deities_or_fairs=["Bagnath Shiva", "Uttarayani Mela", "Coolie-Begar Historic Site"]
    ),
    "jauljibi_sangam": KumaoniPlace(
        id="jauljibi_sangam",
        name_kumaoni="जौलजीबी संगम (काली-गोरी संगम)",
        name_roman="Jauljibi Sangam (Kali-Gori)",
        title="Tri-Nation Confluence of Shauka, Nepali & Kumaoni Traders",
        category="River & Confluence",
        district="Pithoragarh",
        altitude_or_location="Confluence in Jauljibi town",
        spiritual_or_historical_significance="Dramatic natural boundary where milky Gori Ganga merges into the dark emerald waters of the Kali.",
        description="Hosts the century-old international trade fair where carpets, woolens, herbs, and pashmina shawls are traded across borders.",
        associated_deities_or_fairs=["Jauljibi Mela", "Kali Mata", "Trans-border Suspension Bridge"]
    ),
    "pancheshwar_sangam": KumaoniPlace(
        id="pancheshwar_sangam",
        name_kumaoni="पंचेश्वर संगम (काली-सरयू संगम)",
        name_roman="Pancheshwar Sangam (Kali-Saryu)",
        title="Mighty River Confluence & Seat of Chaumu Devta",
        category="River & Confluence",
        district="Champawat",
        altitude_or_location="At the confluence of Kali and Saryu rivers on Indo-Nepal border",
        spiritual_or_historical_significance="Sacred shrine of Chaumu Devta (protector of cattle); devotees offer unboiled milk directly into the swirling waters.",
        description="A dramatic, remote canyon where the two largest river systems of Kumaon unite into a thunderous international waterway.",
        associated_deities_or_fairs=["Chaumu Devta", "Mahashivratri Mela", "Kali-Saryu Confluence"]
    ),

    # ==================== ALPINE PEAKS & GLACIERS ====================
    "nanda_devi_peak": KumaoniPlace(
        id="nanda_devi_peak",
        name_kumaoni="नंदा देवी शिखर",
        name_roman="Nanda Devi Peak",
        title="7,816 m Bliss-Giving Goddess Summit & Jewel of Uttarakhand",
        category="Alpine Peak & Glacier",
        district="Bageshwar",
        altitude_or_location="7,816 m (Border of Chamoli and Pithoragarh/Bageshwar)",
        spiritual_or_historical_significance="Highest peak wholly within India; worshipped across every village in Kumaon and Garhwal as the living Mother Goddess.",
        description="Surrounded by a double ring of impenetrable glaciated peaks forming the Nanda Devi Sanctuary (UNESCO World Heritage Site).",
        associated_deities_or_fairs=["Maa Nanda Devi", "Nanda Raj Jaat", "Nanda Devi Mela"]
    ),
    "trishul_peak": KumaoniPlace(
        id="trishul_peak",
        name_kumaoni="त्रिशूल शिखर",
        name_roman="Trishul Peak",
        title="7,120 m Trident of Mahadev Dominating the Kumaon Skyline",
        category="Alpine Peak & Glacier",
        district="Bageshwar",
        altitude_or_location="7,120 m (Visible across Almora, Kausani, and Ranikhet)",
        spiritual_or_historical_significance="Symbolizes the celestial trident of Lord Shiva standing guard beside Goddess Nanda Devi.",
        description="A breathtaking three-pronged snow massif whose pink and golden sunset glow inspires centuries of Kumaoni folk poetry.",
        associated_deities_or_fairs=["Lord Shiva", "Trishul Jaat", "Kausani Sunrise/Sunset Vistas"]
    ),
    "panchachuli_peaks": KumaoniPlace(
        id="panchachuli_peaks",
        name_kumaoni="पंचाचूली शिखर",
        name_roman="Panchachuli Peaks",
        title="6,904 m Five Cooking Hearths of the Pandavas in Johar Valley",
        category="Alpine Peak & Glacier",
        district="Pithoragarh",
        altitude_or_location="6,904 m (Overlooking Munsyari and Darma valley)",
        spiritual_or_historical_significance="Folk legend states the five Pandava brothers cooked their final earthly meal here on five hearths ('Chuli') before ascending to heaven.",
        description="Five distinct spires of virgin ice and rock standing in magnificent array against the morning sky, immortalized in Kumaoni lore.",
        associated_deities_or_fairs=["Pandavas", "Draupadi", "Munsyari Sightseeing"]
    ),
    "om_parvat": KumaoniPlace(
        id="om_parvat",
        name_kumaoni="ॐ पर्वत",
        name_roman="Om Parvat",
        title="6,191 m Sacred Peak Miraculously Etched with the Snow 'ॐ' Glyph",
        category="Alpine Peak & Glacier",
        district="Pithoragarh",
        altitude_or_location="6,191 m (Vyas Valley on Indo-Tibetan border)",
        spiritual_or_historical_significance="A natural miracle of nature where seasonal snow deposits clearly form the sacred Vedic symbol 'ॐ' against dark mountain shale.",
        description="Revered on the Kailash-Mansarovar pilgrim trail, viewed from Nabhi Dhang in the high Byas valley.",
        associated_deities_or_fairs=["Lord Shiva", "Kailash-Mansarovar Pilgrimage", "Vyas Valley"]
    ),
    "adi_kailash": KumaoniPlace(
        id="adi_kailash",
        name_kumaoni="आदि कैलाश (छोटा कैलाश)",
        name_roman="Adi Kailash (Chhota Kailash)",
        title="5,945 m Ancient Abode of Shiva Beside Parvati Sarovar",
        category="Alpine Peak & Glacier",
        district="Pithoragarh",
        altitude_or_location="5,945 m (Jolingkong in Byas Valley)",
        spiritual_or_historical_significance="Ancient alternative to Mount Kailash in Tibet; site of Parvati Sarovar and an ancient Shiva-Parvati temple.",
        description="A pyramid of rock and ice whose reflection shimmers in the crystal waters of Parvati Lake in the high trans-Himalayan plateau.",
        associated_deities_or_fairs=["Lord Shiva", "Maa Parvati", "Adi Kailash Yatra", "Parvati Sarovar"]
    ),
    "pindari_glacier": KumaoniPlace(
        id="pindari_glacier",
        name_kumaoni="पिण्डारी हिमनद",
        name_roman="Pindari Glacier",
        title="Iconic 30-km Glacial Highway of Bageshwar District",
        category="Alpine Peak & Glacier",
        district="Bageshwar",
        altitude_or_location="3,800 m to 4,500 m (Between Nanda Devi and Nanda Kot)",
        spiritual_or_historical_significance="Birthplace of the Pindar river; legendary Zero Point offers views of the Traill's Pass and Changuch peak.",
        description="One of the most accessible and celebrated Himalayan glaciers, celebrated in travelogues and folklore across the world.",
        associated_deities_or_fairs=["Nanda Devi", "Pindar River", "Trekker Sanctuary"]
    ),
    "milam_glacier": KumaoniPlace(
        id="milam_glacier",
        name_kumaoni="मिलम हिमनद",
        name_roman="Milam Glacier",
        title="Grand 16-km Glacier of the Johar Valley & Gori Ganga Source",
        category="Alpine Peak & Glacier",
        district="Pithoragarh",
        altitude_or_location="3,600 m to 4,200 m (Upper Johar Valley, beneath Trishuli and Hardeol peaks)",
        spiritual_or_historical_significance="Heart of the legendary trans-Himalayan trading empire of Milam Shauka merchants.",
        description="A massive glacier fed by multiple tributaries beneath towering peaks. Flanked by the historic, now ghost village of Milam.",
        associated_deities_or_fairs=["Shauka Culture", "Trishuli Peak", "Milam Village"]
    ),

    # ==================== VALLEYS, HISTORIC TOWNS & PASSES ====================
    "almora_town": KumaoniPlace(
        id="almora_town",
        name_kumaoni="अल्मोड़ा",
        name_roman="Almora",
        title="Cultural, Literary & Artistic Capital of Kumaon",
        category="Valley, Pass & Town",
        district="Almora",
        altitude_or_location="1,638 m (Horse-saddle shaped mountain ridge between Kosi and Suyal rivers)",
        spiritual_or_historical_significance="Founded by Chand King Balo Kalyan Chand in 1568; home of Kumaoni cuisine (Bal Mithai, Singodi), copper craft, and celebrated poets.",
        description="Known for its traditional cobblestone Lala Bazaar, wooden carved doors, historic Nanda Devi temple, and intellectual heritage.",
        associated_deities_or_fairs=["Nanda Devi", "Chitai Golu", "Lala Bazaar", "Nanda Devi Mela"]
    ),
    "nainital_town": KumaoniPlace(
        id="nainital_town",
        name_kumaoni="नैनीताल",
        name_roman="Nainital",
        title="Lake District of Kumaon Surrounded by Seven Hills (Sapta Shring)",
        category="Valley, Pass & Town",
        district="Nainital",
        altitude_or_location="2,084 m (Eye-shaped volcanic depression lake)",
        spiritual_or_historical_significance="Center of the Manaskhanda Tri-Rishi Sarovar legend (Atri, Pulastya, Pulaha); British summer capital of United Provinces.",
        description="Surrounded by emerald peaks including Naina Peak (2,615m). Center for education, sailing, cultural tourism, and mountain walks.",
        associated_deities_or_fairs=["Maa Naina Devi", "Pashan Devi", "Naini Lake", "Nanda Devi Festival"]
    ),
    "champawat_town": KumaoniPlace(
        id="champawat_town",
        name_kumaoni="चम्पावत",
        name_roman="Champawat",
        title="Historic Cradle & First Capital of the Chand Dynasty",
        category="Valley, Pass & Town",
        district="Champawat",
        altitude_or_location="1,610 m (Kali Kumaon basin)",
        spiritual_or_historical_significance="Founded by King Som Chand in the 10th century CE; birthplace of the Golu Devta epic and Baleshwar temple complex.",
        description="Home to the exquisite 13th-century carved stone Baleshwar temple and ancient hill fort of Rajbunga.",
        associated_deities_or_fairs=["Baleshwar Mahadev", "Golu Devta", "Kranteshwar Mahadev"]
    ),
    "munsyari_town": KumaoniPlace(
        id="munsyari_town",
        name_kumaoni="मुनस्यारी (मुनस्यारि)",
        name_roman="Munsyari",
        title="Place with Snow & Gateway to Johar Valley Beneath Panchachuli",
        category="Valley, Pass & Town",
        district="Pithoragarh",
        altitude_or_location="2,200 m (High terrace above Gori river)",
        spiritual_or_historical_significance="Traditional base of trans-Himalayan Shauka traders; renowned for handwoven sheep wool carpets (Dan) and Pashmina.",
        description="Offers close-up, jaw-dropping panoramic views of the Panchachuli range, alpine bugyals of Khalia Top, and the Tribal Heritage Museum.",
        associated_deities_or_fairs=["Nanda Devi", "Meser Kund", "Tribal Heritage Museum"]
    ),
    "dharchula_town": KumaoniPlace(
        id="dharchula_town",
        name_kumaoni="धारचूला",
        name_roman="Dharchula",
        title="Stove-Shaped Mountain Town & Gateway to Kailash-Mansarovar",
        category="Valley, Pass & Town",
        district="Pithoragarh",
        altitude_or_location="940 m (Deep river gorge of Kali river on Nepal border)",
        spiritual_or_historical_significance="Hub of the Rung and Shauka communities; gateway to Darma, Byans, and Chaudas valleys.",
        description="Divided from Darchula (Nepal) only by a swaying pedestrian suspension bridge across the rushing Kali river.",
        associated_deities_or_fairs=["Gabla Devta", "Chipla Kedar", "Kailash-Mansarovar Route"]
    ),
    "dwarahat_town": KumaoniPlace(
        id="dwarahat_town",
        name_kumaoni="द्वाराहाट",
        name_roman="Dwarahat",
        title="Valley of 55 Temples & Heritage Seat of Katyuri Architecture",
        category="Valley, Pass & Town",
        district="Almora",
        altitude_or_location="1,510 m (Pali-Pachhaun valley)",
        spiritual_or_historical_significance="Literally 'Way to Heaven'; renowned for ancient stone temple groups (Gujar Dev, Badrinath, Maniyan, Kacheri).",
        description="An open valley museum of stone carvings dating from the 11th to 14th century, accompanied by the historic Syalde-Bikhoti fair.",
        associated_deities_or_fairs=["Gujar Dev", "Dunagiri Devi", "Syalde-Bikhoti Mela"]
    ),
    "ranikhet_town": KumaoniPlace(
        id="ranikhet_town",
        name_kumaoni="रानीखेत",
        name_roman="Ranikhet",
        title="Queen's Meadow & Regimental Center of the Kumaon Regiment",
        category="Valley, Pass & Town",
        district="Almora",
        altitude_or_location="1,869 m (Pine and deodar ridges with golf course)",
        spiritual_or_historical_significance="According to legend, Queen Padmini of the Katyuri royal family was captivated by this lush green highland meadow.",
        description="Famed for British-era cantonment colonial architecture, rolling 9-hole golf course, Chaubattia apple orchards, and military heritage.",
        associated_deities_or_fairs=["Jhula Devi", "Binsar Mahadev", "Kumaon Regimental Museum"]
    ),
    "johar_valley": KumaoniPlace(
        id="johar_valley",
        name_kumaoni="जोहार घाटी",
        name_roman="Johar Valley",
        title="Ancient Trans-Himalayan Silk-&-Salt Trade Corridor",
        category="Valley, Pass & Town",
        district="Pithoragarh",
        altitude_or_location="2,200 m to 4,500 m along the Gori Ganga",
        spiritual_or_historical_significance="Home of legendary Himalayan explorers (Pandit Nain Singh Rawat, Rai Bahadur Kishen Singh Rawat) who mapped Tibet.",
        description="A canyon of wild beauty climbing to high glaciated villages of Rilkot, Martoli, Burfu, and Milam beneath towering snow walls.",
        associated_deities_or_fairs=["Nanda Devi", "Shauka Trade Heritage", "Milam Glacier"]
    )
}


class PlacesTreasury:
    """Master registry and lookup interface for Kumaon's sacred geography, temples, and places."""

    @classmethod
    def list(cls, category: Optional[str] = None, district: Optional[str] = None) -> List[KumaoniPlace]:
        results = list(PLACES_DATA.values())
        if category:
            cat_lower = category.lower()
            results = [p for p in results if cat_lower in p.category.lower()]
        if district:
            dist_lower = district.lower()
            results = [p for p in results if dist_lower in p.district.lower()]
        return results

    @classmethod
    def get(cls, place_id: str) -> Optional[KumaoniPlace]:
        key = place_id.strip().lower().replace(" ", "_")
        if key in PLACES_DATA:
            return PLACES_DATA[key]
        for p in PLACES_DATA.values():
            if p.id == key or p.name_roman.lower() == place_id.lower() or p.name_kumaoni == place_id:
                return p
        return None

    @classmethod
    def search(cls, query: str) -> List[KumaoniPlace]:
        if not query:
            return cls.list()
        q = query.strip().lower()
        results = []
        for p in PLACES_DATA.values():
            if (q in p.name_kumaoni.lower() or
                q in p.name_roman.lower() or
                q in p.title.lower() or
                q in p.district.lower() or
                q in p.description.lower() or
                q in p.spiritual_or_historical_significance.lower() or
                any(q in deity.lower() for deity in p.associated_deities_or_fairs)):
                results.append(p)
        return results

    @classmethod
    def stats(cls) -> Dict[str, Any]:
        categories: Dict[str, int] = {}
        districts: Dict[str, int] = {}
        for p in PLACES_DATA.values():
            categories[p.category] = categories.get(p.category, 0) + 1
            districts[p.district] = districts.get(p.district, 0) + 1
        return {
            "total_places": len(PLACES_DATA),
            "categories": categories,
            "districts": districts
        }
