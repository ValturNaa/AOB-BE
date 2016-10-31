# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
#image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define val = Character('Captain Valorin', color="#c8ffc8")
define ibeard = Character('Captain Ironbeard', color="#c8ffc8")


# The game starts here.
label start:
    
    $ PCName = "Player"
    $ playerFemale = False

    #scene black_screen

    "{i}I don’t remember much about my early childhood. Just a vague sense of fear and unfamiliarity. I think we moved around a lot."
    
    #scene hazy_house
    #show wolves_gathered

    "{i}But I remember the wolves. They were big, and they were scary, and I thought they were going to kill me."
    
    #show fairy_shadow
    
    "{i}Then she came. I can’t describe her, except that she was beautiful, and they were afraid of her. Her hands were gentle, and her voice was soft, and she promised me I’d be safe."
    
    #scene farm with fade
    
    "{i}The next thing I remember were the bellhorns. There were a lot of them at my family’s farm. I liked the bellhorns. They could look at me without judging me, and they never called me a freak."

    "{i}It’s funny. I spent most of my life looking over my shoulder, afraid that the wolves would come back for me. Who knew, one day, it would be me who came back for them."
    
    #cutscene: Commander K9 rescues you from the fire. After the sequence, Captain Valorin takes center stage.
    
    "Captain" "Are you all right? What's your name?"
    
    #character selection menu. Variables PCName and playerFemale are defined here
    
    val "Captain Valorin Keldoss here. Is this your wolf, [PCName]?"
    
    #val moves left and Commander the wolf appears on the right
    "Commander" "Grrr...."
    
    menu:

        "Back, Commander. He’s not an enemy.":
            #val resumes center stage as Commander slips off screen
            val "Thank you, [PCName]. Now, we should get you out of here. This town is no longer safe. Those savage wolves may have driven off the enemy, but if they come back-"
    
        "Put your teeth away, Commander. No one told you to fight.":
            #val resumes center stage as Commander slips off screen
            val "Thank you, [PCName]. Now, we should get you out of here. This town is no longer safe. Those savage wolves may have driven off the enemy, but if they come back-"
    
        "Start talking, soldier.":
            #val resumes center stage as Commander slips off screen
            val "Thank you, [PCName]. Now, we should get you out of here. This town is no longer safe. Those savage wolves may have driven off the enemy, but if they come back-"
    
    
    #val resumes center stage as Commander slips off screen
    #val "Thank you, [PCName]. Now, we should get you out of here. This town is no longer safe. Those savage wolves may have driven off the enemy, but if they come back-"
    
    menu:
        
        "They aren’t savages, captain.":
            #Val’s image changes to look toward commander, and after a second looks back at the player.
            val "You must be the wolf trainer I’ve heard about. Come with me. Duke Fentler will want to see you."
    
        "Oh, you mean my pets?":
            #Val’s image changes to look toward commander, and after a second looks back at the player.
            val "You must be the wolf trainer I’ve heard about. Come with me. Duke Fentler will want to see you."
    
    
    
    #black screen
    
    "It takes days of traveling to reach Castle Fentren, and days longer to meet with the duke. But in the end, the army takes Commander, and you find yourself staring at what was once a thriving farm. Now, everything is falling apart."
    
    #farm background with Captain Valorin at center screen
    
    val "And here we are. It’s not much, but it’s available."
    
    val "I’m sorry for your loss, [PCName]. Stories like yours are becoming far too common these days. Between monster attacks and those Imperial bastards, I don’t think Bavan has seen such hard times since the Beast Wars."

    menu:
        "Were there any other survivors?":
            val "We couldn’t find anyone else alive. The whole attack was carefully planned. If you hadn’t made all those wolves attack when you did, it would have been all over by the time I arrived."
        "I’m sure it’s not that bad, captain.":
            val "Worse, actually. I’ve lost a lot of good men, and I know other captains who’ve had worse. I was starting to lose all hope. But then I saw you, and the Commander."

    val "I’ve heard stories of tame claw-wolves, but I never thought I’d live to see one. If you can do that again, then maybe we {i}can{/i} survive this war."

    #val moves to the right side, and Ironbeard enters on the left

    "Veteran" "I’ll take it from here, Valorin."

    val "Aye, sir. [PCName], this is Captain Ironbeard, recruiter for Duke Fentler. He’s the man in charge of this little project. You’re going to be working with him a lot, so try to be polite."

    #ibeard's expression changes to a scowl
    ibeard "Thank you, Valorin. You’re dismissed."

    #val disapears and ibeard moves to center stage. Ibeard's image changes to one reading a writ

    ibeard "I am here to provide you with this writ and see that you receive everything you need to start this little project."

    ibeard "By order of Duke Fentler, Lord of the Southern Reach, you, [PCName], are hereby granted this title of land and all rights appertaining thereto. And so on and so forth. Keep this safe, [PCName]. As long as you hold this writ, only the Duke himself can command you."

    #Ironbeard's image returns to normal

    ibeard "Now, I believe Captain Valorin recovered a pair of wolves from the attack. I’ll see to it they’re moved to the barn and proper stalls are set up. I hope you really can tame these brutes. Our soldiers need all the help they can get."

    ibeard "I understand you’re a trainer, but you’ve never {i}bred{/i} monsters before. Is there anything you need to know?"
    
    menu:

        "I grew up on a farm. I'll figure it out.":

            jump finish

        "I could use a refresher.":

            jump tutorial
            

label tutorial:
    
    menu:
        
        "Tell me more about breeding":
            ibeard "Near as I can figure it, these beasts will go at it like rabbits if they get the chance. Gotta keep em in separate pens, or they’ll be making babies left and right and you won’t know who’s the father."
            ibeard "Breeding em is easy enough. Just head to the breeding pen, pick a couple of monsters, and send them inside. They’ll do the rest. You can keep breeding the same pair as long as they have the energy. Once they’re worn out, they won’t offer much resistance when you put em back in their pens."
            ibeard "Once the female takes, she’ll take care of the rest. Soon as the baby pops out, you can breed her again. O’ course, you can keep breeding her anyway, but she can only have one at a time. Don’t worry. Monsters breed fast. A few days in her pen and she’ll be raring to go."
            ibeard "The littl’uns grow up quick. In about a week, they’ll be ready for breeding too. Just don’ push em into it too early. Trust me, they’re breakable. I’ll build a playpen to keep those ones in until they’re old enough."
            ibeard "Any more questions?"
            jump tutorial
        "How do I train monsters":
            ibeard "I thought you were the trainer here. Training a monster is pretty simple. Every time they breed, they get stronger. Every time they fight, they get stronger. But each monster can only train up so much, and eventually you’ll have to breed new ones to get stronger."
            ibeard "Just make sure them monsters know who’s in charge. Brutes like these would kill you the first time you turned your back."
            ibeard "Any more questions?"
            jump tutorial
        "What can I do in the barn":
            ibeard "The barn is where all your monster pens go. Each monster has to be locked in its own cell when you aren’t using them, or they would escape, fight, and randomly breed just like wild monsters."
            ibeard "Use the round pen in the center to exercise the beasts, give them treats that enhance their growth, or harvest them for milk, eggs, and other useful items."
            ibeard "You can also restrain them to examine them more closely, and I’ll give you a box to store detailed breeding information like age and parentage."
            ibeard "Of course you’ll have to search the barn to find the monster you want. But I’m sure you can figure that part out."
            ibeard "Any more questions?"
            jump tutorial
        "What about when I get tired":
            ibeard "Your house is right next to the barn. It don’t look like much right now, but I’ll have it fixed up in no time. When you get tired, just go inside and sleep. Remember, going back to the house starts a new day."
            ibeard "You’ll wake up the next morning with fresh monsters, ready for a new day."
            ibeard "Any more questions?"
            jump tutorial
        "How do I know what you expect from me":
            ibeard "I’ll post jobs for you on this board by the gate. You bring me a monster that fits the requirements on a card and I’ll pay you for it. It’s real simple. But if I don’t get a monster in a reasonable time period, the captain who requested him may be beyond needing help, so try to keep up."
            ibeard "Once in a while, I’ll bring you a request on his Lordship’s gold leaf. The Duke demands only the best, and it won’t be easy to fill his requests, but if you can handle it, you’ll get a lot more coin."
            ibeard "I’ll also leave a standing contract for you. Contracts have no time limit, but filling them will open up new possibilities for our boys in the field and help us win this war."
            ibeard "Any more questions?"
            jump tutorial
        "That’s all for now":
            ibeard "I’ll help you get fixed up and then head back to town. Lets get to work, [PCName]. I hate this farm smell."
            jump finish
            
label finish:
    show screen farm
    pause