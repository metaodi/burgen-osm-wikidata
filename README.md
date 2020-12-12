Burgen-Dossier: OSM-to-wikidata scripts
=======================================

Tasks:

- [ ] Try to find castles on OSM, that have a match on WikiData and add a link on OSM
- [ ]  Try to find castle on OSM, that have no match on WikiData, create the item and add a link on OSM


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
