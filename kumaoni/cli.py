"""
Command-line interface (CLI) for the Kumaoni language library.
Usage:
    python -m kumaoni.cli translate "Hello, how are you?"
    python -m kumaoni.cli lookup "ईजा"
    python -m kumaoni.cli number 42
    python -m kumaoni.cli conjugate "जाण" --tense past
    python -m kumaoni.cli proverb
    python -m kumaoni.cli riddle
"""

import sys
import argparse
import json

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import kumaoni
from kumaoni.constants import Tense, Gender, GrammaticalNumber


def main():
    parser = argparse.ArgumentParser(
        prog="kumaoni",
        description="Kumaoni Language Standard Library CLI"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # translate
    trans_parser = subparsers.add_parser("translate", help="Translate text to Kumaoni")
    trans_parser.add_argument("text", type=str, help="Text to translate")
    trans_parser.add_argument("--source", "-s", default="auto", help="Source language (default: auto)")
    trans_parser.add_argument("--method", "-m", default="auto", choices=["auto", "rule_based", "pivot", "llm"])
    trans_parser.add_argument("--api-key", "-k", default=None, help="Optional Gemini/OpenAI API key")

    # lookup
    lookup_parser = subparsers.add_parser("lookup", help="Dictionary search")
    lookup_parser.add_argument("word", type=str, help="Word to look up")

    # number
    num_parser = subparsers.add_parser("number", help="Convert numbers to Kumaoni words")
    num_parser.add_argument("num", type=int, help="Integer to convert")
    num_parser.add_argument("--script", default="devanagari", choices=["devanagari", "latin"])

    # conjugate
    conj_parser = subparsers.add_parser("conjugate", help="Conjugate Kumaoni verbs")
    conj_parser.add_argument("verb", type=str, help="Infinitive verb (e.g., खाण, जाण)")
    conj_parser.add_argument("--tense", "-t", default="present", choices=["present", "past", "future", "present_continuous"])
    conj_parser.add_argument("--person", "-p", type=int, default=3, choices=[1, 2, 3])
    conj_parser.add_argument("--gender", "-g", default="m", choices=["m", "f"])

    # proverb
    subparsers.add_parser("proverb", help="Display a traditional Kumaoni proverb (Akhaan)")

    # riddle
    subparsers.add_parser("riddle", help="Display a traditional Kumaoni riddle (Aana)")

    # transliterate
    translit_parser = subparsers.add_parser("transliterate", help="Transliterate between Devanagari and Latin")
    translit_parser.add_argument("text", type=str, help="Text to transliterate")
    translit_parser.add_argument("--to", default="devanagari", choices=["devanagari", "latin"])

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "translate":
        res = kumaoni.translate(args.text, source=args.source, method=args.method, api_key=args.api_key)
        print(f"\n[Source ({res.source_lang})]: {res.source}")
        print(f"[Kumaoni]:        {res.text}")
        print(f"[Phonetic]:       {res.romanized}")
        print(f"[Method]:         {res.method} (confidence: {res.confidence:.2f})\n")

    elif args.command == "lookup":
        w = kumaoni.lookup(args.word)
        if w:
            print(f"\nKumaoni:     {w.kumaoni} ({w.roman})")
            print(f"English:     {w.english}")
            print(f"Hindi:       {w.hindi}")
            print(f"Part of Sp.: {w.pos} [{w.category}]\n")
        else:
            results = kumaoni.search(args.word)
            if results:
                print(f"\nFound {len(results)} matches:")
                for r in results:
                    print(f"- {r.kumaoni} ({r.roman}): {r.english} | {r.hindi}")
                print()
            else:
                print(f"\nNo dictionary match found for '{args.word}'.\n")

    elif args.command == "number":
        w = kumaoni.num_to_words(args.num, script=args.script)
        dev_num = kumaoni.to_devanagari_numerals(args.num)
        print(f"\nNumber:    {args.num} ({dev_num})")
        print(f"In words:  {w}\n")

    elif args.command == "conjugate":
        t = Tense(args.tense)
        g = Gender.MASCULINE if args.gender == "m" else Gender.FEMININE
        res = kumaoni.conjugate(args.verb, tense=t, person=args.person, gender=g)
        print(f"\nVerb:       {args.verb}")
        print(f"Tense:      {args.tense}")
        print(f"Conjugated: {res}\n")

    elif args.command == "proverb":
        p = kumaoni.proverbs.random()
        print(f"\nअखाण (Akhaan): {p.get('kumaoni')}")
        print(f"Phonetic:      {p.get('roman')}")
        print(f"Meaning:       {p.get('figurative_meaning')}")
        print(f"Hindi:         {p.get('hindi_equivalent')}")
        print(f"English:       {p.get('english_equivalent')}\n")

    elif args.command == "riddle":
        r = kumaoni.riddles.random()
        print(f"\nआणा (Aana):     {r.get('riddle')}")
        print(f"English:       {r.get('english_translation')}")
        print(f"Answer:        {r.get('answer_kumaoni')} ({r.get('answer_english')})\n")

    elif args.command == "transliterate":
        out = kumaoni.transliterate(args.text, to_script=args.to)
        print(f"\nInput:  {args.text}")
        print(f"Output: {out}\n")


if __name__ == "__main__":
    main()
