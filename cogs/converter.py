import discord
from discord.ext import commands
import random

class Converter(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Converter cog started')

    @commands.command()
    async def convert(self, ctx, *,question):
        # km to mile
        if "km" in question:
            question = ''.join(question.split())[:-2]
            kmToMile = float(question)
            questionConvert = question / 1.60934
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} MPH".upper())
            
        # Mile to km 
        elif "mile" in question:
            question = ''.join(question.split())[:-5]
            mileToKM = float(question)
            questionConvert = kmhToMph * 1.60934
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} KM/ h".upper())
        # Litre to gallon
        elif "litre" in question:   
            question = ''.join(question.split())[:-5]
            litresToGallon = float(question)
            questionConvert = litresToGallon / 3.785
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} Gallon".upper())
        # gallon to Litre
        elif "gallon" in question:
            question = ''.join(question.split())[:-6]
            gallonToLitre = float(question)
            questionConvert = gallonToLitre * 3.785
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} Litre".upper())
        # inch to cm
        elif "inch" in question:
            question = ''.join(question.split())[:-4]
            question = float(question)
            questionConvert = question * 2.54 
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} cm".upper())
        # cm to inch
        elif "cm" in question:
            question = ''.join(question.split())[:-2]
            FootToCM = float(question)
            questionConvert = FootToCM / 2.54 
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} Inch".upper())    
        # celsius to fahrenheight
        elif "c" in question:
            question = ''.join(question.split())[:-1]
            CelsiusToFahrenheit = float(question)
            questionConvert = (CelsiusToFahrenheit * 5/9) + 32 
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} Fahrenheiht".upper())
        # fahrenheight to celsius
        elif "f" in question:
            question = ''.join(question.split())[:-1]
            FahrenheitToCelsius = float(question)
            questionConvert = (FahrenheitToCelsius - 32) + 5/9 
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} Celsius".upper())


def setup(client):
    client.add_cog(Converter(client))