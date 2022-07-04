# adds and overwrites all regions with data from db/data/compendium
# assumes you are in db/data/scripts

rockset api:documents:addDocuments botw-api-v3 regions --body ../data/regions.json