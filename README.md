# pyjokes website

The source of web content for the pyjokes website [pyjok.es](https://pyjok.es) which is
built using a static site generator called [beemo](https://github.com/bennuttall/beemo).

## Content

This repo contains content, static files and
[Chameleon](https://chameleon.readthedocs.io/en/latest/) templates for the pyjokes website.

## Build

Requires [beemo](https://github.com/bennuttall/beemo) with the `logs` extra installed.

```bash
make build          # generate JS and build the site
make logs           # process Apache logs into CSV
make analytics         # generate analytics report
make serve          # serve the site locally on port 8008
make serve-analytics   # serve the analytics report on port 8009
```

## Licences

The site content is copyright Pyjokes Society.

The HTML templates are from [HTML5 Up](https://html5up.net/).