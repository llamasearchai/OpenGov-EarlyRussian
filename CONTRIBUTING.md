# Contributing to OpenGov-EarlyRussian

Thank you for your interest in contributing to OpenGov-EarlyRussian!

## Getting Started

### Prerequisites
- Python 3.9 or higher
- Git
- Virtual environment tool (venv, virtualenv, or conda)

### Development Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/yourusername/earlyrussian.git
   cd earlyrussian
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install development dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Install pre-commit hooks:**
   ```bash
   pre-commit install
   ```

## Development Workflow

### Running Tests

```bash
# Run all tests
make test

# Run tests with coverage
make test-cov

# Run specific test file
pytest tests/test_alphabet.py -v
```

### Code Quality

```bash
# Format code
make format

# Run linter
make lint

# Run type checker
make type

# Run all checks
make all
```

### Making Changes

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write code following PEP 8 style guidelines
   - Add type hints to all functions
   - Add docstrings to public APIs
   - No emojis in code
   - No placeholders or TODOs without implementation

3. **Add tests:**
   - Write unit tests for new functionality
   - Write integration tests for multi-module features
   - Ensure all tests pass

4. **Run validation:**
   ```bash
   ./validate.sh
   ```

5. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Add: descriptive commit message"
   ```

## Code Standards

### Python Style
- Follow PEP 8
- Use black for formatting (line length: 100)
- Use ruff for linting
- Use mypy for type checking
- Add type hints to all functions
- Add docstrings to all public APIs

### Commit Messages
Format: `Type: Brief description`

Types:
- `Add:` New feature
- `Fix:` Bug fix
- `Update:` Modify existing feature
- `Remove:` Remove feature
- `Docs:` Documentation changes
- `Test:` Add or modify tests
- `Refactor:` Code refactoring

Examples:
- `Add: support for adjective declension`
- `Fix: transliteration of soft consonants`
- `Update: improve SRS algorithm efficiency`
- `Docs: add examples for verb conjugation`

### Testing
- Write tests for all new functionality
- Maintain or improve code coverage
- Test edge cases and error conditions
- Use descriptive test names

### Documentation
- Update README.md for user-facing changes
- Add docstrings to all public functions
- Include examples in docstrings
- Update CHANGELOG.md

## Pull Request Process

1. **Update documentation:**
   - Update README.md if needed
   - Update CHANGELOG.md
   - Add docstrings to new code

2. **Ensure all checks pass:**
   ```bash
   make all
   ./validate.sh
   ```

3. **Create pull request:**
   - Use descriptive title
   - Reference any related issues
   - Describe changes clearly
   - List any breaking changes

4. **Wait for review:**
   - Address reviewer comments
   - Update code as needed
   - Ensure CI passes

## Areas for Contribution

### High Priority
- Add more verb conjugation patterns
- Expand noun declension (irregular forms)
- Add adjective declension
- Improve transliteration accuracy
- Add audio pronunciation support

### Medium Priority
- Add more business Russian scenarios
- Expand cultural guide content
- Add more tests for edge cases
- Improve error messages
- Add caching for API responses

### Low Priority
- Web frontend
- Mobile app
- Additional language pairs
- Gamification features
- Social features

## Code of Conduct

### Our Pledge
We are committed to providing a welcoming and inclusive environment for all contributors.

### Our Standards
- Be respectful and professional
- Accept constructive criticism gracefully
- Focus on what is best for the project
- Show empathy towards other contributors

### Unacceptable Behavior
- Harassment or discrimination
- Trolling or insulting comments
- Publishing others' private information
- Other unprofessional conduct

## Getting Help

### Resources
- Documentation: See README.md and docs/
- Examples: See examples/ directory
- Tests: See tests/ directory for usage examples

### Contact
- Email: nikjois@llamasearch.ai
- GitHub Issues: Use for bug reports and feature requests

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project documentation

Thank you for contributing to OpenGov-EarlyRussian!

---

**Author:** Nik Jois <nikjois@llamasearch.ai>  
**License:** MIT

