"""
Kumaoni surnames, clans, historical lineages, gotras, and social structure of Uttarakhand.
Includes comprehensive cataloguing of Brahmin, Kshatriya/Rajput, Shauka, and Shilpkar heritage clans.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict


@dataclass
class KumaoniSurname:
    id: str
    surname_kumaoni: str
    surname_roman: str
    title: str
    community: str  # "Brahmin", "Kshatriya / Rajput", "Shauka / Alpine Bhotia", "Shilpkar / Artisan"
    traditional_title_or_role: str
    gotras: List[str]
    ancestral_villages_or_origin: str
    notable_historical_figures: List[str]
    cultural_and_historical_notes: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


SURNAMES_DATA: Dict[str, KumaoniSurname] = {
    # ==================== KUMAONI BRAHMIN CLANS ====================
    "pant": KumaoniSurname(
        id="pant",
        surname_kumaoni="पंत",
        surname_roman="Pant",
        title="Royal Physicians, Astrologers, Advisors & Literati to Chand Kings",
        community="Brahmin",
        traditional_title_or_role="Royal rajvaidyas, counselors, chief priests, and poets.",
        gotras=["शांडिल्य (Shandilya)", "भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Migrated in 10th-11th century from Konkan/Maharashtra (ancestor Jaideo Pant); established in Uprara, Gangolihat, Almora, Bageshwar, Khantoli.",
        notable_historical_figures=["Gumani Pant (1790-1846, Father of Kumaoni Poetry)", "Pandit Govind Ballabh Pant (Bharat Ratna, Premier of UP & Union Home Minister)", "Sumitranandan Pant (Jnanpith laureate Hindi poet)"],
        cultural_and_historical_notes="Divided into Sharmas (Shandilya gotra) with prestigious branches across Almora and Gangolihat. Renowned across generations for Sanskrit scholarship and civic leadership."
    ),
    "joshi": KumaoniSurname(
        id="joshi",
        surname_kumaoni="जोशी",
        surname_roman="Joshi",
        title="Royal Diwans, Astrologers & Prime Ministers of Kumaon Kingdom",
        community="Brahmin",
        traditional_title_or_role="Diwans (Prime Ministers), Jyotish scholars, royal chroniclers, and administrators.",
        gotras=["गर्ग (Garga)", "कौशिक (Kaushika)", "भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Migrated from Kannauj and Southern India to Champawat; spread through Galli, Jhijhar, Danpur, Almora (Lala Bazaar, Galli).",
        notable_historical_figures=["Harsh Dev Joshi (18th C. Kingmaker & Statesman)", "Manohar Shyam Joshi (Pioneer novelist & Doordarshan scriptwriter)", "Murli Manohar Joshi (Eminent scholar & Union Minister)"],
        cultural_and_historical_notes="Historically held the hereditary office of Diwan under the Chand Kings. Played central political roles in the historic court politics of Almora."
    ),
    "pandey": KumaoniSurname(
        id="pandey",
        surname_kumaoni="पांडे / पाण्डे",
        surname_roman="Pandey / Pande",
        title="Preceptors, Vedic Scholars & Historians of the Himalayan Frontier",
        community="Brahmin",
        traditional_title_or_role="Vedic educators, priests, royal preceptors (Rajguru), and temple custodians.",
        gotras=["भारद्वाज (Bharadwaj)", "उपमन्यु (Upamanyu)", "कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Established at Patia (Patiyals), Dhamas (Dhamis), Gangolihat, Champawat, Dwarahat.",
        notable_historical_figures=["Badri Datt Pande (1882-1965, Kumaon Kesari, Author of 'Kumaun ka Itihas')", "Dr. Trilochan Pandey (Doyen of Kumaoni linguistics)", "Bhairab Dutt Pande (Cabinet Secretary of India)"],
        cultural_and_historical_notes="Renowned for fearless journalism and freedom movement leadership; Badri Datt Pande led the historic 1921 Coolie-Begar abolition movement at Bageshwar."
    ),
    "upreti": KumaoniSurname(
        id="upreti",
        surname_kumaoni="उप्रेती",
        surname_roman="Upreti",
        title="Scholars of the Upper Terrace (Uprara) & Royal Priests",
        community="Brahmin",
        traditional_title_or_role="Royal preceptors, Sanskrit scholars, magistrates, and lexicographers.",
        gotras=["भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Named after the ancestral seat of Uprara in Gangolihat and Almora; branches across Pithoragarh, Dwarahat, and Nainital.",
        notable_historical_figures=["Pandit Ganga Datt Upreti (1894, Author of 'Proverbs & Folklore of Kumaun')", "Mohan Upreti (Legendary theater director & musicologist, creator of 'Bedu Pako')", "Harish Upreti (Eminent academician)"],
        cultural_and_historical_notes="Ganga Datt Upreti served as Extra Assistant Commissioner and authored the first major English-Kumaoni folklore compendium in 1894."
    ),
    "tiwari": KumaoniSurname(
        id="tiwari",
        surname_kumaoni="तिवारी / त्रिपाठी",
        surname_roman="Tiwari / Tripathi",
        title="Masters of the Three Vedas & Royal Preceptors",
        community="Brahmin",
        traditional_title_or_role="Reciters of the three Vedas (Trivedi), religious teachers, and court ministers.",
        gotras=["कश्यप (Kashyapa)", "भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Migrated from Kanyakubja region to Champawat and Almora; established in Tuniya, Dwarahat, and Bageshwar.",
        notable_historical_figures=["Narayan Datt Tiwari (Chief Minister of Uttar Pradesh & Uttarakhand, Union Minister)"],
        cultural_and_historical_notes="Represented the esteemed Chauthani and Pachbiri Brahmin councils that governed religious traditions under the Chand dynasty."
    ),
    "pathak": KumaoniSurname(
        id="pathak",
        surname_kumaoni="पाठक",
        surname_roman="Pathak",
        title="Readers of the Sacred Texts & Vedic Exponents",
        community="Brahmin",
        traditional_title_or_role="Readers (Pathaks) of sacred scriptures, genealogists, and astrologers.",
        gotras=["भारद्वाज (Bharadwaj)", "कौशिक (Kaushika)"],
        ancestral_villages_or_origin="Established across Pali-Pachhaun, Almora, Dwarahat, and Gangolihat.",
        notable_historical_figures=["Prof. Shekhar Pathak (Padma Shri historian, author, founder of PAHAR)"],
        cultural_and_historical_notes="Prominent in literary documentation and environmental social movements (Askot-Arakot Abhiyan)."
    ),
    "bhatt": KumaoniSurname(
        id="bhatt",
        surname_kumaoni="भट्ट",
        surname_roman="Bhatt",
        title="Vedic Philosophers & Hereditary Temple Priests",
        community="Brahmin",
        traditional_title_or_role="Hereditary temple priests (archakas) at major Shiva and Shakti shrines (Jageshwar, Baijnath).",
        gotras=["वशिष्ठ (Vashishta)", "भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Southern and Western India ancestry (often tracing to Dravida Brahmins invited by Adi Shankaracharya and Katyuri kings); Jageshwar, Baijnath.",
        notable_historical_figures=["Pandit Krishna Bhatt (Chand-era court philosopher)"],
        cultural_and_historical_notes="Continue to serve as the chief custodians and ritual conductors at the 124 temples of the Jageshwar Dham complex."
    ),
    "upadhyay": KumaoniSurname(
        id="upadhyay",
        surname_kumaoni="उपाध्याय",
        surname_roman="Upadhyay",
        title="Traditional Preceptors of Vedic Shastras",
        community="Brahmin",
        traditional_title_or_role="Teachers of grammar, Vedic recitations, and philosophical treatises.",
        gotras=["कश्यप (Kashyapa)", "भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Found across Almora, Pithoragarh, Dwarahat, and Champawat.",
        notable_historical_figures=["Acharya Baldev Upadhyay (Renowned Sanskrit scholar)"],
        cultural_and_historical_notes="Maintained traditional gurukuls across Kumaon hills preserving oral recitation of the Samaveda and Yajurveda."
    ),
    "sanwal": KumaoniSurname(
        id="sanwal",
        surname_kumaoni="सांवल",
        surname_roman="Sanwal",
        title="Ancient Scholarly & Administrative Brahmin Lineage",
        community="Brahmin",
        traditional_title_or_role="Civil officers, educators, and scholars.",
        gotras=["शांडिल्य (Shandilya)"],
        ancestral_villages_or_origin="Almora, Nainital, and Someshwar valleys.",
        notable_historical_figures=["B. D. Sanwal (ICS officer and Himalayan art scholar)"],
        cultural_and_historical_notes="Eminent family line known for British-era civil service, judiciary, and documentation of Kumaoni miniature art."
    ),
    "kholiya": KumaoniSurname(
        id="kholiya",
        surname_kumaoni="खोलिया",
        surname_roman="Kholiya",
        title="Scholars of the Kholi Valleys & Temple Priests",
        community="Brahmin",
        traditional_title_or_role="Priests, educators, and rural community leaders.",
        gotras=["भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Kholi village in Gangolihat and Pithoragarh district.",
        notable_historical_figures=["Local folk pandits and Sanskrit teachers"],
        cultural_and_historical_notes="Associated with traditional rituals and folk Jagar ceremonies across eastern Kumaon."
    ),

    # ==================== KUMAONI KSHATRIYA / RAJPUT CLANS ====================
    "bisht": KumaoniSurname(
        id="bisht",
        surname_kumaoni="बिष्ट",
        surname_roman="Bisht",
        title="Feudal Lords, Military Commanders & Landed Nobility",
        community="Kshatriya / Rajput",
        traditional_title_or_role="Feudal lords (Thokdars), army generals, governors, and landed nobility.",
        gotras=["भारद्वाज (Bharadwaj)", "कश्यप (Kashyapa)", "वत्स (Vatsa)"],
        ancestral_villages_or_origin="Derived from Sanskrit 'Vishisht' (eminent/noble); prominent branches across Almora, Pithoragarh (Sor), Nainital, and Bageshwar.",
        notable_historical_figures=["Pratap Singh Bisht (Author of 'Veer Abhimanyu')", "Major Somnath Sharma Bisht family ties", "Ajay Singh Bisht (Yogi Adityanath, Chief Minister of Uttar Pradesh)"],
        cultural_and_historical_notes="One of the most widespread and influential Rajput communities of Uttarakhand. Held hereditary rights as village chieftains and military commanders."
    ),
    "rawat": KumaoniSurname(
        id="rawat",
        surname_kumaoni="रावत",
        surname_roman="Rawat",
        title="Feudal Chiefs, Fortress Commanders & Royal Warriors",
        community="Kshatriya / Rajput",
        traditional_title_or_role="Feudal rulers, fortress commanders (Kotwals), and martial clans.",
        gotras=["भारद्वाज (Bharadwaj)", "कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Derived from Sanskrit 'Raja-putra' / 'Raut'; distributed across Almora, Pithoragarh, Bageshwar, and Champawat.",
        notable_historical_figures=["General Bipin Rawat (First Chief of Defence Staff of India)", "Pandit Nain Singh Rawat (CIE, Great Trans-Himalayan Explorer)", "Harish Rawat (Former Chief Minister of Uttarakhand & Union Minister)"],
        cultural_and_historical_notes="Both Khas-Rajput and Shauka-Johari lineages bear this esteemed name. Legendary for trans-Himalayan exploration and high-altitude courage."
    ),
    "negi": KumaoniSurname(
        id="negi",
        surname_kumaoni="नेगी",
        surname_roman="Negi",
        title="Military Officers & Custodians of Royal Perquisites (Neg)",
        community="Kshatriya / Rajput",
        traditional_title_or_role="Military officers, tax revenue collectors, and provincial administrators who received 'Neg' (royal perquisite).",
        gotras=["भारद्वाज (Bharadwaj)", "कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Spread across Kumaon and Garhwal; Almora, Bageshwar, Nainital.",
        notable_historical_figures=["Rifleman Gabar Singh Negi (Victoria Cross recipient)", "Dhan Singh Negi (Freedom fighter)"],
        cultural_and_historical_notes="Known for legendary martial valor in the Kumaon Regiment and Garhwal Rifles during World Wars I and II."
    ),
    "mehra": KumaoniSurname(
        id="mehra",
        surname_kumaoni="मेहरा / महरा",
        surname_roman="Mehra / Mahara",
        title="Influential Chieftains & Leaders of the 'Mahara Dhada' Faction",
        community="Kshatriya / Rajput",
        traditional_title_or_role="Chieftains, advisors to Chand kings, and factional leaders.",
        gotras=["कश्यप (Kashyapa)", "भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Epicenter in Kali Kumaon (Champawat, Lohaghat); villages of Chaukhutia, Katarmal.",
        notable_historical_figures=["Kalu Singh Mahara (Leader of Kumaon's 1857 First War of Independence uprising)"],
        cultural_and_historical_notes="Formed the historic 'Mahara Dhada' faction that balanced power against the 'Fartyal Dhada' in Chand dynastic politics."
    ),
    "fartyal": KumaoniSurname(
        id="fartyal",
        surname_kumaoni="फर्त्याल",
        surname_roman="Fartyal",
        title="Martial Leaders of the Historic 'Fartyal Dhada' Court Faction",
        community="Kshatriya / Rajput",
        traditional_title_or_role="Military chieftains, royal councilors, and fortress defenders.",
        gotras=["कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Kali Kumaon, Champawat, Lohaghat, and Pithoragarh.",
        notable_historical_figures=["Historic Fartyal commanders who guided the ascension of Chand kings"],
        cultural_and_historical_notes="Fierce defenders of regional sovereignty; their factional rivalry with the Maharas shaped centuries of medieval Kumaoni history."
    ),
    "bhandari": KumaoniSurname(
        id="bhandari",
        surname_kumaoni="भंडारी",
        surname_roman="Bhandari",
        title="Custodians of Royal Treasuries & Legendary War Heroes",
        community="Kshatriya / Rajput",
        traditional_title_or_role="Keepers of the royal granaries, armories, and state treasuries (Bhandar); military commanders.",
        gotras=["कश्यप (Kashyapa)", "भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Almora, Champawat, and Katyur valley.",
        notable_historical_figures=["Kalu Bhandari (Legendary Katyuri military general celebrated in folk ballads)"],
        cultural_and_historical_notes="Kalu Bhandari is immortalized in Kumaoni Pawada folk epics as an invincible warrior who defended the Himalayan passes."
    ),
    "karki": KumaoniSurname(
        id="karki",
        surname_kumaoni="कार्की",
        surname_roman="Karki",
        title="Warrior Commanders of Kali Kumaon & Border Passes",
        community="Kshatriya / Rajput",
        traditional_title_or_role="Fortress guards, tax assessors, and fierce warriors.",
        gotras=["भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Champawat, Lohaghat, and border valleys of Kali river.",
        notable_historical_figures=["Traditional Kotwals of Chand fortifications"],
        cultural_and_historical_notes="A revered martial clan sharing history across both Kumaon and Western Nepal along the Mahakali border."
    ),
    "rautela": KumaoniSurname(
        id="rautela",
        surname_kumaoni="रौतेला",
        surname_roman="Rautela",
        title="Direct Royal Princes & Cadet Lineages of the Chand Dynasty",
        community="Kshatriya / Rajput",
        traditional_title_or_role="Princes, royal governors, and jagirdars.",
        gotras=["कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Champawat, Almora, Kota, and Dhyanirau.",
        notable_historical_figures=["Princes of the Chand royal household"],
        cultural_and_historical_notes="Descendants of younger brothers and sons of the Chand kings; held landed estates across Almora and Champawat."
    ),
    "chand": KumaoniSurname(
        id="chand",
        surname_kumaoni="चंद",
        surname_roman="Chand",
        title="Royal Sovereign Dynasty of Kumaon (10th to 18th Century)",
        community="Kshatriya / Rajput",
        traditional_title_or_role="Kings (Rajas), sovereigns of Kumaon, builders of Baleshwar, Nanda Devi, and Bagnath temples.",
        gotras=["कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Champawat (first capital, Rajbunga fort); shifted to Almora in 1568 CE.",
        notable_historical_figures=["Raja Som Chand (Founder)", "Raja Kalyan Chand", "Raja Baz Bahadur Chand", "Raja Rudra Chand"],
        cultural_and_historical_notes="Ruled Kumaon for nearly a millennium, establishing the standardized Kumaoni administrative, religious, and cultural systems."
    ),
    "manral": KumaoniSurname(
        id="manral",
        surname_kumaoni="मनराल",
        surname_roman="Manral",
        title="Princes of the Katyuri Dynasty (Kartikeyapura Lineage)",
        community="Kshatriya / Rajput",
        traditional_title_or_role="Royal rulers of Pali-Pachhaun, Dwarahat, and Katyur valley.",
        gotras=["शौनक (Shaunaka)", "कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Dwarahat, Baijnath, Askot, and Chaukhutia.",
        notable_historical_figures=["Katyuri descendant rulers who preserved ancient temple complexes at Dwarahat"],
        cultural_and_historical_notes="Traced directly from the classical Katyuri kings who ruled Uttarakhand prior to the Chands."
    ),
    "bora": KumaoniSurname(
        id="bora",
        surname_kumaoni="बोरा",
        surname_roman="Bora",
        title="Prominent Agricultural Nobility & Village Chieftains",
        community="Kshatriya / Rajput",
        traditional_title_or_role="Landowners, village heads, and cavalrymen.",
        gotras=["कश्यप (Kashyapa)", "भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Almora, Pithoragarh, and Champawat.",
        notable_historical_figures=["Prominent community leaders across Kumaon"],
        cultural_and_historical_notes="Known for extensive agriculture in fertile river valleys and active participation in local self-governance."
    ),
    "adhikari": KumaoniSurname(
        id="adhikari",
        surname_kumaoni="अधिकारी",
        surname_roman="Adhikari",
        title="Royal Officers with Executive & Revenue Authority",
        community="Kshatriya / Rajput",
        traditional_title_or_role="Executive officers, revenue collectors, and judicial arbiters under hill rajas.",
        gotras=["भारद्वाज (Bharadwaj)", "कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Found across Almora, Pithoragarh, and Bageshwar.",
        notable_historical_figures=["Court officials and modern military officers"],
        cultural_and_historical_notes="Derived from Sanskrit 'Adhikara' (one possessing authority/office)."
    ),
    "mehta": KumaoniSurname(
        id="mehta",
        surname_kumaoni="मेहता",
        surname_roman="Mehta",
        title="Village Nobles, Land Accountants & Village Heads",
        community="Kshatriya / Rajput",
        traditional_title_or_role="Estate managers, accountants, and chieftains.",
        gotras=["कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Almora, Bageshwar, and Nainital districts.",
        notable_historical_figures=["Traditional village Sayanas and freedom fighters"],
        cultural_and_historical_notes="Prominent in agrarian leadership and pastoral village assemblies."
    ),
    "danu": KumaoniSurname(
        id="danu",
        surname_kumaoni="दानू",
        surname_roman="Danu",
        title="Martial Chieftains of Danpur & Pindar Valley",
        community="Kshatriya / Rajput",
        traditional_title_or_role="Defenders of the upper Pindar gorges, hunters, and village heads.",
        gotras=["कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Danpur region in upper Bageshwar district (Kapkot, Pindari).",
        notable_historical_figures=["High-altitude guides and Danpur folk leaders"],
        cultural_and_historical_notes="Known for endurance and courage across the rugged glaciated terrain of the Pindari valley."
    ),
    "koranga": KumaoniSurname(
        id="koranga",
        surname_kumaoni="कोरंगा",
        surname_roman="Koranga",
        title="Highland Warrior Clan of Bageshwar & Danpur",
        community="Kshatriya / Rajput",
        traditional_title_or_role="Mountain warriors, pastoral landowners, and community heads.",
        gotras=["कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Danpur, Kapkot, and Bageshwar.",
        notable_historical_figures=["Martial leaders in the Indian Army"],
        cultural_and_historical_notes="Distinguished service in the armed forces with traditions of valor in the Himalayas."
    ),

    # ==================== SHAUKA / ALPINE BHOTIA CLANS ====================
    "pangtey": KumaoniSurname(
        id="pangtey",
        surname_kumaoni="पांगती",
        surname_roman="Pangtey",
        title="Scholars, Alpine Merchants & Legendary Explorers of Johar",
        community="Shauka / Alpine Bhotia",
        traditional_title_or_role="Trans-Himalayan trade masters, cartographers, educators, and community leaders.",
        gotras=["शौनक (Shaunaka) / Shauka lineages"],
        ancestral_villages_or_origin="Pangu / Johar valley (Milam, Burfu, Munsyari).",
        notable_historical_figures=["Dr. S. S. Pangtey (Historian and founder of Tribal Heritage Museum Munsyari)"],
        cultural_and_historical_notes="Pioneered the preservation of Johar Shauka traditions, alpine folklore, and trans-Himalayan wool craft."
    ),
    "martolia": KumaoniSurname(
        id="martolia",
        surname_kumaoni="मर्तोलिया",
        surname_roman="Martolia",
        title="Lords of Martoli Village Beneath Nanda Devi",
        community="Shauka / Alpine Bhotia",
        traditional_title_or_role="Alpine traders, high-altitude caravan leaders, and administrators.",
        gotras=["Johari lineage"],
        ancestral_villages_or_origin="Martoli village in high Johar valley (3,380 m), Munsyari.",
        notable_historical_figures=["Prominent trans-Himalayan merchants with trade marts in Gyanema and Gartok (Tibet)"],
        cultural_and_historical_notes="Martoli is home to the historic temple of Nanda Devi where trans-Himalayan caravans prayed before crossing the untamed passes."
    ),
    "johari_rawat": KumaoniSurname(
        id="johari_rawat",
        surname_kumaoni="रावत (जोहारी)",
        surname_roman="Rawat (Johari)",
        title="Pundits of the Survey of India & Master Explorers of Tibet",
        community="Shauka / Alpine Bhotia",
        traditional_title_or_role="Explorers, trade leaders, and geographers.",
        gotras=["Johari Rajput gotra"],
        ancestral_villages_or_origin="Milam and Munsyari in Johar valley.",
        notable_historical_figures=["Pandit Nain Singh Rawat (CIE, Royal Geographical Society Gold Medalist)", "Kishan Singh Rawat (Explorer A.K.)"],
        cultural_and_historical_notes="Nain Singh mapped Tibet and Lhasa on foot using a prayer wheel and beads with superhuman precision when foreigners were forbidden on pain of death."
    ),
    "jangpangi": KumaoniSurname(
        id="jangpangi",
        surname_kumaoni="जंगपांगी",
        surname_roman="Jangpangi",
        title="Alpine Trade Agents & High-Altitude Administrators",
        community="Shauka / Alpine Bhotia",
        traditional_title_or_role="British trade agents in Western Tibet (Gartok), high-altitude administrators.",
        gotras=["Johari lineage"],
        ancestral_villages_or_origin="Burfu and Milam in Johar valley, Munsyari.",
        notable_historical_figures=["Laxman Singh Jangpangi (British Trade Agent in Western Tibet)"],
        cultural_and_historical_notes="Protected Indian traders during the trans-Himalayan trade seasons and represented Indian sovereignty in trans-border outposts."
    ),
    "garbiyal": KumaoniSurname(
        id="garbiyal",
        surname_kumaoni="गर्ब्याल",
        surname_roman="Garbiyal",
        title="Chieftains of Garbyang Town (The Sinking City of Byans)",
        community="Shauka / Alpine Bhotia",
        traditional_title_or_role="Trade magnates on the Kailash-Mansarovar pilgrim route, leaders of Byans valley.",
        gotras=["Rung lineage"],
        ancestral_villages_or_origin="Garbyang village in Byans valley, Dharchula.",
        notable_historical_figures=["Prominent Rung leaders and civil servants"],
        cultural_and_historical_notes="Garbyang was the bustling Himalayan trade hub where Indian, Tibetan, and Nepalese traders bartered salt, borax, gold dust, and grain."
    ),

    # ==================== SHILPKAR & ARTISAN CLANS ====================
    "tamta": KumaoniSurname(
        id="tamta",
        surname_kumaoni="टम्टा",
        surname_roman="Tamta",
        title="Master Coppersmiths of Almora & World-Renowned Metal Sculptors",
        community="Shilpkar / Artisan",
        traditional_title_or_role="Master coppersmiths (Tamrakar), metal utensil artisans, and social reformers.",
        gotras=["विश्वकर्मा (Vishwakarma) gotra"],
        ancestral_villages_or_origin="Tamta Mohalla in Almora; Champawat, Bageshwar.",
        notable_historical_figures=["Munshi Hari Prasad Tamta (Pioneer social reformer who coined the term 'Shilpkar' in 1911)", "Pradeep Tamta (Eminent Member of Parliament)"],
        cultural_and_historical_notes="Crafted the world-famous hand-hammered copper vessels (Gaagar, Phungai) and brass temple bells for which Almora is renowned across Asia."
    ),
    "arya": KumaoniSurname(
        id="arya",
        surname_kumaoni="आर्य",
        surname_roman="Arya",
        title="Pioneers of Social Awakening & Freedom Struggle in Kumaon",
        community="Shilpkar / Artisan",
        traditional_title_or_role="Social reformers, educators, political leaders, and civil servants.",
        gotras=["Arya Samaj heritage lineages"],
        ancestral_villages_or_origin="Widespread across Almora, Nainital, Bageshwar, and Pithoragarh.",
        notable_historical_figures=["Leaders of the Arya Samaj and Kumaon Shilpkar Sudharini Sabha"],
        cultural_and_historical_notes="Adopted during the early 20th century awakening led by Munshi Hari Prasad Tamta to demand dignity, education, and equal rights."
    ),
    "lohar": KumaoniSurname(
        id="lohar",
        surname_kumaoni="लोहार",
        surname_roman="Lohar",
        title="Iron Artisans Who Forged Mountain Agricultural Implements",
        community="Shilpkar / Artisan",
        traditional_title_or_role="Ironsmiths forging hill sickles (Dathudo), plough tips, axes, and stone-carving chisels.",
        gotras=["विश्वकर्मा (Vishwakarma)"],
        ancestral_villages_or_origin="Every rural village settlement across Kumaon.",
        notable_historical_figures=["Rural tool-making masters"],
        cultural_and_historical_notes="Crucial to the survival of terrace farming in the hills; every spring they sharpened ploughs before auspicious sowing days."
    )
}


SOCIAL_CONCEPTS_DATA: Dict[str, Dict[str, str]] = {
    "that": {
        "term_kumaoni": "थात",
        "term_roman": "Thaat",
        "meaning": "Ancestral landed estate, patrimony, and territorial homestead inherited across generations."
    },
    "thatwan": {
        "term_kumaoni": "थातवान",
        "term_roman": "Thaatwaan",
        "meaning": "The hereditary original proprietor or founder of a village settlement holding direct ancestral rights in the land."
    },
    "dhada": {
        "term_kumaoni": "धड़ा",
        "term_roman": "Dhadha",
        "meaning": "The two historic factional political alliances in medieval Kumaon: the Mahara Dhada and Fartyal Dhada that shaped royal court decisions."
    },
    "gauntyar": {
        "term_kumaoni": "गौंत्यार",
        "term_roman": "Gauntyaar",
        "meaning": "Fellow villagers who share the same village boundaries, water naulas, and social mutual-aid ties."
    },
    "biradari": {
        "term_kumaoni": "बिरादरी",
        "term_roman": "Biraadari",
        "meaning": "Kinship brotherhood and clan members of the same sub-caste who observe mutual birth and death ritual observances."
    },
    "gotra": {
        "term_kumaoni": "गोत्र",
        "term_roman": "Gotra",
        "meaning": "Ancestral patrilineal clan tracing descent to one of the ancient Vedic Rishis (Bharadwaj, Kashyapa, Shandilya, Garga, etc.)."
    },
    "neg_jog": {
        "term_kumaoni": "नेग-जोग",
        "term_roman": "Neg-Jog",
        "meaning": "Customary ritual gifts of money, grain, or clothing given to relations, artisans, and family priests at weddings and festivals."
    },
    "jajmani": {
        "term_kumaoni": "जजमानी",
        "term_roman": "Jajmaani",
        "meaning": "Traditional socio-economic patron-client relationship between landholders and service castes (priests, coppersmiths, musicians)."
    }
}


class SurnamesTreasury:
    """Master registry and query interface for Kumaoni surnames, lineages, and social concepts."""

    @classmethod
    def list(cls, community: Optional[str] = None) -> List[KumaoniSurname]:
        results = list(SURNAMES_DATA.values())
        if community:
            com_lower = community.lower()
            results = [s for s in results if com_lower in s.community.lower()]
        return results

    @classmethod
    def get(cls, surname_id: str) -> Optional[KumaoniSurname]:
        key = surname_id.strip().lower().replace(" ", "_")
        if key in SURNAMES_DATA:
            return SURNAMES_DATA[key]
        for s in SURNAMES_DATA.values():
            if s.id == key or s.surname_roman.lower() == surname_id.lower() or s.surname_kumaoni == surname_id:
                return s
        return None

    @classmethod
    def search(cls, query: str) -> List[KumaoniSurname]:
        if not query:
            return cls.list()
        q = query.strip().lower()
        results = []
        for s in SURNAMES_DATA.values():
            if (q in s.surname_kumaoni.lower() or
                q in s.surname_roman.lower() or
                q in s.community.lower() or
                q in s.title.lower() or
                q in s.ancestral_villages_or_origin.lower() or
                any(q in g.lower() for g in s.gotras) or
                any(q in fig.lower() for fig in s.notable_historical_figures) or
                q in s.cultural_and_historical_notes.lower()):
                results.append(s)
        return results

    @classmethod
    def social_concepts(cls) -> Dict[str, Dict[str, str]]:
        return SOCIAL_CONCEPTS_DATA

    @classmethod
    def stats(cls) -> Dict[str, Any]:
        communities: Dict[str, int] = {}
        for s in SURNAMES_DATA.values():
            communities[s.community] = communities.get(s.community, 0) + 1
        return {
            "total_surnames": len(SURNAMES_DATA),
            "communities": communities,
            "total_social_concepts": len(SOCIAL_CONCEPTS_DATA)
        }
