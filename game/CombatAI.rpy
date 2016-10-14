init python:
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
        for x in range(0, len(Unit.BattleSkills)):
            if (ClosestTargetDistance <= Unit.BattleSkills[x].Range):
                Action = "Attack"
            elif (ClosestTargetDistance <= Unit.BattleSkills[x].Range + Unit.MovementCurrent):
                if (Action != "Attack"):
                    Action = "Move Attack"
            else:
                if (Action != "Attack" or Action != "Move Attack"):
                    Action = "Move"
        return Action
        
    def ReturnPlus(x):
        temp1 = x*x
        temp2 = temp1**0.5
        return temp2
        
    def AISetDestination(Unit, Map, StartX, StartY, PathList, AITarget):
        if (StartX > AITarget.Xpos):
            LeftRight = "Up"
        else:
            LeftRight = "Down"
        if (StartY > AITarget.Ypos):
            UpDown = "Right"
        else:
            UpDown = "Left"
        if (LeftRight == "Right"):
            PerfectFinishY = AITarget.Ypos+1
        else:
            PerfectFinishY = AITarget.Ypos-1
        if (UpDown == "Down"):
            PerfectFinishX = AITarget.Xpos+1
        else:
            PerfectFinishX = AITarget.Xpos-1
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
        global MoveCancel
        
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
            MoveCancel = False
            for x in range(0, len(CurrentOverlay)):
                for y in range(0, len(CurrentOverlay[x])):
                    if (CurrentOverlay[x][y].UnitPresent == "Move"):
                        CurrentOverlay[x][y].UnitPresent = "Null"

        
        
        
    def ResetAttack():
        global TempUnitID
        global RangeCalculation
        global TargetX
        global TargetY
        global TargetID
        global SelectedAttack
        global ResolvingDamage
        global CurrentOverlay
            
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

        