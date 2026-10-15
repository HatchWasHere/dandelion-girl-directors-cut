
label opening:

    scene black

    pause 1.0


    # --------------------------------------------------------------
    # Dandelion Field
    # --------------------------------------------------------------

    play music time_to_sleep

    narrator "What is deja vu, exactly?"

    narrator "It's this nagging sense of familiarity, like we've done something or been somewhere once before."

    narrator "You could swear it's definitely your first go-around, though."

    narrator "Somewhere in your head, you think, 'I must have been here, before.'"

    narrator "Naturally, all you can do is ignore it."

    narrator "We trust that we know what happened over what some strange voice in our head tries to tell us."

    pause 0.5

    scene sky
    with corner_fade
  

    narrator "The blue sky stretched as far as the eye could see, over the green pasture."

    narrator "Seasonal flowers dotted the field below, with bright speckles of yellow scattered among them."

    narrator "Dandelions."

    narrator "They swayed back and forth gently in the warm breeze."

    narrator "Technically, dandelions are weeds."

    narrator "They're meant to be ripped out of the ground and tossed in a trash bucket before they can take over a garden."

    narrator "But somehow, under this slice of clear summer sky... I thought those bright yellow plants looked beautiful, too."

    scene black at old_bg
    with Dissolve(0.5)


    narrator "In the middle of the field was a beautiful girl in a white dress, dancing in circles."

    narrator "The flowers danced around her in the breeze, and her straw hat tumbled off her head."

    narrator "Her hair was fair, a shade or two darker than the dandelions."

    narrator "The girl sucked in a deep breath of the sweet summer air and continued her dance."

    pause 1.5

    scene cg julie_dancing at old_bg
    with Dissolve(0.25)


    narrator "She looked... simply happy to be there."

    narrator "For one reason or another, I couldn't take my eyes off her."

    pause 0.5

    scene black at old_bg
    with Dissolve(0.25)

    narrator "She picked up her hat, and held it."

    narrator "She didn't put it back on her head right away."

    narrator "Instead the dandelion girl grinned and held her hand over her eyes, looking at the bright blue sky overhead, and simply took it all in."

    scene sky
    with Dissolve(0.15)

    narrator "There's probably something poetic I could've said about the scene."

    narrator "Something about summer, flowers, or a sonnet..."

    narrator "I watched the girl and felt a strange, almost painful deja vu."

    narrator "Obviously, that was wrong."

    narrator "It was our very first meeting, wasn't it?"


    # --------------------------------------------------------------
    # Julie CG
    # --------------------------------------------------------------

    scene cg_julie_intro_1
    with Dissolve(0.25)

    pause 0.75

    scene cg_julie_intro_2
    with Dissolve(0.25)

    narrator "It was some time before I realized."

    narrator "The dandelion girl with the straw hat had stopped dancing, and now she was just standing there, staring at me with a face like a curious animal."

    narrator "I thought:"

    narrator "One time, in a place far away from here, I'd witnessed a scene just like this."

    stop music fadeout 3.0


    ## == Transition Effect == ##

    pause 0.5

    scene cg_julie_intro_2b
    with corner_fade

    pause 1.0

    scene outro_1a
    with Dissolve(0.75)

    pause 1.5
    
    
    play sound piano_stinger
    scene outro_1b
    with Dissolve(0.75)


    pause

    scene black
    with Dissolve(2.0)


     ## == Transition Effect == ##

    

    jump chapter_1

