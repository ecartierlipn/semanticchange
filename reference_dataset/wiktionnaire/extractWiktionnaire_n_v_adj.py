#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:51:37 2020

@author: lucie
"""

from lxml import etree


#tree = etree.parse("GLAWI-test.xml")
tree = etree.parse("GLAWI_FR_work_D2015-12-26_R2016-05-18.xml")

root = tree.getroot()
cat = 'adjectif' # change for nom, verbe as desired
fout = open("wiktionnary_" + cat + "_def.tsv", mode="w")
fout.write("word\tsense_number\tusage_note\tdefinition\n")

for pos in root.xpath("//article/text/pos"):
    if pos.get("type").find(cat) != -1 and pos.get("lemma").find("1") != -1 :
            #print("***", (pos.find("../..")).find('title').text, "***")
            headword = (pos.find("../..")).find('title').text
            print(headword)
            compteur=0
            marque_usage=[]
            for defi in pos.iter('gloss'):
                for us in defi.iter('label'):
                    marque_usage.append(us.get('type') + ":" + us.get('value'))                
                compteur=compteur+1
                if len(marque_usage) == 0:
                    print(headword, ": ", compteur," ", defi.find('txt').text) 
                    fout.write(headword + "\t" + str(compteur) + "\t\t" + defi.find('txt').text + "\n") 
                else:
                    marque_usage=marque_usage[:-1]
                    print(headword, " : ", compteur," ", str(marque_usage), " ", defi.find('txt').text, sep="")
                    fout.write(headword + "\t" + str(compteur) + "\t" + str(marque_usage) + "\t"+ defi.find('txt').text + "\n")
                    marque_usage=[]

fout.close()




