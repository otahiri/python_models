from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = datetime.now()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field()
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def rule_validator(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValidationError("Contact ID must start with 'AC' (Alien Contact)")
        elif self.contact_type == ContactType.PHYSICAL\
                and not self.is_verified:
            raise ValidationError("Physical contact reports must be verified")
        elif self.contact_type == ContactType.TELEPATHIC and\
                self.witness_count < 3:
            raise ValidationError("Telepathic contact requires at least \
3 witnesses")
        elif self.signal_strength > 7 and not self.message_received:
            raise ValidationError("Strong signals (> 7.0) should include \
received messages")
        else:
            return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    valid_contact = AlienContact(contact_id="AC_2024_001",
                                 location="Area 51, Nevada",
                                 contact_type=ContactType.RADIO,
                                 signal_strength=8.5, duration_minutes=45,
                                 witness_count=5,
                                 message_received="Greetings from Zeta \
    Reticuli")
    print("Valid contact report:")
    print(f"ID: {valid_contact.contact_id}")
    print(f"Type: {valid_contact.contact_type.value}")
    print(f"Location: {valid_contact.location}")
    print(f"Signal: {valid_contact.signal_strength}/10")
    print(f"Duration: {valid_contact.duration_minutes} minutes")
    print("Witnesses: 5")
    print(f"Message: '{valid_contact.message_received}'")
    print("\n======================================")
    print("Expected validation error:")
    try:
        invalid_contact = AlienContact(contact_id="AC_2024_001",
                                       location="Area 51, Nevada",
                                       contact_type=ContactType.TELEPATHIC,
                                       signal_strength=8.5,
                                       duration_minutes=45,
                                       witness_count=2,
                                       message_received="Greetings from Zeta \
Reticuli")
        print(invalid_contact)
    except ValidationError as ve:
        print(ve)


if __name__ == "__main__":
    main()
