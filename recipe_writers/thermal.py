class thermal:
    @staticmethod
    def machine_list():
        return ["centrifuge", "compactor", "still", "inductionsmelter", "magmacrucible", "redstonefurnace", "redstonefurnacepyrolitic", "pulverizer", "sawmill"]
        
    @staticmethod
    def centrifuge():
        line = "mods.thermalexpansion.Centrifuge.addRecipe("
        inputs = []
        ingredients = []
        for i in range(4):
            item = input("enter item ouput " + str(i+1) + ": ")
            inputs.append(item)
        inputs.append(input("enter item input: "))
        inputs.append(input("enter fluid output: "))
        inputs.append(input("enter energy: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        return line
    
    @staticmethod
    def compactor():
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
            return
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter energy: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        return line
    
    @staticmethod
    def still():
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
        return line
    
    @staticmethod
    def inductionsmelter():
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
        return line
    
    @staticmethod
    def magmacrucible():
        line = "mods.thermalexpansion.Crucible.addRecipe("
        inputs = []
        inputs.append(input("enter fluid output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter energy: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        return line
    
    @staticmethod
    def redstonefurnace():
        line = "mods.thermalexpansion.RedstoneFurnace.addRecipe("
        inputs = []
        inputs.append(input("enter item output: "))
        inputs.append(input("enter item input: "))
        inputs.append(input("enter energy: "))
        for text in inputs:
            line = line + text + ", "
        line = line[:-2]
        line = line + ");\n"
        return line
    
    @staticmethod
    def redstonefurnacepyrolitic():
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
        return line
    
    @staticmethod
    def pulverizer():
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
        return line
    
    @staticmethod
    def sawmill():
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
        return line