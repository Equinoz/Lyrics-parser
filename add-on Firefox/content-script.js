// On récupère le message depuis le script d'arrière-plan et on l'affiche sur la page web en cours
browser.runtime.onMessage.addListener(message => {
  alert(message.message);
});
