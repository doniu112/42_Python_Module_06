import alchemy


print("=== Distillation 1 ===")
print("Using: 'import alchemy' structure to access potions")
print(f"Testing strength_potion: {alchemy.heal()}")
print(f"Testing heal alias: {alchemy.strength_potion()}")
