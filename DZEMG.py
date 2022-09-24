# DayZ Expansion Market Data Generator
# This Script Will Take Your Class File and Create Compatible data for DayZ Expansion Market/Trader Mod
# Script Created By: Buddster124
# Documenttaion: https://github.com/Buddster124/DZEMDG
# Last Edit Date: 9/24/22


# Beginning of Script
print("Buddster124's DayZ Expansion Market Data Generator")
input_file = input("Path To The Class File: ")
output_file = input("Output File Path: ")

text_file = open(input_file, "r")
output_file = open(f"{output_file}/Output.txt", "a")
lines = text_file.readlines()
final_lines = []
for x in lines:
    z = x.replace("\n", "")
    final_lines.append(z)
b = ""
for i in final_lines:
    output_file.write('         {\n')
    output_file.write(f'            "ClassName": "{i}",\n')
    output_file.write('            "MaxPriceThreshold": 20,\n')
    output_file.write('            "MinPriceThreshold": 10,\n')
    output_file.write('            "SellPricePercent": -1.0,\n')
    output_file.write('            "MaxStockThreshold": 100,\n')
    output_file.write('            "MinStockThreshold": 1,\n')
    output_file.write('            "QuantityPercent": -1,\n')
    output_file.write('            "SpawnAttachments": [],\n')
    output_file.write('            "Variants": []\n')
    output_file.write('        },\n')


output_file.close()
text_file.close()

