/*
All castles of Switzerland (with name) without wikidata entry
*/
//[out:csv(::"type",::"id",name,historic,access,"description",::"lat",::"lon"; true; ",")];
[out:json];
area["name"="Schweiz/Suisse/Svizzera/Svizra"]->.perimeter; 
(
  nwr[historic~"castle|tower"][name][!wikidata](area.perimeter);
  nwr[historic=archaeological_site][name][site_type=fortification][!wikidata](area.perimeter);
);
// out body; >; out skel qt;
out center;
