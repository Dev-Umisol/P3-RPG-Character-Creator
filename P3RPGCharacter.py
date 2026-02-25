# Building a "Small" App that creates a character for an RPG adventure

#! Project 3: RPG Character Creator
# This project was able to help reinforce learning for conditional statements, logic operators, and functions
# It also was very helpful in string manipulation and formatting.

fullDot = "●"
emptyDot = "○" 

def createCharacter(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    if not (strength + intelligence + charisma) == 7:
        return "The character should start with 7 points"
    return name + "\nSTR" + " " + fullDot * strength + emptyDot * (10 - strength) + "\nINT" + " " + fullDot * intelligence + emptyDot * (10 - intelligence) + "\nCHA" + " " + fullDot * charisma + emptyDot * (10 - charisma)

print(createCharacter("ren", 4, 2, 1)) # Test character creation
