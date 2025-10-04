/*---
title: Export Selection To Svg
description: Esporta gli elementi selezionati in Excalidraw come SVG e copia il link markdown negli appunti
tags:
  - Excalidraw
  - Scripts
  - export
  - export-selection-to-svg
created: 2025-07-04
cssclasses:
  - code
---*/

/*
```javascript */

const EXPORT_FORMATS = ["svg"];
const EXPORT_FRAME_PREFIX = "to";

const EXPORT_DEFAULT_OPTIONS = {
	  withBackground: false,
	  withTheme: true,
	  skipInliningFonts: false,
	  padding: 10
};

const EXPORT_DEFAULT_FOLDER = "assets"
const EXPORT_DEFAULT_FILE = {
	filename: "asset",
	format: "svg"
}

const Logger = (function () {
	const levels = ["debug", "info", "notice", "warn", "error"];
	let currentLevel = "notice";
	
	function shouldLog(level) {
		return levels.indexOf(level) >= levels.indexOf(currentLevel);
	}
	
	return {
		setLevel(level) {
		  if (levels.includes(level)) currentLevel = level;
		},
		debug(...args) {
		  if (shouldLog("debug")) console.debug("[DEBUG]", ...args);
		},
		info(...args) {
		  if (shouldLog("info")) console.info("[INFO]", ...args);
		},
		notice(...args) {
		  if (shouldLog("notice")) {
			  new Notice(...args);
		  };
		},
		noticeAndWarn(){
			if (shouldLog("notice")) {
				new Notice(...args);
				console.warn("[WARN]", ...args);
			};
		},
		warn(...args) {
			if (shouldLog("warn")) console.warn("[WARN]", ...args);
		},
		error(...args) {
			if (shouldLog("error")) console.error("[ERROR]", ...args);
		},
	};
})();

//Logger.setLevel("debug");

const view = app.workspace.activeLeaf?.view;
const activeFile = view?.file;

if (!view || !activeFile || view.getViewType() !== "excalidraw") {
	Logger.notice("Open an Excalidraw file before running this script.");
	return;
}

ea.setView("active");
const api = ea.getExcalidrawAPI();

const fs = app.vault.adapter;
const path = activeFile.parent.path;
const EXPORT_FULL_DEFAULT_FOLDER_PATH = `${path}/${EXPORT_DEFAULT_FOLDER}`;


function sanitizeFilename(name) {
	const invalidChars = /[<>:"|?*.\s]/;
	if (invalidChars.test(name)) {
		Logger.noticeAndWarn("Invalid name for export file name.\n Illegal characters: " + invalidChars);
		return null;
	}
	
	return name.trim()
		.toLowerCase()
		.replace(/^_+|_+$/g, "")
		.replace(/(\\\\)/, "/")
		.replace(/(\/\/)/, "/")
		.replace(/[\\]/, "/") || "frame";
}

function getExportFileName(exportFile){
	return exportFile.filename + '.' + exportFile.format;
}

function buildExportFileNameControls(container, state) {
	new ea.obsidian.Setting(container)
		.setName("File name")
		.addText(text =>
			text
				.setValue(state.filename)
				.onChange(value => state.filename = value)
		);
	
	new ea.obsidian.Setting(container)
		.setName("Format")
		.addDropdown(dropdown =>
			dropdown
				.addOptions(Object.fromEntries(EXPORT_FORMATS.map(f => [f, f])))
				.setValue(state.format)
				.onChange(value => state.format = value)
		);
	
	const activeFile = app.workspace.getActiveFile();
	if (!activeFile) return;
	
	const activeFolder = app.vault.getAbstractFileByPath(activeFile.parent.path);
	if (!(activeFolder instanceof ea.obsidian.TFolder)) return;
	
	const subfolders = activeFolder.children
		.filter(f => f instanceof ea.obsidian.TFolder)
		.map(f => f);
	
	const allFolders = [activeFolder, ...subfolders];
	
	const folderOptions = Object.fromEntries(allFolders.map(folder => [
		folder.path + '/',
		folder.name === activeFolder.name ? `${folder.name} (current)` : folder.name
	]));
	
	const defaultFolderPath = activeFolder.path;
	if (!state.rootFolder) state.rootFolder = defaultFolderPath;
	new ea.obsidian.Setting(container)
		.setName("Save folder")
		.setDesc("Select a folder within the active file folder.")
		.addDropdown(dropdown => {
			dropdown
				.addOptions(folderOptions)
				.setValue(
					Object.keys(folderOptions).find(
						key => key.replace(/\/$/, "") === state.rootFolder.replace(/\/$/, "")
					) ?? Object.keys(folderOptions)[0]
				)
				.onChange(value => state.rootFolder = value);
		});

}


async function promptExportFileName(){
	const state = {
		filename: "asset",
		format: "svg",
		rootFolder: EXPORT_FULL_DEFAULT_FOLDER_PATH + '/'
	};

	const controls = (container) => {
		buildExportFileNameControls(container, state)
	};
	
	const confirmed = await utils.inputPrompt(
		"Export file",
		null, null, null, 1, false,
		controls,
		true, true, false
	);
	if (confirmed !== null) return null;
	if (!state.filename || state.filename.trim() === "") {
		Logger.notice("File name not valid.");
		return null;
	}
	if (!state.rootFolder) {
		Logger.notice("Destination folder not selected.");
		return;
	}
	
	console.assert(state.rootFolder[state.rootFolder.length - 1] === '/')
	return {
		filename: sanitizeFilename(state.filename),
		format: state.format,
		rootFolder: state.rootFolder
	};    
}

function buildExportOptionControls(container, state) {
	new ea.obsidian.Setting(container)
	    .setName("Include background")
	    .addToggle(toggle =>
	      toggle
	        .setValue(state.withBackground)
	        .onChange(value => state.withBackground = value)
	    );
	
	new ea.obsidian.Setting(container)
	    .setName("keep theme")
	    .addToggle(toggle =>
	      toggle
	        .setValue(state.withTheme)
	        .onChange(value => state.withTheme = value)
	    );
	
	new ea.obsidian.Setting(container)
	    .setName("Skip inlining font")
	    .addToggle(toggle =>
	      toggle
	        .setValue(state.skipInliningFonts)
	        .onChange(value => state.skipInliningFonts = value)
	    );
	
	new ea.obsidian.Setting(container)
	    .setName("Padding (px)")
	    .addText(text =>
	      text
	        .setValue(state.padding)
	        .onChange(value => state.padding = value)
	    );
}

/**
 * Estrae formato e nome file da un frame
 * @param {string} frameName - esempio: "toSVG: computer.svg"
 * @returns {{format: string, filename: string} | null}
 */
function parseExportFrameName(frameName) {
	const regex = new RegExp(`^${EXPORT_FRAME_PREFIX}(${EXPORT_FORMATS.map(f => f.toUpperCase()).join('|')}):\\s*(.+)$`);
	const match = frameName.match(regex);
	
	if (!match) {
		Logger.notice("It was not possible to identify a known pattern in the frame name.");
		return null;
	}
	
	const format = match[1].toLowerCase();
	const rawPath = match[2].trim();
	
	const pathWithoutExt = rawPath.replace(/\.[^.\s]+$/, '');
	
	const lastSlash = pathWithoutExt.lastIndexOf('/');
	const rootFolder = path + '/' +  (lastSlash !== -1 ? pathWithoutExt.slice(0, lastSlash + 1): '');
	const filename = lastSlash !== -1 ? pathWithoutExt.slice(lastSlash + 1) : pathWithoutExt;
	console.assert(rootFolder[rootFolder.length - 1] === '/', rootFolder)
	return { format, rootFolder, filename};
}



async function promptExportOptions(initial = {}) {
	
	const state = {
	    withBackground: initial.withBackground ?? EXPORT_DEFAULT_OPTIONS.withBackground,
	    withTheme: initial.withTheme ?? EXPORT_DEFAULT_OPTIONS.withTheme,
	    skipInliningFonts: initial.skipInliningFonts ?? EXPORT_DEFAULT_OPTIONS.skipInliningFonts,
	    padding: initial.padding?.toString() ?? EXPORT_DEFAULT_OPTIONS.padding.toString()
	};
	const customControls = (container) => {
		buildExportOptionControls(container, state);
	};
	
	const confirmed = await utils.inputPrompt(
		"Edit export options", // header
		null,                  // placeholder: string
		null,                  // value: string
		null,                  // buttons
		1,                     // lines: number
		false,                 // displayEditorButtons
		customControls,        // customComponents
		true,                  // blockPointerInputOutsideModal
		true,                  // controlsOnTop
		false                  // draggable
	);
	
	if (confirmed === null){
		const parsedPadding = parseInt(state.padding);
		if (isNaN(parsedPadding)) {
			Logger.noticeAndWarn("Invalid padding value.");
			return null;
		}
		return {
			withBackground: state.withBackground,
			withTheme: state.withTheme,
			skipInliningFonts: state.skipInliningFonts,
			padding: parsedPadding
		};
	}
	return null;
}

async function copyToClipboard(frameId){
	const markdown = `![[${activeFile.path}#^frame=${frameId}]]`
	await navigator.clipboard.writeText(markdown);
	Logger.notice(`Copied to clipboard`);
}

async function promptEditExportFrame(frame) {
	const currentFilename = frame?.name || "";
	const exportData = frame?.customData?.export || {};
	
	const state = {
		filename: exportData.filename || EXPORT_DEFAULT_FILE.filename,
		format: exportData.format || EXPORT_DEFAULT_FILE.format,
		rootFolder: exportData.rootFolder || EXPORT_FULL_DEFAULT_FOLDER_PATH + '/',
		withBackground: exportData.options?.withBackground ?? EXPORT_DEFAULT_OPTIONS.withBackground,
		withTheme: exportData.options?.withTheme ?? EXPORT_DEFAULT_OPTIONS.withTheme,
		skipInliningFonts: exportData.options?.skipInliningFonts ?? EXPORT_DEFAULT_OPTIONS.skipInliningFonts,
		padding: exportData.options?.padding?.toString() ?? EXPORT_DEFAULT_OPTIONS.padding.toString() 
	};
	
	const controls = (container) => {
		buildExportFileNameControls(container, state);
		
		buildExportOptionControls(container, state);
		
		new ea.obsidian.Setting(container)
			.addButton(btn =>
				btn.setButtonText("📋 Copy link")
				.setCta()
				.onClick(async () => {
				copyToClipboard(frame.id)
				})
		);
	};
	
	const confirmed = await utils.inputPrompt(
		"Edit export variables",
		null, null, null, 1, false,
		controls,
		true, true, false
	);
	
	if (confirmed === null) {
		const parsedPadding = parseInt(state.padding);
		if (isNaN(parsedPadding)) {
			Logger.noticeAndWarn("Invalid padding value.");
			return null;
		}

		return {
			filename: state.filename,
			format: state.format,
			rootFolder: state.rootFolder,
			options: {
				withBackground: state.withBackground,
				withTheme: state.withTheme,
				skipInliningFonts: state.skipInliningFonts,
				padding: parsedPadding
			}
		};
	}
	return null;
}


function updateElementsInScene(updatedElementsArray) {
	const allElements = ea.getViewElements();
	
	const updatedMap = new Map(updatedElementsArray.map(el => [el.id, el]));
	
	const existingIds = new Set(allElements.map(el => el.id));
	
	const mergedScene = allElements.map(el =>
	updatedMap.has(el.id) ? updatedMap.get(el.id) : el
	);
	
	const newElements = updatedElementsArray.filter(el => !existingIds.has(el.id));
	
	const finalScene = [...mergedScene, ...newElements];
	
	api.updateScene({ elements: finalScene });
}




function getSingleFrameFullySelected({ elements, allElements }, debug = false) {
	const selectedFrame = elements.find(el => el.type === "frame");
	if (!selectedFrame) return { frame: null };
	
	const frameElements = allElements.filter(el =>
		el.frameId === selectedFrame.id && !el.isDeleted
	);
	
	const selectedNonFrameElements = elements.filter(el => el.id !== selectedFrame.id);
	if (debug){
		Logger.debug(`Selected non frame elements:`)
		Logger.debug(selectedNonFrameElements)
	}
	
	const sameLength = selectedNonFrameElements.length === frameElements.length;
	const sameContent = selectedNonFrameElements.every(el =>
		frameElements.some(f => f.id === el.id)
	);
	
	if (debug){
		Logger.debug(`Selected frame elements: ${selectedNonFrameElements.length}`);
		Logger.debug(`Global frame elements: ${frameElements.length}`);
		Logger.debug(`Same length: ${sameLength}, Same content: ${sameContent}`);
	}
	
	const isFullySelected = sameLength && sameContent;
	return { singleFrameFullySelected: isFullySelected ? selectedFrame : null };
}

function getBigFrameFullySelected({ elements, allElements }, debug = false) {
	const onlyFrames = elements.filter(el => el.type === "frame");
	if (onlyFrames.length === 0){
		if (debug){
		Logger.debug(`----- Final analysis of getBigFrameFullySelected -----`)
		Logger.debug(`Frame fully selected: false`);
		Logger.debug(`Largest frame: null`);
		Logger.debug(`----- End analysis of getBigFrameFullySelected -----`)
		}
		return { singleFrameFullySelected: null };
	}
	let largestFrame = null;
	
	if (onlyFrames.length > 0) {
		largestFrame = onlyFrames.reduce((largest, current) => {
			const areaCurrent = current.width * current.height;
			const areaLargest = largest.width * largest.height;
			return areaCurrent > areaLargest ? current : largest;
		});
	}
	const allElementsInsideLargestFrame = elements.every(element => 
	  largestFrame.x <= element.x &&
	  largestFrame.x + largestFrame.width >= element.x + element.width &&
	  largestFrame.y <= element.y &&
	  largestFrame.y + largestFrame.height >= element.y + element.height
	);
	
	if (debug){
		Logger.debug(`----- Final analysis of getBigFrameFullySelected -----`)
		Logger.debug(`Frame fully selected: ${allElementsInsideLargestFrame}`);
		Logger.debug(`Largest frame: ${largestFrame.id}`);
		Logger.debug(`----- End analysis of getBigFrameFullySelected -----`)
	}
	
	return { singleFrameFullySelected: allElementsInsideLargestFrame ? largestFrame : null };
	
}

function generateExportFrameName(exportFile){
	return EXPORT_FRAME_PREFIX + exportFile.format.toUpperCase() + ": " + exportFile.rootFolder.substr(path.length + 1) + exportFile.filename + "." + exportFile.format 
}


function wrapElementsInFrame({selectedElements, singleFrameFullySelected, exportFile, ea}, debug = false) {
	let minX;
	let minY;
	let maxX  
	let maxY;
	const padding = 120;
	
	let updatedElements;
	let frame;
	if (debug){
		Logger.debug(`Already in a fully selected frame: ${!!singleFrameFullySelected}`)
	}
	if (!!singleFrameFullySelected){
		const elementsButFrame = selectedElements.filter(el => el.id !== singleFrameFullySelected.id)
		
		minX = Math.min(...elementsButFrame.map(el => el.x));
		minY = Math.min(...elementsButFrame.map(el => el.y));
		maxX = Math.max(...elementsButFrame.map(el => el.x + el.width));
		maxY = Math.max(...elementsButFrame.map(el => el.y + el.height));
		if (elementsButFrame.length !== 0){
			frame = {
				...singleFrameFullySelected,
				frameId: null,
				x: minX - padding,
				y: minY - padding,
				width: maxX - minX + 2 * padding,
				height: maxY - minY + 2 * padding
			};
		}else{
			frame = {...singleFrameFullySelected}
		}
		
		frame = {...frame,
				customData:{
					...frame.customData,
					export: {
						...((frame.customData || {}).export || {}),
						filename: exportFile.filename,
						format: exportFile.format,
						rootFolder: exportFile.rootFolder
					}
				},
				name: generateExportFrameName(exportFile)
				}
		
		updatedElements = selectedElements.map(el =>
			el.id === singleFrameFullySelected.id ? frame : {
				...el,
				frameId: frame.id
			}
		);
			
	} else {
		minX = Math.min(...selectedElements.map(el => el.x));
		minY = Math.min(...selectedElements.map(el => el.y));
		maxX = Math.max(...selectedElements.map(el => el.x + el.width));
		maxY = Math.max(...selectedElements.map(el => el.y + el.height));
		
		frame = {
			id: ea.generateElementId(),
			type: "frame",
			x: minX - padding,
			y: minY - padding,
			width: maxX - minX + 2 * padding,
			height: maxY - minY + 2 * padding,
			angle: 0,
			strokeColor: "#bbb",
			backgroundColor: "transparent",
			fillStyle: "solid",
			strokeStyle: "solid",
			strokeWidth: 2,
			roughness: 0,
			opacity: 100,
			groupIds: [],
			frameId: null,
			roundness: null,
			seed: Math.floor(Math.random() * 100000),
			version: 1,
			versionNonce: Math.floor(Math.random() * 1000000000),
			isDeleted: false,
			boundElements: [],
			updated: Date.now(),
			locked: false,
			customData: {
				frameColor: {
					stroke: "#2B2B2B",
					fill: "#525252",
					nameColor: "#858585"
				},
				export: {
					filename: exportFile.filename,
					format: exportFile.format,
					rootFolder: exportFile.rootFolder
				}
			},
			name: generateExportFrameName(exportFile)
		};
		
		updatedElements = [
			...selectedElements.map(el => ({
				...el,
				frameId: frame.id
			}))
		];
	}
	
	return {
		singleFrameFullySelected: frame,
	    updatedElements: [...updatedElements, frame]
	};
}

/*
async function getNextAvailableFilename(folderPath, fileName) {
	const files = app.vault.getFiles();
	const folderFiles = files.filter(f => f.path.startsWith(folderPath));
	
	formatRegExp = new RegExp(`\.[^!.]+$`);
	format = ea.targetView.file.name.match(formatRegExp)
	prefix = ea.targetView.file.name.replace(/\..+$/, "");
	
	const regex = new RegExp(`^${prefix}_(\\d{3})\\.svg$`);
	
	let maxIndex = 0;
	for (const file of folderFiles) {
		const baseName = file.name;
		const match = baseName.match(regex);
		if (match) {
		  const num = parseInt(match[1], 10);
		  if (num > maxIndex) maxIndex = num;
		}
	}
	
	const nextIndex = (maxIndex + 1).toString().padStart(3, "0");
	return `${prefix}_${nextIndex}.${EXPORT_FORMAT}`;
}
*/




// Funzione per ottenere un nome file valido (da frame o da prompt)
async function resolveFilename({ singleFrameFullySelected, ea }, debug = false) {
	
    if (!!singleFrameFullySelected && singleFrameFullySelected.name){
	    const exportFile = parseExportFrameName(singleFrameFullySelected.name);
	    
	    if (!exportFile) return await promptExportFileName();
	    let { format, filename } = exportFile;
	    return {format, filename: sanitizeFilename(filename), rootFolder: exportFile.rootFolder};
	}
	
	return await promptExportFileName();
	
}

function getAllInheritedElements({elements, ea}){
	
	const allElements = ea.getViewElements();
	const onlyFrames = elements.filter(el => el.type === "frame");
	let newElements = new Set();
	onlyFrames.forEach( (frame) => {
		allElements.filter(element => 
			frame.x <= element.x &&
			frame.x + frame.width >= element.x + element.width &&
			frame.y <= element.y &&
			frame.y + frame.height >= element.y + element.height
		).forEach((element) => {
			newElements.add(element)
		})
	});
	if (onlyFrames.length == 0){
		elements.forEach( (element) => {
			newElements.add(element);
		})
	}
	
	return Array.from(newElements)
}

function isExportFrame(frame){
	return (frame.customData.export !== undefined);
}

function getExportOptionFromFrame(frame){
	return frame.customData.export?.options;
}

function updateFrameExportInformation(frame, metadata= {}) {
	frame = {
		...frame,
		customData: {
			...(frame.customData || {}),
			export: {
				...((frame.customData || {}).export || {}),
				...metadata,
				updated: 0
			}
		}
	};
	
	updateElementsInScene([frame]);
	
	return frame
}

/*-----------------------------START MAIN CODE------------------------------------*/

let selectedElements = getAllInheritedElements({elements:ea.getViewSelectedElements(), ea});
let allElements = ea.getViewElements();

Logger.debug(`Selected items:`);
Logger.debug(selectedElements);




if (!selectedElements.length) {
	Logger.notice("No items selected.");
	return;
}else if (selectedElements.length === 1 && selectedElements[0].type == "frame"){
	
	Logger.notice("The selected frame is empty.");
	return;
}


if (!(await fs.exists(EXPORT_FULL_DEFAULT_FOLDER_PATH))) {
	await fs.mkdir(EXPORT_FULL_DEFAULT_FOLDER_PATH);
}

let { singleFrameFullySelected } = getBigFrameFullySelected({
	elements: selectedElements,
	allElements: ea.getViewElements()},
	debug = !1
);

let defaultExportOptions;

let finalFrame;

let exportFile;
let exportFrame;

if (!singleFrameFullySelected || !isExportFrame(singleFrameFullySelected)){
	
	exportFile = await resolveFilename({ singleFrameFullySelected, ea }, !!1);
	
	if (!exportFile) {
		Logger.notice(`Operation canceled.`);
		return;
	}
	
	if (await app.vault.adapter.exists(exportFile.rootFolder.concat(getExportFileName(exportFile)))) {
	  Logger.notice(`The ${exportFile.rootFolder.concat(getExportFileName(exportFile))} already exists.\nExport process aborted.`);
	  return;
	}
	
	
	Logger.debug("Multiple frame selection detected or the current frame is not an export frame");
	let { singleFrameFullySelected: wrappedFrame, updatedElements } = wrapElementsInFrame({
			selectedElements,
			singleFrameFullySelected,
			exportFile,
			ea
	}, !1);
	
	updateElementsInScene(updatedElements)
	
	Logger.debug("Selected elements + frame:")
	Logger.debug(updatedElements);
	singleFrameFullySelected = wrappedFrame
	selectedElements = updatedElements;
	
	api.selectElements([wrappedFrame]);
	
	defaultExportOptions = EXPORT_DEFAULT_OPTIONS;
	finalFrame = wrappedFrame;
	
	
	
	const options = await promptExportOptions(defaultExportOptions);
	if (!options) {
		Logger.notice("Export process aborted.");
		return;
	}
	Logger.debug("Selected export options:", options);
	
	exportFrame = updateFrameExportInformation(finalFrame, {options: options})

}else {
	Logger.debug("Current frame selected is an export frame");
	defaultExportOptions = getExportOptionFromFrame(singleFrameFullySelected)
	finalFrame = singleFrameFullySelected;
	const editResult = await promptEditExportFrame(finalFrame);
	if (!editResult) {
		Logger.notice("Changes canceled.");
		return;
	}
	exportFile = {filename: editResult.filename, format: editResult.format, rootFolder: editResult.rootFolder}
	
	if (parseExportFrameName(finalFrame.name) !== null)
		finalFrame.name = generateExportFrameName(exportFile);
	
	exportFrame = updateFrameExportInformation(finalFrame, editResult);	
}

Logger.debug("Export file:");
Logger.debug(exportFile);
Logger.debug("Export frame:");
Logger.debug(exportFrame);


copyToClipboard(exportFrame.id)
view.forceSave();



