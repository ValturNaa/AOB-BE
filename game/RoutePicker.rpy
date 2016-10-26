init python:
    class Path(object):
        def __init__(self):
            self.Self = self
            self.Name = "None"
            # in the format [[Direction(E.g. "N"), [distance up / down from start. distance left / right from start]]] for each step
            self.WayPoints = []
            # Number of remaining move points needed to use this in the first place
            self.MoveRequired = 0
            # if the path is usable
            self.Active = True
            # if all possible extensions of this path have been explored
            self.Explored = False
            
    def NewPathName(Parent, Direction):
        temp = str(Parent)+str(Direction)
        return temp
        
            
    
    # target tile route compilation, optimal path identifier, code path resolution, visual path resolution and resting variable setting        
        
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
    MoveCancel = False
    
    BugTestPath = "None"
    BugTestList = []
    
    def GeneratePaths(MoveSelect, StartX, StartY):
        PathList = []
        if (MoveSelect.MovementCurrent == 0):
            return PathList
        # Establish the first four directions the path could lead
        else:
            if (CurrentMap[StartX][StartY].PassN == True):
                if (CurrentOverlay[StartX-1][StartY].UnitID == "None"):
                    N = Path()
                    N.Name = "N"
                    N.WayPoints = ["N"]
                    N.MoveRequired = CurrentMap[StartX-1][StartY].MoveRequired
                    PathList.append(N)
            if (CurrentMap[StartX][StartY].PassE == True):
                if (CurrentOverlay[StartX][StartY+1].UnitID == "None"):
                    E = Path()
                    E.Name = "E"
                    E.WayPoints = ["E"]
                    E.MoveRequired = CurrentMap[StartX][StartY+1].MoveRequired
                    PathList.append(E)
            if (CurrentMap[StartX][StartY].PassS == True):
                if (CurrentOverlay[StartX+1][StartY].UnitID == "None"):
                    S = Path()
                    S.Name = "S"
                    S.WayPoints = ["S"]
                    S.MoveRequired = CurrentMap[StartX+1][StartY].MoveRequired
                    PathList.append(S)
            if (CurrentMap[StartX][StartY].PassW == True):
                if (CurrentOverlay[StartX][StartY-1].UnitID == "None"):
                    W = Path()
                    W.Name = "W"
                    W.WayPoints = ["W"]
                    W.MoveRequired = CurrentMap[StartX][StartY-1].MoveRequired
                    PathList.append(W)        
                
        if (MoveSelect.MovementCurrent == 0):
            return PathList
        elif (MoveSelect.MovementCurrent == 1):
            return PathList
        # big o'l for loop to generate remaining paths
        else:
            # determine how far this path leads
            for distance in range(1, MoveSelect.MovementCurrent):
                for path in range(0, len(PathList)):
                    # if there is a path that can be extened then this generates a new, extended path
                    if (PathList[path].Explored == False):
                        # establish start point of parent
                        TempStartX = StartX
                        TempStartY = StartY
                        for waypoint in PathList[path].WayPoints:
                            if (waypoint == "N"):
                                TempStartX -= 1
                            if (waypoint == "E"):
                                TempStartY += 1
                            if (waypoint == "S"):
                                TempStartX += 1
                            if (waypoint == "W"):
                                TempStartY -= 1
                        # check if you can move in next direction and generate a new path for that direction
                        if (CurrentMap[TempStartX][TempStartY].PassN == True):
                            if (CurrentOverlay[TempStartX-1][TempStartY].UnitID == "None"):
                                TempPath = []
                                TempPath.append(NewPathName(PathList[path].Name, "N"))
                                TempPath[0] = Path()
                                TempPath[0].Name = NewPathName(PathList[path].Name, "N")
                                for x in PathList[path].WayPoints:
                                    TempPath[0].WayPoints.append(x)
                                TempPath[0].WayPoints.append("N")
                                TempPath[0].MoveRequired = PathList[path].MoveRequired
                                TempPath[0].MoveRequired += CurrentMap[TempStartX-1][TempStartY].MoveRequired
                                PathList.append(TempPath[0])
                        if (CurrentMap[TempStartX][TempStartY].PassE == True):
                            if (CurrentOverlay[TempStartX][TempStartY+1].UnitID == "None"):
                                TempPath = []
                                TempPath.append(NewPathName(PathList[path].Name, "E"))
                                TempPath[0] = Path()
                                TempPath[0].Name = NewPathName(PathList[path].Name, "E")
                                for x in PathList[path].WayPoints:
                                    TempPath[0].WayPoints.append(x)
                                TempPath[0].WayPoints.append("E")
                                TempPath[0].MoveRequired = PathList[path].MoveRequired
                                TempPath[0].MoveRequired += CurrentMap[TempStartX][TempStartY+1].MoveRequired
                                PathList.append(TempPath[0])
                        if (CurrentMap[TempStartX][TempStartY].PassS == True):
                            if (CurrentOverlay[TempStartX+1][TempStartY].UnitID == "None"):
                                TempPath = []
                                TempPath.append(NewPathName(PathList[path].Name, "S"))
                                TempPath[0] = Path()
                                TempPath[0].Name = NewPathName(PathList[path].Name, "S")
                                for x in PathList[path].WayPoints:
                                    TempPath[0].WayPoints.append(x)
                                TempPath[0].WayPoints.append("S")
                                TempPath[0].MoveRequired = PathList[path].MoveRequired
                                TempPath[0].MoveRequired += CurrentMap[TempStartX+1][TempStartY].MoveRequired
                                PathList.append(TempPath[0])
                        if (CurrentMap[TempStartX][TempStartY].PassW == True):
                            if (CurrentOverlay[TempStartX][TempStartY-1].UnitID == "None"):
                                TempPath = []
                                TempPath.append(NewPathName(PathList[path].Name, "W"))
                                TempPath[0] = Path()
                                TempPath[0].Name = NewPathName(PathList[path].Name, "W")
                                for x in PathList[path].WayPoints:
                                    TempPath[0].WayPoints.append(x)
                                TempPath[0].WayPoints.append("W")
                                TempPath[0].MoveRequired = PathList[path].MoveRequired
                                TempPath[0].MoveRequired += CurrentMap[TempStartX][TempStartY-1].MoveRequired
                                PathList.append(TempPath[0])
                        PathList[path].Explored = True
        
        return PathList 
    
    
    
    
label PathGenerator:
    python:
        PathList = GeneratePaths(MoveSelect[0], StartX, StartY)
        

        for path in range(0, len(PathList)):
            TempStartX = StartX
            TempStartY = StartY
            if PathList[path].MoveRequired <= MoveSelect[0].MovementCurrent:
                for waypoint in PathList[path].WayPoints:
                    if waypoint == "N":
                        TempStartX -= 1
                    if waypoint == "E":
                        TempStartY += 1
                    if waypoint == "S":
                        TempStartX += 1
                    if waypoint == "W":
                        TempStartY -= 1
                CurrentOverlay[TempStartX][TempStartY].RouteStore.append(PathList[path])
                if CurrentOverlay[TempStartX][TempStartY].UnitPresent == "Null":
                    CurrentOverlay[TempStartX][TempStartY].UnitPresent = "Move"
        PickingDestination = True
        SelectedBattleSkills = MoveSelect[0].BattleSkills
    jump RenderMap
            
            
label MostEfficientRoute:
    python:
        for route in range(0, len(FinalDestination[0].RouteStore)):
            if len(FinalPath) == 0:
                FinalPath.append(FinalDestination[0].RouteStore[route])
            if len(FinalPath) > 0:
                FinalPathBuffer = []
                FinalPathBuffer.append(FinalDestination[0].RouteStore[route])
                if FinalPathBuffer[0].MoveRequired < FinalPath[0].MoveRequired:
                    FinalPath = []
                    FinalPath.append(FinalPathBuffer[0])
        AtoB = True
        CurrentOverlay[StartX][StartY].UnitPresent = "Null"
        CurrentOverlay[StartX][StartY].UnitID = "None"
        CurrentOverlay[StartX][StartY].UnitIdle = "None"
        CurrentOverlay[StartX][StartY].UnitHover = "None"
        CurrentOverlay[StartX][StartY].Visibility = 0
        
        for x in range(0, len(CurrentOverlay)):
            for y in range(0, len(CurrentOverlay[x])):
                if CurrentOverlay[x][y].UnitPresent == "Move":
                    CurrentOverlay[x][y].UnitPresent = "Null"
        
        MoveSelect[0].MovementCurrent -= FinalPath[0].MoveRequired
        PickingDestination = False
        if FinalPath[0].WayPoints[0] == "N":
            CurrentFacing = "N"
            if MoveTick == False:
                MoveTick = True
                CurrentMove = MovePathN1
            else:
                MoveTick = False
                CurrentMove = MovePathN2
        elif FinalPath[0].WayPoints[0] == "E":
            CurrentFacing = "E"
            if MoveTick == False:
                MoveTick = True
                CurrentMove = MovePathE1
            else:
                MoveTick = False
                CurrentMove = MovePathE2
        elif FinalPath[0].WayPoints[0] == "S":
            CurrentFacing = "S"
            if MoveTick == False:
                MoveTick = True
                CurrentMove = MovePathS1
            else:
                MoveTick = False
                CurrentMove = MovePathS2
        elif FinalPath[0].WayPoints[0] == "W":
            CurrentFacing = "W"
            if MoveTick == False:
                MoveTick = True
                CurrentMove = MovePathW1
            else:
                MoveTick = False
                CurrentMove = MovePathW2
    hide screen CurrentMap
    jump RenderMap
            
            
label FinishMove:
    python:
        CurrentOverlay[FinalDestinationX][FinalDestinationY].UnitPresent = MoveSelect[0].Self
        CurrentOverlay[FinalDestinationX][FinalDestinationY].UnitID = MoveSelect[0]
        CurrentOverlay[FinalDestinationX][FinalDestinationY].UnitIdle = MoveSelect[0].BattleSpriteIdle
        CurrentOverlay[FinalDestinationX][FinalDestinationY].UnitHover = MoveSelect[0].BattleSpriteHover
        CurrentOverlay[FinalDestinationX][FinalDestinationY].Visibility = 1
    call ResetMoveVariables from _call_ResetMoveVariables
    return

label ResetMoveVariables:
    hide screen PlayerMonsterCard
    hide screen EnemyMonsterCard
    python:
        ResetMoveVariables()
    python:
        for x in range(0, len(CurrentOverlay)):
            for y in range(0, len(CurrentOverlay[x])):
                if CurrentOverlay[x][y].UnitPresent == "Move":
                    CurrentOverlay[x][y].UnitPresent = "Null"
    if MoveCancel == True:
        $ MoveCancel = False
        jump RenderMap
    else:
        return
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
