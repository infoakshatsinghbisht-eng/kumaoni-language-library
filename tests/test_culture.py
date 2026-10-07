import unittest
import kumaoni


class TestCulture(unittest.TestCase):
    def test_festivals(self):
        harela = kumaoni.festivals.get("harela")
        self.assertIsNotNone(harela)
        self.assertEqual(harela.name_kumaoni, "हरेला")
        self.assertTrue(len(harela.rituals) > 0)

        all_fests = kumaoni.festivals.list()
        self.assertEqual(len(all_fests), 40)

        khatarwa = kumaoni.festivals.get("khatarwa")
        self.assertIsNotNone(khatarwa)
        self.assertEqual(khatarwa.name_kumaoni, "खतड़वा")

        bagwal = kumaoni.festivals.get("bagwal")
        self.assertIsNotNone(bagwal)
        self.assertIn("बगवाल", bagwal.name_kumaoni)

        saatu = kumaoni.festivals.get("saatu_aathu")
        self.assertIsNotNone(saatu)
        self.assertIn("सातू-आठूँ", saatu.name_kumaoni)

        hillyatra = kumaoni.festivals.get("hillyatra")
        self.assertIsNotNone(hillyatra)
        self.assertIn("हिलजात्रा", hillyatra.name_kumaoni)

        # Newly expanded festivals
        kandali = kumaoni.festivals.get("kandali_festival")
        self.assertIsNotNone(kandali)
        self.assertIn("कंडाली", kandali.name_kumaoni)

        mosta_mela = kumaoni.festivals.get("mostamanu_mela")
        self.assertIsNotNone(mosta_mela)
        self.assertIn("मोस्टामानु", mosta_mela.name_kumaoni)

        bhitauli = kumaoni.festivals.get("bhitauli")
        self.assertIsNotNone(bhitauli)
        self.assertIn("भिटौली", bhitauli.name_kumaoni)

        # Festival search
        search_pithoragarh = kumaoni.festivals.search("Pithoragarh")
        self.assertGreaterEqual(len(search_pithoragarh), 5)

        search_mela = kumaoni.festivals.search("मेला")
        self.assertGreaterEqual(len(search_mela), 10)

    def test_deities(self):
        """Test the local deities module (40 supreme Kumaoni deities)."""
        deities = kumaoni.deities.list()
        self.assertEqual(len(deities), 40)

        # Golu Devta (God of Justice)
        golu = kumaoni.deities.get("golu_devta")
        self.assertIsNotNone(golu)
        self.assertIn("गोलू", golu.name_kumaoni)
        self.assertEqual(golu.category, "Nyaya Devta")
        self.assertTrue(any("चितई" in s for s in golu.primary_shrines))

        # Nanda Devi
        nanda = kumaoni.deities.get("nanda_devi")
        self.assertIsNotNone(nanda)
        self.assertIn("नंदा", nanda.name_kumaoni)

        # Lakhia Bhoot
        lakhia = kumaoni.deities.get("lakhia_bhoot")
        self.assertIsNotNone(lakhia)
        self.assertIn("लखिया", lakhia.name_kumaoni)

        # Kalbisht of Binsar
        kalbisht = kumaoni.deities.get("kalbisht")
        self.assertIsNotNone(kalbisht)
        self.assertTrue(any("बिनसर" in s for s in kalbisht.primary_shrines))

        # Newly expanded deities
        bhumia = kumaoni.deities.get("bhumia_devta")
        self.assertIsNotNone(bhumia)
        self.assertIn("भूमिया", bhumia.name_kumaoni)

        mosta = kumaoni.deities.get("mosta_devta")
        self.assertIsNotNone(mosta)
        self.assertIn("मोस्टा", mosta.name_kumaoni)

        jiya = kumaoni.deities.get("jiya_rani")
        self.assertIsNotNone(jiya)
        self.assertIn("जिया रानी", jiya.name_kumaoni)

        saim = kumaoni.deities.get("saim_devta")
        self.assertIsNotNone(saim)
        self.assertIn("सैम", saim.name_kumaoni)

        naina = kumaoni.deities.get("naina_devi")
        self.assertIsNotNone(naina)
        self.assertIn("नैना", naina.name_kumaoni)

        gabla = kumaoni.deities.get("gabla_devta")
        self.assertIsNotNone(gabla)
        self.assertIn("गबला", gabla.name_kumaoni)

        # Search
        justice_gods = kumaoni.deities.search("न्याय")
        self.assertGreaterEqual(len(justice_gods), 2)

        # Stats
        stats = kumaoni.deities.stats()
        self.assertEqual(stats["total_deities"], 40)
        self.assertGreaterEqual(len(stats["categories"]), 5)

    def test_places(self):
        """Test the sacred geography and temples module (47 places across Kumaon)."""
        places = kumaoni.places.list()
        self.assertEqual(len(places), 47)

        # Jageshwar Dham
        jageshwar = kumaoni.places.get("jageshwar_dham")
        self.assertIsNotNone(jageshwar)
        self.assertIn("जागेश्वर", jageshwar.name_kumaoni)
        self.assertEqual(jageshwar.district, "Almora")
        self.assertEqual(jageshwar.category, "Temple & Sacred Dham")

        # Patal Bhuvaneshwar
        patal = kumaoni.places.get("patal_bhuvaneshwar")
        self.assertIsNotNone(patal)
        self.assertIn("पाताल", patal.name_kumaoni)

        # Nanda Devi Peak
        nanda = kumaoni.places.get("nanda_devi_peak")
        self.assertIsNotNone(nanda)
        self.assertEqual(nanda.category, "Alpine Peak & Glacier")

        # Saryu River & Bageshwar Sangam
        saryu = kumaoni.places.get("saryu_river")
        self.assertIsNotNone(saryu)
        self.assertEqual(saryu.category, "River & Confluence")

        # Filter by category and district
        temples = kumaoni.places.list(category="Temple")
        self.assertGreaterEqual(len(temples), 20)

        pithoragarh_places = kumaoni.places.list(district="Pithoragarh")
        self.assertGreaterEqual(len(pithoragarh_places), 10)

        # Search
        shiva_places = kumaoni.places.search("Shiva")
        self.assertGreaterEqual(len(shiva_places), 5)

        stats = kumaoni.places.stats()
        self.assertEqual(stats["total_places"], 47)
        self.assertGreaterEqual(len(stats["districts"]), 6)

    def test_surnames(self):
        """Test Kumaoni surnames, lineages, and social concepts module."""
        surnames = kumaoni.surnames.list()
        self.assertEqual(len(surnames), 33)

        # Pant
        pant = kumaoni.surnames.get("pant")
        self.assertIsNotNone(pant)
        self.assertEqual(pant.community, "Brahmin")
        self.assertTrue(any("शांडिल्य" in g for g in pant.gotras))

        # Bisht
        bisht = kumaoni.surnames.get("bisht")
        self.assertIsNotNone(bisht)
        self.assertEqual(bisht.community, "Kshatriya / Rajput")

        # Pangtey (Shauka)
        pangtey = kumaoni.surnames.get("pangtey")
        self.assertIsNotNone(pangtey)
        self.assertEqual(pangtey.community, "Shauka / Alpine Bhotia")

        # Tamta (Shilpkar / Artisan)
        tamta = kumaoni.surnames.get("tamta")
        self.assertIsNotNone(tamta)
        self.assertEqual(tamta.community, "Shilpkar / Artisan")

        # Community filtering
        brahmins = kumaoni.surnames.list(community="Brahmin")
        self.assertGreaterEqual(len(brahmins), 10)

        rajputs = kumaoni.surnames.list(community="Kshatriya")
        self.assertGreaterEqual(len(rajputs), 15)

        # Social concepts (Thaat, Thaatwaan, Dhadha, Gauntyaar)
        concepts = kumaoni.surnames.social_concepts()
        self.assertIn("that", concepts)
        self.assertIn("thatwan", concepts)
        self.assertIn("dhada", concepts)
        self.assertIn("gauntyar", concepts)

        stats = kumaoni.surnames.stats()
        self.assertEqual(stats["total_surnames"], 33)
        self.assertEqual(len(stats["communities"]), 4)

    def test_flora(self):
        """Test Kumaoni ethnobotanical flora and sacred trees module."""
        plants = kumaoni.flora.list()
        self.assertGreaterEqual(len(plants), 40)

        # Banjh (Oak)
        banjh = kumaoni.flora.get("banjh")
        self.assertIsNotNone(banjh)
        self.assertIn("बाँझ", banjh.name_kumaoni)
        self.assertEqual(banjh.scientific_name, "Quercus leucotrichophora")

        # Buransh (Rhododendron)
        buransh = kumaoni.flora.get("buransh")
        self.assertIsNotNone(buransh)
        self.assertIn("बुराँश", buransh.name_kumaoni)
        self.assertEqual(buransh.scientific_name, "Rhododendron arboreum")

        # Brahmakamal (Alpine lotus)
        brahmakamal = kumaoni.flora.get("brahmakamal")
        self.assertIsNotNone(brahmakamal)
        self.assertIn("ब्रह्मकमल", brahmakamal.name_kumaoni)

        # Deodar & Panya
        deodar = kumaoni.flora.get("deodar")
        self.assertIsNotNone(deodar)
        panya = kumaoni.flora.get("panya")
        self.assertIsNotNone(panya)

        # Category filter
        sacred_trees = kumaoni.flora.list(category="Sacred & Ritual Tree")
        self.assertGreaterEqual(len(sacred_trees), 5)

        # Search
        oak_search = kumaoni.flora.search("Oak")
        self.assertGreaterEqual(len(oak_search), 1)

        stats = kumaoni.flora.stats()
        self.assertGreaterEqual(stats["total_plants"], 40)
        self.assertGreaterEqual(len(stats["categories"]), 5)

    def test_rituals(self):
        """Test Kumaoni temple implements, vessels, and ritual objects module."""
        items = kumaoni.rituals.list()
        self.assertGreaterEqual(len(items), 40)

        # Pithyan (Sacred tilak)
        pithyan = kumaoni.rituals.get("pithyan")
        self.assertIsNotNone(pithyan)
        self.assertIn("पिथ्याँ", pithyan.name_kumaoni)
        self.assertEqual(pithyan.category, "Sacred Mark & Thread")

        # Rot (Sweet wheat offering)
        rot = kumaoni.rituals.get("rot")
        self.assertIsNotNone(rot)
        self.assertIn("रोट", rot.name_kumaoni)
        self.assertIn("Bhumia Devta", rot.associated_deities_or_shrines)

        # Ghant (Temple bells of Chitai)
        ghant = kumaoni.rituals.get("ghant")
        self.assertIsNotNone(ghant)
        self.assertIn("Chitai Golu Devta", ghant.associated_deities_or_shrines)

        # Hawankund & Samidha
        hawankund = kumaoni.rituals.get("hawankund")
        self.assertIsNotNone(hawankund)
        samidha = kumaoni.rituals.get("samidha")
        self.assertIsNotNone(samidha)

        # Jagar implements: Hurka, Kansi ki Thali
        hurka = kumaoni.rituals.get("hurka")
        self.assertIsNotNone(hurka)
        kansi = kumaoni.rituals.get("kansi_thali")
        self.assertIsNotNone(kansi)

        # Category filter
        vessels = kumaoni.rituals.list(category="Vessel")
        self.assertGreaterEqual(len(vessels), 5)

        # Search
        justice_search = kumaoni.rituals.search("Chitai")
        self.assertGreaterEqual(len(justice_search), 2)

        stats = kumaoni.rituals.stats()
        self.assertGreaterEqual(stats["total_ritual_items"], 40)
        self.assertGreaterEqual(len(stats["categories"]), 5)

    def test_calendar_and_seasons(self):
        months = kumaoni.get_months()
        self.assertEqual(len(months), 12)
        self.assertEqual(months[0]["kumaoni"], "चैत")

        seasons = kumaoni.get_seasons()
        self.assertIn("grishma", seasons)
        self.assertEqual(seasons["grishma"]["name_kmy"], "रूड़ि")

    def test_proverbs_and_riddles(self):
        proverb = kumaoni.proverbs.random()
        self.assertIn("kumaoni", proverb)
        self.assertIn("figurative_meaning", proverb)
        all_proverbs = kumaoni.proverbs.all()
        self.assertGreaterEqual(len(all_proverbs), 10)

        riddle = kumaoni.riddles.random()
        self.assertIn("riddle", riddle)
        self.assertIn("answer_kumaoni", riddle)
        all_riddles = kumaoni.riddles.all()
        self.assertGreaterEqual(len(all_riddles), 8)

    def test_literature(self):
        epics = kumaoni.literature.epics()
        self.assertGreaterEqual(len(epics), 6)
        
        malu = kumaoni.literature.get_epic("malushahi")
        self.assertIsNotNone(malu)
        self.assertIn("राजुला", malu.title_kumaoni)

        jiya = kumaoni.literature.get_epic("jiya_rani")
        self.assertIsNotNone(jiya)
        self.assertIn("जिया राँणि", jiya.title_kumaoni)

        haru = kumaoni.literature.get_epic("haru_singh_heet")
        self.assertIsNotNone(haru)
        self.assertIn("हीत", haru.title_kumaoni)

        authors = kumaoni.literature.authors()
        self.assertGreaterEqual(len(authors), 10)
        
        gumani = kumaoni.literature.get_author("gumani_pant")
        self.assertIsNotNone(gumani)
        self.assertIn("गुमानी", gumani.name_kumaoni)

        kp = kumaoni.literature.get_author("krishna_pandey")
        self.assertIsNotNone(kp)
        self.assertIn("कृष्ण", kp.name_kumaoni)
        self.assertIn("Kalyug Varnan", kp.famous_works)

        upreti = kumaoni.literature.get_author("ganga_datt_upreti")
        self.assertIsNotNone(upreti)
        self.assertIn("उप्रेती", upreti.name_kumaoni)

        tp = kumaoni.literature.get_author("trilochan_pandey")
        self.assertIsNotNone(tp)
        self.assertIn("त्रिलोचन", tp.name_kumaoni)

        bdp = kumaoni.literature.get_author("badri_datt_pande")
        self.assertIsNotNone(bdp)
        self.assertIn("बद्री दत्त", bdp.name_kumaoni)
        self.assertIn("Kumaun ka Itihas (1937)", bdp.famous_works)

        gj = kumaoni.literature.get_author("gunanand_juyal")
        self.assertIsNotNone(gj)
        self.assertIn("गुणानन्द", gj.name_kumaoni)

        girda = kumaoni.literature.get_author("girda")
        self.assertIsNotNone(girda)
        self.assertIn("गिर्दा", girda.name_kumaoni)

        rana = kumaoni.literature.get_author("heera_singh_rana")
        self.assertIsNotNone(rana)
        self.assertIn("हीरा सिंह", rana.name_kumaoni)

        # Test new poems
        poems = kumaoni.literature.poems()
        self.assertGreaterEqual(len(poems), 6)
        kalyug_poem = next((p for p in poems if p.id == "kalyug_varnan"), None)
        self.assertIsNotNone(kalyug_poem)
        self.assertIn("कलयुग", kalyug_poem.title_kumaoni)

        ghughuti = next((p for p in poems if p.id == "ghughuti_basuti"), None)
        self.assertIsNotNone(ghughuti)
        self.assertIn("घुघूती", ghughuti.title_kumaoni)

        kafal_pako = next((p for p in poems if p.id == "kafal_pako_geet"), None)
        self.assertIsNotNone(kafal_pako)
        self.assertIn("काफल पाको", kafal_pako.title_kumaoni)

        # Test newly integrated epics
        kalu = kumaoni.literature.get_epic("kalu_bhandari")
        self.assertIsNotNone(kalu)
        self.assertIn("कालू भण्डारी", kalu.title_kumaoni)

        ganga = kumaoni.literature.get_epic("ganganath")
        self.assertIsNotNone(ganga)
        self.assertIn("गंगनाथ", ganga.title_kumaoni)

        # Test newly integrated authors
        gairola = kumaoni.literature.get_author("tara_dutt_gairola")
        self.assertIsNotNone(gairola)
        self.assertIn("गैरोला", gairola.name_kumaoni)

        oakley = kumaoni.literature.get_author("e_s_oakley")
        self.assertIsNotNone(oakley)
        self.assertIn("ओकले", oakley.name_kumaoni)

        hem = kumaoni.literature.get_author("hem_pant")
        self.assertIsNotNone(hem)
        self.assertIn("हेम पंत", hem.name_kumaoni)

        # Canonical modern authors: Puran Chandra Kandpal & Sher Singh Bisht
        kandpal = kumaoni.literature.get_author("puran_chandra_kandpal")
        self.assertIsNotNone(kandpal)
        self.assertIn("पूरन चन्द्र कांडपाल", kandpal.name_kumaoni)
        self.assertIn("Kumauni Bhashak Byakaran", kandpal.famous_works)

        anpadh = kumaoni.literature.get_author("sher_singh_bisht")
        self.assertIsNotNone(anpadh)
        self.assertIn("शेर सिंह बिष्ट", anpadh.name_kumaoni)
        self.assertIn("Didi-Bainni", anpadh.famous_works)

    def test_master_bibliography(self):
        """Test master bibliography treasury and query methods."""
        # Stats
        stats = kumaoni.bibliography.stats()
        self.assertGreaterEqual(stats["total_books"], 100)
        self.assertGreaterEqual(stats["works_in_kumaoni"], 80)
        self.assertGreaterEqual(stats["works_about_kumaoni"], 5)
        self.assertGreaterEqual(stats["grammar_and_linguistics"], 3)

        # Categories
        cats = kumaoni.bibliography.categories()
        self.assertIn("works_in_kumaoni", cats)
        self.assertIn("grammar_and_linguistics", cats)
        self.assertIn("works_about_kumaoni", cats)

        # List all
        all_books = kumaoni.bibliography.list()
        self.assertGreaterEqual(len(all_books), 100)

        # Filter by category
        kumaoni_works = kumaoni.bibliography.list(category="works_in_kumaoni")
        self.assertGreaterEqual(len(kumaoni_works), 80)
        for b in kumaoni_works:
            self.assertEqual(b.category, "works_in_kumaoni")

        grammar_works = kumaoni.bibliography.list(category="grammar_and_linguistics")
        self.assertGreaterEqual(len(grammar_works), 3)

        about_works = kumaoni.bibliography.list(category="works_about_kumaoni")
        self.assertGreaterEqual(len(about_works), 5)

        # Filter by author
        kandpal_books = kumaoni.bibliography.list(author="पूरन चन्द्र कांडपाल")
        self.assertGreaterEqual(len(kandpal_books), 8)

        # Search
        results = kumaoni.bibliography.search("ब्याकरण")
        self.assertGreaterEqual(len(results), 1)

        # Access via literature facade
        lit_books = kumaoni.literature.books(category="grammar_and_linguistics")
        self.assertEqual(len(lit_books), len(grammar_works))

        # Get specific book
        b1 = kumaoni.bibliography.get(1)
        self.assertIsNotNone(b1)
        self.assertEqual(b1.id, 1)

    def test_folklore_corpus(self):
        """Test folklore, folk songs, Holi music, and digital archive sources."""
        # Stats
        stats = kumaoni.folklore.stats()
        self.assertEqual(stats["total_folk_songs"], 20)
        self.assertEqual(stats["total_holi_songs"], 20)
        self.assertEqual(stats["total_digital_sources"], 7)

        # Folk Songs
        songs = kumaoni.folklore.songs()
        self.assertEqual(len(songs), 20)

        # Retrieve specific song
        bedu = kumaoni.folklore.song("KSN-0001")
        self.assertIsNotNone(bedu)
        self.assertIn("पाको", bedu.title)
        self.assertEqual(bedu.roman, "Bedu Pako Baro Masa")
        self.assertTrue(len(bedu.verses) > 0)
        self.assertTrue(len(bedu.english_translation) > 0)

        # Filter by artist (Gopal Babu Goswami)
        gbg_songs = kumaoni.folklore.songs(artist="Gopal Babu Goswami")
        self.assertGreaterEqual(len(gbg_songs), 4)

        # Random song
        rnd = kumaoni.folklore.random_song()
        self.assertIsNotNone(rnd)
        self.assertTrue(rnd.id.startswith("KSN-"))

        # Holi Songs
        holi = kumaoni.folklore.holi_songs()
        self.assertEqual(len(holi), 20)

        # Specific Holi song
        h1 = kumaoni.folklore.holi_song("KHL-0001")
        self.assertIsNotNone(h1)
        self.assertIn("Holi", h1.form)
        self.assertEqual(h1.raag, "Khamaj")
        self.assertTrue(len(h1.verses) > 0)

        # Filter by form
        baithaki_holi = kumaoni.folklore.holi_songs(form="Baithaki")
        self.assertGreaterEqual(len(baithaki_holi), 15)
        for bh in baithaki_holi:
            self.assertIn("Baithaki", bh.form)

        khadi_holi = kumaoni.folklore.holi_songs(form="Khadi")
        self.assertGreaterEqual(len(khadi_holi), 3)

        # Random Holi song
        rnd_h = kumaoni.folklore.random_holi_song()
        self.assertIsNotNone(rnd_h)
        self.assertTrue(rnd_h.id.startswith("KHL-"))

        # Digital archive sources
        sources = kumaoni.folklore.sources()
        self.assertEqual(len(sources), 7)
        s1 = kumaoni.folklore.get_source("SRC-001")
        self.assertIsNotNone(s1)
        self.assertIn("Kumauni Archives", s1.source)

        # Literature facade cross-access
        lit_songs = kumaoni.literature.songs()
        self.assertEqual(len(lit_songs), 20)
        lit_holi = kumaoni.literature.holi_songs()
        self.assertEqual(len(lit_holi), 20)


if __name__ == "__main__":
    unittest.main()




