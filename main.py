read = ""
file = open("recipes.zs", "a")
supported_machines = ["nuclearcraft:alloyfurnace","nuclearcraft:centrifuge", "nuclearcraft:chemical_reactor", "nuclearcraft:condenser", "nuclearcraft:crystallizer", "nuclearcraft:decaygenerator", "nuclearcraft:decayhastener", "nuclearcraft:electrolyzer", "nuclearcraft:fission", "nuclearcraft:fluidenricher", "nuclearcraft:fluidextractor", "nuclearcraft:fuelreprocessor", "nuclearcraft:fusion", "nuclearcraft:heatexchanger", "nuclearcraft:fluidinfuser", "nuclearcraft:ingotformer", "nuclearcraft:irradiator", "nuclearcraft:isotopeseparator", "nuclearcraft:manufactory", "nuclearcraft:melter", "nuclearcraft:pressurizer", "nuclearcraft:rockcrusher", "nuclearcraft:saltfission", "nuclearcraft:saltmixer", "nuclearcraft:turbine", "nuclearcraft:supercooler", "techreborn:alloysmelter", "techreborn:assemblingmachine", "techreborn:centrifuge", "techreborn:chemicalreactor", "techreborn:compressor", "techreborn:distillationtower", "techreborn:extractor", "techreborn:thermalgen", "techreborn:gasgen", "techreborn:semigen", "techreborn:dieselgen", "techreborn:plasmagen", "techreborn:fluidreplicator", "techreborn:fusionreactor", "techreborn:grinder", "techreborn:implosioncompressor", "techreborn:blastfurnace", "techreborn:electrolyzer", "techreborn:industrialgrinder", "techreborn:industrialsawmill", "techreborn:platebendingmachine", "techreborn:rollingmachine", "techreborn:solidcanningmachine", "techreborn:vacuumfreezer", "techreborn:wiremill"]
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:chemical_reactor":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:condenser":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:crystallizer":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:decaygenerator":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:decayhastener":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:electrolyzer":
        line = "mods.nuclearcraft.electrolyzer.addRecipe(["
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:fission":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:fluidenricher":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:fluidextractor":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:fuelreprocessor":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:fusion":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:heatexchanger":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:fluidinfuser":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:ingotformer":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:irradiator":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:isotopeseparator":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:manufactory":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:melter":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:pressurizer":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:rockcrusher":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:saltfission":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:saltmixer":
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
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:turbine":
        line = "mods.nuclearcraft.turbine.addRecipe(["
        inputs = []
        inputs.append(input("enter fluid input: "))
        inputs.append(input("enter fluid output: "))
        inputs.append(input("enter power per mB: "))
        inputs.append(input("enter double expansio level: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + "]);"
        file.write(line)
    elif read == "nuclearcraft:supercooler":
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
        line = line + "]);"
        file.write(line)
    elif read == "techreborn:alloysmelter":
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
        line = line + ");"
        file.write(line)
    elif read == "techreborn:assemblingmachine":
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
        line = line + ");"
        file.write(line)
    elif read == "techreborn:assemblingmachine":
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
        line = line + ");"
        file.write(line)
    elif read == "techreborn:centrifuge":
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
        line = line + ");"
        file.write(line)
    elif read == "techreborn:chemicalreactor":
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
        line = line + ");"
        file.write(line)
    elif read == "techreborn:compressor":
        line = "mods.techreborn.compressor.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");"
        file.write(line)
    elif read == "techreborn:distillationtower":
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
        line = line + ");"
        file.write(line)
    elif read == "techreborn:extractor":
        line = "mods.techreborn.extractor.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");"
        file.write(line)
    elif read == "techreborn:thermalgen":
        line = "mods.techreborn.fluidGen.addThermalFluid("
        inputs = []
        inputs.append(input("enter fluid fuel: "))
        inputs.append(input("enter power in EU per mB (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");"
        file.write(line)
    elif read == "techreborn:gasgen":
        line = "mods.techreborn.fluidGen.addGasFluid("
        inputs = []
        inputs.append(input("enter fluid fuel: "))
        inputs.append(input("enter power in EU per mB (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");"
        file.write(line)
    elif read == "techreborn:semigen":
        line = "mods.techreborn.fluidGen.addSemiFluid("
        inputs = []
        inputs.append(input("enter fluid fuel: "))
        inputs.append(input("enter power in EU per mB (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");"
        file.write(line)
    elif read == "techreborn:dieselgen":
        line = "mods.techreborn.fluidGen.addDieselFluid("
        inputs = []
        inputs.append(input("enter fluid fuel: "))
        inputs.append(input("enter power in EU per mB (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");"
        file.write(line)
    elif read == "techreborn:plasmagen":
        line = "mods.techreborn.fluidGen.addPlasmaFluid("
        inputs = []
        inputs.append(input("enter fluid fuel: "))
        inputs.append(input("enter power in EU per mB (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");"
        file.write(line)
    elif read == "techreborn:fluidreplicator":
        line = "mods.techreborn.fluidReplicator.addRecipe("
        inputs = []
        inputs.append(input("enter int input: "))
        inputs.append(input("enter liquid output: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");"
        file.write(line)
    elif read == "techreborn:fusionreactor":
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
        line = line + ");"
        file.write(line)
    elif read == "techreborn:grinder":
        line = "mods.techreborn.grinder.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");"
        file.write(line)
    elif read == "techreborn:implosioncompressor":
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
        line = line + ");"
        file.write(line)
    elif read == "techreborn:blastfurnace":
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
        line = line + ");"
        file.write(line)
    elif read == "techreborn:electrolyzer":
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
        line = line + ");"
        file.write(line)
    elif read == "techreborn:industrialgrinder":
        line = "mods.techreborn.industrialGrinder.addRecipe("
        read = input("enter y for a recipe with a fluid")
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
        line = line + ");"
        file.write(line)
    elif read == "techreborn:industrialsawmill":
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
        line = line + ");"
        file.write(line)
    elif read == "techreborn:platebendingmachine":
        line = "mods.techreborn.plateBendingMachine.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");"
        file.write(line)
    elif read == "techreborn:rollingmachine":
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
        line = line + ");"
        file.write(line)
    elif read == "techreborn:solidcanningmachine":
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
        line = line + ");"
        file.write(line)
    elif read == "techreborn:vacuumfreezer":
        line = "mods.techreborn.vacuumFreezer.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");"
        file.write(line)
    elif read == "techreborn:wiremill":
        line = "mods.techreborn.wireMill.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter tick time: "))
        inputs.append(input("enter power in EU (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");"
        file.write(line)
file.close()
