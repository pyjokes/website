build:
	python scripts/pyjokes_to_js.py
	BEEMO_CONFIG=config.yml beemo

serve:
	python -m http.server -d www 8008 &
