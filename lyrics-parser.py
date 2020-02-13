#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import argparse
import sys
import re
import math

OUTPUT = "scores.log"

""" Gestion des erreurs """
def errorHandler(text):
    print(text)
    sys.exit()

""" Fonction principale """
def main():
  # Arguments de la ligne de commande
  parser = argparse.ArgumentParser(description="Script d'analyse de texte fournissant un indice: plus l'indice est proche de 1 plus le texte est varié, plus l'indice est proche de zéro plus le texte est répétitif")
  parser.add_argument("file", type=str, help="fichier .txt à analyser")
  parser.add_argument("-w", "--write", action="store_true", help="ajout du score du texte analysé dans le fichier " + OUTPUT)
  args = parser.parse_args()

  # Vérification de l'extension du fichier
  if args.file.split('.')[-1] != "txt":
    errorHandler("Erreur: le fichier " + args.file + " doit posséder l'extension .txt")

  # Lecture du fichier
  try:
    with open(args.file, 'r') as openedFile:
      text = openedFile.read()
  except FileNotFoundError:
    errorHandler("Erreur: le fichier nommé " + args.file + " n'as pas été trouvé")

  # Suppression de la ponctuation, des caractères spéciaux et mise en minuscules
  text = re.sub(r"([\.?\"&{}/$€!:;,\(\)\t])", r'', text)
  text = re.sub(r"(['\n\r])", r' ', text)
  text = re.sub(r"(\s{2,})", r' ', text).lower()

  if text == "":
    errorHandler("Erreur: le fichier " + args.file + " ne contient pas de texte")

  # On splitte le texte et on supprime les mots de moins de 3 lettres, non significatifs
  text = [word for word in text.split(' ') if len(word) > 2]

  # On recense les mots différents
  differentsWords = set(text)

  # Calcul du score
  score = math.ceil(len(differentsWords) / len(text) * 100) / 100

  # Affichage du résultat
  print("Nombre de mots de plus de 2 lettres: {}".format(len(text)))
  print("Nombre de mots différents: {}".format(len(differentsWords)))
  print("Score du texte: {}".format(score))

main()
