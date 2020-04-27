browser.runtime.onMessage.addListener(message => {
  alert(message.message);
});
