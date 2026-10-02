import numpy as np
import matplotlib.pyplot as plt
class Noeud:
    def __init__(self,val,enfants):
        self.val=val
        self.enfants=enfants
        if (self.enfants==None):
            self.enfants=[]

    def ajout_noeud(self,noeud):
        if not isinstance(noeud,Noeud):
             TypeError("Le paramètre n'est pas de type noeud")
        self.enfants.append(noeud)

    def afficher(self,):
        res=str(self.val)
        for enfant in self.enfants:
             res+=" "+enfant.afficher()
        return res

    def evaluer(self, variables):
        if isinstance(self.val, (int, float)):
            return self.val
        if self.val not in ["+", "-", "*"]:
            if self.val in variables:
                return variables[self.val]
            raise ValueError(
                "La variable " + self.val + " n'a pas de valeur"
            )
        if self.val == "+":
            return (
                self.enfants[0].evaluer(variables)
                + self.enfants[1].evaluer(variables)
            )
        elif self.val == "-":
            return (
                self.enfants[0].evaluer(variables)
                - self.enfants[1].evaluer(variables)
            )
        elif self.val == "*":
            return (
                self.enfants[0].evaluer(variables)
                * self.enfants[1].evaluer(variables)
            )
        raise ValueError("Opérateur/noeud inconnu")

    def tracer(self, variable, valeurs):
        resultats = []
        for valeur in valeurs:
            variables = {variable: valeur}
            resultats.append(self.evaluer(variables))
        plt.plot(valeurs, resultats)
        plt.xlabel(variable)
        plt.ylabel("f(" + variable + ")")
        plt.grid()
        plt.show()
                             
                        

racine=Noeud("+",None)
racine.ajout_noeud(Noeud(2,None))
racine.ajout_noeud(Noeud(3,None))
#print(racine.enfants)
print(racine.afficher())
print(racine.evaluer({}))

racine = Noeud("*",None)

racine.ajout_noeud(Noeud("x",None))
racine.ajout_noeud(Noeud("x",None))
valeurs = [-2, -1, 0, 1, 2]
racine.tracer("x", valeurs)


