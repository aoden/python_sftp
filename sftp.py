import json
import os
import pysftp
from os import walk

settings = None
with open("settings.txt") as data_file:
    settings = json.load(data_file)
with pysftp.Connection(settings["ip_address"], username=settings["username"], password=settings["password"]) as sftp:
    with sftp.cd(settings["target_location"]):
        f = []
        for (dirpath, dirnames, filenames) in walk(settings["location"]):
                for filename in filenames:
                    sftp.put(os.path.abspath(settings["location"] + "/" + filename))
                break
