import imp


import os

def sync_comm():
    alias = ["git config --global alias.co checkout"]
    alias = [["co", "checkout"], ["ci", "commit"], ["st", "status"]]
    for item in alias:
        os.system(f"git config --global alias.{item[0]} {item[1]}")