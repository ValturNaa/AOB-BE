init -1:    
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



    # Battle sprites defined here

    image SoldierIdle:
        "images/BattleSprites/SoldierFrontStepIdle.png"
        zoom 0.5
    image SoldierHover:
        "SoldierIdle"
        alpha 0.7
    image SoldierMove:
        "SoldierIdle"
        
    
    image FWolfIdle:
        "images/BattleSprites/wolf/FwolfFrontIdle.png"
        zoom 0.5
    image FWolfHover:
        "FWolfIdle"
        alpha 0.7
    image FWolfMoveS:
        zoom 0.5
        "images/BattleSprites/wolf/FwolfFrontIdle.png"
        pause 0.5
        "images/BattleSprites/wolf/FwolfFront1.png"
        pause 0.5
        "images/BattleSprites/wolf/FwolfFrontIdle.png"
        pause 0.5
        "images/BattleSprites/wolf/FwolfFront2.png"
        pause 0.5
        repeat
    image FWolfMoveN:
        zoom 0.5
        "images/BattleSprites/wolf/FwolfBackIdle.png"
        pause 0.5
        "images/BattleSprites/wolf/FwolfBack1.png"
        pause 0.5
        "images/BattleSprites/wolf/FwolfBackIdle.png"
        pause 0.5
        "images/BattleSprites/wolf/FwolfBack2.png"
        pause 0.5
        repeat
    image FWolfMoveE:
        zoom 0.5
        "images/BattleSprites/wolf/FwolfRightIdle.png"
        pause 0.5
        "images/BattleSprites/wolf/FwolfRight1.png"
        pause 0.5
        "images/BattleSprites/wolf/FwolfRightIdle.png"
        pause 0.5
        "images/BattleSprites/wolf/FwolfRight2.png"
        pause 0.5
        repeat
    image FWolfMoveW:
        zoom 0.5
        "images/BattleSprites/wolf/FwolfLeftIdle.png"
        pause 0.5
        "images/BattleSprites/wolf/FwolfLeft1.png"
        pause 0.5
        "images/BattleSprites/wolf/FwolfLeftIdle.png"
        pause 0.5
        "images/BattleSprites/wolf/FwolfLeft2.png"
        pause 0.5
        repeat
    image FWolfMove = ConditionSwitch("CurrentFacing == 'N'", "FWolfMoveN", "CurrentFacing == 'E'", "FWolfMoveE", "CurrentFacing == 'S'", "FWolfMoveS", "CurrentFacing == 'W'", "FWolfMoveW")
        
    
        
        
    image BruiserIdle:
        "images/BattleSprites/bandit/BanditBruiserIdle.png"
        zoom 0.5
    image BruiserHover:
        "BruiserIdle"
        alpha 0.7
    image BruiserMoveS:
        zoom 0.5
        "images/BattleSprites/bandit/BanditBruiserIdle.png"
        pause 0.5
        "images/BattleSprites/bandit/BanditBruiserFrontStep2.png"
        pause 0.5
        "images/BattleSprites/bandit/BanditBruiserIdle.png"
        pause 0.5
        "images/BattleSprites/bandit/BanditBruiserFrontStep1.png"
        pause 0.5
        repeat
    image BruiserMoveN:
        zoom 0.5
        "images/BattleSprites/bandit/BruiserBackIdle.png"
        pause 0.5
        "images/BattleSprites/bandit/BruiserBack2.png"
        pause 0.5
        "images/BattleSprites/bandit/BruiserBackIdle.png"
        pause 0.5
        "images/BattleSprites/bandit/BruiserBack1.png"
        pause 0.5
        repeat
    image BruiserMoveE:
        zoom 0.5
        "images/BattleSprites/bandit/BruiserRightIdle.png"
        pause 0.5
        "images/BattleSprites/bandit/BruiserRight2.png"
        pause 0.5
        "images/BattleSprites/bandit/BruiserRightIdle.png"
        pause 0.5
        "images/BattleSprites/bandit/BruiserRight1.png"
        pause 0.5
        repeat
    image BruiserMoveW:
        zoom 0.5
        "images/BattleSprites/bandit/BruiserLeftIdle.png"
        pause 0.5
        "images/BattleSprites/bandit/BruiserLeft2.png"
        pause 0.5
        "images/BattleSprites/bandit/BruiserLeftIdle.png"
        pause 0.5
        "images/BattleSprites/bandit/BruiserLeft1.png"
        pause 0.5
        repeat
    image BruiserMove = ConditionSwitch("CurrentFacing == 'N'", "BruiserMoveN", "CurrentFacing == 'E'", "BruiserMoveE", "CurrentFacing == 'S'", "BruiserMoveS", "CurrentFacing == 'W'", "BruiserMoveW")

    # mugshots defined here
    image MaleWolfMug = "images/Mugshots/profile_wolf_male.png"
    image FemWolfMug = "images/Mugshots/profile_wolf_fem.png"
    

init 1 python:
    
    
    # extra layer to apply transforms to the map
    config.layers = ['master', 'mapdisplay', 'transient', 'screens', 'overlay']
    
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
        def __init__(self, Name, PassN=True, PassE=True, PassS=True, PassW=True, VisibleN=True, VisibleE=True, VisibleS=True, VisibleW=True, MoveRequired=1, Void=False):
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
            
    def getPresist(Finesse, Cunning):
        temp1 = Finesse+Cunning
        return temp1
    def getCresist(Cunning, Determination):
        temp1 = Determination+Cunning
        return temp1
            
    # every type of attack needs an instance of this
    class weapon(object):
        def __init__(self, Name, Range, Damage, DamageType, Attacks, Cooldown, Idle, Hover, Bonuses=[], IndirectFire=False):
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
    # Used to end battle and return to farm screen
    BattleEnd = False
    
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
    
    
    
    # define weapons here (self, Name, Range, Damage, DamageType, Attacks, Cooldown, Idle, Hover, Bonuses=[], IndirectFire=False)
    Stab = weapon("Stab", 1, 8, "Physical", 1, 1, "None", "None")
    Club = weapon("Club", 1, 5, "Physical", 1, 1, "ClubIdle", "ClubHover")
    Club1 = weapon("Club", 3, 5, "Physical", 1, 1, "ClubIdle", "ClubHover")
    Club2 = weapon("Club", 5, 5, "Physical", 1, 1, "ClubIdle", "ClubHover")
    Club3 = weapon("Club", 1, 5, "Physical", 1, 1, "ClubIdle", "ClubHover", IndirectFire=True)
    Club4 = weapon("Club", 3, 5, "Physical", 1, 1, "ClubIdle", "ClubHover", IndirectFire=True)
    Club5 = weapon("Club", 5, 5, "Physical", 1, 1, "ClubIdle", "ClubHover", IndirectFire=True)
    Claw = weapon("Claw", 1, 8, "Physical", 1, 1, "ClubIdle", "ClubHover")
    
    
    
    #(self, Ferocity, Finesse, Determination, Cunning,  BattleName, OrigionalName, BattleSkills, Traits, MovementMax, BattleSpriteIdle, BattleSpriteHover, BattleSpriteMove, Mugshot, Gender, ArmyID, PAB=0, CAB=0, PRB=0, CRB=0):
    # these are only used for template style reference
    # FWolf = unit(5, 5, 5, 5, "PlaceHolder", "Soldier", [Stab], [], 4, "SoldierIdle", "SoldierHover", "SoldierMove", "Placeholder", "Female", 2)
    # Bruiser = unit(5, 5, 5, 5, "PlaceHolder", "Bruiser", [Club], [], 4, "BruiserIdle", "BruiserHover", "BruiserMove", "Placeholder", "Male", 2)
    
    config.layers = ['master', 'mapdisplay', 'transient', 'screens', 'overlay']
    
    class Army(object):
        def __init__(self, ArmyList, DeployList):
            self.Army = ArmyList
            self.DeployArmy = DeployList
    
    def ReturnArmies():
        return []
    
    ActiveAIArmies = ReturnArmies()
    


    
    
    
    
label CombatEngine:
    python:
        # sets up player army. Works for a fixed army, but will need some sort of selection screen and drawing stats from breeding classes.
        p1 = unit(5, 5, 5, 5, "p1", "Claw Wolf", [Claw], [], 4, "FWolfIdle", "FWolfHover", "FWolfMove", "MaleWolfMug", "Female", 1)
        p2 = unit(5, 5, 5, 5, "p2", "Claw Wolf", [Claw], [], 4, "FWolfIdle", "FWolfHover", "FWolfMove", "MaleWolfMug", "Female", 1)
        p3 = unit(5, 5, 5, 5, "p3", "Claw Wolf", [Claw], [], 4, "FWolfIdle", "FWolfHover", "FWolfMove", "MaleWolfMug", "Female", 1)
        PlayerArmy = Army([p1, p2, p3], [p1, p2, p3])
        # sets up enely 1's army. Will need a generator for random events and scripted ones some sort of selection method
        e1 = unit(5, 5, 5, 5, "e1", "Bruiser", [Club], [], 4, "BruiserIdle", "BruiserHover", "BruiserMove", "MaleWolfMug", "Male", 2)
        e2 = unit(5, 5, 5, 5, "e2", "Bruiser", [Club], [], 4, "BruiserIdle", "BruiserHover", "BruiserMove", "MaleWolfMug", "Male", 2)
        e3 = unit(5, 5, 5, 5, "e3", "Bruiser", [Club], [], 4, "BruiserIdle", "BruiserHover", "BruiserMove", "MaleWolfMug", "Male", 2)
        Enemy1Army = Army([e1, e2, e3], [e1, e2, e3])
        ActiveAIArmies.append(Enemy1Army)
        # completeddeployment keeps track of which units have been deployed, used for all armies in turn and reset after use
        CompletedDeployment = []
        # Instantiation of battlefield.  Will need a generator for random events and scripted ones some sort of selection method
        ###Laird updated this to use the functions
        GrassFieldMap= battlefield(grassField(), grassFieldOverlay(), 0, GrassFieldPlayerDeploy, PlayerArmy.Army, GrassFieldEnemy1Deploy, Enemy1Army.Army)
        # any battlefield instance needs to be stored here
        ###Laird cleaned the BattleFieldList
        BattleFieldList= []
        BattleFieldList.append(GrassFieldMap)
        # Set to extrapolate needed info from BattleFieldList. All that should be needed to set up "current" variables
        CurrentBattlefieldID = 0
        CurrentMap = BattleFieldList[CurrentBattlefieldID].Field
        CurrentOverlay = BattleFieldList[CurrentBattlefieldID].FieldOverlay
        CurrentPlayerDeployment = BattleFieldList[CurrentBattlefieldID].PlayerDeployment
        CurrentEnemy1Deployment = BattleFieldList[CurrentBattlefieldID].Enemy1Deployment
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
    
    
label RenderMap:
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
        randomtest = len(PlayerArmy.Army)
        for x in range(0, len(PlayerArmy.Army)):
            PlayerArmy.Army[x].MovementCurrent = PlayerArmy.Army[x].MovementMax
            PlayerArmy.Army[x].Action = True
    #"[randomtest] and [PlayerArmy.Army]"
    #"Movement current 0 = [PlayerArmy.Army[0].MovementCurrent] / Movement current 1 = [PlayerArmy.Army[1].MovementCurrent] / Movement current 2 = [PlayerArmy.Army[2].MovementCurrent]"
    call ResetMoveVariables from _call_ResetMoveVariables_1
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
                    ResetMoveVariables()
                    
                        

                        
                        
    
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


    