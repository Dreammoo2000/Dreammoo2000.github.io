import json

# Load the JSON data
with open("templates/template.json", "r") as f:
    data = json.load(f)

# Extract data for characters and enemies
Acheron = data["characters"]["Acheron"]
Ruan_Mei = data["characters"]["Ruan_Mei"]
enemy = data["enemy"]

# Character stats
Atk = Acheron["Atk"]
Dmg = Acheron["Dmg"] / 100  # Convert percentage to decimal
Crit_Dmg = Acheron["Crit_Dmg"] / 100
Dmg_Multiplier = Acheron["Dmg_Multiplier"] / 100
Energy = Acheron["Energy"]

# Ruan Mei stats
Dmg += Ruan_Mei["Dmg_Bonus"] / 100  # Add bonus damage
Res_Pen = Ruan_Mei["Res_Pen"] / 100  # Resistance penetration

# Enemy stats
Enemy_Lv = enemy["Level"]
Enemy_Weak = enemy["Weak"]
Vulnerability = enemy["Vulnerability"] / 100  # Convert percentage to decimal
Toughness_Broken = enemy["Toughness_Broken"]
Def_Down = enemy["Def_Down"]

# Calculate enemy defense multiplier
Enemy_Defense_Multiplier = 100 / ((Enemy_Lv + 20) * (1 - Def_Down) + 100)

# Enemy type multiplier
if Enemy_Weak:
    Enemy_Type = 100 / 100  # Convert to decimal
else:
    Enemy_Type = 80 / 100  # Default to 80% for non-weak

# Toughness multiplier
Toughness = 90 / 100 if not Toughness_Broken else 100 / 100

# True damage (fixed 0 as Acheron always has 0 energy)
True_Dmg = 30 / 100 + 6 / 100  # Base 30% + additional 6% when energy is 0

# Final damage formula
result = (
    Atk
    * Dmg_Multiplier
    * (1 + Dmg)
    * (1 + Crit_Dmg)
    * Enemy_Defense_Multiplier
    * (Enemy_Type + Res_Pen)
    * Vulnerability
    * Toughness
    * (1 + True_Dmg)
)

# Output the result
print(f"Acheron's Damage: {result}")
