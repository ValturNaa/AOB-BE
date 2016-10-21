init python:
    
    def CheckWin():
        checkdeathtotal = len(PlayerArmy)
        checkdeath = 0
        WinLose = "No"
        PlayerArmyDead = False
        AllEnemyDead = False
        for x in PlayerArmy.Army:
            if (x.Routed == True):
                checkdeath += 1
        if (checkdeath == checkdeathtotal):
            PlayerArmyDead = True
            
        checkdeathtotal = 0
        for n in ActiveAIArmies:
            checkdeathtotal += len(n.Army)
        checkdeath = 0
        
        for y in ActiveAIArmies:
            for z in y.Army:
                if (y.z.Routed == True):
                    checkdeath += 1
        if (checkdeath == checkdeathtotal):
            AllEnemyDead = True
            
        if (PlayerArmyDead and AllEnemyDead == True):
            WinLose = "Draw"
        elif (PlayerArmyDead == True):
            WinLose = "Lose"
        elif (AllEnemyDead == True):
            WinLose = "Win"
            
        return WinLose
    
    def ReturnPositive(Start, Target):
        temp1 = Start - Target
        temp2 = temp1*temp1
        temp3 = temp2**0.5
        return temp3
        
    def GetX(Unit, Map):
        for x in range(0, len(Map)):
            for y in range(0, len(Map[x])):
                if (Map[x][y].UnitPresent == Unit.BattleName):
                    StartX = x
        return StartX
        
    def GetY(Unit, Map):
        for x in range(0, len(Map)):
            for y in range(0, len(Map[x])):
                if (Map[x][y].UnitPresent == Unit.BattleName):
                    StartY = y
        return StartY
        
        
    class AIEnemyInfo(object):
        def __init__(self, XDistance, YDistance, x, y):
            self.XDistance = XDistance
            self.YDistance = YDistance
            self.TotalDistance = XDistance + YDistance
            self.Xpos = x
            self.Ypos = y
            
    def IDNearestTarget(Unit, Map):
        StartX = 0
        StartY = 0
        PotentialTarget = 0
        TargetList = []
        ClosestTargetDistance = 100000
        ClosestTarget = 0
        for x in range(0, len(Map)):
            for y in range(0, len(Map[x])):
                if (Map[x][y].UnitPresent == Unit.BattleName):
                    StartX = x
                    StartY = y
                else:
                    pass
        for x in range(0, len(Map)):
            for y in range(0, len(Map[x])):
                if (Map[x][y].UnitPresent == "Null"):
                    pass
                else:
                    if (Map[x][y].UnitID.ArmyID == Unit.ArmyID):
                        pass
                    else:
                        TargetList.append(AIEnemyInfo(ReturnPositive(StartX, x), ReturnPositive(StartY, y), x, y))
                        PotentialTarget += 1
        for x in range(0, len(TargetList)):
            if (TargetList[x].TotalDistance < ClosestTargetDistance):
                ClosestTargetDistance = TargetList[x].TotalDistance
                ClosestTarget = x
        return TargetList[ClosestTarget]
        
        
    def AIDecideAction(Unit, Map):
        Action = "Move"
        StartX = 0
        StartY = 0
        PotentialTarget = 0
        TargetList = []
        ClosestTargetDistance = 100000
        ClosestTarget = 0
        for x in range(0, len(Map)):
            for y in range(0, len(Map[x])):
                if (Map[x][y].UnitPresent == Unit.BattleName):
                    StartX = x
                    StartY = y
                else:
                    pass
        for x in range(0, len(Map)):
            for y in range(0, len(Map[x])):
                if (Map[x][y].UnitPresent == "Null"):
                    pass
                else:
                    if (Map[x][y].UnitID.ArmyID == Unit.ArmyID):
                        pass
                    else:
                        TargetList.append(AIEnemyInfo(ReturnPositive(StartX, x), ReturnPositive(StartY, y), x, y))
                        PotentialTarget += 1
        for x in range(0, len(TargetList)):
            if (TargetList[x].TotalDistance < ClosestTargetDistance):
                ClosestTargetDistance = TargetList[x].TotalDistance
                ClosestTarget = TargetList[x]
        Action = "Move"
        for x in Unit.BattleSkills:
            tempaction = IsTarget(Unit, x, StartX, StartY, Indirect=x.IndirectFire)
            if (tempaction == True):
                Action = "Attack"
            else:
                PredictPathList = GeneratePaths(Unit, StartX, StartY)
                PredictFinalPath = []
                PredictFinalPath.append(AISetDestination(Unit, Map, StartX, StartY, PredictPathList, ClosestTarget))
                for y in range(0, len(PredictFinalPath[0].WayPoints)):
                    if (PredictFinalPath[0].WayPoints[y] == "N"):
                        StartX -= 1
                    if (PredictFinalPath[0].WayPoints[y] == "E"):
                        StartY += 1
                    if (PredictFinalPath[0].WayPoints[y] == "S"):
                        StartX += 1
                    if (PredictFinalPath[0].WayPoints[y] == "W"):
                        StartY -= 1
                tempaction = IsTarget(Unit, x, StartX, StartY, Indirect=x.IndirectFire)
                if (tempaction == True):
                    if (Action != "Attack"):
                        Action = "Move Attack"
        return Action
        
    def ReturnPlus(x):
        temp1 = x*x
        temp2 = temp1**0.5
        return temp2
        
    def PerfectFinish(AITarget, LeftRight, UpDown, Map, XY):
        PerfectFinishX = AITarget.Xpos
        PerfectFinishY = AITarget.Ypos
        if (LeftRight == "Right"):
            PerfectFinishY += 1
            if (UpDown == "Down"):
                if (Map.UnitPresent[PerfectFinishX][PerfectFinishY] != "Null"):
                    if (Map.UnitPresent[PerfectFinishX+1][PerfectFinishY] != "Null"):
                        if (Map.UnitPresent[PerfectFinishX-1][PerfectFinishY] != "Null"):
                            if (Map.UnitPresent[PerfectFinishX][PerfectFinishY-2] != "Null"):
                                pass
                            else:
                                PerfectFinishY -= 2
                        else:
                            PerfectFinishX -= 1
                    else:
                        PerfectFinishX += 1
            elif (UpDown == "Up"):
                if (Map.UnitPresent[PerfectFinishX][PerfectFinishY] != "Null"):
                    if (Map.UnitPresent[PerfectFinishX-1][PerfectFinishY] != "Null"):
                        if (Map.UnitPresent[PerfectFinishX+1][PerfectFinishY] != "Null"):
                            if (Map.UnitPresent[PerfectFinishX][PerfectFinishY-2] != "Null"):
                                pass
                            else:
                                PerfectFinishY -= 2
                        else:
                            PerfectFinishX += 1
                    else:
                        PerfectFinishX -= 1
            else:
                if (Map.UnitPresent[PerfectFinishX][PerfectFinishY] != "Null"):
                    if (Map.UnitPresent[PerfectFinishX+1][PerfectFinishY] != "Null"):
                        if (Map.UnitPresent[PerfectFinishX-1][PerfectFinishY] != "Null"):
                            if (Map.UnitPresent[PerfectFinishX][PerfectFinishY-2] != "Null"):
                                pass
                            else:
                                PerfectFinishY -= 2
                        else:
                            PerfectFinishX -= 1
                    else:
                        PerfectFinishX += 1
        if (LeftRight == "Left"): 
            PerfectFinishY -= 1
            if (UpDown == "Down"):
                if (Map.UnitPresent[PerfectFinishX][PerfectFinishY] != "Null"):
                    if (Map.UnitPresent[PerfectFinishX+1][PerfectFinishY] != "Null"):
                        if (Map.UnitPresent[PerfectFinishX-1][PerfectFinishY] != "Null"):
                            if (Map.UnitPresent[PerfectFinishX][PerfectFinishY+2] != "Null"):
                                pass
                            else:
                                PerfectFinishY += 2
                        else:
                            PerfectFinishX -= 1
                    else:
                        PerfectFinishX += 1
            elif (UpDown == "Up"):
                if (Map.UnitPresent[PerfectFinishX][PerfectFinishY] != "Null"):
                    if (Map.UnitPresent[PerfectFinishX-1][PerfectFinishY] != "Null"):
                        if (Map.UnitPresent[PerfectFinishX+1][PerfectFinishY] != "Null"):
                            if (Map.UnitPresent[PerfectFinishX][PerfectFinishY+2] != "Null"):
                                pass
                            else:
                                PerfectFinishY += 2
                        else:
                            PerfectFinishX += 1
                    else:
                        PerfectFinishX -= 1
            else:
                if (Map.UnitPresent[PerfectFinishX][PerfectFinishY] != "Null"):
                    if (Map.UnitPresent[PerfectFinishX+1][PerfectFinishY] != "Null"):
                        if (Map.UnitPresent[PerfectFinishX-1][PerfectFinishY] != "Null"):
                            if (Map.UnitPresent[PerfectFinishX][PerfectFinishY-2] != "Null"):
                                pass
                            else:
                                PerfectFinishY -= 2
                        else:
                            PerfectFinishX -= 1
                    else:
                        PerfectFinishX += 1
        else:
            if (UpDown == "Down"):
                PerfectFinishX -=1
                if (Map.UnitPresent[PerfectFinishX][PerfectFinishY] != "Null"):
                    if (Map.UnitPresent[PerfectFinishX][PerfectFinishY+1] != "Null"):
                        if (Map.UnitPresent[PerfectFinishX][PerfectFinishY-1] != "Null"):
                            if (Map.UnitPresent[PerfectFinishX+2][PerfectFinishY] != "Null"):
                                pass
                            else:
                                PerfectFinishX += 2
                        else:
                            PerfectFinishY -= 1
                    else:
                        PerfectFinishY += 1
            elif (UpDown == "Up"):
                PerfectFinishX +=1
                if (Map.UnitPresent[PerfectFinishX][PerfectFinishY] != "Null"):
                    if (Map.UnitPresent[PerfectFinishX][PerfectFinishY-1] != "Null"):
                        if (Map.UnitPresent[PerfectFinishX][PerfectFinishY+1] != "Null"):
                            if (Map.UnitPresent[PerfectFinishX-2][PerfectFinishY] != "Null"):
                                pass
                            else:
                                PerfectFinishX -= 2
                        else:
                            PerfectFinishY += 1
                    else:
                        PerfectFinishY -= 1
        if (XY == "X"):
            return PerfectFinishX
        else:
            return PerfectFinishY
            

        
        
    def AISetDestination(Unit, Map, StartX, StartY, PathList, AITarget):
        if (StartX > AITarget.Xpos):
            LeftRight = "Up"
        elif (StartX == AITarget.Xpos):
            LeftRight = "Spot on"
        else:
            LeftRight = "Down"
        if (StartY > AITarget.Ypos):
            UpDown = "Right"
        elif (StartY == AITarget.Ypos):
            UpDown = "Spot on"
        else:
            UpDown = "Left"
            
        PerfectFinishX = PerfectFinish(AITarget, LeftRight, UpDown, Map, "X")
        PerfectFinishY = PerfectFinish(AITarget, LeftRight, UpDown, Map, "Y")
            
            
        PathDifference = 1000
        StoreDifference = 1000
        BestPath = 0
        for path in range(0, len(PathList)):
            EndXShort = 0
            EndYShort = 0
            EndX = StartX
            EndY = StartY
            for waypoint in PathList[path].WayPoints:
                if (waypoint == "N"):
                    EndX -= 1
                if (waypoint == "E"):
                    EndY += 1
                if (waypoint == "S"):
                    EndX += 1
                if (waypoint == "W"):
                    EndY -= 1
            EndXShort = ReturnPlus(EndX-PerfectFinishX)
            EndYShort = ReturnPlus(EndY-PerfectFinishY)
            StoreDifference = EndXShort+EndYShort
            if (StoreDifference < PathDifference):
                PathDifference = StoreDifference
                BestPath = path
                
        return PathList[BestPath]
        
    def DetermineFinishX(StartX, StartY, Path):
        for waypoint in Path.WayPoints:
            if (waypoint == "N"):
                StartX -= 1
            if (waypoint == "S"):
                StartX += 1
        return StartX
            
    def DetermineFinishY(StartX, StartY, Path):
        for waypoint in Path.WayPoints:
            if (waypoint == "W"):
                StartY -= 1
            if (waypoint == "E"):
                StartY += 1
        return StartY
    
    def ExecuteMovement():
        renpy.hide_screen("CurrentMap")
        renpy.show_screen("CurrentMap")
        global StartX
        global StartY
        global MoveTick
        global CurrentMove
        global CurrentFacing
        
        renpy.restart_interaction()
        for waypoint in range(0, len(FinalPath[0].WayPoints)):
            if (FinalPath[0].WayPoints[waypoint] == "N"):
                CurrentFacing = "N"
                if (MoveTick == False):
                    MoveTick = True
                    CurrentMove = MovePathN1
                else:
                    MoveTick = False
                    CurrentMove = MovePathN2
                renpy.restart_interaction()
                renpy.pause(1)
                StartX -= 1
            elif (FinalPath[0].WayPoints[waypoint] == "E"):
                CurrentFacing = "E"
                if (MoveTick == False):
                    MoveTick = True
                    CurrentMove = MovePathE1
                else:
                    MoveTick = False
                    CurrentMove = MovePathE2
                renpy.restart_interaction()
                renpy.pause(1)
                StartY += 1
            elif (FinalPath[0].WayPoints[waypoint] == "S"):
                CurrentFacing = "S"
                if (MoveTick == False):
                    MoveTick = True
                    CurrentMove = MovePathS1
                else:
                    MoveTick = False
                    CurrentMove = MovePathS2
                renpy.restart_interaction()
                renpy.pause(1)
                StartX += 1
            elif (FinalPath[0].WayPoints[waypoint] == "W"):
                CurrentFacing = "W"
                if (MoveTick == False):
                    MoveTick = True
                    CurrentMove = MovePathW1
                else:
                    MoveTick = False
                    CurrentMove = MovePathW2
                renpy.restart_interaction()
                renpy.pause(1)
                StartY -= 1
        AtoB = False
        FinishMove()
        renpy.hide_screen("CurrentMap")
        renpy.show_screen("CurrentMap")

    def FinishMove():
        global CurrentOverlay
        CurrentOverlay[FinalDestinationX][FinalDestinationY].UnitPresent = MoveSelect[0].BattleName
        CurrentOverlay[FinalDestinationX][FinalDestinationY].UnitID = MoveSelect[0]
        CurrentOverlay[FinalDestinationX][FinalDestinationY].UnitIdle = MoveSelect[0].BattleSpriteIdle
        CurrentOverlay[FinalDestinationX][FinalDestinationY].UnitHover = MoveSelect[0].BattleSpriteHover
        CurrentOverlay[FinalDestinationX][FinalDestinationY].Visibility = 1
        ResetMoveVariables()
        
    def ResetMoveVariables():
        global PathList
        global StartX
        global StartY
        global MoveSelect
        global TempPath
        global TempStartX
        global TempStartY
        global PickingDestination
        global FinalDestination
        global FinalDestinationX
        global FinalDestinationY
        global FinalPathBuffer
        global FinalPath
        global AtoB
        global CurrentFacing
        global CurrentMove
        global OwnMonsterCard
        global MonsterCardStats
        global CurrentOverlay
        
        renpy.hide_screen("PlayerMonsterCard")
        renpy.hide_screen("EnemyMonsterCard")
        
        PathList = []
        StartX = 0
        StartY = 0
        MoveSelect = []
        TempPath = []
        TempStartX = 0
        TempStartY = 0
        PickingDestination = False
        FinalDestination = []
        FinalDestinationX = 0
        FinalDestinationY = 0
        FinalPathBuffer = []
        FinalPath = []
        AtoB = False
        CurrentFacing = "S"
        CurrentMove = "Starter"
        OwnMonsterCard = False
        MonsterCardStats = []
        for x in range(0, len(CurrentOverlay)):
            for y in range(0, len(CurrentOverlay[x])):
                CurrentOverlay[x][y].RouteStore = []
        ResetAttack()
        if (MoveCancel == True):
            for x in range(0, len(CurrentOverlay)):
                for y in range(0, len(CurrentOverlay[x])):
                    if (CurrentOverlay[x][y].UnitPresent == "Move"):
                        CurrentOverlay[x][y].UnitPresent = "Null"
                        
    def AIMoveAction():
        global AITarget
        global MoveSelect
        global StartX
        global StartY
        global PathList
        global FinalPath
        global FinalDestinationX
        global FinalDestinationY
        global FinalDestination
        global AtoB
        global CurrentOverlay
        global PickingDestination
        global CurrentFacing
        global MoveTick
        global CurrentMove
        AITarget = IDNearestTarget(ActiveAIArmies[army].Army[x], CurrentOverlay)
        MoveSelect.append(ActiveAIArmies[army].Army[x])
        StartX = GetX(ActiveAIArmies[army].Army[x], CurrentOverlay)
        StartY = GetY(ActiveAIArmies[army].Army[x], CurrentOverlay)
        PathList = GeneratePaths(MoveSelect[0], StartX, StartY)
        FinalPath = []
        FinalPath.append(AISetDestination(MoveSelect[0], CurrentMap, StartX, StartY, PathList, AITarget))
        FinalDestinationX = DetermineFinishX(StartX, StartY, FinalPath[0])
        FinalDestinationY = DetermineFinishY(StartX, StartY, FinalPath[0])
        FinalDestination.append(CurrentOverlay[FinalDestinationX][FinalDestinationY])
                        
        AtoB = True
        CurrentOverlay[StartX][StartY].UnitPresent = "Null"
        CurrentOverlay[StartX][StartY].UnitID = "None"
        CurrentOverlay[StartX][StartY].UnitIdle = "None"
        CurrentOverlay[StartX][StartY].UnitHover = "None"
        CurrentOverlay[StartX][StartY].Visibility = 0
        MoveSelect[0].MovementCurrent -= FinalPath[0].MoveRequired
        PickingDestination = False
        if (FinalPath[0].WayPoints[0] == "N"):
            CurrentFacing = "N"
            if (MoveTick == False):
                MoveTick = True
                CurrentMove = MovePathN1
            else:
                MoveTick = False
                CurrentMove = MovePathN2
        elif (FinalPath[0].WayPoints[0] == "E"):
            CurrentFacing = "E"
            if (MoveTick == False):
                MoveTick = True
                CurrentMove = MovePathE1
            else:
                MoveTick = False
                CurrentMove = MovePathE2
        elif (FinalPath[0].WayPoints[0] == "S"):
            CurrentFacing = "S"
            if (MoveTick == False):
                MoveTick = True
                CurrentMove = MovePathS1
            else:
                MoveTick = False
                CurrentMove = MovePathS2
        elif (FinalPath[0].WayPoints[0] == "W"):
            CurrentFacing = "W"
            if (MoveTick == False):
                MoveTick = True
                CurrentMove = MovePathW1
            else:
                MoveTick = False
                CurrentMove = MovePathW2
        ExecuteMovement()
        
        
    ################################## Attack functions ####################################
        
        
    def AIAttackAction(Unit):
        global StartX
        global StartY
        global CurrentOverlay
        global SelectedAttack
        global CombatDamage
        global TargetID
        global ResolvingDamage
        for x in range(0, len(CurrentOverlay)):
            for y in range(0, len(CurrentOverlay[x])):
                if (CurrentOverlay[x][y].UnitPresent == Unit.BattleName):
                    StartX = x
                    StartY = y
        AISelectAttack(Unit, StartX, StartY)
        Target = AIAttackTarget(Unit, SelectedAttack[0], StartX, StartY)
        TargetID = [CurrentOverlay[Target.Xpos][Target.Ypos].UnitID]
        for x in range(0, len(CurrentOverlay)):
            for y in range(0, len(CurrentOverlay[x])):
                if (CurrentOverlay[x][y].UnitPresent == TargetID[0].BattleName):
                    TargetX = x
                    TargetY = y 
        CombatDamage = GetDamage(Unit, SelectedAttack[0], TargetID[0])
        Unit.Action = False
        Unit.MovementCurrent = 0
        ResolvingDamage = True
        renpy.restart_interaction()
        
        renpy.show_screen("PlayerMonsterCard", TargetID[0])
        renpy.show_screen("EnemyMonsterCard", Unit)
        renpy.show_screen("DamageScreen", Damage=CombatDamage.FinalDamage, ArmyID=TargetID[0].ArmyID)
        while CombatDamage.FinalDamage > 0:
            TargetID[0].CurrentMorale -= 1
            CombatDamage.FinalDamage -= 1
            renpy.pause(0.05)
        if TargetID[0].CurrentMorale <= 0:
            renpy.hide("EnemyMonsterCard")
            TargetID[0].Routed = True
            CurrentOverlay[TargetX][TargetY].UnitPresent="Null"
            CurrentOverlay[TargetX][TargetY].UnitIdle="None"
            CurrentOverlay[TargetX][TargetY].UnitHover="None"
            CurrentOverlay[TargetX][TargetY].UnitID="None"
            CurrentOverlay[TargetX][TargetY].Visibility = 0
        renpy.hide_screen("DamageScreen")
        renpy.pause(1.5)
        renpy.hide_screen("PlayerMonsterCard")
        renpy.hide_screen("EnemyMonsterCard")
        ResetMoveVariables()
        renpy.restart_interaction()
        
        
        
        
    
    def AISelectAttack(Unit, StartX, StartY):
        global SelectedAttack
        SameList = ReturnSameList(Unit.BattleSkills)
        for x in range(0, len(Unit.BattleSkills)):
            Temp = IsTarget(Unit, Unit.BattleSkills[x], StartX, StartY)
            if (Temp == "False"):
                SameList[x] = "Nope"
        RandomAttack = renpy.random.randint(0, len(SameList)-1)
        while SameList[RandomAttack] == "Nope":
            RandomAttack = renpy.random.randint(0, len(SameList)-1)
        SelectedAttack = [Unit.BattleSkills[RandomAttack]]
        
            
    def IsTarget(Unit, Attack, StartX, StartY, Indirect=False, ReturnList=False):
        global CurrentOverlay
        is_target = False
        TargetList = []
        if (Indirect == True):
            MaxRangeX = StartX + Attack.Range
            MinRangeX = StartX - Attack.Range
            MaxRangeY = StartY + Attack.Range
            MinRangeY = StartY - Attack.Range
            for x in range(MinRangeX, MaxRangeX):
                for y in range(MinRangeY, MaxRangeY):
                    if (CurrentOverlay[x][y].UnitPresent != "Null"):
                        if (CurrentOverlay[x][y].UnitID.ArmyID != Unit.ArmyID):
                            TargetList.append(AIEnemyInfo(ReturnPositive(StartX, x), ReturnPositive(StartY, y), x, y))
                            is_target = True
        else:
            # Shooting north
            if (CurrentMap[StartX][StartY].VisibleN == True):
                if (CurrentOverlay[StartX-1][StartY].UnitID != "None"):
                    if (CurrentOverlay[StartX-1][StartY].UnitID.ArmyID != Unit.ArmyID):
                        TargetList.append(AIEnemyInfo(ReturnPositive(StartX, StartX-1), ReturnPositive(StartY, StartY), StartX-1, StartY))
                        is_target = True
                    CurrentOverlay[StartX-1][StartY].FireNorth = False
                CurrentOverlay[StartX-1][StartY].RangeCheck = True
                CurrentOverlay[StartX-1][StartY].CheckDelay = True
                CurrentOverlay[StartX-1][StartY].FireSouth = False
            # Shooting east
            if (CurrentMap[StartX][StartY].VisibleE == True):
                if (CurrentOverlay[StartX][StartY+1].UnitID != "None"):
                    if (CurrentOverlay[StartX][StartY+1].UnitID.ArmyID != Unit.ArmyID):
                        TargetList.append(AIEnemyInfo(ReturnPositive(StartX, StartX), ReturnPositive(StartY, StartY+1), StartX, StartY+1))
                        is_target = True
                    CurrentOverlay[StartX][StartY+1].FireEast = False
                CurrentOverlay[StartX][StartY+1].RangeCheck = True
                CurrentOverlay[StartX][StartY+1].CheckDelay = True
                CurrentOverlay[StartX][StartY+1].FireWest = False
            # Shooting south
            if (CurrentMap[StartX][StartY].VisibleS == True):
                if (CurrentOverlay[StartX+1][StartY].UnitID != "None"):
                    if (CurrentOverlay[StartX+1][StartY].UnitID.ArmyID != Unit.ArmyID):
                        TargetList.append(AIEnemyInfo(ReturnPositive(StartX, StartX+1), ReturnPositive(StartY, StartY), StartX+1, StartY))
                        is_target = True
                    CurrentOverlay[StartX+1][StartY].FireSouth = False
                CurrentOverlay[StartX+1][StartY].RangeCheck = True
                CurrentOverlay[StartX+1][StartY].CheckDelay = True
                CurrentOverlay[StartX+1][StartY].FireNorth = False
            # Shooting west
            if (CurrentMap[StartX][StartY].VisibleW == True):
                if (CurrentOverlay[StartX][StartY-1].UnitID != "None"):
                    if (CurrentOverlay[StartX][StartY-1].UnitID.ArmyID != Unit.ArmyID):
                        TargetList.append(AIEnemyInfo(ReturnPositive(StartX, StartX), ReturnPositive(StartY, StartY-1), StartX, StartY-1))
                        is_target = True
                    CurrentOverlay[StartX][StartY-1].FireWest = False
                CurrentOverlay[StartX][StartY-1].RangeCheck = True
                CurrentOverlay[StartX][StartY-1].CheckDelay = True
                CurrentOverlay[StartX][StartY-1].FireEast = False
                
            for ranged in range(1, Attack.Range):
                for x in range(0, len(CurrentOverlay)):
                    for y in range(0, len(CurrentOverlay[x])):
                        if (CurrentOverlay[x][y].RangeCheck == True):
                            if (CurrentOverlay[x][y].CheckAround == False):
                                if (CurrentOverlay[x][y].CheckDelay == True):
                                    if (CurrentMap[x][y].VisibleN == True):
                                        if (CurrentOverlay[x][y].FireNorth == True):
                                            if (CurrentOverlay[x-1][y].UnitID != "None"):
                                                if (CurrentOverlay[x-1][y].UnitID.ArmyID != Unit.ArmyID):
                                                    TargetList.append(AIEnemyInfo(ReturnPositive(StartX, x), ReturnPositive(StartY, y), x, y))
                                                    is_target = True
                                                CurrentOverlay[x-1][y].FireNorth = False
                                            CurrentOverlay[x-1][y].RangeCheck = True
                                            CurrentOverlay[x-1][y].FireSouth = False
                                            if (CurrentOverlay[x+1][y+1].FireEast == False):
                                                if (CurrentOverlay[x+1][y+1].UnitID != "None"):
                                                    CurrentOverlay[x][y+1].FireEast = False
                                            if (CurrentOverlay[x+1][y-1].FireWest == False):
                                                if (CurrentOverlay[x+1][y-1].UnitID != "None"):
                                                    CurrentOverlay[x][y-1].FireWest = False
                                    if (CurrentMap[x][y].VisibleE == True):
                                        if (CurrentOverlay[x][y].FireEast == True):
                                            if (CurrentOverlay[x][y+1].UnitID != "None"):
                                                if (CurrentOverlay[x][y+1].UnitID.ArmyID != Unit.ArmyID):
                                                    TargetList.append(AIEnemyInfo(ReturnPositive(StartX, x), ReturnPositive(StartY, y), x, y))
                                                    is_target = True
                                                CurrentOverlay[x][y+1].FireEast = False
                                            CurrentOverlay[x][y+1].RangeCheck = True
                                            CurrentOverlay[x][y+1].FireWest = False
                                            if (CurrentOverlay[x-1][y-1].FireNorth == False):
                                                if (CurrentOverlay[x-1][y-1].UnitID != "None"):
                                                    CurrentOverlay[x-1][y].FireNorth = False
                                            if (CurrentOverlay[x+1][y-1].FireSouth == False):
                                                if (CurrentOverlay[x+1][y-1].UnitID != "None"):
                                                    CurrentOverlay[x+1][y].FireSouth = False
                                    if (CurrentMap[x][y].VisibleS == True):
                                        if (CurrentOverlay[x][y].FireSouth == True):
                                            if (CurrentOverlay[x+1][y].UnitID != "None"):
                                                if (CurrentOverlay[x+1][y].UnitID.ArmyID != Unit.ArmyID):
                                                    TargetList.append(AIEnemyInfo(ReturnPositive(StartX, x), ReturnPositive(StartY, y), x, y))
                                                    is_target = True
                                                CurrentOverlay[x+1][y].FireSouth = False
                                            CurrentOverlay[x+1][y].RangeCheck = True
                                            CurrentOverlay[x+1][y].FireNorth = False
                                            if (CurrentOverlay[x-1][y+1].FireEast == False):
                                                if (CurrentOverlay[x-1][y+1].UnitID != "None"):
                                                    CurrentOverlay[x][y+1].FireEast = False
                                            if (CurrentOverlay[x-1][y-1].FireWest == False):
                                                if (CurrentOverlay[x-1][y-1].UnitID != "None"):
                                                    CurrentOverlay[x][y-1].FireWest = False
                                    if (CurrentMap[x][y].VisibleW == True):
                                        if (CurrentOverlay[x][y].FireWest == True):
                                            if (CurrentOverlay[x][y-1].UnitID != "None"):
                                                if (CurrentOverlay[x][y-1].UnitID.ArmyID != Unit.ArmyID):
                                                    TargetList.append(AIEnemyInfo(ReturnPositive(StartX, x), ReturnPositive(StartY, y), x, y))
                                                    is_target = True
                                                CurrentOverlay[x][y-1].FireWest = False
                                            CurrentOverlay[x][y-1].RangeCheck = True
                                            CurrentOverlay[x][y-1].FireEast = False
                                            if (CurrentOverlay[x-1][y+1].FireNorth == False):
                                                if (CurrentOverlay[x-1][y+1].UnitID != "None"):
                                                    CurrentOverlay[x-1][y].FireNorth = False
                                            if (CurrentOverlay[x+1][y+1].FireSouth == False):
                                                if (CurrentOverlay[x+1][y+1].UnitID != "None"):
                                                    CurrentOverlay[x+1][y].FireSouth = False
                            
                                    CurrentOverlay[x][y].CheckAround = True        
                                    
                for x in range(0, len(CurrentOverlay)):
                    for y in range(0, len(CurrentOverlay[x])):
                        if (CurrentOverlay[x][y].RangeCheck == True):
                            if (CurrentOverlay[x][y].CheckAround == True):
                                CurrentOverlay[x][y].CheckDelay = False
                            else:
                                CurrentOverlay[x][y].CheckDelay = True
        
        for x in range(0, len(CurrentOverlay)):
            for y in range(0, len(CurrentOverlay[x])):
                CurrentOverlay[x][y].FireNorth = True
                CurrentOverlay[x][y].FireEast = True
                CurrentOverlay[x][y].FireSouth = True
                CurrentOverlay[x][y].FireWest = True
                CurrentOverlay[x][y].RangeCheck = False
                CurrentOverlay[x][y].CheckAround = False
                CurrentOverlay[x][y].CheckDelay = False
        if (ReturnList == False):
            return is_target
        else:
            return TargetList
                
    def ReturnSameList(List):
        temp = []
        for x in range(0, len(List)):
            temp.append(List[x])
        return temp
        
    
    def AIAttackTarget(Unit, Attack, StartX, StartY):
        global CurrentOverlay
        target_list = IsTarget(Unit, Attack, StartX, StartY, Indirect=Attack.IndirectFire, ReturnList=True)
        
        target_ID = 0
        target_distance = 1000
        for x in range(0, len(target_list)):
            if (target_list[x].TotalDistance < target_distance):
                target_ID = x
                target_distance = target_list[x].TotalDistance
        return target_list[target_ID]
        

        
        
        
    def ResetAttack():
        global TempUnitID
        global RangeCalculation
        global TargetX
        global TargetY
        global TargetID
        global SelectedAttack
        global ResolvingDamage
        global CurrentOverlay
        
        StartX = 0
        StartY = 0
        TempUnitID = []
        RangeCalculation = False
        TargetX = 0
        TargetY = 0
        TargetID = []
        SelectedAttack = []
        ResolvingDamage = False
        for x in range(0, len(CurrentOverlay)):
            for y in range(0, len(CurrentOverlay[x])):
                CurrentOverlay[x][y].RangeOverlay = "None"
                CurrentOverlay[x][y].FireNorth = True
                CurrentOverlay[x][y].FireSouth = True
                CurrentOverlay[x][y].FireEast = True
                CurrentOverlay[x][y].FireWest = True
                CurrentOverlay[x][y].RangeCheck = False
                CurrentOverlay[x][y].CheckAround = False
                CurrentOverlay[x][y].CheckDelay = False

        