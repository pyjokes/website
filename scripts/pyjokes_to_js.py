from pathlib import Path

from pyjokes import get_jokes

JS_FILE = Path(__file__).parent.parent / "static" / "js" / "pyjokes.js"
TEMPLATE_JS_FILE = Path(__file__).parent / "pyjokes_js_template.js"

jokes = get_jokes()

template_js_code = TEMPLATE_JS_FILE.read_text()

jokes_array_str = ",\n    ".join(f'"{joke}"' for joke in jokes if '"' not in joke)

js_code = f"""const jokes = [
    {jokes_array_str}
]

{template_js_code}
"""

JS_FILE.write_text(js_code)
