class techreborn:
    @staticmethod
    def alloysmelter():
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
        return line
    
    @staticmethod
    def assemblingmachine():
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
        return line
    
    @staticmethod
    def centrifuge():
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
        return line
    
    @staticmethod
    def chemicalreactor():
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
        return line
    
    @staticmethod
    def compressor():
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
        return line
    
    @staticmethod
    def distillationtower():
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
        return line
    
    @staticmethod
    def extractor():
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
        return line
    
    @staticmethod
    def thermalgen():
        line = "mods.techreborn.fluidGen.addThermalFluid("
        inputs = []
        inputs.append(input("enter fluid fuel: "))
        inputs.append(input("enter power in EU per mB (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        return line
    
    @staticmethod
    def gasgen():
        line = "mods.techreborn.fluidGen.addGasFluid("
        inputs = []
        inputs.append(input("enter fluid fuel: "))
        inputs.append(input("enter power in EU per mB (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        return line
    
    @staticmethod
    def semigen():
        line = "mods.techreborn.fluidGen.addSemiFluid("
        inputs = []
        inputs.append(input("enter fluid fuel: "))
        inputs.append(input("enter power in EU per mB (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        return line
    
    @staticmethod
    def dieselgen():
        line = "mods.techreborn.fluidGen.addDieselFluid("
        inputs = []
        inputs.append(input("enter fluid fuel: "))
        inputs.append(input("enter power in EU per mB (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        return line
    
    @staticmethod
    def plasmagen():
        line = "mods.techreborn.fluidGen.addPlasmaFluid("
        inputs = []
        inputs.append(input("enter fluid fuel: "))
        inputs.append(input("enter power in EU per mB (1EU = 4RF): "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        return line
    
    @staticmethod
    def fluidreplicator():
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
        return line
    
    @staticmethod
    def fusionreactor():
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
        return line
    
    @staticmethod
    def grinder():
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
        return line
    
    @staticmethod
    def implosioncompressor():
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
        return line
    
    @staticmethod
    def blastfurnace():
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
        return line
    
    @staticmethod
    def electrolyzer():
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
        return line
    
    @staticmethod
    def industrialgrinder():
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
        return line
    
    @staticmethod
    def industrialsawmill():
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
        return line
    
    @staticmethod
    def platebendingmachine():
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
        return line
    
    @staticmethod
    def rollingmachine():
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
        return line
    
    @staticmethod
    def solidcanningmachine():
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
        return line
    
    @staticmethod
    def vacuumfreezer():
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
        return line
    
    @staticmethod
    def wiremill():
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
        return line