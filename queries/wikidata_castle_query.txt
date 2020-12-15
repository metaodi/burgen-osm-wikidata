# Castle-like items in Switzerland
SELECT ?castle ?castleLabel ?type ?typeLabel ?coord ?lat ?lon
WHERE 
{
  ?castle wdt:P17 wd:Q39.
  ?castle wdt:P31/wdt:P279* ?type . # castle-like types
  ?castle rdfs:label ?castleLabel .
  FILTER(regex(?castleLabel, ".*{osm_name}.*", "i"))
  OPTIONAL {?castle wdt:P625 ?coord .} # geographic coord
  OPTIONAL {
    ?castle p:P625 ?statement.
    ?statement psv:P625 ?node.
    ?node wikibase:geoLatitude ?lat.
    ?node wikibase:geoLongitude ?lon.
   }

  
  FILTER (?type IN (wd:Q23413,  wd:Q751876, wd:Q88205, wd:Q57821, wd:Q17715832, wd:Q1802963, wd:Q20034791,  wd:Q811979) )
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
