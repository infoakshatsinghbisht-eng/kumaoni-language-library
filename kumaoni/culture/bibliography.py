"""
Bibliography and Scholarly Corpus of the Kumaoni Language.

Provides comprehensive cataloguing of:
1. Works written IN Kumaoni (Early/Classical, Modern Poetry, Story Collections,
   Children's Literature, Religious/Translated texts).
2. Works on Kumaoni Grammar, Lexicography & Linguistics.
3. Scholarly and folkloric works ABOUT Kumaoni language, history, and literature.
"""

import json
import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class KumaoniBook:
    id: int
    title: str
    author: str
    year: str
    genre: str
    category: str  # "works_in_kumaoni", "grammar_and_linguistics", "works_about_kumaoni"
    category_label: str
    language_status: str
    evidence: str
    publisher: str
    pages: str
    isbn: str
    source_url: str
    confidence: str


_BIBLIOGRAPHY_CACHE: Optional[List[KumaoniBook]] = None


def _load_bibliography() -> List[KumaoniBook]:
    global _BIBLIOGRAPHY_CACHE
    if _BIBLIOGRAPHY_CACHE is not None:
        return _BIBLIOGRAPHY_CACHE

    json_path = os.path.join(os.path.dirname(__file__), 'data', 'bibliography.json')
    if not os.path.exists(json_path):
        _BIBLIOGRAPHY_CACHE = []
        return _BIBLIOGRAPHY_CACHE

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    books = []
    for d in data:
        books.append(
            KumaoniBook(
                id=d.get('id', 0),
                title=d.get('title', ''),
                author=d.get('author', ''),
                year=d.get('year', ''),
                genre=d.get('genre', ''),
                category=d.get('category', 'works_in_kumaoni'),
                category_label=d.get('category_label', ''),
                language_status=d.get('language_status', ''),
                evidence=d.get('evidence', ''),
                publisher=d.get('publisher', ''),
                pages=d.get('pages', ''),
                isbn=d.get('isbn', ''),
                source_url=d.get('source_url', ''),
                confidence=d.get('confidence', '')
            )
        )
    _BIBLIOGRAPHY_CACHE = books
    return _BIBLIOGRAPHY_CACHE


class BibliographyTreasury:
    """Interface to access the Master Kumaoni Bibliography."""

    @staticmethod
    def list_books(
        category: Optional[str] = None,
        author: Optional[str] = None,
        genre: Optional[str] = None,
        query: Optional[str] = None
    ) -> List[KumaoniBook]:
        """
        List catalogued books with optional filters.
        
        Args:
            category: "works_in_kumaoni", "grammar_and_linguistics", or "works_about_kumaoni"
            author: Substring to filter by author name
            genre: Substring to filter by genre
            query: Substring search across title, author, and genre
        """
        books = _load_bibliography()
        res = books
        if category:
            cat_lower = category.lower().strip()
            res = [b for b in res if b.category.lower() == cat_lower]
        if author:
            auth_lower = author.lower().strip()
            res = [b for b in res if auth_lower in b.author.lower()]
        if genre:
            genre_lower = genre.lower().strip()
            res = [b for b in res if genre_lower in b.genre.lower()]
        if query:
            q_lower = query.lower().strip()
            res = [
                b for b in res
                if q_lower in b.title.lower()
                or q_lower in b.author.lower()
                or q_lower in b.genre.lower()
                or q_lower in b.category_label.lower()
                or q_lower in b.publisher.lower()
            ]
        return res

    @staticmethod
    def get_book(book_id: int) -> Optional[KumaoniBook]:
        """Retrieve a specific catalogued book by ID."""
        for b in _load_bibliography():
            if b.id == book_id:
                return b
        return None

    @staticmethod
    def search(query: str) -> List[KumaoniBook]:
        """Search books by keyword across title, author, genre, or notes."""
        return BibliographyTreasury.list_books(query=query)

    @staticmethod
    def categories() -> Dict[str, str]:
        """Get available categories and their human-readable labels."""
        return {
            "works_in_kumaoni": "Works Written In Kumaoni (Literature & Texts)",
            "grammar_and_linguistics": "Kumaoni Grammar, Lexicography & Linguistics",
            "works_about_kumaoni": "Works About Kumaoni (Criticism, History & Folk Studies)"
        }

    @staticmethod
    def authors() -> List[str]:
        """Get unique list of authors in the bibliography."""
        seen = set()
        out = []
        for b in _load_bibliography():
            if b.author and b.author not in seen:
                seen.add(b.author)
                out.append(b.author)
        return sorted(out)

    @staticmethod
    def stats() -> Dict[str, Any]:
        """Summary statistics of catalogued literature."""
        books = _load_bibliography()
        from collections import Counter
        cat_counts = Counter(b.category for b in books)
        return {
            "total_books": len(books),
            "works_in_kumaoni": cat_counts.get("works_in_kumaoni", 0),
            "grammar_and_linguistics": cat_counts.get("grammar_and_linguistics", 0),
            "works_about_kumaoni": cat_counts.get("works_about_kumaoni", 0),
            "unique_authors": len(BibliographyTreasury.authors())
        }
