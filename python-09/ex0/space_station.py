from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = datetime.now()
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:

    try:
        valid_station = SpaceStation(station_id="ISS001",
                                     name="International Space Station",
                                     crew_size=6, power_level=85.5,
                                     oxygen_level=92.3, is_operational=True)
        print("Space Station Data Validation")
        print("========================================")
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print(f"Status: {'not ' if not valid_station.is_operational else ''}\
operational")
    except ValidationError as ve:
        print(ve)
    print("\n========================================")
    print("Expected validation error:")
    try:
        invalid_station = SpaceStation(station_id="ISS001",
                                       name="invalid",
                                       crew_size=60, power_level=85.5,
                                       oxygen_level=92.3, is_operational=True)
        print(invalid_station)
    except ValidationError:
        print("Input should be less than or equal to 20")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
