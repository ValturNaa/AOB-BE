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

    "I don’t remember much about my early childhood. Just a vague sense of fear and unfamiliarity. I think we moved a lot."

    #scene hazy_house
    #show wolves_gathered

    "But I remember the wolves. They were big, and they were scary, and I thought they were going to kill me."
    
    #show fairy_shadow
    
    "Then she came. I can’t describe her, except that she was beautiful, and they were afraid of her. Her hands were soft, and she spoke gently. She promised I would be safe."
    
    #scene farm with fade
    
    "The next thing I remember were the bellhorns. There were a lot of them at my family’s farm. I liked the bellhorns. They could look at me without judging me, and they never called me a freak."

    "It’s funny. I spent most of my life looking over my shoulder, afraid that the wolves would come back for me. Who knew, one day, that it would be me who came back for them."
    
    #cutscene: Commander K9 rescues you from the fire. After the sequence, Captain Valorin takes center stage.
    
    "Captain" "Are you all right? What's your name?"
    
    #character selection menu. Variables PCName and playerFemale are defined here
    
    val "Captain Valorin Keldoss here. Is this your wolf, [PCName]?"
    
    #val moves left and Commander the wolf appears on the right
    "Commander" "Grrr...."
    
    "I told Commander to stop. Reluctantly he turned to look at me and then backed down."
    
    #val resumes center stage as Commander slips off screen
    val "Thank you, [PCName]. Now, we should get both of you out of here. This town is no longer safe. Those savage wolves may have driven off the enemy, but if they come back-"
    
    "I told the captain that the wolves weren’t savage. He stared at me for a moment. Then his eyes took in the Commander hovering behind me, and he nodded."
    
    val "You must be the wolf trainer I’ve heard about. Come with me. Duke Fentler will want to see you."
    
    #black screen
    
    "It took days of traveling to reach the duke’s castle, and days longer to meet with the duke. But in the end, the army took Commander, and I found myself staring at what had once been a thriving farm. Now, everything was falling apart. It looked like a stampede."
    
    #farm background with Captain Valorin at center screen
    
    val "And here we are. It’s not much, but it’s available."
    
    if playerFemale == False:
        "I looked around at the dilapidated buildings, the fallen fences, and the empty pastures. It was all familiar to an old farm boy, and I wondered what had happened to the farmers and bellhorns that must have lived here."
    if playerFemale == True:
        "I looked around at the dilapidated buildings, the fallen fences, and the empty pastures. It was all familiar to an old farm girl, and I wondered what had happened to the farmers and bellhorns that must have lived here."
        
    val "I’m sorry for your loss, [PCName]. Stories like yours are becoming far too common these days. Between demons and those Imperial bastards, I don’t think Bavan has seen such hard times since the Beast Wars."

    "I asked if there were any other survivors. Surely out of the dozens of Academy staff, someone-"

    val "We couldn’t find anyone else alive. The whole attack was carefully planned. If you hadn’t made all those wolves attack when you did, it would have been all over by the time I arrived."

    "I tried to explain that I only freed the wolves, and that claw-wolves are naturally protective of their territories, but then I saw the Captain’s eyes staring into the distance, and I fell silent."

    #val shifts to a thoughtful pose, no longer looking out at you
    val "Sometimes, I swear I can see Death himself, old Brazar wrapped in a shroud. I’ve lost a lot of good men to this war, and I know I’ll lose plenty more before this is over."
    
    val "But when I saw the Commander standing over you, protecting you…I saw something else. Hope, hovering like a light over your head. There’s something special about you, [PCName]."

    #val returns to his normal pose
    val "I’ve heard stories of tame claw-wolves, but I never thought I’d live to see one. If you can do that again, and train monsters to fight side by side with soldiers, then maybe we can survive this war."
    
    #val moves to the right side, and Ironbeard enters on the left

    ibeard "I’ll take it from here, Valorin."

    val "Aye, sir. [PCName], this is Captain Ironbeard, recruiter for Duke Fentler. He’s the man in charge of this little project. You’re going to be working with him a lot, so try to be polite."

    #ibeard's expression changes to a scowl
    ibeard "Thank you, Valorin. You’re dismissed."

    val "Good luck, [PCName]. Maybe we’ll meet again in the field one day."
    
    #val disapears and ibeard moves to center stage. Ibeard's image changes to one reading a writ

    ibeard "I am here to provide you with this writ and see that you receive everything you need to get straight to work."

    ibeard "By order of Duke Fentler, Lord of the Southern Reach, you, [PCName], are hereby granted this title of land and all rights appertaining thereto. And so on and so forth. Keep this safe, [PCName]. As long as you hold this writ, only the Duke himself can command you."

    "Ironbeard tied the scroll neatly with a ribbon into a little bow before handing it to me. I accepted the scroll, uncertain whether I was supposed to bow or salute."

    #Ironbeard's image returns to normal

    ibeard "Now, I believe Captain Valorin brought two new wolves for you to train. I’ll see to it they’re moved to the barn and proper stalls are set up. I hope you really can tame these brutes. Our soldiers need all the help they can get."

    ibeard "I understand you’re a trainer, but never bred monsters before. Is there anything you need to know about it?"
    
    menu:

        "I grew up on a farm. I'll figure it out.":

            jump finish

        "I could use a refresher.":

            jump tutorial
            

label tutorial:
    
    menu:
        
        "Tell me more about breeding":
            ibeard "Near as I can figure it, these beasts will go at it like rabbits if they get the chance. Gotta keep em in separate pens, or they’ll be making babies left and right and you won’t know which one’s the father."
            ibeard "Breeding em is easy enough. Just head to the breeding pen, pick a couple of monsters, and send them inside. They’ll do the rest. You can keep breeding the same pair as long as they—and you—have the energy. Once they’re worn out, they won’t offer much resistance when you put em back in their pens."
            ibeard "Once the female takes, she’ll develop over time. In a couple days, the littl’un will just pop out. Soon as that happens, you can keep breeding her. O’ course, you can keep breeding her anyway, but she won’t have any more littl’uns."
            ibeard "The littl’uns grow up quick. In about a week, they’ll be ready for breeding too. Just don’ push em into it too early. Trust me, they’re breakable. I’ll build a playpen to keep those ones in until they’re old enough for breeding and combat training."
            ibeard "Any more questions?"
        "How do I train monsters":
            ibeard "And I thought you were the trainer here. Training a monster is pretty simple. Every time they breed, they get stronger. Every time they fight, they get stronger. But each monster can only train up so much, and eventually you’ll have to breed new ones to get stronger monsters."
            ibeard "Just make sure them monsters know who’s in charge. Brutes like these would kill you the first time you turned your back."
            ibeard "Any more questions?"
        "What can I do in the barn":
            ibeard "The barn is where all your monster pens go. Each monster has to be locked in its own cell when you aren’t using them, or they would escape, fight, and randomly breed just like wild monsters."
            ibeard "I’ll set you up with a secure round-pen in the middle of the barn where you can assess the strengths of your monsters, train and exercise them, or give them special treats that enhance their growth."
            ibeard "Of course you’ll have to search the barn to find the monster you want. But I’m sure you can figure that part out."
            ibeard "Any more questions?"
        "What about when I get tired":
            ibeard "Your house is right next to the barn. It don’t look like much right now, but I’ll have it fixed up in no time. When you get tired, just go inside and sleep. Remember, going back to the house starts a new day."
            ibeard "You’ll wake up the next day with your energy restored, and so will your monsters. If your monsters get hurt, they’ll heal each day, but not as fast as they regain energy. A badly hurt monster will take several days to recover."
            ibeard "Any more questions?"
        "How do I know what you expect from me":
            ibeard "I’ll post my monster requests on this board by the gate. You bring me a monster that fits the requirements on a card and I’ll pay you for it. It’s real simple. But if I don’t get a monster in a reasonable time period, the captain who requested him may be beyond needing reinforcements."
            ibeard "Once in a while, I’ll bring you a request on his Lordship’s gold leaf. The Duke demands only the best, and it won’t be easy to fill his contracts, but if you can handle it, you’ll get a lot more coin."
            ibeard "I’ll also leave a standing contract for you. Contracts have no time limit, but filling them will open up new possibilities for our boys in the field and help us win this war."
            ibeard "Any more questions?"
        "That’s all for now":
            ibeard "Once the barn’s fixed and the house is livable, I’ll be headin’ back. But I’ll swing by every few days to post new requests on the notice board."
            ibeard "No time to waste, [PCName]. Let's get to work."
            jump finish
            
label finish:
    show screen farm
    pause