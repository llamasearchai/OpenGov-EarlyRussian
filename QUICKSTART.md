# OpenGov-EarlyRussian Quick Start Guide

**Author:** Nik Jois <nikjois@llamasearch.ai>  
**Version:** 0.1.0

## Installation (5 minutes)

### Option 1: Using pip (Recommended)

```bash
# Clone or navigate to project directory
cd OpenGov-EarlyRussian

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install package
pip install -e .

# Verify installation
russian version
```

### Option 2: Using Docker

```bash
# Build and run
docker-compose up --build

# API will be available at http://localhost:8000
```

## First Steps (2 minutes)

### 1. Try the CLI

```bash
# Show help
russian --help

# Display alphabet
russian alphabet iotated

# Decline a noun
russian decline книга feminine

# Conjugate a verb
russian conjugate читать --tense present

# Transliterate text
russian translit "Mikhail Lomonosov"
```

### 2. Start the API Server

```bash
# Start server
uvicorn opengov_earlyrussian.api.main:app --reload

# Visit http://localhost:8000/docs for interactive API documentation
```

### 3. Use Python API

```python
from opengov_earlyrussian import (
    AlphabetTeacher,
    CasesTeacher,
    VerbConjugator,
    Transliterator,
)

# Alphabet
teacher = AlphabetTeacher()
print(teacher.get_row("iotated"))

# Cases
cases = CasesTeacher()
print(cases.decline_noun("книга", "feminine"))

# Verbs
verbs = VerbConjugator()
print(verbs.conjugate("читать", "present"))

# Transliteration
trans = Transliterator()
print(trans.to_russian("Mikhail Lomonosov"))
```

## Examples

### Run Example Scripts

```bash
# Basic usage examples
python examples/basic_usage.py

# Business Russian examples
python examples/business_culture.py

# Spaced repetition system
python examples/srs_example.py

# Run demo script
./demo.sh
```

### Test API Endpoints

```bash
# Start API server (in separate terminal)
uvicorn opengov_earlyrussian.api.main:app --reload

# Test endpoints
./test_api.sh
```

## Common Use Cases

### Learning Alphabet

```bash
# Show iotated vowels
russian alphabet iotated

# Show all vowels
russian alphabet vowels

# Show signs (Ъ, Ь)
russian alphabet signs
```

### Declining Nouns

```bash
# Feminine nouns
russian decline книга feminine
russian decline земля feminine

# Masculine nouns (inanimate)
russian decline паспорт masculine

# Masculine nouns (animate)
russian decline студент masculine --animate
```

### Conjugating Verbs

```bash
# Present tense
russian conjugate читать --tense present
russian conjugate говорить --tense present

# Past tense
russian conjugate читать --tense past
russian conjugate говорить --tense past
```

### Transliteration

```bash
# Names
russian translit "Mikhail Lomonosov"
russian translit "Fyodor Dostoevsky"

# Places
russian translit "Sankt-Peterburg"
russian translit "Moskva"

# Phrases
russian translit "Zdravstvuyte"
russian translit "Spasibo"
```

## API Usage

### Test with curl

```bash
# Health check
curl http://localhost:8000/health

# Decline noun
curl -X POST http://localhost:8000/decline \
  -H "Content-Type: application/json" \
  -d '{"noun":"книга","gender":"feminine"}'

# Conjugate verb
curl -X POST http://localhost:8000/conjugate \
  -H "Content-Type: application/json" \
  -d '{"verb":"читать","tense":"present"}'

# Transliterate
curl -X POST http://localhost:8000/transliterate \
  -H "Content-Type: application/json" \
  -d '{"text":"Mikhail Lomonosov"}'
```

### Interactive API Documentation

Visit http://localhost:8000/docs for Swagger UI with interactive API testing.

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=opengov_earlyrussian --cov-report=term-missing

# Run specific test file
pytest tests/test_alphabet.py
pytest tests/test_cases.py
```

## Configuration

Create a `.env` file for optional configuration:

```env
API_HOST=0.0.0.0
API_PORT=8000
OPENAI_API_KEY=sk-...  # Optional: for AI conversation features
LOG_LEVEL=INFO
```

## Troubleshooting

### Issue: Command not found

```bash
# Make sure virtual environment is activated
source .venv/bin/activate

# Verify installation
pip list | grep opengov-earlyrussian
```

### Issue: Port already in use

```bash
# Use different port
uvicorn opengov_earlyrussian.api.main:app --port 8001
```

### Issue: Tests failing

```bash
# Reinstall package
pip install -e .

# Run tests with verbose output
pytest -v
```

## Next Steps

1. **Explore Examples**: Check the `examples/` directory for more usage examples
2. **Read Documentation**: See README.md for comprehensive feature list
3. **API Reference**: Visit `/docs` endpoint for full API documentation
4. **Contribute**: Follow coding standards in .pre-commit-config.yaml

## Support

- Documentation: README.md, VERIFICATION.md
- Examples: examples/ directory
- Tests: tests/ directory
- API Docs: http://localhost:8000/docs (when server is running)

## Key Features

- **Alphabet**: Full Cyrillic with mnemonics
- **Cases**: 6-case declension with animacy support
- **Verbs**: Conjugation with aspect pairs
- **Transliteration**: Latin to Russian conversion
- **Business Russian**: Email and phone templates
- **Cultural Guide**: Holidays, regions, etiquette
- **SRS**: Spaced repetition for vocabulary
- **AI Chat**: OpenAI-powered conversation partner

**Happy learning!** 🇷🇺

