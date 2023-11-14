3.3 THE TELL & THINK COMMANDS

            | Saying things and                                 |
        3.2 < Talking to others               THE SHOUT COMMAND > 3.4

(See also: CONFIG NAMETELLS, CONFIG ALLOWTELLS, EXPRESSIVENESS)

Tells are a way to privately communicate with other online adventurers. To
speak to someone in this manner, the syntax is:

TELL <adventurer> <whatever>

For instance:

tell gawain Why don't Dwarven women shave more often? They really could use it.

TELL <adventurer> *<language> <message>
   - This will send a single tell in the specified language as long as you are
     able to speak it.

REPLY <message>
   - This will send a tell to the last person that sent you a tell.

RETELL/RT <message>
   - This will send a tell to the last person you sent a tell to.


Abbreviations OK
----------------
You may abbreviate tells by simply typing all or part of the adventurer's name,
followed by what you wish to tell them, assuming you have used CONFIG NAMETELLS
ON. For instance:

  gawa Why don't dwarven women shave more often? They really could use it.

Or, if you don't have CONFIG NAMETELLS ON, then you can abbreviate this way:

  tell gawa Why don't dwarven men bathe more often? They really could use it.


Abbreviations Could Mean Trouble
--------------------------------
What if you tried TELL CAIN Hello, but CAINE got the tell? Whoops! This can
happen, since abbreviations are possible, as noted above. There is a solution!
See the next section.


Forcing an exact match
----------------------
As a final option, if you use TELL <name> <message>, you may specify that the
name must match exactly, and that you are absolutely not abbreviating.
To do so - TELL <name>. <message>

For example:

  tell maya. This will go to Maya, but not Mayapple, no matter what!

Get it? Good!

Don't wish to receive tells at all? Type TELLSOFF. TELLSON to turn them back
on.


Altering How Your Tells Sound
-----------------------------
See HELP EXPRESSIVENESS to find out how you can use either emoticons or
free-form adverbs to change how your tells sound to other people.


Tell History
------------
You can check the history of tells that you have sent and received using the
TELLS command.  This will list a brief list of the last fifty tells. You
should use SHOWTELL (#) to see the full message of a specific tell.

You can search the TELLS history with TELLS <parameter>

You can also reverse the list by using TELLS R[EVERSE].

And search the reversed tells list with TELLS R <parameter>!

(See also: CONFIG NAMETELLS and CONFIG ALLOWTELLS)

Thinking
--------
Semi related to telepathic communication is the THINK command.

THINK <thoughts> and those who have a lock upon your mind, those who bear
the helm of telepathy in your location, and those of a Divine disposition
will be able to hear your thoughts.

You think in your racial language.

            | Saying things and                                 |
        3.2 < Talking to others               THE SHOUT COMMAND > 3.4

