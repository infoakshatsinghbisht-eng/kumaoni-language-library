"""
Lightweight, zero-dependency Developer Playground and REST API server for Kumaoni.
Uses Python's built-in http.server.
"""

import sys
import json
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

import kumaoni
from kumaoni.constants import Tense, Gender
from kumaoni.voice import KumaoniVoiceSynthesizer, voice_translate

STATIC_DIR = Path(__file__).parent / "static"


class KumaoniApiHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)

        if path == "/api/lookup":
            q = params.get("q", [""])[0]
            w = kumaoni.lookup(q)
            res = w.to_dict() if w else None
            matches = [x.to_dict() for x in kumaoni.search(q, limit=5)] if not res else []
            self._send_json({"result": res, "matches": matches})
            return

        elif path == "/api/conjugate":
            verb = params.get("verb", ["खाण"])[0]
            tense_str = params.get("tense", ["present"])[0]
            person = int(params.get("person", [3])[0])
            gender_str = params.get("gender", ["m"])[0]
            
            try:
                t = Tense(tense_str)
            except ValueError:
                t = Tense.PRESENT
            g = Gender.MASCULINE if gender_str == "m" else Gender.FEMININE
            
            conj = kumaoni.conjugate(verb, tense=t, person=person, gender=g)
            self._send_json({
                "verb": verb,
                "tense": tense_str,
                "person": person,
                "gender": gender_str,
                "result": conj
            })
            return

        elif path == "/api/number":
            n_str = params.get("n", ["1"])[0]
            try:
                n = int(n_str)
            except ValueError:
                n = 0
            dev_words = kumaoni.num_to_words(n, script="devanagari")
            rom_words = kumaoni.num_to_words(n, script="latin")
            dev_num = kumaoni.to_devanagari_numerals(n)
            ord_word = kumaoni.ordinal(n)
            self._send_json({
                "number": n,
                "devanagari_words": dev_words,
                "romanized_words": rom_words,
                "devanagari_numerals": dev_num,
                "ordinal": ord_word
            })
            return

        elif path == "/api/proverb/random":
            p = kumaoni.proverbs.random()
            self._send_json({"proverb": p})
            return

        elif path == "/api/riddle/random":
            r = kumaoni.riddles.random()
            self._send_json({"riddle": r})
            return

        elif path == "/api/festivals":
            fests = kumaoni.festivals.list()
            self._send_json({"festivals": fests})
            return

        elif path == "/api/voice/phrases":
            cat = params.get("category", ["all"])[0]
            phrases = kumaoni.voice.phrases(category=cat)
            self._send_json({"phrases": phrases})
            return

        elif path == "/api/voice/wav":
            dur = float(params.get("duration", ["0.8"])[0])
            freq = float(params.get("freq", ["440.0"])[0])
            wav_data = KumaoniVoiceSynthesizer.generate_pcm_wav(duration_seconds=dur, freq=freq)
            self.send_response(200)
            self.send_header("Content-Type", "audio/wav")
            self.send_header("Content-Length", str(len(wav_data)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(wav_data)
            return

        # Serve static HTML/JS/CSS
        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8") if content_length > 0 else "{}"
        try:
            data = json.loads(body)
        except Exception:
            data = {}

        if parsed.path == "/api/translate":
            text = data.get("text", "")
            source = data.get("source", "auto")
            method = data.get("method", "auto")
            api_key = data.get("apiKey") or None

            res = kumaoni.translate(text, source=source, method=method, api_key=api_key)
            self._send_json({
                "source_text": res.source,
                "source_lang": res.source_lang,
                "translated_text": res.text,
                "romanized": res.romanized,
                "method": res.method,
                "confidence": res.confidence
            })
            return

        elif parsed.path == "/api/voice/translate":
            text = data.get("text", "")
            source = data.get("source", "auto")
            method = data.get("method", "auto")
            generate_audio = bool(data.get("generate_audio", False))
            api_key = data.get("apiKey") or None

            res = voice_translate(
                text=text,
                source_lang=source,
                method=method,
                generate_audio=generate_audio,
                api_key=api_key
            )
            self._send_json(res.to_dict())
            return

        super().do_POST()

    def _send_json(self, data: dict):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)


def run_server(port: int = 8080):
    server_address = ("", port)
    httpd = HTTPServer(server_address, KumaoniApiHandler)
    print(f"Kumaoni Language Playground running at http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    run_server(port)
