"""
Basic usage examples for OpenGov-EarlyRussian
Author: Nik Jois <nikjois@llamasearch.ai>
"""

from opengov_earlyrussian import (
    AlphabetTeacher,
    PronunciationCoach,
    CasesTeacher,
    VerbConjugator,
    Transliterator,
)


def demonstrate_alphabet():
    """Demonstrate alphabet teaching features."""
    print("[ALPHABET TEACHER]")
    print("-" * 50)
    teacher = AlphabetTeacher()

    # Show iotated vowels
    iotated = teacher.get_row("iotated")
    print(f"Iotated vowels: {', '.join(iotated['letters'])}")

    # Show mnemonics
    for letter in ["Ё", "Ы", "Ь", "Ъ", "Щ"]:
        print(f"\n{letter}: {teacher.mnemonic(letter)}")
    print()


def demonstrate_pronunciation():
    """Demonstrate pronunciation coaching."""
    print("\n[PRONUNCIATION COACH]")
    print("-" * 50)
    coach = PronunciationCoach()

    # Vowel reduction
    vowel_red = coach.get_feature("vowel_reduction")
    print("Vowel Reduction:")
    print(f"  - Аканье: {vowel_red['akanje']}")
    print(f"  - Иканье: {vowel_red['ikanje']}")

    # Minimal pairs
    pairs = coach.minimal_pairs()
    print("\nMinimal Pairs (Hard/Soft):")
    for pair in pairs["hard_soft"]:
        print(f"  - {pair}")
    print()


def demonstrate_cases():
    """Demonstrate case declension."""
    print("\n[CASES TEACHER]")
    print("-" * 50)
    teacher = CasesTeacher()

    # Feminine noun
    print("Feminine noun 'книга' (book):")
    book = teacher.decline_noun("книга", "feminine")
    for case, form in book.items():
        print(f"  {case:15s}: {form}")

    # Masculine inanimate
    print("\nMasculine inanimate 'паспорт' (passport):")
    passport = teacher.decline_noun("паспорт", "masculine", animate=False)
    print(f"  Accusative (inanimate): {passport['винительный']}")

    # Masculine animate
    print("\nMasculine animate 'студент' (student):")
    student = teacher.decline_noun("студент", "masculine", animate=True)
    print(f"  Accusative (animate): {student['винительный']}")
    print(f"  Note: Accusative = Genitive for animate masculines")
    print()


def demonstrate_verbs():
    """Demonstrate verb conjugation."""
    print("\n[VERB CONJUGATOR]")
    print("-" * 50)
    conjugator = VerbConjugator()

    # Aspect pairs
    print("Aspect Pairs (Imperfective → Perfective):")
    verbs = ["читать", "писать", "говорить", "делать"]
    for verb in verbs:
        perfective = conjugator.aspect_pair(verb)
        print(f"  {verb} → {perfective}")

    # Present tense conjugation
    print("\nPresent tense 'читать' (to read):")
    present = conjugator.conjugate("читать", "present")
    for person, form in present["forms"].items():
        print(f"  {person:12s}: {form}")

    # Past tense conjugation
    print("\nPast tense 'говорить' (to speak):")
    past = conjugator.conjugate("говорить", "past")
    for person, form in past["forms"].items():
        print(f"  {person:12s}: {form}")
    print()


def demonstrate_transliteration():
    """Demonstrate transliteration."""
    print("\n[TRANSLITERATOR]")
    print("-" * 50)
    trans = Transliterator()

    examples = [
        "Mikhail Lomonosov",
        "Sankt-Peterburg",
        "Moskva",
        "Zdravstvuyte",
        "Dostoevsky",
        "Tchaikovsky",
    ]

    print("Latin → Russian transliteration:")
    for text in examples:
        result = trans.to_russian(text)
        print(f"  {text:20s} → {result}")
    print()


def main():
    """Run all demonstrations."""
    print("=" * 50)
    print("OpenGov-EarlyRussian Python API Examples")
    print("Author: Nik Jois <nikjois@llamasearch.ai>")
    print("=" * 50)

    demonstrate_alphabet()
    demonstrate_pronunciation()
    demonstrate_cases()
    demonstrate_verbs()
    demonstrate_transliteration()

    print("\n" + "=" * 50)
    print("Demonstrations complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
