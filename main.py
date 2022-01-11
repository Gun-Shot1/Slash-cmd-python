import os
from keep_alive import keep_alive
import discord
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import os
from discord_slash import SlashCommand
from discord_slash import SlashContext
from discord_slash.utils import manage_commands
# ^^ All of our necessary imports

#Define our bot
client = discord.Client()

client = commands.Bot(command_prefix = "!") #put your own prefix here, but it wont matter since slash commands default to /
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game(name='Your Name-Bot')) #Bot status, change this to anything you like
	print("Bot online") #will print "bot online" in the console when the bot is online
	

#Responds with "pong"
@slash.slash(name="ping", description="Ping Pong")
async def _help(ctx: SlashContext):
	await ctx.send(content="pong!")

#Send a preset embed to the channel where command is invoked.
@slash.slash(name="your_cmd_name", description="description of your cmd")
async def your_cmd_name(ctx: SlashContext):
  embed=discord.Embed(title="**title of your cmd", color="hex code")
  embed.add_field(name="field 1 title", value="field 1 description", inline=True or False as per choice)
  embed.add_field(name="field 2 title", value="field 2 description", inline=True or False as per choice)
  await ctx.send(embed=embed)

# Space given text by user
@slash.slash(name="space", description="Space your text", options=[manage_commands.create_option( #create an arg
    name = "text", #Name the arg as "text"
    description = "The text to space", #Describe arg
    option_type = 3, #option_type 3 is string
    required = True #Make arg required
  )])
async def _space(ctx: SlashContext, sentence):
	newword = "" #define new sentence
	for char in sentence: #For each character in given sentence
		newword = newword + char + "   " #Add to new sentence  with space
	await ctx.send(content=newword) #send mew sentence

#Run our webserver, this is what we will ping
keep_alive()

#Run our bot
client.run(os.getenv("TOKEN")) 
