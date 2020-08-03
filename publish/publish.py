import datetime

import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class Publish(commands.Cog): 
    """Publish messages sent in announcement channels"""
    
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @commands.command()
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def publish(self, ctx, message_id: discord.Message.id):
        """Publish message sent in announcement channel"""
        await message_id.publish()
        await ctx.send("Published message successfully.")
                                        
def setup(bot):
    bot.add_cog(Publish(bot))
