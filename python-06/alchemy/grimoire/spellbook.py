# importing the entire module to avoid circular import
import alchemy.grimoire


def record_spell(spell_name: str, ingredients: str) -> str:
    # late importing to avoid circular import
    from ..grimoire import validator
    result = validator.validate_ingredients(ingredients)
    result = alchemy.grimoire.validate_ingredients(ingredients)
    if "INVALID" in result:
        return f"Spell rejected: {spell_name} ({result})"
    else:
        return f"Spell recorded: {spell_name} ({result})"
