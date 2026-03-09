# 📁 RPG Character Creator
A Python function that builds and displays a formatted RPG character sheet with stat validation and a visual dot-based stat bar.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Learning-Journey-orange)

## 📌 About

This project was built to reinforce conditional statements, logical operators, functions, and string formatting. The function creates an RPG character by validating a name and three stats: Strength, Intelligence, and Charisma, then returns a neatly formatted character sheet with visual dot based stat bars. Characters must distribute exactly 7 points across their stats, staying true to classic RPG point buy systems.

## 🧠 What I Learned
- **Chained input validation** — Using a series of individual `if` checks (rather than `elif`) so each rule is clearly separated and independently readable, which made debugging much easier
- **String multiplication for visual output** — Using `"●" * strength` and `"○" * (10 - strength)` to build a filled/empty dot bar entirely from string operations, no loops needed
- **Point-buy validation with arithmetic** — Enforcing a 7-point budget with a single condition: `not (strength + intelligence + charisma) == 7`, combining logic and math in one check
- **String concatenation and `\n`** — Building a multi-line formatted output entirely through string concatenation, using `\n` for line breaks and spacing for alignment
- **Unicode characters** — Using `●` and `○` as visual elements directly in Python strings to make terminal output more engaging

## 🛠️ Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x   | Core Language |

## 💡 How It Works
`createCharacter(name, strength, intelligence, charisma)` validates all inputs then returns a formatted character sheet.

Rules:
- Name must be a non-empty string, max 10 characters, no spaces
- All stats must be integers between 1 and 4
- Stats must add up to exactly 7

**Example Output:**
```
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
```

## 🚀 Future Improvements
- [ ] Add more stat categories (e.g. Dexterity, Luck) with an adjustable point budget
- [ ] Let the user pick a character class (Warrior, Mage, Rogue) that sets stat minimums automatically
- [ ] Refactor the stat bar into a reusable helper function to reduce repetition in the return string
- [ ] Build an interactive CLI so users can input their character details step by step

## 📂 Project Structure
```
rpg-character-creator/
│
├── P3RPGCharacter.py    # createCharacter function and test call
└── README.md
```

*Part of my Python learning journey 🐍 — practicing conditionals, string manipulation, and formatting*
