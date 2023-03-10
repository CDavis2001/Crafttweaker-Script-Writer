from recipe_writers.nuclearcraft import nuclearcraft
from recipe_writers.techreborn import techreborn
from recipe_writers.thermal  import thermal
from recipe_writers.advrocket import advrocket
from recipe_writers.modularmachinery import modularmachinery

read = ""
previous = ""
file = open("recipes.zs", "a")
supported_machines = ["nuclearcraft:alloyfurnace","nuclearcraft:centrifuge", "nuclearcraft:chemicalreactor", "nuclearcraft:condenser", "nuclearcraft:crystallizer", "nuclearcraft:decaygenerator", "nuclearcraft:decayhastener", "nuclearcraft:electrolyser", "nuclearcraft:fission", "nuclearcraft:fluidenricher", "nuclearcraft:fluidextractor", "nuclearcraft:fuelreprocessor", "nuclearcraft:fusion", "nuclearcraft:heatexchanger", "nuclearcraft:fluidinfuser", "nuclearcraft:ingotformer", "nuclearcraft:irradiator", "nuclearcraft:isotopeseparator", "nuclearcraft:manufactory", "nuclearcraft:melter", "nuclearcraft:pressurizer", "nuclearcraft:rockcrusher", "nuclearcraft:saltfission", "nuclearcraft:saltmixer", "nuclearcraft:turbine", "nuclearcraft:supercooler", "techreborn:alloysmelter", "techreborn:assemblingmachine", "techreborn:centrifuge", "techreborn:chemicalreactor", "techreborn:compressor", "techreborn:distillationtower", "techreborn:extractor", "techreborn:thermalgen", "techreborn:gasgen", "techreborn:semigen", "techreborn:dieselgen", "techreborn:plasmagen", "techreborn:fluidreplicator", "techreborn:fusionreactor", "techreborn:grinder", "techreborn:implosioncompressor", "techreborn:blastfurnace", "techreborn:electrolyzer", "techreborn:industrialgrinder", "techreborn:industrialsawmill", "techreborn:platebendingmachine", "techreborn:rollingmachine", "techreborn:solidcanningmachine", "techreborn:vacuumfreezer", "techreborn:wiremill", "thermal:centrifuge", "thermal:compactor", "thermal:still", "thermal:inductionsmelter", "thermal:magmacrucible", "thermal:redstonefurnace", "thermal:redstonefurnacepyrolitic", "thermal:pulverizer", "thermal:sawmill", "advrocket:chemicalreactor", "advrocket:arcfurnace", "modularmachinery"]
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
        for machine in supported_machines:
            print("\t- " + machine + ",")
        continue
    if read in supported_machines:
        previous = read
        if read == "modularmachinery":
            line = modularmachinery.add()
        else:
            reads = read.split(":")
            line = eval(reads[0] + "." + reads[1] + "()")
        
        file.write(line)
    else:
        print("Input Not Recognised")
file.close()
