print("=== Kaboom 1 ===")

try:
    from alchemy.grimoire.dark_spellbook import dark_spell_record
except ImportError as error:
    print(f"Import error: {error}")
else:
    print(dark_spell_record("Dark ritual", "bats and arsenic"))