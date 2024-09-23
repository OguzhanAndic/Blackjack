#uplägg
import random #Detta kommer att behövas senare när vi ska börja plocka spelkort senare så att man får ett slumpmässigt kort 

#----------------------------------------------------------------------------------------------------------------------------------------------
Kung: int = 13
Drottning:int = 12
Knäckt: int = 11
Ess:int= '' #här behövs en placeholder för att spelaren och dealern senare ska kunna 


Kortlek: list = [1,2,3,4,5,6,7,8,9,Kung,Drottning,Knäckt,Ess]

print(Kortlek)

#----------------------------------------------------------------------------------------------------------------------------------------------

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
    def __init__(self, poäng:int, kort:int, )-> None:
        super().__init__(poäng, kort)

    # def DraKort() -> None:





class dealer(AllaSpelara): #Här gör vi dealer med hjälp av överklassen AllaSpelare
    def __init__(self, poäng:int, kort:int)-> None:
        super().__init__(poäng, kort)



print('...')

#----------------------------------------------------------------------------------------------------------------------------------------------

#Temporär plats för att skapa funktioner

def Testkort()->None:
    randomnmr=random.randint(0,12)
    kortlek=randomnmr
    print(f'du drog  {kortlek} vilket ger {kortlek}')
    

Testkort()




















