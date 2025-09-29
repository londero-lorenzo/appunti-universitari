/*---
title: "Startup"
description: ""
tags: [università, "Excalidraw", "startup"]
created: 2025-08-04
cssclasses: code
---*/
/*
#exclude
```js*/
app.metadataTypeManager.setType("excalidraw-single-elements-autoexport", "checkbox")

const WIKI_LINK_JSON_PATH = "Excalidraw/wiki-map.json";

const fs = app.vault.adapter;
if (!(await fs.exists(WIKI_LINK_JSON_PATH)))
	app.vault.create(WIKI_LINK_JSON_PATH, '');
let wikiMap = [];
try {
	const json = await fs.read(WIKI_LINK_JSON_PATH);
	if (json.trim()) {
	  wikiMap = JSON.parse(json);
	}
} catch (e) {
	console.warn("Unable to read the wiki-map.json file:", e);
}
	
/**
 * If set, this callback is triggered when the user closes an Excalidraw view.
 *   onViewUnloadHook: (view: ExcalidrawView) => void = null;
 */
//ea.onViewUnloadHook = (view) => {};

/**
 * If set, this callback is triggered, when the user changes the view mode.
 * You can use this callback in case you want to do something additional when the user switches to view mode and back.
 *   onViewModeChangeHook: (isViewModeEnabled:boolean, view: ExcalidrawView, ea: ExcalidrawAutomate) => void = null;
 */
//ea.onViewModeChangeHook = (isViewModeEnabled, view, ea) => {};

/**
 * If set, this callback is triggered, when the user hovers a link in the scene.
 * You can use this callback in case you want to do something additional when the onLinkHover event occurs.
 * This callback must return a boolean value.
 * In case you want to prevent the excalidraw onLinkHover action you must return false, it will stop the native excalidraw onLinkHover management flow.
 *   onLinkHoverHook: (
 *     element: NonDeletedExcalidrawElement,
 *     linkText: string,
 *     view: ExcalidrawView,
 *     ea: ExcalidrawAutomate
 *   ) => boolean = null;
 */
//ea.onLinkHoverHook = (element, linkText, view, ea) => {};
   
/**
 * If set, this callback is triggered, when the user clicks a link in the scene.
 * You can use this callback in case you want to do something additional when the onLinkClick event occurs.
 * This callback must return a boolean value.
 * In case you want to prevent the excalidraw onLinkClick action you must return false, it will stop the native excalidraw onLinkClick management flow.
 *   onLinkClickHook:(
 *     element: ExcalidrawElement,
 *     linkText: string,
 *     event: MouseEvent,
 *     view: ExcalidrawView,
 *     ea: ExcalidrawAutomate
 *   ) => boolean = null;
 */
//ea.onLinkClickHook = (element,linkText,event, view, ea) => {};
   
/**
 * If set, this callback is triggered, when Excalidraw receives an onDrop event. 
 * You can use this callback in case you want to do something additional when the onDrop event occurs.
 * This callback must return a boolean value.
 * In case you want to prevent the excalidraw onDrop action you must return false, it will stop the native excalidraw onDrop management flow.
 *   onDropHook: (data: {
 *     ea: ExcalidrawAutomate;
 *     event: React.DragEvent<HTMLDivElement>;
 *     draggable: any; //Obsidian draggable object
 *     type: "file" | "text" | "unknown";
 *     payload: {
 *       files: TFile[]; //TFile[] array of dropped files
 *       text: string; //string
 *     };
 *     excalidrawFile: TFile; //the file receiving the drop event
 *     view: ExcalidrawView; //the excalidraw view receiving the drop
 *     pointerPosition: { x: number; y: number }; //the pointer position on canvas at the time of drop
 *   }) => boolean = null;
 */
//ea.onDropHook = (data) => {};
 
/**
 * If set, this callback is triggered, when Excalidraw receives an onPaste event.
 * You can use this callback in case you want to do something additional when the
 * onPaste event occurs.
 * This callback must return a boolean value.
 * In case you want to prevent the excalidraw onPaste action you must return false,
 * it will stop the native excalidraw onPaste management flow.
 *   onPasteHook: (data: {
 *     ea: ExcalidrawAutomate;
 *     payload: ClipboardData;
 *     event: ClipboardEvent;
 *     excalidrawFile: TFile; //the file receiving the paste event
 *     view: ExcalidrawView; //the excalidraw view receiving the paste
 *     pointerPosition: { x: number; y: number }; //the pointer position on canvas
 *   }) => boolean = null;
 */
//ea.onPasteHook = (data) => {};

/**
 * if set, this callback is triggered, when an Excalidraw file is opened
 * You can use this callback in case you want to do something additional when the file is opened.
 * This will run before the file level script defined in the `excalidraw-onload-script` frontmatter.
 *   onFileOpenHook: (data: {
 *     ea: ExcalidrawAutomate;
 *     excalidrawFile: TFile; //the file being loaded
 *     view: ExcalidrawView;
 *   }) => Promise<void>;
 */
//ea.onFileOpenHook = (data) => {};

/**
 * if set, this callback is triggered, when an Excalidraw file is created
 * see also: https://github.com/zsviczian/obsidian-excalidraw-plugin/issues/1124
 *   onFileCreateHook: (data: {
 *     ea: ExcalidrawAutomate;
 *     excalidrawFile: TFile; //the file being created
 *     view: ExcalidrawView;
 *   }) => Promise<void>;
 */
//ea.onFileCreateHook = (data) => {}; 

/**
 * If set, this callback is triggered when a image is being saved in Excalidraw.
 * You can use this callback to customize the naming and path of pasted images to avoid
 * default names like "Pasted image 123147170.png" being saved in the attachments folder,
 * and instead use more meaningful names based on the Excalidraw file or other criteria,
 * plus save the image in a different folder.
 * 
 * If the function returns null or undefined, the normal Excalidraw operation will continue
 * with the excalidraw generated name and default path.
 * If a filepath is returned, that will be used. Include the full Vault filepath and filename
 * with the file extension.
 * The currentImageName is the name of the image generated by excalidraw or provided during paste.
 * 
 * @param data - An object containing the following properties:
 *   @property {string} [currentImageName] - Default name for the image.
 *   @property {string} drawingFilePath - The file path of the Excalidraw file where the image is being used.
 * 
 * @returns {string} - The new filepath for the image including full vault path and extension.
 * 
 * Example usage:
 * onImageFilePathHook: (data) => {
 *   const { currentImageName, drawingFilePath } = data;
 *   const ext = currentImageName.split('.').pop();
 *   // Generate a new filepath based on the drawing file name and other criteria
 *   return `${drawingFileName} - ${currentImageName || 'image'}.${ext}`;
 \_ }
 \_ 
 \_ Signiture:
 \_ onImageFilePathHook: (data: {
 \_   currentImageName: string; // Excalidraw generated name of the image, or the name received from the file system.
 \_   drawingFilePath: string; // The full filepath of the Excalidraw file where the image is being used.
 \_ }) => string = null;  
\_/
// ea.onImageFilePathHook = (data) => { console.log(data); };

/\_\_
 \_ If set, this callback is triggered when the Excalidraw image is being exported to 
 \_ .svg, .png, or .excalidraw.
 \_ You can use this callback to customize the naming and path of the images. This allows
 \_ you to place images into an assets folder.
 \_ 
 \_ If the function returns null or undefined, the normal Excalidraw operation will continue
 \_ with the currentImageName and in the same folder as the Excalidraw file
 \_ If a filepath is returned, that will be used. Include the full Vault filepath and filename
 \_ with the file extension.
 \_ !!!! If an image already exists on the path, that will be overwritten. When returning
 \_ your own image path, you must take care of unique filenames (if that is a requirement) !!!!
 \_ The current image name is the name generated by Excalidraw:
 \_ - my-drawing.png
 \_ - my-drawing.svg
 \_ - my-drawing.excalidraw
 \_ - my-drawing.dark.svg
 \_ - my-drawing.light.svg
 \_ - my-drawing.dark.png
 \_ - my-drawing.light.png
 \_ 
 \_ @param data - An object containing the following properties:
 \_   @property {string} exportFilepath - Default export filepath for the image.
 \_   @property {string} excalidrawFile - TFile: The Excalidraw file being exported.
 \_   @property {string} exportExtension - The file extension of the export (e.g., .dark.svg, .png, .excalidraw).
 \_   @property {string} oldExcalidrawPath - If action === "move" The old path of the Excalidraw file, else undefined
 \_   @property {string} action - The action being performed:
 \_        "export" | "move" | "delete"
 \_        move and delete reference the change to the Excalidraw  file.
 \_ 
 \_ @returns {string} - The new filepath for the image including full vault path and extension.
 \_ 
 \_ action === "move" || action === "delete" is only possible if "keep in sync" is enabled
 \_   in plugin export settings
 \_
 \_ Example usage:
 \_ onImageFilePathHook: (data) => {
 \_   const { currentImageName, drawingFilePath, frontmatter } = data;
 \_   // Generate a new filepath based on the drawing file name and other criteria
 \_   const ext = currentImageName.split('.').pop();
 \_   if(frontmatter && frontmatter["my-custom-field"]) {
 \_   }
 \_   return `${drawingFileName} - ${currentImageName || 'image'}.${ext}`;
 * }
 * 
*/
/*ea.onImageExportPathHook =  (data) => {
  //debugger; //remove comment to debug using Developer Console
  
  let {excalidrawFile, exportFilepath, exportExtension, oldExcalidrawPath, action} = data;
  const frontmatter = app.metadataCache.getFileCache(excalidrawFile)?.frontmatter;
  //console.log(data, frontmatter);
  
  const excalidrawFilename = action === "move"
    ? ea.splitFolderAndFilename(excalidrawFile.name).filename
    : excalidrawFile.name

  if(excalidrawFilename.match(/^icon - /i)) {
    const {folderpath, filename, basename, extension} = ea.splitFolderAndFilename(exportFilepath);
    exportFilepath = "assets/icons/" + filename;
    return exportFilepath;
  }
    
  if(excalidrawFilename.match(/^stickfigure - /i)) {
    const {folderpath, filename, basename, extension} = ea.splitFolderAndFilename(exportFilepath);
    exportFilepath = "assets/stickfigures/" + filename;
    return exportFilepath;
  }
    
  if(excalidrawFilename.match(/^logo - /i)) {
    const {folderpath, filename, basename, extension} = ea.splitFolderAndFilename(exportFilepath);
    exportFilepath = "assets/logos/" + filename;
    return exportFilepath;
  }

	// !!!! frontmatter will be undefined when action === "delete"
	// this means if you base your logic on frontmatter properties, then 
	// plugin settings keep files in sync will break for those files when
	// deleting the Excalidraw file. The images will not be deleted, or worst
	// your logic might result in deleting other files. This hook gives you
	// powerful control, but the hook function logic requires careful testing
	// on your part.
  //if(frontmatter && frontmatter["is-asset"]) { //custom frontmatter property
    exportFilepath = ea.obsidian.normalizePath("assets/" + exportFilepath);
    return exportFilepath;
  //}

  return exportFilepath;
};*/

function isExportFrame(frame){
	return (frame.customData.export?.updated !== undefined);
}

function isExportFrameUpdated(frame, elementsInside) {
	const exportUpdated = frame.customData?.export?.updated;
	if (!exportUpdated) return true;
	
	if (frame.updated > exportUpdated) return true;
	
	for (const el of elementsInside) {
		if (el.updated > exportUpdated) return true;
	}
	
	return false;
}


function updateExportTimestamp(frame) {
	if (!frame.customData.export) {
		frame.customData.export = {};
	}
	frame.customData.export.updated = Date.now();
}

function buildFrameElementsMap(allElements) {
	const frameMap = new Map();
	
	const exportFrames = allElements.filter((el) =>
		el.type === "frame" && isExportFrame(el)
	);
	
	for (const frame of exportFrames) {
		frameMap.set(frame.id, { frame, elements: new Set() });
	}
	
	for (const element of allElements) {
		if (exportFrames.some(frame => frame.id === element.id)) continue;
		for (const frame of exportFrames) {
			if (
				frame.x <= element.x &&
				frame.x + frame.width >= element.x + element.width &&
				frame.y <= element.y &&
				frame.y + frame.height >= element.y + element.height
				) {
				
				frameMap.get(frame.id).elements.add(element);
				//break; // supponiamo che un elemento sia in un solo frame
			}
		}
	}
	return frameMap;
}


function updateWikiMapInMemory(sourcePath, wikilink, svglink, frameId) {
  const existing = wikiMap.find(entry => entry.wikilink === wikilink);
  if (existing) {
    existing.svglink = svglink;
  } else {
    wikiMap.push({ wikilink, svglink, source: sourcePath, frameId });
  }
}

function removeInconsistentWikiFrames(currentViewFramesMap, source){
	wikiMap = wikiMap.filter(item => currentViewFramesMap.has(item.frameId) || item.source !== source);
}


async function exportElementsToSvg({ frame, elements, view}) {
	const exportData = frame.customData.export;
	const options = exportData.options;
	const outputPath = exportData.rootFolder + exportData.filename + '.' + exportData.format;
	
	const scene = {
		elements,
		appState: {
			...view.getScene().appState,
			theme: view.getViewExportTheme(),
			exportEmbedScene: view.getViewExportEmbedScene(),
		},
		files: {},
	};
	
	const export_args = {
		elements: scene.elements,
		appState: {
			...scene.appState,
			exportBackground: options.withBackground,
			exportWithDarkMode: !!options.withTheme && scene.appState.theme !== "light",
		},
		files: scene.files,
		exportPadding: options.padding,
		exportingFrame: null,
		renderEmbeddables: true,
		skipInliningFonts: options.skipInliningFonts,
	};
	
	const svgElement = await ExcalidrawLib.exportToSvg(export_args);
	if (!svgElement) {
		new Notice("Error during SVG export.");
		return;
	}
	
	await app.vault.adapter.write(outputPath, svgElement.outerHTML);
	
	const sourcePath = view.file.path;
	const frameId = frame.id;
	
	const wikilink = `![[${sourcePath}#^frame=${frameId}]]`;
	const svglink = `![${exportData.filename}](/${outputPath})`;
	
	updateWikiMapInMemory(sourcePath, wikilink, svglink, frameId)
	
	updateExportTimestamp(frame)
	new Notice(`SVG saved in:\n${outputPath}`);
}


async function saveWikiMap() {
  try {
    await fs.write(WIKI_LINK_JSON_PATH, JSON.stringify(wikiMap, null, 2));
  } catch (e) {
    new Notice("Error while saving the wiki map.");
    console.error(e);
  }
}


ea.onTriggerAutoexportHook = (data) => {
	let { excalidrawFile } = data;
	const frontmatter = app.metadataCache.getFileCache(excalidrawFile)?.frontmatter;
	
	if (!frontmatter?.["excalidraw-single-elements-autoexport"]) return;
	
	const view = ea.setView("active");
	if (view.file.path !== excalidrawFile.path) return;
	
	void (async () => {
		try {
			const frameMap = buildFrameElementsMap(view.getViewElements());
			await removeInconsistentWikiFrames(frameMap, view.file.path)
			for (const { frame, elements: inside } of frameMap.values()) {
				if (isExportFrameUpdated(frame, inside)) {
					await exportElementsToSvg({ frame, elements: Array.from(inside) , view});
				}
			}
		} catch (err) {
			console.error("Error in automatic export:", err);
		}
		await saveWikiMap()
	})();
	
};



/**
 * Excalidraw supports auto-export of Excalidraw files to .png, .svg, and .excalidraw formats.
 * 
 * Auto-export of Excalidraw files can be controlled at multiple levels.
 * 1) In plugin settings where you can set up default auto-export applicable to all your Excalidraw files.
 * 2) However, if you do not want to auto-export every file, you can also control auto-export
 *    at the file level using the 'excalidraw-autoexport' frontmatter property.
 * 3) This hook gives you an additional layer of control over the auto-export process.
 * 
 * This hook is triggered when an Excalidraw file is being saved.
 * 
 * interface AutoexportConfig {
 *   png: boolean; // Whether to auto-export to PNG
 *   svg: boolean; // Whether to auto-export to SVG
 *   excalidraw: boolean; // Whether to auto-export to Excalidraw format
 *   theme: "light" | "dark" | "both"; // The theme to use for the export
 * }
 *
 * @param {Object} data - The data for the hook.
 * @param {AutoexportConfig} data.autoexportConfig - The current autoexport configuration.
 * @param {TFile} data.excalidrawFile - The Excalidraw file being auto-exported.
 * @returns {AutoexportConfig | null} - Return a modified AutoexportConfig to override the export behavior, or null to use the default.
*/
/*ea.onTriggerAutoexportHook = (data) => {
  let {autoexportConfig, excalidrawFile} = data;
  const frontmatter = app.metadataCache.getFileCache(excalidrawFile)?.frontmatter;
  //console.log(data, frontmatter);
  //logic based on filepath and frontmatter
  if(excalidrawFile.name.match(/^(?:icon|stickfigure|logo) - /i)) {
    autoexportConfig.theme = "light"; 
    autoexportConfig.svg = true;
    autoexportConfig.png = false;
    autoexportConfig.excalidraw = false;
    return autoexportConfig;
  }
  return autoexportConfig;
};*/

/**
 * If set, this callback is triggered whenever the active canvas color changes
 *   onCanvasColorChangeHook: (
 *     ea: ExcalidrawAutomate,
 *     view: ExcalidrawView, //the excalidraw view 
 *     color: string,
 *   ) => void = null;
*/
//ea.onCanvasColorChangeHook = (ea, view, color) => {};
