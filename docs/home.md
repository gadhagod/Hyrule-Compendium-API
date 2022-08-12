<script src="index.js"></script>
<center>
    <img id="logo" src="assets/light_logo.png" length=10% width=10%>
    <h1>Hyrule Compendium API</h1>
    <strong>An API serving data on all creatures, monsters, materials, equipment, and treasure in <i>The Legend of Zelda: Breath of the Wild</i></strong><br>
</center>
<hr>

# Concept
The Hyrule compendium is an encyclopedia of all in-game interactive items and regions. With this brilliant API, you can access this data from code and embed it into your own application. 

You can see a specific item, all items in a category, or all data in our database.
Here is an example request and response, retrieving data on the white-maned lynel:

```bash
$ curl https://botw-compendium.herokuapp.com/api/v3/compendium/entry/white-maned_lynel
{
    "data": {
        "name": "white-maned lynel",
        "id": 123,
        "category": "monsters",
        "description": "These fearsome monsters have lived in Hyrule since ancient times. Their ability to breathe fire makes White-Maned Lynels among the toughest of the species; each one of their attacks is an invitation to the grave. There are so few eyewitness accounts of this breed because a White-Maned Lynel is not one to let even simple passersby escape with their lives.",
        "common_locations":[
            "Hyrule Field",
            "Hebra Mountains"
        ]
        "drops": [
            "lynel horn",
            "lynel hoof",
            "lynel guts"
        ],
        "image": "https://botw-compendium.herokuapp.com/api/v3/compendium/entry/white-maned_lynel/image"
    }
}
```
---------------
# Reference

The base URL is **`https://botw-compendium.herokuapp.com/api/v3`**.

?> In all endpoints, if a value is `null`, it's marked as "unknown" in the compendium.

## Compendium
The `/compendium` endpoint serves data on creatures, equipment, materials, monsters, and treasure.

The schema of an items's data depends on the the category of the item, except for entries of the **creatures** category, where the field `edible` determines its schema.

---------------

### `/compendium/entry`
This endpoint is used for retrieving a specific entry, using it's name or ID. 
If you are using a name to search for an item, spaces are to be replaced with an underscore or "%20".
The schema of the response depends on the the category of the entry.

**HTTP Request**

```http
GET https://botw-compendium.herokuapp.com/api/v3/compendium/entry/<entry>
```
    
**Example Request** \
<br>With name:
```bash
$ curl https://botw-compendium.herokuapp.com/api/v3/compendium/entry/moblin
```

With ID:
```bash
$ curl https://botw-compendium.herokuapp.com/api/v3/compendium/entry/108
```

#### Try endpoint

<form target="fooFrame">
    <label for="entry-IdOrName">Entry ID/Name:</label>
    <input type="text" id="entry-IdOrName" required>
    <br><br>
    <input type="submit" onclick="createButton('compendium/entry/' + document.getElementById('entry-IdOrName').value, [], 'entryRes', 'entryLoader')" value="Send request"></input>
    <div id="entryLoader"></div>
    <div id="entryRes"></div>
</form>

---------------
### `/compendium/all`
This endpoint is for retrieving *all* data.

**HTTP Request**
```http
GET https://botw-compendium.herokuapp.com/api/v3/compendium/all
```
**Example Request**
```bash
$ curl https://botw-compendium.herokuapp.com/api/v3/compendium/all
```
---------------
## `/compendium/category`
This endpoint is used for retrieving all entries in a category. The categories are:

* Creatures
* Equipment
* Materials
* Monsters
* Treasure

**HTTP Request**
```http
GET https://botw-compendium.herokuapp.com/api/v3/compendium/category/<category>
```
**Example Request**
```bash
$ curl https://botw-compendium.herokuapp.com/api/v3/compendium/category/monsters
```
    
!> **Warning**: the creatures category has entries of two possible schemas, determined by whether the `edible` field is `true` or `false`.

---------------

### `/compendium/master_mode/entry`
This endpoint retrieves data on a master mode exclusive entry, using it's name or ID. 
If you are using a name to search for an item, spaces are to be replaced with an underscore or "%20".

**HTTP Request**
```http
GET https://botw-compendium.herokuapp.com/api/v3/compendium/master_mode/entry/<entry>
```
**Example Request**
```bash
$ curl https://botw-compendium.herokuapp.com/api/v3/compendium/master_mode/entry/golden_bokoblin
```
---------------

### `/compendium/master_mode/all`
This endpoint retrieves all data on master mode exclusive entries.

**HTTP Request**
```http
GET https://botw-compendium.herokuapp.com/api/v3/compendium/master_mode/all
```
**Example Request**
```bash
$ curl https://botw-compendium.herokuapp.com/api/v3/compendium/master_mode/all
```
---------------


### Images
This API also serves images. Each item entry has a key `image`, as shown in the example request and response. That key has a link to the image. The images follow this schema:
```bash
https://botw-compendium.herokuapp.com/api/v3/compendium/entry/<entry>/image
```
The `<entry>` can be either the entry's ID or name. For example, the white-maned lynel's image could be retrieved from either of the two links:
* [https://botw-compendium.herokuapp.com/api/v3/compendium/entry/white-maned_lynel/image](http://botw-compendium.herokuapp.com/api/v3/compendium/entry/white-maned_lynel/image)
* [https://botw-compendium.herokuapp.com/api/v3/compendium/entry/123/image](https://botw-compendium.herokuapp.com/api/v3/compendium/entry/123/image)

The images are always in a 280x280 pixel PNG format. 

They can be referenced just as you would reference any other image from the web. For example, using HTML:
```html
<img src="https://botw-compendium.herokuapp.com/api/v3/compendium/entry/123/image">
```
Would result in: \
![](https://botw-compendium.herokuapp.com/api/v3/compendium/entry/123/image)

?> **NOTE**: Master mode entry images use a different URL: `/master_mode/entry/<entry>/image`

## Regions
The `/regions` endoint provides data on Hyrule's eight geographical regions, like encompassed shrines and settlements. The

---------------
### `/regions`
This endpoint returns information on a single region, given the region's name.

**HTTP Request**:
```http
GET https://botw-compendium.herokuapp.com/api/v3/regions/<region>
```
**Example Request**
```bash
$ curl https://botw-compendium.herokuapp.com/api/v3/regions/eldin
```
---------------
### `/regions/all`
The endpoint returns all regions.

**HTTP Request**:
```http
GET https://botw-compendium.herokuapp.com/api/v3/regions/all
```
**Example Request**
```bash
$ curl https://botw-compendium.herokuapp.com/api/v3/regions/all
```
---------------
# Demo

<iframe width="100%" height="700" src="https://botw-compendium-demo.herokuapp.com/"></iframe>

You can also view the demo of the Hyrule Compendium API [here](https://botw-compendium-demo.herokuapp.com). The source code can be found [here](https://github.com/gadhagod/Hyrule-Compendium-Demo).

<iframe name="fooFrame" class="hide"></iframe>