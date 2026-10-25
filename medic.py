import random


calls = ["Car wreck", "Fire", "Heart attack", "Stroke"]

gloveNotes = []

cardioRhythm = ["V-Fib", "V-Tach", "Asystole", "A-Fib", "Sinus"]

radio = random.choice(calls)

print("                    A Deatach Game                                  ")
name = input("Enter your name: ")

opening = input("""The stories you are about to live are True. 
Well not exactly true but written by a real medic. These are his stories.
Enter (y/n) to live the role: """)
print("                                                                    ")
if opening == "y":
            if radio == "Heart attack":
                print("#####################################################")
            dispatch = input("""Ambulance one call for an active cardiac incident. 
Address 175 Second St. Caller adult male 45 increasing
pain shortness of breath and dizzy. 
(y/n to resond to scene): """)           
            
            
            print("                                                          ")
            if dispatch == "y":
                
                print("#### NEW PAGE PD States Cardiac Arrest Compressions in Progress ###")

                print("                                                      ")
                
                print(f"{name}: Ambulance crew one en route.")
                print("                                                        ")
                
                print(f"{name}: Dispatch show ambulance one on scene time 0430.")
                print("                                                      ")
                print("=========================================================")
                sceneSafe = input("""You arrive on scene partner slams the rig into park.
Do you jump out of the rig and run inside? or squeeze through the back and grab go-bag and AED?
Enter (j/g): """)
                if sceneSafe == 'g':
                       print("""While you gathered your gear a cop restrains the dog 
that came toward the ambulance door""")
                       print("""You walk you see a fat male in his forties wedged in the foyer. 
Vomit spilling out of his mouth and a cop doing half-assed compressions""")
                       print("                                                            ")
                       print("""You kneel next to the patient and relieve the cop of his shift.
Your rookie is Straight Outta EMT class and his first in field code. 
So you let him set up the AED to work out the shakes every noob has them even you at one point.""")
                       print("                                                                   ")
                       print("""The rook final got the leads attached only took him a whole 30 seconds. 
He'll speed up he shows potetial""")
                       print("                                                                   ")
                       strip = random.choice(cardioRhythm)
                       shock = input(f"The monitor shows {strip}. Shock or No Shock? (s/n) ")
                       if strip == "V-fib" or strip == "V-tach" and shock == 's':
                            print("I'm Clear, Your Clear, Clear! ")
                            print("...........")
                            print("...........")
                            print("Sinus rythym achieved. Load for hospital!")
                       else: 
                             print("You killed you patient. GameOver!")
                               



            # elif dispatch == 'no':
            #             ("Get chewed out")

            