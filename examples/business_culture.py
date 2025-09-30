"""
Business Russian and Cultural Guide examples
Author: Nik Jois <nikjois@llamasearch.ai>
"""

from opengov_earlyrussian.core.business import BusinessRussian
from opengov_earlyrussian.core.culture import CulturalGuide


def demonstrate_business_email():
    """Show business email templates."""
    print("[BUSINESS EMAIL TEMPLATES]")
    print("-" * 60)
    br = BusinessRussian()

    # Meeting request
    meeting = br.email_template("meeting")
    print("Meeting Request Template:")
    print(f"  Subject: {meeting['subject']}")
    print(f"  Body: {meeting['body']}")
    print(f"  Signoff: {meeting['signoff']}")

    # Follow-up
    print("\nFollow-up Template:")
    followup = br.email_template("follow_up")
    print(f"  Subject: {followup['subject']}")
    print(f"  Body: {followup['body']}")
    print()


def demonstrate_business_phone():
    """Show business phone phrases."""
    print("\n[BUSINESS PHONE PHRASES]")
    print("-" * 60)
    br = BusinessRussian()

    phrases = br.phone_phrases()
    print("Standard phone conversation:")
    print(f"  Opening: {phrases['intro']}")
    print(f"  Check: {phrases['ask_availability']}")
    print(f"  Request: {phrases['request']}")
    print(f"  Closing: {phrases['closing']}")
    print()


def demonstrate_culture():
    """Show cultural information."""
    print("\n[CULTURAL GUIDE]")
    print("-" * 60)
    guide = CulturalGuide()

    # Regions
    print("Major Regions of Russia:")
    for region in guide.regions():
        print(f"  - {region}")

    # Holidays
    print("\nMajor Holidays:")
    holidays = guide.holidays()
    for holiday, date in holidays.items():
        print(f"  - {holiday}: {date}")

    # Etiquette
    print("\nBusiness Etiquette:")
    for rule in guide.etiquette():
        print(f"  - {rule}")
    print()


def create_sample_email():
    """Create a customized business email."""
    print("\n[SAMPLE EMAIL]")
    print("-" * 60)
    br = BusinessRussian()

    template = br.email_template("meeting")

    # Customize template
    email = template["body"].format(date="15 января", time="14:00", name="Иван Петров")
    signoff = template["signoff"].format(
        name="Иван Петров", role="Менеджер проектов", company="ООО 'ТехноСервис'"
    )

    print(f"От: ivan.petrov@technoservice.ru")
    print(f"Тема: {template['subject']}")
    print()
    print(email)
    print()
    print(signoff)
    print()


def create_sample_phone_script():
    """Create a sample phone conversation script."""
    print("\n[SAMPLE PHONE SCRIPT]")
    print("-" * 60)
    br = BusinessRussian()
    phrases = br.phone_phrases()

    intro = phrases["intro"].format(name="Анна Сергеева", company="ИнноТех Решения")
    request = phrases["request"].format(topic="возможность сотрудничества")

    print("Business Phone Call Script:")
    print()
    print(f"1. {intro}")
    print(f"2. {phrases['ask_availability']}")
    print(f"3. {request}")
    print(f"4. [Discussion...]")
    print(f"5. {phrases['closing']}")
    print()


def main():
    """Run all business and culture demonstrations."""
    print("=" * 60)
    print("Business Russian & Cultural Guide Examples")
    print("Author: Nik Jois <nikjois@llamasearch.ai>")
    print("=" * 60)
    print()

    demonstrate_business_email()
    demonstrate_business_phone()
    demonstrate_culture()
    create_sample_email()
    create_sample_phone_script()

    print("=" * 60)
    print("Examples complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
