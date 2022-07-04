class Account:

    def __init__(self, exp, r, c, p):
        self.experience = exp
        self.rating = r
        self.confidence = c
        self.pricing = p

    experience = 0
    rating = 0
    confidence = 0
    pricing = 0


class Task:

    def __init__(self, exp, r, c, p, relv):
        self.experience_modififer = exp
        self.relevance = relv
        self.rating_mod = r
        self.confidence_mod = c
        self.pricing_mod = p

    experience_modififer = 0
    rating_mod = 0
    confidence_mod = 0
    pricing_mod = 0


class Classification(Account, Task):
    def __init__(self, name, exp, r, c, p, exp_mod, rmod, pmod, cmod, relvmod):
        Account.__init__(self, exp, r, c, p)
        Task.__init__(self, exp_mod, rmod, cmod,pmod, relvmod)
        self.name = name
        self.score = 0
