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
        
        if "km" in question:
            question = ''.join(question.split())[:-2]
            question = float(question)
            questionConvert = question / 1.60934
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} MPH".upper())
            
            
        elif "mile" in question:
            question = ''.join(question.split())[:-5]
            kmhToMph = float(question)
            questionConvert = kmhToMph * 1.60934
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} KM/ h".upper())

        elif "litre" in question:   
            question = ''.join(question.split())[:-5]
            litresToGallon = float(question)
            questionConvert = litresToGallon / 3.785
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} Gallon".upper())

        elif "gallon" in question:
            question = ''.join(question.split())[:-6]
            gallonToLitre = float(question)
            questionConvert = gallonToLitre * 3.785
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} Litre".upper())

        elif "inch" in question:
            await ctx.send("something? ")
            question = ''.join(question.split())[:-4]
            question = float(question)
            questionConvert = question * 2.54 
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} cm".upper())

        elif "cm" in question:
            question = ''.join(question.split())[:-3]
            FootToCM = float(question)
            questionConvert = FootToCM / 2.54 
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} Inch".upper())    

        elif "c" in question:
            question = ''.join(question.split())[:-1]
            CelsiusToFahrenheit = float(question)
            questionConvert = (CelsiusToFahrenheit * 5/9) + 32 
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} Fahrenheiht".upper())

        elif "f" in question:
            await ctx.send("somethin")
            question = ''.join(question.split())[:-1]
            FahrenheitToCelsius = float(question)
            questionConvert = (FahrenheitToCelsius - 32) + 5/9 
            formated_convertion = "%.2f" % questionConvert
            await ctx.send(f"{formated_convertion} Celsius".upper())

        
           
        


 

def setup(client):
    client.add_cog(Converter(client))