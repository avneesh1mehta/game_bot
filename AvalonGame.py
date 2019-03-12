class AvalonGame:
    roles = {}
    def __init__(self):
        self.players = []
        self.quest = []
        self.roles = {}
        self.channel = channel
    def add_player(self, player):
        self.playery.add(player)
    def game_start(self, players):
        ruleset = len(players)
        self.roles = rule(ruleset)
    async def loadrules(self):
	       playersnamestring = "|"
	       for x in playerlist:
		       playersnamestring += "` "+x.name+" `|"
	       if playerno == 5:
		        self.quest.append(2) #quest 1
		        self.quest.append(3)
		        self.quest.append(2)
		        self.quest.append(3)
		        self.quest.append(3)
		        self.roles["Merlin"] = ""
		        self.roles["The Assassin"] = ""
		        self.roles["Tenant farmer, Loyal Servant of Arthur"] = ""
		        self.roles["Omegalul Loyal Servant of Arthur"] = ""
		        self.roles["Dat boi, Minion of Mordred"] = ""
		   await client.send_message(message.channel, startStr.format(playersnamestring,len(playerlist),"3","2",rolesStr))
    async def night(self):
	       await client.send_message(message.channel, nighttimemsg)
           roleshuffle = copy.deepcopy(playerlist)
           shuffle(roleshuffle)
           self.roles["Merlin"] = roleshuffle[0]
           self.roles["The Assassin"] = roleshuffle[1]
           self.roles["Tenant farmer, Loyal Servant of Arthur"] = roleshuffle[2]
           self.roles["Omegalul Loyal Servant of Arthur"] = roleshuffle[3]
           self.roles["Dat boi, Minion of Mordred"] = roleshuffle[4]
