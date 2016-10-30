init 1 python:
    #imports
    import os
    import random
    import pygame
    
    #variables
    pregOpen= False
     #monsters
    breedMonster1= None
    breedMonster2= None
    rename= None
    monsterList1= []
    monsterList2= []
    player= Player()
     #fetishes
    gay= True
    straight= True
    lesbian= True
    herms= True
    anal= True
    vaginal= True
    oral= True
    bondage= True
    zoophilia= True
    sceneTags= {}
     #other
    pregChanceGlobal= 0
    exhaust= True
    incest= True
    viewYoung= False
    birthInt= 0
    barnMenu= False
    selectedSave= None
    sellText= None
    
    #classes
    class MissionCard(renpy.Displayable):
        "A mission representation"
        def __init__(self, mis, **kwargs):
            super(MissionCard, self).__init__(**kwargs)
            self.mission= mis
            self.selected= False
            self.hoverCheck= False
            self.width= 300
            self.height= 150
            
        def render(self, width, height, st, at):
            render= renpy.Render(self.width, self.height)
            if (self.selected):
                mcBack= renpy.render(Image("data/menu/breed/mcardBack.png"), width, height, st, at)
            else:
                mcBack= renpy.render(Image("data/menu/breed/bcardBack.png"), width, height, st, at)
            textN= renpy.render(Text(self.mission.title, color= (0,0,0), font= "SegoeBold.ttf", size= 25), width, height, st, at)
            if (self.mission.scouted):
                textE= renpy.render(Text(self.mission.enemyClass, color= (0,0,0), font= "SegoeBold.ttf", size= 20), width, height, st, at)
            else:
                textE= renpy.render(Text("Not scouted", color= (0,0,0), font= "SegoeBold.ttf", size= 20), width, height, st, at)
            #rendering
            render.blit(mcBack, (0, 0))
            render.blit(textN, (10, 5))
            #stats
            render.blit(textE, (10, 40))
            return render
           
        def event(self, ev, x, y, st):
            if (ev.type== pygame.MOUSEBUTTONDOWN):
                if (x> 0 and x< self.width and y> 0 and y< self.height):
                    if (ev.button== 1):
                        global activeMission
                        global missionArmyP
                        global missionArmyE
                        activeMission= self.mission
                        missionArmyP= activeMission.presetArmyP
                        missionArmyE= activeMission.presetArmyE
                        renpy.show_screen("mission")
            if (ev.type== pygame.MOUSEBUTTONUP and ev.button== 1):
                if (x> 0 and x< self.width and y> 0 and y< self.height):   
                    renpy.restart_interaction()
                        
    class SaveCard(renpy.Displayable):
        "A save file representation"
        def __init__(self, slo= 0, **kwargs):
            super(SaveCard, self).__init__(**kwargs)
            self.width= 500
            self.height= 100
            self.slot= slo
            self.name= "New Slot"
            self.date= ""
            self.money= ""
            self.chapter= ""
            self.region= ""
            self.mission= ""
            self.portrait= "data/monster/player/caucasian/male/portrait.png"
            self.knownMonsters= []
            
        def render(self, width, height, st, at):
            global selectedSave
            render= renpy.Render(self.width, self.height)
            if (selectedSave== self):
                back= renpy.render(Image("data/menu/options/saveCardS.png"), width, height, st, at)
            else:
                back= renpy.render(Image("data/menu/options/saveCard.png"), width, height, st, at)
            textN= renpy.render(Text(self.name, color= (0,0,0), size= 25, font= "SegoeBold.ttf"), width, height, st, at)
            textD= renpy.render(Text(self.date, color= (0,0,0), size= 20, font= "SegoeBold.ttf"), width, height, st, at)
            textM= renpy.render(Text(self.money, color= (0,0,0), size= 15, font= "SegoeBold.ttf"), width, height, st, at)
            offXD= 385- (20* len(self.name)/ 2)
            offXM= 385- (16* len(self.date)/ 2)
            render.blit(back, (0, 0))
            render.blit(textN, (20, 2))
            render.blit(textD, (offXD, 20))
            render.blit(textM, (offXM, 50))
            xM= 0
            for monster in self.knownMonsters:
                iconM= renpy.render(im.Scale("data/gene/main/species/"+ monster+ ".png", 50, 50), width, height, st, at)
                render.blit(iconM, (10+ xM, 40))
                xM+= 60
            return render
            
        def event(self, ev, x, y, st):
            global selectedSave
            if (ev.type== pygame.MOUSEBUTTONDOWN and ev.button== 1 and x> 0 and x< self.width and y> 0 and y< self.height):
                selectedSave= self
                for save in saveList:
                    renpy.redraw(save, 0)
                renpy.restart_interaction()

    class TraitPicker(renpy.Displayable):
        "a window for picking traits and charms"
        def __init__(self, tra= [],**kwargs):
            super(TraitPicker, self).__init__(**kwargs)
            self.width= 1300
            self.height= 1000
            self.target= None
            self.active= False
            self.traits= tra
            
        def render(self, width, height, st, at):
            render= renpy.Render(self.width, self.height)
            if (self.active):
                back= renpy.render(Image("data/other/pickBack.png"), width, height, st, at)
                render.blit(back, (200, 50))
                x=0
                y=0
                for trait in self.traits:
                    rend= renpy.render(trait, width, height, st, at)
                    render.blit(rend, (300+ (100* x), 200+ (100* y)))
                    x+= 1
                    if (x> 6):
                        x= 0
                        y+= 1
            return render
            
        def event(self, ev, x, y, st):
            if (self.active):
                if (ev.type== pygame.MOUSEBUTTONDOWN):
                    xO= 0
                    yO= 0
                    for trait in self.traits:
                        trait.event(ev, x- (300+ (100* xO)), y- (200+ (100* yO)), st)
                        xO+= 1
                        if (xO> 7):
                            xO= 0
                            yO+= 1
            
    class TraitBox(renpy.Displayable):
        "displays a trait"
        def __init__(self, tra= "", typ= "", lvl= 1, act= False, ros= False, frm= "regular", **kwargs):
            super(TraitBox, self).__init__(**kwargs)
            self.trait= tra
            self.level= lvl
            self.type= typ
            self.rosette= ros
            self.active= act
            self.form= frm
            if (self.type== "filter" or self.type== "picker"):
                if (self.form== "gender"):
                    self.width= 81
                    self.height= 68
                elif (self.form== "breed"):
                    self.width= 93
                    self.height= 87
                else:
                    self.width= 80
                    self.height= 30
            else:
                self.width= 100
                self.height= 20
            
        def render(self, width, height, st, at):
            render= renpy.Render(self.width, self.height)
            if (self.type== "filter" or self.type== "picker"):
                if (self.form== "regular"):
                    box= renpy.render(Image("data/other/traitBox.png"), width, height, st, at)
                    tex= renpy.render(Text(self.trait, size= 15, font= "SegoeBold.ttf", color= (0,0,0)), width, height, st, at)
                    render.blit(box, (0, 0))
                    render.blit(tex, (10, 0))
                elif (self.form== "gender"):
                    box= renpy.render(Image("data/gene/main/gender/"+ self.trait+ ".png"), width, height, st, at)
                    render.blit(box, (0, 0))
                elif (self.form== "breed"):
                    box= renpy.render(Image("data/gene/main/species/"+ self.trait+ ".png"), width, height, st, at)
                    render.blit(box, (0, 0))
                
            else:
                box= renpy.render(Image("data/other/traitBoxL.png"), width, height, st, at)
                if (self.active):
                    if (self.level>0 and self.level< 4 and self.rosette== True):
                        rank= renpy.render(Image("data/other/waxRank"+ str(self.level)+".png"), width, height, st, at)
                    else:
                        rank= renpy.render(Text(str(self.level), size= 15, bold= True, color= (50,50,50)), width, height, st, at)
                else:
                    rank= renpy.render(Image("data/other/waxRank0.png"), width, height, st, at)
                tex= renpy.render(Text(self.trait, size= 15, font= "SegoeBold.ttf", color= (0,0,0)), width, height, st, at)
                render.blit(box, (0, 0))
                render.blit(rank, (5, 3))
                render.blit(tex, (30, -3))
            return render
            
        def event(self, ev, x, y, st):
            if (ev.type== pygame.MOUSEBUTTONDOWN and ev.button== 1 and x>0 and x<self.width and y>0 and y<self.height):
                if (self.type== "filter"):
                    global traitPick
                    if (self.form== "gender"):
                        traitPick.traits= traitListGender
                    elif (self.form== "breed"):
                        traitPick.traits= traitListBreed
                    else:
                        traitPick.traits= traitListRegular
                    traitPick.active= True
                    traitPick.target= self
                    renpy.redraw(traitPick, 0)
                elif (self.type== "picker"):
                    traitPick.active= False
                    traitPick.target.trait= self.trait
                    renpy.redraw(traitPick.target, 0)
                    traitPick.target= None
                    renpy.redraw(traitPick, 0)
                    if (len(monsterList1)> 0 and monsterList1[0].mode== "breeding"):
                        showBreed()
                        renpy.restart_interaction()
                    elif (len(monsterList1)> 0 and monsterList1[0].mode== "viewer"):
                        showViewer()
                        renpy.restart_interaction()
                    elif (len(monsterList1)> 0 and monsterList1[0].mode== "request"):
                        showRequest()
                        renpy.restart_interaction()
                    elif (len(monsterList1)> 0 and monsterList1[0].mode== "combat"):
                        showCombat()
                        renpy.restart_interaction()     
            return None   
        
    class FilterMonster(renpy.Displayable):
        "filter for monster selection"
        def __init__(self, **kwargs):
            super(FilterMonster, self).__init__(**kwargs)
            self.width= 350
            self.height= 100
            self.gender= "any"
            self.breed= "any"
            self.bredInt= 0
            self.genInt= 0
            self.genderCharm= TraitBox(tra= "any", typ= "filter", frm= "gender")
            self.breedCharm= TraitBox(tra= "any", typ= "filter", frm= "breed")
            self.traits= [TraitBox("any", "filter"), TraitBox("any", "filter"), TraitBox("any", "filter")]
            
        def render(self, width, height, st, at):
            render= renpy.Render(self.width, self.height)
            toke1= renpy.render(self.genderCharm, width, height, st, at)
            toke2= renpy.render(self.breedCharm, width, height, st, at)
            render.blit(toke1, (7, 5))
            render.blit(toke2, (96, 2))
            y= 0
            for trait in self.traits:
                renpy.redraw(trait, 0)
                traitR= renpy.render(trait, width, height, st, at)
                render.blit(traitR, (238, 5+ y))
                y+= 35
            return render
            
        def event(self, ev, x, y, st):
            if (ev.type== pygame.MOUSEBUTTONDOWN and ev.button== 1 and x> 0 and x< self.width and y>0 and y< self.height):
                if (x> 7 and x< 88 and y> 5 and y< 73):
                    self.genderCharm.event(ev, x- 7, y- 5, st)
                    renpy.redraw(self, 0)
                elif (x> 96 and x< 189 and y> 2 and y< 87):
                    self.breedCharm.event(ev, x- 96, y- 2, st)
                    renpy.redraw(self, 0)
                elif (x>240 and x< self.width and y> 0 and y< self.height):
                    yO= 0
                    for trait in self.traits:
                        trait.event(ev, x- 240, y- (10+ yO), st)
                        yO+= 35
                    renpy.redraw(self, 0)
                if (len(monsterList1)> 0 and monsterList1[0].mode== "breeding"):
                    showBreed()
                    renpy.restart_interaction()
                elif (len(monsterList1)> 0 and monsterList1[0].mode== "viewer"):
                    showViewer()
                    renpy.restart_interaction()
                elif (len(monsterList1)> 0 and monsterList1[0].mode== "request"):
                    showRequest()
                    renpy.restart_interaction()
            return None
            
            
    class BlockScroll(renpy.Displayable):
        "custom scroller"
        def __init__(self, w, h, x, y, sx, sy, itW, itH, c, r, l,  **kwargs):
            super(BlockScroll, self).__init__(**kwargs)
            self.width= w
            self.height= h
            self.offX= x
            self.offY= y
            self.offsetX= []
            self.offsetY= []
            self.spaceX= sx
            self.spaceY= sy
            self.columns= c
            self.rows= r
            self.itemList= l
            self.rowMin= 0
            self.rowMax= self.rows
            self.itemWidth= 0
            self.itemHeight= 0
            self.itemWidth= itW
            self.itemHeight= itH

        def render(self, width, height, st, at):
           render= renpy.Render(self.width, self.height)
           x=0
           y=0
           self.offsetX= []
           self.offsetY= []
           topItem= None
           for item in self.itemList[self.rowMin:self.rowMax]:
              if (isinstance(item, Gene)):
                rend= renpy.render(item.icon, width, height, st ,at)
                textR= renpy.render(Text(item.name, size= 10, font= "SegoeBold.ttf"), width, height, st, at)
                rendX= self.offX+ x* (self.itemWidth+ self.spaceX)
                rendY= self.offY+ y* (self.itemHeight+ self.spaceY)
                self.offsetX.append(rendX)
                self.offsetY.append(rendY)
                render.blit(rend, (rendX, rendY))
                render.blit(textR, (rendX+ 5, rendY+ 5))
                x+= 1
                if (x>= self.columns):
                          x= 0
                          y+= 1
              elif (isinstance(item, renpy.Displayable)):
                       rend= renpy.render(item, width, height, st ,at)
                       rendX= self.offX+ x* (self.itemWidth+ self.spaceX)
                       rendY= self.offY+ y* (self.itemHeight+ self.spaceY)
                       self.offsetX.append(rendX)
                       self.offsetY.append(rendY)
                       render.blit(rend, (rendX, rendY))
                       x+= 1
                       if (x>= self.columns):
                          x= 0
                          y+= 1
           #scroll arrows
           up= renpy.render(Image("data/other/arrowSmall.png"), width, height, st ,at)    
           down= renpy.render(Image(im.Flip("data/other/arrowSmall.png", vertical= True)), width, height, st ,at)
           render.blit(up, ((self.itemWidth+ self.spaceX)* self.columns+ self.offX, 0))
           render.blit(down, ((self.itemWidth+ self.spaceX)* self.columns+ self.offX, self.height/ 2))
           return render
           
        def event(self, ev, x, y, st):
               for item in self.itemList[self.rowMin:self.rowMax]:
                   if (isinstance(item, renpy.Displayable)):
                         i= self.itemList.index(item)- self.rowMin
                         offX= self.offsetX[i]
                         offY= self.offsetY[i]
                         item.event(ev, x- offX, y- offY, st)
               if (ev.type== pygame.MOUSEBUTTONDOWN and ev.button== 1):
                   if (x> (self.itemWidth+ self.spaceX)* self.columns+ self.offX and x< self.width and y> self.height/ 2 and y< self.height):
                             self.rowMin+= self.rows
                             self.rowMax+= self.rows
                             if (self.rowMax> len(self.itemList)):
                                 self.rowMin=  len(self.itemList)- 6
                                 self.rowMax=  len(self.itemList)
                   elif (x> (self.itemWidth+ self.spaceX)* self.columns+ self.offX and x< self.width and y> 0 and y< self.height/ 2):
                             self.rowMin-= self.rows
                             self.rowMax-= self.rows
                             if (self.rowMin<0):
                                 self.rowMin= 0
                                 self.rowMax= self.rows
                   renpy.redraw(self, 0)    
            
    class BreedView(renpy.Displayable):
        "idle image selector for monsters in breeding window"
        def __init__(self, mul, **kwargs):
            super(BreedView, self).__init__(**kwargs)
            self.width= 1300
            self.height= 1000
            self.multi= mul
            
        def render(self, width, height, st, at):
            render= renpy.Render(self.width, self.height)
            if (breedMonster1!= None):
                if (self.multi):
                    monsterIdle1Rend= renpy.render(Image(im.Flip(im.Scale("data/monster/"+ breedMonster1.species.species+ "/"+ breedMonster1.variant+ "/"+ breedMonster1.gender+ "/idle.png", 350, 350), horizontal= True)), width, height, st, at)
                    render.blit(monsterIdle1Rend, (350, 150))
                else:
                    monsterIdle1Rend= renpy.render(Image(im.Scale("data/monster/"+ breedMonster1.species.species+ "/"+ breedMonster1.variant+ "/"+ breedMonster1.gender+ "/idle.png", 500, 500)), width, height, st, at)
                    render.blit(monsterIdle1Rend, (750, 300)) 
            if (self.multi and breedMonster2!= None):
               monsterIdle2Rend= renpy.render(Image(im.Scale("data/monster/"+ breedMonster2.species.species+ "/"+ breedMonster2.variant+ "/"+ breedMonster2.gender+ "/idle.png", 350, 350)), width, height, st, at)
               render.blit(monsterIdle2Rend, (600, 450))
            return render
           
        def event(self, ev, x, y, st):
            return None
            
    class BreedCard(renpy.Displayable):
        "displayable for monsters in breeding window"
        def __init__(self, monster, p1, mod, vew, **kwargs):
            super(BreedCard, self).__init__(**kwargs)
            self.monster= monster
            self.mode= mod
            self.viewer= vew
            self.selected= False
            self.hoverCheck= False
            self.width= 300
            self.height= 150
            self.part1= p1
            
        def render(self, width, height, st, at):
            render= renpy.Render(self.width, self.height)
            mcBack= renpy.render(Image("data/menu/breed/bcardBack.png"), width, height, st, at)
            textN= renpy.render(Text(self.monster.name, color= (0,0,0), font= "SegoeBold.ttf", size= 20), width, height, st, at)
            textSFr= renpy.render(Text("Fer:"+ str(int(self.monster.ferocity)), color= (0,0,0), size= 15, font= "SegoeBold.ttf"), width, height, st, at)
            textSFi= renpy.render(Text("Fin:"+ str(int(self.monster.finesse)), color= (0,0,0), size= 15, font= "SegoeBold.ttf"), width, height, st, at)
            textSDe= renpy.render(Text("Det:"+str(int(self.monster.determination)), color= (0,0,0), size= 15, font= "SegoeBold.ttf"), width, height, st, at)
            textSCu= renpy.render(Text("Cun:"+ str(int(self.monster.cunning)), color= (0,0,0), size= 15, font= "SegoeBold.ttf"), width, height, st, at)
            if (self.mode== "request"):
                textSSt= renpy.render(Text("Val:"+ str(self.monster.valueM), color= (50,50,0), size= 15, font= "SegoeBold.ttf"), width, height, st, at)
            else:
                textSSt= renpy.render(Text("End:"+ str(self.monster.stamina), color= (0,0,0), size= 15, font= "SegoeBold.ttf"), width, height, st, at)
            traitScroller= renpy.display.viewport.VPGrid(cols= 1)
            traitScroller.edgescroll= (20, 50)
            for gene in self.monster.genes:
                traitScroller.children.append(TraitBox(tra= gene.name, lvl= gene.power, act=gene.active, ros= "trait" in gene.effect))
            scrollTrait= renpy.render(traitScroller, width, height, st, at)
            #rendering
            render.blit(mcBack, (0, 0))
            if (self.mode== "request" and self.part1== False):
                rendB= renpy.render(Image("data/menu/request/species/"+ self.monster.species.species+ ".png"), width, height, st, at)
                rendG= renpy.render(Image("data/menu/request/gender/"+ self.monster.gender+ ".png"), width, height, st, at)
                render.blit(rendG, (5, 35))
                render.blit(rendB, (15, 45))
            else:
                port= renpy.render(Image("data/monster/"+ self.monster.species.species+ "/"+ self.monster.variant+ "/"+ self.monster.gender+"/portrait.png"), width, height, st, at)
                render.blit(port, (15, 45))
            render.blit(textSSt,  (120, 120))
            circle= None
            if (self.mode== "breeding" or self.mode== "request"):
                if (self.part1 and breedMonster1!= None and self.monster== breedMonster1):
                    circle= renpy.render(Image("data/menu/breed/bcardBack1.png"), width, height, st, at)
                elif (not self.part1 and self.monster== breedMonster2):
                    circle= renpy.render(Image("data/menu/breed/bcardBack2.png"), width, height, st, at)
            else:
                if (self.selected):
                    circle= renpy.render(Image("data/menu/breed/bcardBack1.png"), width, height, st, at)
                else:
                    circle= None
            if (circle!= None):
                render.blit(circle, (0, 5))
            render.blit(textN, (25, 5))
            #stats
            render.blit(textSFr, (120, 40))
            render.blit(textSFi, (120, 60))
            render.blit(textSDe, (120, 80))
            render.blit(textSCu,  (120, 100))
            render.blit(scrollTrait, (190, 10))
            return render
           
        def event(self, ev, x, y, st):
            global breedMonster1
            global  breedMonster2
            global currentPair
            if (ev.type== pygame.MOUSEMOTION or ev.type== pygame.MOUSEBUTTONDOWN):
                if (x> 0 and x< self.width and y> 0 and y< self.height):
                    if (ev.type== pygame.MOUSEBUTTONDOWN and ev.button== 3):
                        if (self.mode== "combat" and self.selected and self.monster in selectorActive):
                            selectorActive.remove(self.monster)
                        self.selected= False
                        if (self.part1):
                            breedMonster1= None
                        else:
                            breedMonster2= None
                        if (self.viewer!= None):
                            renpy.redraw(self.viewer, 0)
                        renpy.redraw(self, 0)
                        if (self.mode== "breeding"):
                                showBreed()
                                renpy.restart_interaction()
                        elif (self.mode== "request"):
                                showRequest()
                                renpy.restart_interaction()
                        elif (self.mode== "combat"):
                                renpy.restart_interaction()
                        elif (self.mode== "viewer"):
                                global barnMenu
                                barnMenu= False
                                renpy.restart_interaction()
                    if (ev.type== pygame.MOUSEBUTTONDOWN and ev.button== 1):
                        if (x< self.width* 0.8):
                            if (self.mode== "breeding" or self.mode== "request"):
                                if (self.part1):
                                    for monster in monsterList1:
                                        if (monster.selected):
                                            monster.selected= False
                                            renpy.redraw(monster, 0)
                                    breedMonster1= self.monster
                                    self.selected= True
                                else:
                                    for monster in monsterList2:
                                        if (monster.selected):
                                            monster.selected= False
                                            renpy.redraw(monster, 0)
                                    breedMonster2= self.monster
                                    self.selected= True
                            elif (self.mode== "combat"):
                               if (len(selectorActive)< activeMission.maxTeam):
                                    if (self.selected== False):
                                        selectorActive.append(self.monster)  
                                    self.selected= True
                            elif (self.mode== "viewer"):
                                for monster in monsterList1:
                                    if (monster.selected):
                                            monster.selected= False
                                            renpy.redraw(monster, 0)
                                self.selected= True
                                breedMonster1= self.monster
                            if (self.viewer!= None):
                                renpy.redraw(self.viewer, 0)
                            renpy.redraw(self, 0)
                            if (self.mode== "breeding"):
                                currentPair= False
                                showBreed()
                                renpy.restart_interaction()
                            elif (self.mode== "request"):
                                showRequest()
                                renpy.restart_interaction()
                            elif (self.mode== "combat"):
                                renpy.restart_interaction()
                            elif (self.mode== "viewer"):
                                global barnMenu
                                barnMenu= False
                                renpy.restart_interaction()
            return None
            
           
    #functions
    def randomColor(limits):
        "generates a random color with RGB limits passed as a list"
        return (random.randint(limits[0], limits[1]), random.randint(limits[2], limits[3]), random.randint(limits[4], limits[5]))
      
    def viable(monster1, monster2):
        "checks if monster1 can get pregnant"
        if (monster1.gender== "male" or monster2.gender== "female"):
            return False
        else:
            for gene in monster1.genes:
                if (gene.name== "Pregnant"):
                    return False
        return True
        
    def impregnate(monster1, monster2):
         "Starts monster1's pregnancy"
         if (viable(monster1, monster2)):
             monster1.addGene(Gene("data/gene/status/pregnant.png", "Pregnant", "Baby due in ", "status|fertility(0)", 3, " days.", True))
             monster1.pregChild= newMonsterBred(monster1, monster2)
             monster1.applyGenes()
             monster1.relatives.append(monster1.pregChild)
             monster2.relatives.append(monster1.pregChild)
             monster1.pregChild.relatives.append(monster1)
             monster1.pregChild.relatives.append(monster2)
             for monster in playerMonsters:
                 if (len(monster.relatives)> 1 and (monster1.pregChild.relatives[0]== monster.relatives[0] or monster1.pregChild.relatives[1]== monster.relatives[1])):
                     monster1.pregChild.relatives.append(monster)
                     monster.relatives.append(monster1.pregChild)
             for monster in youngMonsters:
                 if (len(monster.relatives)> 1 and (monster1.pregChild.relatives[0]== monster.relatives[0] or monster1.pregChild.relatives[1]== monster.relatives[1])):
                     monster1.pregChild.relatives.append(monster)
                     monster.relatives.append(monster1.pregChild)
             if (monster2.pregChild!= None):
                 monster1.pregChild.relatives.append(monster2.pregChild)
                 monster2.pregChild.relatives.append(monster1.pregChild)
             return True
         else:
            return False
    
#monster generators
    def newMonsterRequest():
        "creates a random monster request"
        temp= Monster()
        if (random.randint(0, 100)< 25):
            spec= [v for v in knownSpecies.values()]
            temp.species= spec[random.randint(0, len(spec)- 1)]
        if (random.randint(0, 100)< 25):
            temp.variant= knownVariants[random.randint(0, len(knownVariants)- 1)]
        if (random.randint(0, 100)< 25):
            genRan= random.randint(0, 100)
            if (genRan< temp.species.hermLim):
                temp.gender= "hermaphrodite"
            elif (genRan< temp.species.femLim):
                temp.gender= "female"
            else:
                temp.gender= "male"
        if (random.randint(0, 100)< 25):
            temp.ferocity= random.randint(10, 200)
        if (random.randint(0, 100)< 25):
            temp.finesse= random.randint(10, 200)
        if (random.randint(0, 100)< 25):
            temp.determination= random.randint(10, 200)
        if (random.randint(0, 100)< 25):
            temp.cunning= random.randint(10, 200)
        if (len(temp.species.genes)> 0):
            lengen= random.randint(0,  len(temp.species.genes))
            gen2= random.randint(0, 3)
            genMatch= False
            while (gen2> 0):
                gene= temp.species.genes[gen]
                gen= random.randint(0, len(temp.species.genes))
                for gene2 in temp.genes:
                    if (gene.name == gene2.name):
                        genMatch= True
                        if (genMatch == False):
                            temp.genes.append(gene)
                        else:
                            genMatch= False
            gen2-= 1
        temp.addGene(Gene("data/gene/main/variant/wild.png", "test1", "A test",  "trait|testing", 1, " lvl", True))
        temp.calcValue()
        temp.calcFertility()
        temp.calcEndurance()
        temp.stamina= temp.maxStamina
        return temp
    
    def newMonsterWild(species):
        "creates a random monster of the species"
        global currentID
        temp= Monster()
        currentID+= 1
        temp.intID= currentID
        temp.species= species
        temp.variant= "wild"
        temp.base= random.randint(0, species.baseVars)
        temp.baseColor= randomColor(species.base)
        temp.hair= random.randint(0, species.hairVars)
        temp.hairColor= randomColor(species.hair)
        temp.marking= random.randint(0,species.markingVars)
        temp.markingColor= randomColor(species.mark)
        genRan= random.randint(0, 100)
        if (genRan< temp.species.hermLim):
            temp.gender= "hermaphrodite"
        elif (genRan< temp.species.femLim):
            temp.gender= "female"
        else:
            temp.gender= "male"
        temp.ferocity= random.randint(10* species.ferMod, 50* species.ferMod)+ 0.0
        temp.finesse= random.randint(10* species.finMod, 50* species.finMod)+ 0.0
        temp.determination= random.randint(10* species.detMod, 50* species.detMod)+ 0.0
        temp.cunning= random.randint(10* species.cunMod, 50* species.cunMod)+ 0.0
        temp.calcFertility()
        if (len(species.genes)> 0):
            lengen= random.randint(0,  len(species.genes))
            gen2= random.randint(0, 3)
            genMatch= False
            while (gen2> 0):
                gene= species.genes[gen]
                gen= random.randint(0, len(species.genes))
                for gene2 in temp.genes:
                    if (gene.name == gene2.name):
                        genMatch= True
                        if (genMatch == False):
                            temp.genes.append(gene)
                        else:
                            genMatch= False
            gen2-= 1
        temp.addGene(Gene("data/gene/main/variant/wild.png", "test1", "A test",  "trait|testing", 1, " lvl", True))
        temp.calcValue
        temp.calcFertility()
        temp.calcEndurance()
        temp.stamina= temp.maxStamina
        return temp
        
    def newMonsterBred(parent1, parent2):
        "creates a monster based on two other monsters"
        temp= Monster()
        global currentID
        currentID+= 1
        temp.intID= currentID
        #basics (species, variant, gender)
        temp.variant= "wild"
        if (random.randint(0,100)< 50):
            if (parent1.species.species!= "player"):
                temp.species= parent1.species
            else:
                temp.species= parent2.species
        else:
            if (parent2.species.species!= "player"):
                temp.species= parent2.species
            else:
                temp.species= parent1.species
        genRan= random.randint(0, 100)
        if (genRan< temp.species.hermLim):
            temp.gender= "hermaphrodite"
        elif (genRan< temp.species.femLim):
            temp.gender= "female"
        else:
            temp.gender= "male"
        #appearance: style
        if (random.randint(0,100)< 50):
            temp.base= parent1.base
        else:
            temp.base= parent2.base
        if (random.randint(0,100)< 50):
            temp.hair= parent1.hair
        else:
            temp.hair= parent2.hair
        if (random.randint(0,100)< 50):
            temp.marking= parent1.marking
        else:
            temp.marking= parent2.marking
        if (temp.base> temp.species.baseVars):
            temp.base= temp.species.baseVars
        if (temp.hair> temp.species.hairVars):
            temp.hair= temp.species.hairVars
        if (temp.marking> temp.species.markingVars):
            temp.marking= temp.species.markingVars
        #appearance: color
        if (random.randint(0,100)< 50):
            temp.baseColor= parent1.baseColor
        else:
            temp.baseColor= parent2.baseColor
        if (random.randint(0,100)< 50):
            temp.hairColor= parent1.hairColor
        else:
            temp.hairColor= parent2.hairColor
        if (random.randint(0,100)< 50):
            temp.markingColor= parent1.markingColor
        else:
            temp.markingColor= parent2.markingColor
        #stats
        tempStatRan= random.randint(0, 100)
        temp.ferocity= (parent1.ferocity* tempStatRan+ parent2.ferocity* (100- tempStatRan))/ 100
        temp.ferocity+= int(random.randint(-20, 20)* (temp.ferocity/ 100.0))
        if (temp.ferocity> 250):
            temp.ferocity= 250
        tempStatRan= random.randint(0, 100)
        temp.finesse= (parent1.finesse* tempStatRan+ parent2.finesse* (100- tempStatRan))/ 100
        temp.finesse+= int(random.randint(-20, 20)* (temp.finesse/ 100.0))
        if (temp.finesse> 250):
            temp.finesse= 250
        tempStatRan= random.randint(0, 100)
        temp.determination= (parent1.determination* tempStatRan+ parent2.determination* (100- tempStatRan))/ 100
        temp.determination+= int(random.randint(-20, 20)* (temp.determination/ 100.0))
        if (temp.determination> 250):
            temp.determination= 250
        tempStatRan= random.randint(0, 100)
        temp.cunning= (parent1.cunning* tempStatRan+ parent2.cunning* (100- tempStatRan))/ 100
        temp.cunning+= int(random.randint(-20, 20)* (temp.cunning/ 100.0))
        if (temp.cunning> 250):
            temp.cunning= 250
        #genes
        for gene in parent1.genes:
            if ("status" not in gene.effect):
                foundGene= False
                for gene2 in parent2.genes:
                        if (gene2.name == gene.name):
                            averagePower= (gene.power+ gene2.power)/ 2
                            if (random.randint(0, 100)< 10):
                                averagePower+= 1
                            if (averagePower> 3):
                                averagePower= 3
                            if (gene.active):
                                if (gene2.active):
                                    temp.addGene(Gene(gene.icon, gene.name, gene.description, gene.effect, averagePower, gene.unit, True))
                                else:
                                    if (random.randint(0,100)< 50):
                                        temp.addGene(Gene(gene.icon, gene.name, gene.description, gene.effect, averagePower, gene.unit, True))
                                    else:
                                        temp.addGene(Gene(gene.icon, gene.name, gene.description, gene.effect, averagePower, gene.unit, False))
                            else:
                                if (gene2.active):
                                    if (random.randint(0,100)< 50):
                                        temp.addGene(Gene(gene.icon, gene.name, gene.description, gene.effect, averagePower, gene.unit, True))
                                    else:
                                        temp.addGene(Gene(gene.icon, gene.name, gene.description, gene.effect, averagePower, gene.unit, False))
                                else:
                                    if (random.randint(0,100)< 25):
                                        temp.addGene(Gene(gene.icon, gene.name, gene.description, gene.effect, averagePower, gene.unit, True))
                                    else:
                                        if (random.randint(0,100)< 75):
                                            temp.addGene(Gene(gene.icon, gene.name, gene.description, gene.effect, averagePower, gene.unit, False))
                            foundGene= True
                            break
                if (foundGene== False):
                    if (gene.active):
                        temp.addGene(Gene(gene.icon, gene.name, gene.description, gene.effect, gene.power/2, gene.unit, False))
                    else:
                        if (random.randint(0,100)< 50):
                            temp.addGene(Gene(gene.icon, gene.name, gene.description, gene.effect, gene.power/2, gene.unit, False))
        temp.addGene(Gene("data/gene/status/child.png", "Young", "Monster ages up in ", "status|fertility(0)", 5, " days", True))
        temp.calcFertility()
        temp.calcEndurance()
        temp.stamina= temp.maxStamina
        return temp
    
    def giveBirth2():
        global birthInt
        global rename
        for monster in playerMonsters[birthInt:]:
            for gene in monster.genes:
                if (gene.name== "Pregnant" and gene.power< 1):
                    monster.genes.remove(gene)
                    rename= monster.pregChild
                    renpy.show_screen("birth", name= monster.name, monster= monster.pregChild)
                    renpy.restart_interaction()
                    youngMonsters.append(monster.pregChild)
                    monster.pregChild= None
                    monster.calcFertility()
                    birthInt+= 1
                    break
        
    def giveBirth():
        global birthInt
        global rename
        for monster in playerMonsters[birthInt:]:
            for gene in monster.genes:
                if (gene.name== "Pregnant" and gene.power< 1):
                    monster.genes.remove(gene)
                    rename= monster.pregChild
                    renpy.show_screen("birth", name= monster.name, monster= monster.pregChild)
                    renpy.restart_interaction()
                    youngMonsters.append(monster.pregChild)
                    monster.pregChild= None
                    monster.calcFertility()
                    birthInt+= 1
                    return True
            return False
            
    def advanceDayLaird():
        "starts a new day"
        renpy.show_screen("fadeSleeper")
        global gameDay
        global gameMonth
        global gameHour
        global gameMinute
        global rename
        global birthInt
        global requestedMonsters
        global availableMissions
        birthInt= 0
        gameDay+= 1
        if (gameDay> 30):
            gameDay= 1
            gameMonth+= 1
            if (gameMonth> 12):
                gameMonth= 1
        gameHour= 6
        gameMinute= 0
        for monster in playerMonsters:
            monster.health= monster.maxHealth
            monster.calcEndurance()
            monster.stamina= monster.maxStamina
            for gene in monster.genes:
                if ("status" in gene.effect):
                    gene.power-= 1
                    if (gene.power< 1):
                        if (gene.name!= "Pregnant"):
                            monster.genes.remove(gene)
        for monster in youngMonsters:
           for gene in monster.genes:
                if ("status" in gene.effect):
                    gene.power-= 1
                    if (gene.power<= 0):
                        monster.genes.remove(gene)
                        if (gene.name== "Young"):
                            renpy.show_screen("ageUp", name= monster.name)
                            monster.stamina= monster.maxStamina
                            playerMonsters.append(monster)
                            youngMonsters.remove(monster)
                            monster.calcFertility()
                            monster.fertility= monster.fertilityBase
        for monster in playerMonsters:
            if (giveBirth()):
                break
            else:
                birthInt+= 1
        if (gameDay % 10== 0):
            requestedMonsters.append(newMonsterRequest())
            availableMissions.append(newMission())
        if (len(requestedMonsters)> 8):
            requestedMonsters= requestedMonsters[:8]
        if (len(availableMissions)> 8):
            availableMissions= availableMissions[:8]
        for mission in availableMissions:
            mission.decay-= 1
            if (mission.decay<=0 ):
                availableMissions.remove(mission)
        for request in requestedMonsters:
            request.decay-= 1
            if (request.decay<=0 ):
                requestedMonsters.remove(request)
        renpy.restart_interaction()
        
    def updateTimeKeeper():
        renpy.redraw(clock, 0)
        renpy.restart_interaction()
        
    def refreshBreed():
        showBreed()
        renpy.restart_interaction()
        
    def clearFilters():
        global filter1
        global filter2
        filter1= FilterMonster()
        filter2= FilterMonster()
        
    def clearText():
        global sellText
        sellText= None
        
    def showCombat():
        global monsterList1
        global combatMonsters
        monsterList1= []
        for monster in playerMonsters:
            if (monster.species.species!= "player" and (filter1.genderCharm.trait== "any" or monster.gender== filter1.genderCharm.trait) and (filter1.breedCharm.trait== "any" or monster.species.species== filter1.breedCharm.trait)):
                    traitCheck= False
                    for trait in filter1.traits:
                        traitCheck= False
                        if (trait.trait== "any"):
                            traitCheck= True
                        else:
                            for gene in monster.genes:
                                if (gene.name== trait.trait):
                                    traitCheck= True
                                    break
                        if (traitCheck== False):
                           break
                    if (traitCheck): 
                        monsterList1.append(BreedCard(monster, True, "combat", None))
                        if (monster in selectorActive):
                            monsterList1[len(monsterList1)- 1].selected= True
            
    def showViewer():
        global monsterList1
        if (breedMonster1== None):
            global barnMenu
            barnMenu= False
        monsterList1= []
        if (viewYoung):
            for monster in youngMonsters:
                if ((filter1.genderCharm.trait== "any" or monster.gender== filter1.genderCharm.trait) and (filter1.breedCharm.trait== "any" or monster.species.species== filter1.breedCharm.trait)):
                    traitCheck= False
                    for trait in filter1.traits:
                        traitCheck= False
                        if (trait.trait== "any"):
                            traitCheck= True
                        else:
                            for gene in monster.genes:
                                if (gene.name== trait.trait):
                                    traitCheck= True
                                    break
                        if (traitCheck== False):
                           break
                    if (traitCheck): 
                        monsterList1.append(BreedCard(monster, True, "viewer", viewerV))
        else:
            for monster in playerMonsters:
                if ((filter1.genderCharm.trait== "any" or monster.gender== filter1.genderCharm.trait) and (filter1.breedCharm.trait== "any" or monster.species.species== filter1.breedCharm.trait)):
                    traitCheck= False
                    for trait in filter1.traits:
                        traitCheck= False
                        if (trait.trait== "any"):
                            traitCheck= True
                        else:
                            for gene in monster.genes:
                                if (gene.name== trait.trait):
                                    traitCheck= True
                                    break
                        if (traitCheck== False):
                           break
                    if (traitCheck): 
                        monsterList1.append(BreedCard(monster, True, "viewer", viewerV))
    
    def showSaveN():
        global saveList
        saveList= []
        itint= 0
        if not (os.path.exists("saves")):
            os.makedirs("saves")
        for file in os.listdir("saves"):
            temp= SaveCard(slo= itint)
            quickLoad(itint, temp)
            saveList.append(temp)
            itint+= 1
        saveList.append(SaveCard(slo= itint))
        
    def showSave():
        global saveList
        saveList= []
        itint= 0
        if not (os.path.exists("saves")):
            os.makedirs("saves")
        for file in os.listdir("saves"):
            temp= SaveCard(slo= itint)
            quickLoad(itint, temp)
            saveList.append(temp)
            itint+= 1
                        
    def showRequest():
        global monsterList1
        global monsterList2
        monsterList1= []
        monsterList2= []
        for monster in playerMonsters:
            if ((filter1.genderCharm.trait== "any" or monster.gender== filter1.genderCharm.trait) and (filter1.breedCharm.trait== "any" or monster.species.species== filter1.breedCharm.trait)):
                    traitCheck= False
                    for trait in filter1.traits:
                        traitCheck= False
                        if (trait.trait== "any"):
                            traitCheck= True
                        else:
                            for gene in monster.genes:
                                if (gene.name== trait.trait):
                                    traitCheck= True
                                    break
                        if (traitCheck== False):
                           break
                    if (traitCheck): 
                        monster.calcValue()
                        monsterList1.append(BreedCard(monster, True, "request", None))  
        for monster in requestedMonsters:
            monster.calcValue()
            monsterList2.append(BreedCard(monster, False, "request", None))  
        breedMonster1= None
        breedMonster2= None
    
    def toggleIncest():
        global incest
        if (incest):
            incest= False
        else:
            incest= True
            
    def toggleExhaust():
        global exhaust
        if (exhaust):
            exhaust= False
        else:
            exhaust= True
     
    def toggleViewYoung():
        global viewYoung
        if (viewYoung):
            viewYoung= False
        else:
            viewYoung= True
        clearBreedMonsters()
        renpy.redraw(viewerV, 0)
        showViewer()
        renpy.restart_interaction()
            
    def toggleBarnMenu():
        global barnMenu
        if (barnMenu== True):
            barnMenu= False
        else:
            barnMenu= True
        showViewer()
        renpy.restart_interaction()
        
    def clearBreedMonsters():
        global breedMonster1
        global breedMonster2
        breedMonster1= None
        breedMonster2= None
    
    def showBreed():
        global monsterList1
        global monsterList2
        global breedMonster1
        global breedMonster2
        global pregChanceGlobal
        monsterList1= []
        monsterList2= []
        for monster in playerMonsters:
            if ((exhaust== True or monster.stamina> 0)):
                if ((filter1.genderCharm.trait== "any" or monster.gender== filter1.genderCharm.trait) and (filter1.breedCharm.trait== "any" or monster.species.species== filter1.breedCharm.trait) and (incest== True or (breedMonster2== None or monster not in breedMonster2.relatives)) and monster!= breedMonster2):
                    traitCheck= False
                    for trait in filter1.traits:
                        traitCheck= False
                        if (trait.trait== "any"):
                            traitCheck= True
                        else:
                            for gene in monster.genes:
                                if (gene.name== trait.trait):
                                    traitCheck= True
                                    break
                        if (traitCheck== False):
                           break
                    if (traitCheck): 
                        monsterList1.append(BreedCard(monster, True, "breeding", viewerB))
                if ((filter2.genderCharm.trait== "any" or monster.gender== filter2.genderCharm.trait) and (filter2.breedCharm.trait== "any" or monster.species.species== filter2.breedCharm.trait) and (incest== True or (breedMonster1== None or monster not in breedMonster1.relatives)) and monster!= breedMonster1):
                    traitCheck= False
                    for trait in filter2.traits:
                        traitCheck= False
                        if (trait.trait== "any"):
                            traitCheck= True
                        else:
                            for gene in monster.genes:
                                if (gene.name== trait.trait):
                                    traitCheck= True
                                    break
                        if (traitCheck== False):
                           break
                    if (traitCheck): 
                        monsterList2.append(BreedCard(monster, False, "breeding", viewerB))
            if (breedMonster1!= None and breedMonster2!= None):
                if ((breedMonster1.gender== "hermaphrodite" or breedMonster2.gender== "hermaphrodite") or (breedMonster1.gender== "male" and breedMonster2.gender== "female") or (breedMonster1.gender== "female" and breedMonster2.gender== "male")):
                    if (breedMonster1.fertility> 0 and breedMonster2.fertility> 0):
                        pregChanceGlobal= (breedMonster1.fertility+ breedMonster2.fertility)/ 2
                    else:
                        pregChanceGlobal= 0
                else:
                    pregChanceGlobal= 0
            else:
                pregChanceGlobal= 0
        
    def startSex():
        global gameHour
        global currentPair
        if (gameHour< 23 and breedMonster1!= None and breedMonster2!= None and breedMonster1!= breedMonster2 and breedMonster1.stamina>0 and breedMonster2.stamina> 0):
                gameHour+= 1
                breedMonster1.stamina-= 1
                breedMonster2.stamina-= 1
                currentPair= True
                calcTraining(breedMonster1, breedMonster2)
                calcTraining(breedMonster2, breedMonster1)
                if (gameHour> 24):
                    advanceDayLaird()
                #get scene
                permitted= True
                if (breedMonster1.gender== "male" and breedMonster2.gender== "male" and gay== False):
                    permitted= False
                if (breedMonster1.gender== "female" and breedMonster2.gender== "female" and lesbian== False ):
                    permitted= False
                if (((breedMonster1.gender== "female" and breedMonster2.gender== "male") or (breedMonster2.gender== "female" and breedMonster1.gender== "male")) and straight== False):
                    permitted= False
                if ((breedMonster1.gender== "hermaphrodite" or breedMonster2.gender== "hermaphrodite") and herms== False):
                    permitted= False
                if ((breedMonster1.variant== "wild" or breedMonster2.variant== "wild") and zoophilia== False):
                    permitted= False
                animString= breedMonster1.species.species+ breedMonster1.gender+ "X"+ breedMonster2.species.species+ breedMonster2.gender
                i= 0
                checkExists= renpy.has_image(animString+ str(i))
                if (checkExists== False):
                    animString= breedMonster2.species.species+ breedMonster2.gender+ "X"+ breedMonster1.species.species+ breedMonster1.gender
                    checkExists= renpy.has_image(animString+ str(i))
                if (checkExists):
                    if ("oral" in sceneTags[animString] and oral== False):
                        permitted= False
                    if ("vaginal" in sceneTags[animString] and vaginal== False):
                        permitted= False
                    if ("anal" in sceneTags[animString] and anal== False):
                        permitted= False
                    if ("bondgae" in sceneTags[animString]and bondage== False):
                        permitted= False
                if (checkExists and permitted):
                    renpy.show_screen("h_scene_start", animString)
                    renpy.restart_interaction()
                else:
                    calcPreg()
        else:
            showBreed()
            renpy.show_screen("breed")
            renpy.restart_interaction()
    
    def sellMonster():
        bm1= breedMonster2
        bm2= breedMonster1
        global sellText
        if ((bm1.species.species== "any" or bm2.species.species== bm1.species.species) and (bm1.gender== "any" or bm2.gender== bm1.gender) and (bm1.variant== "any" or bm2.variant== bm1.variant)):
            if (bm2.ferocity>= bm1.ferocity and bm2.finesse>= bm1.finesse and bm2.determination>= bm1.determination and bm2.cunning>= bm1.cunning):
                for gene1 in bm1.genes:
                    sellMatch= False
                    for gene2 in bm2.genes:
                        if (gene2.name== gene1.name):
                            sellMatch= True
                            break
                    if (sellMatch== False):
                        break
                if (sellMatch):
                    global gameMoney
                    gameMoney+= (bm2.valueM+ bm1.valueM)
                    requestedMonsters.remove(bm1)
                    playerMonsters.remove(bm2)
                    sellText= bm2.name+ " sold for "+ str(bm2.valueM+ bm1.valueM)
                    showRequest()
     
    def increaseFertility(monster1, monster2):
        if (monster1.gender!= "male" and monster2.gender!= "female"):
            if (monster1.fertilityBase> 20):
                monster1.fertility+= monster1.fertilityBase/ 10 
            else:
                monster1.fertility+= 2
            if (monster1.fertilityBase> 20 and monster1.fertility> monster1.fertilityBase* 1.5):
                monster1.fertility= monster1.fertilityBase* 1.5
            if (monster1.fertility> 100):
                monster1.fertility= 100
        
    def calcPreg():
        "calculate which monster gets pregnant, if any"
        pregnantCheck= False
        pm1= False
        #pregnancy chance
        increaseFertility(breedMonster1, breedMonster2)
        increaseFertility(breedMonster2, breedMonster1)
        if (random.randint(0,100)<= pregChanceGlobal):
                #which monster got pregnant
                if (random.randint(0,100)< 50):
                    if (impregnate(breedMonster1, breedMonster2)== True):
                        pm1= True
                        pregnantCheck= True
                    else:
                        if (impregnate(breedMonster2, breedMonster1)== True):
                            pm1= False
                            pregnantCheck= True
                else:
                    if (impregnate(breedMonster2, breedMonster1)== True):
                        pm1= False
                        pregnantCheck= True
                    else:
                        if (impregnate(breedMonster1, breedMonster2)== True):
                            pregnantCheck= True
                            pm1= True
                if (pm1):
                    pregName= breedMonster1.name+ " got pregnant!"
                else:
                    pregName= breedMonster2.name+ " got pregnant!"
        if (pregnantCheck):
            showBreed()
            renpy.show_screen("breed")
            renpy.show_screen("pregnantWin", pregName)
            renpy.restart_interaction
        else:
            showBreed()
            renpy.show_screen("breed")
            renpy.restart_interaction()
            
    def renameMonster(newName):
        global rename
        rename.name= newName
        
    def discardMonsterBirth():
        global rename
        for monster in rename.relatives:
                monster.relatives.remove(rename)
        youngMonsters.remove(rename)
        
    def addMonsterWild():
        global breedMonster1
        playerMonsters.append(breedMonster1)
        breedMonster1= None
        
    def discardMonsterBarn():
        global breedMonster1
        if (breedMonster1.species.species!= "player"):
            if (viewYoung):
                youngMonsters.remove(breedMonster1)
            else:
                playerMonsters.remove(breedMonster1)
            for monster in breedMonster1.relatives:
                monster.relatives.remove(breedMonster1)
            breedMonster1= None
            showViewer()
            renpy.redraw(viewerV, 0)
            renpy.restart_interaction()

#training
    def calcTraining(monster1, monster2):
        if (monster1.training> 0):
            monster1.ferocity+= monster2.species.ferMod* monster1.statPoints
            if (monster1.ferocity> 200):
                monster1.ferocity= 200
            monster1.finesse+= monster2.species.finMod* monster1.statPoints
            if (monster1.finesse> 200):
                monster1.finesse= 200
            monster1.determination+= monster2.species.detMod* monster1.statPoints
            if (monster1.determination> 200):
                monster1.determination= 200
            monster1.cunning+= monster2.species.cunMod* monster1.statPoints
            if (monster1.cunning> 200):
                monster1.cunning= 200
            if (monster1.species.species!= "player"):
                monster1.training-= 1
        
    def trainFerocity():
        global breedMonster1
        stam= random.randint(2, 5)
        if (stam> breedMonster1.stamina):
            stam= breedMonster1.stamina
        breedMonster1.ferocity+= stam
        breedMonster1.stamina-= stam
        if (breedMonster1.ferocity> 250):
            breedMonster1.ferocity= 250
        breedMonster1.calcFertility()
        breedMonster1.calcEndurance()
        breedMonster1.applyGenes()
        breedMonster1.training+= 1
            
    def trainFinesse():
        global breedMonster1
        stam= random.randint(2, 5)
        if (stam> breedMonster1.stamina):
            stam= breedMonster1.stamina
        breedMonster1.finesse+= stam
        breedMonster1.stamina-= stam
        if (breedMonster1.finesse> 250):
            breedMonster1.finesse= 250
        breedMonster1.training+= 1
            
    def trainDetermination():
        global breedMonster1
        stam= random.randint(2, 5)
        if (stam> breedMonster1.stamina):
            stam= breedMonster1.stamina
        breedMonster1.determination+= stam
        breedMonster1.stamina-= stam
        if (breedMonster1.determination> 250):
            breedMonster1.determination= 250
        breedMonster1.calcEndurance()
        breedMonster1.applyGenes()
        breedMonster1.training+= 1
            
    def trainCunning():
        global breedMonster1
        stam= random.randint(2, 5)
        if (stam> breedMonster1.stamina):
            stam= breedMonster1.stamina
        breedMonster1.cunning+= stam
        breedMonster1.stamina-= stam
        if (breedMonster1.cunning> 250):
            breedMonster1.cunning= 250
        breedMonster1.calcFertility()
        breedMonster1.applyGenes()
        breedMonster1.training+= 1
        
    #fetish toggles
    def toggleGay():
        global gay
        if gay:
            gay= False
        else:
            gay= True
        renpy.restart_interaction()

    def toggleStraight():
        global straight
        if straight:
            straight= False
        else:
            straight= True
        renpy.restart_interaction()
        
    def toggleLesbian():
        global lesbian
        if lesbian:
            lesbian= False
        else:
            lesbian= True
        renpy.restart_interaction()
        
    def toggleHerms():
        global herms
        if herms:
            herms= False
        else:
            herms= True
        renpy.restart_interaction()
    
    def toggleAnal():
        global anal
        if anal:
            anal= False
        else:
            anal= True
        renpy.restart_interaction()

    def toggleVaginal():
        global vaginal
        if vaginal:
            vaginal= False
        else:
            vaginal= True
        renpy.restart_interaction()
        
    def toggleOral():
        global oral
        if oral:
            oral= False
        else:
            oral= True
        renpy.restart_interaction()
        
    def toggleBondage():
        global bondage
        if bondage:
            bondage= False
        else:
            bondage= True
        renpy.restart_interaction()    
        
    def toggleZoophilia():
        global zoophilia
        if zoophilia:
            zoophilia= False
        else:
            zoophilia= True
        renpy.restart_interaction()      