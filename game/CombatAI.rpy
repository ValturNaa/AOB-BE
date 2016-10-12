init python:
    def ReturnPositive(Start, Target):
        temp1 = Start - Target
        temp2 = temp1*temp1
        temp3 = temp2**0.5
        return temp2
        
    def GetX(Unit):
        for x in range(0, len(Map)):
            for y in range(0, len(Map[x])):
                if (Map.UnitPresent == Unit.BattleName):
                    StartX = x
        return StartX
        
    def GetY(Unit):
        for x in range(0, len(Map)):
            for y in range(0, len(Map[x])):
                if (Map.UnitPresent == Unit.BattleName):
                    StartY = y
        return StartY
        
        
    class AIEnemyInfo(object):
        def __init__(self, XDistance, YDistance, x, y):
            self.XDistance = XDistance
            self.Ydistance = YDistance
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
                if (Map.UnitPresent == Unit.BattleName):
                    StartX = x
                    StartY = y
                else:
                    pass
        for x in range(0, len(Map)):
            for y in range(0, len(Map[x])):
                if (Map[x][y].UnitPresent == "Null"):
                    pass
                else:
                    if (Map[x][y].UnitPresent.ArmyID == Unit.ArmyID):
                        pass
                    else:
                        TargetList.append(AIEnemyInfo(ReturnPositive(StartX, x), ReturnPositive(StartY, y), x, y))
                        PotentailTarget += 1
        for x in range(0, len(TargetList)):
            if (TargetList[x].TotalDistance < ClosestTargetDistance):
                ClosestTargetDistance = TargetList[x].TotalDistance
                ClosestTarget = x
        return TargetList[ClosestTarget]
        
    def AIDecideAction(Unit, Map):
        Action = "Move"
        ClosestTarget = IDNearestTarget(Unit, Map)
        for x in range(0, len(Unit.BattleSkills)):
            if (ClosestTargetDistance >= Unit.BattleSkills[x].Range):
                Action = "Attack"
            elif (ClosestTargetDistance >= Unit.BattleSkills[x].Range + Unit.MovementCurrent):
                if (Action != "Attack"):
                    Action = "Move Attack"
            else:
                if (Action != "Attack" and Action != "Move Attack"):
                    Action = "Move"
        return Action
        
    def ReturnPlus(x):
        temp1 = x*x
        temp2 = temp1**0.5
        return temp2
        
    def AISetDestination(Unit, Map, StartX, StartY, PathList, AITarget):
        if (StartX > AITarget.Xpos):
            LeftRight = "Right"
        else:
            LeftRight = "Left"
        if (StartY > AITarget.Ypos):
            UpDown = "Down"
        else:
            UpDown = "Up"
        if (LeftRight == "Right"):
            PerfectFinishX = AITarget.Xpos+1
        else:
            PerfectFinishX = AITarget.Xpos-1
        if (UpDown == "Down"):
            PerfectFinishY = AITarget.Ypos+1
        else:
            PerfectFinishY = AITarget.Ypos-1
        PathDifference = 1000
        StoreDifference = 1000
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
                BestPath = path
                
        return PathList[BestPath]
            
            
        