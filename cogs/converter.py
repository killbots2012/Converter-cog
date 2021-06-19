import discord
from discord.ext import commands
import random

class Converter(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Converter cog started')

    @commands.Cog.listener()
    async def on_message(self, message):
        # km to mile
         if  "km" in message.content:
            print(message.content)
            question = message.content.split(" ")[0]
            kmToMile = float(question)
            questionConvert = kmToMile / 1.60934
            formated_convertion = "%.2f" % questionConvert
            await message.channel.send(f"{formated_convertion} MPH".upper())
            
        # # Mile to km 
         elif "mile" in message.content:
            print(message.content)
            question = message.content.split(" ")[0]
            mileToKM = float(question)
            questionConvert = mileToKM * 1.60934
            formated_convertion = "%.2f" % questionConvert
            await message.channel.send(f"{formated_convertion} KM/ h".upper())
        
        # # Litre to gallon
         elif "litre" in message.content:
            print(message.content)
            question = message.content.split(" ")[0]
            litresToGallon = float(question)
            questionConvert = litresToGallon / 3.785
            formated_convertion = "%.2f" % questionConvert
            await message.channel.send(f"{formated_convertion} Gallon".upper())
        
        # gallon to Litre
         elif "gallon" in message.content:
            print(message.content)
            question = message.content.split(" ")[0]
            gallonToLitre = float(question)
            questionConvert = gallonToLitre * 3.785
            formated_convertion = "%.2f" % questionConvert
            await message.channel.send(f"{formated_convertion} Litre".upper())
       
        # # inch to cm
         elif "inch" in message.content:
            print(message.content)
            question = message.content.split(" ")[0]
            question = float(question)
            questionConvert = question * 2.54 
            formated_convertion = "%.2f" % questionConvert
            await message.channel.send(f"{formated_convertion} cm".upper())
        
        # # cm to inch
         elif "cm" in message.content:
            print(message.content)
            question = message.content.split(" ")[0]
            FootToCM = float(question)
            questionConvert = FootToCM / 2.54 
            formated_convertion = "%.2f" % questionConvert
            await message.channel.send(f"{formated_convertion} Inch".upper())        

        # # celsius to fahrenheight
         elif "c" in message.content:
            print(message.content)
            question = message.content.split(" ")[0]
            CelsiusToFahrenheit = float(question)
            questionConvert = (CelsiusToFahrenheit * 5/9) + 32 
            formated_convertion = "%.2f" % questionConvert
            await message.channel.send(f"{formated_convertion} Fahrenheiht".upper())

        # # fahrenheight to celsius
         elif "f" in message.content:
            print(message.content)
            question = message.content.split(" ")[0]
            FahrenheitToCelsius = float(question)
            questionConvert = (FahrenheitToCelsius - 32) + 5/9 
            formated_convertion = "%.2f" % questionConvert
            await message.channel.send(f"{formated_convertion} Celsius".upper())


def setup(client):
    client.add_cog(Converter(client))