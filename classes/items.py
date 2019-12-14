

class items(object):

    def __init__(self, name, work, quentity, tpe, dmg):
        self.name = name
        self.work = work
        self.quentity = quentity
        self.tpe = tpe
        self.dmg = dmg
    
    def qn_update(self):
        self.quentity -= 1

    

