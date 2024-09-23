#uplägg
import random #Detta kommer att behövas senare när vi ska börja plocka spelkort senare så att man får ett slumpmässigt kort 





#Här ska klasser först skappas (en överklass för spelet, en för spelare och en för dealer)



#GAMMALT
# class Kort(): #Här skapar jag en def kring hela kortleken
#     def __init__(self, Ess: int = 1 or 14, Kung: int= 13, Drottning: int =12, Knäckt: int = 11)-> None: #Här definneras spelets kort och vad de är värda
#         self.Ess = Ess
#         self.Kung = Kung
#         self.Drottning = Drottning
#         self.Knäckt = Knäckt



class AllaSpelara: #Överklassen
    def __init__(self, poäng:int, kort:int)-> None:
        self.poäng=poäng
        self.kort=kort



class spelare(AllaSpelara): #Här gör vi spelaran med hjälp av överklassen AllaSpelare
    def __init__(self, poäng:int, kort:int)-> None:
        super().__init__(poäng, kort)

class dealer(AllaSpelara): #Här gör vi dealer med hjälp av överklassen AllaSpelare
    def __init__(self, poäng:int, kort:int)-> None:
        super().__init__(poäng, kort)



print('...')