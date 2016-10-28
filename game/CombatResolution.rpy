init:
    transform Fade:
        alpha 1.0
        linear 1.0 alpha 0.0
    transform FloatingDamage1:
        xpos 235 ypos 825
        linear 1.0 xpos 235 ypos 750
    transform FloatingDamage2:
        xpos 1085 ypos 825
        linear 1.0 xpos 1085 ypos 750


init python:
    TempUnitID = []
    RangeCalculation = False
    TargetX = 0
    TargetY = 0
    TargetID = []
    ResolvingDamage = False
    
    class Damage(object):
        def __init__(self):
            self.FinalDamage = 0
            self.CriticalHit = False
            self.CriticalResist = False
            self.DamageType = "None"
            
    # will always be GetDamage(MoveSelect[0], SelectedAttack[0], TargetID[0])        
    def GetDamage(Attacker, Weapon, Defender):
        ReturnedAttack = Damage()
        if (Weapon.DamageType == "Physical"):
            ReturnedAttack.DamageType = "Physical"
        elif (Weapon.DamageType == "Charm"):
            ReturnedAttack.DamageType = "Charm"
            
        if (Weapon.DamageType == "Physical"):
            Basic = Attacker.Agression+Weapon.Damage
        elif (Weapon.DamageType == "Charm"):
            Basic = Attacker.Seduction+Weapon.Damage
        TopDamage = int(Basic*1.2)
        BottomDamage = int(Basic*0.8)
        UnmodifiedDamage = renpy.random.randint(BottomDamage, TopDamage)

        if (Weapon.DamageType =="Physical"):
            ResistRange = Defender.PhysicalResist+Defender.PRB
        elif (Weapon.DamageType =="Physical"):
            ResistRange = Defender.CharmResist+Defender.CRB
        RandomBlock = renpy.random.randint(0, ResistRange)
        
        BlockedDamage = UnmodifiedDamage-RandomBlock
        if (BlockedDamage <= 0):
            BlockedDamage = 1
        CritDamage = BlockedDamage
        CompleteDamage = BlockedDamage
        
        CritCalculator = renpy.random.randint(0, 10)
        if (CritCalculator == 1):
            ReturnedAttack.CriticalHit = True
            CritDamage = BlockedDamage*1.5
            CompleteDamage = CritDamage
            
        ResistCalculator = renpy.random.randint(0, 10)
        if (ResistCalculator == 1):
            ReturnedAttack.CriticalResist = True
            CompleteDamage = CritDamage*0.3
        ReturnedAttack.FinalDamage = int(CompleteDamage)
        
        return ReturnedAttack
    




    
label AttackRange:
    python:
        RangeCalculation = True
        PickingDestination = False
        # Reset the invisible overlay
        for x in range(0, len(CurrentOverlay)):
            for y in range(0, len(CurrentOverlay[x])):
                if CurrentOverlay[x][y].UnitPresent == "Move":
                    CurrentOverlay[x][y].UnitPresent = "Null"
        
        # Since all weapons have a range of at least 1, establish the first four directional target tiles
        if SelectedAttack[0].IndirectFire == False:
            # Shooting north
            if CurrentOverlay[StartX-1][StartY].UnitID != "None":
                TempUnitID = []
                TempUnitID.append(CurrentOverlay[StartX-1][StartY].UnitID)
                if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                    CurrentOverlay[StartX-1][StartY].RangeOverlay = "Range"
                    CurrentOverlay[StartX-1][StartY].FireNorth = False
                else:
                    CurrentOverlay[StartX-1][StartY].RangeOverlay = "Target"
                    CurrentOverlay[StartX-1][StartY].FireNorth = False
            else:
                CurrentOverlay[StartX-1][StartY].RangeOverlay = "Range"
            CurrentOverlay[StartX-1][StartY].RangeCheck = True
            CurrentOverlay[StartX-1][StartY].CheckDelay = True
            CurrentOverlay[StartX-1][StartY].FireSouth = False
            # Shooting east
            if CurrentOverlay[StartX][StartY+1].UnitID != "None":
                TempUnitID = []
                TempUnitID.append(CurrentOverlay[StartX][StartY+1].UnitID)
                if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                    CurrentOverlay[StartX][StartY+1].RangeOverlay = "Range"
                    CurrentOverlay[StartX][StartY+1].FireEast = False
                else:
                    CurrentOverlay[StartX][StartY+1].RangeOverlay = "Target"
                    CurrentOverlay[StartX][StartY+1].FireEast = False
            else:
                CurrentOverlay[StartX][StartY+1].RangeOverlay = "Range"
            CurrentOverlay[StartX][StartY+1].RangeCheck = True
            CurrentOverlay[StartX][StartY+1].CheckDelay = True
            CurrentOverlay[StartX][StartY+1].FireWest = False
            # Shooting south
            if CurrentOverlay[StartX+1][StartY].UnitID != "None":
                TempUnitID = []
                TempUnitID.append(CurrentOverlay[StartX+1][StartY].UnitID)
                if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                    CurrentOverlay[StartX+1][StartY].RangeOverlay = "Range"
                    CurrentOverlay[StartX+1][StartY].FireSouth = False
                else:
                    CurrentOverlay[StartX+1][StartY].RangeOverlay = "Target"
                    CurrentOverlay[StartX+1][StartY].FireSouth = False
            else:
                CurrentOverlay[StartX+1][StartY].RangeOverlay = "Range"
            CurrentOverlay[StartX+1][StartY].RangeCheck = True
            CurrentOverlay[StartX+1][StartY].CheckDelay = True
            CurrentOverlay[StartX+1][StartY].FireNorth = False
            # Shooting west
            if CurrentOverlay[StartX][StartY-1].UnitID != "None":
                TempUnitID = []
                TempUnitID.append(CurrentOverlay[StartX][StartY-1].UnitID)
                if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                    CurrentOverlay[StartX][StartY-1].RangeOverlay = "Range"
                    CurrentOverlay[StartX][StartY-1].FireWest = False
                else:
                    CurrentOverlay[StartX][StartY-1].RangeOverlay = "Target"
                    CurrentOverlay[StartX][StartY-1].FireWest = False
            else:
                CurrentOverlay[StartX][StartY-1].RangeOverlay = "Range"
            CurrentOverlay[StartX][StartY-1].RangeCheck = True
            CurrentOverlay[StartX][StartY-1].CheckDelay = True
            CurrentOverlay[StartX][StartY-1].FireEast = False
                    
            for ranged in range(1, SelectedAttack[0].Range):
                for x in range(0, len(CurrentOverlay)):
                    for y in range(0, len(CurrentOverlay[x])):
                        if CurrentOverlay[x][y].RangeCheck == True:
                            if CurrentOverlay[x][y].CheckAround == False:
                                if CurrentOverlay[x][y].CheckDelay == True:
                                    if CurrentMap[x][y].VisibleN == True:
                                        if CurrentOverlay[x][y].FireNorth == True:
                                            if CurrentOverlay[x-1][y].UnitID != "None":
                                                TempUnitID = []
                                                TempUnitID.append(CurrentOverlay[x-1][y].UnitID)
                                                if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                                                    CurrentOverlay[x-1][y].RangeOverlay = "Range"
                                                    CurrentOverlay[x-1][y].FireNorth = False
                                                else:
                                                    CurrentOverlay[x-1][y].RangeOverlay = "Target"
                                                    CurrentOverlay[x-1][y].FireNorth = False
                                            else:
                                                CurrentOverlay[x-1][y].RangeOverlay = "Range"
                                            CurrentOverlay[x-1][y].RangeCheck = True
                                            CurrentOverlay[x-1][y].FireSouth = False
                                            if CurrentOverlay[x+1][y+1].FireEast == False:
                                                if CurrentOverlay[x+1][y+1].UnitID != "None":
                                                    CurrentOverlay[x][y+1].FireEast = False
                                            if CurrentOverlay[x+1][y-1].FireWest == False:
                                                if CurrentOverlay[x+1][y-1].UnitID != "None":
                                                    CurrentOverlay[x][y-1].FireWest = False
                                    if CurrentMap[x][y].VisibleE == True:
                                        if CurrentOverlay[x][y].FireEast == True:
                                            if CurrentOverlay[x][y+1].UnitID != "None":
                                                TempUnitID = []
                                                TempUnitID.append(CurrentOverlay[x][y+1].UnitID)
                                                if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                                                    CurrentOverlay[x][y+1].RangeOverlay = "Range"
                                                    CurrentOverlay[x][y+1].FireEast = False
                                                else:
                                                    CurrentOverlay[x][y+1].RangeOverlay = "Target"
                                                    CurrentOverlay[x][y+1].FireEast = False
                                            else:
                                                CurrentOverlay[x][y+1].RangeOverlay = "Range"
                                            CurrentOverlay[x][y+1].RangeCheck = True
                                            CurrentOverlay[x][y+1].FireWest = False
                                            if CurrentOverlay[x-1][y-1].FireNorth == False:
                                                if CurrentOverlay[x-1][y-1].UnitID != "None":
                                                    CurrentOverlay[x-1][y].FireNorth = False
                                            if CurrentOverlay[x+1][y-1].FireSouth == False:
                                                if CurrentOverlay[x+1][y-1].UnitID != "None":
                                                    CurrentOverlay[x+1][y].FireSouth = False
                                    if CurrentMap[x][y].VisibleS == True:
                                        if CurrentOverlay[x][y].FireSouth == True:
                                            if CurrentOverlay[x+1][y].UnitID != "None":
                                                TempUnitID = []
                                                TempUnitID.append(CurrentOverlay[x+1][y].UnitID)
                                                if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                                                    CurrentOverlay[x+1][y].RangeOverlay = "Range"
                                                    CurrentOverlay[x+1][y].FireSouth = False
                                                else:
                                                    CurrentOverlay[x+1][y].RangeOverlay = "Target"
                                                    CurrentOverlay[x+1][y].FireSouth = False
                                            else:
                                                CurrentOverlay[x+1][y].RangeOverlay = "Range"
                                            CurrentOverlay[x+1][y].RangeCheck = True
                                            CurrentOverlay[x+1][y].FireNorth = False
                                            if CurrentOverlay[x-1][y+1].FireEast == False:
                                                if CurrentOverlay[x-1][y+1].UnitID != "None":
                                                    CurrentOverlay[x][y+1].FireEast = False
                                            if CurrentOverlay[x-1][y-1].FireWest == False:
                                                if CurrentOverlay[x-1][y-1].UnitID != "None":
                                                    CurrentOverlay[x][y-1].FireWest = False
                                    if CurrentMap[x][y].VisibleW == True:
                                        if CurrentOverlay[x][y].FireWest == True:
                                            if CurrentOverlay[x][y-1].UnitID != "None":
                                                TempUnitID = []
                                                TempUnitID.append(CurrentOverlay[x][y-1].UnitID)
                                                if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                                                    CurrentOverlay[x][y-1].RangeOverlay = "Range"
                                                    CurrentOverlay[x][y-1].FireWest = False
                                                else:
                                                    CurrentOverlay[x][y-1].RangeOverlay = "Target"
                                                    CurrentOverlay[x][y-1].FireWest = False
                                            else:
                                                CurrentOverlay[x][y-1].RangeOverlay = "Range"
                                            CurrentOverlay[x][y-1].RangeCheck = True
                                            CurrentOverlay[x][y-1].FireEast = False
                                            if CurrentOverlay[x-1][y+1].FireNorth == False:
                                                if CurrentOverlay[x-1][y+1].UnitID != "None":
                                                    CurrentOverlay[x-1][y].FireNorth = False
                                            if CurrentOverlay[x+1][y+1].FireSouth == False:
                                                if CurrentOverlay[x+1][y+1].UnitID != "None":
                                                    CurrentOverlay[x+1][y].FireSouth = False
                            
                                    CurrentOverlay[x][y].CheckAround = True
                for x in range(0, len(CurrentOverlay)):
                    for y in range(0, len(CurrentOverlay[x])):
                        if CurrentOverlay[x][y].RangeCheck == True:
                            if CurrentOverlay[x][y].CheckAround == True:
                                CurrentOverlay[x][y].CheckDelay = False
                            else:
                                CurrentOverlay[x][y].CheckDelay = True
                                
                
        else:
            if CurrentMap[StartX-1][StartY].Void == False:
                # Shooting north
                if CurrentOverlay[StartX-1][StartY].UnitID != "None":
                    TempUnitID = []
                    TempUnitID.append(CurrentOverlay[StartX-1][StartY].UnitID)
                    if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                        CurrentOverlay[StartX-1][StartY].RangeOverlay = "Range"
                    else:
                        CurrentOverlay[StartX-1][StartY].RangeOverlay = "Target"
                else:
                    CurrentOverlay[StartX-1][StartY].RangeOverlay = "Range"
                CurrentOverlay[StartX-1][StartY].RangeCheck = True
                CurrentOverlay[StartX-1][StartY].CheckDelay = True
            if CurrentMap[StartX][StartY+1].Void == False:
                # Shooting east
                if CurrentOverlay[StartX][StartY+1].UnitID != "None":
                    TempUnitID = []
                    TempUnitID.append(CurrentOverlay[StartX][StartY+1].UnitID)
                    if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                        CurrentOverlay[StartX][StartY+1].RangeOverlay = "Range"
                    else:
                        CurrentOverlay[StartX][StartY+1].RangeOverlay = "Target"
                else:
                    CurrentOverlay[StartX][StartY+1].RangeOverlay = "Range"
                CurrentOverlay[StartX][StartY+1].RangeCheck = True
                CurrentOverlay[StartX][StartY+1].CheckDelay = True
            if CurrentMap[StartX+1][StartY].Void == False:
                # Shooting south
                if CurrentOverlay[StartX+1][StartY].UnitID != "None":
                    TempUnitID = []
                    TempUnitID.append(CurrentOverlay[StartX+1][StartY].UnitID)
                    if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                        CurrentOverlay[StartX+1][StartY].RangeOverlay = "Range"
                    else:
                        CurrentOverlay[StartX+1][StartY].RangeOverlay = "Target"
                else:
                    CurrentOverlay[StartX+1][StartY].RangeOverlay = "Range"
                CurrentOverlay[StartX+1][StartY].RangeCheck = True
                CurrentOverlay[StartX+1][StartY].CheckDelay = True
            if CurrentMap[StartX][StartY-1].Void == False:
                # Shooting west
                if CurrentOverlay[StartX][StartY-1].UnitID != "None":
                    TempUnitID = []
                    TempUnitID.append(CurrentOverlay[StartX][StartY-1].UnitID)
                    if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                        CurrentOverlay[StartX][StartY-1].RangeOverlay = "Range"
                    else:
                        CurrentOverlay[StartX][StartY-1].RangeOverlay = "Target"
                else:
                    CurrentOverlay[StartX][StartY-1].RangeOverlay = "Range"
                CurrentOverlay[StartX][StartY-1].RangeCheck = True
                CurrentOverlay[StartX][StartY-1].CheckDelay = True
        
            for ranged in range(1, SelectedAttack[0].Range):
                
                for x in range(0, len(CurrentOverlay)):
                    for y in range(0, len(CurrentOverlay[x])):
                        if CurrentOverlay[x][y].RangeCheck == True:
                            if CurrentOverlay[x][y].CheckAround == False:
                                if CurrentOverlay[x][y].CheckDelay == True:
                                    if CurrentMap[x-1][y].Void == False:
                                        if CurrentOverlay[x-1][y].UnitID != "None":
                                            TempUnitID = []
                                            TempUnitID.append(CurrentOverlay[x-1][y].UnitID)
                                            if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                                                CurrentOverlay[x-1][y].RangeOverlay = "Range"
                                            else:
                                                CurrentOverlay[x-1][y].RangeOverlay = "Target"
                                        else:
                                            CurrentOverlay[x-1][y].RangeOverlay = "Range"
                                        CurrentOverlay[x-1][y].RangeCheck = True
                                    if CurrentMap[x][y+1].Void == False:    
                                        if CurrentOverlay[x][y+1].UnitID != "None":
                                            TempUnitID = []
                                            TempUnitID.append(CurrentOverlay[x][y+1].UnitID)
                                            if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                                                CurrentOverlay[x][y+1].RangeOverlay = "Range"
                                            else:
                                                CurrentOverlay[x][y+1].RangeOverlay = "Target"
                                        else:
                                            CurrentOverlay[x][y+1].RangeOverlay = "Range"
                                        CurrentOverlay[x][y+1].RangeCheck = True
                                    if CurrentMap[x+1][y].Void == False:
                                        if CurrentOverlay[x+1][y].UnitID != "None":
                                            TempUnitID = []
                                            TempUnitID.append(CurrentOverlay[x+1][y].UnitID)
                                            if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                                                CurrentOverlay[x+1][y].RangeOverlay = "Range"
                                            else:
                                                CurrentOverlay[x+1][y].RangeOverlay = "Target"
                                        else:
                                            CurrentOverlay[x+1][y].RangeOverlay = "Range"
                                        CurrentOverlay[x+1][y].RangeCheck = True
                                    if CurrentMap[x][y-1].Void == False:
                                        if CurrentOverlay[x][y-1].UnitID != "None":
                                            TempUnitID = []
                                            TempUnitID.append(CurrentOverlay[x][y-1].UnitID)
                                            if MoveSelect[0].ArmyID == TempUnitID[0].ArmyID:
                                                CurrentOverlay[x][y-1].RangeOverlay = "Range"
                                            else:
                                                CurrentOverlay[x][y-1].RangeOverlay = "Target"
                                        else:
                                            CurrentOverlay[x][y-1].RangeOverlay = "Range"
                                        CurrentOverlay[x][y-1].RangeCheck = True
                                    CurrentOverlay[x][y].CheckAround = True
                        
                                    
                for x in range(0, len(CurrentOverlay)):
                    for y in range(0, len(CurrentOverlay[x])):
                        if CurrentOverlay[x][y].RangeCheck == True:
                            if CurrentOverlay[x][y].CheckAround == True:
                                CurrentOverlay[x][y].CheckDelay = False
                            else:
                                CurrentOverlay[x][y].CheckDelay = True
            
            
            
    jump RenderMap
    
    
    
label ResolveDamage:
    default CombatDamage = "Nothing"
    python:
        CombatDamage = GetDamage(MoveSelect[0], SelectedAttack[0], TargetID[0])
        MoveSelect[0].Action = False
        MoveSelect[0].MovementCurrent = 0
        ResolvingDamage = True
        RangeCalculation = False
        renpy.restart_interaction()
    
    show screen DamageScreen(Damage=CombatDamage.FinalDamage, ArmyID=TargetID[0].ArmyID, Attacker=MoveSelect[0], Defender=TargetID[0], Attack=SelectedAttack[0])
    python:
        while CombatDamage.FinalDamage > 0:
            TargetID[0].CurrentMorale -= 1
            CombatDamage.FinalDamage -= 1
            renpy.pause(0.01)
        if TargetID[0].CurrentMorale <= 0:
            renpy.hide("EnemyMonsterCard")
            TargetID[0].Routed = True
            CurrentOverlay[TargetX][TargetY].UnitPresent="Null"
            CurrentOverlay[TargetX][TargetY].UnitIdle="None"
            CurrentOverlay[TargetX][TargetY].UnitHover="None"
            CurrentOverlay[TargetX][TargetY].UnitID="None"
            CurrentOverlay[TargetX][TargetY].Visibility = 0
    pause 2.5
    hide screen DamageScreen
    call ResetMoveVariables from _call_ResetMoveVariables_2
    jump RenderMap
    

screen DamageScreen(Damage, ArmyID, Attacker, Defender, Attack):
    
    if Attacker.ArmyID == 1:
        add Attack.Animation xpos 100 ypos 100
    else:
        add Attack.Animation xpos 600 ypos 100
        
    if Defender.ArmyID == 1:
        add Defender.PFlinch xpos 100 ypos 100
    else:
        add Defender.PFlinch xpos 600 ypos 100
    
    if ArmyID == 1:
        text "-[Damage]" at FloatingDamage1, Fade
    else:
        text "-[Damage]" at FloatingDamage2, Fade