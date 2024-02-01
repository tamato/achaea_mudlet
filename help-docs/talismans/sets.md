# Talismans commands
- help talisman

TALISMAN INFO <piece name, ie deathcape>
TALISMAN SET <set name, death>

- help talismanmarket
TALISMAN MARKET SELL # <piece> <FROM promo|questin|foray|bashing> amount
snowballreform

# Breif Sets
Name: death
    Partial name: 
        death
    Description: 
        A set of talismans related to death.
    Talismans:
        a sycophantic shoulder cape (deathcape)
        a cowled practice dummy (deathdummy)
        a vulture's talon (vulturetalon)
        death's call (deathscall)
        a lichen-mottled gravestone (gravestone)
        a candle of cessation (deathcandle)
        a soulfire crucible (crucible)
        a spiralled loop of mortal coil (mortalcoil)

Name: wanderer
    Partial name: 
        wanderer
    Description: 
        A set of talismans memorialising Khalas, the Wanderer.
    Talismans:
        A slice of waybread. (waybread)
        A globe of the aimless. (aimlessglobe)
        A sheet of tattered parchment. (tatteredparchment)
        A starchart. (wandererstarchart)
        A Khalasian compass. (khalasiancompass)
        A featureless sculpture. (sculpture)
        A bloody knife. (bloodyknife)
        Some woven hand wraps. (handwraps)
        Robes of the wanderer. (wandererrobes)

CALL next attack from wrap gag
    - find everywhere that calls 'botter.checkForTargets'
    - event to raise 'continueBashing'

Remove all referenceds to 
  botter.triggers.recovered = tempTrigger("You have recovered equilibrium", botter.checkForTargets)
  disableTrigger(botter.triggers.recovered)

why does flinging priestess stop other things in the FREE queue?

