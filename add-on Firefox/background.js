// Création de l'élément dans le menu contextuel
browser.menus.create({
  id: "lyrics-parser",
  title: browser.i18n.getMessage("itemLyricsParser"),
  contexts: ["selection"]
});

browser.menus.onClicked.addListener((info) => {
  // Suppression de la ponctuation, des caractères spéciaux et mise en minuscules du texte sélectionné
  let text = info.selectionText.replace(/[\.?\"&{}\[\]/$€!:;,\(\)\t=+#~]/g, '');
  text = text.replace(/['\n\r]/g, ' ');
  text = text.replace(/\s{2,}/g, ' ').toLowerCase();

  // On splitte le texte et on supprime les mots de moins de 3 lettres, considérés comme non significatifs
  let words = text.split(' ').filter(word => { return (word.length > 2) });

  // On recense les mots différents en passant le tableau dans un set
  let differentsWords = new Set(words);

  // Calcul du score
  let score = Math.ceil(differentsWords.size / words.length * 100) / 100;

  // Préparation du message
  let message;
  if (words.length > 0) {
    message = "Nombre de mots de plus de 2 lettres: " + words.length + "\n";
    message += "Nombre de mots différents: " + differentsWords.size + "\n";
    message += "Score du texte: " + score;
  }
  else
    message = "Merci de sélectionner du texte analysable";

  // On récupère l'onglet courant et on envoie le message au script de contenu
	browser.tabs.query({active: true, currentWindow: true})
	.then(tabs => {
    browser.tabs.sendMessage(tabs[0].id, {message: message});
	});
});
