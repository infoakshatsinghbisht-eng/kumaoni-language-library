"""
Digital Heritage & Folklore Integration Pipeline for Kumaoni Language Library.
Ingests:
- Kumaoni Songs Corpus (KSN-0001 to KSN-0020) from Sheet 3
- Kumaoni Holi Songs Corpus (KHL-0001 to KHL-0020) from Sheet 4
- Digital Archive Sources (SRC-001 to SRC-007) from Sheet 5
- Vocabulary extraction from song texts into words.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'kumaoni', 'lexicon', 'data')
CULTURE_DATA_DIR = os.path.join(ROOT_DIR, 'kumaoni', 'culture', 'data')
os.makedirs(CULTURE_DATA_DIR, exist_ok=True)

WORDS_FILE = os.path.join(DATA_DIR, 'words.json')
SONGS_FILE = os.path.join(CULTURE_DATA_DIR, 'songs.json')
HOLI_FILE = os.path.join(CULTURE_DATA_DIR, 'holi_songs.json')
SOURCES_FILE = os.path.join(CULTURE_DATA_DIR, 'digital_sources.json')

# -------------------------------------------------------------
# 1. EXTRACT NEW WORDS FROM SONG & FOLKLORE CORPUS
# -------------------------------------------------------------
NEW_SONG_WORDS = [
    {"kumaoni": "मैता", "roman": "maita", "english": "maternal home of a married woman / natal village", "hindi": "मायका / पीहर", "pos": "noun", "category": "kinship"},
    {"kumaoni": "हियो", "roman": "hiyo", "english": "heart / inner bosom / innermost soul", "hindi": "हृदय / मन / छाती", "pos": "noun", "category": "anatomy"},
    {"kumaoni": "नराई", "roman": "naraai", "english": "deep nostalgic yearning / homesickness for maternal home", "hindi": "मायके की विरह-वेदना / पुरानी याद", "pos": "noun", "category": "emotions"},
    {"kumaoni": "जुन्याली", "roman": "junyaali", "english": "radiant moonlit night in mountain valleys / moonlight", "hindi": "चाँदनी रात / चाँदनी", "pos": "noun", "category": "nature"},
    {"kumaoni": "दगड़िया", "roman": "dagadya", "english": "beloved companion / close friend / comrade", "hindi": "साथी / सखा / मित्र", "pos": "noun", "category": "people"},
    {"kumaoni": "बाना", "roman": "baana", "english": "graceful young maiden / mountain belle / sweetheart", "hindi": "युवती / सुंदरी / प्रेयसी", "pos": "noun", "category": "people"},
    {"kumaoni": "जोबन", "roman": "joban", "english": "youthful prime / bloom and vigor of youth", "hindi": "यौवन / जवानी", "pos": "noun", "category": "state"},
    {"kumaoni": "फाग", "roman": "phaag", "english": "traditional spring songs celebrating the Holi festival", "hindi": "फाग / वसंत व होली के गीत", "pos": "noun", "category": "culture"},
    {"kumaoni": "चीर", "roman": "cheer", "english": "sacred ceremonial Holi mast / colored cloth banner tied to a tree branch", "hindi": "होली का चीर / रंगीन ध्वज-स्तंभ", "pos": "noun", "category": "culture"},
    {"kumaoni": "दमुवां", "roman": "damuwaan", "english": "traditional hemispherical copper kettledrum paired with Dhol", "hindi": "दमाऊँ / छोटा नगाड़ा", "pos": "noun", "category": "tools"},
    {"kumaoni": "अबीर", "roman": "abeer", "english": "scented colored powder sprinkled during festive gatherings", "hindi": "अबीर / गुलाल", "pos": "noun", "category": "culture"},
    {"kumaoni": "चुनर", "roman": "chunar", "english": "traditional colorful patterned scarf or veil", "hindi": "चुनरी / ओढ़नी", "pos": "noun", "category": "clothing"}
]

with open(WORDS_FILE, 'r', encoding='utf-8') as f:
    words = json.load(f)

word_set = {w['kumaoni'] for w in words}
added_w = 0
for w in NEW_SONG_WORDS:
    if w['kumaoni'] not in word_set:
        words.append(w)
        word_set.add(w['kumaoni'])
        added_w += 1

with open(WORDS_FILE, 'w', encoding='utf-8') as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Words: Added {added_w} song/folklore words. Total: {len(words)}")

# -------------------------------------------------------------
# 2. SONGS CORPUS (KSN-0001 to KSN-0020)
# -------------------------------------------------------------
SONGS_DATA = [
    {
        "id": "KSN-0001",
        "title": "बेडु पाको बारो मासा",
        "roman": "Bedu Pako Baro Masa",
        "artist": "Traditional / Mohan Upreti arrangement",
        "genre": "Folk Song / Valley Lyrical",
        "corpus": "Traditional corpus",
        "theme": "Mountain seasons, flora, and eternal Pahari longing",
        "lyrics_sample": "बेड़ू पाको बारह मासा, ओ नरण काफल पाको चैत, मेरी छैला!\nरुपै की सिलिंग, टका की लिबोंग...",
        "verses": [
            "बेड़ू पाको बारह मासा, ओ नरण काफल पाको चैत, मेरी छैला!",
            "रुपै की सिलिंग, टका की लिबोंग...",
            "अल्मोड़ा की नंदा देवी, ओ नरण फूल चढ़ूँलो पाती, मेरी छैला!",
            "काफल पाको चैत, मेरी छैला!"
        ],
        "english_translation": "Wild figs ripen throughout the twelve months, oh Naran; wild bayberries ripen in the spring month of Chait, my love!",
        "cultural_context": "The international anthem of Kumaon, made famous worldwide by Mohan Upreti and Parvatiya Kala Kendra.",
        "source_url": "https://www.kumauni.in/"
    },
    {
        "id": "KSN-0002",
        "title": "घुघुती ना बासा",
        "roman": "Ghughuti Na Basa",
        "artist": "Traditional / Folk Ballad",
        "genre": "Folk Song / Separation (Viraha)",
        "corpus": "Traditional corpus",
        "theme": "Homesickness (Naraai) and dove's melancholic cooing",
        "lyrics_sample": "घुघुती ना बासा, न बस घुघुती बासा...\nमैता की नराई लागी, छाती म झुरण...",
        "verses": [
            "घुघुती ना बासा, न बस घुघुती बासा,",
            "तू बासि-बासि हिया म आगि न लगा!",
            "मैता की नराई लागी, छाती म झुरण,",
            "परदेस म छन दाज्यू, कख जाणू मैं!"
        ],
        "english_translation": "Do not coo, O mountain dove, do not coo! Your plaintive call kindles the fire of yearning for my mother's home in my heart.",
        "cultural_context": "Sung by married women experiencing intense homesickness (naraai) for their maternal village (maita).",
        "source_url": "https://www.kumauni.in/"
    },
    {
        "id": "KSN-0003",
        "title": "काफल पाको चैत",
        "roman": "Kafal Pako Chait",
        "artist": "Traditional / Ritu-Geet",
        "genre": "Seasonal Folk Song",
        "corpus": "Traditional corpus",
        "theme": "Spring berry ripening and the cuckoo's tragic forest call",
        "lyrics_sample": "काफल पाको मिल नी चाखो, पुरपुड़ा पाको चार...\nबैनि रोणी बन म सुवा, कख ग्या म्यर दाज्यू...",
        "verses": [
            "काफल पाको मिल नी चाखो, पुरपुड़ा पाको चार,",
            "चैत का मैना म काफल पाकि रैन!",
            "डाल्यूँ-डाल्यूँ म बोलूँ काफल पक्वा पंछी,",
            "याद करूँ अपनी ईजा-बाबू कणि!"
        ],
        "english_translation": "The kafal berries have ripened, yet I tasted none! In the spring month of Chait, the cuckoo cries through the forest branches.",
        "cultural_context": "Legend of the innocent hill sister who starved while guarding wild bayberries for her brother.",
        "source_url": "https://www.kumauni.in/"
    },
    {
        "id": "KSN-0004",
        "title": "म्यर शोभनी होस्यारा",
        "roman": "Myar Shobhani Hosyaara",
        "artist": "Traditional / Satirical Folk",
        "genre": "Humorous Folk Song",
        "corpus": "Traditional corpus",
        "theme": "Witty village satire on a lazy yet boastful son",
        "lyrics_sample": "अहा सब च्यालों है बेरा म्यर शोभनी होस्यारा...\nसब ल्यूंनि नगदा भागि म्यर शोभनी उधारा...",
        "verses": [
            "अहा सब च्यालों है बेरा म्यर शोभनी होस्यारा,",
            "सब ल्यूंनि नगदा भागि म्यर शोभनी उधारा!",
            "सब खानी हो रोट साग, म्यर शोभनी शिकारा,",
            "सब हिटनी पाँव-पैदल, म्यर शोभनी असवारा!"
        ],
        "english_translation": "Of all sons my Shobhan is the sharpest! Everyone buys on cash, but my Shobhan gets everything on credit!",
        "cultural_context": "Celebrated comic folk song poking fun at indulgent village parents and roguish sons.",
        "source_url": "https://devbhoomidarshan.in/old-kumauni-song-lyrics/"
    },
    {
        "id": "KSN-0005",
        "title": "तेरी खुटी मेरी सलाम",
        "roman": "Teri Khuti Meri Salaam",
        "artist": "Traditional Dialogue Song",
        "genre": "Folk Dialogue / Romantic Debate",
        "corpus": "Traditional corpus",
        "theme": "Husband-wife banter regarding visiting maternal home in the monsoon",
        "lyrics_sample": "तेरी खुटी मेरी सलाम, मैं मैता जाण दे भागी...\nचौमासी ढुंग चिफलो, तेर खुटो रड़ी जालो...",
        "verses": [
            "तेरी खुटी मेरी सलाम, मैं मैता जाण दे भागी!",
            "तेरि खुटी मेरी सलाम, तू मैता नि जा भागि!",
            "चौमासी ढुंग चिफलो, तेर खुटो रड़ी जालो,",
            "मेरो हियो झुरि जालो, तू मैता नी जा भागि!"
        ],
        "english_translation": "I bow down to your feet, pray let me visit my mother's home! But slippery are the stones in the monsoon; if your foot slips, my heart will pine away!",
        "cultural_context": "Traditional humorous domestic dialogue capturing the risks of Himalayan monsoon trails.",
        "source_url": "https://devbhoomidarshan.in/old-kumauni-song-lyrics/"
    },
    {
        "id": "KSN-0006",
        "title": "सुपारि खई खई सुण माया",
        "roman": "Supari Khai Khai Sun Maya",
        "artist": "Traditional Folk Song",
        "genre": "Lyrical Romance",
        "corpus": "Traditional corpus",
        "theme": "Hill harvest, bright winter sun, and romance",
        "lyrics_sample": "हई हई हई सुपारि खई सुण माया, क्या रामरो घाम लागो छ...\nनान माणी मडुवा भरो ग्यूं भरा ठुल माणी...",
        "verses": [
            "हई हई हई सुपारि खई सुण माया,",
            "क्या रामरो घाम लागो छ!",
            "नान माणी मडुवा भरो ग्यूं भरा ठुल माणी,",
            "बांसुई का बन भागि तू मेरि राधिका, मैं तेरो मोहन!"
        ],
        "english_translation": "Chewing betelnut listen, my beloved, what delightful sunshine warms our hills! In the bamboo grove you are my Radha, and I am your Krishna.",
        "cultural_context": "Harvest love song sung in terrace fields during grain threshing.",
        "source_url": "https://devbhoomidarshan.in/old-kumauni-song-lyrics/"
    },
    {
        "id": "KSN-0007",
        "title": "माठु माठु हिटैली मेरी बाना",
        "roman": "Maathu Maathu Hitaili Meri Baana",
        "artist": "Traditional Pastoral Lyric",
        "genre": "Forest Romantic Song",
        "corpus": "Traditional corpus",
        "theme": "Gentle footsteps on rugged mountain slopes",
        "lyrics_sample": "पहाड़ का ऊँचा नीचा डाना, माठु माठु हिटैलो मेरी बाना...\nमडुवा को माणो सुवा मडुवा को माणो...",
        "verses": [
            "पहाड़ का ऊँचा नीचा डाना,",
            "माठु माठु हिटैलो मेरी बाना!",
            "मडुवा को माणो सुवा मडुवा को माणो,",
            "हँसी ल्हिये नाचि ल्हिये द्वी दिन बचणो,",
            "चार दिन रूंछो वे जोबना!"
        ],
        "english_translation": "High and steep are the mountain ridges; walk softly, gently, my graceful maiden! Life is brief as a handful of millet, dance and laugh while youth blooms.",
        "cultural_context": "Philosophical Pahari romance celebrating youth while urging caution on dangerous mountain paths.",
        "source_url": "https://devbhoomidarshan.in/old-kumauni-song-lyrics/"
    },
    {
        "id": "KSN-0008",
        "title": "यो बाटो का जान्या",
        "roman": "Yo Baato Ka Jaanya",
        "artist": "Traditional Pilgrim / Trail Song",
        "genre": "Folk Ballad",
        "corpus": "Traditional corpus",
        "theme": "Winding Himalayan trails leading to mountain shrines",
        "lyrics_sample": "यो बाटो कां जान्यां होला, सुरा सुरा देवी का मंदिर...\nचमकनी गिलास सुवा रमकनी चाहा छ...",
        "verses": [
            "यो बाटो कां जान्यां होला, सुरा सुरा देवी का मंदिर!",
            "चमकनी गिलास सुवा रमकनी चाहा छ,",
            "तेरी मेरी पिरीत कों दुनिये डाहा छ!",
            "तेरो बाटों चानें चानें उमर काटो मैता!"
        ],
        "english_translation": "Where does this mountain path lead? Step by step to the shrine of the goddess! The world is envious of our love, as I spend my youth watching for your return.",
        "cultural_context": "Iconic trail song blending sacred shrine pilgrimage with eternal romantic devotion.",
        "source_url": "https://devbhoomidarshan.in/old-kumauni-song-lyrics/"
    },
    {
        "id": "KSN-0009",
        "title": "ओ परूवा बौज्यूँ",
        "roman": "O Paruwa Bojyoon",
        "artist": "Traditional Folk Song",
        "genre": "Domestic Folk Ballad",
        "corpus": "Traditional corpus",
        "theme": "Daughter-in-law demanding fair clothing from parents-in-law",
        "lyrics_sample": "ओ परूवा बौज्यू, आँगड़ि क्ये ल्याछा यस...\nओ परूली ईजा, तू कस माँगि छै कस...",
        "verses": [
            "ओ परूवा बौज्यू, आँगड़ि क्ये ल्याछा यस,",
            "नै टुपुक बूटा, घाघरि क्ये ल्याछा यस!",
            "ओ परूली ईजा, तू कस माँगि छै कस,",
            "धन तेरो मिजाता, हाई कस मांग छै कस!"
        ],
        "english_translation": "O elder father-in-law, what kind of traditional dress have you brought? And mother-in-law, why do you scrutinize all that I request?",
        "cultural_context": "Traditional domestic teasing song performed during mountain wedding feasts and fair trips.",
        "source_url": "https://devbhoomidarshan.in/old-kumauni-song-lyrics/"
    },
    {
        "id": "KSN-0010",
        "title": "झन दिया बौज्यूँ छाना बिलोरी",
        "roman": "Jhan Diya Bojyoon Chhaana Bilori",
        "artist": "Traditional Folk Ballad",
        "genre": "Social Folk Song",
        "corpus": "Traditional corpus",
        "theme": "A daughter's plea against marriage into a harsh, water-scarce village",
        "lyrics_sample": "झन दिया बौज्यू छाना बिलोरी...\nसासुलि दारुण बड़ी कुटैली, पाणी को न्हौलो दूर...",
        "verses": [
            "झन दिया बौज्यू छाना बिलोरी,",
            "सासुलि दारुण बड़ी कुटैली!",
            "पाणी को न्हौलो दूर डाना म,",
            "घास का बोझा भारी उठैली!"
        ],
        "english_translation": "O father, do not marry me into Chhana Bilori! The mother-in-law there is stern and cruel, and the water spring is far up the ridge!",
        "cultural_context": "Expresses the realistic hardships of mountain women fetching water and grass in steep villages.",
        "source_url": "https://devbhoomidarshan.in/old-kumauni-song-lyrics/"
    },
    {
        "id": "KSN-0011",
        "title": "जय जय हो बदरी नाथ के",
        "roman": "Jai Jai Ho Badri Nath Ke",
        "artist": "Traditional Devotional Bard",
        "genre": "Devotional Folk Song (Bhajan)",
        "corpus": "Traditional corpus",
        "theme": "Praise of Badrinath, Kedarnath, and sacred land of Kumaon-Garhwal",
        "lyrics_sample": "जय जय हो बदरी नाथ के, केदार नाथ के...\nशिवं ज्यू की तपो भूमि, देवतों को जनमा भूमि म्यर कुमू गढवाला...",
        "verses": [
            "जय जय हो बदरी नाथ के, केदार नाथ के,",
            "जै तेरी गोमुखा, गंगोत्री ज्यू की धार!",
            "शिवं ज्यू की तपो भूमि, देवतों की जनम भूमि,",
            "म्यर कुमू गढवाला!"
        ],
        "english_translation": "Victory to Lord Badrinath and Kedarnath! The penance grounds of Shiva, the sacred birthplace of gods—my beloved Kumaon and Garhwal!",
        "cultural_context": "Sung by pilgrims on mountain trails leading across Himalayan shrines.",
        "source_url": "https://devbhoomidarshan.in/old-kumauni-song-lyrics/"
    },
    {
        "id": "KSN-0012",
        "title": "रंगीली धाना",
        "roman": "Rangili Dhana",
        "artist": "Traditional Folk / Popular Recorded",
        "genre": "Folk Dance Song (Jhora)",
        "corpus": "Traditional corpus",
        "theme": "The vibrant charm of mountain damsel Dhana of Almora",
        "lyrics_sample": "रंगीली धाना, अल्मोड़ा की बाना...\nकान म झुमका, माथा म बिन्दुली, कमर म घाघरी...",
        "verses": [
            "रंगीली धाना, अल्मोड़ा की बाना,",
            "कान म झुमका, माथा म बिन्दुली!",
            "रंगीलो देश हमरो देवभूमि पहाड़ा,",
            "नाचो-गावो मिलि बेर सब दगड़िया!"
        ],
        "english_translation": "Vibrant Dhana, charming belle of Almora, wearing earrings in ears and bindi on forehead! Our colorful Devbhoomi hills echo with dance and song.",
        "cultural_context": "Energetic Jhora dance song performed at fairs and community festivals.",
        "source_url": "https://lyricstranslate.com/en/language/kumaoni-lyrics"
    },
    {
        "id": "KSN-0013",
        "title": "सुण ले दगड़िया",
        "roman": "Sun Le Dagadya",
        "artist": "Traditional / Hill Movement Song",
        "genre": "Folk Song / Social Consciousness",
        "corpus": "Traditional corpus",
        "theme": "Solidarity and hill hardships among comrades",
        "lyrics_sample": "सुण ले दगड़िया, बात सुण ले...\nपहाड़ की पीड़ा हमैरि सुण ले, बाँझ-बुराँश की छाया म बस ले...",
        "verses": [
            "सुण ले दगड़िया, बात सुण ले,",
            "पहाड़ की पीड़ा हमैरि सुण ले!",
            "बाँझ-बुराँश की छाया म बस ले,",
            "माटी को ऋण आपणो चुका ले!"
        ],
        "english_translation": "Listen, my companion, hear my words! Understand the deep yearning of our hills, and repay the debt we owe to our mother soil.",
        "cultural_context": "Anthem of regional solidarity and ecological preservation.",
        "source_url": "https://lyricstranslate.com/en/language/kumaoni-lyrics"
    },
    {
        "id": "KSN-0014",
        "title": "बलमा घर आयो फागुन में",
        "roman": "Balma Ghar Aayo Phaagun Mein",
        "artist": "Traditional / Seasonal Holi",
        "genre": "Holi / Seasonal Folk",
        "corpus": "Traditional corpus",
        "theme": "Spring arrival of soldier spouse for Phalguna festival",
        "lyrics_sample": "बलमा घर आयो फागुन में, खेलूँगी होरी रंग-अबीर...\nकेसर घोरूँगी, रंग बरसाऊँगी...",
        "verses": [
            "बलमा घर आयो फागुन में,",
            "खेलूँगी होरी रंग-अबीर!",
            "केसर घोरूँगी, पिचकारी भरूँगी,",
            "पहाड़क डाना म फाग गूँजि रौ!"
        ],
        "english_translation": "My beloved spouse has returned home in the spring month of Phalguna; I shall play Holi with saffron water and fragrant abeer powder!",
        "cultural_context": "Traditional seasonal Holi celebration song honoring returning hill soldiers.",
        "source_url": "https://www.ekumaon.com/2024/03/10-famous-holi-songs-of-kumaon-uttarakhand.html"
    },
    {
        "id": "KSN-0015",
        "title": "जोगी आयो शहर में व्योपारी",
        "roman": "Jogi Aayo Shahar Mein Vyopaari",
        "artist": "Traditional / Ascetic Ballad",
        "genre": "Folk Ballad / Mystical",
        "corpus": "Traditional corpus",
        "theme": "The wandering ascetic sage arriving in the mountain bazaar",
        "lyrics_sample": "जोगी आयो शहर में व्योपारी, अंग भभूत गले मृगछाला...\nमाया-मोह सब झूठी बाता...",
        "verses": [
            "जोगी आयो शहर में व्योपारी,",
            "अंग भभूत गले मृगछाला!",
            "हाथ म खप्पर, चिमटा खड़कै,",
            "राम नाम को अमृत बाँटै!"
        ],
        "english_translation": "A mystic ascetic has arrived in the hill bazaar, ashes smeared upon his limbs and deer-pelt over his shoulder, dispensing the nectar of devotion.",
        "cultural_context": "Nath yogi tradition deeply interwoven with Kumaon's Gopichand and Gorakhnath folklore.",
        "source_url": "https://kavitahindikavita.wordpress.com/"
    },
    {
        "id": "KSN-0016",
        "title": "निमंत्रण",
        "roman": "Nimantran",
        "artist": "Traditional Ritu-Geet",
        "genre": "Seasonal Folk Song",
        "corpus": "Traditional corpus",
        "theme": "Invitation to celebrate spring blossoms in Kumaon",
        "lyrics_sample": "फौग का दिना ऐ रैन, रंग खेलण आ जा सुवा...\nबुराँश फुली गो डाना म, हरियाली छै गै...",
        "verses": [
            "फौग का दिना ऐ रैन, रंग खेलण आ जा सुवा,",
            "बुराँश फुली गो डाना म, हरियाली छै गै!",
            "घास काटना दगड़िया, न्योली गावनी,",
            "आ जा हमरा गौं म बहार ऐ गै!"
        ],
        "english_translation": "The joyful days of spring have arrived; come, beloved, let us play with flowers! Rhododendrons bloom on ridges, and springtime fills our village.",
        "cultural_context": "Celebration of Chait and Phalguna blossoming across oak forests.",
        "source_url": "https://kavitahindikavita.wordpress.com/"
    },
    {
        "id": "KSN-0017",
        "title": "कैले बाजी मुरुली",
        "roman": "Kaile Baaji Muruli",
        "artist": "Gopal Babu Goswami",
        "genre": "Recorded Folk Legend",
        "corpus": "Modern/recorded corpus",
        "theme": "Haunting pastoral flute melodies across Kumaoni ridges",
        "lyrics_sample": "कैले बाजी मुरुली बैणा, कख बाजी मुरुली...\nडाना-काना गूँजी मुरुली, सुर सुणी मन भुलि गे...",
        "verses": [
            "कैले बाजी मुरुली बैणा, कख बाजी मुरुली,",
            "डाना-काना गूँजी मुरुली, सुर सुणी मन भुलि गे!",
            "चीड़ का बना म कख बाजी मुरुली,",
            "गौंका ग्वाला ले बजाई मुरुली!"
        ],
        "english_translation": "Who played the melodious flute, O sister, where did that flute sound? Resounding across peaks and valleys, its music enchanted my soul!",
        "cultural_context": "Landmark recording by Gopal Babu Goswami, the immortal Voice of Kumaon.",
        "source_url": "https://www.youtube.com/"
    },
    {
        "id": "KSN-0018",
        "title": "हाय तेरी रुमाला",
        "roman": "Haay Teri Rumaala",
        "artist": "Gopal Babu Goswami",
        "genre": "Recorded Modern Folk",
        "corpus": "Modern/recorded corpus",
        "theme": "Silk kerchief and mountain courtship",
        "lyrics_sample": "हाय तेरी रुमाला गुलाबी मुखड़ी, घुंघराली जुल्फी तेरी चम्पा कसी मुखड़ी...\nअल्मोड़ा का बजार म भेंट भई...",
        "verses": [
            "हाय तेरी रुमाला गुलाबी मुखड़ी,",
            "घुंघराली जुल्फी तेरी चम्पा कसी मुखड़ी!",
            "अल्मोड़ा का बजार म भेंट भई सुवा,",
            "नजरों से दिल म तीर मारी गे!"
        ],
        "english_translation": "Ah, your silk kerchief and rosy countenance, your curled locks and radiant face! We met in Almora bazaar, and your glance pierced my heart.",
        "cultural_context": "One of the most famous Pahari love songs in Himalayan music history.",
        "source_url": "https://www.youtube.com/"
    },
    {
        "id": "KSN-0019",
        "title": "छूटी गे नैनीताल",
        "roman": "Chhooti Ge Nainitaal",
        "artist": "Gopal Babu Goswami",
        "genre": "Migration Folk Song",
        "corpus": "Modern/recorded corpus",
        "theme": "Rural migration and painful departure from hill lakes and valleys",
        "lyrics_sample": "छूटी गे नैनीताल म्यर छूटी गे, काठगोदाम म छूटी गे रेल...\nडाना-काँठ छूटि गया, रोणी छै आँखा...",
        "verses": [
            "छूटी गे नैनीताल म्यर छूटी गे,",
            "काठगोदाम म छूटी गे रेल!",
            "डाना-काँठ छूटि गया, छूटि ग्या घर-बार,",
            "परदेश जाँछू मैं, छूटी गे पहाड़!"
        ],
        "english_translation": "Left behind is my Nainital, the railway departs from Kathgodam! Left behind are the ridges and my homestead; I journey to distant lands, leaving my hills behind.",
        "cultural_context": "Heart-wrenching classic on Pahari out-migration (*Palaayan*) to lowland cities.",
        "source_url": "https://www.youtube.com/"
    },
    {
        "id": "KSN-0020",
        "title": "ओ भिना कसक",
        "roman": "O Bhina Kasak",
        "artist": "Gopal Babu Goswami",
        "genre": "Humorous Kinship Song",
        "corpus": "Modern/recorded corpus",
        "theme": "Witty kinship banter between sister-in-law (Saali) and brother-in-law (Bhina)",
        "lyrics_sample": "ओ भिना कसक, कख जाँछा भिना...\nमोटर म बैठि भिना अल्मोड़ा जाँछा, हमरी लीजि के ल्यूँछा...",
        "verses": [
            "ओ भिना कसक, कख जाँछा भिना,",
            "मोटर म बैठि भिना अल्मोड़ा जाँछा!",
            "हमरी लीजि बालमिठाई क्ये ल्यूँछा,",
            "हँसि-हँसि भिना बात करूँछा!"
        ],
        "english_translation": "O brother-in-law, where are you bound? Riding the bus to Almora, what famous Baal-Mithai sweet will you bring back for me?",
        "cultural_context": "Playful Kumaoni kinship humor (*Bhina-Saali*) typical of hill family gatherings.",
        "source_url": "https://www.youtube.com/"
    }
]

with open(SONGS_FILE, 'w', encoding='utf-8') as f:
    json.dump(SONGS_DATA, f, ensure_ascii=False, indent=2)

print(f"Saved {len(SONGS_DATA)} songs to {SONGS_FILE}")

# -------------------------------------------------------------
# 3. HOLI SONGS CORPUS (KHL-0001 to KHL-0020)
# -------------------------------------------------------------
HOLI_DATA = [
    {
        "id": "KHL-0001",
        "title": "गोरी प्यारी लागे है तेरो झनकारो",
        "form": "Baithaki/Khadi Holi",
        "raag": "Khamaj",
        "theme": "Playful ankle-bell jingling and spring revelry",
        "verses": [
            "गोरी प्यारी लागे है तेरो झनकारो,",
            "पायल की झनकार म मदन मचायो भारी!",
            "फागुन को मैना म अबीर उड़ायो,",
            "रंग म भिगोई दियो चूनर सारी!"
        ],
        "english_translation": "Charming maiden, lovely is the chime of your anklets! In the spring month of Phalguna, colored powders fly as your scarf is drenched in color.",
        "archive_source": "Kumaoni Holi Archive",
        "source_url": "https://www.kumaoniholiarchive.org/audio"
    },
    {
        "id": "KHL-0002",
        "title": "होली खेलन मैं अनूप सखिरी",
        "form": "Baithaki Holi",
        "raag": "Kafi",
        "theme": "Incomparable beauty of Braj Holi celebrated in Himalayan courtyards",
        "verses": [
            "होली खेलन मैं अनूप सखिरी,",
            "नंद के लाल संग रंग रली कीनी!",
            "अबीर गुलाल उड़ै अंबर म,",
            "मनमोहन ले पिचकारी दीनी!"
        ],
        "english_translation": "Incomparable is the joy of playing Holi, O companion, reveling in colors with the prince of Nanda!",
        "archive_source": "Kumaoni Holi Archive",
        "source_url": "https://www.kumaoniholiarchive.org/audio"
    },
    {
        "id": "KHL-0003",
        "title": "केहि विधि फाग रचायो",
        "form": "Baithaki Holi",
        "raag": "Dhrupad / Dhamar",
        "theme": "Classical poetic wonder at the choreography of spring colors",
        "verses": [
            "केहि विधि फाग रचायो गिरधर,",
            "ग्वाल-बाल सब संग सिधायो!",
            "कुंकुम केसर घोरी कड़ाही म,",
            "गोपिन के मुख रंग लगायो!"
        ],
        "english_translation": "In what wondrous manner has Girdhar orchestrated this spring festival, stirring cauldrons of saffron and applying color to the gopis' faces!",
        "archive_source": "Kumaoni Holi Archive",
        "source_url": "https://www.kumaoniholiarchive.org/audio"
    },
    {
        "id": "KHL-0004",
        "title": "सैयाँ सारी हमारी रंगाई क्यों न दो",
        "form": "Baithaki Holi",
        "raag": "Desh / Sorath",
        "theme": "Wife urging spouse to dye her garments in spring colors",
        "verses": [
            "सैयाँ सारी हमारी रंगाई क्यों न दो,",
            "होली आई री फागुन म!",
            "धानी रंग म पियवा रंगाई दियो,",
            "पहाड़क आँगन म रंग बरसाई दियो!"
        ],
        "english_translation": "O beloved, why do you not get my saree dyed for Holi in the month of Phalguna? Rain colors across our mountain courtyard!",
        "archive_source": "Kumaoni Holi Archive",
        "source_url": "https://www.kumaoniholiarchive.org/audio"
    },
    {
        "id": "KHL-0005",
        "title": "हैं सब अपने अपने मैं सजनी",
        "form": "Baithaki Holi",
        "raag": "Bhairavi",
        "theme": "Companions gathering in joyous chamber communion",
        "verses": [
            "हैं सब अपने अपने मैं सजनी,",
            "आनंद उमग्यो री आज आँगन म!",
            "ढोलक मंजीरा की ताल म बाजे,",
            "बैठकी होली म सुर सजे!"
        ],
        "english_translation": "Each is absorbed in her own delight, O friend, as bliss overflows today in our courtyard to the rhythm of dholak and manjeera!",
        "archive_source": "Kumaoni Holi Archive",
        "source_url": "https://www.kumaoniholiarchive.org/audio"
    },
    {
        "id": "KHL-0006",
        "title": "होली खेल रहे नंदलाला गोकुल की कुंज गली में",
        "form": "Baithaki Holi",
        "raag": "Kafi",
        "theme": "Krishna and Gopis celebrating Holi in narrow bowers",
        "verses": [
            "होली खेल रहे नंदलाला गोकुल की कुंज गली में,",
            "हाथन कनक कटोरी लीनी, अबीर गुलाल उड़ाय रहे!",
            "गोपी ग्वालन संग रंग मचायो,",
            "गोकुल की कुंज गली में!"
        ],
        "english_translation": "Nandalala plays Holi in the leafy lanes of Gokul, holding golden cups and scattering red vermilion on all around!",
        "archive_source": "Kumaoni Holi Archive",
        "source_url": "https://www.kumaoniholiarchive.org/audio"
    },
    {
        "id": "KHL-0007",
        "title": "साजन रे चुनरिया मैका लाल रंगा दे",
        "form": "Baithaki Holi",
        "raag": "Khamaj",
        "theme": "Plea for red bridal chunari on spring festival",
        "verses": [
            "साजन रे चुनरिया मैका लाल रंगा दे,",
            "होली को त्योहार आयो!",
            "लाल अबीर म गोटा जड़ाई दे,",
            "देवभूमि म रंग उड़ायो!"
        ],
        "english_translation": "O beloved, dye my veil deep scarlet, for the joyous festival of Holi has arrived!",
        "archive_source": "Kumaoni Holi Archive",
        "source_url": "https://www.kumaoniholiarchive.org/audio"
    },
    {
        "id": "KHL-0008",
        "title": "कहियो संदेशा",
        "form": "Baithaki Holi / Viraha",
        "raag": "Pilu",
        "theme": "Message to distant soldier husband across mountain passes",
        "verses": [
            "कहियो संदेशा मेरो पियवा कणि जाई,",
            "फागुन आयो परदेश म मत रुको!",
            "घर म सजी गो होली को रंग,",
            "चली आओ पियवा अपनी पहाड़ी म!"
        ],
        "english_translation": "Deliver my message to my faraway beloved: spring has arrived, do not linger in foreign plains; return to your native hills!",
        "archive_source": "Kumaoni Holi Archive",
        "source_url": "https://www.kumaoniholiarchive.org/audio"
    },
    {
        "id": "KHL-0009",
        "title": "मेरो रंगीलो देवर घर आई रौ छो",
        "form": "Mahila / Khadi Holi",
        "raag": "Chhaiti / Folk",
        "theme": "Witty women's celebration of brother-in-law's homecoming",
        "verses": [
            "मेरो रंगीलो देवर घर आई रौ छो,",
            "हाथ म अबीर की झोली ली रौ छो!",
            "भाभी-देवर की होली म ठट्ठा,",
            "हाँसी-हाँसी रंग डारि रौ छो!"
        ],
        "english_translation": "My spirited brother-in-law is coming home, holding bags of colored powder in his hand, laughing and splashing spring colors!",
        "archive_source": "Kumaoni Holi Archive",
        "source_url": "https://www.kumaoniholiarchive.org/audio"
    },
    {
        "id": "KHL-0010",
        "title": "शोभा बरनी न जाय",
        "form": "Baithaki Holi",
        "raag": "Bhimpalasi",
        "theme": "Sublime aesthetic beauty of nature and devotion in spring",
        "verses": [
            "शोभा बरनी न जाय आज हिमालय म,",
            "बुराँश फुली गो डाना-काना म!",
            "देवता दर्शन करन आए,",
            "होली को रंग बरसि रौ!"
        ],
        "english_translation": "Indescribable is the splendour upon the Himalayas today, as rhododendrons burst into bloom across peaks and ridges!",
        "archive_source": "Kumaoni Holi Archive",
        "source_url": "https://www.kumaoniholiarchive.org/audio"
    },
    {
        "id": "KHL-0011",
        "title": "भाव भंजन गुण गाऊँ",
        "form": "Baithaki Holi / Devotional",
        "raag": "Yaman",
        "theme": "Philosophical opening hymn of Baithaki gathering",
        "verses": [
            "भाव भंजन गुण गाऊँ प्रभु तोरा,",
            "चरण कमल म शीश झुकाऊँ!",
            "होली को पावन पर्व आयो,",
            "सकल क्लेश मिटाई पाऊँ!"
        ],
        "english_translation": "I sing Thy praises, O destroyer of worldly sorrow, bowing my head at Thy lotus feet on this sacred festival of colors.",
        "archive_source": "Kumaoni Holi Archive",
        "source_url": "https://www.kumaoniholiarchive.org/audio"
    },
    {
        "id": "KHL-0012",
        "title": "सिद्धि को दाता, विघ्न विनाशन",
        "form": "Baithaki Holi (Ganesh Vandana)",
        "raag": "Kafi",
        "theme": "Classical ceremonial opening hymn invoking Lord Ganesha",
        "verses": [
            "सिद्धि को दाता, विघ्न विनाशन,",
            "प्रथम मनाऊँ गौरी पुत्र गजानन!",
            "रिद्धि-सिद्धि संग बिराजो आँगन,",
            "होली की बैठक सफल करो स्वामी!"
        ],
        "english_translation": "Bestower of wisdom and remover of obstacles, first I invoke Gauri's son Gajanana! Grace our courtyard with auspiciousness and bless our assembly.",
        "archive_source": "Kumaoni Holi Collection",
        "source_url": "https://www.ekumaon.com/2023/02/kumaoni-holi-song-pdf.html"
    },
    {
        "id": "KHL-0013",
        "title": "तुम सिद्धि करो महाराज",
        "form": "Baithaki Holi (Mangal Vandana)",
        "raag": "Khamaj",
        "theme": "Invocatory prayer to open musical gathering",
        "verses": [
            "तुम सिद्धि करो महाराज,",
            "होली की सभा म आन बिराजो!",
            "सुर-ताल म ज्ञान जगाओ,",
            "सब भक्तन के काज संवारो!"
        ],
        "english_translation": "Grant fulfillment, O Lord, take Thy seat in our Holi assembly and bless our musical melodies with divine grace!",
        "archive_source": "Kumaoni Holi Collection",
        "source_url": "https://www.ekumaon.com/2023/02/kumaoni-holi-song-pdf.html"
    },
    {
        "id": "KHL-0014",
        "title": "हाँ हाँ हाँ मोहन गिरधारी",
        "form": "Baithaki Holi",
        "raag": "Kafi",
        "theme": "Playful Gopi-Krishna complaint of torn veils and teasing",
        "verses": [
            "हाँ हाँ हाँ मोहन गिरधारी,",
            "ऐसो अनाड़ी चुनर गयो फाड़ी!",
            "ओ हँसी-हँसी दे गयो गारी, मोहन गिरधारी!",
            "चीर चुराय कदम चढ़ी बैठ्यो, लुकी-छिपि करत शुमारी!"
        ],
        "english_translation": "Yes, yes, Mohan Girdhari! Such a rogue who tore my veil, laughing playfully and perching upon the Kadamba tree!",
        "archive_source": "Kumaoni Holi Collection",
        "source_url": "https://www.ekumaon.com/2024/03/10-famous-holi-songs-of-kumaon-uttarakhand.html"
    },
    {
        "id": "KHL-0015",
        "title": "शिव के मन माहि बसे काशी",
        "form": "Baithaki Holi (Shaivite)",
        "raag": "Bhairavi",
        "theme": "Lord Shiva and sacred Kashi celebrated in Himalayan gathering",
        "verses": [
            "शिव के मन माहि बसे काशी,",
            "कैलाश पति डमरू बजावै!",
            "गौरा संग खेलत होरी भोले,",
            "अंग भभूत अबीर लगावै!"
        ],
        "english_translation": "Within Shiva's heart dwells sacred Kashi; the Lord of Kailash beats his damru and plays Holi with Gaura, rubbing holy ash and abeer!",
        "archive_source": "Kumaoni Holi Collection",
        "source_url": "https://www.ekumaon.com/2024/03/10-famous-holi-songs-of-kumaon-uttarakhand.html"
    },
    {
        "id": "KHL-0016",
        "title": "मथुरा में खेलें एक घड़ी",
        "form": "Baithaki Holi",
        "raag": "Khamaj",
        "theme": "Radha-Krishna Holi celebration with damru and red staff",
        "verses": [
            "मथुरा में खेलें एक घड़ी,",
            "काहे के हाथ में डमरु बिराजे, काहे के हाथ में लाल छड़ी!",
            "राधा के हाथ में डमरु बिराजे, कान्हा के हाथ में लाल छड़ी,",
            "मथुरा में खेलें एक घड़ी!"
        ],
        "english_translation": "Let them play for an hour in Mathura! In Radha's hand rests the damru, in Krishna's hand the scarlet rod as they celebrate Holi!",
        "archive_source": "Kumaoni Holi Collection",
        "source_url": "https://www.ekumaon.com/2024/03/10-famous-holi-songs-of-kumaon-uttarakhand.html"
    },
    {
        "id": "KHL-0017",
        "title": "कान्हा बजा गयो बाँसुरिया",
        "form": "Baithaki Holi",
        "raag": "Piloo",
        "theme": "The alluring flute melody stealing the hearts of village milkmaids",
        "verses": [
            "कान्हा बजा गयो बाँसुरिया,",
            "यमुना तट म रंग मचायो!",
            "सुर सुणि सुध-बुध बिसरी गई,",
            "होली म सब जग बौरायो!"
        ],
        "english_translation": "Kanha played upon his flute, stirring colors along the Yamuna bank; hearing his notes, all the world was captivated!",
        "archive_source": "Kumaoni Holi Collection",
        "source_url": "https://www.ekumaon.com/2024/03/10-famous-holi-songs-of-kumaon-uttarakhand.html"
    },
    {
        "id": "KHL-0018",
        "title": "राधे जमुना अकेली मत जाइयो",
        "form": "Baithaki Holi",
        "raag": "Desh",
        "theme": "Friendly warning to Radha against going alone during Holi",
        "verses": [
            "राधे जमुना अकेली मत जाइयो,",
            "कान्हा ठाढ़ो कदम तरिया!",
            "रंग म चूनर भिगोई देगो,",
            "पकड़ लेगो नाजुक बइयाँ!"
        ],
        "english_translation": "Radha, do not go alone to Yamuna's shore; Kanha waits beneath the Kadamba tree and will soak your veil in color!",
        "archive_source": "Kumaoni Holi Collection",
        "source_url": "https://www.ekumaon.com/2024/03/10-famous-holi-songs-of-kumaon-uttarakhand.html"
    },
    {
        "id": "KHL-0019",
        "title": "रंग में होली कैसे खेलूँ",
        "form": "Baithaki Holi (Viraha / Shringar)",
        "raag": "Bhairavi",
        "theme": "Pang of separation while playing colors without the beloved",
        "verses": [
            "रंग में होली कैसे खेलूँ री सखी,",
            "पिया बिन सूनी सेज हमारी!",
            "नैना बरसत सावन-भादों,",
            "अबीर गुलाल भयो बैरी!"
        ],
        "english_translation": "How can I play with colors, O companion, when my beloved is far away? Without him, even festive colors feel desolate.",
        "archive_source": "Kumaoni Holi Collection",
        "source_url": "https://www.ekumaon.com/2024/03/10-famous-holi-songs-of-kumaon-uttarakhand.html"
    },
    {
        "id": "KHL-0020",
        "title": "देवा के भवन बिराजे होरी",
        "form": "Baithaki / Khadi Holi (Temple Celebration)",
        "raag": "Kafi / Dhamar",
        "theme": "Grand culmination of Holi in village temples and shrines",
        "verses": [
            "देवा के भवन बिराजे होरी,",
            "चीर बँध्यो छै गाँव का थान म!",
            "ढोल-दमुवां की गूँज उठी छ,",
            "सब जन गावनि आशीष मगन!"
        ],
        "english_translation": "Holi resounds within the temple of the deities! The sacred cheer banner is tied at the village shrine to the beat of dhol-damau, as blessings flow to all.",
        "archive_source": "Kumaoni Holi Collection",
        "source_url": "https://www.ekumaon.com/2024/03/10-famous-holi-songs-of-kumaon-uttarakhand.html"
    }
]

with open(HOLI_FILE, 'w', encoding='utf-8') as f:
    json.dump(HOLI_DATA, f, ensure_ascii=False, indent=2)

print(f"Saved {len(HOLI_DATA)} Holi songs to {HOLI_FILE}")

# -------------------------------------------------------------
# 4. DIGITAL ARCHIVE SOURCES (SRC-001 to SRC-007)
# -------------------------------------------------------------
SOURCES_DATA = [
    {
        "id": "SRC-001",
        "source": "Kumauni Archives",
        "what_it_provides": "Books, articles, maps, audio recordings, manuscripts; primary preservation repository for Kumaoni heritage",
        "url": "https://kumauniarchives.com/",
        "preservation_status": "Active primary digital archive"
    },
    {
        "id": "SRC-002",
        "source": "Kumaoni Holi Archive",
        "what_it_provides": "Audio, video and image documentation of Kumaoni Baithaki, Khadi and Mahila Holi traditions",
        "url": "https://www.kumaoniholiarchive.org/",
        "preservation_status": "Cultural audio-visual archive"
    },
    {
        "id": "SRC-003",
        "source": "Kumauni.in E-Books",
        "what_it_provides": "Digitized Kumaoni books, poetry collections, classical literature and linguistic materials",
        "url": "https://www.kumauni.in/p/e-books-relating-to-kumauni-language.html",
        "preservation_status": "Digital literature repository"
    },
    {
        "id": "SRC-004",
        "source": "Uttarakhand Library Hub",
        "what_it_provides": "Out-of-copyright digitized books on Kumaon folklore, history, music, and Himalayan customs",
        "url": "https://uttarakhandhub.com/library",
        "preservation_status": "Public domain digital library"
    },
    {
        "id": "SRC-005",
        "source": "Open Library — Kumaoni Folk Songs",
        "what_it_provides": "Bibliographic discovery and catalogued volumes indexed under Kumaoni folk songs and oral traditions",
        "url": "https://openlibrary.org/subjects/kumaoni_folk_songs",
        "preservation_status": "Global bibliographic index"
    },
    {
        "id": "SRC-006",
        "source": "Google Books — Kumaun ke Lokgeet",
        "what_it_provides": "1996, 197-page selected Kumaoni folk-song anthology with Hindi translations and cultural annotations",
        "url": "https://books.google.com/books?id=-351AAAAIAAJ",
        "preservation_status": "Digitized scholarly compilation"
    },
    {
        "id": "SRC-007",
        "source": "Creative Uttarakhand Publications",
        "what_it_provides": "Regional-language preservation publications including Ghughuti Basuti and Nyauli Sankalan",
        "url": "https://creativeuttarakhand.aipan.org/initiatives/publications/",
        "preservation_status": "Living linguistic initiative"
    }
]

with open(SOURCES_FILE, 'w', encoding='utf-8') as f:
    json.dump(SOURCES_DATA, f, ensure_ascii=False, indent=2)

print(f"Saved {len(SOURCES_DATA)} sources to {SOURCES_FILE}")
