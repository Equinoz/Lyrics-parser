#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import argparse

OUTPUT = "scores.log"

# Arguments de la ligne de commande
parser = argparse.ArgumentParser(description="Script d'analyse de texte fournissant un indice: plus l'indice est proche de 1 plus le texte est varié, plus l'indice est proche de zéro plus le texte est répétitif")
parser.add_argument("file", type=str, help="fichier .txt à analyser")
parser.add_argument("-w", "--write", action="store_true", help="ajout du score du texte analysé dans le fichier " + OUTPUT)

args = parser.parse_args()
