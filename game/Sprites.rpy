init:
    # Battle sprites defined here
    
    image MWolfIdle:
        "images/BattleSprites/MWolf/Walk/MwolfFrontIdle.png"
        zoom 0.5
    image MWolfHover:
        "MWolfIdle"
        alpha 0.7
    image MWolfMoveS:
        zoom 0.5
        "images/BattleSprites/MWolf/Walk/MwolfFrontIdle.png"
        pause 0.5
        "images/BattleSprites/MWolf/Walk/MwolfFront1.png"
        pause 0.5
        "images/BattleSprites/MWolf/Walk/MwolfFrontIdle.png"
        pause 0.5
        "images/BattleSprites/MWolf/Walk/MwolfFront2.png"
        pause 0.5
        repeat
    image MWolfMoveN:
        zoom 0.5
        "images/BattleSprites/MWolf/Walk/MwolfBackIdle.png"
        pause 0.5
        "images/BattleSprites/MWolf/Walk/MwolfBack1.png"
        pause 0.5
        "images/BattleSprites/MWolf/Walk/MwolfBackIdle.png"
        pause 0.5
        "images/BattleSprites/MWolf/Walk/MwolfBack2.png"
        pause 0.5
        repeat
    image MWolfMoveE:
        zoom 0.5
        "images/BattleSprites/MWolf/Walk/MwolfRightIdle.png"
        pause 0.5
        "images/BattleSprites/MWolf/Walk/MwolfRight1.png"
        pause 0.5
        "images/BattleSprites/MWolf/Walk/MwolfRightIdle.png"
        pause 0.5
        "images/BattleSprites/MWolf/Walk/MwolfRight2.png"
        pause 0.5
        repeat
    image MWolfMoveW:
        zoom 0.5
        "images/BattleSprites/MWolf/Walk/MwolfLeftIdle.png"
        pause 0.5
        "images/BattleSprites/MWolf/Walk/MwolfLeft1.png"
        pause 0.5
        "images/BattleSprites/MWolf/Walk/MwolfLeftIdle.png"
        pause 0.5
        "images/BattleSprites/MWolf/Walk/MwolfLeft2.png"
        pause 0.5
        repeat
    image MWolfMove = ConditionSwitch("CurrentFacing == 'N'", "MWolfMoveN", "CurrentFacing == 'E'", "MWolfMoveE", "CurrentFacing == 'S'", "MWolfMoveS", "CurrentFacing == 'W'", "MWolfMoveW")
    
    image FWolfIdle:
        "images/BattleSprites/FWolf/Walk/FwolfFrontIdle.png"
        zoom 0.5
    image FWolfHover:
        "FWolfIdle"
        alpha 0.7
    image FWolfMoveS:
        zoom 0.5
        "images/BattleSprites/FWolf/Walk/FwolfFrontIdle.png"
        pause 0.5
        "images/BattleSprites/FWolf/Walk/FwolfFront1.png"
        pause 0.5
        "images/BattleSprites/FWolf/Walk/FwolfFrontIdle.png"
        pause 0.5
        "images/BattleSprites/FWolf/Walk/FwolfFront2.png"
        pause 0.5
        repeat
    image FWolfMoveN:
        zoom 0.5
        "images/BattleSprites/FWolf/Walk/FwolfBackIdle.png"
        pause 0.5
        "images/BattleSprites/FWolf/Walk/FwolfBack1.png"
        pause 0.5
        "images/BattleSprites/FWolf/Walk/FwolfBackIdle.png"
        pause 0.5
        "images/BattleSprites/FWolf/Walk/FwolfBack2.png"
        pause 0.5
        repeat
    image FWolfMoveE:
        zoom 0.5
        "images/BattleSprites/FWolf/Walk/FwolfRightIdle.png"
        pause 0.5
        "images/BattleSprites/FWolf/Walk/FwolfRight1.png"
        pause 0.5
        "images/BattleSprites/FWolf/Walk/FwolfRightIdle.png"
        pause 0.5
        "images/BattleSprites/FWolf/Walk/FwolfRight2.png"
        pause 0.5
        repeat
    image FWolfMoveW:
        zoom 0.5
        "images/BattleSprites/FWolf/Walk/FwolfLeftIdle.png"
        pause 0.5
        "images/BattleSprites/FWolf/Walk/FwolfLeft1.png"
        pause 0.5
        "images/BattleSprites/FWolf/Walk/FwolfLeftIdle.png"
        pause 0.5
        "images/BattleSprites/FWolf/Walk/FwolfLeft2.png"
        pause 0.5
        repeat
    image FWolfMove = ConditionSwitch("CurrentFacing == 'N'", "FWolfMoveN", "CurrentFacing == 'E'", "FWolfMoveE", "CurrentFacing == 'S'", "FWolfMoveS", "CurrentFacing == 'W'", "FWolfMoveW")
        
    
        
        
    image BruiserIdle:
        "images/BattleSprites/BanditBruiser/Walk/BanditBruiserIdle.png"
        zoom 0.5
    image BruiserHover:
        "BruiserIdle"
        alpha 0.7
    image BruiserMoveS:
        zoom 0.5
        "images/BattleSprites/BanditBruiser/Walk/BanditBruiserIdle.png"
        pause 0.5
        "images/BattleSprites/BanditBruiser/Walk/BanditBruiserFrontStep2.png"
        pause 0.5
        "images/BattleSprites/BanditBruiser/Walk/BanditBruiserIdle.png"
        pause 0.5
        "images/BattleSprites/BanditBruiser/Walk/BanditBruiserFrontStep1.png"
        pause 0.5
        repeat
    image BruiserMoveN:
        zoom 0.5
        "images/BattleSprites/BanditBruiser/Walk/BruiserBackIdle.png"
        pause 0.5
        "images/BattleSprites/BanditBruiser/Walk/BruiserBack2.png"
        pause 0.5
        "images/BattleSprites/BanditBruiser/Walk/BruiserBackIdle.png"
        pause 0.5
        "images/BattleSprites/BanditBruiser/Walk/BruiserBack1.png"
        pause 0.5
        repeat
    image BruiserMoveE:
        zoom 0.5
        "images/BattleSprites/BanditBruiser/Walk/BruiserRightIdle.png"
        pause 0.5
        "images/BattleSprites/BanditBruiser/Walk/BruiserRight2.png"
        pause 0.5
        "images/BattleSprites/BanditBruiser/Walk/BruiserRightIdle.png"
        pause 0.5
        "images/BattleSprites/BanditBruiser/Walk/BruiserRight1.png"
        pause 0.5
        repeat
    image BruiserMoveW:
        zoom 0.5
        "images/BattleSprites/BanditBruiser/Walk/BruiserLeftIdle.png"
        pause 0.5
        "images/BattleSprites/BanditBruiser/Walk/BruiserLeft2.png"
        pause 0.5
        "images/BattleSprites/BanditBruiser/Walk/BruiserLeftIdle.png"
        pause 0.5
        "images/BattleSprites/BanditBruiser/Walk/BruiserLeft1.png"
        pause 0.5
        repeat
    image BruiserMove = ConditionSwitch("CurrentFacing == 'N'", "BruiserMoveN", "CurrentFacing == 'E'", "BruiserMoveE", "CurrentFacing == 'S'", "BruiserMoveS", "CurrentFacing == 'W'", "BruiserMoveW")
    
    
    image ThugIdle:
        "images/BattleSprites/BanditThug/Walk/BanditThugIdle.png"
        zoom 0.5
    image ThugHover:
        "ThugIdle"
        alpha 0.7
    image ThugMoveS:
        zoom 0.5
        "images/BattleSprites/BanditThug/Walk/ThugIdle.png"
        pause 0.5
        "images/BattleSprites/BanditThug/Walk/ThugFront2.png"
        pause 0.5
        "images/BattleSprites/BanditThug/Walk/ThugIdle.png"
        pause 0.5
        "images/BattleSprites/BanditThug/Walk/ThugFront1.png"
        pause 0.5
        repeat
    image ThugMoveN:
        zoom 0.5
        "images/BattleSprites/BanditThug/Walk/ThugBackIdle.png"
        pause 0.5
        "images/BattleSprites/BanditThug/Walk/ThugBack2.png"
        pause 0.5
        "images/BattleSprites/BanditThug/Walk/ThugBackIdle.png"
        pause 0.5
        "images/BattleSprites/BanditThug/Walk/ThugBack1.png"
        pause 0.5
        repeat
    image ThugMoveE:
        zoom 0.5
        "images/BattleSprites/BanditThug/Walk/ThugRightIdle.png"
        pause 0.5
        "images/BattleSprites/BanditThug/Walk/ThugRight2.png"
        pause 0.5
        "images/BattleSprites/BanditThug/Walk/ThugRightIdle.png"
        pause 0.5
        "images/BattleSprites/BanditThug/Walk/ThugRight1.png"
        pause 0.5
        repeat
    image ThugMoveW:
        zoom 0.5
        "images/BattleSprites/BanditThug/Walk/ThugLeftIdle.png"
        pause 0.5
        "images/BattleSprites/BanditThug/Walk/ThugLeft2.png"
        pause 0.5
        "images/BattleSprites/BanditThug/Walk/ThugLeftIdle.png"
        pause 0.5
        "images/BattleSprites/BanditThug/Walk/ThugLeft1.png"
        pause 0.5
        repeat
    image ThugMove = ConditionSwitch("CurrentFacing == 'N'", "ThugMoveN", "CurrentFacing == 'E'", "ThugMoveE", "CurrentFacing == 'S'", "ThugMoveS", "CurrentFacing == 'W'", "ThugMoveW")
    
    image BanditArcherIdle:
        "images/BattleSprites/BanditArcher/Walk/BanditArcherIdle.png"
        zoom 0.5
    image BanditArcherHover:
        "BanditArcherIdle"
        alpha 0.7
    image BanditArcherMoveS:
        zoom 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherIdle.png"
        pause 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherFront2.png"
        pause 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherIdle.png"
        pause 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherFront1.png"
        pause 0.5
        repeat
    image BanditArcherMoveN:
        zoom 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherBackIdle.png"
        pause 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherBack2.png"
        pause 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherBackIdle.png"
        pause 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherBack1.png"
        pause 0.5
        repeat
    image BanditArcherMoveE:
        zoom 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherRightIdle.png"
        pause 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherRight2.png"
        pause 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherRightIdle.png"
        pause 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherRight1.png"
        pause 0.5
        repeat
    image BanditArcherMoveW:
        zoom 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherLeftIdle.png"
        pause 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherLeft2.png"
        pause 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherLeftIdle.png"
        pause 0.5
        "images/BattleSprites/BanditArcher/Walk/BanditArcherLeft1.png"
        pause 0.5
        repeat
    image BanditArcherMove = ConditionSwitch("CurrentFacing == 'N'", "BanditArcherMoveN", "CurrentFacing == 'E'", "BanditArcherMoveE", "CurrentFacing == 'S'", "BanditArcherMoveS", "CurrentFacing == 'W'", "BanditArcherMoveW")
    
    image MCIdle:
        "images/BattleSprites/MC/Walk/MCIdle.png"
        zoom 0.5
    image MCHover:
        "MCIdle"
        alpha 0.7
    image MCMoveS:
        zoom 0.5
        "images/BattleSprites/MC/Walk/MCIdle.png"
        pause 0.5
        "images/BattleSprites/MC/Walk/MCFront2.png"
        pause 0.5
        "images/BattleSprites/MC/Walk/MCIdle.png"
        pause 0.5
        "images/BattleSprites/MC/Walk/MCFront1.png"
        pause 0.5
        repeat
    image MCMoveN:
        zoom 0.5
        "images/BattleSprites/MC/Walk/MCBackIdle.png"
        pause 0.5
        "images/BattleSprites/MC/Walk/MCBack2.png"
        pause 0.5
        "images/BattleSprites/MC/Walk/MCBackIdle.png"
        pause 0.5
        "images/BattleSprites/MC/Walk/MCBack1.png"
        pause 0.5
        repeat
    image MCMoveE:
        zoom 0.5
        "images/BattleSprites/MC/Walk/MCRightIdle.png"
        pause 0.5
        "images/BattleSprites/MC/Walk/MCRight2.png"
        pause 0.5
        "images/BattleSprites/MC/Walk/MCRightIdle.png"
        pause 0.5
        "images/BattleSprites/MC/Walk/MCRight1.png"
        pause 0.5
        repeat
    image MCMoveW:
        zoom 0.5
        "images/BattleSprites/MC/Walk/MCLeftIdle.png"
        pause 0.5
        "images/BattleSprites/MC/Walk/MCLeft2.png"
        pause 0.5
        "images/BattleSprites/MC/Walk/MCLeftIdle.png"
        pause 0.5
        "images/BattleSprites/MC/Walk/MCLeft1.png"
        pause 0.5
        repeat
    image MCMove = ConditionSwitch("CurrentFacing == 'N'", "MCMoveN", "CurrentFacing == 'E'", "MCMoveE", "CurrentFacing == 'S'", "MCMoveS", "CurrentFacing == 'W'", "MCMoveW")
    

    # mugshots defined here
    image MaleWolfMug = "images/Mugshots/profile_wolf_male.png"
    image FemWolfMug = "images/Mugshots/profile_wolf_fem.png"