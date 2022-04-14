def log_agroup(archive):
    game = 0
    total_kills = 0
    players = []
    kills = {}
    weapons = {}

    archive = open(file=archive, mode="r", encoding="utf8")
    for line in archive:
        if "Kill:" in line:
            total_kills += 1
            if line.split()[-1] in weapons:
                weapons[line.split()[-1]] += 1
            else:
                weapons[line.split()[-1]] = 1
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
                        if string not in players:
                            players.append(string)
            if line.split()[5] not in players:
                if line.split()[6] != "killed":
                    pass
                    if line.split()[7] == "killed":
                        list = []
                        list.append(line.split()[5])
                        list.append(line.split()[6])
                        string = ' '.join(list)
                        if string not in players:
                            players.append(string)
            if line.split()[5] not in players:
                if line.split()[6] == "killed":
                    string = line.split()[5]
                    if string not in players:
                        if string != "<world>":
                            players.append(string)
        if "0:00 InitGame" in line:
            game += 1
    archive.close()
    return ("total_kills = " + str(total_kills), game, players, weapons, kills)


print(log_agroup("qgames.log"))
