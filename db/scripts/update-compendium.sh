# adds and overwrites all compendium entries with data from db/data/compendium
# assumes you are in db/scripts

rockset api:documents:addDocuments botw-api-v3 creatures --body ../data/compendium/creatures.json
rockset api:documents:addDocuments botw-api-v3 equipment --body ../data/compendium/equipment.json
rockset api:documents:addDocuments botw-api-v3 materials --body ../data/compendium/materials.json
rockset api:documents:addDocuments botw-api-v3 monsters --body ../data/compendium/monsters.json
rockset api:documents:addDocuments botw-api-v3 treasure --body ../data/compendium/treasure.json
rockset api:documents:addDocuments botw-api-v3 master_mode --body ../data/compendium/master_mode.json