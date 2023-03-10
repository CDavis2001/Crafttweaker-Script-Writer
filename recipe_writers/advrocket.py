class advrocket:
    @staticmethod
    def machine_list():
        return ["chemicalreactor", "arcfurnace"]
    
    @staticmethod
    def chemicalreactor():
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
        line = line + ");\n"
        return line
    
    @staticmethod
    def arcfurnace():
        line = "mods.advancedrocketry.ArcFurnace.addRecipe("
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
        line = line + ");\n"
        return line