import time
import teamdata
import teamfunctıon

print(" WELCOME TO FOOTBALL GAME \n\n")

while(True):
    print("1.Start Game\n")
    print("2.Edıt Team\n")
    print("3.Settings\n")
    print("4.Exıt Game\n")

    choose=int(input())
    if (choose==1):


    elif(choose==2):
        while(True):
            print(" Choose team:\n")
            print("1.TS\n")
            print("2.GS\n")
            print("3.FB\n")
            print("4.BJK\n")
            print("5.for come back main menu\n")

            choose3=int(input())

            if(choose3==1):
                teamfunctıon.TSarrangement()
                print("\n\n")
                print("For changing player,You pull their numbers\n\n")
                teamfunctıon.TSlist()
                print("\n\n")
                while(True):
                    change1=int(input("later first number ,you pull enter\n"))
                    change2=int(input())
                    print("If you finish changing,you can type 'ok'\n")
                    teamfunctıon.TSedit(change1,change2)
                    print("You type 'ok' for contuınıng\n")
                    print("İf you dont want ,you type somethıng(and go to another teams)\n")
                    choose4 = str(input())
                    if (choose4 == 'ok'):
                        continue
                    else:
                        break

            elif(choose3 == 2):
                teamfunctıon.GSarrangement()
                print("\n\n")
                print("For changing player,You pull their numbers\n\n")
                teamfunctıon.GSlist()
                print("\n\n")
                while (True):
                    change3 = input("later first number ,you pull enter\n")
                    change4 = int(input())
                    print("If you finish changing,you can type 'ok'\n")
                    teamfunctıon.GSedit(change3, change4)
                    print("You type 'ok' for contuınıng\n")
                    print("İf you dont want ,you type somethıng(and go to another teams)\n")
                    choose5 = str(input())
                    if (choose5 == 'ok'):
                        continue
                    else:
                        break

            elif(choose3 == 3):
                teamfunctıon.FBarrangement()
                print("\n\n")
                print("For changing player,You pull their numbers\n\n")
                teamfunctıon.FBlist()
                print("\n\n")
                while(True):
                    change5=int(input("later first number ,you pull enter\n"))
                    change6=int(input())
                    print("If you finish changing,you can type 'ok'\n")
                    teamfunctıon.FBedit(change5,change6)
                    print("You type 'ok' for contuınıng\n")
                    print("İf you dont want ,you type somethıng(and go to another teams)\n")
                    choose6 = str(input())
                    if (choose6 == 'ok'):
                        continue
                    else:
                        break

            elif( choose3 == 4):
                teamfunctıon.BJKarrangement()
                print("\n\n")
                print("For changing player,You pull their numbers\n\n")
                teamfunctıon.BJKlist()
                print("\n\n")
                while(True):
                    change7=int(input("later first number ,you pull enter\n"))
                    change8=int(input())
                    print("If you finish changing,you can type 'ok'\n")
                    teamfunctıon.BJKedit(change7,change8)
                    print("You type 'ok' for contuınıng\n")
                    print("İf you dont want ,you type somethıng(and go to another teams)\n")
                    choose7 = str(input())
                    if (choose7 == 'ok'):
                        continue
                    else:
                        break

            elif(choose3==5):
                print("comıng back....\n")
                time.sleep(3)
                break

            else:
                print("You typed wrong value,type again\n")
                continue

    elif(choose==3):
        while(True):
            print("1.Musıc\n")
            print("2.Sound\n")
            choose2=int(input())
            if (choose2==1):

            elif(choose2==2):

            else:
                print("You typed wrong value,type again\n")
                continue

    elif(choose==4):
        print("Exıtıng from Football Game...\n")
        time.sleep(5)
        break
    else:
        print("You typed wrong value,type again\n")
        continue


print("Game ıs fınıshed:(")
