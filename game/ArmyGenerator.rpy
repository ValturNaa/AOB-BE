      
init 5 python:
    # def __init__(self, Ferocity, Finesse, Determination, Cunning,  BattleName, OrigionalName, BattleSkills, Traits, MovementMax, BattleSpriteIdle, BattleSpriteHover, BattleSpriteMove, Mugshot, Gender, ArmyID, PAB=0, CAB=0, PRB=0, CRB=0)

    FWolf = unit(0, 0, 0, 0, "FWolf", "Claw Wolf", [E_FWolfClaw], [], 4, "FWolfIdle", "FWolfHover", "FWolfMove", "FWolfMug", "Female", 2)
    MWolf = unit(0, 0, 0, 0, "MWolf", "Claw Wolf", [E_MWolfClaw], [], 4, "MWolfIdle", "MWolfHover", "MWolfMove", "MWolfMug", "Male", 2)
    Bruiser = unit(0, 0, 0, 0, "Bruiser", "Bruiser", [E_BruiserClub], [], 2, "BruiserIdle", "BruiserHover", "BruiserMove", "BruiserMug", "Male", 2)
    BanditArcher = unit(0, 0, 0, 0, "BanditArcher", "Bandit Archer", [E_BanditArcherBow], [], 3, "BanditArcherIdle", "BanditArcherHover", "BanditArcherMove", "BanditArcherMug", "Female", 2)
    Thug = unit(0, 0, 0, 0, "Thug", "Thug", [E_ThugKnife], [], 4, "ThugIdle", "ThugHover", "ThugMove", "ThugMug", "Male", 2)
        
    def EnemyArmyGenerator(ArmyType, Quantity, Strength):
        enemy_pool = []
        if (ArmyType == "Bandits"):
            enemy_pool.append(Bruiser)
            enemy_pool.append(BanditArcher)
            enemy_pool.append(Thug)
        if (ArmyType == "Wolf Pack"):
            enemy_pool.append(FWolf)
            enemy_pool.append(MWolf)
        
        return_army = []
        for x in range(0, Quantity):
            random = renpy.random.randint(0, len(enemy_pool)-1)
            return_army.append(unit(EnemyStat(Strength), EnemyStat(Strength), EnemyStat(Strength), EnemyStat(Strength),  enemy_pool[random].BattleName, enemy_pool[random].OrigionalName, enemy_pool[random].BattleSkills, enemy_pool[random].Traits, enemy_pool[random].MovementMax, enemy_pool[random].BattleSpriteIdle, enemy_pool[random].BattleSpriteHover, enemy_pool[random].BattleSpriteMove, enemy_pool[random].Mugshot, enemy_pool[random].Gender, enemy_pool[random].ArmyID))
        
        for x in return_army:
            if (x.BattleName == "BanditArcher"):
                x.PhysicalResist = x.PhysicalResist/2
        return return_army
    
    
    
    def EnemyStat(Strength):
        bottom = int(Strength/1.5)
        top = int(Strength*1.5)
        stat = renpy.random.randint(bottom, top)
        return stat