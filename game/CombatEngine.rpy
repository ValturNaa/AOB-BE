init -1:
    default BE_ACTIVE = False
    
# zoom and alpha transforms used to wrap various tiles and sprites in the main viewport, though they can be used anywhere.
    transform hidden:
        alpha 0.0
    transform a0p5:
        alpha 0.5
    transform visible:
        alpha 1.0
        

    transform x0p2:
        zoom 0.2
    transform x0p4:
        zoom 0.4
    transform x0p6:
        zoom 0.6
    transform x0p8:
        zoom 0.8
    transform x1:
        zoom 1.0
    transform x1p2:
        zoom 1.2
    transform x1p4:
        zoom 1.4
    transform x1p6:
        zoom 1.6
    transform x1p8:
        zoom 1.8
    transform x2:
        zoom 2.0
        
    # map movement transform
    transform MovePathN1:
        xpos CurrentOverlay[StartX][StartY].XPos ypos CurrentOverlay[StartX][StartY].YPos xanchor 0.0 yanchor 0.0
        linear 1 xpos CurrentOverlay[StartX-1][StartY].XPos ypos CurrentOverlay[StartX-1][StartY].YPos xanchor 0.0 yanchor 0.0
    transform MovePathE1:
        xpos CurrentOverlay[StartX][StartY].XPos ypos CurrentOverlay[StartX][StartY].YPos xanchor 0.0 yanchor 0.0
        linear 1 xpos CurrentOverlay[StartX][StartY+1].XPos ypos CurrentOverlay[StartX][StartY+1].YPos xanchor 0.0 yanchor 0.0
    transform MovePathS1:
        xpos CurrentOverlay[StartX][StartY].XPos ypos CurrentOverlay[StartX][StartY].YPos xanchor 0.0 yanchor 0.0
        linear 1 xpos CurrentOverlay[StartX+1][StartY].XPos ypos CurrentOverlay[StartX+1][StartY].YPos xanchor 0.0 yanchor 0.0
    transform MovePathW1:
        xpos CurrentOverlay[StartX][StartY].XPos ypos CurrentOverlay[StartX][StartY].YPos xanchor 0.0 yanchor 0.0
        linear 1 xpos CurrentOverlay[StartX][StartY-1].XPos ypos CurrentOverlay[StartX][StartY-1].YPos xanchor 0.0 yanchor 0.0
    transform MovePathN2:
        xpos CurrentOverlay[StartX][StartY].XPos ypos CurrentOverlay[StartX][StartY].YPos xanchor 0.0 yanchor 0.0
        linear 1 xpos CurrentOverlay[StartX-1][StartY].XPos ypos CurrentOverlay[StartX-1][StartY].YPos xanchor 0.0 yanchor 0.0
    transform MovePathE2:
        xpos CurrentOverlay[StartX][StartY].XPos ypos CurrentOverlay[StartX][StartY].YPos xanchor 0.0 yanchor 0.0
        linear 1 xpos CurrentOverlay[StartX][StartY+1].XPos ypos CurrentOverlay[StartX][StartY+1].YPos xanchor 0.0 yanchor 0.0
    transform MovePathS2:
        xpos CurrentOverlay[StartX][StartY].XPos ypos CurrentOverlay[StartX][StartY].YPos xanchor 0.0 yanchor 0.0
        linear 1 xpos CurrentOverlay[StartX+1][StartY].XPos ypos CurrentOverlay[StartX+1][StartY].YPos xanchor 0.0 yanchor 0.0
    transform MovePathW2:
        xpos CurrentOverlay[StartX][StartY].XPos ypos CurrentOverlay[StartX][StartY].YPos xanchor 0.0 yanchor 0.0
        linear 1 xpos CurrentOverlay[StartX][StartY-1].XPos ypos CurrentOverlay[StartX][StartY-1].YPos xanchor 0.0 yanchor 0.0
        

    # colours defined here
    image blue = Solid("#00ccff")
    image yellow = Solid("#ffff33")
    image black = Solid("#000000")
    image white = Solid("#fff")
    image grey = Solid("#cccccc")
    image greyer = Solid("#808080")
    image green = Solid("#00b300")
    image red = Solid("#ff0000")
    
    # GUI defenition
    image BattleCardUnder = "images/GUI/menu_bottom.png"
    image BattleMonsterCard = "images/GUI/BattleParchment.png"
    image BattleMonsterCardSmall = "images/GUI/BattleParchmentSmall.png"
    image TopBanner = "images/GUI/menu_top.png"
    
    # attack buttons defined here
    image BlankBlock = "images/GUI/blank move button.png"
    image BlankHover = "images/GUI/blank move button active.png"
    
    image ClubIdle = LiveComposite((50, 50), (0, 0), "BlankBlock", (0, 0), "images/GUI/bludgeon_inactive.png")
    image ClubHover = LiveComposite((50, 50), (0, 0), "BlankHover", (0, 0), "images/GUI/bludgeon_active.png")
    
    image AxeIdle = LiveComposite((50, 50), (0, 0), "BlankBlock", (0, 0), "images/GUI/axe_inactive.png")
    image AxeHover = LiveComposite((50, 50), (0, 0), "BlankHover", (0, 0), "images/GUI/axe_active.png")
    
    image BowIdle = LiveComposite((50, 50), (0, 0), "BlankBlock", (0, 0), "images/GUI/bow_inactive.png")
    image BowHover = LiveComposite((50, 50), (0, 0), "BlankHover", (0, 0), "images/GUI/bow_active.png")
    
    image ClawIdle = LiveComposite((50, 50), (0, 0), "BlankBlock", (0, 0), "images/GUI/claw_inactive.png")
    image ClawHover = LiveComposite((50, 50), (0, 0), "BlankHover", (0, 0), "images/GUI/claw_active.png")
    
    image KnifeIdle = LiveComposite((50, 50), (0, 0), "BlankBlock", (0, 0), "images/GUI/knife_inactive.png")
    image KnifeHover = LiveComposite((50, 50), (0, 0), "BlankHover", (0, 0), "images/GUI/knife_active.png")
    


    # generic buttons defined here
    image ZoomOutIdle = "images/GUI/zoom_out.png"
    image ZoomOutHover:
        "ZoomOutIdle"
        alpha 0.8
    image ZoomOutAlpha:
        "ZoomInIdle"
        alpha 0.6
    image ZoomInIdle = "images/GUI/zoom_in.png"
    image ZoomInHover:
        "ZoomInIdle"
        alpha 0.8
    image ZoomInAlpha:
        "ZoomInIdle"
        alpha 0.6
    image FinishDeploymentIdle = "images/GUI/deployment.png"
    image FinishDeploymentAlpha:
        "FinishDeploymentIdle"
        alpha 0.6
    image FinishDeploymentHover = "images/GUI/deployment_active.png"
    image NextTurnIdle = "images/GUI/hourglass.png"
    image NextTurnHover = "images/GUI/hourglasshover.png"
    image CancelMoveIdle:
        "images/GUI/X.png"
        alpha 0.5
    image CancelMoveHover:
        "images/GUI/X.png"
    image DeploymentIdle:
        "YellowTile"
        alpha 0.5
    image DeploymentHover:
        "YellowTile"
        alpha 0.8
    image MoveIdle:
        "BlueTile"
        alpha 0.5
    image MoveHover:
        "BlueTile"
        alpha 0.8
    image RangeTile:
        "RedTile"
        alpha 0.25
    image TargetIdle:
        "images/GUI/TargetIdle.png"
        alpha 0.7
    image TargetHover:
        "images/GUI/TargetHover.png"
        alpha 0.7
        
    
    # Tiles images defined here
    image Null = LiveComposite((50, 50), (0, 0), "white")
    image Clear:
        "Null"
        alpha 0.0
    image YellowTile = LiveComposite((50, 50), (0, 0), "yellow")
    image BlueTile = LiveComposite((50, 50), (0, 0), "blue")
    image RedTile = LiveComposite((50, 50), (0, 0), "red")


    

init 1 python:
    # used to ensure smooth movement
    MoveTick = False
    
    # used to determine the level of zoom applied to the battle map and resize the viewport accordingly
    zoomlist = [[x0p2, 0.2], [x0p4, 0.4], [x0p6, 0.6], [x0p8, 0.8], [x1, 1], [x1p2, 1.2], [x1p4, 1.4], [x1p6, 1.6], [x1p8, 1.8], [x2, 2]]
    
    def FindPos(x, ZoomLevel):
        temp1 = int(50*ZoomLevel)
        temp2 = temp1*x
        return temp2
        
                    
                
    # one instantiated for each type of tile that exists in the game.        
    class tile(object):
        def __init__(self, Name, PassN=True, PassE=True, PassS=True, PassW=True, VisibleN=True, VisibleE=True, VisibleS=True, VisibleW=True, MoveRequired=1, Void=False, VoidSight=False):
            # Type of tile, string
            self.Name = Name
            # can you move north from this tile (Boolean)
            self.PassN = PassN
            # can you move east from this tile (Boolean)
            self.PassE = PassE
            # can you move south from this tile (Boolean)
            self.PassS = PassS
            # can you move west from this tile (Boolean)
            self.PassW = PassW
            # can you see north from this tile (RANGED ATTACKS) (Boolean)
            self.VisibleN = VisibleN
            # can you see east from this tile (RANGED ATTACKS) (Boolean)
            self.VisibleE = VisibleE
            # can you see south from this tile (RANGED ATTACKS) (Boolean)
            self.VisibleS = VisibleS
            # can you see west from this tile (RANGED ATTACKS) (Boolean)
            self.VisibleW = VisibleW
            # how many move points moving onto this tile will take
            self.MoveRequired = MoveRequired
            # used for absolute edges
            self.Void = Void
            self.VoidSight = VoidSight
            # used with special tiles
            self.Special = False

            
    
    # One instance created for each tile on the battlefield, keeps track of who is where.
    class battletile(object):
        def __init__(self, Visibility, XPos=0, YPos=0, UnitPresent="Null", UnitIdle="None", UnitHover="None", UnitID="None", RangeOverlay="None"):
            self.Name = str(self)
            # name of unit present on this tile. If none defaults to Null
            self.UnitPresent = UnitPresent
            # Float between 1 and 0, relative screen position. Needs an algorithim to calculate.
            self.XPos = XPos
            # Float between 1 and 0, relative screen position. Needs an algorithim to calculate.
            self.YPos = YPos
            # Float between 1 and 0 setting images alpha
            self.Visibility = Visibility
            # used for deployment and selection imagebuttons
            self.UnitIdle = UnitIdle
            # same as above
            self.UnitHover = UnitHover
            # used to replace the unit into the player deployment list
            self.UnitID = UnitID
            # how many routes are available to this tile
            self.RouteStore = []
            # used to work out if direct fire can hit the tile behind this one
            self.FireNorth = True
            self.FireEast = True
            self.FireSouth = True
            self.FireWest = True
            # used to give a ranged overlay
            self.RangeOverlay = RangeOverlay
            self.RangeCheck = False
            self.CheckAround = False
            self.CheckDelay = False
            
            
    # One instantiated for each battle. Keeps all the 2d and 3d list arrays that make up the battlefield plus information about deployment zones.
    # can handle up to 4 armies but easily accomodate more with a few added lines. I figure up to 4 armies is enough for now.
    class battlefield(object):
        def __init__(self, Field, FieldOverlay, FieldID, PlayerDeployment, PlayerArmy, Enemy1Deployment, Enemy1Army, Enemy2=False, Enemy2Deployment=[], Enemy2Army=[], Enemy3=False, Enemy3Deployment=[], Enemy3Army=[]):
            # self
            self.Self = self
            # 2d list
            self.Field = Field
            # 2d list
            self.FieldOverlay = FieldOverlay
            # integer
            self.FieldID = FieldID
            # 2d list
            self.PlayerDeployment = PlayerDeployment
            # list
            self.PlayerArmy = PlayerArmy
            # 2d list
            self.Enemy1Deployment = Enemy1Deployment
            # list
            self.Enemy1Army = Enemy1Army
            # Boolean
            self.Enemy2 = Enemy2
            # 2d list
            self.Enemy2Deployment = Enemy2Deployment
            # list
            self.Enemy2Army = Enemy2Army
            # boolean
            self.Enemy3 = Enemy2
            # 2d list
            self.Enemy3Deployment = Enemy3Deployment
            # list
            self.Enemy3Army = Enemy3Army
            
            
    # One instantiated for every individual unit involved in each battle. Keeps track of stats without messing with the classes instantiated for breeding purposes. 
    # Monster stats for each chosen to participate passed into this class, used as needed and then discareded at the end of the battle. Any stat increases or bonuses passed back to the breeding class at the end.
    class unit(object):
        def __init__(self, Ferocity, Finesse, Determination, Cunning,  BattleName, OrigionalName, BattleSkills, Traits, MovementMax, BattleSpriteIdle, BattleSpriteHover, BattleSpriteMove, Mugshot, Gender, ArmyID, PAB=0, CAB=0, PRB=0, CRB=0):
            # used to append self to lists
            self.Self = self
            # string used to reference self
            self.BattleName = BattleName
            # used to help transition stat changes back to origional seeding monster in the breeding engine
            self.OrigionalName = OrigionalName
            # integer, used to gaugue army power level. Some sort of sum based on four basic stats
            self.PowerLevel = Cunning+Finesse+Ferocity+Determination
            # list.
            self.BattleSkills = BattleSkills
            # list
            self.Traits = Traits
            # integer
            self.MovementMax = MovementMax
            # integer
            self.MovementCurrent = MovementMax
            # string
            self.BattleSpriteIdle = BattleSpriteIdle
            # string
            self.BattleSpriteHover = BattleSpriteHover
            # string
            self.BattleSpriteMove = BattleSpriteMove
            # string
            self.Mugshot = Mugshot
            # integer
            self.ArmyID = ArmyID
            # Stands for physical attack bonus, integer
            self.PAB = PAB
            # Stands for charm attack bonus, integer
            self.CAB = PAB
            # stats
            self.Ferocity = Ferocity
            self.Finesse = Finesse
            self.Determination = Determination
            self.Cunning = Cunning
            self.Agression = Ferocity+Finesse
            self.Seduction = Finesse+Cunning
            self.CurrentMorale = Determination*4+Ferocity*2
            self.BufferMorale = 0
            self.MaxMorale = Determination*4+Ferocity*2
            self.Power = Cunning/2
            # integer, used to offset physical damage
            self.PhysicalResist = getPresist(Finesse, Cunning)
            # integer. stands for physical resist bonus, multiplier bonus applied to Physical resist
            self.PRB = PRB
            # integer. offests charm damage
            self.CharmResist = getCresist(Cunning, Determination)
            # integer, stands for charm resist bonus. bonus Applied to Charm resistance 
            self.CRB = CRB
            # toggle to kill monster
            self.Routed = False
            # has the unit attacked
            self.Action = True
            # Gender
            self.Gender = Gender
            # flinch
            self.PFlinch = GetPFlinch(ArmyID, Mugshot)
            
    def GetPFlinch(ArmyID, Mugshot):
        return_flinch = "None"
        if (Mugshot == "MWolfMug"):
            if (ArmyID == 1):
                return_flinch = im.Flip("images/BattleSprites/MWolf/Attack/MWClaw1.png", horizontal=True)
            else:
                return_flinch = "images/BattleSprites/MWolf/Attack/MWClaw1.png"
        elif (Mugshot == "FWolfMug"):
            if (ArmyID == 1):
                return_flinch = im.Flip("images/BattleSprites/FWolf/Attack/FWClaw10.png", horizontal=True)
            else:
                return_flinch = "images/BattleSprites/FWolf/Attack/FWClaw10.png"
        elif (Mugshot == "MCMug"):
            if (ArmyID == 1):
                return_flinch = im.Flip("images/BattleSprites/MC/Attack/MCAxe9.png", horizontal=True)
        elif (Mugshot == "BanditArcherMug"):
            if (ArmyID == 1):
                return_flinch = "images/BattleSprites/BanditArcher/Attack/BanditArcherBow13.png"
            else:
                return_flinch = im.Flip("images/BattleSprites/BanditArcher/Attack/BanditArcherBow13.png", horizontal=True)
        elif (Mugshot == "ThugMug"):
            if (ArmyID == 1):
                return_flinch = "images/BattleSprites/BanditThug/Attack/ThugKnife10.png"
            else:
                return_flinch = im.Flip("images/BattleSprites/BanditThug/Attack/ThugKnife10.png", horizontal=True)
        elif (Mugshot == "BruiserMug"):
            if (ArmyID == 1):
                return_flinch = "images/BattleSprites/BanditBruiser/Attack/BruiserClub1.png"
            else:
                return_flinch = im.Flip("images/BattleSprites/BanditBruiser/Attack/BruiserClub1.png", horizontal=True)
        return return_flinch
                
    def getPresist(Finesse, Cunning):
        temp1 = Finesse+Cunning
        return temp1
    def getCresist(Cunning, Determination):
        temp1 = Determination+Cunning
        return temp1
            
    # every type of attack needs an instance of this
    class weapon(object):
        def __init__(self, Name, Range, Damage, DamageType, Attacks, Cooldown, Idle, Hover, Animation, Bonuses=[], IndirectFire=False):
            # string, used to append self to lists
            self.Name = Name
            # integer, distance in tiles not including own
            self.Range = Range
            # integer, base damage before moster stats and multipliers are applied
            self.Damage = Damage
            # string, charm physical etc.
            self.DamageType = DamageType
            # integer,number of hits per attack. used to create multi hit attacks
            self.Attacks = Attacks
            # integer
            self.Cooldown = Cooldown
            # 2d list, traits species etc that this weapon has a bonus agaisnt [[trait, bonus in percent], [monster, bonus in percent]]
            self.Bonuses = Bonuses
            # determines type of targeting used
            self.IndirectFire = IndirectFire
            # button idle image
            self.WeaponIdle = Idle
            # button hover image
            self.WeaponHover = Hover
            # Animation, needs to be unit specific
            self.Animation = Animation
            
    
    # various battle engine only variables here
    
    # if a battlefield is created, it muct be appended to this
    BattleFieldList = []
    # used to identify which battlefield we will be using
    CurrentBattlefieldID = 0
    # boolean to switch between deployment and battle mode
    DeploymentPhase = True
    # what the battle viewport draws on. Is changed to whatever 2d battlefield array we are using for this battle
    CurrentMap = []
    # used for movement and attack buttons, same basis as CurrentMap
    CurrentOverlay = []
    # Players deployment area, same basis as CurrentMap
    CurrentPlayerDeployment = []
    # enemy 1's deployment area, same basis as CurrentMap
    CurrentEnemy1Deployment = []
    # enemy 2's deployment area (if used), same basis as CurrentMap
    CurrentEnemy2Deployment = []
    # enemy 3's deployment area (if used), same basis as CurrentMap
    CurrentEnemy3Deployment = []
    
    PlayerArmy = "None"
    Enemy1Army = "None"


    DeploymentStart = False
    ActiveDeployment = []
    CompletedDeployment = []
    PlaceUnit = False
    UnitPlaced = False
    TempIndecesX = 0
    TempIndecesY = 0
    DeploymentRandomiser = 0
    SelectedBattleSkills = []
    SelectedAttack = []
    ReturnBattleInfo = "None"
    Turn = 1
    
    
    
    # define weapons here (self, Name, Range, Damage, DamageType, Attacks, Cooldown, Idle, Hover, Bonuses=[], IndirectFire=False)
    # weapons prefixed with E_ will face left(enemy unit), no prefix faces right(Player unit)
    E_ThugKnife = weapon("Knife", 1, 4, "Physical", 1, 1, "KnifeIdle", "KnifeHover", "E_ThugKnife")
    E_BruiserClub = weapon("Club", 1, 5, "Physical", 1, 1, "ClubIdle", "ClubHover", "E_BruiserClub")
    E_BanditArcherBow = weapon("Bow", 5, 3, "Physical", 1, 1, "BowIdle", "BowHover", "E_BanditArcherBow")
    ThugKnife = weapon("Knife", 1, 4, "Physical", 1, 1, "KnifeIdle", "KnifeHover", "ThugKnife")
    BruiserClub = weapon("Club", 1, 5, "Physical", 1, 1, "ClubIdle", "ClubHover", "BruiserClub")
    BanditArcherBow = weapon("Bow", 5, 3, "Physical", 1, 1, "BowIdle", "BowHover", "BanditArcherBow")
    MCAxe = weapon("Axe", 1, 60, "Physical", 1, 1, "AxeIdle", "AxeHover", "MCAxe")
    E_FWolfClaw = weapon("Wolf Claw", 1, 8, "Physical", 1, 1, "ClawIdle", "ClawHover", "E_FWClaw")
    FWolfClaw = weapon("Wolf Claw", 1, 60, "Physical", 1, 1, "ClawIdle", "ClawHover", "FWClaw")
    E_MWolfClaw = weapon("Wolf Claw", 1, 8, "Physical", 1, 1, "ClawIdle", "ClawHover", "E_MWClaw")
    MWolfClaw = weapon("Wolf Claw", 1, 60, "Physical", 1, 1, "ClawIdle", "ClawHover", "MWClaw")
    
    
    #(self, Ferocity, Finesse, Determination, Cunning,  BattleName, OrigionalName, BattleSkills, Traits, MovementMax, BattleSpriteIdle, BattleSpriteHover, BattleSpriteMove, Mugshot, Gender, ArmyID, PAB=0, CAB=0, PRB=0, CRB=0):
    # these are only used for template style reference
    # FWolf = unit(5, 5, 5, 5, "PlaceHolder", "Soldier", [Stab], [], 4, "SoldierIdle", "SoldierHover", "SoldierMove", "Placeholder", "Female", 2)
    # Bruiser = unit(5, 5, 5, 5, "PlaceHolder", "Bruiser", [Club], [], 4, "BruiserIdle", "BruiserHover", "BruiserMove", "Placeholder", "Male", 2)
    
    
    class Army(object):
        def __init__(self, ArmyList, DeployList):
            self.Army = ArmyList
            self.DeployArmy = DeployList
    
    def ReturnArmies():
        return []
    
    ActiveAIArmies = ReturnArmies()
    


    
    
    
    
label CombatEngine:
    default testarmy = []
    python:
        # sets up player army. Works for a fixed army, but will need some sort of selection screen and drawing stats from breeding classes.
        p1 = unit(5, 5, 5, 5, "p1", "Claw Wolf", [MWolfClaw], [], 4, "MWolfIdle", "MWolfHover", "MWolfMove", "MWolfMug", "Male", 1)
        p2 = unit(5, 5, 5, 5, "p2", "Claw Wolf", [FWolfClaw], [], 4, "FWolfIdle", "FWolfHover", "FWolfMove", "FWolfMug", "Female", 1)
        p3 = unit(5, 5, 5, 5, "p3", "Player", [MCAxe], [], 4, "MCIdle", "MCHover", "MCMove", "MCMug", "Male", 1)
        PlayerArmy = Army([p1, p2, p3], [p1, p2, p3])
        # sets up enely 1's army. Will need a generator for random events and scripted ones some sort of selection method
        testarmy = EnemyArmyGenerator("Bandits", 3, 4)
        Enemy1Army = Army(testarmy, testarmy)
        ActiveAIArmies.append(Enemy1Army)
        # completeddeployment keeps track of which units have been deployed, used for all armies in turn and reset after use
        CompletedDeployment = []
        # Instantiation of battlefield.  Will need a generator for random events and scripted ones some sort of selection method
        ###Laird updated this to use the functions
        GrassFieldMap= battlefield(grassField(), grassFieldOverlay(), 0, GrassFieldPlayerDeploy, PlayerArmy.Army, GrassFieldEnemy1Deploy, Enemy1Army.Army)
        
        
        
        # any battlefield instance needs to be stored here
        ###Laird cleaned the BattleFieldList
        BattleFieldList= []
        BattleFieldList.append(UnderlayGenerator(15, 15, "grass", [SpecialFeature(grassStone)], 6, [SpecialFeature([[grassHBkade, grassHBkade, grass, grassHBkade,grassHBkade], [grassVBkade, grass, grass, grass, grassVBkade], [grass, grass, grassCampfire, grass, grass], [grassVBkade, grass, grass, grass, grassVBkade], [grassHBkade, grassHBkade, grass, grassHBkade,grassHBkade]], SpecificPlacing=True, SpecificX=7, SpecificY=7, MultiPart=True)]))
        BattleFieldList.append(UnderlayGenerator(15, 15, "light forest", [SpecialFeature(grassStone)], 6, [SpecialFeature([[grassHBkade, grassHBkade, grass, grassHBkade,grassHBkade], [grassVBkade, grass, grass, grass, grassVBkade], [grass, grass, grassCampfire, grass, grass], [grassVBkade, grass, grass, grass, grassVBkade], [grassHBkade, grassHBkade, grass, grassHBkade,grassHBkade]], SpecificPlacing=True, SpecificX=7, SpecificY=7, MultiPart=True)]))
        BattleFieldList.append(UnderlayGenerator(15, 15, "forest", [SpecialFeature(grassStone)], 6, [SpecialFeature([[grassHBkade, grassHBkade, grass, grassHBkade,grassHBkade], [grassVBkade, grass, grass, grass, grassVBkade], [grass, grass, grassCampfire, grass, grass], [grassVBkade, grass, grass, grass, grassVBkade], [grassHBkade, grassHBkade, grass, grassHBkade,grassHBkade]], SpecificPlacing=True, SpecificX=7, SpecificY=7, MultiPart=True)]))
        BattleFieldList.append(UnderlayGenerator(15, 15, "heavy forest", [SpecialFeature(grassStone)], 6, [SpecialFeature([[grassHBkade, grassHBkade, grass, grassHBkade,grassHBkade], [grassVBkade, grass, grass, grass, grassVBkade], [grass, grass, grassCampfire, grass, grass], [grassVBkade, grass, grass, grass, grassVBkade], [grassHBkade, grassHBkade, grass, grassHBkade,grassHBkade]], SpecificPlacing=True, SpecificX=7, SpecificY=7, MultiPart=True)]))
        
        
        
        # Set to extrapolate needed info from BattleFieldList. All that should be needed to set up "current" variables
    menu:
        "Pick your battlefield type"
        
        "Grassland":
            $ CurrentBattlefieldID = 0
        "Light forest":
            $ CurrentBattlefieldID = 1
        "Forest":
            $ CurrentBattlefieldID = 2
        "Dense forest":
            $ CurrentBattlefieldID = 3
        
        
        
    python:
        BE_ACTIVE = True # Global variable so we know if BE sequence is still running.
        CurrentMap = BattleFieldList[CurrentBattlefieldID]
        CurrentOverlay = OverlayGenerator(CurrentMap)
        CurrentPlayerDeployment = DeployGenerator(CurrentMap, 4, 4, 3, 3)
        CurrentEnemy1Deployment = DeployGenerator(CurrentMap, 7, 7, 5, 5)
        
        
        
        
        # Sets the players deployment zone up on the overlay map
        for i in range(0, len(CurrentPlayerDeployment)):
            TempIndecesY = CurrentPlayerDeployment[i][0]
            TempIndecesX = CurrentPlayerDeployment[i][1]
            CurrentOverlay[TempIndecesY][TempIndecesX].UnitPresent = "Deploy"
        # getPlayerMonsters()
    jump SetPos
    
label SetPos:
    python:
        for y in range(0, len(CurrentOverlay)):
            for x in range(0, len(CurrentOverlay[y])):
                CurrentOverlay[y][x].XPos = FindPos(x, zoomlist[MapZoom][1])
                CurrentOverlay[y][x].YPos = FindPos(y, zoomlist[MapZoom][1])
        DeploymentStart = True
        
    jump RenderMap
    
label finished_be:
    $ renpy.call_screen("VictoryScreen", BE_ACTIVE)
    $ ClearEverything()
    $ BE_ACTIVE = False # Could be moved to ClearEverything...
    return # Should be back to the game!
    
label RenderMap:
    
    $ CheckWin()
    
    if UnitPlaced == True:
        $ ActiveDeployment = []
        $ UnitPlaced = False
        $ PlaceUnit = False
    if AddZoom == 1:
        python:
            MapZoom += 1
            AddZoom = 0
            for y in range(0, len(CurrentOverlay)):
                for x in range(0, len(CurrentOverlay[y])):
                    CurrentOverlay[y][x].XPos = FindPos(x, zoomlist[MapZoom][1])
                    CurrentOverlay[y][x].YPos = FindPos(y, zoomlist[MapZoom][1])
    if MinusZoom == 1:
        python:
            MapZoom -= 1
            MinusZoom = 0
            for y in range(0, len(CurrentOverlay)):
                for x in range(0, len(CurrentOverlay[y])):
                    CurrentOverlay[y][x].XPos = FindPos(x, zoomlist[MapZoom][1])
                    CurrentOverlay[y][x].YPos = FindPos(y, zoomlist[MapZoom][1])
    if AtoB == True:
        python:
            ExecuteMovement()
    show screen CurrentMap
    if AITurn == True:
        return
    else:
        call screen ZoomScreen
    ###Laird Removed looping call
    
    
    
label NextTurn:
    default randomtest = 0
    python:
        Turn += 1
        randomtest = len(PlayerArmy.Army)
        
        # The range is meaningless here:
        # for x in range(0, len(PlayerArmy.Army)):
            # PlayerArmy.Army[x].MovementCurrent = PlayerArmy.Army[x].MovementMax
            # PlayerArmy.Army[x].Action = True
            
        for actor in PlayerArmy.Army:
            actor.MovementCurrent = actor.MovementMax
            actor.Action = True
            
    #"[randomtest] and [PlayerArmy.Army]"
    #"Movement current 0 = [PlayerArmy.Army[0].MovementCurrent] / Movement current 1 = [PlayerArmy.Army[1].MovementCurrent] / Movement current 2 = [PlayerArmy.Army[2].MovementCurrent]"
    call ResetMoveVariables
    jump AITurn
    
label showpath:
    "[FinalPath[0].WayPoints] / startx [StartX] starty [StartY] / finishx [FinalDestinationX] finishy [FinalDestinationY]"
    " targetx[AITarget.Xpos] targety [AITarget.Ypos] / tagetx distance [AITarget.XDistance] tagety distance [AITarget.YDistance] / Total distance [AITarget.TotalDistance]"
    return
    
    
label AITurn:
    default AIAction = "None"
    default AITurn = False
    default AITarget = "None"
    $ AITurn = True
    python:
        for army in range(0, len(ActiveAIArmies)):
            for x in range(0, len(ActiveAIArmies[army].Army)):
                if ActiveAIArmies[army].Army[x].Routed == False:
                    AIAction = AIDecideAction(ActiveAIArmies[army].Army[x], CurrentOverlay)
                    if AIAction == "Move":
                        AIMoveAction()
                    elif AIAction == "Attack":
                        AIAttackAction(ActiveAIArmies[army].Army[x])
                    elif AIAction == "Move Attack":
                        AIMoveAction()
                        AIAttackAction(ActiveAIArmies[army].Army[x])
                    elif AIAction == "Idle":
                        pass
                    ResetMoveVariables()
                    CheckWin()
                    
    call ResetAI from _call_ResetAI
    jump RenderMap
    
label ResetAI:
    python:
        AIAction = "None"
        AITurn = False
        for army in range(0, len(ActiveAIArmies)):
            for x in range(0, len(ActiveAIArmies[army].Army)):
                if ActiveAIArmies[army].Army[x].Routed == False:
                    ActiveAIArmies[army].Army[x].MovementCurrent = ActiveAIArmies[army].Army[x].MovementMax
                    ActiveAIArmies[army].Army[x].Action = True
    return
    


screen VictoryScreen(Condition):
    
    add Solid("#FFF") # Se we have a background...
    
    add "images/GUI/VictoryScreen/victor_background.png" xpos 0 ypos 0
    if Condition == "Win":
        add "images/GUI/VictoryScreen/victor_winner.png" xpos 550 ypos 100
    elif Condition == "Draw":
        add "images/GUI/VictoryScreen/victor_tie.png" xpos 550 ypos 100
    elif Condition == "Lose":
        add "images/GUI/VictoryScreen/victor_loser.png" xpos 550 ypos 100
        
    add "images/GUI/VictoryScreen/victor_gold.png" xpos 600 ypos 520
    text "[ReturnBattleInfo.Gold]" xpos 710 ypos 520
    
    add "images/GUI/VictoryScreen/victor_fame.png" xpos 600 ypos 580
    text "[ReturnBattleInfo.Fame]" xpos 710 ypos 580

    add "images/GUI/VictoryScreen/victor_exp.png" xpos 600 ypos 640
    text "[ReturnBattleInfo.EXP]" xpos 710 ypos 640
    
    add "images/GUI/VictoryScreen/victor_turns.png" xpos 800 ypos 520
    text "[ReturnBattleInfo.Turn]" xpos 980 ypos 520

    add "images/GUI/VictoryScreen/victor_kills.png" xpos 800 ypos 580
    text "[ReturnBattleInfo.Kills]" xpos 980 ypos 580
    
    add "images/GUI/VictoryScreen/victor_unitsused.png" xpos 800 ypos 640
    text "[ReturnBattleInfo.UnitsUsed]" xpos 980 ypos 640
    
    add "images/GUI/VictoryScreen/victor_lost.png" xpos 800 ypos 700
    text "[ReturnBattleInfo.UnitsRouted]" xpos 980 ypos 700
    
    add "images/GUI/VictoryScreen/victor_sides.png" xpos 800 ypos 760
    text "[ReturnBattleInfo.SideQuests]" xpos 980 ypos 760
    
    imagebutton idle "images/GUI/VictoryScreen/victor_return_idle.png" hover "images/GUI/VictoryScreen/victor_return_hover.png" xpos 520 ypos 770 action Return()
    
    
    
    
    
    
    
    
    
    