# adds and overwrites all regions with data from db/botw/compendium
# assumes you are in db/scripts

rockset api:documents:addDocuments botw-api-v3 regions --body ../botw/regions.json