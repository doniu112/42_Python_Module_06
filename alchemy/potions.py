import elements
from alchemy.elements import *

def healing_potion() -> str:
    return (f"Healing potion brewed with "
            f"'{create_earth()}' and '{create_air()}'")

def strength_potion() -> str:
    return (f"Strength potion brewed with "
            f"'{elements.create_fire()}' and '{elements.create_water()}'")
