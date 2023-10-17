Ratting script
----------------

Print GMCP to console in Mudlet

Find exits
- gmcp:  GMCP.Room.Info.exits
- ignore: up, down, in, and out
    - There is a door in the way, to the <>.
- Check for 

Get denizens
- gmcp: 
    - gmcp.Char.Items.Remove.item.id (just an id can be used for targets)
    - gmcp.Char.Items.Add.item.id 
    - gmcp.Char.Items.Add.item.name -- "a rat", "a baby rat"
    - gmcp.Char.Items.List.items[*].id/name
    - displayed name is the last word in 'name' with its 'id' appended.

- "baby rats" can be kicked
- "young rats" take 3 or so kicks
- "You have slain ..."

- Warning, remote target
    A <> wanders back into its warren where you may not follow

-- targets
local targets = {'a.\*rat$'}

-- list of exits
local prohibited_exits = {'up', 'down', 'in', 'out'}
prohibited_rooms = prohibited_rooms or {} -- add id for Gates of Ashtan

for dir,id in pairs(GMCP.Room.Info.exits) do
    if dir in prohibited_exits then
        if id in prohibited_rooms then
            continue
        continue
    end

    -- check balances
    -- have it runing the whole time
    enableTrigger("CheckBlocked") 
        -- possibly adds id to prohibited_rooms
        -- restarts this script on failure
    break
end

send(dir)

## GMCP
{
    Char = {  
      Afflictions = {  
        List = {}  
      },  
      Defences = {  
        Add = {  
          desc = "This tattoo will passively regenerate your health.",  
          name = "boartattoo"  
        },  
        InfoList = { {  
            category = "general",  
            color = "green",  
            desc = "",  
            icon = "eye-slash",  
            important = "1",  
            name = "blindness"  
          }, {  
            category = "general",  
            color = "green",  
            desc = "",  
            icon = "ear-deaf",  
            important = "1",  
            name = "deafness"  
          }, {  
            category = "general",  
            color = "purple",  
            desc = "",  
            icon = "podcast",  
            important = "1",  
            name = "mindseye"  
          }, {  
            category = "general",  
            color = "yellow",  
            desc = "",  
            icon = "eye",  
            important = "1",  
            name = "thirdeye"  
          }, {  
            category = "general",  
            color = "purple",  
            desc = "",  
            icon = "skull",  
            important = "1",  
            name = "deathsight"  
          }, {  
            category = "general",  
            color = "purple",  
            desc = "",  
            icon = "circle-half-stroke",  
            important = "1",  
            name = "fangbarrier"  
          }, {  
            category = "general",  
            color = "blue",  
            desc = "",  
            icon = "snooze",  
            important = "1",  
            name = "insomnia"  
          }, {  
            category = "general",  
            color = "pink",  
            desc = "",  
            icon = "heart-pulse",  
            important = "1",  
            name = "kola"  
          }, {  
            category = "general",  
            color = "#aaaaff",  
            desc = "",  
            icon = "bolt",  
            important = "1",  
            name = "metawake"  
          }, {  
            category = "general",  
            color = "yellow",  
            desc = "",  
            icon = "skull-cow",  
            important = "1",  
            name = "boartattoo"  
          }, {  
            category = "general",  
            color = "#ffff80",  
            desc = "",  
            icon = "moon",  
            important = "1",  
            name = "moontattoo"  
          }, {  
            category = "general",  
            color = "white",  
            desc = "",  
            icon = "hood-cloak",  
            important = "1",  
            name = "cloak"  
          }, {  
            category = "general",  
            color = "purple",  
            desc = "",  
            icon = "circle-dot",  
            important = "1",  
            name = "rebounding"  
          }, {  
            category = "general",  
            color = "blue",  
            desc = "",  
            icon = "weight-hanging",  
            important = "1",  
            name = "density"  
          }, {  
            category = "general",  
            color = "#9a679a",  
            desc = "",  
            icon = "cloud",  
            important = "1",  
            name = "softfocusing"  
          } },  
        List = {}  
      },  
      Items = {  
        List = {  
          items = { {  
              attrib = "m",  
              icon = "animal",  
              id = "19316",  
              name = "a guard pig"  
            } },  
          location = "room"  
        }  
      },  
      Name = {  
        fullname = "Uaithne Varik",  
        name = "Varik"  
      },  
      Skills = {  
        Groups = { {  
            name = "Vision",  
            rank = "Inept"  
          }, {  
            name = "Avoidance",  
            rank = "Inept"  
          }, {  
            name = "Tattoos",  
            rank = "Inept"  
          }, {  
            name = "Survival",  
            rank = "Skilled"  
          }, {  
            name = "Weaponry",  
            rank = "Skilled"  
          }, {  
            name = "Riding",  
            rank = "Inept"  
          }, {  
            name = "Attainment",  
            rank = "Skilled"  
          }, {  
            name = "Aeonics",  
            rank = "Inept"  
          }, {  
            name = "Shadowmancy",  
            rank = "Apprentice"  
          }, {  
            name = "Constitution",  
            rank = "Inept"  
          }, {  
            name = "Thermology",  
            rank = "Inept"  
          }, {  
            name = "Frost",  
            rank = "Inept"  
          }, {  
            name = "Antidotes",  
            rank = "Inept"  
          }, {  
            name = "Fitness",  
            rank = "Inept"  
          }, {  
            name = "Galvanism",  
            rank = "Inept"  
          }, {  
            name = "Philosophy",  
            rank = "Inept"  
          } }  
      },  
      Status = {  
        age = "18",  
        bank = "3011",  
        boundcredits = "18",  
        boundmayancrowns = "0",  
        city = "Eleusis (1)",  
        class = "Depthswalker",  
        explorerrank = "a Sightseer",  
        fullname = "Uaithne Varik",  
        gender = "male",  
        gold = "2304",  
        house = "(None)",  
        lessons = "225",  
        level = "16 (9%)",  
        mayancrowns = "0",  
        name = "Varik",  
        order = "(None)",  
        race = "Human",  
        specialisation = "",  
        target = "None",  
        unboundcredits = "0",  
        unread_msgs = "0",  
        unread_news = "43801",  
        xp = "9%",  
        xprank = "0"  
      },  
      StatusVars = {  
        age = "Age",  
        bank = "Bank",  
        boundcredits = "Bound Credits",  
        boundmayancrowns = "Bound Mayan Crowns",  
        city = "City",  
        class = "Class",  
        explorerrank = "Explorer Rank",  
        fullname = "Full Name",  
        gender = "Gender",  
        gold = "Gold",  
        house = "House",  
        lessons = "Lessons",  
        level = "Experience Level",  
        mayancrowns = "Unbound Mayan Crowns",  
        name = "Name",  
        order = "Order",  
        race = "Race",  
        specialisation = "Race Specialisation",  
        target = "Target",  
        unboundcredits = "Unbound Credits",  
        unread_msgs = "Unread Messages",  
        unread_news = "Unread News",  
        xp = "Experience To Next Level",  
        xprank = "Achaean XP Rank"  
      },  
      Vitals = {  
        bal = "1",  
        charstats = { "Bleed: 0", "Rage: 0", "Word: Yes", "Age: 0" },  
        ep = "3600",  
        eq = "1",  
        hp = "1100",  
        maxep = "3600",  
        maxhp = "1100",  
        maxmp = "1100",  
        maxwp = "3600",  
        mp = "850",  
        nl = "9",  
        string = "H:1100/1100 M:850/1100 E:3600/3600 W:3600/3600 NL:9/100 ",  
        wp = "3600"  
      }  
    },  
    Client = {  
      Map = {  
        url = "http://www.achaea.com/maps/map.xml"  
      }  
    },  
    External = {  
      Discord = {  
        Info = {  
          applicationid = "497629003130208267",  
          inviteurl = "https://discord.gg/achaea"  
        },  
        Status = {  
          details = "www.achaea.com",  
          game = "Achaea",  
          partymax = 0,  
          partysize = 0,  
          smallimage = { "sword" },  
          smallimagetext = "Level 16",  
          starttime = "0",  
          state = "Varik"  
        }  
      }  
    },  
    Room = {  
      Info = {  
        area = "the Valley of Lodi",  
        coords = "9,0,0,0",  
        desc = "A large ornate piece of metal has been mounted upon two thick tree stumps which grow   
  directly from the earth. Lattices and budding flowers have been permanently etched into heated   
  metal and then cooled. A bed of red and white flowers surrounds each stump. A small yet steady   
  stream of pedestrian traffic enters the hamlet from a winding road and heads to Inventor's Square,   
  weaving around the gates.",  
        details = {},  
        environment = "Path",  
        exits = {  
          n = 3884,  
          s = 6224  
        },  
        map = "www.achaea.com/irex/maps/clientmap.php?map=9&building=0&level=0 6 16",  
        name = "North gate (road)",  
        num = 6181  
      },  
      Players = { {  
          fullname = "Uaithne Varik",  
          name = "Varik"  
        } }  
    }  
  }





