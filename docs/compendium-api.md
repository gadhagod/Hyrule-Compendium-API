<script src="index.js"></script>

# Compendium API
The `/compendium` endpoint serves data on creatures, equipment, materials, monsters, and treasure.

---------------
## Get entry

**Endpoint**: `/compendium/entry`

This endpoint retrieves a specific entry given its name or ID. 
If you are using a name to search for an item, spaces should be replaced with an underscore or "%20" (usually done automatically when encoding the URL).
The schema of the response depends on the category of the entry.

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

### Try endpoint

<form target="fooFrame">
    <label for="entry-IdOrName">Entry ID/Name:</label>
    <input type="text" id="entry-IdOrName" required>
    <br><br>
    <input type="submit" onclick="createButton('compendium/entry/' + document.getElementById('entry-IdOrName').value, 2, 'entryRes', 'entryLoader')" value="Send request"></input>
    <div id="entryLoader"></div>
    <div id="entryRes"></div>
</form>

---------------
## Get all entries

**Endpoint**: `/compendium/all`

This endpoint retrieves all compendium entries.

**HTTP Request**
```http
GET https://botw-compendium.herokuapp.com/api/v3/compendium/all
```
**Example Request**
```bash
$ curl https://botw-compendium.herokuapp.com/api/v3/compendium/all
```
---------------
## Get category

**Endpoint**: `/compendium/category`

This endpoint is used for retrieving all entries in a given category. The categories are:

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

---------------

## Get master mode entry
 
**Endpoint**: `/compendium/master_mode/entry`

This endpoint retrieves data on a master mode exclusive entry given its name or ID. 
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

## Get all master mode entries

**Endpoint**: `/compendium/master_mode/all`

This endpoint retrieves all master mode exclusive entries.

**HTTP Request**
```http
GET https://botw-compendium.herokuapp.com/api/v3/compendium/master_mode/all
```
**Example Request**
```bash
$ curl https://botw-compendium.herokuapp.com/api/v3/compendium/master_mode/all
```

---------------

## *Tears of the Kingdom* entries
You can configure which game to query by setting URL parameter `game`. If `game` is not set, it defaults to *Breath of the Wild*. If it is set to `1` or `botw`, *Breath of the Wild* is queried. If `game` is set to `2` or `totk`, *Tears of the Kingdom* is queried.

Example URLs for *Breath of the Wild*:
```
https://botw-compendium.herokuapp.com/api/v3/compendium/entry/123
https://botw-compendium.herokuapp.com/api/v3/compendium/entry/123?game=1
https://botw-compendium.herokuapp.com/api/v3/compendium/entry/123?game=botw
```

Example URLs for *Tears of the Kingdom*:
```
https://botw-compendium.herokuapp.com/api/v3/compendium/entry/123?game=2
https://botw-compendium.herokuapp.com/api/v3/compendium/entry/123?game=totk
```

!> **NOTE**: If the `game` paramater is defined and is not `1`, `2`, `botw`, `totk`, you will recieve a 400 status code.

---------------

## Images
This API also serves images of each entry. Each compendium entry has the field `image`. Its value of `image` is a link to the entry's image in a 280x280 pixel PNG format. The image links follow this schema:
```bash
https://botw-compendium.herokuapp.com/api/v3/compendium/entry/<entry>/image
```
`<entry>` can be either the entry's ID or name. For example, the white-maned lynel's image could be retrieved from either of the two links:
* [https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lynel/image](http://botw-compendium.herokuapp.com/api/v3/compendium/entry/lynel/image)
* [https://botw-compendium.herokuapp.com/api/v3/compendium/entry/121/image](https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lynel/image)

?> **NOTE**: You do not have to make a request to `/entry/<entry>` every time you want an image! Entry image links are guaranteed to be in the format `/entry/<entry>/image`.

They can be referenced just as you would reference any other image from the web. For example, using HTML:
```html
<img src="https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lynel/image">
```
Results in: \
![](https://botw-compendium.herokuapp.com/api/v3/compendium/entry/lynel/image)

?> **NOTE**: Master mode entry images use the format: `/master_mode/entry/<entry>/image`

?> **NOTE**: Images of *Tears of the Kingdom* entries are retrieved by specifying the `game` paramater ([more information](compendium-api?id=tears-of-the-kingdom-entries)). 

---------------

## Entry Schemas
The schema of an entry's data depends on the category of the item.

**Monster schema**:
```json
{ 
    "name": "...", // string
    "id": 0,  // integer; ID as shown in compendium
    "category": "...", // string; "monsters"
    "description": "...", // string; short paragraph
    "image": "...", // string; URL of image
    "common_locations": [], // array of strings or null for unknown; where the entry is commonly seen
    "drops": [], // array of strings or null for unknown; recoverable materials from killing
    "dlc": false // boolean; whether the entry is from a DLC pack
}
```

**Equipment schema**:
```json
{ 
    "name": "...", // string; entry name
    "id": 0,  // integer; ID as shown in compendium
    "category": "...", // string; "equipment"
    "description": "...", // string; short paragraph
    "image": "...", // string; URL of image
    "common_locations": [], // array of strings or null for unknown; where the entry is commonly seen
    "properties": { 
        "attack": 0, // integer; damage the entry does (0 for sheilds and arrows)
        "defense": 0, // integer; defense the entry offers (0 for equipment that aren't shields)
        /* TEARS OF THE KINGDOM ONLY */
        "effect": "...", // string; special effect of the weapon (e.g. "wind razor"), empty if none
        "type": "..." // string; type of weapon (e.g. "one-handed weapon")
        /* */
    },
    "dlc": false // boolean; whether the entry is from a DLC pack

}
```
**Material schema**:
```json
{
    "name": "...", // string; entry name
    "id": 0, // integer; ID as shown in compendium
    "category": "...", // string; "materials"
    "description": "...", // string; short paragraph
    "image": "...", // string, URL of image
    "common_locations": [], // array of strings or null for unknown; where the entry is commonly seen
    "hearts_recovered": 0.0, // float; health recovered when eaten raw
    "cooking_effect": "...", // string; special effect when used in a dish/elixir (e.g. "stamina recovery"), empty if none
    "dlc": false, // boolean, whether the entry is from a DLC pack
    /* TEARS OF THE KINGDOM ONLY */
    "fuse_attack_power": 0 // integer; damage added when fused with a weapon
    /* */
},
```

**Creature schema**:

Food (field "edible" is <code>true</code>):
```json
{
    "name": "...", // string; entry name
    "id": 0, // integer; ID as shown in compendium
    "category": "...", // string; "creatures"
    "description": "...", // string; short paragraph
    "image": "...", // string; URL of image
    "cooking_effect": "...", // string; special effect when used in a dish/elixir (e.g. "stamina recovery"), empty if none
    "common_locations": [], // array of strings or null for unknown; where the entry is commonly seen
    "edible": true, // boolean; true, whether the creature can be eaten or incorporated into a dish/elixir
    "hearts_recovered": 0.0, // float; hearts recovered when eaten raw
    "dlc": false // boolean, whether the entry is from a DLC pack
}
```

Non-food (field "edible" is <code>false</code>):
```json
{
    "name": "...", // string; entry name
    "id": 0, // integer; ID as shown in compendium
    "category": "...", // string; "creatures"
    "description": "...", // string; short paragraph
    "image": "...", // string; URL of image
    "common_locations": [], // array of strings or null for unknown; where the entry is commonly seen
    "edible": false, // boolean; false, whether the creature can be eaten or incorporated into a dish/elixir
    "drops": [], // array of strings or null for unknown; recoverable materials from killing
    "dlc": false // boolean, whether the entry is from a DLC pack
}
```

**Treasure schema**:
```json
{ 
    "name": "...", // string
    "id": 0,  // integer; ID as shown in compendium
    "category": "...", // string; "treasure"
    "description": "...", // string; short paragraph
    "image": "...", // string; URL of image
    "common_locations": [], // array of strings or null for unknown; where the entry is commonly seen
    "drops": [], // array of strings or null for unknown; recoverable materials when accessed
    "dlc": false // boolean; whether the entry is from a DLC pack
}
```

## Demo

Built by [Arjun Kahlon](https://github.com/arjunkahlon), this demo uses *Breath of the Wild* data through the Hyrule Compendium API. View the source code [here](https://github.com/gadhagod/Hyrule-Compendium-Demo).

<iframe width="100%" height="700" src="https://gadhagod.github.io/hyrule-compendium-demo/"></iframe>

<iframe name="fooFrame" class="hide"></iframe>