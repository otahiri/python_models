import random
import functools
import time


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def timer(*args: tuple, **kwargs: dict):
        start = time.time()
        print(f"Casting {func.__name__}")
        res = func(*args, **kwargs)
        print(f"Spell completed in {time.time() - start} seconds")
        return res
    return timer


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def validate(power: int, *args: tuple, **kwargs: dict) -> str:
            if power < min_power:
                return "Insufficient power for this spell"
            else:
                return func(power, *args, **kwargs)
        return validate
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def retry(*args: tuple, **kwargs: dict) -> str:
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... (attempt \
{attempt}/{max_attempts})")
                    else:
                        return f"Spell casting failed after \
{max_attempts} attempts"
        return retry
    return decorator


@retry_spell(7)
def spell() -> str:
    if random.random() < 0.7:
        raise ValueError
    else:
        return "spell cast  succefful"


print(spell())


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all([c.isalpha or c == " " for c in name])

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"
