init -1 python hide:
    ##Screen Setup
    print ""
    config.screen_width= 1300
    config.screen_height= 1000
    config.window_title= u"Ashes of Bavan"
    config.name= "AoB indev"
    config.version= "0.0.10"
    config.rollback_enabled= False
    config.keymap["dismiss"]= ['K_SPACE']
    config.keymap["hide_windows"]= []
    config.keymap["game_menu"]= []
    config.keymap["rollback"] =[]
    config.keymap["rollforward"] =[]
    
    #theme
    theme.a_white_tulip(
        widget= "#c1c6d3",
        widget_hover= "#d7dbe5",
        widget_selected= "#c1c6d3",
        disabled= "#b4b4b4",
        frame= "#9391c9",
        mm_root= "#ffffff",
        gm_root= "#ffffff",
        regular_font= "_theme_awt/Quicksand-Regular.ttf",
        bold_font= "_theme_awt/Quicksand-Bold.ttf",
        )

python early:
    #saves
    config.save_directory = "BSR-1469644732"

init -1 python hide:
    #default settings
    config.default_fullscreen = False
    config.default_text_cps = 0
    config.default_afm_time = 10


## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "BSR-1.0"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "BSR"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    