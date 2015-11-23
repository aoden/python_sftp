import json
import pysftp
from os import walk

settings = None
with open("settings.txt") as data_file:
    settings = json.load(data_file)
with pysftp.Connection(settings["ip"], username=settings["id"], password=settings["password"]) as sftp:
    with sftp.cd(settings["target_location"]):
        f = []
        for (dirpath, dirnames, filenames) in walk(settings["target_location"]):
                for filename in filenames:
                    sftp.put(filename)
                break
