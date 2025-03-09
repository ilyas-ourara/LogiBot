class Project :
    #constructeur de la classe
    def __init__ (self,etat,niveau,model) :
        self.status=etat 
        self.level=niveau
        self.model=model


    def detection(self,object) :
        if self.model.detect(object)=="obstacle" :
            return "Stop" 
        else :
            return "GO"


        
        