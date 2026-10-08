"""
Simple language translator.

Install:
    pip install deep-translator

Usage:
    python translator.py                       # interactive mode
    python translator.py "Hello world" -t hi   # one-off translation
    python translator.py "Bonjour" -s fr -t en # specify source language
    python translator.py --list                # show supported languages
"""

import argparse
import sys

from deep_translator import GoogleTranslator


def translate(text: str, target: str = "en", source: str = "auto") -> str:
    """Translate text into the target language."""
    return GoogleTranslator(source=source, target=target).translate(text)


def list_languages() -> None:
    langs = GoogleTranslator().get_supported_languages(as_dict=True)
    for name, code in sorted(langs.items()):
        print(f"{code:8} {name}")


def interactive() -> None:
    print("Language Translator (type 'quit' to exit, 'list' to see languages)")
    source = input("Source language code (press Enter for auto-detect): ").strip() or "auto"
    target = input("Target language code (e.g. hi, fr, es, de, ja): ").strip() or "en"

    while True:
        text = input("\nText> ").strip()
        if text.lower() in {"quit", "exit", "q"}:
            break
        if text.lower() == "list":
            list_languages()
            continue
        if not text:
            continue
        try:
            print("Translation:", translate(text, target, source))
        except Exception as e:
            print(f"Error: {e}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Translate text between languages.")
    parser.add_argument("text", nargs="?", help="Text to translate")
    parser.add_argument("-s", "--source", default="auto", help="Source language code (default: auto)")
    parser.add_argument("-t", "--target", default="en", help="Target language code (default: en)")
    parser.add_argument("--list", action="store_true", help="List supported languages")
    args = parser.parse_args()

    if args.list:
        list_languages()
    elif args.text:
        try:
            print(translate(args.text, args.target, args.source))
        except Exception as e:
            sys.exit(f"Error: {e}")
    else:
        interactive()


if __name__ == "__main__":
    main()
