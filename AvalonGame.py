class AvalonGame:
    roles = {}
    PercAndMorg = False;
    Mordred = False;
    Oberon = False;
    Norebo = False;

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

    async def loadBoard(self):
	       playersnamestring = "|"
	       for x in playerlist:
		     playersnamestring += "` "+x.name+" `|"
	       if playerno == 5:
		        self.quest.append(2) #quest 1
		        self.quest.append(3)
		        self.quest.append(2)
		        self.quest.append(3)
		        self.quest.append(3)

            elif playerno == 6:
                self.quest.append(2) #quest 1
		        self.quest.append(3)
		        self.quest.append(4)
		        self.quest.append(3)
		        self.quest.append(4)

            elif playerno == 7:
                self.quest.append(2) #quest 1
		        self.quest.append(3)
		        self.quest.append(3)
		        self.quest.append(4)
		        self.quest.append(4)

            elif playerno <= 10 and playerno >= 8:
                self.quest.append(3) #quest 1
		        self.quest.append(4)
		        self.quest.append(4)
		        self.quest.append(5)
		        self.quest.append(5)
            else:
                return "Invalid Number of Players"
                await client.send_message(message.channel, startStr.format
                (playersnamestring,len(playerlist),"3","2",rolesStr))

    async def chooseRoles(self):
        #should ask the player for what roles they want to play with
            return

    async def loadRoles(self):
        self.roles["Merlin"] = ""
        self.roles["The Assassin"] = ""

        if PercAndMorg:
            self.roles["Percival"] = ""
            self.roles["Morgana"] = ""

        elif Mordred:
            self.roles["Mordred"] = ""

        elif Oberon:
            self.roles["Oberon"] = ""

        elif Norebo:
            self.roles["Norebo"] = ""

        #make function/case to create all good/bad normies

        else:
            pass

    async def chooseQuest(self):
        #asks for members of the quest using @user
        return

    async def voteQuest(self):
        """sends a dm to the players to see if they approve or reject the quest.
        ask 'Please type "approve" or "reject".
        """
        return

    async def quest(self):
        """sends a dm to the players on the quest. if exalibur is a part of
        the game, allow the player to view and switch the vote of one person if
        they choose"""

        return

    async def questResults(self):
        """posts a message about the results of the quest"""
        return

    async def assassinate(self):
        """If the good guys are able to sucessfully complete 3 quests, the bot
        sends a message directed at the Assassin.
        "Alright @Assassin, who do you think is Merlin? (Please use @user)"

        If Merlin is chosen correctly, send a message saying bad guys won.
        Otherwise good guys win.
        """
        return


    async def night(self):
	       await client.send_message(message.channel, nighttimemsg)
           roleshuffle = copy.deepcopy(playerlist)
           shuffle(roleshuffle)

           self.roles["Merlin"] = roleshuffle[0]
           self.roles["The Assassin"] = roleshuffle[1]

           if PercAndMorg:
               self.roles["Morgana"] = roleshuffle[2]
               self.roles["Percival"] = roleshuffle[3]

           elif Mordred:
               self.roles["Mordred"] = roleshuffle[4]

           elif Oberon:
               self.roles["Oberon"] = roleshuffle[5]

           elif Norebo:
               self.roles["Norebo"] = roleshuffle[6]

           #make fucntion/case to asssign all good/ban normies

       else:
           pass
