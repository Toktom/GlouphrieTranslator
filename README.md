# GlouphrieTranslator

**GlouphrieTranslator** (or **GT**) is an integration of **MWParserFromHell** and **PyWikiBot**. This tool allows **PT-BR Runescape Wiki** editors to increase their editing speed when translating the pages from **RSW**. The key feature of the tool is the auto-template translator.

## Installation

1. Before installing the tool, you need to install the following dependencies:

- [Pywikibot](https://github.com/wikimedia/pywikibot);
- [MWParserFromHell](https://github.com/earwig/mwparserfromhell); and
- [requests](https://github.com/psf/requests).

2. Install [git](https://git-scm.com/) to be able to proceed with the installation.

3. Go to your Python directory installation folder and go to the folder `Lib/site-packages` and then find the folder `pywikibot`. Inside **pywikibot** folder open the folder `families` and add the python file `rsw_family.py` to it (this file can be found at the [pywikibot_family](pywikibot_family)).

4. Finally, you can install the tool by running the following command:

```pip install git+https://github.com/Toktom/GlouphrieTranslator```.

## Features

The tool has the following features:

- Extraction of the Infobox Template from an item's page.

## Examples

The folder [examples](examples) contain some examples of how to use the tool. Currently, there is only one example: to extract the **Infobox Item** template from an item page.

## Todos

- Add support for more infoboxes templates;
- Add support for navigation box templates;
- Add documentation to functions;
- Add automatic installation verification;
- Speed optimization (remove for loops where is feasible); and
- Improve usage of try/except in functions and classes.
