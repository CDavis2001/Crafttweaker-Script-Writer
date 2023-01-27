read = ""
file = open("recipes.zs", "a")
supported_machines = ["nuclearcraft:alloyfurnace","nuclearcraft:centrifuge"]
while read != "end":
    print("Welcome to Crafttweaker Script Writer")
    read = input("Enter machine type or enter 'end' to exit. Or enter 'help' to print a list of options\n\t")
    if read == "end":
        break
    elif read == "help":
        print("machine options are:")
        for machine in supported_machines:
            print(machine + ",")
        continue
    elif read == "nuclearcraft:alloyfurnace":
        line = "mods.nuclearcraft.alloy_furnace.addRecipe(["
        inputs = []
        inputs.append(input("enter item input 1: "))
        inputs.append(input("enter item input 2: "))
        inputs.append(input("enter item output: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:centrifuge":
        line = "mods.nuclearcraft:centrifuge"

file.close()