4.6.1 Queueing

        4.6 < EQUILIBRIUM AND BALANCE                    TITLES > 4.7

Adventurers may have differing levels of latency (or lag), which has the
potential to affect the outcome of a battle. To combat this, Achaea has a
server-side queueing system that will automatically attempt to run a command
when you recover balance.


Automatic Queueing
------------------
When using automatic queueing, there are two types of queues, one for physical balance and one for
mental equilibrium. Items are added to this queue when they're attempted while off their respected 
balance. For example: You're hunting rats with your sword, and JAB RAT to attack it. If you 
attempted to JAB RAT while still off balance from the first attack, it'll be added to the queue and 
will run automatically when you regain balance next.

Queue-related commands:

CONFIG USEQUEUEING <ON|OFF>             - Enable or disable the queueing
                                          functionality.
CONFIG SHOWQUEUEALERTS <ON|OFF>         - Enable or disable the system messages
                                          regarding queueing.

Manual Queueing
---------------
Alternatively, you may manually insert items into your queue. Manually inserted items may use any
combination of the queue types available below.

Queue-related commands:

CLEARQUEUE <queue>                      - Clear one of your queues.
CLEARQUEUE ALL                          - Clear everything out of your queues.
QUEUE LIST                              - List your current queue.
QUEUE ADD <queue> <command>
                                        - Add an item to the end of one of your
                                          queues.
QUEUE ADDCLEAR <queue> <command>
                                        - Clear the specified queue and add an
                                          item to the fresh queue.
QUEUE ADDCLEARFULL <queue> <command>
                                        - Clear the whole queue and add an item
                                          to the fresh queue.
QUEUE INSERT <queue> <index> <command>
                                        - Add an item to a specific point in one
                                          of your queues.
QUEUE PREPEND <queue> <command>
                                        - Add an item to the start of one of
                                          your queues.
QUEUE REPLACE <queue> <index> <command>
                                        - Replace an item in one of your queues.
QUEUE REMOVE <index>
                                        - Remove an item from a queue.
QUEUE CLEAR <queue>
                                        - Same as CLEARQUEUE


Queue Limits and Specifics
--------------------------
Queued commands are limited to a maximum of ten across ALL QUEUE TYPES. This limit is not per-queue.
INSERTing or PREPENDing queue commands past your queue limit will remove the last queued command 
across all queues. ADDCLEAR will remove queued commands of the specified queue type, and if there is 
still not space in the queue, the command will fail. ADDCLEARFULL will remove all queued commands 
and then insert the new command at the beginning of your queue.


Simple Queue Types
------------------
Eq          = Equilibrium
Bal         = Balance
Eqbal       = Both eq and balance
Class       = Any of the various class balances
Ship        = Ship command balance
Para        = Not paralysed
Unbound     = Not bound
Stun        = Not stunned
Free        = Eqbal, unbound, not paralyzed, and not stunned
Freestand   = Free, plus standing
Full        = Freestand, plus class balance


Custom Queue Types
------------------
In addition to the simple queue types above, you may use fully custom queue types, mixing and
matching the following balances and statuses as you see fit.

e = Have equilibrium
b = Have balance
c = Have class balance
s = Have ship balance
p = Have paralysis
w = Are bound
u = Is upright (not prone)
t = Is stunned

To mix and match these queues, you can use any combination of these flags, or their inverse by
marking them with an exclamation point. For example:

QUEUE ADD c!p!tu <command>
Would execute when you had class balance, were not paralysed, were not stunned, and were standing.

QUEUE ADD eb!w!p!t <command>
Would add something to the FREE queue.

QUEUE ADD s <command>
Would add something to your ship queue.

