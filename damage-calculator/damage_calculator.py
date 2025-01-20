# Values for Acheron
Acheron = True  # Main DPS character
Energy = 0 if Acheron else None  # Fixed 0 energy for Acheron

# Basic stats
Atk = 5000
Dmg_Multiplier = 500 / 100  # Convert percentage to decimal
Dmg = 300 / 100  # Convert percentage to decimal
Crit_Dmg = 300 / 100  # Convert percentage to decimal

# Enemy stats
Enemy_Lv = 95
Def_Down = 0  # No defense down applied
Enemy_Weak = True  # Enemy is weak
Vulnerability = 50 / 100  # Convert percentage to decimal
Toughness_Broken = False  # Enemy is not toughness broken
Res_Pen = 0  # Resistance Penetration

# Adjustments for Ruan Mei
Ruan_mei = True  # Ruan Mei is active
if Ruan_mei:
    Dmg += 68 / 100  # 68% additional damage
    Res_Pen += 25 / 100  # 25% resistance penetration

# Calculate enemy defense multiplier
Enemy_Defense_Multiplier = 100 / ((Enemy_Lv + 20) * (1 - Def_Down) + 100)

# Enemy type multiplier
if Enemy_Weak:
    Enemy_Type = 100 / 100  # Convert to decimal for calculation
else:
    Enemy_Type = 80 / 100  # Assume false weak as default

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
