        # def __init__(self, Ferocity, Finesse, Determination, Cunning,  BattleName, OrigionalName, BattleSkills, Traits, MovementMax, BattleSpriteIdle, BattleSpriteHover, BattleSpriteMove, Mugshot, Gender, ArmyID, PAB=0, CAB=0, PRB=0, CRB=0)
    
    init 5 python:
        
        FWolf = unit(0, 0, 0, 0, "FWolf", "Claw Wolf", [FWolfClaw], [], 4, "FWolfIdle", "FWolfHover", "FWolfMove", "FWolfMug", "Female", 2)
        MWolf = unit(0, 0, 0, 0, "MWolf", "Claw Wolf", [MWolfClaw], [], 4, "MWolfIdle", "MWolfHover", "MWolfMove", "MWolfMug", "Male", 2)
        Bruiser = unit(0, 0, 0, 0, "Bruiser", "Bruiser", [BruiserClub], [], 2, "BruiserIdle", "BruiserHover", "BruiserMove", "MWolfMug", "Male", 2)
        BanditArcher = unit(0, 0, 0, 0, "BanditArcher", "Bandit Archer", [BanditArcherBow], [], 3, "BanditArcherIdle", "BanditArcherHover", "BanditArcherMove", "FWolfMug", "Female", 2)
        Thug = unit(0, 0, 0, 0, "Thug", "Thug", [ThugKnife], [], 4, "ThugIdle", "ThugHover", "ThugMove", "MWolfMug", "Male", 2)
        
        def EnemyArmyGenerator(ArmyType, Quantity, Strength):
            return "None"
            