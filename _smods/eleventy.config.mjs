import interlinker from "@photogabble/eleventy-plugin-interlinker";

import markdownIt from "markdown-it";
import markdownItReplaceLink from "markdown-it-replace-link";
import markdownItObsidian from "markdown-it-obsidian";

let markdownItOptions = {
  html: true,
  replaceLink: function (link, env) {
    // Convert links such as `./blah.md` to `.././blah/`.
    return link.replace(/^\./, '../.').replace(/.md$/, '/');
  }
};


export default async function(eleventyConfig) {

    const mark = markdownIt(markdownItOptions)
                    .use(markdownItObsidian)
                    .use(markdownItReplaceLink)

    eleventyConfig.setLibrary("md", mark);
    eleventyConfig.addPlugin(interlinker, {
        
    });
};