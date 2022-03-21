# from multiprocessing import context
import quantumrandom
from discord.ext import commands
# from fastapi import FastAPI


# client = discord.Client()
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'Logado como {bot.user} rodando na maquina do Abade uhuuuuu')


@bot.command()
async def welcome(ctx: commands.Context):
    await ctx.send(f"Seja bem vindo(a) ao nosso RPG {ctx.guild.name}, {ctx.author}")


@bot.command(name="dice-roll")
async def dice_roll(ctx: commands.Context, *args):
    try:
        roll_n = int(args[0])
        if roll_n not in (4, 6, 8, 10, 12, 20, 100):
            raise NotAllowedDiceNumber
        rand_n = int(quantumrandom.randint(0, roll_n))
        print(f"dado de {roll_n} jogado, com resultado: {rand_n}")
        await ctx.send(f"Seu dado de {roll_n} lados deu: {rand_n}")
    except (ValueError, IndexError):
        await ctx.send("Você deve inserir um numero de lados do seu dado, ao lado do comando, exemplo: <!dice-roll 20>")
    except NotAllowedDiceNumber:
        await ctx.send("Voce pode jogar apenas dados de: 4, 6, 8, 10, 12, 20 e 100 lados")


from config_handler import get_config
token = get_config("DISCORD_TOKEN")
bot.run(token)

class NotAllowedDiceNumber(Exception):
    ...
