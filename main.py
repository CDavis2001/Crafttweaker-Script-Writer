from recipe_writers.nuclearcraft import nuclearcraft
from recipe_writers.techreborn import techreborn
from recipe_writers.thermal  import thermal
from recipe_writers.advrocket import advrocket
from recipe_writers.modularmachinery import modularmachinery

read = ""
previous = ""
file = open("recipes.zs", "a")
supported_mods = ["nuclearcraft", "techreborn", "thermal", "advrocket"]
supported_machines = dict()
for mod in supported_mods:
    supported_machines[mod] = (eval(mod + ".machine_list()"))
    
while read != "end":
    print("\nWelcome to Crafttweaker Script Writer")
    read = input("Please Enter one of the following options\n\tEnter Machine Type to create a recipe\n\tEnter 'end' to exit\n\tEnter 'repeat' for the same machine as last time\n\tEnter 'help' to print a list of options\n\nInput: ")
    if read == "end":
        break
    elif read == "repeat":
        print("Repeating: " + previous)
        read = previous
    elif read == "help":
        print("Machine Options are:")
        for key in supported_mods:
            print(key + ":" )
            for machine in supported_machines[key]:
                print("\t" + machine)
        continue
    if read == "modularmachinery":
        line = modularmachinery.add()
        file.write(line)
    
    reads = read.split(":")
    if len(reads) == 2:
        if reads[0] in supported_machines:
            print("found mod")
            if reads[1] in supported_machines[reads[0]]:
                print("found machine")
                line = eval(reads[0] + "." + reads[1] + "()")
                file.write(line)
        
    else:
        print("Input Not Recognised")
file.close()
