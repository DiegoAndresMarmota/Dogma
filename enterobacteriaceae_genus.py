import enterobacteriaceae_class as Enterobacteriaceae


class Genus(Enterobacteriaceae):
    def __init__(self, monodermic, didermic):
        super().__init__()
        self.monodermic = monodermic
        self.didermic = didermic
        return Genus


class Monodermic(Genus):
    def __init__(self, actinobacteria, chloroflexi, firmicutes):
        super().__init__()
        self.actinobacteria = actinobacteria
        self.chloroflexi = chloroflexi
        self.firmicutes = firmicutes
        return Monodermic


class Didermic(Genus):
    def __init__(self, aquificae, armatimonadetes, atribacteria, bacteroidetes,
                caldiserica, chlamydiae, cyanobacteria, coprothermobacterota,
                deinococcus_thermus, dictyoglomi, elusimicrobia,
                fibrobacteres, fusobacteria, gemmatimonadetes,
                patescibacteria, planctomycetes, proteobacteria, spirochaetes,
                synergistetes, thermodesulfobacteriota, thermotogae,
                verrucomicrobia):
        self.aquificae = aquificae
        self.armantimonadetes = armatimonadetes
        self.atribacteria = atribacteria
        self.bacteroidetes = bacteroidetes
        self.caldiserica = caldiserica
        self.chlamydiae = chlamydiae
        self.cyanobacteria = cyanobacteria
        self.coprothermobacterota = coprothermobacterota
        self.deinococcus_thermus = deinococcus_thermus
        self.dictyoglomi = dictyoglomi
        self.elusimicrobia = elusimicrobia
        self.fibrobacteres = fibrobacteres
        self.fusobacteria = fusobacteria
        self.gemmatimonadetes = gemmatimonadetes
        self.patescibacteria = patescibacteria
        self.planctomycetes = planctomycetes
        self.proteobacteria = proteobacteria
        self.spirochaetes = spirochaetes
        self.synergistetes = synergistetes
        self.thermodesulfobacteriota = thermodesulfobacteriota
        self.thermotogae = thermotogae
        self.verrucomicrobia = verrucomicrobia
        return Didermic


class Form(Enterobacteriaceae):
    def __init__(self, cocci, bacilli, budding, others_form):
        super().__init__()
        self.cocci = cocci
        self.bacilli = bacilli
        self.budding = budding
        self.others_form = others_form
        return Form


class Cocci(Form):
    def __init__(self, coccus, diplococci, diplococci_encapsulated,
                staphylococci, streptococci, sarcina, tetrad):
        super().__init__()
        self.coccus = coccus
        self.diplococci = diplococci
        self.diplococci_encapsulated = diplococci_encapsulated
        self.staphylococci = staphylococci
        self.streptococci = streptococci
        self.sarcina = sarcina
        self.tetrad = tetrad
        return Cocci


class Bacilli(Form):

    def __init__(self, coccobacillus, bacillus, diplobacilli, palisades,
                streptobacilli):
        super().__init__()
        self.coccobacillus = coccobacillus
        self.bacillus = bacillus
        self.diplobacilli = diplobacilli
        self.palisades = palisades
        self.streptobacilli = streptobacilli
        return Bacilli


class Budding(Form):
    def __init__(self, hypha, stalk):
        super().__init__()
        self.hypha = hypha
        self.stalk = stalk
        return Budding


class Others_Form(Form):
    def __init__(self, enlarged_rod, vibrio, comma_form, club_rod,
                helical_form, corkscrew, filamentous, spirochete):
        super().__init__()
        self.enlarged_rod = enlarged_rod
        self.vibrio = vibrio
        self.comma_form = comma_form
        self.club_form = club_rod
        self.helical_form = helical_form
        self.corkscrew = corkscrew
        self.filamentous = filamentous
        self.spirochete = spirochete
        return Others_Form
