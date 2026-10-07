"""
Kumaoni traditional festivals, historic fairs (melas), and cultural celebrations.
Covering 20 major celebrations of Kumaon's cultural and spiritual calendar.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, asdict


@dataclass
class Festival:
    name_kumaoni: str
    name_roman: str
    month: str
    description: str
    rituals: List[str]
    traditional_song_or_couplet: str


FESTIVALS_DATA: Dict[str, Festival] = {
    "harela": Festival(
        name_kumaoni="हरेला",
        name_roman="Harela",
        month="साउन (July - Kark Sankranti)",
        description="A major Himalayan agricultural festival marking the onset of the monsoon and the new crop season, dedicated to Lord Shiva and Goddess Parvati.",
        rituals=[
            "Sowing seeds of 5 to 9 different grains (wheat, barley, maize, mustard, etc.) in small bamboo or clay pots 9-10 days before the festival.",
            "Harvesting the vibrant green yellow shoots on the day of Harela.",
            "Elders blessing family members by placing green Harela stalks behind their ears with the auspicious blessing: 'जी रया, जागि रया, तीष्ट रया...'"
        ],
        traditional_song_or_couplet="जी रया, जागि रया, तीष्ट रया, पनपि रया। हिमाल म ह्युं छन तक, गंगा म पाणि छन तक।"
    ),
    "phool_dei": Festival(
        name_kumaoni="फूलदेई",
        name_roman="Phool Dei",
        month="चैत (March - Chaitra Sankranti)",
        description="The spring festival of flowers celebrating nature's blossom and the first day of the Hindu solar new year in the hills.",
        rituals=[
            "Young children (Phoolari) gather wild Himalayan spring flowers such as Pyoli (Reinwardtia), Buransh (Rhododendron), and mustard.",
            "Children go house-to-house placing flowers on every doorstep (dehari), singing traditional greetings.",
            "Householders bless the children and reward them with sweets, rice, jaggery (gur), and coins."
        ],
        traditional_song_or_couplet="फूल देई, छम्मा देई, दैणी द्वार, भर भकार। यो देली स बारम्बार नमस्कार!"
    ),
    "ghughutiya": Festival(
        name_kumaoni="घुघुतिया / उत्तरायणी मेला",
        name_roman="Ghughutiya / Uttarayani",
        month="माघ (January - Makar Sankranti)",
        description="Celebrated when the sun enters Capricorn (Uttarayana). Deeply tied to folk legends of King Kalyan Chand, minister Nirbhaya, and crows, as well as the historic Uttarayani fair of Bageshwar.",
        rituals=[
            "Deep-frying twisted, sweet dough cookies made of wheat flour and jaggery shaped like spotted doves (ghughute), knives, drums, and flowers.",
            "Threading the sweets into wearable necklaces (ghughut mala) with an orange in the center.",
            "Early morning calling of crows to eat the sweets from children's hands with playful folk chants.",
            "Historic Coolie-Begar movement registers thrown into Saryu confluence at Bageshwar on Uttarayani in 1921."
        ],
        traditional_song_or_couplet="काले कौवा काले, घुघुति माला खाले! ले कौवा भात, मकै दे सुनक थात।"
    ),
    "olgia": Festival(
        name_kumaoni="ओलगिया / घी संक्रांति",
        name_roman="Olgia / Ghee Sankranti",
        month="भादौ (August - Simha Sankranti)",
        description="Ancient thanksgiving festival celebrating the peak of crop growth, ripening of grain ears, and dairy abundance in the monsoon.",
        rituals=[
            "Artisans, farmers, and family members present traditional gifts (Olga) of fresh harvest, cucumbers, walnuts, and dairy to elders and patrons.",
            "Consuming large amounts of freshly churned homemade cow/buffalo ghee, curd, and stuffed urad-dal bedu roti to ward off sluggishness and strengthen health."
        ],
        traditional_song_or_couplet="घी संक्रातिक दिन घी जरूर खाण चाइन, नि खाए त अगिल जनम म गणेल बणि जालो।"
    ),
    "nanda_devi": Festival(
        name_kumaoni="नंदा देवी मेला",
        name_roman="Nanda Devi Mela",
        month="भादौ / आसोज (September - Shukla Ashtami)",
        description="Historic cultural fair held in Almora, Nainital, Ranikhet, Bageshwar, and Kot Bhramari honoring Goddess Nanda, the divine patron and daughter of Kumaon.",
        rituals=[
            "Creating sacred idols of Goddess Nanda and Sunanda using trunk sections of the Kadali (banana/plantain) tree.",
            "Grand traditional procession, Chholiya martial dance performances, Hurkiya singing, and sacred immersion.",
            "Animal sacrifice historically performed, now replaced by coconut offering."
        ],
        traditional_song_or_couplet="जय माँ नंदा, जय माँ सुनंदा, सुख-समृद्धि दै। हिया म दया, घर म शांति राख माँ!"
    ),
    "khatarwa": Festival(
        name_kumaoni="खतड़वा",
        name_roman="Khatarwa",
        month="आसोज (Mid-September - Kanya Sankranti)",
        description="Unique agrarian and pastoral bonfire festival celebrating the historic victory of Kumaon's general Khatad Singh / Chand army and welcoming the winter, with special protective rites for cattle.",
        rituals=[
            "Children gather dry bushes, twigs, and wood to construct a effigy-bonfire (Khatarwa) in the village commons.",
            "At twilight, lighting the fire and brandishing flaming torches (Bhelo) while singing rhythmic rhyming chants.",
            "Beating cattle pens with green branches and feeding domestic animals fresh grass, cucumber, and flour pancakes.",
            "Eating large mountain cucumbers mixed with hemp seeds and rock salt (kakadi-noon)."
        ],
        traditional_song_or_couplet="भैलो जी भैलो, खतड़वा को भैलो! खतड़वा पड़ि ग्यो खात म, गैया आ गई गोठ म!"
    ),
    "saatu_aathu": Festival(
        name_kumaoni="सातू-आठूँ (गौरा-महेश)",
        name_roman="Saatu-Aathu (Gaura-Mahesh)",
        month="भादौ (August-September - Saptami & Ashtami)",
        description="Deeply emotional women's folk festival celebrating the arrival of Gaura (Parvati) to her maternal home (Maita) and her reunion with Mahesh (Shiva). Predominant in Pithoragarh and Champawat.",
        rituals=[
            "On Saptami (Saatu), creating ceremonial effigies of Gaura and Mahesh using wild mountain grasses and fresh paddy stalks.",
            "Women observe strict fast, wear sacred seven-knot cotton cords (Dor/Dubda) on their necks.",
            "Dancing in circular rings singing ancient Gamra and Jhora ballads portraying domestic trials and mountain affection.",
            "On Ashtami (Aathu), grand ceremonial wedding and tearful farewell (Bidai) of Gaura to Kailash."
        ],
        traditional_song_or_couplet="गौरा रानी म्येता आई, हरिया दूब का सेज बनाई। गौरा-महेश की जोड़ी सोवै!"
    ),
    "bagwal": Festival(
        name_kumaoni="देवीधुरा की बगवाल (पाषाण युद्ध)",
        name_roman="Bagwal of Devidhura",
        month="साउन (August - Raksha Bandhan / Shravan Purnima)",
        description="Famous traditional stone-pelting ritual battle fought at the temple of Maa Barahi Devi in Devidhura (Champawat), dating back centuries.",
        rituals=[
            "Four warrior clans (Khams: Chamyal, Gaharwal, Lamgaria, and Valigya) enter the Kholi Khandan arena carrying large wicker shields (Chhatolis).",
            "Clans pelt stones at one another in a ritual mock battle until the temple priest (Pujari) blows the conch shell, signifying the offering of human blood to appease the goddess.",
            "Tended wounds are dressed with medicinal nettle and herbal pastes without malice."
        ],
        traditional_song_or_couplet="जय माँ बाराही देवीधुरा धाम, चारि खामों को प्रणाम!"
    ),
    "bikhoti": Festival(
        name_kumaoni="स्याल्दे बिखौती मेला (बिस्सू)",
        name_roman="Syalde Bikhoti",
        month="बैसाख (April - Baisakhi / Mesh Sankranti)",
        description="Historic martial fair held at Dwarahat (Almora) in the complex of ancient stone temples, celebrating the valor of the Katyuri era and spring harvest.",
        rituals=[
            "Cultural factions (Dall) representing different valleys arrive with brass trumpets (Ransingha), drums, and battle standards.",
            "Performing the martial Oda-bhent ritual, dancing with swords and shields.",
            "Singing Jhora and Chhapeli songs through the night at the Syalde Pokhar reservoir."
        ],
        traditional_song_or_couplet="बिखौती को मेलो लागो द्वाराहाट, ढोल-दमुवां बाजि रैन घाट-घाट!"
    ),
    "jageshwar_mela": Festival(
        name_kumaoni="जागेश्वर श्रावणी मेला",
        name_roman="Jageshwar Shravani Mela",
        month="साउन (July-August)",
        description="Month-long pilgrimage fair held at the 8th-12th century stone temple cluster of Jageshwar Dham (Dandeshwar-Mritunjaya), surrounded by dense deodar forests.",
        rituals=[
            "Devotees take holy dips in the Jataganga rivulet and perform Rudrabhishek.",
            "Childless couples observe the sacred night vigil holding earthen lamps (Deepdan) in their palms before Lord Jageshwar.",
            "Chholiya dancers and classical bards perform sacred jagars."
        ],
        traditional_song_or_couplet="हर-हर महादेव, नागेशं दारुकावने। जय जागेश्वर महाप्रभो!"
    ),
    "purnagiri_mela": Festival(
        name_kumaoni="पूर्णागिरी मेला",
        name_roman="Purnagiri Mela",
        month="चैत (March-April - Chaitra Navratri)",
        description="One of the largest pilgrimage congregations of North India, held on the summit ridge of Tanakpur (Champawat) where Sati's naval (Nabhi) fell.",
        rituals=[
            "Trekking the steep mountain trail from Thuligad and Tunyas to the mountain peak temple.",
            "Offering red flags, chunari, and silver bells to Goddess Purnagiri.",
            "Visiting the shrine of Bhairav Devta on return to complete the pilgrimage."
        ],
        traditional_song_or_couplet="जय माँ पूर्णागिरी, पर्वत वासिनी, संकट नाशिनी।"
    ),
    "kainchi_dham_mela": Festival(
        name_kumaoni="कैंची धाम मेला (15 जून)",
        name_roman="Kainchi Dham Mela",
        month="आषाढ़ (15 June Foundation Day)",
        description="Massive annual festival celebrating the consecration of the temple of Neem Karoli Baba and Lord Hanuman in the Kshipra valley near Bhowali/Nainital.",
        rituals=[
            "Over a hundred thousand pilgrims gather from all over the world.",
            "Distribution of the famous sacred Malpua prasad prepared in pure ghee.",
            "Continuous chanting of Hanuman Chalisa and bhajans."
        ],
        traditional_song_or_couplet="जय बाबा नीब करौरी, जय बजरंग बली महाराज!"
    ),
    "kumaoni_holi": Festival(
        name_kumaoni="कुमाऊँनी बैठकी एवं खड़ी होली",
        name_roman="Kumaoni Baithaki and Khadi Holi",
        month="पूस से फागुन (December to March)",
        description="One of the most refined musical traditions of the Himalayas, divided into Baithaki Holi (seated classical Hindustani riyaz) and Khadi Holi (rhythmic circular dance).",
        rituals=[
            "Starting from the first Sunday of Paush month, singers gather in living rooms for Baithaki Holi, singing classical ragas (Kafi, Khamaj, Bhairavi, Desh).",
            "Cheer Bandhan: Tying a sacred ceremonial mast of colored cloths to an oak or paiyan branch on Ekadashi.",
            "Khadi Holi: Villagers clad in traditional white churidars dance from courtyard to courtyard with jhanjh and hurka.",
            "Mahila Holi: Celebrated exclusively in female domestic circles with humorous and devotional verses."
        ],
        traditional_song_or_couplet="गोरी प्यारी लागे है तेरो झनकारो! राग काफी म गाओ सखी सब, रंग अबीर उड़ाय!"
    ),
    "hillyatra": Festival(
        name_kumaoni="हिलजात्रा (लखिया भूत)",
        name_roman="Hillyatra",
        month="भादौ (August-September)",
        description="Fascinating pastoral carnival and agricultural mystery play of the Sor Valley (Pithoragarh), rooted in the rice transplantation rituals of the Chand dynasty.",
        rituals=[
            "Performers wear masks depicting bullocks, farmers, deer, and mythological characters in the muddy fields.",
            "Grand dramatic appearance of Lakhia Bhoot (an incarnation of Mahadev's attendant Veerabhadra) wielding ropes and blessing the crowds.",
            "Chants praising agricultural fertility and protection from pestilence."
        ],
        traditional_song_or_couplet="लखिया भूत आयो रे, महादेव को गण! सब दुख दूर कर, धरती म अन्न उपजा!"
    ),
    "chaitol": Festival(
        name_kumaoni="चैतोल (देवल समेत यात्रा)",
        name_roman="Chaitol",
        month="चैत (March-April)",
        description="Sacred spring royal pilgrimage of the Sor Valley (Pithoragarh), where the deity Deval Samet walks in royal procession across 22 villages.",
        rituals=[
            "The divine sedan/palanquin (Doli) of Deval Samet is carried barefoot across mountain ridges.",
            "Villagers welcome the procession at their thresholds with flowers, roasted grain, and lighted lamps.",
            "Traditional bards recite the genealogies of local rulers."
        ],
        traditional_song_or_couplet="जय देवल समेत महाराज, बाईस गाँव की रक्षा करा!"
    ),
    "somnath_mela": Festival(
        name_kumaoni="सोमनाथ मेला, मासी",
        name_roman="Somnath Mela (Masi)",
        month="बैसाख (May)",
        description="Ancient commercial and cultural cattle-and-textile fair held on the banks of the Western Ramganga river at Masi (Almora).",
        rituals=[
            "Traditional trade of hill bullocks, ploughs, iron implements, and woven woolens (Thulma, Chutka).",
            "Ritual bathing in the Ramganga river and night-long Jhora singing competition.",
            "Nal Dhaul ceremony throwing walnuts into the river."
        ],
        traditional_song_or_couplet="मासी का सोमनाथ मेलो, रामगंगा का तीर म!"
    ),
    "chhipla_jaat": Festival(
        name_kumaoni="छिप्ला जात (छिप्ला केदार)",
        name_roman="Chhipla Jaat",
        month="भादौ (Once every 2-3 years, August-September)",
        description="The ultimate barefoot alpine pilgrimage of the borderland valleys of Dharchula and Pithoragarh, ascending to 14,000 ft at the sacred tarn of Chhipla Kedar.",
        rituals=[
            "Pilgrims walk over 100 kilometers barefoot across rugged cliffs, glacier beds, and rhododendron forests.",
            "Carrying sacred parasols (Chhatra) and conch shells while keeping vows of absolute silence on high ridges.",
            "Holy bath in the glacial lake Chhipla Kund to seek health, prosperity, and blessings for offspring."
        ],
        traditional_song_or_couplet="छिप्ला केदार बाबा की जय! हिमाल का शिखर म विराजित!"
    ),
    "bagnath_shivratri": Festival(
        name_kumaoni="बागनाथ शिवरात्रि मेला",
        name_roman="Bagnath Shivratri Mela",
        month="फागुन (February-March - Mahashivratri)",
        description="Spiritual fair held at the historic 1499 CE Bagnath Temple in Bageshwar, at the confluence of Saryu and Gomati rivers.",
        rituals=[
            "Devotees bathe in the sacred Saryu-Gomati Sangam at dawn.",
            "Offering bel-patra, wild flowers, and holy water to the self-manifested tiger-faced Shiva lingam.",
            "Night vigil with Akhand Kirtan and folk fairs."
        ],
        traditional_song_or_couplet="स्यू-गोमती का संगम म बाघनाथ महाकाल, जय भोले बाबा!"
    ),
    "kailpal_mela": Festival(
        name_kumaoni="कैलपाल मेला",
        name_roman="Kailpal Mela",
        month="कातिक (November)",
        description="Local village fair dedicated to Kailpal Devta, the territorial guardian deity who protects village boundaries and cattle herds.",
        rituals=[
            "Consecration of new iron tridents (Trishul) and bells at the ridge-top shrine.",
            "Villagers offer first milk from cows (Kheer) and freshly harvested grains.",
            "Shamanic jagar where the Dangariya gets possessed by the spirit of Kailpal."
        ],
        traditional_song_or_couplet="कैलपाल महाराज, सीम-सीमाना की रक्षा करा, गौ-बछिया कणी सुख दिया!"
    ),
    "nanda_raj_jaat": Festival(
        name_kumaoni="नंदा राजजात",
        name_roman="Nanda Raj Jaat",
        month="भादौ (Once every 12 years)",
        description="The grandest 280-kilometer Himalayan pilgrimage of Uttarakhand, bidding farewell to Goddess Nanda Devi from Nauti/Kurud to the high altitude snow lake of Homkund at 17,500 ft.",
        rituals=[
            "Led by the mysterious four-horned ram (Chausingha Khadu) carrying offerings on its back.",
            "The golden ringal parasol (Chantoli) of Goddess Nanda is accompanied by hundreds of thousands of pilgrims.",
            "Passing through Bedni Bugyal, Roopkund (Lake of Skeletons), and culminating at Homkund where the ram walks into the glaciers alone."
        ],
        traditional_song_or_couplet="नंदा देवी राजजात, सुवा बंक्या हिमाल म! ईजा नंदा म्येता बाटी ससुरे जाँछी!"
    ),
    "kandali_festival": Festival(
        name_kumaoni="कंडाली उत्सव (किर्जी उत्सव)",
        name_roman="Kandali Festival (Kirji)",
        month="आसोज (Once every 12 years, October)",
        description="Famous 12-yearly victory and flowering festival celebrated by the Rung / Shauka community in Chaundas Valley (Pithoragarh), commemorating both the blooming of the sacred Kandali shrub (Strobilanthes wallichii) and the historic defeat of General Zorawar Singh's invading army in 1841.",
        rituals=[
            "Women and men dress in traditional Rung attire (Byanthloo and Chugti).",
            "Women march in a triumphant procession armed with wooden pestles (Musals) and silver-mounted walking sticks (Chhyakuk) to uproot and destroy blooming Kandali bushes.",
            "Performance of traditional Chhyamo dances through village courtyards."
        ],
        traditional_song_or_couplet="कंडाली फूल खिलि ग्यो चौंदास म, रूँग महिलाएँ निकलीं विजय उत्सव म!"
    ),
    "jauljibi_mela": Festival(
        name_kumaoni="जौलजीबी मेला",
        name_roman="Jauljibi Mela",
        month="मंसिर (14-21 November)",
        description="Historic international trade, cultural, and trans-Himalayan mela held at the confluence of the sacred Kali and Gori rivers in Pithoragarh, where India, Nepal, and Tibet historically met.",
        rituals=[
            "Ceremonial holy dip at the confluence (Sangam) of Kali and Gori rivers.",
            "Display and trade of indigenous high-altitude Himalayan crafts: hand-knotted Dan carpets, Pashmina shawls, Thulma, Chutka, Jimbu, and Tibetan sheep.",
            "Cross-border cultural exchanges between Kumaoni, Rung, and Nepalese bards singing Jhora and Chhapeli."
        ],
        traditional_song_or_couplet="काली-गोरी का संगम म जौलजीबी को मेलो, हिमाल का ऊन-कालीन की बहार!"
    ),
    "thal_mela": Festival(
        name_kumaoni="थल मेला",
        name_roman="Thal Mela",
        month="बैसाख (April - Baisakhi)",
        description="Celebrated on the auspicious day of Baisakhi along the banks of the Eastern Ramganga river at Thal (Pithoragarh) near the ancient Baleshwar temple. Instituted in 1940 to honor the martyrs of Jallianwala Bagh.",
        rituals=[
            "Holy morning bath in the Eastern Ramganga river.",
            "Flag hoisting and patriotic remembrance of national and Himalayan martyrs.",
            "Vibrant performances of traditional Chholiya sword dances, Hurka beats, and folk songs in the bazaar."
        ],
        traditional_song_or_couplet="बैसाख को थल मेलो, रामगंगा का तीर म बाजि रैन हुड़को-दमुवां!"
    ),
    "gananath_mela": Festival(
        name_kumaoni="गणनाथ मेला",
        name_roman="Gananath Mela",
        month="कातिक (November - Kartik Purnima)",
        description="Ancient night-long pilgrimage fair held at the scenic cave temple of Lord Shiva at Gananath near Takula (Almora), famous for the miraculous 'Khada Diya' ritual.",
        rituals=[
            "Childless women stand erect the entire night holding burning earthen lamps (Khada Diya) in their open palms facing Lord Shiva's sanctum.",
            "Devotees sing night-long devotional Jagars and bhajans to keep the flame alive until dawn to receive the divine boon of offspring.",
            "Auspicious holy bathing at water spouts before dawn."
        ],
        traditional_song_or_couplet="गणनाथ बाबा का द्वार म ठाड़ो दीयो जलाया, मन की मुराद पूरी करा महादेव!"
    ),
    "chaiti_mela": Festival(
        name_kumaoni="चैती मेला (माँ बालसुंदरी)",
        name_roman="Chaiti Mela (Maa Balasundari)",
        month="चैत (March-April - Chaitra Navratri)",
        description="Massive historic Navratri congregation held at the ancient Chaiti Temple in Kashipur (Udhamsingh Nagar), honoring Maa Balasundari, tutelary deity of the Chand Rajas of Kumaon.",
        rituals=[
            "The sacred golden idol and Doli of Maa Balasundari are carried in a ceremonial nocturnal procession from the chief priest's residence to the historic shrine.",
            "Pilgrims offer coconuts, flags, sweets, and ceremonial yellow cloth.",
            "Large-scale rural trading fair of agricultural equipment, wooden crafts, and traditional utensils."
        ],
        traditional_song_or_couplet="जय माँ बालसुंदरी चैती वाली, कूर्मांचल की रक्षक, मनोकामना पूर्ण करणि!"
    ),
    "mostamanu_mela": Festival(
        name_kumaoni="मोस्टामानु मेला",
        name_roman="Mostamanu Mela",
        month="भादौ (August-September - Krishna Ashtami)",
        description="A vibrant rain-gratitude fair held at the Mostamanu temple atop the Chandak hills overlooking the Sor Valley of Pithoragarh, dedicated to Mosta Devta, the Himalayan rain and cloud god.",
        rituals=[
            "Villagers carry the divine palanquin (Doli) of Mosta Devta to the hill summit temple.",
            "Farmers offer the fresh harvest of maize, cucumber, and milk to thank the god for timely monsoon rain.",
            "Grand community circular Jhora folk singing with women wearing Rangwali Pichhauda."
        ],
        traditional_song_or_couplet="मोस्टा महाराज बादल बरसाओ, खेत-खलिहान म हरियाली ल्याओ!"
    ),
    "bhitauli": Festival(
        name_kumaoni="भिटौली (चेत की भिटौली)",
        name_roman="Bhitauli",
        month="चैत (March-April)",
        description="The most touching and emotional social-familial tradition of Kumaon, wherein parents and brothers travel across mountains to visit married daughters and sisters living in distant villages.",
        rituals=[
            "Mothers and brothers prepare special homemade delicacies: sweet fried flour cakes (Rots), Puris, Arsa, and hill sweets.",
            "Brothers carry the auspicious gift hamper (Bhitauli) along with new clothes and blessings to their sister's in-laws' home.",
            "Immortalized in the poignant cry of the 'Ghuguti' and 'Nyoli' birds singing: 'भै भूखो, मैं भिटौली!'"
        ],
        traditional_song_or_couplet="ओ नरण घुघुती ना बासा, चैत की भिटौली याद आ गई! ईजा-बाबू को प्यार आयो!"
    ),
    "janopunyu": Festival(
        name_kumaoni="जनोपून्यु (रक्षाबंधन / ऋषितर्पण)",
        name_roman="Janopunyu (Rishitarpan)",
        month="साउन (August - Shravan Purnima)",
        description="Kumaoni celebration of Shravan Purnima, marked by the solemn ritual renewal of the sacred thread (Yajnopavita / Janeu) and universal kinship bonding.",
        rituals=[
            "Men gather at village riverbanks or sacred Naulas for early morning Vedic ablutions, Panchagavya purification, and Saptarishi Tarpan.",
            "Priests tie the auspicious protective thread (Raksha Sutra) to householders chanting: 'येन बद्धो बली राजा...'",
            "Families feast on festive stuffed Urad-dal puris (Bedu Roti) and Kheer."
        ],
        traditional_song_or_couplet="साउन मास की पून्यू आई, जनऊ बदल्यो, बहिनि कणी रक्षा को वचन दियो!"
    ),
    "vat_savitri": Festival(
        name_kumaoni="बट सावित्री",
        name_roman="Vat Savitri",
        month="जेठ (May-June - Jyeshtha Amavasya)",
        description="A deeply revered observance where married Kumaoni women fast and worship the sacred Banyan tree (Vat Vriksha) for the long life, health, and prosperity of their husbands.",
        rituals=[
            "Women dress in auspicious traditional attire and Rangwali Pichhauda.",
            "Circumambulating the Banyan tree 108 times while wrapping raw white cotton thread around its trunk.",
            "Reciting the legendary ballad of faithful Savitri defeating Yama to reclaim Prince Satyavan's soul.",
            "Sharing sprouted soaked pulses and seasonal hill fruits."
        ],
        traditional_song_or_couplet="बट वृक्ष कणी धागा लपेटी, सती सावित्री का पाँव पूजी, अमर सुहाग को वरदान माँगो!"
    ),
    "basant_panchami": Festival(
        name_kumaoni="बसंत पंचमी (श्रीपंचमी)",
        name_roman="Basant Panchami",
        month="माघ (January-February - Shukla Panchami)",
        description="Marks the auspicious advent of spring (Rituraj Basant) and the official beginning of public courtyard Holi songs across Kumaon.",
        rituals=[
            "Wearing auspicious yellow garments and applying bright yellow turmeric tilak (Pithya).",
            "Offering green shoots of newly sprouted barley (Jau) and yellow mustard blossoms to family deities and books.",
            "Baithaki Holi gatherings move outdoors into temple courtyards singing spring-themed Dhrupad and Dhamar ragas."
        ],
        traditional_song_or_couplet="आयो बसंत सखी, बन-बन महक्यौ बुराँश! पीला बस्तर पहिरी गाओ मंगल गान!"
    ),
    "kot_bhramari_mela": Festival(
        name_kumaoni="कोट भ्रामरी मेला (कोट की माई)",
        name_roman="Kot Bhramari Mela",
        month="भादौ / चैत (Nanda Ashtami & Navratri)",
        description="Historic festival held at Kot Bhramari Temple (Ranchula Kot) atop the Katyur valley in Garur/Baijnath, sacred seat of the sovereign tutelary goddess of the ancient Katyuri kings.",
        rituals=[
            "Ceremonial worship of the golden and stone idols of Goddess Kot Bhramari.",
            "Villagers from all Katyur hamlets arrive with silver umbrellas and floral offerings.",
            "Performance of traditional Katyuri bards reciting the royal saga of King Sukhaldev and Asanti-Basanti."
        ],
        traditional_song_or_couplet="जय माँ कोट भ्रामरी, कत्यूर घाटी की महारानी, रणचुलाहाट म रक्षा करा!"
    ),
    "chitai_golu_mela": Festival(
        name_kumaoni="चितई गोलू मेला",
        name_roman="Chitai Golu Mela",
        month="चैत एवं अश्विन (Navratri celebrations)",
        description="Annual gathering of justice-seekers, pilgrims, and thankful devotees at the world-famous Chitai Golu Devta Temple near Almora.",
        rituals=[
            "Devotees whose court cases, domestic disputes, or illness prayers have been resolved bring brass bells weighing from 1 kg to over 100 kg to hang on temple walls.",
            "Offering handwritten formal petitions on legal stamp paper to the deity's court.",
            "Hereditary jagariya singers recite the legendary life of Goril Devta."
        ],
        traditional_song_or_couplet="चितई का गोलू महाराज, घंटी बाजी टन-टन! न्याय की अदालत म सब की पुकार सुणी!"
    ),
    "ganga_dussehra": Festival(
        name_kumaoni="गंगा दशहरा (द्वार-पत्र / द्वाश)",
        name_roman="Ganga Dussehra",
        month="जेठ (June - Jyeshtha Shukla Dashami)",
        description="Commemorating the descent of Goddess Ganga to Earth, observed with the distinctive Kumaoni architectural folk art ritual of pasting sanctified 'Dwar-Patra' on household entrances.",
        rituals=[
            "Priests hand-craft sacred illustrated paper seals (Dwar-Patra / Dwash) adorned with geometric lotus yantras and protection shlokas.",
            "Pasting the Dwar-Patra on the main wooden door lintel (Dehari) using wheat flour paste to shield the home from lightning, snakes, and malevolent forces.",
            "Taking purifying ritual baths in mountain rivulets and springs."
        ],
        traditional_song_or_couplet="अगस्त्यश्च पुलस्त्यश्च वैशम्पायन एव च... गंगा दशहरा म द्वार-पत्र लगायो, सब विघ्न टल्यो!"
    ),
    "kumaoni_diwali_bhelo": Festival(
        name_kumaoni="कुमाऊँनी दीपावली एवं भैलो",
        name_roman="Kumaoni Diwali and Bhelo",
        month="कातिक (October-November - Kartik Amavasya & Pratipada)",
        description="The Himalayan celebration of lights, enriched with pastoral cattle worship and the thrilling mountain sport of twirling flaming resinous pine-wood torches (Bhelo).",
        rituals=[
            "Drawing intricate Aipan art with red clay (Geru) and rice paste (Biswar) from the courtyard threshold to the altar.",
            "Lighting pine torches (Bhelo) made of dry resinous Cheed wood (Chhilla) and swinging them in glowing fiery circles while singing folk couplets.",
            "Govardhan and cattle blessing: feeding cows seasoned rice flour loaves and garlanding bullocks."
        ],
        traditional_song_or_couplet="भैलो जी भैलो, दिवाली को भैलो! गोठ म गैया सुखी, घर म लक्ष्मी को वास!"
    ),
    "dronagiri_mela": Festival(
        name_kumaoni="द्रोणागिरी (दूनागिरी) मेला",
        name_roman="Dronagiri (Dunagiri) Mela",
        month="चैत एवं आसोज (Navratri)",
        description="Celebrated at the sacred Vaishnavi Shaktipeeth of Dunagiri atop the dense pine-clad peak near Dwarahat, revered since the Treta Yuga.",
        rituals=[
            "Climbing the flight of 500 stone stairs through cedar and oak woods to the mountain ridge.",
            "Offering brass bells, red flags, and dry coconuts to Goddess Dunagiri.",
            "Pilgrims invoke the divine mother for health and inner spiritual peace."
        ],
        traditional_song_or_couplet="दूनागिरी की भगवती माता, पर्वत शिखर विराजित! संकट काटो महारानी!"
    ),
    "devidhura_ashtami": Festival(
        name_kumaoni="देवीधुरा दुर्गाष्टमी मेला",
        name_roman="Devidhura Durgashtami Mela",
        month="आसोज (October - Ashwin Shukla Ashtami)",
        description="Autumn spiritual fair held at Maa Barahi Temple in Devidhura (Champawat), complementing the summer stone-pelting Bagwal.",
        rituals=[
            "Elaborate Vedic Chandi Path and Havans inside the sanctum formed by monumental megalithic split rocks.",
            "Sacred night Jagars invoking the guardian deities of Kali Kumaon.",
            "Blessing of children and families with Barahi's holy vermilion."
        ],
        traditional_song_or_couplet="जय माँ बाराही, देवीधुरा वासिनी! दुर्गम पर्वत म रक्षा करा माँ!"
    ),
    "ghantakarna_mela": Festival(
        name_kumaoni="घंटाकर्ण मेला",
        name_roman="Ghantakarna Mela",
        month="जेठ / आषाढ़ (June)",
        description="Village festival dedicated to Ghantakarna (Ghar Kurna), the fierce yet compassionate attendant of Lord Shiva and guardian against epidemic diseases.",
        rituals=[
            "Erecting high timber flagpoles with green pine boughs outside village gates.",
            "Ringing of large bronze bells (Ghanta) to purify the valley from epidemics and evil influences.",
            "Offerings of roasted barley flour and fried cakes."
        ],
        traditional_song_or_couplet="जय घंटाकर्ण महाबली, घंटी की गूंज म सब रोग दूर भगा!"
    ),
    "malushahi_mela": Festival(
        name_kumaoni="मालूशाही मेला, बैजनाथ",
        name_roman="Malushahi Mela (Baijnath)",
        month="बैसाख (May)",
        description="Cultural and musical fair at historic Baijnath on the banks of Gomati, celebrating the eternal love epic of King Malushahi of Katyur and Rajula of Johar.",
        rituals=[
            "Gathering of hereditary Hurkiya balladeers reciting the multiday Pauwada of Rajula-Malushahi.",
            "Performances of traditional Jhora and Chhapeli duets.",
            "Communal feasts commemorating Katyuri cultural heritage."
        ],
        traditional_song_or_couplet="बैजनाथ का संगम म मालूशाही गाईजै, अमर प्रेम की अमर कहानी!"
    ),
    "berinag_nagpanchami": Festival(
        name_kumaoni="बेरीनाग नागपंचमी मेला",
        name_roman="Berinag Nag Panchami Mela",
        month="साउन (July-August - Shukla Panchami)",
        description="Traditional serpent veneration fair at the ancient wooded temple of Berinag in Pithoragarh, headquarters of the historic Kumaoni serpent shrines.",
        rituals=[
            "Offering fresh cow's milk and unboiled rice in hollow stone cups at the Naga idols.",
            "Drawing serpent motifs with rice paste on home lintels for snakebite protection.",
            "Prayers to Dhaulinag, Kalinag, Feninag, and Pinglenag for underground aquifer vitality."
        ],
        traditional_song_or_couplet="जय नागराज बेरीनाग वासी, पाणि का नौला हरा-भरा राखो महाराज!"
    ),
    "rung_kirji": Festival(
        name_kumaoni="रंग किर्जी एवं गबला पूजा",
        name_roman="Rung Kirji & Gabla Puja",
        month="कातिक (November - Pre-winter migration)",
        description="Traditional borderland thanksgiving festival of the Rung/Shauka trans-Himalayan communities before their winter descent to the lower valleys.",
        rituals=[
            "Propitiation of Gabla Devta, the supreme lord of trans-Himalayan fortune and alpine trade.",
            "Community feast of high-altitude buckwheat and barley bread with yak butter tea.",
            "Solemn prayers for safe passage through snowy Himalayan passes."
        ],
        traditional_song_or_couplet="गबला बाबा हिमाल का स्वामी, व्यापार म बरकत दिया, बफिला बाटो म रक्षा करा!"
    )
}


def get_festival(name: str) -> Optional[Festival]:
    """Retrieve festival information by key (e.g., 'harela', 'khatarwa', 'bagwal', 'kandali_festival')."""
    key = name.lower().replace("-", "_").replace(" ", "_")
    if key in FESTIVALS_DATA:
        return FESTIVALS_DATA[key]
    for k, f in FESTIVALS_DATA.items():
        if key in k or key in f.name_roman.lower() or name in f.name_kumaoni:
            return f
    return None


def list_festivals() -> List[Dict]:
    """List all 40 major traditional Kumaoni festivals and melas."""
    return [asdict(f) for f in FESTIVALS_DATA.values()]


def search_festivals(query: str) -> List[Festival]:
    """Search festivals by name, month, description, or rituals."""
    q = query.lower().strip()
    return [
        f for f in FESTIVALS_DATA.values()
        if q in f.name_kumaoni
        or q in f.name_roman.lower()
        or q in f.month.lower()
        or q in f.description.lower()
        or any(q in r.lower() for r in f.rituals)
    ]

