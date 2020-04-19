import discord

from .timedelta import format_time


class GuildResource:
    def __init__(self, ctx, color):
        self.ctx = ctx
        self.guild = self.ctx.guild
        self.color = color

    def guild_embed(self):
        """Creëer een insltuiting met daarin de informatie van de server."""

        g: discord.Guild = self.guild

        bots = len([m for m in g.members if m.bot])
        humans = len([m for m in g.members if not m.bot])
        online = len([m for m in g.members if not m.status != discord.Status.online])

        embed = discord.Embed(color=self.color)

        embed.set_author(name=f"{g.name}'s Stats")

        embed.add_field(
            name=f"Member Count",
            value=f"Online: {online}\nHumans: {humans}\nBots: {bots}\nMember Count: {g.member_count}",
        )
        embed.add_field(name="Catagorieën", value=len(g.categories))
        embed.add_field(name="Tekstkanalen", value=len(g.text_channels))
        embed.add_field(name="Spraakkanelen", value=len(g.voice_channels))
        embed.add_field(name="Rollen", value=len(g.roles))
        embed.add_field(name="Server Regio", value=g.region.name.title())
        embed.add_field(name="Server Eigenaar", value=g.owner.mention)
        embed.add_field(name="Gecreëerd", value=format_time(g.created_at))

        embed.set_thumbnail(url=str(g.icon_url))
        embed.set_footer(text=f"Server ID: {g.id}")

        return embed
