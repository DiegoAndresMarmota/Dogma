class Bacterium:
    def __init__(self, shell, appendage, bacterial_nucleus, endospore):
        self.shell = shell
        self.appendage = appendage
        self.bacterial_nucleus = bacterial_nucleus
        self.endospore = endospore
        
class Shell(Bacterium):
    def __init__(self, capsule, membrane_exterior):
        super().__init__(self.shell)
        self.capsule = capsule
        self.membrane_exterior = membrane_exterior

    def capsule(self):
        capsule = {
        0 : "polisacaride",
        1 : "polipeptide"
        }
        if capsule == 0:
            return "polisacaride"
        elif capsule == 1:
            return "polipeptide"
        else: "please, introduce a valid number"
    
    def membrane_exterior(self):
        membrane_exterior = {
        0 : "protein, fosfolipide, lipopolisacaride",
        1 : "peptideglucan",
        2 : "protein, oligosacaride",
        3 : "protein, fosfolipide"
        }
        if membrane_exterior == 0:
            return "protein, fosfolipide, lipopolisacaride"
        elif membrane_exterior == 1:
            return "peptideglucan"
        elif membrane_exterior == 2:
            return "protein, oligosacaride"
        elif membrane_exterior == 3:
            return "protein, fosfolipide"
        else: "please, introduce a valid number"

        
class Appendage(Bacterium):
    def __init__(self, pili, flagella):
        super().__init__(self.appendage)
        self.pili = pili
        self.flagella = flagella
        
    def pili(self):
        pili = {
        0 : "protein",
        1 : "no protein"
        }
        if pili == 0:
            return "protein"
        elif pili == 1:
            return "no protein"
        else: "please, introduce a valid number"
            
    def flagella(self):
        flagella = {
        0 : "protein with flageline",
        1 : "protein not flageline"
        }
        if flagella == 0:
            return "protein with flageline"
        elif flagella == 1:
            return "protein not flageline"
        else: "please, introduce a valid number"
        
        
class Bacterial_Nucleus(Bacterium):
    def __init__(self, cytoplasm, nucleus, plasmid):
        super().__init__(self.bacterial_nucleus)
        self.cytoplasm = cytoplasm
        self.nucleus = nucleus
        self.plasmid = plasmid
        
        
class Endospore(Bacterium):
    def __init__(self, endosymbiont, endosymbiont_cell, endosymbiont_membrane):
        super().__init__(self.endospore)
        self.endosymbiont = endosymbiont
        self.endosymbiont_cell = endosymbiont_cell
        self.endosymbiont_membrane = endosymbiont_membrane
        
        