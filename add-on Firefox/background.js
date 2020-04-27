browser.menus.create({
  id: "lyrics-parser",
  title: browser.i18n.getMessage("itemLyricsParser"),
  contexts: ["selection"]
});

browser.menus.onClicked.addListener((info) => {
	browser.tabs.query({active: true, currentWindow: true})
	.then(tabs => {
    browser.tabs.sendMessage(tabs[0].id, {message: info.selectionText});
	});
});
