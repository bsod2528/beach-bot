import discord


class RepoLink(discord.ui.View):
    def __init__(self):
        super().__init__()
        url = f"https://github.com/bsod2528/Beach-Bot"
        self.add_item(discord.ui.Button(label="Beach Bot Repo", url=url))
