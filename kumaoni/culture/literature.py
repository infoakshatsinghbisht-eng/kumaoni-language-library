"""
Literature, Folklore, and Oral Heritage of the Kumaoni Language.

Features:
- Folk Epics (पवाड़े / भड़): Malushahi-Rajula, Ajuva Bafaul, Golu Devta legends
- Lyrical Valley Songs (न्योली): Forest couplets of mountain romance and philosophy
- Festive Dance Songs (झोड़ा, छपेली, चाँचरी)
- Canonical Poets: Gumani Pant, Gaurda (Gauridutt Pande), Charu Chandra Pande
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field


@dataclass
class FolkEpic:
    id: str
    title_kumaoni: str
    title_english: str
    genre: str  # "Pauwada", "Jagar", "Ballad"
    region: str
    synopsis: str
    cultural_significance: str
    sample_verses: List[Dict[str, str]] = field(default_factory=list)


@dataclass
class FolkPoem:
    id: str
    title_kumaoni: str
    title_english: str
    form: str  # "Nyoli", "Jhora", "Chhapeli", "Chanchari", "Bair"
    theme: str
    verses_kumaoni: List[str]
    verses_roman: List[str]
    english_translation: str
    cultural_context: str


@dataclass
class KumaoniAuthor:
    name_kumaoni: str
    name_english: str
    era: str
    significance: str
    famous_works: List[str]
    sample_quote: Dict[str, str]


# --- Database of Kumaoni Literature ---

EPICS: Dict[str, FolkEpic] = {
    "malushahi": FolkEpic(
        id="malushahi",
        title_kumaoni="राजुला मालूशाही",
        title_english="Rajula and Malushahi",
        genre="Pauwada / Premgatha (Oral Epic Ballad)",
        region="Katyur Valley (Bageshwar) to Johar Valley (Pithoragarh / Tibet border)",
        synopsis=(
            "The timeless love epic between Prince Malushahi of the Katyur dynasty (Vairat/Bageshwar) "
            "and Princess Rajula, daughter of Sunpati Shauka, the wealthy Trans-Himalayan Bhotia trader. "
            "Overcoming formidable mountain passes, sorcery, and royal opposition, Rajula embarks on a solo "
            "perilous journey across the snowy Himalayas to be reunited with Malushahi."
        ),
        cultural_significance=(
            "Considered the Romeo and Juliet of the Central Himalayas, sung by traditional bards (Hurkiyas) "
            "accompanied by the hurka drum over multi-night winter sessions."
        ),
        sample_verses=[
            {
                "kumaoni": "हिमवंत डांडी-काँठी, बर्फक पाथर, राजुला हिंडी चली मालूक देश।",
                "roman": "Himavant daandi-kaanthi, barphak paathar, Rajula hindi chali Malook desh.",
                "english": "Across snowy ridges and slate cliffs, Rajula marched onward to the land of Malu."
            }
        ]
    ),
    "ajuva_bafaul": FolkEpic(
        id="ajuva_bafaul",
        title_kumaoni="अजुवा बफौल की भड़",
        title_english="Ballad of Ajuva Bafaul",
        genre="Bhad / Pauwada (Martial Heroic Epic)",
        region="Sor Valley (Pithoragarh / Champawat)",
        synopsis=(
            "Celebrates the extraordinary courage, honor, and loyalty of warrior brothers Ajuva and Kufwa Bafaul, "
            "who defended the people and regional chieftains with unparalleled bravery in medieval hill battles."
        ),
        cultural_significance="Symbol of Himalayan chivalry, justice, and martial valor celebrated in Kumaoni folklore."
    ),
    "golu_devta": FolkEpic(
        id="golu_devta",
        title_kumaoni="गोलू देवता जागर",
        title_english="Jagar of Lord Golu (God of Justice)",
        genre="Jagar / Sacred Folk Ballad",
        region="Chitai (Almora), Ghorakhal (Nainital), Champawat",
        synopsis=(
            "The sacred narrative of Prince Goril / Golu, incarnation of Lord Shiva, son of King Jhalu Rai and Queen Kalinka. "
            "After surviving treacherous stepmothers, he performs divine feats and is venerated across Kumaon as the ultimate "
            "arbiter of truth, righteousness, and prompt justice (Nyaya ke Devta)."
        ),
        cultural_significance=(
            "Devotees write legal petitions on stamped paper and hang brass bells at Chitai temple, "
            "testifying to Golu Devta's supreme role in folk jurisprudence."
        )
    ),
    "jiya_rani": FolkEpic(
        id="jiya_rani",
        title_kumaoni="जिया राँणि की गाथा",
        title_english="Gatha of Queen Jiya Rani (The Warrior Queen of Katyur)",
        genre="Veergatha / Pauwada (Martial Legend)",
        region="Ranibagh (Nainital) / Katyur Valley",
        synopsis=(
            "The heroic saga of Queen Jiya Rani (Moula Devi), the legendary Katyuri queen who mobilized mountain "
            "clans and led troops into battle against invading Rohilla forces at Chitrashila (Ranibagh). She is revered "
            "as the immortal guardian mother of Kumaon."
        ),
        cultural_significance=(
            "Celebrated during the annual Uttarayani / Chitrashila fair at Ranibagh where women sing her martial ballad."
        ),
        sample_verses=[
            {
                "kumaoni": "रानीबाग म रणभूमि म जिया राँणि गरज उठी, कच्यूरी फौज का साथ देश बचाई लियो।",
                "roman": "Raanibaag ma ranabhoomi ma Jiya Raani garaj uthi, Katyuri fauj ka saath desh bachaai liyo.",
                "english": "In the battlefield of Ranibagh Queen Jiya Rani roared like a lioness, saving her homeland alongside Katyuri warriors."
            }
        ]
    ),
    "haru_singh_heet": FolkEpic(
        id="haru_singh_heet",
        title_kumaoni="वीर बालक हरु सिंह हीत",
        title_english="Ballad of Young Hero Haru Singh Heet",
        genre="Khandkavya / Lokgatha (Heroic Ballad)",
        region="Kumaon Hills / Kali Kumaon",
        synopsis=(
            "The stirring heroic chronicle of adolescent warrior Haru Singh Heet, who displayed extraordinary chivalry "
            "and sacrificed his young life in defense of the realm against injustice and enemy assault."
        ),
        cultural_significance="Immortalized in Kumaoni folk theater and ballads by Kheemanand as a paragon of youthful valor."
    ),
    "amar_gopichand": FolkEpic(
        id="amar_gopichand",
        title_kumaoni="अमर गोपीचन्द योगी",
        title_english="Legend of Amar Gopichand Yogi",
        genre="Nath Panthi Lokgatha (Ascetic Spiritual Ballad)",
        region="Almora / Katyur / Garur",
        synopsis=(
            "The sacred ascetic tale of King Gopichand who renounced royal pleasures on the counsel of his mother Mainavati "
            "and Guru Gorakhnath to attain spiritual enlightenment and immortality in the Himalayas."
        ),
        cultural_significance="Sung by traditional Nath Jogi bards playing the Sarangi across Kumaon villages during winter nights."
    )
}

POEMS: List[FolkPoem] = [
    FolkPoem(
        id="bedu_pako",
        title_kumaoni="बेड़ू पाको बारह मासा",
        title_english="Bedu Pako Baro Masa (The Anthem of the Hills)",
        form="Jhora / Folk Song",
        theme="Nature, Himalayan Seasons, and Romance",
        verses_kumaoni=[
            "बेड़ू पाको बारह मासा, ओ नरण काफल पाको चैत, मेरी छैला!",
            "रूंणी-भूंणी सौंण भादौ, ओ नरण बरखा लागूँ छै, मेरी छैला!",
            "आल्मोड़ा की बाल मिठाई, ओ नरण खानी भौत मीठ, मेरी छैला!"
        ],
        verses_roman=[
            "Bedu pako baarah maasa, O Naran kaaphal paako Chait, meri chhaila!",
            "Rooni-bhooni Saun Bhaadau, O Naran barkha laagoon chhai, meri chhaila!",
            "Aalmoda ki Baal Mithai, O Naran khaani bhaut meeth, meri chhaila!"
        ],
        english_translation=(
            "The wild fig ripens through all twelve months, O brother! The sweet mountain berries ripen in spring! "
            "In the misty monsoon of Saun and Bhado, the sweet rains fall softly! "
            "And how delicious is the famous Baal Mithai of Almora town!"
        ),
        cultural_context="Worldwide recognized signature folk anthem of Kumaon, made internationally renowned by Mohan Upreti and the Kumaon folk troupe."
    ),
    FolkPoem(
        id="nyoli_forest_song",
        title_kumaoni="डाँडा-काँठा की न्योली",
        title_english="Nyoli of the Mountain Ridges",
        form="Nyoli",
        theme="Solitude, Mountain Longing, and Philosophy of Life",
        verses_kumaoni=[
            "उँच डांडा म घाम लागूँ, तल्लो गाड़ म छाँव।",
            "आपण मुलुक छाड़ि बेर, कसिक रौलो आन गाँव?"
        ],
        verses_roman=[
            "Unch daanda ma ghaam laagoon, tallo gaad ma chhaanv.",
            "Aapan muluk chhaadi ber, kasik raulo aan gaanv?"
        ],
        english_translation=(
            "Bright sunshine gleams on the mountain peak, while cool shadow rests in the river valley. "
            "Leaving one's beloved homeland behind, how can one ever feel at home in an alien village?"
        ),
        cultural_context="Traditional two-line metered couplet sung across pine hills by woodcutters, grass collectors, and shepherds echoing across valleys."
    ),
    FolkPoem(
        id="kalyug_varnan",
        title_kumaoni="कलयुग वर्णन",
        title_english="Description of the Degenerate Age (Kalyug Varnan)",
        form="Chhand / Satire",
        theme="Social Satire, Colonial Bureaucracy, and Moral Decline",
        verses_kumaoni=[
            "कलयुग आयो भारी, धरम करम सब छूटि गो।",
            "कचहरी म झूटो जितूँ, सांचो मन्खि रुणि छै।"
        ],
        verses_roman=[
            "Kalyug aayo bhaari, dharam karam sab chhooti go.",
            "Kachahari ma jhooto jitoon, saancho mankhi runi chhai."
        ],
        english_translation=(
            "The mighty age of Kali has descended; moral duty and righteous acts are abandoned. "
            "In the legal courts the liar triumphs, while the truthful person weeps in silence."
        ),
        cultural_context="Iconic early 19th-century folk satire composed by Krishna Pandey reflecting on social changes under early British and Gorkha rules."
    ),
    FolkPoem(
        id="bajyaani_ka_dhur",
        title_kumaoni="बज्याणी का धूर",
        title_english="High Ridges of Bajyaani (Himalayan Ecology)",
        form="Lokgeet / Nature Hymn",
        theme="Ecology, Sacred Oaks (Banj), Rhododendron, and Clean Water Spouts",
        verses_kumaoni=[
            "बाँझ-बुराँश का बोट बचाओ, धूर-धार म हरियाली लाओ।",
            "नौला-धारा सूखि जाला, जों जों जङ्गल कटि जाला।"
        ],
        verses_roman=[
            "Baanjh-buraansh ka bot bachaao, dhoor-dhaar ma hariyaali laao.",
            "Naula-dhaara sookhi jaala, jon jon jangal kati jaala."
        ],
        english_translation=(
            "Protect the sacred Oak and Rhododendron trees; bring verdant green to the mountain summits! "
            "The holy stepwells and spring spouts will wither dry wherever forests are felled."
        ),
        cultural_context="Ecological folk songs from Dr. Pramila Joshi's environmental education work linking Kumaoni culture to forest conservation."
    ),
    FolkPoem(
        id="kumaun_ke_samrat",
        title_kumaoni="कुमाऊँ के सम्राट (शौर्य गान)",
        title_english="Emperors of Kumaon (Dynastic Historical Epic)",
        form="Bir-Ras Kavya / Ballad",
        theme="Dynastic Chivalry of Katyuri and Chand Kings",
        verses_kumaoni=[
            "चंपावत की राजधानी, अल्मोड़ा को राजकाज।",
            "सोमचंद, कल्याण चंद, कुमाऊँ की शान आज।"
        ],
        verses_roman=[
            "Champaavat ki raajdhaani, Aalmoda ko raajkaaj.",
            "Somchand, Kalyaan Chand, Kumaun ki shaan aaj."
        ],
        english_translation=(
            "From the ancient throne of Champawat to the royal courts of Almora, "
            "Kings Som Chand and Kalyan Chand stand as the enduring pride of Kumaon."
        ),
        cultural_context="Epic historical verse by Chintamani Paliwal chronicling medieval Himalayan mountain kingdoms."
    ),
    FolkPoem(
        id="ghughuti_basuti",
        title_kumaoni="घुघूती बासूती (पारंपरिक बालगीत / लोरी)",
        title_english="Ghughuti Basuti (Traditional Folk Rhyme & Lullaby)",
        form="Balgeet / Lori",
        theme="Motherly Love, Himalayan Birds, Child Nurture, and Hearth",
        verses_kumaoni=[
            "निनुरी ढुलि गे, ढुलि गे मुयै ढुलि गे।",
            "बिछणो भुलि गे, भुलि गे मुयै भुलि गे।",
            "पानि-भरन भुलि गे, भुलि गे मुयै भुलि गे।",
            "रोट पक्वौण भुलि गे, भुलि गे मुयै भुलि गे।"
        ],
        verses_roman=[
            "Ninuri dhuli ge, dhuli ge muyai dhuli ge.",
            "Bichhno bhuli ge, bhuli ge muyai bhuli ge.",
            "Paani-bharan bhuli ge, bhuli ge muyai bhuli ge.",
            "Rot pakwaun bhuli ge, bhuli ge muyai bhuli ge."
        ],
        english_translation=(
            "Slumber has gently descended on the little one, o mother it has descended. "
            "In watching the child sleep, I forgot the bedding, forgot to fetch fresh water from the spring, "
            "and forgot to bake bread over the hearth!"
        ),
        cultural_context="Celebrated traditional Kumaoni nursery song and lullaby sung by mothers and grandmothers across generations in every hill hamlet, compiled in Hem Pant's 'Ghughuti Basuti' (2022)."
    )
]

AUTHORS: Dict[str, KumaoniAuthor] = {
    "badri_datt_pande": KumaoniAuthor(
        name_kumaoni="बद्री दत्त पाण्डे (कुमाऊँ केसरी)",
        name_english="Badri Datt Pande (Kumaun Kesari)",
        era="1882 – 1965",
        significance="Legendary freedom fighter, editor of Almora Akhbar and Shakti, leader of the historic 1921 Coolie-Begar abolition at Bageshwar, and author of the monumental 1937 history 'Kumaun ka Itihas'.",
        famous_works=["Kumaun ka Itihas (1937)", "Shakti Editorials", "Coolie-Begar Andolan History"],
        sample_quote={
            "kumaoni": "कुमाऊँ का वीर जनता ले अन्यायक विरुद्ध कभै सिर नि झुकाओ।",
            "roman": "Kumaun ka veer janta le anyaayak viruddh kabhai sir ni jhukaao.",
            "meaning": "The valiant people of Kumaon have never bowed their heads to tyranny and injustice."
        }
    ),
    "gunanand_juyal": KumaoniAuthor(
        name_kumaoni="डॉ. गुणानन्द जुयाल",
        name_english="Dr. Gunanand Juyal",
        era="Mid 20th Century",
        significance="Linguistic scholar who produced the authoritative comparative structural study of Central Pahari dialects (Garhwali and Kumaoni) and their Sanskrit/Prakrit foundations.",
        famous_works=["Madhya Pahadi Bhasha: Garhwali Kumauni ka Anushilan aur Uska Hindi se Sambandh (1967)"],
        sample_quote={
            "kumaoni": "मध्य पहाड़ी भाषाएं वैदिक संस्कृत और शौरसेनी प्राकृत की प्रत्यक्ष उत्तराधिकारिणी छन।",
            "roman": "Madhya Pahaadi bhaashaayein Vaidik Sanskrit aur Shaurseni Praakrit ki pratyaksh uttaraadhikaarini chhan.",
            "meaning": "Central Pahari languages are the direct inheritors of Vedic Sanskrit and Sauraseni Prakrit."
        }
    ),
    "krishna_pandey": KumaoniAuthor(
        name_kumaoni="कृष्ण पाण्डे (किष्णा पाण्डे)",
        name_english="Krishna Pandey",
        era="c. 1790 – 1850",
        significance="Earliest recorded Kumaoni satirist and folk poet, renowned for trenchant verses critiquing social degeneration, courtroom bribery, and colonial administration.",
        famous_works=["Kalyug Varnan", "Gorkhyani Satire", "Kachahari Chhand"],
        sample_quote={
            "kumaoni": "कलयुग आयो भारी, सांचो मन्खि रुणि छै।",
            "roman": "Kalyug aayo bhaari, saancho mankhi runi chhai.",
            "meaning": "The mighty age of degeneration has arrived; the honest man is left to weep."
        }
    ),
    "ganga_datt_upreti": KumaoniAuthor(
        name_kumaoni="पं. गंगा दत्त उप्रेती (राय बहादुर)",
        name_english="Pt. Ganga Datt Upreti (Rai Bahadur)",
        era="1834 – 1910",
        significance="Foundational scholar of Central Himalayan linguistics and folklore who compiled the monumental encyclopaedia of Kumaoni proverbs, axioms, and dialectology.",
        famous_works=["Proverbs & Folklore of Kumaun and Garhwal (1894)", "Hill Dialects of the Kumaon Division (1900)"],
        sample_quote={
            "kumaoni": "अपणा जोगि जोगता, पल्ले गौं का संत।",
            "roman": "Apna jogi jogta, palle gaun ka sant.",
            "meaning": "One's own local talent is taken for granted, while an outsider is revered."
        }
    ),
    "trilochan_pandey": KumaoniAuthor(
        name_kumaoni="डॉ. त्रिलोचन पाण्डे",
        name_english="Dr. Trilochan Pandey",
        era="1930 – 2020",
        significance="Eminent folklorist and academic pioneer whose doctoral research established the foundational taxonomy of Kumaoni oral genres (Jagar, Bhada, Nyoli, Akhaan).",
        famous_works=["Kumaoni Lok-Sahitya ki Prushthbhoomi (1962)", "Kumaoni Lok-Bhasha Vigyan", "Kumaoni Bhasha aur Uska Sahitya"],
        sample_quote={
            "kumaoni": "कुमाऊँनी लोक साहित्य हमैरि आत्मा और हिमालयी चेतना को दर्पण छ।",
            "roman": "Kumaoni lok sahitya hamairi aatma aur Himalayi chetna ko darpan chha.",
            "meaning": "Kumaoni folk literature is the true mirror of our collective soul and Himalayan consciousness."
        }
    ),
    "dewan_singh_bisht": KumaoniAuthor(
        name_kumaoni="ठाकुर दीवान सिंह बिष्ट",
        name_english="Thakur Dewan Singh Bisht",
        era="Early 20th Century",
        significance="Pioneering playwright and poet who introduced humorous, satirical court dramas and social commentary in everyday spoken Kumaoni.",
        famous_works=["Deewani Vinod", "Kumaoni Hasya Kavitavali"],
        sample_quote={
            "kumaoni": "मुकदमा लड़न म घर-बार बिकि जाँ, हाँसी-खुशी म जिनगि बिताओ!",
            "roman": "Mukadama ladan ma ghar-baar biki jaan, haansi-khushi ma jinagi bitaao!",
            "meaning": "Litigation ruins hearth and home; spend your life in joyful harmony."
        }
    ),
    "chintamani_paliwal": KumaoniAuthor(
        name_kumaoni="चिन्तामणी पालीवाल",
        name_english="Chintamani Paliwal",
        era="Mid 20th Century",
        significance="Prolific folklorist and poet who documented Kumaoni royal history in verse, along with compilations of travelogues and traditional folk songs.",
        famous_works=["Kumaun ke Samrat (Vols 1-4)", "Kumaun ke Prasiddh Lokgeet", "Shailani"],
        sample_quote={
            "kumaoni": "चंपावत की माटी म वीर कच्यूरी और चंद राजाओं को अमर इतिहास छ।",
            "roman": "Champaavat ki maati ma veer Katyuri aur Chand rajaon ko amar itihaas chha.",
            "meaning": "In the sacred soil of Champawat lies the immortal history of brave Katyuri and Chand kings."
        }
    ),
    "pramila_joshi": KumaoniAuthor(
        name_kumaoni="डॉ. प्रमिला जोशी",
        name_english="Dr. Pramila Joshi",
        era="Contemporary",
        significance="Author and ecological educationist who championed Himalayan environmental preservation and women's rural lore through Kumaoni songs.",
        famous_works=["Bajyaani Ka Dhur (Kumaoni Lokgeet)", "Himalayan Paryavaran Shiksha"],
        sample_quote={
            "kumaoni": "बाँझ-बुराँश हमैरि जीवनरेखा छन, इनर रक्षा हमरो धर्म छ।",
            "roman": "Baanjh-buraansh hamairi jeevanrekha chhan, inar raksha hamro dharam chha.",
            "meaning": "Oak and rhododendron are our lifeblood; protecting them is our sacred duty."
        }
    ),
    "gumani_pant": KumaoniAuthor(
        name_kumaoni="गुमानी पन्त (लोकरत्न पन्त)",
        name_english="Gumani Pant (Lokratna Pant)",
        era="1790 – 1846",
        significance="Revered as the Aadi Kavi (First Poet) of Kumaoni literature, master of multi-lingual verses blending Kumaoni, Sanskrit, and Khariboli.",
        famous_works=["Gumani Niti", "Kumaoni Lok Shatak", "Ganga Mahatmya"],
        sample_quote={
            "kumaoni": "जति देखूँ तति कौवा कागा, आपण मुलुक छाड़ि कताँ भागा?",
            "roman": "Jati dekhoon tati kauwa kaaga, aapan muluk chhaadi kataan bhaaga?",
            "meaning": "Witty social satire examining human migration and local governance."
        }
    ),
    "gaurda": KumaoniAuthor(
        name_kumaoni="गौर्दा (गौरीदत्त पाण्डे)",
        name_english="Gaurda (Gauridutt Pande)",
        era="1872 – 1939",
        significance="The fiery people's bard and nationalist freedom poet of Uttarakhand whose patriotic songs inspired the Coolie-Begar movement and social reform.",
        famous_works=["Kumaoni Padya Sangrah", "Gaurda Vani", "Desh Prem Git"],
        sample_quote={
            "kumaoni": "उठो, जाग्या, हमैरि बोलि हमैरि पछ्याण!",
            "roman": "Utho, jaagya, hamairi boli hamairi pachhyaan!",
            "meaning": "Call for cultural rejuvenation and preservation of mother tongue."
        }
    ),
    "charu_chandra_pande": KumaoniAuthor(
        name_kumaoni="डॉ. चारु चन्द्र पाण्डे",
        name_english="Dr. Charu Chandra Pande",
        era="1923 – 2018",
        significance="Eminent linguist, poet, and folklore chronicler who systematized Kumaoni grammar, idioms, and children's folk rhymes.",
        famous_works=["Kumaoni Lok Sahitya", "Angwal", "Dharohar"],
        sample_quote={
            "kumaoni": "हमैरि संस्कृति हिमालयक चोटी जसि पावन छ।",
            "roman": "Hamairi sanskriti Himaalayak choti jasi paavan chha.",
            "meaning": "Our cultural heritage is as sacred and lofty as the Himalayan peaks."
        }
    ),
    "girda": KumaoniAuthor(
        name_kumaoni="गिरीश तिवारी 'गिर्दा'",
        name_english="Girish Tiwari 'Girda'",
        era="1945 – 2010",
        significance="Legendary Jan-Kavi (People's Poet), folk dramatist, and voice of Uttarakhand's ecological and social movements (Chipko, Uttarakhand statehood).",
        famous_works=["Shikharon ke Swar", "Ham Ladte Rahe Re", "Rangdari", "Jaimin Kautik"],
        sample_quote={
            "kumaoni": "जैंत हमरो गौं, जैंत हमरो देश!",
            "roman": "Jaint hamro gaun, jaint hamro desh!",
            "meaning": "Victory to our village, victory to our mountain land!"
        }
    ),
    "heera_singh_rana": KumaoniAuthor(
        name_kumaoni="हीरा सिंह राणा",
        name_english="Heera Singh Rana",
        era="1942 – 2020",
        significance="Iconic Kumaoni folk lyricist, singer, and poet whose songs of hill yearning, rural migration, and nature resonated across millions.",
        famous_works=["Mankhaun Padyouv Main", "Maanilai Daani", "Hita Didi Hita Bhula", "Rangili Bindi"],
        sample_quote={
            "kumaoni": "मानिलै डानि म घाम लागूँ, तल्लो गाड़ म छाँव।",
            "roman": "Maanilai daani ma ghaam laagoon, tallo gaad ma chhaanv.",
            "meaning": "Sunlight gleams on Manila ridge, while cool shadow rests in the valley below."
        }
    ),
    "kabootari_devi": KumaoniAuthor(
        name_kumaoni="कबूतरी देवी",
        name_english="Kabootari Devi",
        era="1945 – 2018",
        significance="First female folk singer and living legend of Kumaoni oral traditions, pioneer of Teej-Tyohar, Ritu-Geet, and Nyoli recordings.",
        famous_works=["Kumaoni Lokgeet Sangrah", "Nyoli & Chaiti Gayan"],
        sample_quote={
            "kumaoni": "पहाड़क दर्द हमैरि न्योली म बोलूँ छ।",
            "roman": "Pahaadak dard hamairi nyoli ma booloon chha.",
            "meaning": "The deep longing of the mountains speaks through our Nyoli songs."
        }
    ),
    "mohan_upreti": KumaoniAuthor(
        name_kumaoni="मोहन उप्रेती",
        name_english="Mohan Upreti",
        era="1928 – 1997",
        significance="Pioneering theater composer, folklorist, and founder of Parvatiya Kala Kendra who brought 'Bedu Pako' and Kumaoni Ramlila to international renown.",
        famous_works=["Bedu Pako Baro Masa Arrangement", "Rajula Malushahi Musical Opera", "Kumaoni Loknatya"],
        sample_quote={
            "kumaoni": "लोक संगीत हमैरि माटी की सुगंध छ।",
            "roman": "Lok sangeet hamairi maati ki sugandh chha.",
            "meaning": "Folk music is the very fragrance of our mother soil."
        }
    ),
    "sher_singh_pangti": KumaoniAuthor(
        name_kumaoni="डॉ. शेर सिंह पांगती",
        name_english="Dr. Sher Singh Pangti",
        era="1937 – 2020",
        significance="Eminent ethnographer, historian, and folklorist of Johar Valley who founded the Tribal Heritage Museum in Munsyari and authored authoritative treatises on Himalayan cultural heritage.",
        famous_works=["Shauka: Seemavarti Janjaati", "Johar ka Itihaas va Sanskriti", "Kumaun Himalayan Heritage"],
        sample_quote={
            "kumaoni": "हिमालयक उच्च घाटियों की संस्कृति मानव और प्रकृतिक सामंजस्य की अद्भुत गाथा छ।",
            "roman": "Himaalayak uchha ghaatiyon ki sanskriti maanav aur prakritik saamanjasya ki adbhut gaatha chha.",
            "meaning": "The culture of high Himalayan valleys is a magnificent saga of harmony between human and nature."
        }
    ),
    "shivani_pant": KumaoniAuthor(
        name_kumaoni="गौरा पन्त 'शिवानी'",
        name_english="Gaura Pant 'Shivani'",
        era="1923 – 2003",
        significance="Renowned novelist and litterateur from Kumaon whose writings richly captured Kumaoni domestic life, folklore, dialects, customs, and women's inner worlds.",
        famous_works=["Chaudah Phere", "Krishnakali", "Kunti", "Bhairavi", "Aparadhini"],
        sample_quote={
            "kumaoni": "कुमाऊँ की घाटियों म रची-बसी संवेदना संसार भर कणि अनूठी छ।",
            "roman": "Kumaun ki ghaatiyon ma rachi-basi samvedana sansaar bhar kani anuthi chha.",
            "meaning": "The deep sensibilities nurtured in the valleys of Kumaon are unique to the entire world."
        }
    )
}


class LiteratureTreasury:
    """Interface to access Kumaoni folk epics, poetry, and canonical authors."""

    @staticmethod
    def get_epic(epic_id: str) -> Optional[FolkEpic]:
        return EPICS.get(epic_id)

    @staticmethod
    def list_epics() -> List[FolkEpic]:
        return list(EPICS.values())

    @staticmethod
    def list_poems(form: Optional[str] = None) -> List[FolkPoem]:
        if form:
            return [p for p in POEMS if p.form.lower() == form.lower()]
        return POEMS

    @staticmethod
    def get_author(author_id: str) -> Optional[KumaoniAuthor]:
        return AUTHORS.get(author_id)

    @staticmethod
    def list_authors() -> List[KumaoniAuthor]:
        return list(AUTHORS.values())
