class nuclearcraft:
    @staticmethod
    def alloyfurnace():
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
        return line
    
    @staticmethod
    def centrifuge():
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
        return line
    
    @staticmethod
    def chemicalreactor():
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
        return line
    
    @staticmethod
    def condenser():
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
        return line
    
    @staticmethod
    def crystallizer():
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
        return line
    
    @staticmethod
    def decaygenerator():
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
        return line
    
    @staticmethod
    def decayhastener():
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
        return line
    
    @staticmethod
    def electrolyser():
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
        return line
    
    @staticmethod
    def fission():
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
        return line
    
    @staticmethod
    def fluidenricher():
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
        return line
    
    @staticmethod
    def fluidextractor():
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
        return  line
    
    @staticmethod
    def fuelreprocessor():
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
        return line
    
    @staticmethod
    def fusion():
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
        return line
    
    @staticmethod
    def heatexchanger():
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
        return line
    
    @staticmethod
    def fluidinfuser():
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
        return line
    
    @staticmethod
    def ingotformer():
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
        return line
    
    @staticmethod
    def irradiator():
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
        return line
    
    @staticmethod
    def isotopeseparator():
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
        return line
    
    @staticmethod
    def manufactory():
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
        return line
    
    @staticmethod
    def melter():
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
        return line
    
    @staticmethod
    def pressurizer():
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
        return line
    
    @staticmethod
    def rockcrusher():
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
        return line
    
    @staticmethod
    def saltfission():
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
        return line
    
    @staticmethod
    def saltmixer():
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
        return line
    
    @staticmethod
    def turbine():
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
        return line
    
    @staticmethod
    def supercooler():
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
        return line