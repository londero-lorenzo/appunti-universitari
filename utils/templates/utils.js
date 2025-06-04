class Utils {
	split_and_capitolize(str, c){
		let words = str.split(c)
		return words
			.map((word, idx) => {
				return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
			})
			.join(c)
	}
	
  formatTitle(str) {
    const lowerWords = ["di", "del", "della", "dei", "degli", "delle", "a", "con", "in", "su", "per", "tra", "fra", "e", "o"];
    let words = str.replace(/_/g, " ").split(" ");
    return words
      .map((word, idx) => {
        if (lowerWords.includes(word.toLowerCase()))
          return word.toLowerCase();
        return this.split_and_capitolize(word, '-')
      })
      .join(" ");
  }

  formatTagsFromPath(file_path) {
    const parts = file_path.split("/");
    const tags = parts.map(p => p.trim().replace(/\.[^/.]+$/, "")).map(p => p.replace(/_/g, '-')).filter(p => p.length > 0);
    return tags.map(t => `"${t}"`).join(", ");
  }
}

module.exports = () => new Utils();
