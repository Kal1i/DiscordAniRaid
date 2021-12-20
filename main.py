from discord.ext import commands
import datetime



client = commands.AutoShardedBot(command_prefix="!")
token = "Enter your token"

@client.command()
async def on_member_join(member):
    await client.wait_until_ready()
    names_to_check = ["", "", "", "", ""] # You can put here names you want to ban from the server
    if any(i in member.name.lower() for i in names_to_check):
        await member.ban()
    now = datetime.datetime.now()
    diff = now - member.created_at
    if diff.total_seconds() < 86400:
        await member.send("Due to an influx of raids, your account has been deemed to young to join this server.")
        await member.kick()


client.run(token)
print("Starting!")
