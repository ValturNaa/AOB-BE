## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define e = Character('Eileen')


## The game starts here.

label wolf_event:

    ## Show a black or forested background
    scene

    ## generate the wolf's card here with sex, stats, colors, and so forth
    ## here 0 represents male, 1 is female, and 2 is herm    
    python:
        genders= ["male", "female", "hermaphrodite"]
        monster= newMonsterWild(knownSpecies["clawwolf"])
        
    $ player_gender = genders.index(player.gender)
    $ wolf_gender = genders.index(monster.gender)
    $ sex_enabled = True
    python:
        winint= random.randint(0, 1)
    if (winint== 1):
        $ win = True
    else:
        $ win = False
    ## compare PC and wolf sexes, and run a global checker to determine if sex is enabled for this pair

    "Wandering the woods near my farm, I find I can finally relax. No monsters snapping from their pens, and no soldiers peering over my shoulder trying to see my training methods."
    "A familiar growl comes from the bushes up ahead. The sound is easy to follow, and leads only a short way off the trail."
    
    if wolf_gender == 0:
            "It comes from a wild claw wolf leaning up against a tree. His fur is marked in ragged chalk patterns and his ears hang low in sad dejection. Even his cock, typically erect in a virile male, is sadly couched in its sheath."
            "A twig snaps underfoot, and the wolf springs to his feet, baring teeth and readying his claws for battle. I know those signs. I have to respond, and quickly. But what should I do?"
    if wolf_gender == 1:
            "It comes from a wild claw wolf leaning up against a tree. Her fur is streaked with white, as if rough paws tried to wipe away the usual chalk markings. A stream of her own cum drips from her cunt, and she brushes at it sadly."
            "A twig snaps underfoot, and the wolf springs to her feet, baring teeth and readying her claws for battle. I know those signs. I have to respond, and quickly. But what should I do?"
    
    menu:
        "dominate the wolf":
            ## run contest simulator to determine who wins
            "I set my feet prepare to stand my ground. This is a dominance match, and I’ve seen enough of those to know what to expect. When the wolf charges, I’m ready for the attack."
            if player_gender == 0 and wolf_gender == 0:
                if win and sex_enabled:
                    "The wolf is a strong fighter, but I’ve fought his type before. After he goes down, breathing hard, I get behind him and drop my pants. His head turns to watch me and his eyes grow wide."
                    "-rape scene plays-"
                    jump endWin
                elif sex_enabled:
                    "I think I underestimated this wolf. He’s a lot stronger than I had figured, and he leaves me on the ground in a heartbeat. I’m pulled up by the belt, and then my clothes are ripped off my body while the wolf’s dick rises behind me."
                    "-rape scene plays-"
                    jump endLose
                if win and not sex_enabled:
                    "The wolf’s own ferocity plays to my strength. He flies into trees, into rocks, and onto the ground before he stops getting up. Then I hover over him and press his claws to his own throat."
                    "His eyes close and his breath stalls as if he waits for death, but I pull him back to his feet and give him a cold, hard stare. He drops his gaze to acknowledge me as his leader."
                    jump endWin
                elif not sex_enabled:
                    "I am no stranger to fighting, but this wolf is far too strong for me. He puts me down hard on my seat and stands over me, tall and menacing. But then he winces, clutches at his shoulder, and stumbles away."
                    jump endLose
            
            elif player_gender == 0 and wolf_gender == 1:
                if win and sex_enabled:
                    "The wolf is strong, but she seems to lack heart. After a couple of clashes, she hits the dirt and lies still. She jumps when I press my tongue to her clit, and watches me disrobe with astonished eyes. She must be in heat, because she doesn’t even resist."
                    "-rape scene plays-"
                    jump endWin
                elif sex_enabled:
                    "I think I underestimated this wolf. She’s a lot stronger than I had figured, and puts me on the ground in a heartbeat. Then she bends over me with her nose to my dick, and shreds my pants to get at me."
                    "-rape scene plays-"
                    jump endLose
                if win and not sex_enabled:
                    "It doesn’t take much to put the wolf on the ground. One faceplant into a tree and she seems to lack the will to get up. My fingers wrapped in her fur, I pull her to her feet."
                    "She drops to her knees and presses her head against me in defeat. I catch her hands and draw her up. She meets my eyes then bows her head and gently licks my hand to acknowledge my strength."
                    jump endWin
                elif not sex_enabled:
                    "The wolf fights with aggressive desperation, and all my training proves ineffective. As I lie still on the grass, she raises her claws to finish me, but then clutches her stomach with one hand and slowly moves away."
                    jump endLose
                
            elif player_gender == 1 and wolf_gender == 0:
                if win and sex_enabled:
                    "I don’t think the wolf thought a woman could best him. I bend over him as he lies on his back, and I draw back his sheath. His eyes follow me as I strip down, and his ears stand up again in hope."
                    "-rape scene plays-"
                    jump endWin
                elif sex_enabled:
                    "I’d like to think I let him win, but it comes to the same thing either way. The wolf puts me down with little effort and goes straight for my ass, as I knew he would. His dick flowers right in front of me, and he rips my clothes out of the way."
                    "-rape scene plays-"
                    jump endLose
                if win and not sex_enabled:
                    "The wolf’s own ferocity plays to my strength. He flies into trees, into rocks, and onto the ground before he stops getting up. Then I hover over him and press his claws to his own throat."
                    "His eyes close and his breath stalls as if he waits for death, but I pull him back to his feet and give him a cold, hard stare. He drops his gaze to acknowledge me as his leader."
                    jump endWin
                elif not sex_enabled:
                    "I am no stranger to fighting, but this wolf is far too strong for me. He puts me down hard on my seat and stands over me, tall and menacing. But then he winces, clutches at his shoulder, and stumbles away."
                    jump endLose
            
            elif player_gender == 1 and wolf_gender == 1:
                if win and sex_enabled:
                    "It doesn’t take much to overpower the wolf. Even an outsider like me can see her heart isn’t in it, and when I put her to the ground, she quietly sobs into the grass."
                    "She must be in heat to show so much weakness. I bend to her ass to cheer her up, and her sobbing suddenly stops when I lick her clit. I disrobe with a gentle smile and prepare to make her happy."
                    "-rape scene plays-"
                    jump endWin
                elif sex_enabled:
                    "Fighting seems to bring back the wolf’s sense of purpose, and she counters me with surprising strength. After  a few repeats of me hitting the ground, I just can’t get up anymore. Howling triumph, the wolf hauls me to my feet and gropes my breasts."
                    "My breath catches in my throat, and my legs give out when she raises her claws meaningfully. By the time they slide inside me, I can’t fight back anymore."
                    "-rape scene plays-"
                    jump endLose
                if win and not sex_enabled:
                    "It doesn’t take much to put the wolf on the ground. One faceplant into a tree and she seems to lack the will to get up. My fingers wrapped in her fur, I pull her to her feet."
                    "She drops to her knees and presses her head against me in defeat. I catch her hands and draw her up. She meets my eyes then bows her head and gently licks my hand to acknowledge my strength."
                    jump endWin
                elif not sex_enabled:
                    "The wolf fights with aggressive desperation, and all my training proves ineffective. As I lie still on the grass, she raises her claws to finish me, but then clutches her stomach with one hand and slowly moves away."
                    jump endLose
            
        "calm the wolf":
            "It’s hard to tell if this is a dominance match or a territorial battle, and I’d rather not get caught in a death match. Before the wolf can attack, I drop submissively to my hands and knees."
            
            if wolf_gender == 0:
                "He looks startled, but his claws relax. I heave a sigh. At least the fight was forestalled. Now, I just have to bear with whatever comes next."
                if win and sex_enabled:
                    "His dick blooms back to life as he approaches me with a dominant strut. And as if I didn’t already know what he wants, he shoves it in my face. I meekly look up at him as I flick my tongue across the shaft. His tongue hangs out to relish the attention."
                    "I give him a hand on the balls and another on the knot and swallow his cock halfway to the knot. His eyes roll and his legs get weak, and I put him on the ground without any effort."
                    "A light glimmers in his eyes as he realizes my ploy. But my mouth on his cock excites him, and he can’t find the will to resist my advance."
                    "-rape scene plays-"
                    jump endWin
                elif sex_enabled:
                    "His dick blooms back to life as he approaches me with a dominant strut. And as if I didn’t already know what he wants, he shoves it in my face. Trying to play the docile puppy, I meekly catch his cock in one hand and place the tip in my mouth."
                    "After a moment or two of gentle sucking, his hand goes to my head and forces his dick down my throat. I gasp, gurgle, and try to pull free and get my breath, but he doesn’t let me up."
                    "Dissatisfied with the blowjob, the wolf pulls me sputtering to my feet, and before I quite realize what he’s doing, my clothes lie in shreds on the ground."
                    "-rape scene plays-"
                    jump endLose
                if win and not sex_enabled:
                    "The wolf watches as I approach him. I can almost hear the gears grinding in his head. He doesn’t see it coming. I flip him off his feet with one hand on his tail and the other on his knee, and he stares up as I pin him to the ground."
                    "By the time he thinks to fight back, there’s nothing he can do. I press his claws to his throat as a warning, and he deflates. Shock crosses his face when I let him up, and he meekly licks my hand to acknowledge my victory."
                    jump endWin
                elif not sex_enabled:
                    "The wolf watches as I approach him. His eye gleams cunningly. I try to surprise him, but it is I who gets thrown off my feet. Then the beating begins."
                    jump endLose
            
            elif wolf_gender == 1:
                "She looks startled, but her claws relax. I heave a sigh. At least the fight was forestalled. Now, I just have to bear with whatever comes next."
                if win and sex_enabled:
                    "She watches curiously as I approach her slowly on all fours. With a little distracted pawing at her thighs, I reach for her tits and begin to suckle. Her eyes droop in satisfaction, but when I insert my fingers for a top-and-bottom attack, her body goes limp."
                    "She doesn’t resist when I ease her to the ground, but her eyes gleam with understanding as I take charge. When I draw back to disrobe, she waits patiently."
                    "-rape scene plays-"
                    jump endWin
                elif sex_enabled:
                    "She watches curiously as I approach her on all fours. A tentative hand on her thigh relaxes her a little, and I press my tongue to her pussy. Her eye gleams cunningly, and she catches me by the hair."
                    if player_gender == 0:
                        "Her hand reaches for my hardening cock, and she rubs herself meaningfully. She pushes me to the ground, and her claws shred my clothes. Then she takes her position."
                    elif player_gender == 1:
                        "Her hand clasps my breast, then closes around my clothes and rips my top apart. She chokes me to keep me in line, shreds the rest of my clothes, and pushes me into position."
                    "-rape scene plays-"
                    jump endLose
                if win and not sex_enabled:
                    "The wolf watches as I approach her. I can almost hear the gears grinding in her head, but she still doesn’t see it coming. I spring from the ground, pinning her hands against the tree and distracting her by pressing my body against hers."
                    "By the time she thinks to fight back, I have complete control. I press her claws to her throat as a warning, and then let her go. Falling to her knees, she meekly licks my hand to acknowledge my victory."
                    jump endWin
                elif not sex_enabled:
                    "The wolf watches with cunning eyes as I approach her. I try to spring and pin her, but she wrestles free and pins me to the ground instead. Her eyes gleam fiercely, and she punishes my trickery with a sound beating."
                    jump endLose
                
                
        "escape":
            "I’d rather not tangle with an enraged claw wolf. Luckily the wolf isn’t a fast runner. He/she falls rapidly behind and sinks against another tree with a mournful howl. I glance back, startled. I wonder if the wolf will follow me."
            show screen farm
            pause
    
    return
    
label endWin:
    if wolf_gender == 0:
        "The wolf’s growling subsides as he acknowledges me. The journey home is quick, and my new wolf follows me all the way."
        "He doesn’t even complain when I sweep out a stall for him. I think the smell of other wolves reassures him. Can’t wait to find out how he performs."
    if wolf_gender == 1:
        "The wolf’s growling subsides as she acknowledges me. The journey home is quick, and my new wolf follows me all the way."
        "She doesn’t even complain when I sweep out a stall for her. I think the smell of other wolves reassures her. Can’t wait to find out how she performs."
    show screen farm
    python:
        global rename
        rename= monster
        renpy.show_screen("birth", "", monster, True)
    pause
    
    
label endLose:
    "I wake up alone in the silent forest. Though the dirt is still scuffed from our fight, the wolf is long gone."
    "After the beating I’ve taken, I have to drag myself off the ground. I take a few minutes to clean myself off, then prepare for the long, painful hike home. I hope I can slip into some fresh clothes before anyone notices."
    show screen farm
    pause
