        # def __init__(self, Ferocity, Finesse, Determination, Cunning,  BattleName, OrigionalName, BattleSkills, Traits, MovementMax, BattleSpriteIdle, BattleSpriteHover, BattleSpriteMove, Mugshot, Gender, ArmyID, PAB=0, CAB=0, PRB=0, CRB=0)
    
    init python:
        
        FWolf = unit(5, 5, 5, 5, "PlaceHolder", "Soldier", [Stab], [], 4, "SoldierIdle", "SoldierHover", "SoldierMove", "Placeholder", "Female", 2)
        Bruiser = unit(5, 5, 5, 5, "PlaceHolder", "Bruiser", [Club], [], 4, "BruiserIdle", "BruiserHover", "BruiserMove", "Placeholder", "Male", 2)
        def EnemyArmyGenerator(ArmyType, Quantity, Strength):
            
            