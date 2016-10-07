# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:
    
    # Im keeping all my combat stuff in modulated files to try and keep thing neat. Look at CombatEngine.rpy

    jump CombatEngine
    
    return
