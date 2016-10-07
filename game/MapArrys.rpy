init 2 python:
    # any xpos is always across(left to right), any ypos down
    
    # Tile classes instantiated here
    blank = tile("images/Tiles/blankTile.png", Void=True)
    grass = tile("images/Tiles/grassTile.png")
    grassEdgeN = tile("images/Tiles/grassTile.png", PassN=False, VisibleN=False)
    grassEdgeE = tile("images/Tiles/grassTile.png", PassE=False, VisibleE=False)
    grassEdgeS = tile("images/Tiles/grassTile.png", PassS=False, VisibleS=False)
    grassEdgeW = tile("images/Tiles/grassTile.png", PassW=False, VisibleW=False)    
    grassEdgeNE = tile("images/Tiles/grassTile.png", PassN=False, VisibleN=False, PassE=False, VisibleE=False)
    grassEdgeES = tile("images/Tiles/grassTile.png", PassE=False, VisibleE=False, PassS=False, VisibleS=False)
    grassEdgeSW = tile("images/Tiles/grassTile.png", PassS=False, VisibleS=False, PassW=False, VisibleW=False)
    grassEdgeWN = tile("images/Tiles/grassTile.png", PassW=False, VisibleW=False, PassN=False, VisibleN=False)  
    

            
    
    
    
    class BattleMapClass(renpy.Displayable):
        def __init__(self, BattleMap):
            super(BattleMapClass, self).__init__()
            self.BattleMap = BattleMap
            self.Size = 50
            self.TotalWidth = self.Size*len(BattleMap[0])
            self.TotalHeight = self.Size*len(BattleMap)
            
        def render(self, width, height, st, at):
            constructor = Grid(cols=len(self.BattleMap), rows=len(self.BattleMap[0]))
            for x in range(0, len(self.BattleMap)):
                for y in range(0, len(self.BattleMap[x])):
                    constructor.add(self.BattleMap[x][y].Name)
            r = renpy.Render(self.TotalWidth, self.TotalHeight)
            r.place(constructor)
            return r
            
    class MoveOverlayClass(renpy.Displayable):
        def __init__(self, Overlay):
            super(MoveOverlayClass, self).__init__()
            self.Overlay = Overlay
            self.Size = 50
            self.TotalWidth = self.Size*len(Overlay[0])
            self.TotalHeight = self.Size*len(Overlay)
            
        def render(self, width, height, st, at):
            constructor = Grid(cols=len(self.Overlay), rows=len(self.Overlay[0]))
            for x in range(0, len(self.Overlay)):
                for y in range(0, len(self.Overlay[x])):
                    if self.UnitPresent == "Null":
                        constructor.add("images/Tiles/Null.png")
                    elif self.UnitPresent == "Move":
                        constructor.add("images/Tiles/Blue60.png")
                    else:
                        constructor.add(self.Overlay.UnitIdle)
            r = renpy.Render(self.TotalWidth, self.TotalHeight)
            r.place(constructor)
            return r
            
            
        

    # controlls if the map edgescroll works
    EdgeScroll = True
     
    
    ###Laird turned this into a function
    def grassField():
         return [[blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank],
        [blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank],
        [blank, blank, grassEdgeWN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeN, grassEdgeNE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeW, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grass, grassEdgeE, blank, blank],
        [blank, blank, grassEdgeSW, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeS, grassEdgeES, blank, blank],
        [blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank],
        [blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank, blank]]
    
     # (alpha wave", unit present")
     ###Laird and also this
    def grassFieldOverlay():
        return list([battletile(0, UnitPresent="Null") for x in range(0, len(grassField()[y]))] for y in range(0, len(grassField())))
    GrassFieldPlayerDeploy = [[4, 4],[5, 4],[6, 4],[7, 4],
        [4, 5],[5, 5],[6, 5],[7, 5],
        [4, 6],[5, 6],[6, 6],[7, 6],
        [4, 7],[5, 7],[6, 7],[7, 7]]
    GrassFieldEnemy1Deploy = [[16, 16], [17, 16], [18, 16],
        [16, 17], [18, 17],
        [16, 18], [17, 18], [18, 18]]
    SetFirst = 0
    SetSecond = 0
    
    
    # define battlefields here
    TutorialBattle = battlefield(grassField(), grassFieldOverlay(), 0, GrassFieldPlayerDeploy, PlayerArmy, GrassFieldEnemy1Deploy, Enemy1Army)
    
    
    # used in conjunction with the self.Visibility of the battletile class
    ImageAlpha = [hidden, visible]
    
    
    # used to controll zoom and viewport position on the battlefield
    MapCenterx = ui.adjustment()
    MapCentery = ui.adjustment()                
    MCX = MapCenterx
    MCY = MapCentery
    MapZoom = 5
    AddZoom = 0
    MinusZoom = 0
    ZoomList = [[x0p2, 0.2], [x0p4, 0.4], [x0p6, 0.6], [x0p8, 0.8], [x1, 1], [x1p2, 1.2], [x1p4, 1.4], [x1p6, 1.6], [x1p8, 1.8], [x2, 2]]
    AtoB = False
    CurrentFacing = "N"
    CurrentMove = "None"

    
    
    
    
screen CurrentMap:
    add "TopBanner" xpos 0 ypos 0
    viewport:
        area 0, 50, 1300, 750
        draggable True
        if EdgeScroll == True:
            edgescroll (150, 600)
        xadjustment MCX
        yadjustment MCY
        child_size 50*ZoomList[MapZoom][1]*len(CurrentMap[1]), 50*ZoomList[MapZoom][1]*len(CurrentMap)
        
        add BattleMapClass(CurrentMap) at ZoomList[MapZoom][0]
                        

        if DeploymentStart == False:
            # active battle overlay
            if PickingDestination == False:
                if RangeCalculation == False:
                    if AtoB == True:
                        # shows if unit is moving
                        grid len(CurrentOverlay) len(CurrentOverlay[0]):
                            for x in range(0, len(CurrentOverlay)): 
                                for y in range(0, len(CurrentOverlay[x])):
                                    if CurrentOverlay[x][y].UnitPresent == "Null":
                                        add "Null" at ImageAlpha[CurrentOverlay[x][y].Visibility]
                                    else:
                                        add CurrentOverlay[x][y].UnitIdle
                            at ZoomList[MapZoom][0]
                    else:
                        # Idle overlay
                        grid len(CurrentOverlay) len(CurrentOverlay[0]):
                            for x in range(0, len(CurrentOverlay)): 
                                for y in range(0, len(CurrentOverlay[x])):
                                    if CurrentOverlay[x][y].UnitPresent == "Null":
                                        add "Null" at ImageAlpha[CurrentOverlay[x][y].Visibility]
                                    else:
                                        if CurrentOverlay[x][y].UnitID.ArmyID == 1:
                                            imagebutton idle CurrentOverlay[x][y].UnitIdle hover CurrentOverlay[x][y].UnitHover hovered Show("PlayerMonsterCard", Unit=CurrentOverlay[x][y].UnitID) unhovered Hide("PlayerMonsterCard") action SetVariable("StartX", x), SetVariable("StartY", y), AddToSet(MoveSelect, CurrentOverlay[x][y].UnitID), Show("PlayerMonsterCard", Unit=CurrentOverlay[x][y].UnitID), Jump("PathGenerator")
                                        else:
                                            if ResolvingDamage == False:
                                                imagebutton idle CurrentOverlay[x][y].UnitIdle hover CurrentOverlay[x][y].UnitIdle hovered Show("EnemyMonsterCard", Unit=CurrentOverlay[x][y].UnitID) unhovered Hide("EnemyMonsterCard") action NullAction()
                                            else:
                                                imagebutton idle CurrentOverlay[x][y].UnitIdle hover CurrentOverlay[x][y].UnitIdle action NullAction()

                            at ZoomList[MapZoom][0]
                                
                                        
                else:
                    # movement range overlay
                    grid len(CurrentOverlay) len(CurrentOverlay[0]):
                        for x in range(0, len(CurrentOverlay)): 
                            for y in range(0, len(CurrentOverlay[x])):
                                if CurrentOverlay[x][y].UnitPresent == "Null":
                                    add "Null" at ImageAlpha[CurrentOverlay[x][y].Visibility]
                                elif CurrentOverlay[x][y].UnitPresent == "Move":
                                    imagebutton idle "MoveIdle" hover "MoveHover" action SetVariable("FinalDestinationX", x), SetVariable("FinalDestinationY", y), SetVariable("FinalDestination", [CurrentOverlay[x][y]]), Jump("MostEfficientRoute")
                                else:
                                    imagebutton idle CurrentOverlay[x][y].UnitIdle hover CurrentOverlay[x][y].UnitIdle hovered Show("EnemyMonsterCard", Unit=CurrentOverlay[x][y].UnitID) unhovered Hide("EnemyMonsterCard") action NullAction()
                        at ZoomList[MapZoom][0]
            else:
                # movement range overlay
                grid len(CurrentOverlay) len(CurrentOverlay[0]):
                    for x in range(0, len(CurrentOverlay)): 
                        for y in range(0, len(CurrentOverlay[x])):
                            if CurrentOverlay[x][y].UnitPresent == "Null":
                                add "Null" at ImageAlpha[CurrentOverlay[x][y].Visibility]
                            elif CurrentOverlay[x][y].UnitPresent == "Move":
                                imagebutton idle "MoveIdle" hover "MoveHover" action SetVariable("FinalDestinationX", x), SetVariable("FinalDestinationY", y), SetVariable("FinalDestination", [CurrentOverlay[x][y]]), Jump("MostEfficientRoute")
                            else:
                                imagebutton idle CurrentOverlay[x][y].UnitIdle hover CurrentOverlay[x][y].UnitIdle hovered Show("EnemyMonsterCard", Unit=CurrentOverlay[x][y].UnitID) unhovered Hide("EnemyMonsterCard") action NullAction()
                    at ZoomList[MapZoom][0]
                                
                                    
        # target range overlay
        if DeploymentStart == False:
            if RangeCalculation == True:
                grid len(CurrentOverlay) len(CurrentOverlay[0]):
                    for x in range(0, len(CurrentOverlay)): 
                        for y in range(0, len(CurrentOverlay[x])):
                            if CurrentOverlay[x][y].RangeOverlay == "Range":
                                add "RangeTile"
                            elif CurrentOverlay[x][y].RangeOverlay == "Target":
                                imagebutton idle "TargetIdle" hover "TargetHover" hovered Show("EnemyMonsterCard", Unit=CurrentOverlay[x][y].UnitID) unhovered Hide("EnemyMonsterCard") action SetVariable("TargetX", x), SetVariable("TargetY", y), SetVariable("TargetID", [CurrentOverlay[x][y].UnitID]), Show("EnemyMonsterCard", Unit=CurrentOverlay[x][y].UnitID), Jump("ResolveDamage")
                            else:
                                add "Null" at hidden
                    at ZoomList[MapZoom][0]
        
            
        else:
            # deployment overlay
            grid len(CurrentOverlay) len(CurrentOverlay[0]):
                for x in range(0, len(CurrentOverlay)): 
                    for y in range(0, len(CurrentOverlay[x])):
                        if CurrentOverlay[x][y].UnitPresent == "Null":
                            add "Null" at ImageAlpha[CurrentOverlay[x][y].Visibility]
                        elif CurrentOverlay[x][y].UnitPresent == "Deploy":
                            add "Null" at ImageAlpha[CurrentOverlay[x][y].Visibility]
                        else:
                            # used to remove an already deployed unit and put them back into the deployment list, re-setting the battletile perameters
                            imagebutton idle CurrentOverlay[x][y].UnitIdle hover CurrentOverlay[x][y].UnitHover action AddToSet(PlayerPartyDep, CurrentOverlay[x][y].UnitID), SetField(CurrentOverlay[x][y], "UnitID", "None"), SetField(CurrentOverlay[x][y], "UnitPresent", "Deploy"), SetField(CurrentOverlay[x][y], "Visibility", 0), SetField(CurrentOverlay[x][y], "UnitIdle", "None"), SetField(CurrentOverlay[x][y], "UnitHover", "None"), Jump("RenderMap")
                at ZoomList[MapZoom][0]    
                        
                        
        if PickingDestination == True:
            if AtoB == False:
                imagebutton idle "CancelMoveIdle" hover "CancelMoveHover" xpos CurrentOverlay[StartX][StartY].XPos ypos CurrentOverlay[StartX][StartY].YPos at ZoomList[MapZoom][0] action SetVariable("MoveCancel", True), Jump("ResetMoveVariables")
        if RangeCalculation == True:
            imagebutton idle "CancelMoveIdle" hover "CancelMoveHover" xpos CurrentOverlay[StartX][StartY].XPos ypos CurrentOverlay[StartX][StartY].YPos at ZoomList[MapZoom][0] action SetVariable("MoveCancel", True), Jump("ResetMoveVariables")
                
        # moving sprite
        if AtoB == True:
            add MoveSelect[0].BattleSpriteMove at CurrentMove, ZoomList[MapZoom][0]
            
        if PlaceUnit == True:
            # Activates when unit is selected for deployment
            grid len(CurrentOverlay) len(CurrentOverlay[0]):
                for x in range(0, len(CurrentOverlay)): 
                    for y in range(0, len(CurrentOverlay[x])): 
                        if CurrentOverlay[x][y].UnitPresent == "Deploy":
                            imagebutton idle "DeploymentIdle" hover "DeploymentHover" action SetField(CurrentOverlay[x][y], "UnitID", ActiveDeployment[0]), SetField(CurrentOverlay[x][y], "UnitPresent", ActiveDeployment[0].BattleName), SetField(CurrentOverlay[x][y], "UnitIdle", ActiveDeployment[0].BattleSpriteIdle), SetField(CurrentOverlay[x][y], "UnitHover", ActiveDeployment[0].BattleSpriteHover), SetField(CurrentOverlay[x][y], "Visibility", 1), Jump("UnitPlacement")
                        else:
                            add "Clear"
                at ZoomList[MapZoom][0]

    
    # GUI at the bottom of the map
    add "BattleCardUnder" xpos 0 ypos 800
    add "BattleMonsterCard" xpos 0 ypos 800
    if DeploymentStart == True:
            hbox:
                xpos 20 ypos 820
                for x in range(0, len(PlayerPartyDep)):
                    imagebutton:
                        idle PlayerPartyDep[x].BattleSpriteIdle
                        hover PlayerPartyDep[x].BattleSpriteHover
                        action SetVariable("ActiveDeployment", [PlayerPartyDep[x].Self]), SetVariable("PlaceUnit", True), Jump("RenderMap")
   
    add "BattleMonsterCardSmall" xpos 450 ypos 800
        
    add "BattleMonsterCard" xpos 850 ypos 800
    if DeploymentStart == True:
            hbox:
                xpos 870 ypos 820
                for x in range(0, len(Enemy1Army)):
                    add Enemy1Army[x].BattleSpriteIdle
    
    hbox:
        xpos 0
        ypos 735
        for x in range(0, 6):
            add "BlankBlock"
    if PickingDestination == True:
    
        hbox:
            xpos 0
            ypos 735
            for x in range(0, len(SelectedBattleSkills)):
                if MoveSelect[0].Action == True:
                    imagebutton idle SelectedBattleSkills[x].WeaponIdle hover SelectedBattleSkills[x].WeaponHover right_padding 23 hovered SetVariable("EdgeScroll", False) unhovered SetVariable("EdgeScroll", True) action SetVariable("SelectedAttack", [SelectedBattleSkills[x]]), Jump("AttackRange")
                

    
    if DeploymentStart == True:
        if len(PlayerPartyDep) == 0:
            imagebutton idle "FinishDeploymentIdle" hover "FinishDeploymentHover" xpos 0.44 ypos 0.84 action Jump("FinishDeployment")
        else:
            add "FinishDeploymentAlpha" xpos 0.44 ypos 0.84
    if DeploymentStart == False:
        if AtoB == False:
            imagebutton idle "NextTurnIdle" hover "NextTurnHover" xpos 650 ypos 0 action Jump("NextTurn")
            




screen PlayerMonsterCard(Unit):
    add "images/GUI/stat_morale.png" xpos 187 ypos 820
    add "images/GUI/stat_aggression.png" xpos 190 ypos 865
    add "images/GUI/stat_charm.png" xpos 190 ypos 905
    add "images/GUI/stat_block.png" xpos 190 ypos 930
    add "images/GUI/charmRes.png" xpos 188 ypos 960
    
    bar:
        value StaticValue(Unit.CurrentMorale, Unit.MaxMorale)
        right_bar im.Scale("images/GUI/hp_empty.png", 150, 20)
        left_bar im.Scale("images/GUI/hp_full.png", 150, 20)
        thumb None 
        thumb_shadow None
        xysize 150, 20
        xpos 235
        ypos 825
        left_gutter 0
        right_gutter 0
    text "{}".format(Unit.CurrentMorale) xpos 390 ypos 824
        
    text "{}".format(Unit.Agression) xpos 235 ypos 865
    text "{}".format(Unit.Seduction) xpos 235 ypos 905
    text "{}".format(Unit.PhysicalResist) xpos 235 ypos 930
    text "{}".format(Unit.CharmResist) xpos 235 ypos 960
    
    text "{}".format(Unit.OrigionalName) xpos 40 ypos 820
    add Unit.Mugshot xpos 30 ypos 845
    
screen EnemyMonsterCard(Unit):
    add "images/GUI/stat_morale.png" xpos 1037 ypos 820
    add "images/GUI/stat_aggression.png" xpos 1040 ypos 865
    add "images/GUI/stat_charm.png" xpos 1040 ypos 905
    add "images/GUI/stat_block.png" xpos 1040 ypos 930
    add "images/GUI/charmRes.png" xpos 1038 ypos 960
    
    bar:
        value StaticValue(Unit.CurrentMorale, Unit.MaxMorale)
        right_bar im.Scale("images/GUI/hp_empty.png", 150, 20)
        left_bar im.Scale("images/GUI/hp_full.png", 150, 20)
        thumb None 
        thumb_shadow None
        xysize 150, 20
        xpos 1085
        ypos 825
        left_gutter 0
        right_gutter 0
    text "{}".format(Unit.CurrentMorale) xpos 1240 ypos 824
        
    text "{}".format(Unit.Agression) xpos 1085 ypos 865
    text "{}".format(Unit.Seduction) xpos 1085 ypos 905
    text "{}".format(Unit.PhysicalResist) xpos 1085 ypos 930
    text "{}".format(Unit.CharmResist) xpos 1085 ypos 960
    
    text "{}".format(Unit.OrigionalName) xpos 890 ypos 820
    add Unit.Mugshot xpos 880 ypos 845





screen ZoomScreen:
    if AtoB == False:
        if MapZoom == 9:
            add "ZoomInAplha" xpos 580 ypos 5
        else:
            imagebutton idle "ZoomInIdle" hover "ZoomInHover" xpos 605 ypos 5 action SetVariable("AddZoom", 1), Jump("RenderMap") focus_mask True
        if MapZoom == 0:
            add "ZoomOutAplha" xpos 730 ypos 5
        else:
            imagebutton idle "ZoomOutIdle" hover "ZoomOutHover" xpos 730 ypos 5 action SetVariable("MinusZoom", 1), Jump("RenderMap") focus_mask True
        
        
        
label UnitPlacement:
    $ PlayerPartyDep.remove(ActiveDeployment[0])
    $ CompletedDeployment.append(ActiveDeployment[0])
    $ ActiveDeployment = []
    $ UnitPlaced = True
    jump RenderMap
    
label FinishDeployment: 
    # The following can be pretty much copy pasted for enemy2 and 3 with just a change of the digit 1 to 2 or 3
    # reset deployment overlay
    python:
        ActiveDeployment = []
        for x in range(0, len(CurrentOverlay)):
            for y in range(0, len(CurrentOverlay[x])):
                if CurrentOverlay[x][y].UnitPresent == "Deploy":
                    CurrentOverlay[x][y].UnitPresent = "Null"
        # set deployment overlay for enemy 1
        for i in range(0, len(CurrentEnemy1Deployment)):
                TempIndecesY = CurrentEnemy1Deployment[i][0]
                TempIndecesX = CurrentEnemy1Deployment[i][1]
                CurrentOverlay[TempIndecesY][TempIndecesX].UnitPresent = "Deploy"
        
        # physically deploy enemy1 units (More sophisticated versions will be made, but for now random deployment is fine)
        for i in range(0, len(Enemy1ArmyDep)):
            ActiveDeployment.append(Enemy1ArmyDep[i])
            DeploymentRandomiser = renpy.random.randint(0, len(Enemy1ArmyDep))
            while CurrentOverlay[CurrentEnemy1Deployment[DeploymentRandomiser][0]][CurrentEnemy1Deployment[DeploymentRandomiser][1]].UnitPresent != "Deploy":
                DeploymentRandomiser = renpy.random.randint(0, len(Enemy1ArmyDep))
            CurrentOverlay[CurrentEnemy1Deployment[DeploymentRandomiser][0]][CurrentEnemy1Deployment[DeploymentRandomiser][1]].UnitID = ActiveDeployment[0]
            CurrentOverlay[CurrentEnemy1Deployment[DeploymentRandomiser][0]][CurrentEnemy1Deployment[DeploymentRandomiser][1]].UnitPresent = ActiveDeployment[0].BattleName
            CurrentOverlay[CurrentEnemy1Deployment[DeploymentRandomiser][0]][CurrentEnemy1Deployment[DeploymentRandomiser][1]].UnitIdle = ActiveDeployment[0].BattleSpriteIdle
            CurrentOverlay[CurrentEnemy1Deployment[DeploymentRandomiser][0]][CurrentEnemy1Deployment[DeploymentRandomiser][1]].UnitHover = ActiveDeployment[0].BattleSpriteHover
            CurrentOverlay[CurrentEnemy1Deployment[DeploymentRandomiser][0]][CurrentEnemy1Deployment[DeploymentRandomiser][1]].Visibility = 1
            ActiveDeployment = []
            
        for x in range(0, len(CurrentOverlay)):
            for y in range(0, len(CurrentOverlay[x])):
                if CurrentOverlay[x][y].UnitPresent == "Deploy":
                    CurrentOverlay[x][y].UnitPresent = "Null"
        DeploymentStart = False
    jump RenderMap