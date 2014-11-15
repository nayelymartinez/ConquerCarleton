# Name: Conquer Carleton
# Authors: Written in Python by Katie Koza and Nayely Martinez
# Contributors: With advice from Sherri Goings and Roy Wiggins
# Class: Intro to Computer Science, Sherri Goings, Carleton College, March 2013
# Description: A version of the popular world domination game, Risk. This game was designed using Pygame. The user plays against the AI, attacking neutral territories. Eventually, the AI and the user are able to attack each other.

bif="map.jpg"

import pygame, sys
from pygame.locals import *
import random

class Buildings:

    def __init__(self, name):
        self.numCarls = 100
        self.troopsToDeploy = 0
        self.name = name

    def drawBuildingCircle(self, screen, BuildingColorDictionary, Ours):
        if Ours:
            pygame.draw.circle(screen, (242,203,11), BuildingColorDictionary[self], 10)
        else:
            pygame.draw.circle(screen, (0,0,153), BuildingColorDictionary[self], 10)

        pygame.display.update()

    def changeBuildingColor(self, screen, toAttackObject, MyBuildingList, BuildingColorDictionary):
        #If we win, then changes building color to yellow
        if toAttackObject in MyBuildingList:
            pygame.draw.circle(screen, (242, 203, 11), BuildingColorDictionary[toAttackObject], 10)
        # If AI wins, then changes building color to yellow.
        elif toAttackObject not in MyBuildingList:
            pygame.draw.circle(screen, (0, 0, 153), BuildingColorDictionary[toAttackObject], 10)
            
        pygame.display.update()

    # Hypothetical idea: Each circle would display the number of troops it has
    def displayNumCarls(self, screen, AllBuildingList, BuildingColorDictionary, BuildingRectangleDictionary):
        for b in AllBuildingList:
            pygame.draw.rect(screen, (255,255,255), BuildingRectangleDictionary[b])
            num = str(b.getNumCarls())
            font = pygame.font.Font(None, 20)
            displ = font.render(num, 1, (220, 0, 0))
            screen.blit(displ, (BuildingColorDictionary[b]))

        
    def getNumCarls(self):
        return self.numCarls

    def getName(self):
        return self.name

    def addCarls(self, addedCarls):
        self.numCarls=self.numCarls+addedCarls
        return self.numCarls

    def setNumCarls(self, newNumCarls):
        self.numCarls=newNumCarls

    def loseCarls(self, lostCarls):
        self.numCarls=self.numCarls-lostCarls
        return self.numCarls

    def CarlsAttack(self, attackingDormObject, troopsAttackerDeploys):
        #The number of troops that the attacker attacks with leave their dorm.
        attackingDormObject.loseCarls(troopsAttackerDeploys)
        print "There are", attackingDormObject.getNumCarls(), "left in the attacking dorm", attackingDormObject.getName()

        print
        print "FURY OF BATTLE!"
        print
        
        numAttackedCarls=self.getNumCarls()
        print self.getName(), "fought back with", numAttackedCarls, "troops."
        
        totalChances=int(troopsAttackerDeploys)+int(numAttackedCarls)
        spam=random.randrange(totalChances)

        attackerWins = spam <= troopsAttackerDeploys

        if attackerWins:
            print "The attacker has defeated the dorm!"
            self.setNumCarls(troopsAttackerDeploys)
            print "There are", self.getNumCarls(), "troops in", self.name, "now."
            print "And there are", attackingDormObject.getNumCarls(), "troops in", attackingDormObject.getName(), ", now."
            return True

        else:
            print "The attacker lost the battle! Agony of defeat!"
            # Now, the attacker will have lost all of its troops, and the attacked dorm will be weakened by half.
            self.setNumCarls(self.getNumCarls()/2)
            print "Now", self.getName(), "has", self.getNumCarls(), "troops."
            print "And there are", attackingDormObject.getNumCarls(), "troops in", attackingDormObject.getName(), "now."
            return False            

def findWeakBuilding(AllBuildingList, MyBuildingList, AIBuildingList, turncounter):
    minNum=1000
    for b in AllBuildingList:
        if b not in AIBuildingList and (b.getNumCarls() < minNum):
            #If building not in our list or if building is in user list but enough turns passed, then that building will be the one AI attacks. Otherwise, continue loop.
            if b not in MyBuildingList or (b in MyBuildingList and turncounter >= 3):
                minNum=b.getNumCarls()
                toAttackObject=b
    return toAttackObject

def findStrongBuilding(AIBuildingList):
    AIMax=0
    for b in AIBuildingList:
        if b.getNumCarls()>AIMax:
            AIMax=b.getNumCarls()
            AttackingBuilding=b
            return AttackingBuilding

# Finds weakest building AI has
def findAIWeakBuilding(AIBuildingList):
    AIMin=1000
    for b in AIBuildingList:
        if b.getNumCarls()<AIMin:
            AIMin=b.getNumCarls()
            AIweakBuilding=b
            return AIweakBuilding
    
    



def main():

#Initiates pygame and loads screen and background image

    pygame.init()
    screen=pygame.display.set_mode((694, 906))

    background=pygame.image.load(bif).convert()

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background, (0,0))

        font = pygame.font.Font(None, 20)
        pygame.display.update()

        print
        print "Fight against the Guardians of Schiller and the neutral dorms to Conquer Carleton!"
        print "This is a version of the world domination game Risk."
        print "All dorms start with 100 Carls at first."
        print "You can only attack The Guardians (Blue territory) after you have done 5 turns."
        print "Your buildings show up on the map in maize, and the Guardians' buildings show up in blue."
        print "Black buildings are neutral territory."
        print
        raw_input("Hit Enter to begin playing!")
        print


        burton=Buildings("burton")
        cassat=Buildings("cassat")
        davis=Buildings("davis")
        evans=Buildings("evans")
        goodhue=Buildings("goodhue")
        memorial=Buildings("memorial")
        musser=Buildings("musser")
        myers=Buildings("myers")
        nourse=Buildings("nourse")
        severance=Buildings("severance")
        townhouses=Buildings("townhouses")
        watson=Buildings("watson")

        AllBuildingList=[burton, cassat, davis, evans, goodhue, memorial, musser, myers, nourse, severance, townhouses, watson]
        AllBuildingDictionary={"burton": burton, "cassat": cassat, "davis": davis, "evans": evans, "goodhue": goodhue, "memorial": memorial, "musser": musser, "myers": myers, "nourse": nourse, "severance": severance, "townhouses": townhouses, "watson": watson}
        BuildingColorDictionary = {burton:(185, 600), cassat: (485, 629), davis: (185, 623), evans: (540, 600), goodhue: (550, 458), memorial: (435, 629), musser: (160, 635), myers: (490, 580), nourse: (426, 600), severance: (200, 560), townhouses: (132, 650), watson: (514, 678)}
        BuildingRectangleDictionary = {burton:(185, 600, 23, 13), cassat: (485, 629, 23, 13), davis: (185, 623, 23, 13), evans: (540, 600, 23, 13), goodhue: (550, 458, 23, 13), memorial: (435, 629, 23, 13), musser: (160, 635, 23, 13), myers: (490, 580,23, 13), nourse: (426, 600, 23, 13), severance: (200, 560, 23, 13), townhouses: (132, 650, 23, 13), watson: (514, 678, 23, 13)}

        #Picks the user's starting building
        startIndex=random.randrange(0,11)
        startBuilding=AllBuildingList[startIndex]
        # Draws yellow circle on starting building
        Ours = True
        startBuilding.drawBuildingCircle(screen, BuildingColorDictionary, Ours)

        #Appends name of start to MyBuildingList
        MyBuildingList=[]
        MyBuildingList.append(startBuilding)
        print "You can deploy from", startBuilding.getName()

        #Picks the AI's starting building
        startAIndex=random.randrange(0,11)
        while startAIndex==startIndex:
            startAIndex=random.randrange(0,11)
        startAIBuilding=AllBuildingList[startAIndex]
        # Draws blue circle on starting building
        Ours = False
        startAIBuilding.drawBuildingCircle(screen, BuildingColorDictionary, Ours)

        # Appends the AI's starting building to their building list
        AIBuildingList=[]
        AIBuildingList.append(startAIBuilding)
        print "The Guardians have", startAIBuilding.getName()

        #The following is trying to display the number of Carls in each building, and should update each time someone makes a turn, meaning that this code needs to also be replicated at the end of the AI and user's turn. 
        pygame.display.update()    
        startAIBuilding.displayNumCarls(background, AllBuildingList, BuildingColorDictionary, BuildingRectangleDictionary)
        pygame.display.update()    

        # Draws black circles for neutral territories not yet conquered.
        for b in AllBuildingList:
            if b not in MyBuildingList and b not in AIBuildingList:
                pygame.draw.circle(screen, (50, 50, 50), BuildingColorDictionary[b], 10)
        pygame.display.update()    

        
        turncounter = 1
        
        # While Carleton is not conquered...
        while 1 <= len(MyBuildingList) <= 11 or 1 <= len(AIBuildingList) <= 11:

            #The AI takes a turn.
            while turncounter%2 !=0:
                print "The Guardians are taking a turn"

                #Finds the weakest building that it does not have.
                toAttackObject=findWeakBuilding(AllBuildingList, MyBuildingList, AIBuildingList, turncounter)
                
                #Finds the strongest building that it DOES have.
                AttackingBuilding=findStrongBuilding(AIBuildingList)
                
                #Finds the weakest building that it HAS.
                AIweakBuilding=findAIWeakBuilding(AIBuildingList)
                                     
                #Should add 10 troops to its weakest building.
                AIweakBuilding.addCarls(10)

                print AttackingBuilding.getNumCarls()
                print toAttackObject.getNumCarls()

                #Decides whether or not to act
                if AttackingBuilding.getNumCarls()>2*(toAttackObject.getNumCarls()) and 2*(toAttackObject.getNumCarls())>2:
                    troopsAIDeploys=(toAttackObject.getNumCarls())-1
                    print "The Guardians attacked from", AttackingBuilding.getName(), "with", troopsAIDeploys, "Carls."
                    print "The Guardians attacked", toAttackObject.getName()

                    #Now, attack toAttackObject with AttackingBuilding
                    Won = toAttackObject.CarlsAttack(AttackingBuilding, troopsAIDeploys)

                    #Updates MyBuildingList if the guardians beat one of our buildings.
                    if Won:

                        for i in range(len(MyBuildingList)):
                            if MyBuildingList[i].getName() == toAttackObject.getName():
                                MyBuildingList.pop(i)
                                break
                        AIBuildingList.append(toAttackObject)
                        toAttackObject.changeBuildingColor(screen, toAttackObject, MyBuildingList, BuildingColorDictionary)

                else:
                    print "The Guardians have decided not to attack but instead to bide their time."

                startAIBuilding.displayNumCarls(screen, AllBuildingList, BuildingColorDictionary, BuildingRectangleDictionary)
                pygame.display.update()
                
                turncounter=turncounter+1

            #If AI conquers our only remaining building, the following lines should break out of the while loop and print Carleton has been conquered.
            if len(MyBuildingList) == 0 or len(AIBuildingList) == 0:
                break
            
            while turncounter%2==0:
                print
                print "It's your turn now!"

                buildingAddTroopsRound = raw_input("Where would you like to add 10 prospies to? Or, enter 's' to move on to attack.").lower()

                while buildingAddTroopsRound != 's':
                    # NEW: Checks for user input error. If string is a valid building name in all building dictionary and it is a building in user list, then proceeds.
                    if buildingAddTroopsRound in AllBuildingDictionary.keys() and AllBuildingDictionary[buildingAddTroopsRound] in MyBuildingList:
                            buildingToAddTo=AllBuildingDictionary[buildingAddTroopsRound]
                            buildingToAddTo.addCarls(10)
                            startAIBuilding.displayNumCarls(screen, AllBuildingList, BuildingColorDictionary, BuildingRectangleDictionary)
                            pygame.display.update() 
                            break
                    else:
                            buildingAddTroopsRound=raw_input("You can't add prospies to that dorm. Where would you like to add 10 prospies to? Or, enter 's' to move on to attack.").lower()
                            

                answer=raw_input("Press A to attack, or P to pass this turn.").lower()
                if answer=="a":

                    buildingstring=raw_input("Where would you like to deploy troops of Carls from?").lower()
                    #Checks if that is a valid dorm that the user can deploy from.
                    valid = False
                    while valid == False:
                        if buildingstring not in AllBuildingDictionary.keys():
                            buildingstring=raw_input("That is not in the dictionary of dorms. Where would you like to deploy troops of Carls from?").lower()
                        elif AllBuildingDictionary[buildingstring] not in MyBuildingList:
                             buildingstring=raw_input("That is not in your list of dorms. Where would you like to deploy troops of Carls from?").lower()
                        else:
                            break

                   
                    for b in MyBuildingList:
                        if b.getName()==buildingstring:
                            AttackingBuilding=b
                            troopsInChosenBuilding = AttackingBuilding.getNumCarls()
                            print buildingstring, "has", troopsInChosenBuilding, "troop(s) in the building."
                        
                            troopsToDeploy = raw_input("How many Carls would you like to deploy from there?")

                            #Checks that troopsToDeploy is an int.
                            while True:
                                try:
                                    troopsToDeploy=int(troopsToDeploy)
                                    break
                                except ValueError:
                                    troopsToDeploy = raw_input("That is not a valid number of troops to deploy. How many Carls would you like to deploy?")

                    #Checks that they can deploy that particular number of troops from that particular building        
                    while troopsToDeploy > AttackingBuilding.getNumCarls()-1:
                        print AttackingBuilding.getNumCarls()
                        troopsToDeploy = raw_input("You can't deploy that many Carls. How many Carls would you like to deploy?")
                        troopsToDeploy = int(troopsToDeploy)
                            
                    toAttackString=raw_input("Where would you like to attack?:").lower()

                            
                    while True:
                        try:
                            toAttackObject=AllBuildingDictionary[toAttackString]
                            # If building we attack is in our list or in the AI's list...
                            while toAttackObject in MyBuildingList or toAttackObject in AIBuildingList or toAttackObject not in AllBuildingList:
                                # If in our building, no-no
                                if toAttackString not in AllBuildingDictionary.keys():
                                    toAttackString=raw_input("You have to pick a Carleton dorm. Which one would you like to attack?").lower()
                                    toAttackObject=AllBuildingDictionary[toAttackString]

                                elif toAttackObject in MyBuildingList:
                                    toAttackString=raw_input("You can't attack one of your own dorms, silly. Which dorm would you like to attack?").lower()
                                    toAttackObject=AllBuildingDictionary[toAttackString]

                                # If it is in the AI's list and there has been less than 10 turns
                                elif toAttackObject in AIBuildingList and turncounter <= 3:
                                    toAttackString=raw_input("You can't attack the AI quite yet. Which other dorm would you like to attack?").lower()
                                    toAttackObject = AllBuildingDictionary[toAttackString]

                                #If it is in AI list but there are more than 10 turns, it retrieves that object to attack
                                else:
                                    toAttackObject = AllBuildingDictionary[toAttackString]
                                    break
                            break
                        except:
                            toAttackString=raw_input("Nope, this is not a valid dorm name. Where would you like to attack?:").lower()




                    #CarlsAttack returns the result of the battle as True or False
                    Won = toAttackObject.CarlsAttack(AttackingBuilding, troopsToDeploy)

                    # If we win
                    if Won:
                        for i in range(len(AIBuildingList)):
                            if AIBuildingList[i].getName()==toAttackObject.getName():
                                AIBuildingList.pop(i)
                                break
                        # Appends to our list. Needs to append before changing building color.
                        MyBuildingList.append(toAttackObject)

                        #call changeBuildingColor
                        toAttackObject.changeBuildingColor(screen, toAttackObject, MyBuildingList, BuildingColorDictionary)

               
       
                startAIBuilding.displayNumCarls(screen, AllBuildingList, BuildingColorDictionary, BuildingRectangleDictionary)
                pygame.display.update() 
                
                print
                raw_input("The AI will take its turn now. Hit 'Enter' to continue.")
                print
                turncounter=turncounter+1

        raw_input("Carleton has been conquered! Hit Enter to quit")
        break
        
if __name__=="__main__":
    main()

