##MENUS
#Main Menu
screen main_menu():
    #tag
    tag menu
    #background
    add "data/menu/main/back.png"
    add "data/menu/main/fore.png"
    add "data/menu/main/menuBack.png" xpos 460 ypos 677
    #buttons
    imagebutton auto "data/menu/main/new_%s.png" xpos 540 ypos 737 focus_mask True action newGameVars, Start
    imagebutton auto "data/menu/main/load_%s.png" xpos 539 ypos 807 focus_mask True action showSave, Show("fileOp", None, False)
    imagebutton auto "data/menu/main/options_%s.png" xpos 515 ypos 877 focus_mask True action Show("options", None, False)
    imagebutton auto "data/menu/main/quit_%s.png" xpos 600 ypos 937 focus_mask True action Quit(confirm= False)

screen newGame():
    python:
        resetBreedVars()

#game menu
screen game_menu():
    modal True
    add "data/menu/main/backGame.png"
    imagebutton auto "data/menu/main/return_%s.png" xpos 520 ypos 737 action Hide("game_menu")
    imagebutton auto "data/menu/main/data_%s.png" xpos 530 ypos 807 action Hide("game_menu"), showSaveN, Show("fileOp", None, True)
    imagebutton auto "data/menu/main/options_%s.png" xpos 497 ypos 877 focus_mask True action Show("options", None, True)
    imagebutton auto "data/menu/main/quit_%s.png" xpos 584 ypos 937 focus_mask True action Hide("game_menu"), Hide("farm"), Hide("map"), Show("main_menu")
        
#Options
screen options(game):
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    modal True
    add im.Scale("data/menu/options/back.png", 1300, 1000)
    imagebutton auto "data/menu/options/return_%s.png" xpos 250 ypos 760  action Hide("options")
    if (_preferences.fullscreen):
        imagebutton auto "data/menu/options/window_%s.png" xpos 505 ypos 450  action Preference("display", "window")
    else:
        imagebutton auto "data/menu/options/fullscreen_%s.png" xpos 505 ypos 450  action Preference("display", "fullscreen")
    imagebutton auto "data/menu/options/default_%s.png" xpos 770 ypos 760 action Hide("options")
    if (gay):
        imagebutton auto "data/menu/options/gayOn_%s.png" xpos 285 ypos 605 action toggleGay
    else:
        imagebutton auto "data/menu/options/gayOff_%s.png" xpos 285 ypos 605 action toggleGay
    if (straight):
        imagebutton auto "data/menu/options/straightOn_%s.png" xpos 447 ypos 605 action toggleStraight
    else:
        imagebutton auto "data/menu/options/straightOff_%s.png" xpos 447 ypos 605 action toggleStraight
    if (lesbian):
        imagebutton auto "data/menu/options/lesbianOn_%s.png" xpos 639 ypos 605 action toggleLesbian
    else:
        imagebutton auto "data/menu/options/lesbianOff_%s.png" xpos 639 ypos 605 action toggleLesbian
    if (herms):
        imagebutton auto "data/menu/options/hermsOn_%s.png" xpos 850 ypos 605 action toggleHerms
    else:
        imagebutton auto "data/menu/options/hermsOff_%s.png" xpos 850 ypos 605 action toggleHerms
    if (anal):
        imagebutton auto "data/menu/options/analOn_%s.png" xpos 298 ypos 659 action toggleAnal
    else:
        imagebutton auto "data/menu/options/analOff_%s.png" xpos 298 ypos 659 action toggleAnal
    if (vaginal):
        imagebutton auto "data/menu/options/vaginalOn_%s.png" xpos 436 ypos 659 action toggleVaginal
    else:
        imagebutton auto "data/menu/options/vaginalOff_%s.png" xpos 436 ypos 659 action toggleVaginal
    if (oral):
        imagebutton auto "data/menu/options/oralOn_%s.png" xpos 585 ypos 659 action toggleOral
    else:
        imagebutton auto "data/menu/options/oralOff_%s.png" xpos 585 ypos 659 action toggleOral
    if (bondage):
        imagebutton auto "data/menu/options/bondageOn_%s.png" xpos 708 ypos 659 action toggleBondage
    else:
        imagebutton auto "data/menu/options/bondageOff_%s.png" xpos 708 ypos 659 action toggleBondage
    if (zoophilia):
        imagebutton auto "data/menu/options/zoophiliaOn_%s.png" xpos 883 ypos 659 action toggleZoophilia
    else:
        imagebutton auto "data/menu/options/zoophiliaOff_%s.png" xpos 883 ypos 659 action toggleZoophilia
    
#Save/ Load
screen fileOp(game):
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    modal True
    add im.Scale("data/menu/options/backSave.png", 1300, 1000)
    fixed:
        area (70, 115, 503, 720)
        vpgrid id"vpS":
            cols 1
            spacing 10
            draggable True
            mousewheel True
            for save in saveList:
                add save
        vbar value YScrollValue("vpS") xpos 1.0
    if (selectedSave!= None):
        add im.Scale(selectedSave.portrait, 200, 200) xpos 800 ypos 200
        text selectedSave.name size 30 font "SegoeBold.ttf" color(0,0,0) xanchor 0.5 xpos 900 ypos 160
        text selectedSave.date size 20 font "SegoeBold.ttf" color(0,0,0) xanchor 0.5 xpos 765 ypos 420
        text selectedSave.money size 20 font "SegoeBold.ttf" color(0,0,0) xanchor 0.5 xpos 1060 ypos 420
        text selectedSave.chapter size 20 font "SegoeBold.ttf" color(0,0,0) xpos 900 ypos 500
        text selectedSave.region size 20 font "SegoeBold.ttf" color(0,0,0) xpos 900 ypos 530
        text selectedSave.mission size 20 font "SegoeBold.ttf" color(0,0,0) xpos 900 ypos 560
        fixed:
            area (670, 450, 182, 385)
            vpgrid id"vp":
                cols 1
                spacing 10
                draggable True
                mousewheel True
                for monster in selectedSave.knownMonsters:
                    text monster size 25 font "SegoeBold.ttf" color(0,0,0)
            vbar value YScrollValue("vp") xpos 1.0
    if (game):
        imagebutton auto "data/menu/options/save_%s.png" xpos 145 ypos 870  action saveGameTest
    imagebutton auto "data/menu/options/saveReturn_%s.png" xanchor 0.5 xpos 1060 ypos 870  action Hide("fileOp"), clearSelection
    imagebutton auto "data/menu/options/load_%s.png" xpos 400 ypos 870  action Hide("fileOp"), loadGameTest
  
##LOCATIONS        
        
#Map
screen map:
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    modal True
    #background
    add im.Scale("data/menu/map/back.png", 1300, 1000)
    #buttons
    imagebutton auto "data/menu/map/menu_%s.png" xpos 132 ypos 900 action Show("game_menu")
    imagebutton auto "data/menu/map/back_%s.png" xpos 535 ypos 895 action Hide("map")
    imagebutton auto "data/menu/map/farm_%s.png" xpos 915 ypos 900 focus_mask True action Hide("map"), Hide("farm"), Hide("combat"), Show("farm")
    
#Farm
screen farm():
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    #background
    add im.Scale("data/menu/farm/back.png", 1300, 1000)
    #buttons
    imagebutton auto "data/menu/farm/map_%s.png" xpos 0 ypos 0 focus_mask True action Show("map")
    imagebutton auto "data/menu/farm/viewer_%s.png" xpos 840 ypos 360 focus_mask True action Hide("farm"), clearBreedMonsters, showViewer, Show("barn")
    imagebutton auto "data/menu/farm/house_%s.png" xpos 1060 ypos 610 focus_mask True action advanceDayLaird
    imagebutton auto "data/menu/farm/request_%s.png" xpos 460 ypos 420 focus_mask True action Hide("farm"), clearBreedMonsters, showRequest, Show("request")
    imagebutton auto "data/menu/farm/combat_%s.png" xpos 90 ypos 520 focus_mask True action Hide("farm"), clearBreedMonsters, showCombat, Show("combat")
    imagebutton auto "data/menu/farm/breed_%s.png" xpos 710 ypos 590 focus_mask True action Hide("farm"), clearBreedMonsters, showBreed, Show("breed")
    add "data/menu/farm/tree.png"
    imagebutton auto "data/menu/farm/menu_%s.png" xpos 0 ypos 0 focus_mask True action Show("game_menu")
    #info
    add clock xpos 525
    text ("Money: "+ str(gameMoney)+ "G") size 25 font "SegoeBold.ttf" color (250,250,50) xpos (650- len(str("Money: "+ str(gameMoney)+ "G")* 20)/ 2) ypos 150
  
#monster info
screen details():
    modal True
    add "data/menu/viewer/detailBack.png"
    text breedMonster1.name size 40 font "SegoeBold.ttf" color (0,0,0) xpos (650- len(breedMonster1.name)* 28/ 2) ypos 20
    text ("Ferocity: "+ str(breedMonster1.ferocity)) size 30 font "SegoeBold.ttf" color (0,0,0) xpos 250 ypos 500
    text ("Finesse: "+ str(breedMonster1.finesse)) size 30 font "SegoeBold.ttf" color (0,0,0) xpos 800 ypos 500
    text ("Determination: "+ str(breedMonster1.determination)) size 30 font "SegoeBold.ttf" color (0,0,0) xpos 250 ypos 600
    text ("Cunning: "+ str(breedMonster1.cunning)) size 30 font "SegoeBold.ttf" color (0,0,0) xpos 800 ypos 600
    text ("Fertility: "+ str(breedMonster1.fertility)) size 30 font "SegoeBold.ttf" color (0,0,0) xpos 250 ypos 700
    text ("Endurance: "+ str(breedMonster1.stamina)+ "/"+ str(breedMonster1.maxStamina)) size 30 font "SegoeBold.ttf" color (0,0,0) xpos 800 ypos 700
    if (len(breedMonster1.relatives)> 1):
        add BreedCard(breedMonster1.relatives[1], False, "other", None) xpos 80 ypos 220 id "cardF"
        add BreedCard(breedMonster1.relatives[0], False, "other", None) xpos 875 ypos 220 id "cardM"
    imagebutton auto "data/menu/viewer/detailClose_%s.png" xpos 570 ypos 930 action Hide("details")
    
#Monster viewer
screen barn():
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    add im.Scale("data/menu/viewer/back.png", 1300, 1000)
    add viewerV
    add "data/menu/viewer/penFront.png" xpos 604 ypos 608
    add "data/menu/viewer/lighting.png"
    if (viewYoung):
        imagebutton auto "data/menu/viewer/old_%s.png" xpos 550 ypos 0  action toggleViewYoung
    else:
        imagebutton auto "data/menu/viewer/young_%s.png" xpos 550 ypos 0  action toggleViewYoung
    fixed:
        area (20, 150, 300, 850)
        vpgrid:
            cols 1
            draggable True
            mousewheel True
            for monster in monsterList1:
                add monster
    add filter1 xpos 5 ypos 15
    if (breedMonster1!= None):
        if (barnMenu):
            imagebutton auto "data/menu/viewer/hideMenu_%s.png" xpos 1050 ypos 0  action toggleBarnMenu
            imagebutton auto "data/menu/viewer/feed_%s.png" xpos 1050 ypos 120  action toggleBarnMenu
            if (breedMonster1.species.species!= "player"):
                imagebutton auto "data/menu/viewer/release_%s.png" xpos 1050 ypos 240  action discardMonsterBarn
            #if (breedMonster1.training< 10 and breedMonster1.stamina> 0):
                #imagebutton auto "data/menu/viewer/train_%s.png" xpos 1050 ypos 360  action Hide("barn"), Show("train")
        else:
            imagebutton auto "data/menu/viewer/showMenu_%s.png" xpos 1050 ypos 0  action toggleBarnMenu
        imagebutton auto "data/menu/viewer/info_%s.png" xpos 800 ypos 0  action Show("details")
    imagebutton auto "data/menu/viewer/back_%s.png" xpos 400 ypos 900  action Hide("barn"), Show("farm"), clearBreedMonsters, clearFilters
    add traitPick
  
##Training
screen train():
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    add im.Scale("data/menu/training/back.png", 1300, 1000)
    imagebutton auto "data/menu/training/fer_%s.png" xpos 100 ypos 100  action trainFerocity, Hide("train"), Show("barn")
    imagebutton auto "data/menu/training/fin_%s.png" xpos 800 ypos 100  action trainFinesse, Hide("train"), Show("barn")
    imagebutton auto "data/menu/training/det_%s.png" xpos 100 ypos 500  action trainDetermination, Hide("train"), Show("barn")
    imagebutton auto "data/menu/training/cun_%s.png" xpos 800 ypos 500  action trainCunning, Hide("train"), Show("barn")
    imagebutton auto "data/menu/training/back_%s.png" xpos 500 ypos 850  action Hide("train"), Show("barn")
        
#Monster requests
screen request():
    modal True
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    add im.Scale("data/menu/request/back.png", 1300, 1000)
    vpgrid:
        cols 2
        draggable True
        mousewheel True
        xpos 100
        ypos 165
        for monster in monsterList2:
            fixed:
                area (0, 0, 400, 190)
                add monster:
                    align (0.5, 0.5)
    vpgrid:
        cols 1
        draggable True
        mousewheel True
        xpos 970
        ypos 150
        for monster in monsterList1:
            add monster
    add filter1 xpos 958 ypos 15
    imagebutton auto "data/menu/request/back_%s.png" xpos 400 ypos 900  action Hide("request"), Show("farm"), clearBreedMonsters, clearFilters, clearText
    imagebutton auto "data/menu/request/fulfil_%s.png" xpos 395 ypos 0  action Hide("request"), sellMonster, Show("request")
    if (sellText!= None):
        text sellText size 40 color (80, 80, 0) font "SegoeBold.ttf" xpos (650- 30*len(sellText)/ 2) ypos 480 at fadeOutText
    add traitPick
    
#Mission/ Explore
screen combat():
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    add im.Scale("data/menu/battleHub/back.png", 1300, 1000)
    vpgrid:
        cols 2
        draggable True
        mousewheel True
        xpos 160
        ypos 255
        for mission in availableMissions:
            fixed:
                area (0, 0, 420, 165)
                add MissionCard(mission):
                    align (0.5, 0.5)
    imagebutton auto "data/menu/battleHub/back_%s.png" xpos 400 ypos 900  action Hide("combat"), Show("farm"), clearBreedMonsters, clearFilters
    imagebutton auto "data/menu/battleHub/explore_%s.png" xpos 700 ypos 0  action setExplore, Show("mission")
    imagebutton auto "data/menu/battleHub/map_%s.png" xpos 250 ypos 0  action Show("map")
    
screen mission(leave= True):
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    add im.Scale("data/menu/battleHub/backMission.png", 1300, 1000)
    text activeMission.title size 40 font "SegoeBold.ttf" italic True color (0,0,0,) xalign 0.5 ypos 100
    if (activeMission.scouted):
        text activeMission.enemies size 20 font "SegoeBold.ttf" color (0,0,0,) xpos 250 ypos 200
        text activeMission.primary size 20 font "SegoeBold.ttf" color (0,0,0,) xpos 250 ypos 235
        text activeMission.secondary size 20 font "SegoeBold.ttf" color (0,0,0,) xpos 250 ypos 270
        text activeMission.recommend size 20 font "SegoeBold.ttf" color (0,0,0,) xpos 250 ypos 305
        text activeMission.team size 20 font "SegoeBold.ttf" color (0,0,0,) xpos 250 ypos 340
        python:
            descText= activeMission.description
            itint= 0
            line1= ""
            line2= ""
            line3= ""
            line4= ""
            line5= ""
            line6= ""
            listLine= [line1, line2, line3, line4, line5]
            while (itint< 6):
                 if (len(descText)> 60):
                        textOut= descText[0: descText.find(" ", 60)]
                 else:
                        textOut= descText
                 if (itint== 0):
                     line1= textOut
                 elif (itint== 1):
                     line2= textOut
                 elif (itint== 2):
                     line3= textOut
                 elif (itint== 3):
                     line4= textOut
                 elif (itint== 4):
                     line5= textOut
                 elif (itint== 5):
                     line6= textOut
                 itint+= 1
                 if (len(descText)> 60):
                        descText= descText[descText.find(" ", 60)+ 1: ]
                 else:
                        break
        text line1 size 20 font "SegoeBold.ttf" color (0,0,0,) xpos 250 ypos 450
        text line2 size 20 font "SegoeBold.ttf" color (0,0,0,) xpos 250 ypos 490
        text line3 size 20 font "SegoeBold.ttf" color (0,0,0,) xpos 250 ypos 530
        text line4 size 20 font "SegoeBold.ttf" color (0,0,0,) xpos 250 ypos 570
        text line5 size 20 font "SegoeBold.ttf" color (0,0,0,) xpos 250 ypos 610
        text line6 size 20 font "SegoeBold.ttf" color (0,0,0,) xpos 250 ypos 650
    else:
        text "Details Unknown, send a scout to learn more" size 25 font "SegoeBold.ttf" color (0,0,0,) xpos 250 ypos 200
        imagebutton auto "data/menu/battleHub/scout_%s.png" xpos 570 ypos 730  action scoutMission
    if (leave):
        imagebutton auto "data/menu/battleHub/backMission_%s.png" xpos 250 ypos 720  action Hide("mission")
    imagebutton auto "data/menu/battleHub/selectorOpen_%s.png" xpos 800 ypos 720  action Hide("mission"), showCombat, Show("teamPickScreen")
    
screen teamPickScreen():
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    add im.Scale("data/menu/battleHub/backSelector.png", 1300, 1000)
    fixed:
        area (100, 150, 1300, 850)
        vpgrid:
            cols 3
            spacing 80
            draggable True
            mousewheel True
            for monster in monsterList1:
                add monster
    add filter1 xpos 138 ypos 13
    text activeMission.title size 30 font "SegoeBold.ttf" italic True color (0,0,0,) xalign 0.5 ypos 30
    text (str(len(selectorActive))+ "/"+ str(activeMission.maxTeam)+ " monsters.") size 20 font "SegoeBold.ttf" color (0,0,0,) xalign 0.5 ypos 80
    imagebutton auto "data/menu/battleHub/embark_%s.png" xpos 750 ypos 900  action Hide("teamPickScreen"), Hide("combat"), removeMission, Jump("CombatEngine")
    imagebutton auto "data/menu/battleHub/backSelector_%s.png" xpos 350 ypos 900  action Hide("teamPickScreen"), Show("mission"), clearSelection
    add traitPick
    
##BREEDING

#Breed
screen breed():
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    #background
    add im.Scale("data/menu/breed/back.png", 1300, 1000)
    text (str(int(pregChanceGlobal))+ "%") size 25 font "SegoeBold.ttf" xpos 645 ypos 40
    add viewerB
    #monster lists
    fixed:
        area (20, 150, 300, 850)
        vpgrid:
            cols 1
            draggable True
            mousewheel True
            for monster in monsterList1:
                add monster
    fixed:
        area (970, 150, 300, 850)
        vpgrid:
            cols 1
            draggable True
            mousewheel True
            for monster in monsterList2:
                add monster
    add filter1 xpos 10 ypos 15
    add filter2 xpos 958 ypos 15
    #buttons
    imagebutton auto "data/menu/breed/back_%s.png" xpos 530 ypos 955 action Hide("breed"), Show("farm"), clearBreedMonsters, clearFilters
    if (currentPair):
        if (breedMonster1!= None and breedMonster2!= None and breedMonster1.stamina> 0 and breedMonster2.stamina>0):
            imagebutton auto "data/menu/breed/repeat_%s.png" xpos 660 ypos 955 action Hide("breed"), startSex
        else:
            add "data/menu/breed/repeat_disabled.png" xpos 660 ypos 955
    else:
        if (breedMonster1!= None and breedMonster2!= None and breedMonster1.stamina> 0 and breedMonster2.stamina>0):
            imagebutton auto "data/menu/breed/breed_%s.png" xpos 660 ypos 955 action Hide("breed"), startSex
        else:
            add "data/menu/breed/breed_disabled.png" xpos 660 ypos 955
    if (incest):
        imagebutton auto "data/menu/breed/incest2_%s.png" xpos 510 ypos 5 action toggleIncest, refreshBreed
    else:
        imagebutton auto "data/menu/breed/incest_%s.png" xpos 510 ypos 5 action toggleIncest, refreshBreed
    if (exhaust):
        imagebutton auto "data/menu/breed/exhaust_%s.png" xpos 640 ypos 5 action toggleExhaust, refreshBreed
    else:
        imagebutton auto "data/menu/breed/exhaust2_%s.png" xpos 640 ypos 5 action toggleExhaust, refreshBreed
    add traitPick
                
#sex scene
screen h_scene(animString, i):
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    add "data/menu/hscene/back.png"
    add animString+ str(i)
    if (renpy.has_image(animString+ str(i+ 1))):
        imagebutton auto "data/menu/hscene/next_%s.png" xpos 1050 ypos 200 action Hide("h_scene"), ShowTransient("h_scene", None, animString, i+ 1)
    if (i> 0):
        imagebutton auto "data/menu/hscene/prev_%s.png" xpos 50 ypos 200 action Hide("h_scene"), ShowTransient("h_scene", None, animString, i- 1)
    imagebutton auto "data/menu/hscene/exit_%s.png" xpos 600 ypos 790 action calcPreg, Hide("h_scene")
        
screen h_scene_start(animString):
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()    
    add "data/menu/hscene/back.png"
    add animString+ str(0)
    if (renpy.has_image(animString+ str(1))):
        imagebutton auto "data/menu/hscene/next_%s.png" xpos 1050 ypos 200 action Hide("h_scene_start"), ShowTransient("h_scene", None, animString, 1)
    imagebutton auto "data/menu/hscene/exit_%s.png" xpos 600 ypos 790 action calcPreg, Hide("h_scene_start")
        
##ALERTS            
            
#Birth
screen birth(name, monster, wild= False):
    modal True
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    add im.Scale("data/menu/alert/back.png", 1300, 1000)
    python:
        global breedMonster1
        breedMonster1= monster
        renpy.redraw(viewerV, 0)
    if not (wild):
        add BreedCard(monster.relatives[1], False, "other", None) xpos 225 ypos 400 id "cardF"
        add BreedCard(monster.relatives[0], False, "other", None) xpos 700 ypos 400 id "cardM"
    add BreedCard(monster, False, "other", None) xpos 475 ypos 600 id "card"
    if (wild):
        text "Obtained a new monster!" size 50 color (0,0,0) font "SegoeBold.ttf" xpos 400 ypos 200
    else:
        text name+ " gave birth!" size 50 color (0,0,0) font "SegoeBold.ttf" xpos 400 ypos 200
    text "New monster's name:" size 30 color (0,0,0) font "SegoeBold.ttf" xpos 420 ypos 270
    button:
        id "input_1"
        xysize (500, 30)
        action NullAction()
        add Input(hover_color="#3399ff", size= 30, color="#000", default= "nameless", changed= renameMonster, length= 30, button= renpy.get_widget("birth", "input_1")) 
        xpos 370
        ypos 320
    if (wild):
        imagebutton auto "data/menu/alert/done_%s.png" xpos 878 ypos 800 action Hide("birth"), addMonsterWild
        imagebutton auto "data/menu/alert/release_%s.png" xpos 193 ypos 800 action Hide("birth")
    else:
        imagebutton auto "data/menu/alert/done_%s.png" xpos 878 ypos 800 action Hide("birth"), giveBirth2
        imagebutton auto "data/menu/alert/release_%s.png" xpos 193 ypos 800 action Hide("birth"), discardMonsterBirth, giveBirth2

#Age Up
screen ageUp(name):
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    add im.Scale("data/menu/alert/back.png", 1300, 1000)
    text name+ " has grown up!" size 50 color (0,0,0) font "SegoeBold.ttf" xpos 400 ypos 250
    imagebutton auto "data/menu/alert/done_%s.png" xpos 878 ypos 800 action Hide("ageUp")

#Pregnancy
screen pregnantWin(pregName):
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    add im.Scale("data/menu/alert/back.png", 1300, 1000)
    text pregName size 50 color (0,0,0) font "SegoeBold.ttf" xpos  400 ypos 250
    imagebutton auto "data/menu/alert/done_%s.png" xpos 878 ypos 800 action Hide("pregnantWin")
    
#fade
screen fadeSleeper():
    modal True
    add "data/other/blackscreen.png" at fadeSleep
    timer 1.0 action Hide("fadeSleeper"), updateTimeKeeper
    