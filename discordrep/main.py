import requests

def getrep(token="",id=""):
    discordrep = requests.get("https://discordrep.com/api/v3/rep/"+ id, headers={"Authorization":token})
    return discordrep.json()

def getwarnings(token="",id=""):
    discordrep = requests.get("https://discordrep.com/api/v3/infractions/"+ id, headers={"Authorization":token})
    return discordrep.json()

def upvote(token="",voterid="",targetid="",):
    discordrep = requests.post("https://discordrep.com/api/v3/vote/upvote/"+ voterid+"/"+ targetid +, headers={"Authorization":token})
    return discordrep.json()

def downvote(token="",voterid="",targetid="",):
    discordrep = requests.post("https://discordrep.com/api/v3/vote/downvote/"+ voterid+"/"+ targetid , headers={"Authorization":token},)
    return discordrep.json()


def editbio(token="",id="",bio=""):
    discordrep = requests.post("https://discordrep.com/api/v3/infractions/"+ id, headers={"Authorization":token},body={"bio":bio})
    return discordrep.json()
