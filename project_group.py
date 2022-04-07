def log_agroup(archive):
    game = 0
    total_kills = 0
    players = []
    kills = {}

    archive = open(file=archive, mode="r", encoding="utf8")
    for line in archive:
        line = archive.readline()
        if "0:00 InitGame" in line:
            print(line)
            game += 1
        elif "Kill:" in line:
            total_kills += 1
    archive.close()
    return ("total_kills = " + str(total_kills), game)


print(log_agroup("qgames.log"))
