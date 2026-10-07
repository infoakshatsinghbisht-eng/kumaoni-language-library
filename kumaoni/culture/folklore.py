"""
Folklore, Traditional Songs, and Musical Heritage of Kumaon.

Includes:
1. Traditional Folk & Recorded Songs Corpus (KSN-0001 to KSN-0020).
2. Kumaoni Holi Corpus (KHL-0001 to KHL-0020) spanning Baithaki, Khadi, and Mahila Holi.
3. Digital Archive Sources (SRC-001 to SRC-007) for heritage preservation.
"""

import json
import os
import random
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field


@dataclass
class KumaoniSong:
    id: str
    title: str
    roman: str
    artist: str
    genre: str
    corpus: str
    theme: str
    lyrics_sample: str
    verses: List[str]
    english_translation: str
    cultural_context: str
    source_url: str


@dataclass
class KumaoniHoliSong:
    id: str
    title: str
    form: str  # "Baithaki Holi", "Khadi Holi", "Mahila Holi"
    raag: str
    theme: str
    verses: List[str]
    english_translation: str
    archive_source: str
    source_url: str


@dataclass
class DigitalArchiveSource:
    id: str
    source: str
    what_it_provides: str
    url: str
    preservation_status: str


_SONGS_CACHE: Optional[List[KumaoniSong]] = None
_HOLI_CACHE: Optional[List[KumaoniHoliSong]] = None
_SOURCES_CACHE: Optional[List[DigitalArchiveSource]] = None


def _load_songs() -> List[KumaoniSong]:
    global _SONGS_CACHE
    if _SONGS_CACHE is not None:
        return _SONGS_CACHE

    path = os.path.join(os.path.dirname(__file__), 'data', 'songs.json')
    if not os.path.exists(path):
        _SONGS_CACHE = []
        return _SONGS_CACHE

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    songs = []
    for d in data:
        songs.append(
            KumaoniSong(
                id=d.get('id', ''),
                title=d.get('title', ''),
                roman=d.get('roman', ''),
                artist=d.get('artist', ''),
                genre=d.get('genre', ''),
                corpus=d.get('corpus', ''),
                theme=d.get('theme', ''),
                lyrics_sample=d.get('lyrics_sample', ''),
                verses=d.get('verses', []),
                english_translation=d.get('english_translation', ''),
                cultural_context=d.get('cultural_context', ''),
                source_url=d.get('source_url', '')
            )
        )
    _SONGS_CACHE = songs
    return _SONGS_CACHE


def _load_holi_songs() -> List[KumaoniHoliSong]:
    global _HOLI_CACHE
    if _HOLI_CACHE is not None:
        return _HOLI_CACHE

    path = os.path.join(os.path.dirname(__file__), 'data', 'holi_songs.json')
    if not os.path.exists(path):
        _HOLI_CACHE = []
        return _HOLI_CACHE

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    holi_songs = []
    for d in data:
        holi_songs.append(
            KumaoniHoliSong(
                id=d.get('id', ''),
                title=d.get('title', ''),
                form=d.get('form', ''),
                raag=d.get('raag', ''),
                theme=d.get('theme', ''),
                verses=d.get('verses', []),
                english_translation=d.get('english_translation', ''),
                archive_source=d.get('archive_source', ''),
                source_url=d.get('source_url', '')
            )
        )
    _HOLI_CACHE = holi_songs
    return _HOLI_CACHE


def _load_sources() -> List[DigitalArchiveSource]:
    global _SOURCES_CACHE
    if _SOURCES_CACHE is not None:
        return _SOURCES_CACHE

    path = os.path.join(os.path.dirname(__file__), 'data', 'digital_sources.json')
    if not os.path.exists(path):
        _SOURCES_CACHE = []
        return _SOURCES_CACHE

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    sources = []
    for d in data:
        sources.append(
            DigitalArchiveSource(
                id=d.get('id', ''),
                source=d.get('source', ''),
                what_it_provides=d.get('what_it_provides', ''),
                url=d.get('url', ''),
                preservation_status=d.get('preservation_status', '')
            )
        )
    _SOURCES_CACHE = sources
    return _SOURCES_CACHE


class FolkloreTreasury:
    """Interface to access Kumaoni folk songs, Holi music, and digital archives."""

    @staticmethod
    def list_songs(
        genre: Optional[str] = None,
        artist: Optional[str] = None,
        corpus: Optional[str] = None,
        query: Optional[str] = None
    ) -> List[KumaoniSong]:
        """List catalogued songs with optional filtering."""
        songs = _load_songs()
        res = songs
        if genre:
            g_low = genre.lower().strip()
            res = [s for s in res if g_low in s.genre.lower()]
        if artist:
            a_low = artist.lower().strip()
            res = [s for s in res if a_low in s.artist.lower()]
        if corpus:
            c_low = corpus.lower().strip()
            res = [s for s in res if c_low in s.corpus.lower()]
        if query:
            q_low = query.lower().strip()
            res = [
                s for s in res
                if q_low in s.title.lower()
                or q_low in s.roman.lower()
                or q_low in s.artist.lower()
                or q_low in s.theme.lower()
                or any(q_low in v.lower() for v in s.verses)
            ]
        return res

    @staticmethod
    def get_song(song_id: str) -> Optional[KumaoniSong]:
        """Retrieve a song by its unique identifier (e.g. 'KSN-0001')."""
        id_clean = song_id.upper().strip()
        for s in _load_songs():
            if s.id.upper() == id_clean or id_clean in s.title:
                return s
        return None

    @staticmethod
    def random_song() -> Optional[KumaoniSong]:
        """Return a random catalogued folk song."""
        songs = _load_songs()
        return random.choice(songs) if songs else None

    @staticmethod
    def list_holi_songs(
        form: Optional[str] = None,
        raag: Optional[str] = None,
        query: Optional[str] = None
    ) -> List[KumaoniHoliSong]:
        """List catalogued Kumaoni Holi songs with optional filtering."""
        holi = _load_holi_songs()
        res = holi
        if form:
            f_low = form.lower().strip()
            res = [h for h in res if f_low in h.form.lower()]
        if raag:
            r_low = raag.lower().strip()
            res = [h for h in res if r_low in h.raag.lower()]
        if query:
            q_low = query.lower().strip()
            res = [
                h for h in res
                if q_low in h.title.lower()
                or q_low in h.form.lower()
                or q_low in h.raag.lower()
                or q_low in h.theme.lower()
                or any(q_low in v.lower() for v in h.verses)
            ]
        return res

    @staticmethod
    def get_holi_song(song_id: str) -> Optional[KumaoniHoliSong]:
        """Retrieve a Holi song by ID (e.g. 'KHL-0001') or title."""
        id_clean = song_id.upper().strip()
        for h in _load_holi_songs():
            if h.id.upper() == id_clean or id_clean in h.title:
                return h
        return None

    @staticmethod
    def random_holi_song() -> Optional[KumaoniHoliSong]:
        """Return a random catalogued Holi song."""
        holi = _load_holi_songs()
        return random.choice(holi) if holi else None

    @staticmethod
    def list_sources() -> List[DigitalArchiveSource]:
        """List active digital heritage and archival repositories."""
        return _load_sources()

    @staticmethod
    def get_source(source_id: str) -> Optional[DigitalArchiveSource]:
        """Retrieve digital source by ID (e.g. 'SRC-001')."""
        id_clean = source_id.upper().strip()
        for src in _load_sources():
            if src.id.upper() == id_clean or id_clean in src.source.lower():
                return src
        return None

    @staticmethod
    def stats() -> Dict[str, Any]:
        """Summary metrics of Kumaoni digital folklore corpus."""
        songs = _load_songs()
        holi = _load_holi_songs()
        sources = _load_sources()
        from collections import Counter
        form_counts = Counter(h.form for h in holi)
        genre_counts = Counter(s.genre for s in songs)
        return {
            "total_folk_songs": len(songs),
            "total_holi_songs": len(holi),
            "total_digital_sources": len(sources),
            "holi_forms": dict(form_counts),
            "song_genres": dict(genre_counts)
        }
