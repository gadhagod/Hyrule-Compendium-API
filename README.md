<p align="center">
<img src="https://static.wikia.nocookie.net/characterprofile/images/c/c8/BotW_Link.png/revision/latest/scale-to-width-down/340?cb=20170306180639" length=10% width=10%>
</p>
<h1 align="center">Hyrule Compendium API</h1>
<p align="center"><b>An API serving data on all creatures, monsters, materials, equipment, and treasure in <i>The Legend of Zelda: Breath of the Wild</i>.</b><br>
<sub>By <a href="https://github.com/gadhagod">Aarav Borthakur</a></sub></p>


***

## Concept
The Hyrule compendium is an encyclopedia of all in-game interactive items. With this brilliant API, you can access this data from code and embed it into your own application. See the [compendium directory](compendium) of this repository to see all entries in the compendium. 385 entries and 5 categories of entries are in the compendium.

You can see a specific item, all items in a category, or all data in our database.
Here is an example request and response, retrieving data on the silver lynel:

    $ curl https://botw-compendium.herokuapp.com/api/v1/entry/white-maned_lynel
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
            "image": "https://botw-compendium.herokuapp.com/api/v1/entry/white-maned_lynel/image"
        }
    }

Let's get started!

## API Refrence

The base URL is **https://botw-compendium.herokuapp.com/api/v1**.

---------------

#### `/category`
This endpoint is used for retrieving all entries in a category. The categories are:

* Creatures
* Equipment
* Materials
* Monsters
* Treasure

**HTTP Request**

    GET https://botw-compendium.herokuapp.com/api/v1/category/<category>
    
**Example Request**

    $ curl https://botw-compendium.herokuapp.com/api/v1/category/monsters
    
---------------

#### `/entry`
This endpoint is used for retrieving a specific entry, using it's name or ID. 
If you are using a name to search for an item, spaces are to be replaced with an underscore or "%20".

**HTTP Request**

    GET https://botw-compendium.herokuapp.com/api/v1/entry/<entry>
    
**Example Request** \
<br>With name:

    $ curl https://botw-compendium.herokuapp.com/api/v1/entry/moblin
    
With name with spaces:

    $ curl https://botw-compendium.herokuapp.com/api/v1/entry/silver%20moblin
    
With ID:

    $ curl https://botw-compendium.herokuapp.com/api/v1/entry/70
    
---------------

#### `/`
This endpoint is for retrieving *all* data.

**HTTP Request**

    GET https://botw-compendium.herokuapp.com/api/v1

**Example Request**

    $ curl https://botw-compendium.herokuapp.com/api/v1

### Notes

If a key's value is `null`, that means it's marked as "unknown" in the Hyrule Compendium. \
The response schema of the "creatures" category is much different from the others, because it has two sub-categories ("food" and "non-food").

## Images

This API also serves images. Each item entry has a key `image`, as shown in the example request and response. That key has a link to the image. The images follow this schema:

    https://botw-compendium.herokuapp.com/api/v1/entry/<entry>/image

The `<entry>` can be either the entry's ID or name. For example, the white-maned lynel's image could be retrieved from either of the two links:
* [https://botw-compendium.herokuapp.com/api/v1/entry/white-maned_lynel/image](http://botw-compendium.herokuapp.com/api/v1/entry/white-maned_lynel/image)
* [https://botw-compendium.herokuapp.com/api/v1/entry/123/image](https://botw-compendium.herokuapp.com/api/v1/entry/123/image])

The images are always in a 280x280 pixel PNG format. 

They can be refrenced just as you would refrence any other image from the web. For example, using HTML:

    <img src="https://botw-compendium.herokuapp.com/api/v1/entry/123/image">

## Support and Suggestions

If you come across a malfunction or have any suggestions open an [issue](https://github.com/gadhagod/Hyrule-Compendium-API/issues) or a [pull request](https://github.com/gadhagod/Hyrule-Compendium-API/pulls).

## Client Libraries

* [Python](https://github.com/gadhagod/pyrule-compendium)
* [Ruby](https://github.com/gadhagod/Hyrule-Compendium-ruby-client)
* [Web Javascript](https://github.com/gadhagod/Hyrule-Compendium-web-client)
* [CLI](https://github.com/gadhagod/Hyrule-Compendium-CLI)

## Running locally
Instructions for running locally can be found [here](local/README.md).

## Status
Server status: \
![](https://pyheroku-badge.herokuapp.com/?app=botw-compendium)

Check the latest "test endpoints" workflow run to see if the server status.

## Author
Made with awesomeness by [@gadhagod](https://github.com/gadhagod).
