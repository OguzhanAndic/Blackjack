import random #Detta kommer att behövas senare när vi ska börja plocka spelkort senare så att man får ett slumpmässigt kort 

#----------------------------------------------------------------------------------------------------------------------------------------------

Kortlek: tuple = [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(11,'Knäckt'),(12,'Drottning'),(13,'Kung'),('Ess','Ess')]

#----------------------------------------------------------------------------------------------------------------------------------------------
#Här ska klasser först skappas (en överklass för spelet, en för spelare och en för dealer)

class AllaSpelara: #Överklassen
    def __init__(self, poäng:int = 0, )-> None:
        self.poäng=poäng



class Spelare(AllaSpelara): #Här gör vi spelaran med hjälp av överklassen AllaSpelare
    def __init__(self, poäng:int =0 )-> None:
        super().__init__(poäng)

    def Ta_kort(self) -> None:
        Randomkort =random.choice(Kortlek)
        if Randomkort[1] == 'Ess':
            while True:
                print(f'Du drog ett Ess, vilket värde ska den vara? 1 eller 14')
                ValFörVärde = input('välj här: ')
                if ValFörVärde== '1':
                    print(f'Du valde {ValFörVärde}, vilket ger dig {ValFörVärde} poäng')
                    self.poäng += 1
                    break
                elif ValFörVärde== '14':
                    print(f'Du valde {ValFörVärde}, vilket ger dig {ValFörVärde} poäng')
                    self.poäng += 14
                    break
                else:  
                    print('Du måste skriva in ett av de angivna värdena, gör om!')
                    continue
                    
        else:
            print(f'Du drog {Randomkort[1]}, vilket ger dig {Randomkort[0]} poäng')
            self.poäng += Randomkort[0]
    
    def poängkoll(self)->None: 
        print(f'Din nuvarande poäng är {self.poäng}')
    
    def SpelaSpelet(self)->None:
        while True:
            self.poängkoll()
            Player1Val=input('Vill du göra ett till drag? Svara ja eller nej! : ').lower()
            if Player1Val == 'ja':
                self.Ta_kort()
                if self.poäng > 21:
                    print('Du fick mer än 21, du förlorar automatiskt!')
                    break
            elif Player1Val=='nej':
                print(f'Du väljer att stanna, du har totalt {self.poäng} poäng!')
                break
            else:
                print('Du måste skriva något av de följande alternativ: ja eller nej. Frågar igen... ')
                continue



class Dealer(AllaSpelara): #Här gör vi dealer med hjälp av överklassen AllaSpelare
    def __init__(self, poäng:int = 0)-> None:
        super().__init__(poäng)
    
    def Ta_kort(self) -> None:
            # print(f'Dealerns nuvarande poäng är {self.poäng}')
            Randomkort =random.choice(Kortlek)
            if Randomkort[1] == 'Ess':
                while True:
                    print(f'Dealer drog ett Ess, dealern väljer värde mellan 1 och 14...')
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
        print(f'Dealerns nuvarande poäng är {self.poäng}')

    def DealernsPoäng(self)->None:
        print(f'Dealerns nuvarande poäng är {self.poäng}')

    def SpelaSpelet(self)->None:
        while True:
            self.DealernsPoäng()
            if self.poäng <17:
                self.Ta_kort()
                continue
            elif self.poäng >= 17 and not self.poäng > 21:
                print('Dealern stannar!')
                self.poängkoll()
                break
            elif self.poäng > 21:
                print('Dealern har mer än 21')
                break
            self.poängkoll()
            break   


#----------------------------------------------------------------------------------------------------------------------------------------------
#Här körs spelet


def Blackjack()->None:
    while True: 
        Player1: Spelare = Spelare()
        Player1.SpelaSpelet()
        if Player1.poäng > 21:
            print('Du har förlorat spelet för att du fick 21. Dealern vann!')
            break
        Dealer1: Dealer = Dealer()
        Dealer1.SpelaSpelet()
        if Dealer1.poäng > 21:
            print('Dealern har förlorat spelet för att hen fick över 21 poäng. Du vann!')
            break
        else:
            if Player1.poäng == Dealer1.poäng:
                print('Datorn vinner, du måste ha mer för att vinna! House allways wins ;) ')
                break
            elif Player1.poäng > Dealer1.poäng:
                print('Du fick högre än dealern och vinner!')
                break
            elif Player1.poäng < Dealer1.poäng:
                print('Du fick mindre än dealern och förlorar!')
                break

def LoopaBlackjack():
    while True:
        Spela_Eller_Avsluta=input('Vill du spela igen?, svara ja eller nej : ').lower()
        if Spela_Eller_Avsluta=='ja':
            print('startar om Blackjack')
            Blackjack()
            continue
        if Spela_Eller_Avsluta=='nej':
            print('Avslutar programmet')
            break
        else:
            print('Ogiltigt svar, frågar samma fråga igen!')
        continue

def Hela_Programmet()->None:
    while True:
        StartaProgram=input('Vill du sätta igång spelet? : ').lower()
        if StartaProgram== 'ja':
            Blackjack()
            LoopaBlackjack()
            break
        elif StartaProgram=='nej':
            print('Avslutar programmet')
            break
        else:
            print('Ogiltigt svar, frågar användaren igen!')
            continue
        
Hela_Programmet()



#----------------------------------------------------------------------------------------------------------------------------------------------
#Gammalt material som jag inte vill ta bort än









# while True:
#     StartaProgram=input('vill du sätta igång spelet?').lower()
#     if StartaProgram== 'ja':
#         print('Startar BlackJack/21')
#         while True: 
#             Player1: spelare = spelare()
#             Player1.SpelaSpelet()
#             if Player1.poäng > 21:
#                 print('Du har förlorat spelet för att du fick 21. Dealern vann!')
#                 break
#             Dealer1: dealer = dealer()
#             Dealer1.SpelaSpelet()
#             if Dealer1.poäng > 21:
#                 print('Dealern har förlorat spelet för att hen fick 21. Du vann!')
#                 break
#             else:
#                 if Player1.poäng == Dealer1.poäng:
#                     print('Det blev oavgjort')
#                     break
#                 elif Player1.poäng > Dealer1.poäng:
#                     print('Du fick högre än dealern och vinner!')
#                     break
#                 elif Player1.poäng < Dealer1.poäng:
#                     print('Du fick mindre än dealern och förlorar!')
#                     break
#     elif StartaProgram=='nej':
#         print('Avslutar programmet')
#         break
#     else:
#         print('Ogiltigt svar, Frågar Användare igen!')
#         continue







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



















