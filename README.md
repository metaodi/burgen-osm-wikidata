Burgen-Dossier: OSM-to-wikidata scripts
=======================================

Tasks:

- [ ] Try to find castles on OSM, that have a match on WikiData and add a link on OSM
- [ ] Try to find castle on OSM, that have no match on WikiData, create the item and add a link on OSM


General idea:
- Run query on overpass
- Run wikidata query for each found OSM castle with the name as param
- Check if there are any results
   * If yes, check if they are actually a match and link them
   * If no, create a new wikidata item using the information from the OSM node

## Setup

It is recommended to install all dependencies in a virtualenv. In order to setup the virtualenv for this project, simply run:

```bash
./setup.sh
```

### WikiData

To update WikiData you should create a new [BotPassword](https://www.wikidata.org/wiki/Special:BotPasswords). Please add the following grants:
* "Edit existing pages"
* "Create, edit, and move pages"

Save the name and password in the `.env` file like that:

```
BOT_NAME=Metaodi@MySuperBot
BOT_PASSWORD=my-password
```

## Usage

### Find items on WikiData that are not on OSM

If you want to check, if there are castles on OSM that already have a WikiData item, but are not yet properly linked, run the following script:

```bash
./check_wikidata.sh
```

This runs a query on overpass to find all castle-like structures in Switzerland, that do not have a Wikidata tag.
The scripts runs a SPARQL query for each castle using its name as input.

Always check the coordinates as well, since there are some entries, that are named very similary.

### Create WikiData items stubs, if they do not exist

If you are most certainly sure, that a castle does not yet exist on WikiData, you can use this script to create a new WikiData item stub with the available information.

```bash
./create_wikidata_items.sh
```
