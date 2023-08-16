import enterobacteriaceae_domain as Enterobacteriaceae

class Citrobacter(Enterobacteriaceae):
    def __init__(self, name, activity, bacillus, infection):
        super.__init__(name)
        self.name = name
        self.activity = "mobile"
        self.bacillus = "gram_negative"
        self.infection = "opportunistic"
