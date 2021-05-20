import requests

class Api():
    def __init__(self,token):
        self.token = token

    def getrep(self,id=""):
        discordrep = requests.get(f"https://discordrep.com/api/v3/rep/id/{id}", headers={"Authorization": self.token})
        return discordrep.json()


    def getwarnings(self,id=""):
        discordrep = requests.get(f"https://discordrep.com/api/v3/infractions/{id}", headers={"Authorization":self.token})
        return discordrep.json()


    def upvote(self,voterid="",targetid="",):
        discordrep = requests.post(f"https://discordrep.com/api/v3/vote/upvote/{voterid}/{targetid}" headers={"Authorization": self.token})
        return discordrep.json()


    def downvote(self,voterid="",targetid="",):
        discordrep = requests.post(f"https://discordrep.com/api/v3/vote/downvote/{voterid}/{targetid}", headers={"Authorization": self.token},)
        return discordrep.json()

    def editbio(self,id="",bio=""):
        discordrep = requests.post(f"https://discordrep.com/api/v3/infractions/{id}", headers={"Authorization": self.token},body={"bio":bio})
        return discordrep.json()
