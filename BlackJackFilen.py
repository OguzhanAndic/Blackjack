#När du läser kommentarer så refererar kommentaren alltid 1 steg upp. Exempel:
    #TEST
    #Den här kommentaren refererar ett steg upp, vilket blir kommentaren som det står "TEST" på

import random 
#Detta kommer att behövas senare när vi ska börja plocka spelkort senare så att man får ett slumpmässigt kort 


kortlek: tuple = [(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(11,'Knäckt'),(12,'Drottning'),(13,'Kung'),('Ess','Ess')] 
#Här är alla kort som kommer att användas i programmet inuti en tuple. I varje parantes är först värdet av ett kort, och sedan kommer kortets namn. Den enda variabeln som inte har ett värde är Ess. Detta har jag lämnat med flit som en str för att senare ge möjligheten för användaren att göra valet mellan 1 och 14 om de skulle dra Ess.


class AllaSpelara: 
#Här börjar huvudklassen. Det finns två subklasser som kommer att göra olika saker, men båda subklasserna delar en gemensam sak. Båda behöver ha en egen poäng (dvs egna attributs som räknar hur mycket deras värde är från kortleken).
    def __init__(self, poäng:int = 0, )-> None:
    #(här tilldelas attributsen, och retyrtypen None: eftersom att programmet inte ska returnera något till oss)
        self.poäng=poäng
        #Klassen säger att poäng är klassens egna poäng



class Spelare(AllaSpelara): 
#Här gör vi klassen för spelaren med hjälp av överklassen AllaSpelare
    def __init__(self, poäng:int =0 )-> None: 
    #Samma attributes som innan eftersom att atributsen som dealer och spelaren använder kommer att behövas för att hålla koll på poäng varje runda
        super().__init__(poäng) 
        #Refererar till Huvudklassen så att variabeln poäng funkar på samma sätt som ovan. Då blir alltså poäng precis som innan self.poäng=poäng

    def Ta_kort(self) -> None: 
    #Här är metoden för att spelaren ska kunna ta ett kort från kortleken
        randomkort: tuple =random.choice(kortlek)
        #Först använder vi random choice från random modulen för att kunna plocka ett slumpmässigt kort för att senare lägga in detta kort i den nya tuplen Randomkort
        if randomkort[1] == 'Ess':
        #Nu kommer första if satsen, om du skulle få kortet Ess
            while True:
            #Här startar en loop fram för att spelaren ska vara tvungen att välja ett värde, gör spelaren inte det eller försöker ge ett svar som inte är rimligt så kommer spelaren vara kvar i loopen
                print(f'Du drog ett Ess, vilket värde ska den vara? 1 eller 14')
                #En print som ger frågan om Esset ska vara värt 1 eller 14
                ValFörVärde: str = input('Välj här: ')
                #En input till variabeln  Valförvärde, här ska spelaren stoppa in sifran 1 eller 14 (som en string).
                if ValFörVärde== '1':
                #En till if sats som är om spelaren skrev 1
                    print(f'Du valde {ValFörVärde}, vilket ger dig {ValFörVärde} poäng')
                    #Talar om för spelaren vad de valde för värde och hur mycket poäng det motsvarar.
                    self.poäng += 1
                    #lägger till 1 poäng i spelarens nuvarnade poängräknare
                    break
                    #bryter sig ut ur loopen
                elif ValFörVärde== '14':
                #En till if sats som är om spelaren skrev 1
                    print(f'Du valde {ValFörVärde}, vilket ger dig {ValFörVärde} poäng')
                    #Talar om för spelaren vad de valde för värde och hur mycket poäng det motsvarar.
                    self.poäng += 14
                    #Lägger till 14 poäng i spelarens nuvarnade poängräknare
                    break
                    #Bryter sig ut ur loopen
                else:  
                #En else sats som gör ifall spelaren inte skriver 1 eller 14
                    print('Du måste skriva in ett av de angivna värdena, Frågar om samma fråga!')
                    #En print som förklarar att spelaren gjort fel och ska svara om på frågan
                    continue            
                    #tar spelaren tillbaka till början av loopen, vilket blir att spelaren måste svara på om värdet ska vara 1 eller 14 på ditt Ess
        else:
        #En else sats som gör följande om spelaren inte drog ett Ess
            print(f'Du drog {randomkort[1]}, vilket ger dig {randomkort[0]} poäng')
            #en print som visar vilket kort spelaren drog och vad den hadde för värde (notera att namnet på kortet är [1] och värdet är [0])
            self.poäng += randomkort[0]
            #Lägger till kortets värde (Randomkort[0]) in i poängräknaren
    
    def poängkoll(self)->None: 
    #En metod som är till för att snabbt printa ut vad för poäng spelaren har vid den tidpunkten 
        print(f'Din nuvarande poäng är {self.poäng}\n')
        #printen som säger hur mycket poäng spelaren har
    
    def SpelareSpelaSpelet(self)->None:
    #En metod för att spelaren ska kunna spela sin del av spelet (dealern får sin egna metod för att spela)
        while True:
        #En loop som gör att du alltid börjar med att se hur mycket poäng du har sammanlagt innan du gör ett aktivt val
            self.poängkoll()
            #Här är metoden poängkoll lagd för att man alltid ska börja med att se vad spelaren har för poäng
            Player1Val=input('Vill du göra ett till drag? Svara ja eller nej! : ').lower()
            #Player1Val Inputen som spelaren har för att kunna välja om hen ska dra ett kort eller stanna. 
            if Player1Val == 'ja':
            #Ifsats för om spelaren vill ha ett till kort
                self.Ta_kort()
                #Här används den tidigare metoden för att dra ett kort från kortleken
                if self.poäng > 21:
                #En ifsats som gör att om spelaren skulle ha mer än 21 efter att ha dragit kortet, detta för att du automatikst ska förlora vid 21. 
                    print('Du fick mer än 21, du kan inte dra fler kort!')
                    #En print som säger att du inte kan dra fler kort eftersom du har mer än 21
                    break
                    #en break som tar ut dig ur loopen
            elif Player1Val == 'nej':
            #Elif sats om spelaren väljer nej som sitt alternativ
                print(f'Du väljer att stanna, du har totalt {self.poäng} poäng!')
                #Prints som säger att du stannar och hur mycket poäng du har totalt
                break
                #En break som tar ut dig ur loopen
            else:
            #En else sats som ger dig följande konsekvenser om du inte väljer ja eller nej
                print('Du måste skriva något av de följande alternativ: ja eller nej. Frågar igen... ')
                #En prints som förklarar att spelaren har gjort ett felaktigt val och att frågan kommer igen
                continue
                #Forsätter loopa och går därmed tillbaka till början av loopen. Där ställs samma fråga igen efter att du fått se din nuvarande poäng.



class Dealer(AllaSpelara): 
#Här gör vi klassen för dealern med hjälp av överklassen AllaSpelare
    def __init__(self, poäng:int = 0)-> None:
    #Samma attributes som innan eftersom att atributsen som dealer och spelaren använder kommer att behövas för att hålla koll på poäng varje runda
        super().__init__(poäng)
        #Refererar till Huvudklassen så att variabeln poäng funkar på samma sätt som ovan. Då blir alltså poäng precis som innan self.poäng=poäng
    
    def Ta_kort(self) -> None:
    #Här är metoden för att Dealern ska kunna ta ett kort från kortleken
            randomkort: tuple = random.choice(kortlek)
            #Först använder vi random choice från random modulen för att kunna plocka ett slumpmässigt kort för att senare lägga in detta kort i den nya tuplen Randomkort
            if randomkort[1] == 'Ess':
            #Nu kommer första if satsen, om dealern skulle få kortet Ess
                while True:
                #Här startar en loop fram för att dealern ska vara tvungen att välja ett värde ifall dealern drar kortet Ess
                    print(f'Dealer drog ett Ess, dealern väljer värde mellan 1 och 14...')
                    #En print som säger att dealern drog ett Ess och ska välja värdet på kortet
                    botVal=random.randint(1,2)
                    #Här gör Dealern ett val genoma att dra en slumpmässig siffra mellan 1 och 2, för att sedan lagra informationen i Variabeln BotVal1
                    if botVal== 1:
                    #En if sats om siffran som valts var 1
                        print(f'Dealern valde {botVal}, vilket ger Dealern {botVal} poäng')
                        #En print som säger vad boten valt (1) och hur mycket värdet är 
                        self.poäng += botVal
                        #Lägger in kortets värde i poängräknaren
                        break
                        #bryter sig ur loopen (notera att den bryter inte ut sig ur hela loopen utan endast den loopen som hanterar om dealern får ett Ess)
                    elif botVal == 2:
                    #En if sats om siffran som valts var 2
                        print(f'Dealern valde 14, vilket ger Dealern 14 poäng')
                        #En print som säger vad boten valt (2) och hur mycket värdet
                        self.poäng += 14
                        #Lägger in kortets värde i poängräknaren
                        break  
                        #bryter sig ur loopen (notera att den bryter inte ut sig ur hela loopen utan endast den loopen som hanterar om dealern får ett Ess)      
            else:
            #En else sats som gör följande om dealern får något annat kort än Ess
                print(f'Dealern drog {randomkort[1]}, vilket ger Dealern {randomkort[0]} poäng')
                #En print som talar om vad dealern drog för kort (Randomkort[1]) och vilket värde den ger (Randomkort[0])
                self.poäng += randomkort[0]
                #Lägger in det dragna kortets värde i dealerns poängräknare

    def DealernsPoäng(self)->None:
    #En metod som kollar Dealerns nuvarande totala poäng
        print(f'\nDealerns nuvarande poäng är {self.poäng}')
        #Print som visar hur mycket poäng dealern har

    def DealerSpelarSpelet(self)->None:
    #en metod som används av dealern för att spela sin del av rundan
        while True:
        #loopar spelet för dealern tills dealern har nått vissa brytpuntker
            self.DealernsPoäng()
            #här visas dealerns poäng genom vald metod
            if self.poäng <17:
            #if sats för om dealern har mindre än 17 poäng
                self.Ta_kort()
                #dealern drar ett till kort genom ta kort metoden
                continue
                #forsätter att loopa
            elif self.poäng >= 17 and not self.poäng > 21:
            #elif sats om dealern har minst 17 poäng och inte har mer än 21 poäng
                print('Dealern stannar!')
                #prints som säger att dealern ska stanna
                # self.DealernsPoäng()
                # #visar dealerns poäng med DealernsPoäng metoden
                break
                #bryter loopen med en break
            elif self.poäng > 21:
            # elif sats som gör följande om dealerns har mer än 21 i poäng
                print('Dealern har mer än 21 poäng')
                #printar att dealern har mer än 21 poäng
                break
                #bryter loopen med en break




def Blackjack()->None:
#Här är hela spelupgången upplagd i en def. Detta till skillnad från SpelarenSpelarSpelet och DealerSpelarSpelet är att inte endast låta en person spela utan lägga upp spelaren mot dealern i en runda.
    while True: 
    #Här startar en loop för hela spelgången
        player1: Spelare = Spelare()
        #Först görs objektet för spelaren kopplat till variabeln Player1
        player1.SpelareSpelaSpelet()
        #Här sätts spelet igång för objektet/spelaren
        if player1.poäng > 21:
        #Här ser jag till att om Spelaren (du) får över 21 poäng att spelet stoppas automatiskt eftersom dealern alltid vinner om du får över 21! Detta genom en if sats om spelaren får mer en 21.
            print('Du har förlorat spelet för att du fick mer än 21 poäng. Dealern vann!')
            #En print som talar om att du förlorat
            break
            #En break för att ta dig ur loopen
        print('\nDealerns tur')
        #en print för för att vissa vems tur det är (bots)
        dealer1: Dealer = Dealer()
        #Här görs obejektet för dealern/boten kopplad till variablen Dealer1
        dealer1.DealerSpelarSpelet()
        #Spelet sätts igång för dealern
        print(f'\nDu hade {player1.poäng} poäng \ndealern hade {dealer1.poäng} poäng')
        #en print som vissar den totala poängen efter rundan
        if dealer1.poäng > 21:
        #Här gör jag en if sats lik den förra, om dealern får över 21 poäng. Då kommer spelaren att vinna eftersom dealern förlorar automatikst om hen får över 21.
            print('\nDealern har förlorat spelet för att hen fick över 21 poäng. Du vann!')
            #En print som talar om att dealern har förlorat och att spelaren har vunnit
            break
            #En break för att stänga ner loopen
        else:
        #Här kommer en else sats som kommer att checka varje möjlighet om spelaren och dealern båda stannar innan de fått över 21 poäng
            if player1.poäng == dealer1.poäng:
            #If sats som vissar om Spelarens poäng är lika mycket som dealerns
                print('\nDatorn vinner, ni hade lika mycket poäng i handen, du måste ha mer poäng för att vinna! House allways wins ;) ')
                #En print som talar om att dattorn har vunnit (detta eftersom reglerna nämner att dealern/huset vinner om du har lika mycket poäng).
                break
                #Stänger loopen med en break
            elif player1.poäng > dealer1.poäng:
            #En elif sats som vissar om spelaren har mer poäng än dealern
                print('\nDu fick högre än dealern och vinner!')
                #En print som talar om att spelaren har vunnit eftersom att spelaren har mer poäng än dealern 
                break
                #en break som stänger ner loopen
            elif player1.poäng < dealer1.poäng:
            #En sista elif sats som vissar om dealern har mer poäng än spelaren
                print('\nDu fick mindre än dealern och förlorar!')
                #En print som talar om att dealern har vunnit eftersom att dealern har mer poäng än spelaren
                break
                #Den sista breaken för att stänga loopen

def LoopaBlackjack():
#Här har jag gjort en till def eftersom att jag vill att man ska kunna spela blackjack/21 igen utan att stänga ner hela programmet.
    while True:
    #En while true för att loopa
        spela_Eller_Avsluta=input('\nVill du spela igen?, svara ja eller nej : ').lower()
        #En input som frågar om du vill spela igen.
        if spela_Eller_Avsluta=='ja':
        #if sats som gör följande om användaren väljer att svara ja på frågan över
            print('startar om Blackjack')
            #Här printas det ut att spelet ska starta om
            Blackjack()
            #spelet startar om igen genom att köra blackjack defen
            continue
            #en continue som forsätter att loopen så att användaren får samma fråga igen från början av loopen
        elif spela_Eller_Avsluta=='nej':
        #En elif sats om användaren väljer att svara nej på inputen
            print('Avslutar programmet')
            #En print som talar om att programmet avslutas
            break
            #en break för att stänga loopen
        else:
        #en else sats ifall användaren väljer att vara jobbig och inte svara på frågan korrekt
            print('Ogiltigt svar, frågar samma fråga igen!')
            #en print som säger att att användaren inte svarat korrekt och kommer få samma fråga
            continue
            #en continue som forsätter att loopa så att användaren får samma fråga igen från början av loopen

def Hela_Programmet()->None:
#till sist hela programmet i sin slutliga form genom en def
    while True:
    #Här börjar hela programmet genom en while true loop
        startaProgram=input('Vill du sätta igång spelet? Svara ja eller nej : ').lower()
        #Här frågar programmet om användaren ens vill starta spelet genom en input
        if startaProgram== 'ja':
        #om användaren svarar ja kommer denna ifsats ge användaren följande 
            print('Startar blackjack...\n')
            #print som talar om att spelat startas igång
            Blackjack()
            #här startas blackjack spelet med dens def
            LoopaBlackjack()
            #här frågar spelet genom följande def om användaren vill spela igen, antingen så loopar spelet om användaren svara ja, annars kommer användaren få ett avslutar programmet medelande och forsätta till nästa break.
            break
            #brytter hela loopen med en break som stägner programmet
        elif startaProgram=='nej':
        #om användaren väljer att skriva nej i inputen kommer denna elif ge användaren följande 
            print('Avslutar programmet')
            #en print som säger att programmet stängs ner
            break
            #breaken som bryter hela loopen och stänger av programmet
        else:
        #en else sats om användaren vill vara jobbig och inte svara på frågan
            print('Ogiltigt svar, frågar användaren igen! \n')
            #en print som talar om att det är ett ogiltigt svar och att frågan ställs om 
            continue
            #en continue som tar användaren till första inputen i loopen.
        
Hela_Programmet()
#Här är bara programmets def aktivt för att man ska kunna köra spelet/programmet :) 



