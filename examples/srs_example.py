"""
Spaced Repetition System (SRS) example
Author: Nik Jois <nikjois@llamasearch.ai>
"""

from opengov_earlyrussian.core.srs import SRS
from datetime import datetime


def demonstrate_srs():
    """Demonstrate the spaced repetition system."""
    print("[SPACED REPETITION SYSTEM]")
    print("-" * 60)

    # Create SRS instance
    srs = SRS()

    # Add vocabulary items
    print("Adding vocabulary items...")
    items = [
        ("vocab1", "книга (род.)", "книги"),
        ("vocab2", "студент (вин. anim.)", "студента"),
        ("vocab3", "говорить (я)", "говорю"),
        ("vocab4", "читать (perfective)", "прочитать"),
        ("vocab5", "Здравствуйте (meaning)", "Hello (formal)"),
    ]

    for item_id, prompt, answer in items:
        item = srs.add(item_id, prompt, answer)
        print(f"  Added: {prompt} → {answer}")

    print(f"\nTotal items in system: {len(srs.items)}")
    print()

    # Simulate review session
    print("\n[REVIEW SESSION 1]")
    print("-" * 60)

    # Easy review
    print("\nReviewing 'vocab1' with quality: easy")
    item = srs.review("vocab1", "easy")
    print(f"  Interval: {item.interval} days")
    print(f"  Ease factor: {item.ease:.2f}")
    print(f"  Next review: {item.next_review.strftime('%Y-%m-%d')}")

    # Good review
    print("\nReviewing 'vocab2' with quality: good")
    item = srs.review("vocab2", "good")
    print(f"  Interval: {item.interval} days")
    print(f"  Ease factor: {item.ease:.2f}")
    print(f"  Next review: {item.next_review.strftime('%Y-%m-%d')}")

    # Hard review
    print("\nReviewing 'vocab3' with quality: hard")
    item = srs.review("vocab3", "hard")
    print(f"  Interval: {item.interval} days")
    print(f"  Ease factor: {item.ease:.2f}")
    print(f"  Next review: {item.next_review.strftime('%Y-%m-%d')}")

    # Failed review
    print("\nReviewing 'vocab4' with quality: fail")
    item = srs.review("vocab4", "fail")
    print(f"  Interval: {item.interval} days (reset to 1)")
    print(f"  Ease factor: {item.ease:.2f}")
    print(f"  Next review: {item.next_review.strftime('%Y-%m-%d')}")

    print()

    # Show all items status
    print("\n[CURRENT STATUS OF ALL ITEMS]")
    print("-" * 60)
    print(f"{'Item ID':<12} {'Reps':<8} {'Interval':<10} {'Ease':<8} {'Next Review'}")
    print("-" * 60)

    for item_id, item in srs.items.items():
        print(
            f"{item_id:<12} {item.reps:<8} {item.interval:<10} {item.ease:<8.2f} "
            f"{item.next_review.strftime('%Y-%m-%d')}"
        )

    print()

    # Multiple review cycles
    print("\n[MULTIPLE REVIEW CYCLES]")
    print("-" * 60)
    print("Simulating multiple successful reviews of 'vocab5':")

    item = srs.items["vocab5"]
    print(f"\nInitial: interval={item.interval}, ease={item.ease:.2f}")

    for i in range(1, 6):
        item = srs.review("vocab5", "good")
        print(f"Review {i}: interval={item.interval}, ease={item.ease:.2f}")

    print()


def demonstrate_learning_curve():
    """Show how SRS intervals grow over time."""
    print("\n[LEARNING CURVE SIMULATION]")
    print("-" * 60)

    srs = SRS()
    srs.add("test", "тест", "test")

    print("Quality: GOOD (consistent)")
    print(f"{'Review #':<12} {'Interval (days)':<18} {'Ease Factor'}")
    print("-" * 60)

    for i in range(10):
        item = srs.items["test"]
        print(f"{i:<12} {item.interval:<18} {item.ease:.2f}")
        srs.review("test", "good")

    print("\nNote: With consistent 'good' ratings, intervals grow exponentially")
    print("      allowing for efficient long-term retention.")
    print()


def main():
    """Run all SRS demonstrations."""
    print("=" * 60)
    print("Spaced Repetition System (SRS) Examples")
    print("Author: Nik Jois <nikjois@llamasearch.ai>")
    print("=" * 60)
    print()

    demonstrate_srs()
    demonstrate_learning_curve()

    print("=" * 60)
    print("SRS demonstrations complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
