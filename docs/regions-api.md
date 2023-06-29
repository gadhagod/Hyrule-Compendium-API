# Regions API
The `/regions` endpoint provides data on Hyrule's eight geographical regions, like encompassed shrines and settlements. The Regions API only supports the *Breath of the Wild* map as of now. 

---------------
## Get region

**Endpoint**: `/regions`

This endpoint retrieves information on a single region given its name.

**HTTP Request**:
```http
GET https://botw-compendium.herokuapp.com/api/v3/regions/<region>
```
**Example Request**
```bash
$ curl https://botw-compendium.herokuapp.com/api/v3/regions/eldin
```
---------------
## Get all regions

**Endpoint**: `/regions/all`

This endpoint retrieves all regions.

**HTTP Request**:
```http
GET https://botw-compendium.herokuapp.com/api/v3/regions/all
```
**Example Request**
```bash
$ curl https://botw-compendium.herokuapp.com/api/v3/regions/all
```
