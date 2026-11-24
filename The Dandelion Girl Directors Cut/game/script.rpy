

label start:


    scene new_black with Dissolve(3.0)

    pause 2.0

    show screen game_menu_button

    jump opening

label before_main_menu:

    if persistent.game_completed:
        play music "bgm/seasons.mp3" fadein 2.0
    else:
        play music "bgm/longing_still_goes_on.mp3" fadein 2.0

    return
