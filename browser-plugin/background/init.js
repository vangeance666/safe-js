console.log("menu.js loaded");

browser.contextMenus.create({
	id: "muted-tab", 
	title: "Analyze in Safe-JS",
	contexts: ['link']
});

// browser.contextMenus.create({
//   id: "log-selection",
//   title: browser.i18n.getMessage("contextMenuItemSelectionLogger"),
//   contexts: ["selection"]
// }, onCreated)