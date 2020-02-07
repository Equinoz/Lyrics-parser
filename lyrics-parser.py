#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import argparse
import sys
import re

OUTPUT = "scores.log"

""" Fonction vérifiant l'extension du fichier passé en argument """
def checkExtension(file):
  if file.split('.')[-1] != "txt":
    print("Erreur: le fichier " + file + " doit posséder l'extension .txt")
    sys.exit()

""" Fonction principale """
def main():
  # Arguments de la ligne de commande
  parser = argparse.ArgumentParser(description="Script d'analyse de texte fournissant un indice: plus l'indice est proche de 1 plus le texte est varié, plus l'indice est proche de zéro plus le texte est répétitif")
  parser.add_argument("file", type=str, help="fichier .txt à analyser")
  parser.add_argument("-w", "--write", action="store_true", help="ajout du score du texte analysé dans le fichier " + OUTPUT)

  args = parser.parse_args()

  # Vérification de l'extension du fichier
  checkExtension(args.file)

  # Lecture du fichier
  file = ""
  try:
    with open(args.file, "r") as openedFile:
      file = openedFile.read()
  except FileNotFoundError:
    print("Erreur: le fichier nommé " + args.file + " n'as pas été trouvé")
    sys.exit()

  # Suppression de la ponctuation et mise en minuscules
  file = re.sub(r"([\.?;,\(\)\t])", r"", file)
  file = re.sub(r"(['\n\r])", r" ", file)
  file = re.sub(r"(\s{2,})", r" ", file).lower()

  print(file)

main()