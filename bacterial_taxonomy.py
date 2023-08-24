class Bacterial_taxonomy():
    def __init__(self, life, domain, kingdom, phylum, classs, order, family, genus, species):
        super().__init__()
        self.life = life(Life)
        self.domain = domain(Domain)
        self.kingdom = kingdom(Kingdom)
        self.phylum = phylum(Phylum)
        self.classs = classs(Classs)
        self.order = order(Order)
        self.family = family(Family)
        self.genus = genus(Genus)
        self.species = species(Species)
        return Bacterial_taxonomy


class Life(Bacterial_taxonomy):
    def __init__(self, non_cellular_life, cellullar_life):
        super().__init__()
        self.non_cellullar_life = non_cellular_life
        self.cellullar_life = cellullar_life(Domain)
        return Life


class Domain(Bacterial_taxonomy):
    def __init__(self, bacteria, ):
        super().__init__()
        self.bacterial = bacteria
        return Domain


class Kingdom(Bacterial_taxonomy):
    def __init__(self):
        super().__init__()
        pass


class Phylum(Bacterial_taxonomy):
    def __init__(self, name, group):
        super().__init__()
        self.name = name
        self.group = group
        pass


class Classs(Bacterial_taxonomy):
    def __init__(self):
        super().__init__()
        pass


class Order(Bacterial_taxonomy):
    def __init__(self):
        super().__init__()
        pass


class Family(Bacterial_taxonomy):
    def __init__(self):
        super().__init__()
        pass


class Genus(Bacterial_taxonomy):
    def __init__(self):
        super().__init__()
        pass


class Species(Bacterial_taxonomy):
    def __init__(self):
        super().__init__()
        pass