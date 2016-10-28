init:
    transform fadeSleep:
        alpha 0.0
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0.0
        
    transform fadeOutText:
        alpha 1.0
        linear 5.0 alpha 0.0

init python:
    #imports
    import re
    #variables
     #monsters
    playerMonsters= list()
    youngMonsters= list()
    requestedMonsters= list()
    knownSpecies= {}
    knownVariants= list()
     #time
    gameMinute= 0
    gameHour= 6
    gameDay= 1
    gameMonth= 6
    gameYear= 587
    monthNames= ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
     #player
    gameMoney= 0
    playerName= "Player"
    playerPortrait= "data/monster/player/caucasian/male/portrait.png"
     #other
    currentID= 0
    traitListRegular= []
    traitListGender= []
    traitListBreed= []
    gameChapter= ""
    gameRegion= ""
    gameMission= ""
    saveList= []
    
    #classes
    class Species():
        "defines a species used for monster generation"
        def __init__(self, spe, bas, har, mar):
           self.species= spe
           self.genes= list()
           self.baseVars= bas
           self.hairVars= har
           self.markingVars= mar
           self.base= [0, 255, 0, 255, 0, 255]
           self.hair= [0, 255, 0, 255, 0, 255]
           self.mark= [0, 255, 0, 255, 0, 255]
           self.ferMod= 1.0
           self.finMod= 1.0
           self.detMod= 1.0
           self.cunMod= 1.0
           self.hermLim= 0
           self.femLim= 50
           self.movement= 4
           self.battleName= spe
           self.attacklist= {"male": [], "female": [], "hermaphrodite": []}
    
    class TestBox(renpy.Displayable):
        "A test displayable"
        def __init__(self, **kwargs):
            super(TestBox, self).__init__(**kwargs)
            self.width= 250
            self.height= 150
            self.back= Image("data/other/clockBack.png")
            
        def render(self, width, height, st, at):
            render= renpy.Render(self.width, self.height)
            back= renpy.render(self.back, width, height, st, at)
            render.blit(back, (0,0))
            return render
            
        def visit(self):
            return [self.back]
    
    class Monster:
        "A monster"
        def __init__(self):
           #basics
            self.name= "nameless"
            self.intID= 0
            self.species= Species("any", 0, 0, 0)
            self.species.hermLim= 20
            self.species.femLim= 60
            self.variant= "any"
            self.gender= "any"
            #appearance
            self.base= 0
            self.baseColor= (0,0,0)
            self.hair= 0
            self.hairColor= (0,0,0)
            self.marking= 0
            self.markingColor= (0,0,0)
            self.baseVars= 0;
            self.hairVars= 0;
            self.markingVars= 0;
            #attributes
            self.ferocity= 0.0
            self.finesse= 0.0
            self.determination= 0.0
            self.cunning= 0.0
            self.fertility= 0
            self.fertilityBase= 0
            self.genes= list()
            #condition bars
            self.lust= 0
            self.rage= 0
            self.health= 100
            self.maxHealth= 100
            self.stamina= 1
            self.maxStamina= 1
            #condition other
            self.pregChild= None
            self.valueM= 100
            self.training= 10
            self.statPoints= 1.0
            self.relatives= []
            self.relativeNames= []
            
        def addGene(self, gene):
            self.genes.append(gene)
            
        def removeGene(self, geneName):
            for gene in self.genes:
                if (geneName== gene.name):
                    self.genes.remove(gene)
                    
        def calcFertility(self):
            self.fertilityBase= int((self.ferocity/ 15.0) * (self.cunning/ 25))
            if (self.fertilityBase> 100):
                self.fertilityBase= 100
            elif (self.fertilityBase< 1):
                self.fertilityBase= 1
            
        def calcEndurance(self):
            self.maxStamina= int(self.determination/ 25+ self.ferocity/ 50)
            if (self.maxStamina< 1):
                self.maxStamina= 1
                
        def calcValue(self):
            self.valueM= int(self.ferocity+ self.finesse+ self.determination+ self.cunning)
            for trait in self.genes:
                if ("status" not in trait.effect and trait.active):
                    if ("bad" in trait.effect):
                        self.valueM-= trait.power* 10
                    else:
                        self.valueM+= trait.power* 10
                if ("money" in trait.effect and trait.active):
                    self.valueM+= trait.power* 90
                    
        def applyGenes(self):
            for gene in self.genes:
                if ("status" in gene.effect):
                    if ("fertility" in gene.effect):
                        self.fertility= int(re.sub("[^0-9]", "", gene.effect))
                        
        def getCombatMonster(self):
            bName= self.gender[0].upper()+ self.species.battleName
            return unit(self.ferocity, self.finesse, self.determination, self.cunning, "p"+ str(len(PlayerArmy.Army)), self.name, self.species.attacklist[self.gender], [], 4, bName+ "Idle", bName+ "Hover", bName+ "Move", bName+ "Mug", self.gender[0].upper()+ self.gender[1:], 1)
            
            
        def loadRelatives(self):
            for kin in self.relativeNames:
                for monster in playerMonsters:
                    if (kin== monster.intID):
                        self.relatives.append(monster)
                for monster in youngMonsters:
                    if (kin== monster.intID):
                        self.relatives.append(monster)
                if (self.pregChild!= None):
                   self.pregChild.loadRelatives()
  
                   
    class Player(Monster):
        "The player character"
        def __init__(self):
            Monster.__init__(self)
            self.name= "Player"
            self.species= Species("player", 0, 0, 0)
            self.gender= "male"
            self.variant= "caucasian"
            self.ferocity= 2
            self.finesse= 2
            self.determination= 2
            self.cunning= 2
            
        def getCombatMonster(self):
            return unit(self.ferocity, self.finesse, self.determination, self.cunning, "p"+ str(len(PlayerArmy.Army)), self.name, [MCAxe], [], 4, "MCIdle", "MCHover", "MCMove", "MCMug", "Male", 1)
        
       
            
    class Gene:
        "One of a monster's traits/stats/etc"
        def __init__(self, img, nam, des, eff, pow, uni, act):
            self.icon= img
            self.name= nam
            self.description= des
            self.effect= eff
            self.power= pow
            self.unit= uni
            self.active= act
     
            
    class Mission:
        "A mission for the combat engine"
        def __init__(self, tit= "Explore", ene= "Unknown", obj= "Enter a random encounter", obj2= "None", rec= "A balanced squad", tea= 4, des= "Explore the local area to train your monsters, find treasure and capture wild beasts!"):
            self.title= tit
            self. scouted= False
            self.enemies= "Possible enemies: "+ ene
            self.primary= "Primary objective: "+ obj
            self.secondary= "Secondary objective: "+ obj2
            self.recommend= "Recommendations: "+ rec
            self.maxTeam= tea
            self.team= "Max team size: "+ str(tea)
            self.description= des
            self.presetArmyP= Army([], [])
            self.presetArmyE= None
           
            
    class ClockBox(renpy.Displayable):
        "reders a clock using gameTime and gameDay"
        def __init__(self, **kwargs):
            super(ClockBox, self).__init__(**kwargs)
            self.width= 250
            self.height= 150
            self.minute= None
            self.hour= None
            self.back= Image("data/other/clockBack.png")
            self.day= Text(str(gameDay), size= 60, color= (200,0,0), font= "SegoeBold.ttf")
            self.month= Text(monthNames[gameMonth- 1], size= 35, bold= True, color= (200,0,0), font= "SegoeBold.ttf")
        
        def update(self):
            self.hour= Transform("data/other/clockHour.png")
            self.hour.rotate_pad= True
            self.hour.anchor= (0.5,0.5)
            if (gameHour< 12):
                self.hour.rotate= (360/ 12)* gameHour
            else:
                self.hour.rotate= (360/ 12)* (gameHour- 12)
            self.hour.update()
            self.minute= Transform("data/other/clockMinute.png")
            self.minute.rotate_pad= True
            self.minute.anchor= (0.5,0.5)
            self.minute.rotate= (360/ 60)* gameMinute
            self.minute.update()
            self.day= Text(str(gameDay), size= 60, color= (200,0,0), font= "SegoeBold.ttf")
            self.month= Text(monthNames[gameMonth- 1], size= 35, bold= True, color= (200,0,0), font= "SegoeBold.ttf")
        
        def render(self, width, height, st, at):
            self.update()
            render= renpy.Render(self.width, self.height)
            back= renpy.render(self.back, width, height, st, at)
            day= renpy.render(self.day, width, height, st, at)
            month= renpy.render(self.month, width, height, st, at)
            hour= renpy.render(self.hour, width, height, st, at)
            minute= renpy.render(self.minute, width, height, st, at)
            lenD= self.day.size()[0]/ 2
            lenM= self.month.size()[0]/ 2
            render.blit(back, (0, 0))
            render.blit(day, (55- lenD, 40))
            render.blit(month, (55- lenM, 15))
            render.blit(hour, (97, -3))
            render.blit(minute, (97, -3))
            return render
            
        def visit(self):
            return [self.back, self.day, self.hour, self.minute]
    
            
            
    #functions    
    def col(val):
        return val/ 255.0
    
    def recolorImage(img, old, new):
        red= clr[0]
        green= clr[1]
        blue= clr[2]
        if (old== "red"):
            matrix= (col(red), 0.0, 0.0, 0.0, 0.0,
                           col(green), 1.0, 0.0, 0.0, 0.0,
                           col(blue), 0.0, 1.0, 0.0, 0.0,
                           0.0, 0.0, 0.0, 1.0, 0.0)
        else:
            if (old== "green"):
                matrix= (1.0, col(red), 0.0, 0.0, 0.0,
                               0.0, col(green), 0.0, 0.0, 0.0,
                               0.0, col(blue), 1.0, 0.0, 0.0,
                               0.0, 0.0, 0.0, 1.0, 0.0)
            else:
                matrix= (1.0, 0.0, col(red), 0.0, 0.0,
                                0.0, 1.0, col(green), 0.0, 0.0,
                                0.0, 0.0, col(blue), 0.0, 0.0,
                                0.0, 0.0, 0.0, 1.0, 0.0)
        temp= im.MatrixColor(img,  matrix)
        return temp
       
    def saveMonster(file, monster):
        file.write(monster.name+ "\n")
        file.write(str(monster.intID)+ "\n")
        file.write(monster.species.species+ "\n")
        file.write(monster.variant+ "\n")
        file.write(monster.gender+ "\n")
        file.write(str(monster.ferocity)+ "\n")
        file.write(str(monster.finesse)+ "\n")
        file.write(str(monster.determination)+ "\n")
        file.write(str(monster.cunning)+ "\n")
        file.write(str(monster.lust)+ "\n")
        file.write(str(monster.rage)+ "\n")
        file.write(str(monster.health)+ "\n")
        file.write(str(monster.stamina)+ "\n")
        file.write(str(monster.training)+ "\n")
        file.write(str(monster.statPoints)+ "\n")
        file.write(str(monster.fertility)+ "\n")
        for kin in monster.relatives:
            file.write("k="+ str(kin.intID)+ "\n")
        for gene in monster.genes:
            file.write("newGene"+ "\n")
            saveGene(file, gene)
        if (monster.pregChild!= None):
            file.write("pregChild"+ "\n")
            saveMonster(file, monster.pregChild)
        file.write("finishMonster\n")
        
    def saveGene(file, gene):
        file.write(gene.name+ "\n")
        file.write(gene.description+ "\n")
        file.write(gene.effect+ "\n")
        file.write(str(gene.power)+ "\n")
        file.write(gene.unit+ "\n")
        file.write(str(gene.active)+ "\n")    
        
    def saveGame(slot):
        file= open("saves/aobSave"+ str(slot)+ ".txt", 'w')
        file.write(playerName+ "\n")
        file.write(str(gameDay)+ "/"+ str(gameMonth)+ "/"+ str(gameYear)+ "\n")
        file.write("Money: "+ str(gameMoney)+ "\n")
        file.write(gameChapter+ "\n")
        file.write(gameRegion+ "\n")
        file.write(gameMission+ "\n")
        file.write(playerPortrait+ "\n")
        for key in knownSpecies:
            file.write(key+ "\n")
        file.write("quicksave done\n")
        file.write(str(gay)+ "\n")
        file.write(str(straight)+ "\n")
        file.write(str(lesbian)+ "\n")
        file.write(str(herms)+ "\n")
        file.write(str(anal)+ "\n")
        file.write(str(vaginal)+ "\n")
        file.write(str(oral)+ "\n")
        file.write(str(bondage)+ "\n")
        file.write(str(zoophilia)+ "\n")
        file.write(str(gameMonth)+ "\n")
        file.write(str(gameDay)+ "\n")
        file.write(str(gameHour)+ "\n")
        file.write(str(gameMinute)+ "\n")
        file.write(str(gameMoney)+ "\n")
        file.write(str(currentID)+ "\n")
        for monster in playerMonsters:
            file.write("newMonster"+ "\n")
            saveMonster(file, monster)
        for monster in youngMonsters:
            file.write("newYoungMonster"+ "\n")
            saveMonster(file, monster)
        for monster in requestedMonsters:
            file.write("newRequestMonster"+ "\n")
            saveMonster(file, monster)
        file.close()
    
    def loadMonster(file):
        monster= Monster()
        monster.name= file.readline()[:-1]
        monster.intID= int(file.readline()[:-1])
        species= file.readline()[:-1]
        if (species== "player"):
            name= monster.name
            monster= Player()
            monster.name= name
        elif (species!= "any"):
            monster.species= knownSpecies[species]
        monster.variant= file.readline()[:-1]
        monster.gender= file.readline()[:-1]
        monster.ferocity= float(file.readline()[:-1])
        monster.finesse= float(file.readline()[:-1])
        monster.determination= float(file.readline()[:-1])
        monster.cunning= float(file.readline()[:-1])
        monster.lust= int(file.readline()[:-1])
        monster.rage= int(file.readline()[:-1])
        monster.health= int(file.readline()[:-1])
        monster.stamina= int(file.readline()[:-1])
        monster.training= int(file.readline()[:-1])
        monster.statPoints= float(file.readline()[:-1])
        monster.fertility= int(file.readline()[:-1])
        line= file.readline()[:-1]
        while (line[0]== 'k'):
            monster.relativeNames.append(int(line[2:]))
            line= file.readline()[:-1]
        while (line== "newGene"):
            monster.addGene(loadGene(file))
            line= file.readline()[:-1]
        if (line== "pregChild"):
            monster.pregChild= loadMonster(file)
            line= file.readline()[:-1]
        while (line!= "finishMonster"):
            line= file.readline()[:-1]
        monster.calcEndurance()
        monster.calcFertility()
        monster.applyGenes()
        print monster.name
        return monster
    
    def loadGene(file):
        return Gene(None, file.readline()[:-1], file.readline()[:-1], file.readline()[:-1], int(file.readline()[:-1]), file.readline()[:-1],  (file.readline()[:-1])== "True")

    def quickLoad(slot, target):
        try:
            file= open("saves/aobSave"+ str(slot)+ ".txt", 'r')
            print "read start"
            target.name= file.readline()[:-1]
            target.date= file.readline()[:-1]
            target.money= file.readline()[:-1]
            target.chapter= "Chapter "+ file.readline()[:-1]
            target.region= "Region "+ file.readline()[:-1]
            target.mission= "Mission "+ file.readline()[:-1]
            target.portrait= file.readline()[:-1]
            target.knownMonsters= []
            line= file.readline()[:-1]
            while ("quicksave done" not in line):
                target.knownMonsters.append(line)
                line= file.readline()[:-1]
            file.close()
            print "read stop"
        except:
            import traceback
            traceback.print_exc()
    
    def loadGameTest():
        if (selectedSave!= None):
            loadGame(selectedSave.slot)
        
    def saveGameTest():
        global selectedSave
        if (selectedSave!= None):
            saveGame(selectedSave.slot)
            selectedSave= None
            showSaveN()
            renpy.restart_interaction()
            
    def loadGame(slot):
       try:
            global gameMonth
            global gameDay
            global gameHour
            global gameMinute
            global gameMoney
            global currentID
            global playerMonsters
            global youngMonsters
            global requestedMonsters
            global knownSpecies
            global knownVariants
            global currentID
            global gameChapter
            global gameRegion
            global gameMission
            global playerName
            global playerPortrait
            global gay
            global straight
            global lesbian
            global herms
            global anal
            global vaginal
            global oral
            global bondage
            global zoophilia
            playerMonsters= []
            youngMonsters= []
            requestedMonsters= list()
            knownSpecies= {}
            knownVariants= list()
            knownSpecies["clawwolf"]= clawwolf
            knownVariants.append("wild")
            file= open("saves/aobSave"+ str(slot)+ ".txt", 'r')
            playerName= file.readline()[:-1]
            file.readline()[:-1]
            gameMoney= file.readline()[:-1]
            gameChapter= file.readline()[:-1]
            gameRegion= file.readline()[:-1]
            gameMission= file.readline()[:-1]
            playerPortrait= file.readline()[:-1]
            while ("quicksave done" not in file.readline()[:-1]):
                pass
            gay= file.readline()[:-1]== "True"
            straight= file.readline()[:-1]== "True"
            lesbian= file.readline()[:-1]== "True"
            herms= file.readline()[:-1]== "True"
            anal= file.readline()[:-1]== "True"
            vaginal= file.readline()[:-1]== "True"
            oral= file.readline()[:-1]== "True"
            bondage= file.readline()[:-1]== "True"
            zoophilia= file.readline()[:-1]== "True"
            gameMonth= int(file.readline()[:-1])
            gameDay= int(file.readline()[:-1])
            gameHour= int(file.readline()[:-1])
            gameMinute= int(file.readline()[:-1])
            gameMoney= int(file.readline()[:-1])
            currentID= int(file.readline()[:-1])
            line= file.readline()[:-1]
            while (line== "newMonster"):
                playerMonsters.append(loadMonster(file))
                line= file.readline()[:-1]
            while (line== "newYoungMonster"):
                youngMonsters.append(loadMonster(file))
                line= file.readline()[:-1]
            while (line== "newRequestMonster"):
                requestedMonsters.append(loadMonster(file))
                line= file.readline()[:-1]
            file.close()
            for monster in playerMonsters:
                monster.loadRelatives()
                if (monster.intID> currentID):
                    currentID= monster.intID+ 1
            for monster in youngMonsters:
                monster.loadRelatives()
                if (monster.intID> currentID):
                    currentID= monster.intID+ 1
            renpy.show_screen("farm")
            renpy.restart_interaction()
       except:
            import traceback
            traceback.print_exc()
            newGameVars()
            renpy.jump("start")     
            
    def newGameVars():
        "sets the variables for a new game"
        #global
        global playerMonsters
        global youngMonsters
        global requestedMonsters
        global knownSpecies
        global knownVariants
        global gameMinute
        global gameHou
        global gameDay
        global gameMonth
        global gameMoney
        global pregOpen
        global breedMonster1
        global breedMonster2
        global monsterList1
        global monsterList2
        global player
        global pregChanceGlobal
        global exhaust
        global incest
        global filter1
        global filter2
        global currentID
        global gameChapter
        global gameRegion
        global gameMission
        global playerName
        global playerPortrait
        global gay
        global straight
        global lesbian
        global herms
        global anal
        global vaginal
        global oral
        global bondage
        global zoophilia
        gay= True
        straight= True
        lesbian= True
        herms= True
        anal= True
        vaginal= True
        oral= True
        bondage= True
        zoophilia= True
        playerMonsters= list()
        youngMonsters= list()
        requestedMonsters= list()
        knownSpecies= {}
        knownVariants= list()
        gameMinute= 0
        gameHour= 6
        gameDay= 1
        gameMonth= 6
        gameMoney= 0
        pregOpen= False
        breedMonster1= None
        breedMonster2= None
        monsterList1= []
        monsterList2= []
        player= Player()
        pregChanceGlobal= 0
        exhaust= True
        incest= True
        filter1= FilterMonster()
        filter2= FilterMonster()
        #monsterlists
         #world
        knownSpecies["clawwolf"]= clawwolf
        knownVariants.append("wild")
        requestedMonsters.append(newMonsterRequest())
        requestedMonsters.append(newMonsterRequest())
        gameChapter= "1: Origin"
        gameRegion= "1: Valley"
        gameMission= "1: Fight Bandits"
         #player
        playerName= "Player"
        playerPortrait= "data/monster/player/caucasian/male/portrait.png"
        playerMonsters.append(player)
        playerMonsters.append(newMonsterWild(knownSpecies["clawwolf"]))
        playerMonsters.append(newMonsterWild(knownSpecies["clawwolf"]))
        playerMonsters[1].gender= "male"
        playerMonsters[1].name= "Commander"
        playerMonsters[1].ferocity= 75.0
        playerMonsters[1].finesse= 50.0
        playerMonsters[1].determination= 50.0
        playerMonsters[1].cunning= 60.0
        playerMonsters[1].calcFertility()
        playerMonsters[2].gender= "female"
        playerMonsters[2].name= "Bisca"
        playerMonsters[2].relatives.append(player)
        player.relatives.append(playerMonsters[2])
        playerMonsters[1].addGene(Gene("data/gene/main/variant/wild.png", "test2", "A test",  "trait|testing", 2, " lvl", False))
        playerMonsters[2].addGene(Gene("data/gene/main/variant/wild.png", "test2", "A test",  "trait|testing", 2, " lvl", False))
        playerMonsters[2].addGene(Gene("data/gene/main/variant/wild.png", "test3", "A test",  "trait|testing", 3, " lvl", True))
        playerMonsters[1].calcFertility()
        playerMonsters[1].calcEndurance()
        playerMonsters[1].stamina= playerMonsters[1].maxStamina
        playerMonsters[2].calcFertility()
        playerMonsters[2].calcEndurance()
        playerMonsters[2].stamina= playerMonsters[2].maxStamina
        playerMonsters[1].training= 10
        playerMonsters[2].training= 10
        playerMonsters[1].intID= 1
        playerMonsters[2].intID= 2
        currentID= 3
        
    def getPlayerMonsters():
        monsterCombat= player.getCombatMonster()
        PlayerArmy.Army.append(monsterCombat)
        PlayerArmy.DeployArmy.append(monsterCombat)
        for monster in selectorActive:
                monsterCombat= monster.getCombatMonster()
                PlayerArmy.Army.append(monsterCombat)
                PlayerArmy.DeployArmy.append(monsterCombat)
                
    def setExplore():
        global activeMission
        global missionArmyP
        global missionArmyE
        activeMission= Mission()
        missionArmyP= activeMission.presetArmyP
        missionArmyE= activeMission.presetArmyE

    def scoutMission():
        activeMission.scouted= True
        renpy.restart_interaction()
        
    def clearSelection():
        selectorActive= []
        selectedSave= None
        
init 3 python:
    #final variable inititation, mostly for CDDs
    clock= ClockBox()
    viewerB= BreedView(True)
    viewerV= BreedView(False)
    filter1= FilterMonster()
    filter2= FilterMonster()
    traitListRegular= [TraitBox(tra= "any", typ= "picker"), TraitBox(tra= "test1", typ= "picker"), TraitBox(tra= "test2", typ= "picker"), TraitBox(tra= "test3", typ= "picker"), TraitBox(tra= "test4", typ= "picker"), TraitBox(tra= "test5", typ= "picker"), TraitBox(tra= "test6", typ= "picker"), TraitBox(tra= "test7", typ= "picker"), TraitBox(tra= "test8", typ= "picker"), TraitBox(tra= "test9", typ= "picker"), TraitBox(tra= "test10", typ= "picker")]
    traitListGender= [TraitBox(tra= "any", typ= "picker", frm= "gender"), TraitBox(tra= "female", typ= "picker", frm= "gender"), TraitBox(tra= "male", typ= "picker", frm= "gender"), TraitBox(tra= "hermaphrodite", typ= "picker", frm= "gender")]
    traitListBreed= [TraitBox(tra= "any", typ= "picker", frm= "breed"), TraitBox(tra= "clawwolf", typ= "picker", frm= "breed"), TraitBox(tra= "player", typ= "picker", frm= "breed")]
    traitPick= TraitPicker(traitListRegular)
    clawwolf= Species("clawwolf", 0, 0, 0)
    clawwolf.battleName="Wolf"
    clawwolf.ferMod= 1.2
    clawwolf.finMod= 1.0
    clawwolf.detMod= 1.0
    clawwolf.cunmod= 1.0
    clawwolf.attacklist["male"].append(MWolfClaw)
    clawwolf.attacklist["female"].append(FWolfClaw)
    activeMission= Mission()
    selectorActive= []
    #combat
    missionArmyP= Army([], [])
    missionArmyE= Army([], [])
