def log_reader(archive):
    archive = open(file=archive, mode="r", encoding="utf8")
    read = archive.read()
    print(read)
    archive.close()


log_reader("qgames.log")
