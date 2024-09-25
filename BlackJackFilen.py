#uplägg
import random #Detta kommer att behövas senare när vi ska börja plocka spelkort senare så att man får ett slumpmässigt kort 

#----------------------------------------------------------------------------------------------------------------------------------------------
# Kung: int = 13
# Drottning:int = 12
# Knäckt: int = 11
# Ess:int= '' #här behövs en placeholder för att spelaren och dealern senare ska kunna 


Kortlek: tuple = [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(11,'Knäckt'),(12,'Drottning'),(13,'Kung'),('Ess','Ess')]

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
Summa: int= 0
def Testkort()->None:
    global Summa
    Randomkort =random.choice(Kortlek)
    if Randomkort[1] == 'Ess':
        while True:
            print(f'du drog ett Ess, vilket värde ska den vara? 1 eller 14')
            ValFörVärde: int = int(input('välj här: '))
            if ValFörVärde== 1 or ValFörVärde== 14:
                print(f'du valde {ValFörVärde}, vilket ger dig dig {ValFörVärde} poäng')
                Summa += ValFörVärde
                break
            else:
                print('du har inte gjort ett kortekt val, välj om!')         
    else:
        print(f'du drog {Randomkort[1]}, vilket ger dig {Randomkort[0]} poäng')
        Summa += Randomkort[0]


Testkort()
Testkort()
print('din summa är ', Summa)



















