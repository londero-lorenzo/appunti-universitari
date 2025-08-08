
window.excalidrawUtils  = 
 exportElementsToSvg: {
	async function exportElementsToSvg({ elementIds, outputPath }) {
	  const view = await ea.setView("active");
	  if (!view) {
		new Notice("Nessuna view Excalidraw attiva.");
		return;
	  }

	  const allElements = await ea.getViewElements();
	  const targetElements = allElements.filter(el => elementIds.includes(el.id));

	  if (targetElements.length === 0) {
		new Notice("Nessun elemento trovato per gli ID forniti.");
		return;
	  }
	  
	const scene = {
	  elements: targetElements,
	  appState: {
		...view.getScene().appState,
		theme: view.getViewExportThere(),
		exportEmbedScene: view.getViewExportEmbedScene()
	  },
	  files: {}
	};

	const options = {
	  withBackground: view.getViewExportWithBackground(),
	  withTheme: true,
	  isMask: false,
	  skipInliningFonts: false
	};


	  //await ea.setViewSelectedElements(targetElements);
	  const svgElement = await getSVG(scene, options, 10, null); // padding, hostFile=null

	  if (!svgElement) {
		new Notice("Errore durante l'esportazione SVG.");
		return;
	  }

	  await app.vault.adapter.write(outputPath, svgElement.outerHTML);
	  new Notice(`SVG salvato in ${outputPath}`);
	}