import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN)                 #Pin13 input (drukken op de knop)
GPIO.setup(16, GPIO.IN)                 #Pin16 input (drukken op de knop)
GPIO.setup(7, GPIO.OUT)                 #Pin7 output
GPIO.output(7, False)                   #Pin7 uitzetten
GPIO.setup(12, GPIO.OUT)                #Pin12 output
GPIO.output(12, False)                  #Pin12 uitzetten

code = '4444'
blinkrood = False
blinkSpeed = 1


def blinkenrood():
        global blinkrood
        global blinkSpeed
        if blinkrood == True:
                GPIO.output(7,True)                     ## Zet lichtje aan
                time.sleep(blinkSpeed/10)               ## Wacht 1 seconde
                GPIO.output(7,False)                    ## Zet lichtje uit
                time.sleep(blinkSpeed/10)               ## Wacht weer 1 seconde



while True:                                             #Wanneer iets 1 is doe het volgende:
        if  GPIO.input(13)==1:                          #Als Pin13 aan is laat lampje rood blinken
                print('Er is ingebroken!')
                blinkrood = True

        if GPIO.input(16)==1 and blinkrood == True:             #Als Pin15 aan is en het rode lampje blinkt doe het volgende:
                invoer = input(str('Voer de code in om het alarm uit te zetten: '))             #Laat de gebruiker een code invoeren om het alarm uit zetten

                if invoer == code:                      #als invoer hetzelfde is als de code
                        print('Code is juist!')
                        blinkrood = False               #Zet het rode lampje uit
                        GPIO.output(12, True)           #Zet het groene lampje aan
                        time.sleep(2)                   #Wacht 2 seconde
                        GPIO.output(12, False)          #Zet het groene lampje uit
                        speed = int(input("Voer hier de snelheid in voor de volgende keer dat het alarm afgaat: "))     #Vraag de gebruiker om de snelheid voor het volgende alarm
                        if speed > 1 and speed <= 10:           #Als de snelheid groter is dan 1 en kleiner en gelijk aan 10:
                                blinkSpeed = speed              #Zet de blinksnelheid naar de invoer van de gebruiker
                        print("Alarm uitgeschakeld")            #Geef aan dat het alarm is uitgeschakeld
                else:                                   #als de code verkeerd is:
                        GPIO.output(12, False)          #zet het groene lampje uit
                        print("Verkeerde code, druk de knop opnieuw in en probeer opnieuw")     #Laat de gebruiker opnieuw code opgeven
                        continue
        blinkenrood()

