<p align="center">
<img src="https://static.wikia.nocookie.net/characterprofile/images/c/c8/BotW_Link.png/revision/latest/scale-to-width-down/340?cb=20170306180639" length=10% width=10%>
</p>
<h1 align="center">Hyrule Compendium API</h1>
<p align="center"><b>An API serving data on all creatures, monsters, materials, equipment, and treasure in <i>The Legend of Zelda: Breath of the Wild</i>.</b><br>
    <sub>By <a href="http://github.com/gadhagod">Aarav Borthakur</a></sub></p>


***

## Concept
The Hyrule compendium is an encyclopedia of all in-game interactive items. With this brilliant API, you can access this data from code and embed it into your own application. See the [compendium directory](compendium) of this repository to see all entries in the compendium. 385 entries and 5 categories of entries are in the compendium.

You can see a specific item, all items in a category, or all data in our database.
Here is an example request and response, retrieving data on the silver lynel:

    $ curl http://botw-compendium.herokuapp.com/api/v1/entry/silver_lynel
    {
        "data": {
            "category": "monsters",
            "description": "Silver Lynels are not to be trifled with. They have been influenced by Ganon's fiendish magic, so they are the strongest among the Lynel species, surpassing even the strength of those with white manes. The term \"silver\" denotes not only their color but also their rarity. The purple stripes help them to stand out even more.",
            "drops": [
                "lynel horn",
                "lynel hoof",
                "lynel guts",
                "topaz",
                "ruby",
                "sapphire",
                "diamond",
                "star fragment"
            ],
            "id": 124,
            "name": "silver lynel"
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

## Support and Suggestions

If you come across a malfunction or have any suggestions open an [issue](https://github.com/gadhagod/Hyrule-Compendium-API/issues) or a [pull request](https://github.com/gadhagod/Hyrule-Compendium-API/pulls).

## Notes

If a key's value is `null`, that means it's marked as "unknown" in the Hyrule Compendium.
The response schema of the "creatures" category is much different from the others, because it has two sub-categories ("food" and "non-food").

## Client Libraries

* [Python](https://github.com/shaunikm/Hyrule-Compendium-python-client) (from [@shaunikm](https://github.com/shaunikm))
* [Ruby](https://github.com/gadhagod/Hyrule-Compendium-ruby-client)

## Author
Made with awesomeness by [@gadhagod](http://github.com/gadhagod).
