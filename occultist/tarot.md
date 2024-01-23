announce 5452 is in 898, 09/28/2022
announce 5460 is in 900, 10/17/2022
doesn't seem to be mentioned in this range.

CLASSLEADS NEWS #108                                    (10/12/2022 at 00:51)
Occultism
---------
* ENLIGHTEN conditions moved from 5 afflictions to 6 normally, and from 4 with whisperingmadness to 5 with whisperingmadness.
* INSTILL now does 3% hp/mana damage. This is raised to 6% if you hold a Glaaki derived truename (corpse ones do not do this).
* WHISPERINGMADNESS no longer gives a focus affliction when you focus. It is just a focus balance extender now.
* BODYWARP has been expanded significantly. See the abfile for details.
* AGUE now freezes twice if a target has more than one restoration broken limb.
* New ability: REGRESS.
* New ability: COMPEL.
* new ability: INTERLINK.
* ENLIGHTEN now credits the occultist with the kill when they die to alternative sources.


Abilities in Tarot:
-------------------------------------------------------------------------------
Inscribing           The ability to inscribe images upon blank Tarot cards.
Sun                  Create a portable light source.
Cardpacks            Use the handy cardpacks for easier storage.
Emperor              Create the compulsion in others to follow you.
Magician             Replenish your mana with the might of the Magician.
Priestess            Heal yourself with the benevolence of the Priestess.
Fool                 Shrug off afflictions with blind courage.
Chariot              Create an infernal chariot to ride.
Hermit               Teleport to an uninhabited location.
Empress              Summon your friends to you.
Lovers               Create a strong love for you in your target.
Hangedman            Hinder your opponent with a mass of ropes.
Tower                Cause a crumbling tower to appear in your location.
Wheel                Spin the wheel and take your chances.
Creator              Create an illusion in an adjacent room.
Justice              Bring justice to the unjust.
Star                 Strike down a foe with a flaming meteor.
Aeon                 Curse your foe with the mark of Chronos.
Lust                 Cause an opponent to hopelessly lust after you.
Universe             Transport yourself around the land.
Devil                Call a Devil to serve you, though no more than once.
Moon                 Bestow the maladies of the moon upon your enemy.
Death                Call down Death itself to claim the soul of your enemy.

Occultist specific Specialisation: 
Heretic              Raised from Ruin.
Ruinate              Two sides of the same coin.

-------------------------------------------------------------------------------
To gain further information on an ability, AB <ability>.


Inscribing (Tarot)                            Known: Yes
-------------------------------------------------------------------------------
Syntax:            INSCRIBE BLANK WITH [1-20] <IMAGE>
Resource:          10 mana
Details:
With this ability, you may inscribe blank tarot cards with the various images of the Major Arcana.
-------------------------------------------------------------------------------

Sun (Tarot)                                   Known: Yes
-------------------------------------------------------------------------------
Syntax:            FLING SUN AT GROUND
Works on/against:  Room
Cooldown:          3.00 seconds of balance
Details:
This Tarot will create a small ball of light to illuminate your
surroundings.

In addition, for as long as the globe of light remains at your location,
it shall periodically heal you of afflictions.

-------------------------------------------------------------------------------


Cardpacks (Tarot)                             Known: Yes
-------------------------------------------------------------------------------
Syntax:            IND [number|ALL] <card>
                   OUTD [ALL|number] <card>
                   DECKLIST
Details:
Cardpacks is the ability to store and retrieve tarot cards using a tarot deck. You may store up to
5000 of each card type. This ability requires that you have a tarot deck in your inventory.
-------------------------------------------------------------------------------


Emperor (Tarot)                               Known: Yes
-------------------------------------------------------------------------------
Syntax:            FLING EMPEROR AT <target>
Works on/against:  Adventurers
Cooldown:          3.00 seconds of balance
Details:
The Emperor is a symbol of leadership and power. With this card, you
will force other adventurers to recognise your leadership and follow
you.
-------------------------------------------------------------------------------


Magician (Tarot)                              Known: Yes
-------------------------------------------------------------------------------
Syntax:            FLING MAGICIAN AT <target>
Works on/against:  Adventurers
Cooldown:          3.00 seconds of balance
Details:
The Magician represents the power of magic and the power of the mind. This card will replenish the mana of the adventurer it is thrown at.

-------------------------------------------------------------------------------


Priestess (Tarot)                             Known: Yes
-------------------------------------------------------------------------------
Syntax:            FLING PRIESTESS AT <target>
Works on/against:  Adventurers
Cooldown:          3.00 seconds of balance
Details:
The Priestess represents benevolent healing. Flinging this card at an adventurer will heal some of
his health.

-------------------------------------------------------------------------------


Fool (Tarot)                                  Known: Yes
-------------------------------------------------------------------------------
Syntax:            FLING FOOL AT <target>
Works on/against:  Adventurers
Cooldown:          3.00 seconds of balance
Details:
The Fool is pictured as being immune to fear and full of courage. With
this Tarot you may throw off three afflictions by denying their
existence. You must wait a time(*) before the Fool will attend you
again.

* 35 second cooldown.

-------------------------------------------------------------------------------


Chariot (Tarot)                               Known: Yes
-------------------------------------------------------------------------------
Syntax:            FLING CHARIOT AT GROUND
                   BOARD CHARIOT
                   SPUR CHARIOT SKYWARDS
                   LAND
                   DISMOUNT
Cooldown:          3.00 seconds of balance
Details:
The Chariot will create an infernal chariot upon which you may ride. It has the ability to fly also.
BOARD CHARIOT will board your chariot. SPUR CHARIOT SKYWARDS will drive it up to the sky. LAND will 
bring you back down again. While in the Chariot, you may move about using the usual commands. Be 
warned: flinging cards at the ground while flying is a useless endeavour.

-------------------------------------------------------------------------------


Hermit (Tarot)                                Known: Yes
-------------------------------------------------------------------------------
Syntax:            ACTIVATE HERMIT [tag]
                   FLING HERMIT AT GROUND [tag]
                   SNIFF HERMIT
                   HERMITS
Extra Information: Activation: 2.00 seconds of equilibrium.

Cooldown:          3.00 seconds of balance
Details:
The Hermit is a solitary person. When you activate the hermit card, it will remember the location at
which you activated it. Then, when you fling it, you will be transported to that location, provided 
there are no adventurers in that location at the time. SNIFF HERMIT will tell you the name of the 
location at which the hermit was activated.

- TODO: Can Hermit be used off eq?
- TODO: can Istria be used when off balance?

-------------------------------------------------------------------------------


Empress (Tarot)                               Known: Yes
-------------------------------------------------------------------------------
Syntax:            FLING EMPRESS AT <target>
                   SNIFF EMPRESS <target>
Works on/against:  Adventurers
Cooldown:          3.00 seconds of balance
Details:
With this ability, you may summon someone from anywhere within the local area, provided you are on his or her allies list. If you have forced yourself onto that list via the Lust tarot, then you will be able to summon that person from anywhere on the continent.

You may also SNIFF a card inscribed with this image to determine if you have someone lusted.

-------------------------------------------------------------------------------

Lovers (Tarot)                                Known: Yes
-------------------------------------------------------------------------------
Syntax:            FLING LOVERS AT <target>
Works on/against:  Adventurers
Cooldown:          3.00 seconds of balance
Details:
The Lovers tarot will inspire your target to fall deeply in love with you. While in love with you, he or she will be generally unwilling to cause you harm.

When ruinated, the lovers become the betrayer. It shall inflict manaleech when flung.

-------------------------------------------------------------------------------


Hangedman (Tarot)                             Known: Yes
-------------------------------------------------------------------------------
Syntax:            FLING HANGEDMAN AT <target>
Works on/against:  Adventurers
Cooldown:          3.00 seconds of balance
Details:
The Hangedman will entangle your foe in a mass of ropes.

-------------------------------------------------------------------------------


Tower (Tarot)                                 Known: Yes
-------------------------------------------------------------------------------
Syntax:            FLING TOWER AT GROUND
Works on/against:  Room
Cooldown:          3.00 seconds of balance
Details:
The Tower card will cause a crumbling tower to appear in your location, which will then collapse,
making it difficult to leave via some of the exits.

-------------------------------------------------------------------------------


**RUINATE** Wheel (Tarot)                                 Known: Yes
-------------------------------------------------------------------------------
Syntax:            **RUINATE** WHEEL AT GROUND
Works on/against:  **Everyone** in the Room
Cooldown:          3.00 seconds of balance
Details:
The Wheel of Fortune is mysterious and represents luck, neither good nor bad. Sometimes it will bring good things, sometimes bad. The effects of this card are permanent, except those affecting adventurer statistics.

Use of this card which affects anyone unwillingly could result in very serious repercussions.

Between each turn, and to the start of the first, 7 seconds, 4 seconds after fling.
Then each of these, in this order, each after 7 seconds.

Cold Blue - seems to be shiver/cold
- Rays of cold blue light lash out from the Wheel of Chaos, irradiating the location.
- shiver cured by: APPLY caloric

Vibrant indigo - stupidity
- Vibrant indigo rays of light lash out from the Wheel of Chaos
- Stupidity: cured by EAT Goldenseal/Plumbum

Violet - aeon
- Rays of violet light lash out at the location from the Wheel of Chaos.
- Use PinchAura to remove Speed defence ~26 seconds in for Aeon to land.
 - PinchAura's messae is hidden from the target.
- Aeon: 
 - cured by SMOKE ELM/Cinnabar
 - This is the only affliction cured with smoking Elm. e.g. Stacking smoking aff's don't mean anythng.
  - need to stack things that block asthma.


PREREQ - Devil
Fling/Ruinate wheel
- (shiver timer)    then temptimer( 7, interlink shiver); DOMINATE use with hecate to ruin limbs (apply mending)
- (stupidity timer) then temptimer(14, ); DOMINATE 
- (aeon timer)      then tmeptimer(20, tarot aeon); DOMINATE (weariness) command hound at <tar>
 - curing system seems to prefer smoking to cure SLICKNESS, smoking is needed to cure AEON.
 - SMOKING AFF
    - Aeon,             elm/cinnabar
    - Disfigurement,    valerian/realgar
    - Mana Leech,       valerian/realgar
    - Slickness,        valerian/realgar

shiver
end time:   23:17:57.77
start time: 23:17:44.48


aeon time:  23:10:30.90
start time: 23:10:01.58


-------------------------------------------------------------------------------


Creator (Tarot)                               Known: Yes
-------------------------------------------------------------------------------
Syntax:            FLING CREATOR <direction> [LETHAL] <illusion text>
Works on/against:  Room
Cooldown:          3.00 seconds of balance
Details:
This Tarot card will allow you to create an illusion of your choosing in an adjacent location. You may embed a single newline by including the characters \n at the appropriate spot. For limitations and restrictions, please refer to HELP ILLUSIONS.

-------------------------------------------------------------------------------


Justice (Tarot)                               Known: Yes
-------------------------------------------------------------------------------
Syntax:            FLING JUSTICE AT <target>
Works on/against:  Adventurers
Cooldown:          3.00 seconds of balance
Details:
The Justice tarot will bring the wrath of Miramar, the Even-Handed, down upon your foe.

When ruinated, the justice becomes tyranny. It will convert the following afflictions into broken limbs: 
    paralysis       instill, nin'kharsag, chaosrays, 
    sensitivity     instill
    healthleech,    instill
    haemophilia,    scrag
    weariness,      lycantha
    asthma,         instill, 
    clumsiness.     instill

If five or more afflictions are converted, the target is frozen; this ability will also prone your target if both of their legs are broken when it resolves.

- A reason to use this card/ability is to stack on Devil

-------------------------------------------------------------------------------


Star (Tarot)                                  Known: Yes
-------------------------------------------------------------------------------
Syntax:            FLING STAR AT <target>
Works on/against:  Adventurers
Cooldown:          3.00 seconds of balance
Details:
The Star tarot will bring down a flaming meteor upon your unlucky foe's
head. Your foe must be within three rooms of your line of sight and both
you and he must be outdoors.

-------------------------------------------------------------------------------


Aeon (Tarot)                                  Known: No (138 lessons required)
-------------------------------------------------------------------------------
Syntax:            FLING AEON AT <target>
Works on/against:  Adventurers
Cooldown:          3.70 seconds of balance
Details:
The Aeon tarot will give the curse of Chronos the Eternal to an adventurer, slowing his passage through time.

- It seems to take 2 seconds for Aeon to "hit"
- need to get a log of this.
 - Aeon used time:
 - Slows down message:
 - Cure message:
 - TODO Add this all to wheel too.

-------------------------------------------------------------------------------


Lust (Tarot)                                  Known: No (276 lessons required)
-------------------------------------------------------------------------------
Syntax:            FLING LUST AT <target>
Works on/against:  Adventurers
Cooldown:          3.00 seconds of balance
Details:
With this Tarot, you may instill a lust for you in another adventurer, so that he or she will consider you an ally.

- <> quickly flings a tarot card at you, and you feel unreasonable lust for <>.

-------------------------------------------------------------------------------


Universe (Tarot)                              Known: No (379 lessons required)
-------------------------------------------------------------------------------
Syntax:            FLING UNIVERSE AT GROUND
                   UNIVERSE LIST
                   TOUCH <location>
Cooldown:          3.00 seconds of balance
Details:
The Universe tarot will allow you to quickly travel throughout Achaea, with instant transport to a number of locations on the mainland of Sapience and continent of Meropis.

-------------------------------------------------------------------------------


Devil (Tarot)                                 Known: No (517 lessons required)
-------------------------------------------------------------------------------
Syntax:            FLING DEVIL AT GROUND
                   SUPPRESS DEVIL
Cooldown:          3.00 seconds of balance
Details:
The Devil is a rather unique card. When you fling it at the ground, a Devil will be called up, who will serve you once, and only once. He will possess your body and, the next Tarot card you fling, he will cause you to immediately fling another one of six random tarot cards.

Does not use up entity balance
The 6 are: 
    Aeon
    HangedMan
    Justice
    Lover
    Lust
    Moon

-------------------------------------------------------------------------------


Moon (Tarot)                                  Known: No (586 lessons required)
-------------------------------------------------------------------------------
Syntax:            FLING MOON AT <target> [affliction]
Extra Information: Specified affliction cooldown: 2.10 seconds of balance (at transcendent Tarot).

Works on/against:  Adventurers
Cooldown:          3.00 seconds of balance
Details:
The moon tarot will give your enemy maladies associated with the mind.
The affliction will be random if unspecified, and hidden from the
victim. If you specify an affliction, the ability is faster to recover
from, but the victim shall see what was delivered. 
You may pick from:          Cures
    stupidity,          | eat goldenseal/plumbum
    masochism,          | eat lobelia/argentum (same with wmad)
    hallucinations,     | eat ash/stannum
    hypersomnia,        | eat ash/stannum
    confusion,          | eat ash/stannum
    epilepsy,           | eat goldenseal/plumbum
    claustrophobia,     | eat lobelia/argentum (wmad)
    agoraphobia.        | eat lobelia/argentum (wmad)

-------------------------------------------------------------------------------


Death (Tarot)                                 Known: No (828 lessons required)
-------------------------------------------------------------------------------
Syntax:            RUB DEATH ON <target>
                   SNIFF DEATH
                   FLING DEATH AT <target>
Extra Information: Rub: 3.20 seconds of equilibrium.

Works on/against:  Adventurers
Cooldown:          3.00 seconds of balance
Details:
To attune Death, you must first rub it on your enemy seven times.

Sniffing the card will tell you how many times you have rubbed it on
your foul oppressor, while flinging it will begin the process of calling
Death himself to gather the soul of your enemy to him. Be warned though
that this process takes concentration and you may not do anything else
while Death is on his way.

When rubbing Death, normally your card will only gain one charge towards
attunement. However, the number of charges generated for each rub will
be increased for each of a set of conditions that are true(*).

Finally, rubbing death on your target will attempt to freeze that
adventurer, though can only ever make them shiver at worst.

* Death rubs are increased for each of: stun, aeon, entangled,
shivering, or paralysed.

-------------------------------------------------------------------------------


Heretic (Tarot)                               Known: Yes
-------------------------------------------------------------------------------
Syntax:            RUINATE HERETIC AT <target>
                   ORDER <target> WITNESS <vision>
Details:
When mysterious forces attempted to gain influence over the Occultists
of Ashtan in the 899th year after the fall of the Seleucarian Empire, a
group of ritualists did the unthinkable and irrevocably damaged the
symbolic nature of their Hierophant. Though it no longer holds any power
in the hands of Occultists, out of their machinations was born a new
card entirely: the first example of a nontransient ruinated image, that
of the Heretic.

When a victim falls under the Heretic's sway, the Occultist may command
them to witness an image: and so long as they are not blind, they will
be unable to avoid gazing upon that which is brought forth.

-------------------------------------------------------------------------------


Ruinate (Tarot)                               Known: No (690 lessons required)
-------------------------------------------------------------------------------
Syntax:            RUINATE <card> at <target>
Details:
So few truly understand the duality inherent in the nature of Chaos.
With a minor application of your recondite knowledge, twist one of the
major arcana just so to display its opposite face.

Currently, the 
    lovers  - manaleech
    justice - tyranny (converst phys afflictions to broken limbs, APPLY) from EAT to APPLY
    creator - death, but quicker and with restrictions
    wheel   - reduced chaosrays,  aeon(violet), stupidity(indigo)

cards may be ruinated. See their ability files for details.

-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
Syntax:            FLING CREATOR <direction> [LETHAL] <illusion text>
Works on/against:  Room
Cooldown:          3.00 seconds of balance
Details:
This Tarot card will allow you to create an illusion of your choosing in an adjacent location. You
may embed a single newline by including the characters \n at the appropriate spot. For limitations 
and restrictions, please refer to HELP ILLUSIONS.

When ruinated, the Creator becomes the Destroyer. This manifestation of
destruction requires a fully charged Death card to invoke, and that
Death card will also be consumed in the process. You may only fling the
Destroyer at a target who is both blacked out and shivering; but when
you do, they will be slain shortly there after(*).

* This is a channel similar to death tarot, but resolves faster when the
additional conditions are met.

-------------------------------------------------------------------------------



