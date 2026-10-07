# ================================================================
# The Dandelion Girl: Don't You Remember Me?
# Image Definitions
# ================================================================


# ----------------------------------------------------------------
# TRANSFORMS
# ----------------------------------------------------------------

# Temporary transform for original 800x600 backgrounds.
#
# The remake runs at 1280x720 (16:9), while the original game
# ran at 800x600 (4:3).
#
# This enlarges the old background proportionally to 1280x960
# and centers it, allowing the top and bottom to be cropped.
#
# DO NOT use this on character sprites, logos, UI elements, etc.
#
# As backgrounds are replaced with native 1280x720 artwork,
# they will no longer need this transform.

transform old_bg:
    xysize (1280, 960)
    xalign 0.5
    yalign 0.5

# Temporary transform for original 800x600 fullscreen CGs.
# Preserves the original 4:3 aspect ratio while filling a 1280x720 screen.
#
# Like old_bg, this is temporary until CGs are replaced/reworked
# for the remake's native 16:9 resolution.

transform old_cg:
    xysize (1280, 960)
    xalign 0.5
    yalign 0.5

transform old_credits:
    xysize (1280, 960)
    xalign 0.5
    yalign 0.5



# ================================================================
# BACKGROUNDS
# ================================================================

# Opening sky / dandelion field
image bg sky = "bg/sky.png"

# Mark's office
image bg office = Transform(
    "bg/bg08.jpg",
    xysize=(1920, 1080)
)


# Mark and Anne's home
image bg mark_home = "bg/bg04.jpg"

# Vacation cabin
image bg cabin = "bg/bg04_05_new.png"

# Dandelion field
image bg dandelion_field = "bg/bg01.jpg"

# Dandelion field, second view
image bg dandelion_field_2 = Transform(
    "bg/dandelion_field_2.jpg",
    xysize=(1920, 1080)
)


## ====== ##
## OUTROS ##
## ====== ##

image outro_1a = "images/outros/outro_1_a.png"
image outro_1b = "images/outros/outro_1_b.png"



# ================================================================
# CHARACTER SPRITES
# ================================================================

# Julie — white outfit

image julie curious = "char/julie/sprite_white_talk_2-4.png"
image julie smile = "char/julie/sprite_white_talk_1-2.png"
image julie excited = "char/julie/sprite_white_talk_2-3.png"
image julie delighted = "char/julie/sprite_white_talk_2-9.png"
image julie horrified = "char/julie/sprite_white_talk_1-10.png"
image julie shudder = "char/julie/sprite_white_talk_1-6.png"
image julie relaxed = "char/julie/sprite_white_talk_2-2.png"
image julie animated = "char/julie/sprite_white_talk_2-3.png"
image julie coy = "char/julie/sprite_white_talk_2-6.png"
image julie giggle = "char/julie/sprite_white_talk_2-7.png"
image julie suspicious = "char/julie/sprite_white_talk_2-8.png"
image julie pout = "char/julie/sprite_white_talk_2-10.png"
image julie questioning = "char/julie/sprite_white_talk_1-7.png"
image julie surprised = "char/julie/sprite_white_talk_1-8.png"
image julie happy = "char/julie/sprite_white_talk_1-9.png"
image julie neutral = "char/julie/sprite_white_talk_1-1.png"


# Julie explaining her father / the future
image cg julie_explains = "cg/srsexpln.png"


# ================================================================
# JULIE — BLUE DRESS
# ================================================================

image julie blue_1 = "char/julie/sprite_blue_talk_2-1.png"
image julie blue_2 = "char/julie/sprite_blue_talk_2-2.png"
image julie blue_3 = "char/julie/sprite_blue_talk_2-3.png"
image julie blue_4 = "char/julie/sprite_blue_talk_2-4.png"
image julie blue_5 = "char/julie/sprite_blue_talk_2-5.png"
image julie blue_6 = "char/julie/sprite_blue_talk_2-6.png"
image julie blue_7 = "char/julie/sprite_blue_talk_2-7.png"
image julie blue_8 = "char/julie/sprite_blue_talk_2-8.png"
image julie blue_9 = "char/julie/sprite_blue_talk_2-9.png"
image julie blue_10 = "char/julie/sprite_blue_talk_2-10.png"

# Julie lying in the dandelion field
image cg julie_ponders_blue = "cg/CG_blue_1.png"


# Julie grieving / Mark comforting her
image cg julie_sobbing = "cg/sprite_black_hugz_1.png"

# Julie — black outfit
image julie black_4 = "char/julie/sprite_black_stand_3.png"
image julie black_5 = "char/julie/sprite_black_stand_4.png"
image julie black_6 = "char/julie/sprite_black_stand_5.png"

# ================================================================
# CGs
# ================================================================


image cg_julie_intro_1 = "cg/julie_intro_cg_1.png"
image cg_julie_intro_2 = "cg/julie_intro_cg_2.png"
image cg_julie_intro_2b = "cg/julie_intro_cg_2_b.png"


# Julie in the dandelion field
image cg julie_field = "cg/frame01.png"
image cg julie_field_2 = "cg/frame02.png"
image cg julie_pointing = "cg/sprite_point_2.png"

image cg julie_dancing = "cg/frame04.png"

# Julie explains her father's theory of time
image cg julie_ponders = "cg/CG_blue_0.png"

# ================================================================
# INTERSTITIALS / TITLE CARDS
# ================================================================

# Opening chapter transition
image interstitial 1 = "bg/inbetween1.png"
image interstitial 1b = "bg/inbetween1b.png"

image interstitial 2 = "bg/inbetween2.png"
image interstitial 2b = "bg/inbetween2b.png"


# ================================================================
# CHAPTER 2 — TIME PASSING / JULIE'S RETURN
# ================================================================

# Interstitial used after the Book of Time conversation.
# Note: ONScripter calls these inbetween_6/inbetween_6b,
# but the actual files are inbetween7a/7b.
image interstitial 6 = "bg/inbetween7a.png"
image interstitial 6b = "bg/inbetween7b.png"

# Sunset as Mark continues returning to the field
image bg sad_sunset = "bg/bg06.jpg"

# Field when Mark encounters Julie again
image bg sad_dandelion_field = "bg/sprite_black_bg_1.png"

# Julie's return
image cg sad_julie_standing = "cg/sprite_black_stand_1.png"

# ================================================================
# CHAPTER 2 — MARK'S HOME / ATTIC
# ================================================================

image bg home = "bg/bg05.jpg"
image bg rain = "bg/bg10.png"
image bg attic = "bg/attic.png"

# Next interstitial
image interstitial 5 = "bg/inbetween5.png"
image interstitial 5b = "bg/inbetween5b.png"

# ================================================================
# FINALE — WEDDING FLASHBACK
# ================================================================

image bg church_a = "bg/Church1.png"
image bg church_b = "bg/Church2.png"

image cg wedding = "cg/CG_Wedding_1.png"

# ================================================================
# FINALE — BUS STOP / ENDING
# ================================================================

image bg bus_stop_a = "bg/rain_1.png"
image bg bus_stop_b = "bg/rain_2.png"
image bg bus_stop_c = "bg/rain_3.png"
image bg bus_stop_d = "bg/rain_4.png"

image cg anne_runs_in_rain = "cg/CG_rain_5.png"
image cg anne_runs_in_rain_dark = "cg/CG_rain_5_dark.png"

# This is the same image used earlier for Julie's breakdown.
image cg julie_sobs = "cg/sprite_black_hugz_1.png"

image cg hugs_for_anne = "cg/04_sprite_01.jpg"
image cg julie_looks_up = "cg/cg_final_2.png"

# ================================================================
# CREDITS
# ================================================================

image credits 1 = "c/credits1.png"
image credits 2 = "c/credits2.png"
image credits 3 = "c/credits3.png"
image credits 4 = "c/credits4.png"
image credits 5 = "c/credits5.png"
image credits 6 = "c/credits6.png"
image credits 12 = "c/credits12.png"
image credits final = "c/finalcredit.png"
