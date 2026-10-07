define narrator = Character(None)
define mark = Character("Mark")
define girl = Character("Strange Girl")
define julie = Character("Julie")
define anne = Character("Anne")

define audio.curtain_fall = "bgm/curtain fall alt.mp3"
define audio.passing_time = "bgm/on the passing of time.mp3"
define audio.calm = "bgm/calm.mp3"
define audio.maid_with_the_flaxen_hair = "bgm/maidwiththeflaxenhair.ogg"
define audio.blue_feather = "bgm/bluefeather.mp3"
define audio.sad_slow = "bgm/sadslowcut.mp3"
define audio.moody_princess = "bgm/moody princess snip.mp3"


define sprite_dissolve = Dissolve(0.12)
define slow_sprite_dissolve = Dissolve(1.0)

define down_fade = ImageDissolve(
    Transform(
        "sys/fade_masks/down.jpg",
        xysize=(1920, 1080)
    ),
    2.5,
    ramplen=128
)

define corner_fade = ImageDissolve(
    Transform(
        "sys/fade_masks/top_right_corner_dissolve.jpg",
        xysize=(1920, 1080)
    ),
    2.5,
    ramplen=128
)

define cross_fade = ImageDissolve(
    Transform(
        "sys/fade_masks/x_mask.jpg",
        xysize=(1920, 1080)
    ),
    2.5,
    ramplen=128
)



## TRANSFORMS ##

transform gentle_shake:
    xoffset 0
    yoffset 0

    linear 0.05 xoffset -10 yoffset 3
    linear 0.05 xoffset 8 yoffset -5
    linear 0.05 xoffset -7 yoffset 5
    linear 0.05 xoffset 9 yoffset -3
    linear 0.05 xoffset -5 yoffset 2
    linear 0.05 xoffset 0 yoffset 0


## NEW OST ##

define audio.time_to_sleep = "bgm/time_to_sleep.mp3"
define audio.seasons = "bgm/seasons.mp3"
define audio.sunshine_doll = "bgm/sunshine_doll.mp3"
define audio.sweet_potato = "bgm/sweet_potato.mp3"

define audio.credits_fast = "bgm/creditsfast.mp3"
define audio.fall = "sfx/fall.wav"

define audio.dark_blue_night = "bgm/dark_blue_night.mp3"
define audio.dianthus = "bgm/dianthus.mp3"

define audio.cold_funk = "bgm/coldfunk.mp3"
define audio.sproing = "sfx/sproing.wav"
