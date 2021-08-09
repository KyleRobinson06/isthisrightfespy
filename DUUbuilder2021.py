import random
teams=[]
x=0

while len(teams)<10: # Number of teams to generate
    plusone = ["Grimmsnarl",
               "Hitmontop",
               "Indeedee",
               "Scrafty",
               "Weavile",
               "Wartortle"]
    legends = ["Regigigas",
                "Cresselia",
                "Victini",
                "Latias",
                "Latios",
                "Zarude",
                "Glastrier",
                "Moltres-G",
                "Regidrago",
                "Spectrier",
                "Tornadus",
                "Articuno-G",
                "Entei",
                "Keldeo",
                "Moltres",
                "Raikou",
                "Registeel",
                "Suicune",
                "Terrakion",
                "Thundurus",
                "Thundurus-T",
                "Celesteela",
                "Tapu Bulu",
                "Blacephalon",
                "Buzzwole",
                "Pheromosa",
                "Xurkitree",
                "Naganadel",
                "Kyurem",
                "Regirock"]
    team=[]
    
    while len(team)<1:
        teammate = random.choice(plusone)
        team.append(teammate)
        plusone.remove(teammate)
        
    while len(team)<6:
        teammate = random.choice(legends)
        team.append(teammate)
        legends.remove(teammate)

    team=sorted(team)

    fireweak=0
    waterweak=0
    grassweak=0
    electricweak=0
    iceweak=0
    fightingweak=0
    poisonweak=0
    groundweak=0
    flyingweak=0
    psychicweak=0
    bugweak=0
    rockweak=0
    ghostweak=0
    darkweak=0
    dragonweak=0
    steelweak=0
    fairyweak=0
    speedcontrol= False
    phaze=False
    spreadspecial=False
    spreadphysical=False
    firemove=False
    grassmove=False

    #WEAKNESS COUNTER
    if "Grimmsnarl" in team:
        fairyweak=fairyweak+1
        poisonweak=poisonweak+1
        steelweak=steelweak+1
    if "Hitmontop" in team:
        fairyweak=fairyweak+1
        flyingweak=flyingweak+1
        psychicweak=psychicweak+1
    if "Indeedee" in team:
        bugweak=bugweak+1
        darkweak=darkweak+1
        spreadspecial=True
    if "Scrafty" in team:
        fairyweak=fairyweak+1
        flyingweak=flyingweak+1
        fightingweak=fightingweak+1
    if "Weavile" in team:
        bugweak=bugweak+1
        fairyweak=fairyweak+1
        fightingweak=fightingweak+1
        fireweak=fireweak+1
        rockweak=rockweak+1
        steelweak=steelweak+1
    if "Wartortle" in team:
        electricweak=electricweak+1
        grassweak=grassweak+1
    if "Regigigas" in team:
        fightingweak=fightingweak+1
    if "Cresselia" in team:
        bugweak=bugweak+1
        darkweak=darkweak+1
        ghostweak=ghostweak+1
        speedcontrol=True
    if "Victini" in team:
        darkweak=darkweak+1
        ghostweak=ghostweak+1       
        groundweak=groundweak+1
        rockweak=rockweak+1
        waterweak=waterweak+1
        firemove=True
    if "Latias" in team:
        bugweak=bugweak+1
        darkweak=darkweak+1
        dragonweak=dragonweak+1
        fairyweak=fairyweak+1
        ghostweak=ghostweak+1       
        iceweak=iceweak+1
        speedcontrol=True       
    if "Latios" in team:
        bugweak=bugweak+1
        darkweak=darkweak+1
        dragonweak=dragonweak+1
        fairyweak=fairyweak+1
        ghostweak=ghostweak+1       
        iceweak=iceweak+1
        speedcontrol=True
    if "Zarude" in team:
        bugweak=bugweak+1
        fairyweak=fairyweak+1
        fightingweak=fightingweak+1
        fireweak=fireweak+1
        flyingweak=flyingweak+1
        iceweak=iceweak+1
        poisonweak=poisonweak+1
        grassmove=True
    if "Glastrier" in team:
        fightingweak=fightingweak+1
        fireweak=fireweak+1
        rockweak=rockweak+1
        steelweak=steelweak+1
        if "Cresselia" not in team:
            team.clear()
            x=x+1
            continue
    if "Moltres-G" in team:
        electricweak=electricweak+1
        fairyweak=fairyweak+1
        iceweak=iceweak+1
        rockweak=rockweak+1
        phaze=True
        spreadspecial=True
    if "Regidrago" in team:
        dragonweak=dragonweak+1
        fairyweak=fairyweak+1
        iceweak=iceweak+1
        spreadspecial=True
    if "Spectrier" in team:
        darkweak=darkweak+1
        ghostweak=ghostweak+1
        phaze=True
    if "Tornadus" in team:
        electricweak=electricweak+1
        iceweak=iceweak+1
        rockweak=rockweak+1
        speedcontrol=True
        phaze=True
    if "Articuno-G" in team:
        darkweak=darkweak+1
        electricweak=electricweak+1
        ghostweak=ghostweak+1
        iceweak=iceweak+1
        rock=rockweak+1
        speedcontrol=True
    if "Entei" in team:
        groundweak=groundweak+1
        rockweak=rockweak+1
        waterweak=waterweak+1
        firemove=True
    if "Keldeo" in team:
        electricweak=electricweak+1
        fairyweak=fairyweak+1
        flyingweak=flyingweak+1
        grassweak=grassweak+1
        psychicweak=psychicweak+1
        phaze=True
    if "Moltres" in team:
        electricweak=electricweak+1
        waterweak=waterweak+1
        rockweak=rockweak+1
        speedcontrol=True
        spreadspecial=True
    if "Raikou" in team:
        groundweak=groundweak+1
    if "Registeel" in team:
        fightingweak=fightingweak+1
        fireweak=fireweak+1
        groundweak=groundweak+1
    if "Suicune" in team:
        electricweak=electricweak+1
        grassweak=grassweak+1
        speedcontrol=True
    if "Terrakion" in team:
        fairyweak=fairyweak+1
        fightingweak=fightingweak+1
        grassweak=grassweak+1
        groundweak=groundweak+1
        psychicweak=psychicweak+1
        steelweak=steelweak+1
        waterweak=waterweak+1
        spreadphysical=True
        phaze=True
    if "Thundurus" in team:
        iceweak=iceweak+1
        rockweak=rockweak+1
    if "Thundurus-T" in team:
        iceweak=iceweak+1
        rockweak=rockweak+1        
    if "Celesteela" in team:
        electricweak=electricweak+1
        fireweak=fireweak+1
        firemove=True
        grassmove=True
    if "Tapu Bulu" in team:
        fireweak=fireweak+1
        flyingweak=flyingweak+1
        iceweak=iceweak+1
        poisonweak=poisonweak+1
        steelweak=steelweak+1
        grassmove=True
    if "Blacephalon" in team:
        darkweak=darkweak+1
        ghostweak=ghostweak+1
        groundweak=groundweak+1
        rockweak=rockweak+1
        waterweak=waterweak+1
        phaze=True
        spreadspecial=True
        firemove=True
    if "Buzzwole" in team:
        fairyweak=fairyweak+1
        fireweak=fireweak+1
        flyingweak=flyingweak+1
        psychicweak=psychicweak+1
    if "Pheromosa" in team:
        fairyweak=fairyweak+1
        fireweak=fireweak+1
        flyingweak=flyingweak+1
        psychicweak=psychicweak+1
    if "Xurkitree" in team:
        groundweak=groundweak+1
    if "Naganadel" in team:
        dragonweak=dragonweak+1
        groundweak=groundweak+1
        iceweak=iceweak+1
        psychicweak=psychicweak+1
        speedcontrol=True
    if "Kyurem" in team:
        dragonweak=dragonweak+1
        fairyweak=fairyweak+1
        fightingweak=fightingweak+1
        rockweak=rockweak+1
        steelweak=steelweak+1
        speedcontrol=True
        spreadspecial=True
    if "Regirock" in team:
        fightingweak=fightingweak+1
        grassweak=grassweak+1
        groundweak=groundweak+1
        steelweak=steelweak+1
        waterweak=waterweak+1
        spreadphysical=True

    if fireweak >2:
        team.clear()
        x=x+1
        continue
    if waterweak>1:
        team.clear()
        x=x+1
        continue        
    if grassweak>2:
        team.clear()
        x=x+1
        continue
    if electricweak>2:
        team.clear()
        x=x+1
        continue    
    if iceweak>1:
        team.clear()
        x=x+1
        continue    
    if fightingweak>2:
        team.clear()
        x=x+1
        continue    
    if poisonweak>2:
        team.clear()
        x=x+1
        continue 
    if groundweak>2:
        team.clear()
        x=x+1
        continue 
    if flyingweak>2:
        team.clear()
        x=x+1
        continue
    if psychicweak>2:
        team.clear()
        x=x+1
        continue
    if bugweak>2:
        team.clear()
        x=x+1
        continue
    if rockweak>1:
        team.clear()
        x=x+1
        continue
    if ghostweak>2:
        team.clear()
        x=x+1
        continue
    if darkweak>2:
        team.clear()
        x=x+1
        continue    
    if dragonweak>2:
        team.clear()
        x=x+1
        continue
    if steelweak>2:
        team.clear()
        x=x+1
        continue
    if fairyweak>2:
        team.clear()
        x=x+1
        continue

    if speedcontrol==False:
        team.clear()
        x=x+1
        continue
    if phaze==False:
        team.clear()
        x=x+1
        continue
    if spreadspecial==False:
        team.clear()
        x=x+1
        continue
    if spreadphysical==False:
        team.clear()
        x=x+1
        continue
    if firemove==False:
        team.clear()
        x=x+1
        continue
    if grassmove==False:
        team.clear()
        x=x+1
        continue
    #Form filter
    if "Thundurus" in team and "Thundurus-T" in team:
        team.clear()
        x=x+1
        continue
    if "Moltres" in team and "Moltres-G" in team:
        team.clear()
        x=x+1
        continue

    #Duplicate filter    
    if team == team in teams:
        team.clear()
        x=x+1
        continue
    
    teams.append(team)
    print(team)
    print(x)
    print ()
