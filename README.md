# OpenGov-EarlyRussian

![CI](https://github.com/opengov/earlyrussian/actions/workflows/ci.yml/badge.svg)
![Coverage 100%](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Version](https://img.shields.io/badge/version-0.1.0-blue)

AI-powered Russian language learning platform featuring interactive lessons, Business Russian, cultural immersion, and personalized learning tools.

## Author

Nik Jois <nikjois@llamasearch.ai>

## Features

- Alphabet & Pronunciation:
  - Full Cyrillic alphabet with Ё, Й, Ъ (hard sign), Ь (soft sign), Ы
  - Iotated vowels: Я, Ю, Ё, Е; palatalization via Ь and front vowels
  - Stress and vowel reduction (аканье/иканье), final devoicing, assimilation
  - Hard/soft consonant pairs, "ши/жи" spelling rules

- Grammar Mastery:
  - 6 cases: именительный, родительный, дательный, винительный, творительный, предложный
  - Animacy in accusative (masc. animate → genitive forms)
  - Gender (m/f/n), basic declension patterns (-а/-я; consonant-stem; -о/-е)
  - Verbs: aspects (impf/perf), present, past, simple/compound future, imperative (intro)
  - Pronouns and politeness (Вы/ты)

- Conversational Practice:
  - AI conversation partner (OpenAI-backed, offline-safe fallback)
  - Real-life scenarios, cultural notes, formal vs. informal register

- Business Russian:
  - Email templates, phone phrases, meeting and negotiation language

- Cultural Context:
  - Regions, holidays, etiquette, contemporary culture

- Tools:
  - Transliteration Latin → Russian, SRS (spaced repetition), CLI utilities

## Quick Start

```bash
# Install uv (optional)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone & install
cd OpenGov-EarlyRussian
pip install -e ".[dev]"

# Or using uv
uv sync

# Create .env file
echo "OPENAI_API_KEY=sk-..." > .env

# Run tests
pytest

# Start API server
uvicorn opengov_earlyrussian.api.main:app --reload

# Use CLI
russian --help
```

## CLI Examples

```bash
# Display alphabet
russian alphabet iotated

# Decline a noun
russian decline книга feminine

# Conjugate a verb
russian conjugate читать present

# Transliterate text
russian translit "Mikhail Lomonosov"

# Show version
russian version
```

## API Examples

### Health Check
```bash
curl http://localhost:8000/health
```

### Decline a noun
```bash
curl -X POST http://localhost:8000/decline \
  -H "Content-Type: application/json" \
  -d '{"noun":"книга","gender":"feminine"}'
```

### Conjugate a verb
```bash
curl -X POST http://localhost:8000/conjugate \
  -H "Content-Type: application/json" \
  -d '{"verb":"читать","tense":"present"}'
```

### Transliterate text
```bash
curl -X POST http://localhost:8000/transliterate \
  -H "Content-Type: application/json" \
  -d '{"text":"Mikhail Lomonosov"}'
```

### AI Chat
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"utterance":"Здравствуйте!","level":"A1","formal":true}'
```

## Python API Examples

### Alphabet
```python
from opengov_earlyrussian import AlphabetTeacher
t = AlphabetTeacher()
print(t.get_row("iotated")["letters"])  # ['Я','Ю','Ё','Е']
print(t.mnemonic("Ё"))
```

### Cases (animacy-aware)
```python
from opengov_earlyrussian import CasesTeacher
c = CasesTeacher()
print(c.decline_noun("книга", gender="feminine"))["винительный"]  # книгу
print(c.decline_noun("паспорт", gender="masculine", animate=False)["винительный"])  # паспорт
print(c.decline_noun("студент", gender="masculine", animate=True)["винительный"])   # студента
```

### Verbs & aspect
```python
from opengov_earlyrussian import VerbConjugator
v = VerbConjugator()
print(v.aspect_pair("читать"))  # прочитать
prs = v.conjugate("читать", "present")
print(prs["forms"]["я"])  # читаю
past = v.conjugate("говорить", "past")
print(past["forms"]["я (м.)"])  # говорил
```

### Transliteration
```python
from opengov_earlyrussian import Transliterator
tr = Transliterator()
print(tr.to_russian("Mikhail Lomonosov"))  # Михаил Ломоносов
```

## Docker

```bash
# Build and run
docker-compose up --build

# Or manually
docker build -t opengov-earlyrussian .
docker run -p 8000:8000 -e OPENAI_API_KEY=sk-... opengov-earlyrussian
```

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests with coverage
pytest --cov=opengov_earlyrussian --cov-report=term-missing

# Format code
black opengov_earlyrussian tests

# Lint
ruff check opengov_earlyrussian tests

# Type check
mypy opengov_earlyrussian tests

# Run all checks
pytest && black --check opengov_earlyrussian tests && ruff check opengov_earlyrussian tests
```

## License

MIT License

Copyright (c) 2025 Nik Jois

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
