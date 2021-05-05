<center>
    <img src="logo.png" length=10% width=10%>
    <h1>Hyrule Compendium API</h1>
    <strong>An API serving data on all creatures, monsters, materials, equipment, and treasure in <i>The Legend of Zelda: Breath of the Wild</i></strong><br>
</center>
<hr>

## Concept
The Hyrule compendium is an encyclopedia of all in-game interactive items. With this brilliant API, you can access this data from code and embed it into your own application. 385 entries and 5 categories of entries make up the compendium.

You can see a specific item, all items in a category, or all data in our database.
Here is an example request and response, retrieving data on the silver lynel:

```bash
$ curl https://botw-compendium.herokuapp.com/api/v2/entry/white-maned_lynel
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
        "image": "https://botw-compendium.herokuapp.com/api/v2/entry/white-maned_lynel/image"
    }
}
```
Let's get started!

## API Refrence

The base URL is **https://botw-compendium.herokuapp.com/api/v2**.

---------------

### `/entry`
This endpoint is used for retrieving a specific entry, using it's name or ID. 
If you are using a name to search for an item, spaces are to be replaced with an underscore or "%20".

**HTTP Request**

```http
GET https://botw-compendium.herokuapp.com/api/v2/entry/<entry>
```
    
**Example Request** \
<br>With name:
```bash
$ curl https://botw-compendium.herokuapp.com/api/v2/entry/moblin
```

With ID:
```bash
$ curl https://botw-compendium.herokuapp.com/api/v2/entry/108
```
---------------

### `/category`
This endpoint is used for retrieving all entries in a category. The categories are:

* Creatures
* Equipment
* Materials
* Monsters
* Treasure

**HTTP Request**
```http
GET https://botw-compendium.herokuapp.com/api/v2/category/<category>
```
**Example Request**
```bash
$ curl https://botw-compendium.herokuapp.com/api/v2/category/monsters
```
    
!> **Warning**: the creatures category has two sub categores as keys, `food` and `non_food`.

---------------

### `/all`
This endpoint is for retrieving *all* data.

**HTTP Request**
```http
GET https://botw-compendium.herokuapp.com/api/v2
```
**Example Request**
```bash
$ curl https://botw-compendium.herokuapp.com/api/v2
```

---------------

### `/entry/<>/image`
This endpoint serves an image on a given entry.

**HTTP Request**
```http
GET https://botw-compendium.herokuapp.com/api/v2/entry/<entry>/image    
```
**Example Request**
```bash
$ curl https://botw-compendium.herokuapp.com/api/v2/entry/horse/image   # returns a bunch of binary
```
More on images at [compendium images](?id=images).

---------------

?> In all API endpoints, if a value is `null`, it's marked as "unknown" in the compendium.

## Images (BETA)
This API also serves images. Each item entry has a key `image`, as shown in the example request and response. That key has a link to the image. The images follow this schema:
```bash
https://botw-compendium.herokuapp.com/api/v2/entry/<entry>/image
```
The `<entry>` can be either the entry's ID or name. For example, the white-maned lynel's image could be retrieved from either of the two links:
* [https://botw-compendium.herokuapp.com/api/v2/entry/white-maned_lynel/image](http://botw-compendium.herokuapp.com/api/v2/entry/white-maned_lynel/image)
* [https://botw-compendium.herokuapp.com/api/v2/entry/123/image](https://botw-compendium.herokuapp.com/api/v2/entry/123/image])

The images are always in a 280x280 pixel PNG format. 

They can be refrenced just as you would refrence any other image from the web. For example, using HTML:
```html
<img src="https://botw-compendium.herokuapp.com/api/v2/entry/123/image">
```
Would result in: \
![](https://botw-compendium.herokuapp.com/api/v2/entry/123/image)

!> **Warning**: The images feature is still in development. Issues can happen. 
