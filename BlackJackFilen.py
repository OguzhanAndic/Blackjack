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
    def __init__(self, poäng:int = 0, )-> None:
        self.poäng=poäng



class spelare(AllaSpelara): #Här gör vi spelaran med hjälp av överklassen AllaSpelare
    def __init__(self, poäng:int =0, )-> None:
        super().__init__(poäng)

    def Ta_kort(self) -> None:
        print(f'din nuvarande poäng är {self.poäng}')
        Randomkort =random.choice(Kortlek)
        if Randomkort[1] == 'Ess':
            while True:
                print(f'du drog ett Ess, vilket värde ska den vara? 1 eller 14')
                ValFörVärde: int = int(input('välj här: '))
                if ValFörVärde== 1 or ValFörVärde== 14:
                    print(f'du valde {ValFörVärde}, vilket ger dig {ValFörVärde} poäng')
                    self.poäng += ValFörVärde
                    break
                else:
                    print('du har inte gjort ett kortekt val, välj om!')         
        else:
            print(f'du drog {Randomkort[1]}, vilket ger dig {Randomkort[0]} poäng')
            self.poäng += Randomkort[0]
    def poängkoll(self)->None: 
        print(f'din nuvarande poäng är {self.poäng}')




class dealer(AllaSpelara): #Här gör vi dealer med hjälp av överklassen AllaSpelare
    def __init__(self, poäng:int = 0)-> None:
        super().__init__(poäng)
    
    def Ta_kort(self) -> None:
            print(f'dealerns nuvarande poäng är {self.poäng}')
            Randomkort =random.choice(Kortlek)
            if Randomkort[1] == 'Ess':
                while True:
                    print(f'dealer drog ett Ess, dealern väljer värde mellan 1 och 14...')
                    BotVal=random.randint(1,2)
                    if BotVal== 1:
                        print(f'Dealern valde {BotVal}, vilket ger Dealern {BotVal} poäng')
                        self.poäng += BotVal
                        break
                    elif BotVal == 2:
                        print(f'Dealern valde 14, vilket ger Dealern 14 poäng')
                        self.poäng += 14
                        break        
            else:
                print(f'Dealern drog {Randomkort[1]}, vilket ger Dealern {Randomkort[0]} poäng')
                self.poäng += Randomkort[0]
    def poängkoll(self)->None: 
        print(f'din nuvarande poäng är {self.poäng}')



print('...')

#----------------------------------------------------------------------------------------------------------------------------------------------
#Här körs spelet

# Player1: spelare = spelare()

# Player1.Ta_kort()
# Player1.Ta_kort()
# Player1.poängkoll()

# Dealer1: dealer = dealer()

# Dealer1.Ta_kort()
# Dealer1.Ta_kort()
# Dealer1.poängkoll()















#----------------------------------------------------------------------------------------------------------------------------------------------
#Gammalt material som jag inte vill ta bort än

#Temporär plats för att skapa funktioner
# Summa: int= 0
# def Testkort()->None:
#     global Summa
#     Randomkort =random.choice(Kortlek)
#     if Randomkort[1] == 'Ess':
#         while True:
#             print(f'du drog ett Ess, vilket värde ska den vara? 1 eller 14')
#             ValFörVärde: int = int(input('välj här: '))
#             if ValFörVärde== 1 or ValFörVärde== 14:
#                 print(f'du valde {ValFörVärde}, vilket ger dig dig {ValFörVärde} poäng')
#                 Summa += ValFörVärde
#                 break
#             else:
#                 print('du har inte gjort ett kortekt val, välj om!')         
#     else:
#         print(f'du drog {Randomkort[1]}, vilket ger dig {Randomkort[0]} poäng')
#         Summa += Randomkort[0]


# Testkort()
# Testkort()
# print('din summa är ', Summa)



















