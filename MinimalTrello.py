# Making required imports.
import requests
import os
import json

# Assigning a few environment variables to use later.
# NOTE: This script must be ran from the command prompt if environment variables are set. You can't run this script through a GUI.
key = os.environ['Trello_Key']
token = os.environ["Trello_Token"]

# Function finds name of variable:
def varname(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

# This class will be the main pillar of the library.
class Trello(object):

    # Initializing the class, accepting Trello key and token as arguments.
    def __init__(self, key, token):
        self.key = key
        self.token = token
        self.url = "https://api.trello.com/1/boards/"

    # This function creates a board on Trello with a custom name. Only the name argument is a requirement to use.
    def createBoard(self, name, defaultLabels=0,
                    prefs_permissionLevel=0, defaultLists=0,
                    keepFromSource=0, prefs_voting=0, prefs_comments=0,
                    prefs_invitations=0, prefs_selfJoin=0, prefs_cardCovers=0,
                    prefs_background=0, prefs_cardAging=0):
        # This is the default query that will be sent to Trello. It can be changed by modifying properties with arguments passed to CreateBoard.
        query = {"name":str(name),
               "defaultLabels":"true",
               "defaultLists":"true",
               "keepFromSource":"none",
               "prefs_permissionLevel":"private",
               "prefs_voting":"disabled",
               "prefs_comments":"members",
               "prefs_invitations":"members",
               "prefs_selfJoin":"true",
               "prefs_cardCovers":"true",
               "prefs_background":"grey",
               "prefs_cardAging":"regular",
               "key":key,
               "token":token}
        # This loop checks all arguments in the function, looking if any of the optional ones have been changed.
        for i in defaultLabels, defaultLists, keepFromSource, prefs_permissionLevel, prefs_voting, prefs_comments, prefs_invitations, prefs_selfJoin, prefs_cardCovers, prefs_background, prefs_cardAging:
            # If the argument has been modified, then the default query is updated accordingly.
            if i != 0:
                name = varname(i, locals())
                query[str(name[0])] == str(i)
        # A simple post request to Trello's API, with the response being converted using the json module.
        response = requests.request("POST", self.url, params=query)
        jsonresponse = json.loads(response.text)
        return jsonresponse

    # This function creates a new list in a specified board.
    def createList(self, name, idBoard, idListSource=0, pos=0):
        query = {"name": name,
                 "idBoard":idBoard,
                 "key":key,
                 "token":token}
        for i in idListSource, pos:
            if i != 0:
                query[str(varname(i, locals()))]
        response = requests.request("POST", self.url, params=query)
        jsonresponse = json.loads(response.text)
        print jsonresponse
        return jsonresponse
