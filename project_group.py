import json


# this function will store the informations of the log to return it
def log_agroup(archive):
    game = 0
    total_kills = 0
    players = []
    kills = {}
    weapons = {}
    world = 0

    # this line will open the log
    archive = open(file=archive, mode="r", encoding="utf8")
    # this line will read the log line by line
    for line in archive:
        # these lines will add each kill made separately by weapons
        if "Kill:" in line:
            total_kills += 1
            if line.split()[-1] in weapons:
                weapons[line.split()[-1]] += 1
            else:
                weapons[line.split()[-1]] = 1
            # these lines will add a player that has 3 names separately by spaces, plus it will add a kill to them each time them kill an enemy
            if line.split()[5] in players:
                pass
            if line.split()[5] not in players:
                if line.split()[6] != "killed":
                    pass
                    if line.split()[7] != "killed":
                        list = []
                        list.append(line.split()[5])
                        list.append(line.split()[6])
                        list.append(line.split()[7])
                        string = ' '.join(list)
                        if string in players:
                            kills[string] += 1
                        if string not in players:
                            players.append(string)
                            kills[string] = 1
            # these lines will add a player that has 2 names separately by a space, plus it will add a kill to them each time them kill an enemy
            if line.split()[5] not in players:
                if line.split()[6] != "killed":
                    pass
                    if line.split()[7] == "killed":
                        list = []
                        list.append(line.split()[5])
                        list.append(line.split()[6])
                        string = ' '.join(list)
                        if string in players:
                            kills[string] += 1
                        if string not in players:
                            players.append(string)
                            kills[string] = 1
            # these lines will add a player that has only 1 name and it filters to <world> doesn't get a kill like a player, plus it will add a kill to them each time them kill an enemy
            if line.split()[6] == "killed":
                string = line.split()[5]
                if string in players:
                    if string != "<world>":
                        kills[string] += 1
            if line.split()[5] not in players:
                if line.split()[6] == "killed":
                    string = line.split()[5]
                    if string != "<world>":
                        players.append(string)
                        kills[string] = 1
                if string == "<world>":
                    world += 1
        # these lines will add/increase each time a game/new game starts
        if "0:00 InitGame" in line:
            game += 1
    # this line will close the log
    archive.close()
    # these lines will return JSON with the match informations
    json_return = {
            "total_kills": total_kills,
            "players": players,
            "kills": kills,
            "weapon_kill": weapons
        }
    json_print = json.dumps(json_return)
    return json_print


# this line will print to the terminal the match informations made by the function
print(log_agroup("qgames.log"))
