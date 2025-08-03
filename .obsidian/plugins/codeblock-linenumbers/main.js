"use strict";
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// src/main.ts
var main_exports = {};
__export(main_exports, {
  default: () => CodeblockLineNumbersPlugin
});
module.exports = __toCommonJS(main_exports);
var import_obsidian = require("obsidian");
var import_view = require("@codemirror/view");
var EditorLineNumberMarker = class extends import_view.GutterMarker {
  constructor(number) {
    super();
    this.number = number;
  }
  eq(other) {
    return this.number === other.number;
  }
  toDOM() {
    const div = document.createElement("div");
    div.textContent = String(this.number);
    div.className = "obs-code-line-number-editor";
    return div;
  }
};
var CodeblockLineNumbersPlugin = class extends import_obsidian.Plugin {
  constructor() {
    super(...arguments);
    this.codeBlocks = [];
  }
  onload() {
    this.injectCss();
    this.registerMarkdownPostProcessor((el, ctx) => {
      this.decorateCodeblocksInPreview(el, ctx);
    });
    this.registerEditorExtension([
      createEditorViewPlugin(this),
      (0, import_view.gutter)({
        class: "obs-code-gutter-editor",
        lineMarker: (view, line) => {
          const lineNumber = view.state.doc.lineAt(line.from).number;
          for (const block of this.getCodeBlocksFromEditor(view.state.doc)) {
            if (lineNumber > block.from && lineNumber < block.to) {
              return new EditorLineNumberMarker(lineNumber - block.from);
            }
          }
          return null;
        }
      })
    ]);
  }
  // ----------- Preview Mode Utilities -----------
  getAtomicNodes(element) {
    if (element.nodeType == Node.TEXT_NODE) {
      const text = element.textContent || "";
      if (text.includes("\n")) {
        let newLineElements = [];
        if (text.substring(0, text.search("\n")) != "")
          newLineElements.push(document.createTextNode(text.substring(0, text.search("\n"))));
        for (let i = 0; i < (text.match(/\n/g) || []).length; i++) {
          newLineElements.push(document.createTextNode("\n"));
        }
        if (text.substring(text.lastIndexOf("\n") + 1) != "")
          return [...newLineElements, document.createTextNode(text.substring(text.lastIndexOf("\n") + 1))];
        return newLineElements;
      }
      return [element];
    }
    let atomicChildren = [];
    element.childNodes.forEach((child) => {
      atomicChildren = atomicChildren.concat(this.getAtomicNodes(child));
    });
    return atomicChildren;
  }
  findLineRoot(node) {
    if (!node.parentElement || node.parentElement.textContent?.includes("\n")) {
      return node;
    }
    return this.findLineRoot(node.parentElement);
  }
  formatLineContent(nodes) {
    const wrapper = document.createElement("div");
    wrapper.className = "obs-code-line-preview-content";
    nodes.forEach((n) => {
      if (n instanceof Node)
        wrapper.appendChild(n);
    });
    return wrapper;
  }
  splitCodeblockByLine(codeBlock) {
    const lines = [];
    const atomicNodes = this.getAtomicNodes(codeBlock);
    let buffer = [];
    atomicNodes.forEach((node) => {
      if (node.textContent === "\n") {
        lines.push(this.formatLineContent([...buffer]));
        buffer = [];
      } else {
        buffer.push(this.findLineRoot(node));
      }
    });
    if (buffer.length) {
      lines.push(this.formatLineContent(buffer));
    }
    return lines;
  }
  decorateCodeblocksInPreview(el, ctx) {
    requestAnimationFrame(() => {
      el.querySelectorAll("pre code").forEach((codeBlock) => {
        const pre = codeBlock.parentElement;
        if (!pre || pre.classList.contains("frontmatter"))
          return;
        const langMatch = codeBlock.className.match(/language-(\w+)/);
        if (!langMatch)
          return;
        const lines = this.splitCodeblockByLine(codeBlock);
        const wrapper = document.createElement("div");
        wrapper.className = "obs-codeblock-preview";
        lines.forEach((lineContent, index) => {
          const lineRow = document.createElement("div");
          lineRow.className = "obs-code-line-preview-wrapper";
          const lineNumber = document.createElement("span");
          lineNumber.className = "obs-code-line-number-preview";
          lineNumber.textContent = String(index + 1);
          lineRow.appendChild(lineNumber);
          lineRow.appendChild(lineContent);
          wrapper.appendChild(lineRow);
        });
        pre.parentElement?.replaceChild(wrapper, pre);
      });
    });
  }
  // ----------- Editor Mode Utilities -----------
  getCodeBlocksFromEditor(doc) {
    const blocks = [];
    let openLine = null;
    for (let i = 1; i <= doc.lines; i++) {
      const line = doc.line(i).text.trim();
      if (line.startsWith("```")) {
        if (openLine === null) {
          openLine = i;
        } else {
          blocks.push({ from: openLine, to: i });
          openLine = null;
        }
      }
    }
    if (openLine !== null) {
      blocks.push({ from: openLine, to: doc.lines });
    }
    return blocks;
  }
  updateEditorGutter(view) {
    this.codeBlocks = this.getCodeBlocksFromEditor(view.state.doc);
    let maxLines = 0;
    for (const block of this.codeBlocks) {
      const count = block.to - block.from - 1;
      if (count > maxLines)
        maxLines = count;
    }
    const digits = Math.max(2, Math.floor(Math.log10(maxLines || 1)) + 1);
    const gutter2 = view.dom.querySelector(".obs-code-gutter-editor");
    if (gutter2) {
      gutter2.classList.remove("width-1", "width-2", "width-3", "width-4", "width-5", "width-6");
      gutter2.classList.add(`width-${digits}`);
    }
  }
  injectCss() {
    this.registerDomEvent(document, "DOMContentLoaded", () => {
      const link = document.createElement("link");
      link.rel = "stylesheet";
      link.type = "text/css";
      link.href = this.app.vault.adapter.getResourcePath(this.manifest.dir + "/styles.css");
      document.head.appendChild(link);
    });
  }
};
function createEditorViewPlugin(plugin) {
  return import_view.ViewPlugin.fromClass(
    class {
      constructor(view) {
        plugin.updateEditorGutter(view);
      }
      update(update) {
        if (update.docChanged || update.view.viewport.from !== update.view.viewport.to) {
          plugin.updateEditorGutter(update.view);
        }
      }
    }
  );
}
