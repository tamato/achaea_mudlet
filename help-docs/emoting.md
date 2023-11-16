3.6 Emoting and the EMOTE Command

        3.5 < THE ACHAEAN NEWS SYSTEM   Channels and using them > 3.7

(See also HELP EMOTIONS, HELP EMOTIONLIST, HELP EMOTICONS, HELP ALIASES)

Emoting is a way of making your adventurer act out whatever it is you wish,
from the possible to the ridiculous. Using the command is simple. Simply type:
EMOTE <whatever you wish to do>.


The Basics
----------
When you emote something, your name is prepended to your actions.

  If Shakti enters the text:    EMOTE gives a secretive smile
  then onlookers will see:      Shakti gives a secretive smile.

If you wish to use the possessive form of your name in an emote, simply type:
EMOTE 's <whatever you wish to come after>.

  So if Covenant enters:        EMOTE 's yodel echoes through the trees.
  Others will see:              Covenant's yodel echoes through the trees.

You can also prepend to an emote by enclosing the text in parenthesis.

  Tancred enters:               EMOTE (Stepping up to the podium,) begins to
                                recite an epic ballad.
  Others will see:              Stepping up to the podium, Tancred begins to
                                recite an epic ballad.


Says
----
Anything within quotations in a custom emote will colourise per your SAYS
config.


Interacting with Items
----------------------
Items can be included in your emotes by referencing them after an @ symbol.
This can be either the name, item number, or a combination of both.

Let's say that Maran is in a room with a statue of Deucalion, and wants to
reference it in his emote:

  Maran enters:                 EMOTE cleans some moss from @statue
  Others will see:              Maran cleans some moss from a statue of
                                Deucalion.


Interacting with Adventurers
----------------------------
Most emotes will involve other adventurers in some form, so other players
can be simply included with the use of the $ symbol before their name. You can
also directly reference yourself as $me.

  Gawain enters:                EMOTE glares at $harlequin, pure hatred
                                in his eyes
  Harlequin sees:               Gawain glares at you, pure hatred in his
                                eyes.
  Others will see:              Gawain glares at Harlequin, pure hatred in
                                his eyes.

Pronouns can also be added to further reference that player. Below is an
easy to follow table of the options available.

   Syntax                           What target sees   What others see
 +--------------------------------+------------------+-------------------+
 | $name (e.g. $Tecton)           | you              | Tecton            |
 | $name's                        | your             | Tecton's          |
 | $name_is                       | you're           | Tecton's          |
 | $name_he, $name_she            | you              | he/she/fae        |
 | $name_him                      | you              | him/her/faen      |
 | $name_himself, $name_herself   | yourself         | him/her/faenself  |
 | $name_his                      | your             | his/her/faes      |
 | $name_hiss, $name_hers         | yours            | his/hers/faes     |
 +--------------------------------+------------------+-------------------+

  Kaelin enters:                EMOTE grabs $roncli by the throat and roars
                                in $roncli_his face
  Roncli sees:                  Kaelin grabs you by the throat and roars in
                                your face.
  Others will see:              Kaelin grabs Roncli by the throat and roars
                                in his face.

All variables may be capitalised by adding a + symbol after the $ or @, so
$+Tecton_his will show Your to Tecton and His to everyone else.


Combining Actions with Custom Emotes
------------------------------------
Emotes may be combined with some common commands to truly customise many facets
of your character's actions. We currently offer this functionality to the
following verbs:

  DRINK        PUT
  DROP         REMOVE
  EAT(*)       SIT
  GIVE         STAND
  KNEEL        TAKE/GET
  LIE          WEAR

To include an emote with these commands, simply append your command with the :
symbol and then the emote you wish to show.

For many of the emotes, you'll need to include the @thing as a reference to the
item you're interacting with, and a reference to the person you're
also interacting with (if applicable). For get and put, where a container is
involved, you will also need to reference @container.

Let's say Yig has a quiver in his inventory named "a shoddy quiver".

  Yig enters:                   DROP QUIVER: (finding the workmanship
                                unacceptable,) drops @thing in disgust.
  Others will see:              Finding the workmanship unacceptable, Yig
                                drops a shoddy quiver in disgust.

(*) Note: As some food items have special reactions upon being eaten, custom
    emotes may not work on all foods.

For those with the SII (or SEEITEMINTERACTIONS) config option enabled, you'll
see a summary of the action following the emote.


Putting Everything Together
---------------------------
We've just provided basic examples of each possibility so far, but the true
power in emoting is the ability to combine everything together! For example:

  EMOTE (Turning $me_his head to the skies,) starts rambling aimlessly to
  $tecton about the complexities of nature and the universe. $+me_he begins
  to gesticulate wildly and accidentally strikes $sarapis in the face; $me
  turns red and stammers out a profuse apology.

or

  GET HAT FROM CHEST: (Reaching into @container and rummaging around,) pulls
  out @thing and begins to press out the creases with $me_his hands. @+thing
  releases a cloud of dust and dirt into the air at the rough treatment,
  making $me_him cough.


Emoting and Player-vs-Player Combat
-----------------------------------
Custom emotes are intended for ways to express yourself. They are not to be
used in combat and are not an alternative to the various illusion type skills.
Use of emotes for combat messages, or to obfuscate offensive or defensive
actions is not allowed. Should you encounter any abuse of this system, please
file an ISSUE and let us know.


Customisation
-------------
If the $ and @ characters are used by your client, or simply inconvenient, you
can choose different ones by typing CONFIG EMOTING. You can choose any
non-alphanumeric character to identify players or things, but you must have
different symbols for players and things.

        3.5 < THE ACHAEAN NEWS SYSTEM   Channels and using them > 3.7
