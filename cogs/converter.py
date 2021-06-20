import discord
from discord.ext import commands
import re

class Converter(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Converter cog started')

    @commands.Cog.listener()
    async def on_message(self, message):
        # km to mile
        if "km" in message.content: 
            kmtoMile = ""
            for word in message.content.split():
             if word.isdigit():
                 kmtoMile = int(word)
                 questionConvert = kmtoMile / 1.60934
                 formated_convertion = "%.2f" % questionConvert
                 await message.channel.send(f"{word} km = {formated_convertion} miles".upper()) 
         
        elif "kph" in message.content:
            kphtoMph = ""
            for word in message.content.split():
             if word.isdigit():
                 kphtoMph = int(word)
                 questionConvert = kphtoMph / 1.60934
                 formated_convertion = "%.2f" % questionConvert
                 await message.channel.send(f"{word} kph = {formated_convertion} mph".upper())

        # # Mile to km 
        elif "mile" in message.content:
            mileToKM = ""
            for word in message.content.split():
             if word.isdigit():
                 mileToKM = int(word)
                 questionConvert = mileToKM * 1.60934
                 formated_convertion = "%.2f" % questionConvert
                 await message.channel.send(f"{word} mile = {formated_convertion} km".upper())

        elif "mph" in message.content:
            mileToKM = ""
            for word in message.content.split():
             if word.isdigit():
                 mileToKM = int(word)
                 questionConvert = mileToKM * 1.60934
                 formated_convertion = "%.2f" % questionConvert
                 await message.channel.send(f"{word} mph = {formated_convertion} kph".upper())                   
        
        # # Litre to gallon
        elif "litre" in message.content:
            litresToGallon = ""
            for word in message.content.split():
             if word.isdigit():
                litresToGallon = int(word)
                questionConvert = litresToGallon / 3.785
                formated_convertion = "%.2f" % questionConvert
                await message.channel.send(f"{word} litres = {formated_convertion} Gallon".upper())
        
        # gallon to Litre
        elif "gallon" in message.content:
            gallonToLitre = ""
            for word in message.content:
             if word.isdigit():
                 gallonToLitre = int(word)
                 questionConvert = gallonToLitre * 3.785
                 formated_convertion = "%.2f" % questionConvert
                 await message.channel.send(f"{word} gallon = {formated_convertion} Litre".upper())
       
        # # inch to cm
        elif "inch" and "in" in message.content:
            inchToCm= ""
            for word in message.content:
             if word.isdigit():
                inchToCm = int(word)
                questionConvert = inchToCm * 2.54 
                formated_convertion = "%.2f" % questionConvert
                await message.channel.send(f"{word} inch = {formated_convertion} cm".upper())
        
        # # cm to inch
        elif "cm" and "centimeter" and "centimetre" in message.content:
            cmToInch =""
            for word in message.content:
             if word.isdigit():
                cmToInch = int(word)
                questionConvert = cmToInch / 2.54 
                formated_convertion = "%.2f" % questionConvert
                await message.channel.send(f"{word} cm = {formated_convertion} Inch".upper())
        
        # Foot to meter
        elif "foot" and "feet" in message.content:
            FootToMeter = ""
            for word in message.content:
             if word.isdigit():
                FootToMeter = int(word)
                questionConvert = FootToMeter / 3.281 
                formated_convertion = "%.2f" % questionConvert
                await message.channel.send(f"{word} foot {formated_convertion} meter".upper())

        elif "meter" in message.content:
            meterToFeet = ""
            for word in message.content:
             if word.isdigit():
                meterToFeet = int(word)
                questionConvert = meterToFeet * 3.281 
                formated_convertion = "%.2f" % questionConvert
                await message.channel.send(f"{word} meter = {formated_convertion} feet".upper())               

        # pound to kg
        elif "pound" in message.content:
             poundToKg = ""
             for word in message.content:
              if word.isdigit():
                 poundToKg = int(word)
                 questionConvert = poundToKg / 2.20462
                 formated_convertion = "%.2f" % questionConvert
                 await message.channel.send(f"{word} Ib {formated_convertion} kg".upper())
        # kg to pound          
        elif "kg" in message.content:
            kgToPound = ""
            for word in message.content:
              if word.isdigit():
                 kgToPound = int(word)   
                 questionConvert = kgToPound * 2.20462
                 formated_convertion = "%.2f" % questionConvert
                 await message.channel.send(f"{word} kg = {formated_convertion} pound".upper()) 

        # PSI to BAR
        elif "psi" in message.content:
            psiToBar = ""
            for word in message.content:
              if word.isdigit():
                  psiToBar = int(word)  
                  questionConvert = psiToBar * 14.504
                  formated_convertion = "%.2f" % questionConvert
                  await message.channel.send(f"{word} psi = {formated_convertion} bar".upper()) 

         # PSI to BAR
        elif "bar" in message.content:
            barToPsi = ""
            for word in message.content:
             if word.isdigit():
              barToPsi = int(word)
              questionConvert = barToPsi * 14.504
              formated_convertion = "%.2f" % questionConvert
              await message.channel.send(f"{word} bar = {formated_convertion} PSI".upper())   
             

        # # celsius to fahrenheight
        elif "c" in message.content:
            CelsiusToFahrenheit = ""
            for word in message.content:
             if word.isdigit:
              CelsiusToFahrenheit = int(word)
              questionConvert = (CelsiusToFahrenheit * 5/9) + 32 
              formated_convertion = "%.2f" % questionConvert
             await message.channel.send(f"{word} celsius = {formated_convertion} Fahrenheiht".upper())

        # # fahrenheight to celsius
        elif "f" in message.content:
            FahrenheitToCelsius = ""
            for word in message.content:
             if word.isdigit:
              FahrenheitToCelsius = int(word)
              questionConvert = (FahrenheitToCelsius - 32) + 5/9 
              formated_convertion = "%.2f" % questionConvert
              await message.channel.send(f"{word} fahrenheight = {formated_convertion} Celsius".upper())


def setup(client):
    client.add_cog(Converter(client))