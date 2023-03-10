class modularmachinery:
    @staticmethod
    def add():
        recipeName = input("Enter recipe registry name: ")
        machineName = input("Enter machine registry name: ")
        time = input("Enter tick Processing Time: ")
        line1 = "val temp = mods.modularmachinery.RecipeBuilder.newBuilder(\"" + recipeName + "\", \"" + machineName + "\", " + time + ");\n"
        inputs = input("Enter number of item inputs: ")
        outputs = input("Enter number of item outputs: ")
        finputs = input("Enter number of fluid inputs: ")
        foutputs = input("Enter number of fluid outputs: ")
        line2 = "temp"
        for i in range(int(inputs)):
            read = input("Enter item input: ")
            line2 = line2 + ".addItemInput(" + read + ")"
        for i in range(int(outputs)):
            read = input("Enter item output: ")
            line2 = line2 + ".addItemOutput(" + read + ")"
        for i in range(int(finputs)):
            read = input("Enter fluid input: ")
            line2 = line2 + ".addFluidInput(" + read + ")"
        for i in range(int(foutputs)):
            read = input("Enter fluid output: ")
            line2 = line2 + ".addFluidOutput(" + read + ")"
        read = input("Enter energy per tick: ")
        line2 = line2 + ".addEnergyPerTickInput(" + read + ").build();\n"
        return line1 +  "\n" + line2