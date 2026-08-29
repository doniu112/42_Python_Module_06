import alchemy


print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}\n")

print(f"Testing the hidden create_earth: ", end="")
print(f"{alchemy.create_earth()}")

