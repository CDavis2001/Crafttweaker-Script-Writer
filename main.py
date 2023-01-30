read = ""
previous = ""
file = open("recipes.zs", "a")
supported_machines = ["nuclearcraft:alloyfurnace","nuclearcraft:centrifuge", "nuclearcraft:chemical_reactor", "nuclearcraft:condenser", "nuclearcraft:crystallizer", "nuclearcraft:decaygenerator", "nuclearcraft:decayhastener", "nuclearcraft:electrolyser", "nuclearcraft:fission", "nuclearcraft:fluidenricher", "nuclearcraft:fluidextractor", "nuclearcraft:fuelreprocessor", "nuclearcraft:fusion", "nuclearcraft:heatexchanger", "nuclearcraft:fluidinfuser", "nuclearcraft:ingotformer", "nuclearcraft:irradiator", "nuclearcraft:isotopeseparator", "nuclearcraft:manufactory", "nuclearcraft:melter", "nuclearcraft:pressurizer", "nuclearcraft:rockcrusher", "nuclearcraft:saltfission", "nuclearcraft:saltmixer", "nuclearcraft:turbine", "nuclearcraft:supercooler", "techreborn:alloysmelter", "techreborn:assemblingmachine", "techreborn:centrifuge", "techreborn:chemicalreactor", "techreborn:compressor", "techreborn:distillationtower", "techreborn:extractor", "techreborn:thermalgen", "techreborn:gasgen", "techreborn:semigen", "techreborn:dieselgen", "techreborn:plasmagen", "techreborn:fluidreplicator", "techreborn:fusionreactor", "techreborn:grinder", "techreborn:implosioncompressor", "techreborn:blastfurnace", "techreborn:electrolyzer", "techreborn:industrialgrinder", "techreborn:industrialsawmill", "techreborn:platebendingmachine", "techreborn:rollingmachine", "techreborn:solidcanningmachine", "techreborn:vacuumfreezer", "techreborn:wiremill", "thermal:centrifuge", "thermal:compactor", "thermal:still", "thermal:inductionsmelter", "thermal:magmacrucible", "thermal:redstonefurnace", "thermal:redstonefurnacepyrolitic", "thermal:pulverizer", "thermal:sawmill", "advrocket:chemicalreactor"]
while read != "end":
    print("Welcome to Crafttweaker Script Writer")
    read = input("Please Enter one of the following options\n\tEnter Machine Type\n\tEnter 'end' to exit\n\tEnter 'repeat' for the same machine as last time\n\tEnter 'help' to print a list of options\n\nInput: ")
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
    if read == "nuclearcraft:alloyfurnace":
        previous = read
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
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:centrifuge":
        previous = read
        line = "mods.nuclearcraft.centrifuge.addRecipe(["
        inputs = []
        inputs.append(input("enter fluid input: "))
        inputs.append(input("enter fluid output 1: "))
        inputs.append(input("enter fluid output 2: "))
        inputs.append(input("enter fluid output 3: "))
        inputs.append(input("enter fluid output 4: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:chemical_reactor":
        previous = read
        line = "mods.nuclearcraft.chemical_reactor.addRecipe(["
        inputs = []
        inputs.append(input("enter fluid input 1: "))
        inputs.append(input("enter fluid input 2: "))
        inputs.append(input("enter fluid output 1: "))
        inputs.append(input("enter fluid output 2: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:condenser":
        previous = read
        line = "mods.nuclearcraft.condenser.addRecipe(["
        inputs = []
        inputs.append(input("enter fluid input: "))
        inputs.append(input("enter fluid output: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:crystallizer":
        previous = read
        line = "mods.nuclearcraft.crystallizer.addRecipe(["
        inputs = []
        inputs.append(input("enter fluid input: "))
        inputs.append(input("enter item output: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:decaygenerator":
        previous = read
        line = "mods.nuclearcraft.decay_generator.addRecipe(["
        inputs = []
        inputs.append(input("enter block input: "))
        inputs.append(input("enter block output: "))
        inputs.append(input("enter lifetime ticks: "))
        inputs.append(input("enter energy per second: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:decayhastener":
        previous = read
        line = "mods.nuclearcraft.decay_hastener.addRecipe(["
        inputs = []
        inputs.append(input("enter item input: "))
        inputs.append(input("enter item output: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:electrolyser":
        previous = read
        line = "mods.nuclearcraft.electrolyser.addRecipe(["
        inputs = []
        inputs.append(input("enter fluid input: "))
        inputs.append(input("enter fluid output 1: "))
        inputs.append(input("enter fluid output 2: "))
        inputs.append(input("enter fluid output 3: "))
        inputs.append(input("enter fluid output 4: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:fission":
        previous = read
        line = "mods.nuclearcraft.fission.addRecipe(["
        inputs = []
        inputs.append(input("enter item input: "))
        inputs.append(input("enter item output: "))
        inputs.append(input("enter base time: "))
        inputs.append(input("enter base power: "))
        inputs.append(input("enter base heat: "))
        inputs.append(input("enter string gui name: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:fluidenricher":
        previous = read
        line = "mods.nuclearcraft.dissolver.addRecipe(["
        inputs = []
        inputs.append(input("enter item input: "))
        inputs.append(input("enter fluid input: "))
        inputs.append(input("enter fluid output: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:fluidextractor":
        previous = read
        line = "mods.nuclearcraft.extractor.addRecipe(["
        inputs = []
        inputs.append(input("enter item input: "))
        inputs.append(input("enter item output: "))
        inputs.append(input("enter fluid output: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:fuelreprocessor":
        previous = read
        line = "mods.nuclearcraft.fuel_reprocessor.addRecipe(["
        inputs = []
        inputs.append(input("enter item input: "))
        inputs.append(input("enter item output: "))
        inputs.append(input("enter fluid output: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:fusion":
        previous = read
        line = "mods.nuclearcraft.fusion.addRecipe(["
        inputs = []
        inputs.append(input("enter fluid input 1: "))
        inputs.append(input("enter fluid input 2: "))
        inputs.append(input("enter fluid output 1: "))
        inputs.append(input("enter fluid output 2: "))
        inputs.append(input("enter fluid output 3: "))
        inputs.append(input("enter fluid output 4: "))
        inputs.append(input("enter item output: "))
        inputs.append(input("enter combo time: "))
        inputs.append(input("enter combo power: "))
        inputs.append(input("enter combo heat var: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:heatexchanger":
        previous = read
        line = "mods.nuclearcraft.heat_exchanger.addRecipe(["
        inputs = []
        inputs.append(input("enter fluid input: "))
        inputs.append(input("enter fluid output: "))
        inputs.append(input("enter heat required: "))
        inputs.append(input("enter temperature in: "))
        inputs.append(input("enter temperature out: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:fluidinfuser":
        previous = read
        line = "mods.nuclearcraft.infuser.addRecipe(["
        inputs = []
        inputs.append(input("enter item input: "))
        inputs.append(input("enter fluid input: "))
        inputs.append(input("enter item output: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:ingotformer":
        previous = read
        line = "mods.nuclearcraft.ingot_former.addRecipe(["
        inputs = []
        inputs.append(input("enter fluid input: "))
        inputs.append(input("enter item output: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:irradiator":
        previous = read
        line = "mods.nuclearcraft.irradiator.addRecipe(["
        inputs = []
        inputs.append(input("enter fluid input 1: "))
        inputs.append(input("enter fluid input 2: "))
        inputs.append(input("enter fluid output 1: "))
        inputs.append(input("enter fluid output 2: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:isotopeseparator":
        previous = read
        line = "mods.nuclearcraft.isotope_separator.addRecipe(["
        inputs = []
        inputs.append(input("enter item input: "))
        inputs.append(input("enter item output 1: "))
        inputs.append(input("enter item output 2: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:manufactory":
        previous = read
        line = "mods.nuclearcraft.manufactory.addRecipe(["
        inputs = []
        inputs.append(input("enter item input: "))
        inputs.append(input("enter item output: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:melter":
        previous = read
        line = "mods.nuclearcraft.melter.addRecipe(["
        inputs = []
        inputs.append(input("enter item input: "))
        inputs.append(input("enter fluid output: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:pressurizer":
        previous = read
        line = "mods.nuclearcraft.pressurizer.addRecipe(["
        inputs = []
        inputs.append(input("enter item input: "))
        inputs.append(input("enter item output: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:rockcrusher":
        previous = read
        line = "mods.nuclearcraft.rock_crusher.addRecipe(["
        inputs = []
        inputs.append(input("enter item input: "))
        inputs.append(input("enter item output 1: "))
        inputs.append(input("enter item output 2: "))
        inputs.append(input("enter item output 3: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:saltfission":
        previous = read
        line = "mods.nuclearcraft.salt_fission.addRecipe(["
        inputs = []
        inputs.append(input("enter fluid input: "))
        inputs.append(input("enter fluid output: "))
        inputs.append(input("enter base time: "))
        inputs.append(input("enter base power: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:saltmixer":
        previous = read
        line = "mods.nuclearcraft.salt_mixer.addRecipe(["
        inputs = []
        inputs.append(input("enter fluid input 1: "))
        inputs.append(input("enter fluid input 2: "))
        inputs.append(input("enter fluid output 1: "))
        inputs.append(input("enter fluid output 2: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:turbine":
        previous = read
        line = "mods.nuclearcraft.turbine.addRecipe(["
        inputs = []
        inputs.append(input("enter fluid input: "))
        inputs.append(input("enter fluid output: "))
        inputs.append(input("enter power per mB: "))
        inputs.append(input("enter double expansio level: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "nuclearcraft:supercooler":
        previous = read
        line = "mods.nuclearcraft.supercooler.addRecipe(["
        inputs = []
        inputs.append(input("enter fluid input: "))
        inputs.append(input("enter fluid output: "))
        inputs.append(input("enter time multiplier: "))
        inputs.append(input("enter power multiplier: "))
        inputs.append(input("enter process radiation: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);\n"
        file.write(line)
    elif read == "techreborn:alloysmelter":
        previous = read
        line = "mods.techreborn.alloySmelter.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input 1: "))
        inputs.append(input("enter item input 2: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:assemblingmachine":
        previous = read
        line = "mods.techreborn.assemblingMachine.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input 1: "))
        inputs.append(input("enter item input 2: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:assemblingmachine":
        previous = read
        line = "mods.techreborn.assemblingMachine.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input 1: "))
        inputs.append(input("enter item input 2: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:centrifuge":
        previous = read
        line = "mods.techreborn.centrifuge.addRecipe("
        inputs = []
        inputs.append(input("enter item output 1: "))
        inputs.append(input("enter item output 2: "))
        inputs.append(input("enter item output 3: "))
        inputs.append(input("enter item output 4: "))
        inputs.append(input("enter item input 1: "))
        inputs.append(input("enter item input 2: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:chemicalreactor":
        previous = read
        line = "mods.techreborn.chemicalReactor.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input 1: "))
        inputs.append(input("enter item input 2: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:compressor":
        previous = read
        line = "mods.techreborn.compressor.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:distillationtower":
        previous = read
        line = "mods.techreborn.distillationTower.addRecipe("
        inputs = []
        inputs.append(input("enter item output 1: "))
        inputs.append(input("enter item output 2: "))
        inputs.append(input("enter item output 3: "))
        inputs.append(input("enter item output 4: "))
        inputs.append(input("enter item input 1: "))
        inputs.append(input("enter item input 2: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:extractor":
        previous = read
        line = "mods.techreborn.extractor.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:thermalgen":
        previous = read
        line = "mods.techreborn.fluidGen.addThermalFluid("
        inputs = []
        inputs.append(input("enter fluid fuel: "))
        inputs.append(input("enter power in EU per mB (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:gasgen":
        previous = read
        line = "mods.techreborn.fluidGen.addGasFluid("
        inputs = []
        inputs.append(input("enter fluid fuel: "))
        inputs.append(input("enter power in EU per mB (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:semigen":
        previous = read
        line = "mods.techreborn.fluidGen.addSemiFluid("
        inputs = []
        inputs.append(input("enter fluid fuel: "))
        inputs.append(input("enter power in EU per mB (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:dieselgen":
        previous = read
        line = "mods.techreborn.fluidGen.addDieselFluid("
        inputs = []
        inputs.append(input("enter fluid fuel: "))
        inputs.append(input("enter power in EU per mB (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:plasmagen":
        previous = read
        line = "mods.techreborn.fluidGen.addPlasmaFluid("
        inputs = []
        inputs.append(input("enter fluid fuel: "))
        inputs.append(input("enter power in EU per mB (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:fluidreplicator":
        previous = read
        line = "mods.techreborn.fluidReplicator.addRecipe("
        inputs = []
        inputs.append(input("enter int input: "))
        inputs.append(input("enter liquid output: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:fusionreactor":
        previous = read
        line = "mods.techreborn.fusionReactor.addRecipe("
        inputs = []
        inputs.append(input("enter item top input: "))
        inputs.append(input("enter item bottom input: "))
        inputs.append(input("enter item output: "))
        inputs.append(input("enter start EU: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        inputs.append(input("enter tick time: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:grinder":
        previous = read
        line = "mods.techreborn.grinder.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:implosioncompressor":
        previous = read
        line = "mods.techreborn.implosionCompressor.addRecipe("
        inputs = []
        inputs.append(input("enter item output 1: "))
        inputs.append(input("enter item output 2: "))
        inputs.append(input("enter item input 1: "))
        inputs.append(input("enter item input 2: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:blastfurnace":
        previous = read
        line = "mods.techreborn.blastFurnace.addRecipe("
        inputs = []
        inputs.append(input("enter item output 1: "))
        inputs.append(input("enter item output 2: "))
        inputs.append(input("enter item input 1: "))
        inputs.append(input("enter item input 2: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        inputs.append(input("enter needed heat: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:electrolyzer":
        previous = read
        line = "mods.techreborn.industrialElectrolyzer.addRecipe("
        inputs = []
        inputs.append(input("enter item output 1: "))
        inputs.append(input("enter item output 2: "))
        inputs.append(input("enter item output 3: "))
        inputs.append(input("enter item output 4: "))
        inputs.append(input("enter cell item input: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:industrialgrinder":
        previous = read
        line = "mods.techreborn.industrialGrinder.addRecipe("
        read = input("enter y for a recipe with a fluid: ")
        inputs = []
        inputs.append(input("enter item output 1: "))
        inputs.append(input("enter item output 2: "))
        inputs.append(input("enter item output 3: "))
        inputs.append(input("enter item output 4: "))
        inputs.append(input("enter item input 1: "))
        inputs.append(input("enter item input 2: "))
        if read == "y":
            inputs.append(input("enter fluid input: "))    
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:industrialsawmill":
        previous = read
        line = "mods.techreborn.industrialSawmill.addRecipe("
        read = input("enter y for a recipe with a fluid")
        inputs = []
        inputs.append(input("enter item output 1: "))
        inputs.append(input("enter item output 2: "))
        inputs.append(input("enter item output 3: "))
        inputs.append(input("enter item input 1: "))
        if read == "y":
            inputs.append(input("enter fluid input: "))    
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        read = input("enter y for a oredict recipe")
        if read == "y":
            inputs.append("true")
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:platebendingmachine":
        previous = read
        line = "mods.techreborn.plateBendingMachine.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:rollingmachine":
        previous = read
        read = input("enter y for shaped recipe, anything else for shapeless")
        inputs = []
        inputs.append(input("enter item output: "))
        if read == "y":
            line = "mods.techreborn.rollingMachine.addShaped("
            grid = [[]]
            for i in range(3):
                for j in range(3):
                    item = input.append("enter item in slot (" + str(i) + "," + str(j) + "): ")
                    grid[i,j] = item
            inputs.append(grid)
        else:
            line = "mods.techreborn.rollingMachine.addShapeless("
            ingredients = []
            for i in range(9):
                item = input("enter item input (enter end to finish): ")
                if item == "end":
                    break
                else:
                    ingredients.append(item)
            inputs.append(ingredients)
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:solidcanningmachine":
        previous = read
        line = "mods.techreborn.solidCanningMachine.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input 1: "))
        inputs.append(input("enter item input 2: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:vacuumfreezer":
        previous = read
        line = "mods.techreborn.vacuumFreezer.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "techreborn:wiremill":
        previous = read
        line = "mods.techreborn.wireMill.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "thermal:centrifuge":
        previous = read
        line = "mods.thermalexpansion.Centrifuge.addRecipe("
        inputs = []
        ingredients = []
        for i in range(4):
            item = input("enter item input (enter end to finish): ")
            if item == "end":
                break
            else:
                ingredients.append(item)
        inputs.append(ingredients)
        inputs.append(input("enter item input: "))
        inputs.append(input("enter fluid output: "))
        inputs.append(input("enter energy: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "thermal:compactor":
        previous = read
        read = input("enter type of recipe: coin, plate, gear, misc: ")
        if read == "coin":
            line = "mods.thermalexpansion.Compactor.addMintRecipe("
        elif read == "plate"  :
            line = "mods.thermalexpansion.Compactor.addStorageRecipe("
        elif read == "gear"  :
            line = "mods.thermalexpansion.Compactor.addGearRecipe("
        elif read == "misc"  :
            line = "mods.thermalexpansion.Compactor.addPressRecipe("
        else:
            print("invalid option")
            continue
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter energy: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "thermal:still":
        previous = read
        line = "mods.thermalexpansion.Refinery.addRecipe("
        inputs = []
        inputs.append(input("enter fluid output: "))
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter energy: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "thermal:inductionsmelter":
        previous = read
        line = "mods.thermalexpansion.InductionSmelter.addRecipe("
        inputs = []
        inputs.append(input("enter primary item output: "))
        inputs.append(input("enter primary item input: "))
        inputs.append(input("enter primary item input: "))
        inputs.append(input("enter energy: "))
        read = input("enter y for a secondary item: ")
        if read == "y":
            inputs.append(input("enter secondary item output: "))
            inputs.append(input("enter secondary item chance: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "thermal:magmacrucible":
        previous = read
        line = "mods.thermalexpansion.Crucible.addRecipe("
        inputs = []
        inputs.append(input("enter fluid output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter energy: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "thermal:redstonefurnace":
        previous = read
        line = "mods.thermalexpansion.RedstoneFurnace.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter energy: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "thermal:redstonefurnacepyrolitic":
        previous = read
        line = "mods.thermalexpansion.RedstoneFurnace.addPyrolysisRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter energy: "))
        inputs.append(input("enter mB of Creosote output: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "thermal:pulverizer":
        previous = read
        line = "mods.thermalexpansion.Pulverizer.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter energy: "))
        read = input("enter y for a secondary item: ")
        if read == "y":
            inputs.append(input("enter secondary item output: "))
            inputs.append(input("enter secondary item chance: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "thermal:sawmill":
        previous = read
        line = "mods.thermalexpansion.Sawmill.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter energy: "))
        read = input("enter y for a secondary item: ")
        if read == "y":
            inputs.append(input("enter secondary item output: "))
            inputs.append(input("enter secondary item chance: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        file.write(line)
    elif read == "advrocket:chemicalreactor":
        previous = read
        line = "mods.advancedrocketry.ChemicalReactor.addRecipe("
        inputs = []
        inputs.append(input("enter item or fluid output: "))
        inputs.append(input("enter ticks: "))
        inputs.append(input("enter rf/t: "))
        read = int(input("enter number of inputs:"))
        for i in range(read):
            inputs.append(input("enter item or fluid input: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n\n"
        file.write(line)
file.close()
