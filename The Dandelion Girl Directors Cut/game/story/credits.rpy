label credits:

    scene black

    # Prevent normal skipping through the credit roll.
    $ _skipping = False

    scene credits 1 at old_credits
    with Dissolve(1.0)
    pause 8.0

    scene credits 2 at old_credits
    with Dissolve(1.0)
    pause 8.0

    scene credits 3 at old_credits
    with Dissolve(1.0)
    pause 8.0

    scene credits 4 at old_credits
    with Dissolve(1.0)
    pause 8.0

    scene credits 5 at old_credits
    with Dissolve(1.0)
    pause 8.0

    scene credits 6 at old_credits
    with Dissolve(1.0)
    pause 8.0

    scene credits 12 at old_credits
    with Dissolve(1.0)
    pause 8.0

    scene credits final at old_credits
    with Dissolve(1.0)
    pause 8.0

    scene black
    with Dissolve(1.0)

    pause 1.0

    return
