class Bacterium:
    def __init__(self, shell, appendage, bacterial_nucleus, endospore):
        if isinstance(shell, Shell) and isinstance(appendage, Appendage) and isinstance(bacterial_nucleus, bacterial_nucleus) and isinstance(endospore, Endospore):
            self.shell = shell
            self.appendage = appendage
            self.bacterial_nucleus = bacterial_nucleus
            self.endospore = endospore
            if isinstance(shell, bool):
                self.shell = True
            if isinstance(appendage, bool):
                self.appendage = True
            if isinstance(bacterial_nucleus, bool):
                self.bacterial_nucleus = True
            if isinstance(endospore, bool):
                self.endospore = True
        
        
class Shell(Bacterium):
    def __init__(self, capsule, membrane_exterior):
        super().__init__(self.shell)
        if isinstance(capsule, dict):
            self.capsule = capsule
        if isinstance(membrane_exterior, dict):
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
        if isinstance(pili, dict(int, str)):
            self.pili = pili
        if isinstance(flagella, dict(int, str)):
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
        if isinstance(cytoplasm, dict(int, str)):
            self.cytoplasm = cytoplasm
        if isinstance(nucleus, dict(int, str)):
            self.nucleus = nucleus
        if isinstance(plasmid, dict(int, str)):
            self.plasmid = plasmid
            
    def cytoplasm(self):
        cytoplasm = {
        0 : "protein",
        1 : "no protein"
        }
        if cytoplasm == 0:
            return "protein"
        elif cytoplasm == 1:
            return "no protein"
        else: "please, introduce a valid number"
    
    def nucleus(self):
        nucleus = {
        0 : "protein",
        1 : "no protein"
        }
        if nucleus == 0:
            return "protein"
        elif nucleus == 1:
            return "no protein"
        else: "please, introduce a valid number"
        
    def plasmid(self):
        plasmid = {
        0 : "protein",
        1 : "no protein"
        }
        if plasmid == 0:
            return "protein"
        elif plasmid == 1:
            return "no protein"
        else: "please, introduce a valid number"
        
        
class Endospore(Bacterium):
    def __init__(self, endosymbiont, endosymbiont_cell, endosymbiont_membrane):
        super().__init__(self.endospore)
        if isinstance(endosymbiont, dict(int, str)):
            self.endosymbiont = endosymbiont
        if isinstance(endosymbiont_cell, dict(int, str)):
            self.endosymbiont_cell = endosymbiont_cell
        if isinstance(endosymbiont_membrane, dict(int, str)):
            self.endosymbiont_membrane = endosymbiont_membrane
    
    def endosymbiont(self):
        endosymbiont = {
        0 : "protein",
        1 : "no protein"
        }
        if endosymbiont == 0:
            return "protein"
        elif endosymbiont == 1:
            return "no protein"
        else: "please, introduce a valid number"
        
    def endosymbiont_cell(self):
        endosymbiont_cell = {
        0 : "protein",
        1 : "no protein"
        }
        if endosymbiont_cell == 0:
            return "protein"
        elif endosymbiont_cell == 1:
            return "no protein"
        else: "please, introduce a valid number"
        
    def endosymbiont_membrane(self):
        endosymbiont_membrane = {
        0 : "protein",
        1 : "no protein"
        }
        if endosymbiont_membrane == 0:
            return "protein"
        elif endosymbiont_membrane == 1:
            return "no protein"
        else: "please, introduce a valid number"