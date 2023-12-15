def solve(protons_start, neutrons_start, protons_target, neutrons_target):
    recipe = []
    
    while protons_start != protons_target or neutrons_start != neutrons_target:
        if protons_start < protons_target:
            recipe.append("PROTON")
            protons_start += 1
        elif protons_start > protons_target:
            recipe.append("ALPHA")
            protons_start -= 2
            neutrons_start -= 2
        
        if neutrons_start < neutrons_target:
            recipe.append("NEUTRON")
            neutrons_start += 1
        elif neutrons_start > neutrons_target:
            recipe.append("ALPHA")
            protons_start -= 2
            neutrons_start -= 2
        
        if len(recipe) > 1000:  # Condition pour éviter une boucle infinie
            return ["Too many operations, unable to synthesize."]
    
    return recipe

protons_start = 5
neutrons_start = 8
protons_target = 10
neutrons_target = 5

result = solve(protons_start, neutrons_start, protons_target, neutrons_target)
print(result)
