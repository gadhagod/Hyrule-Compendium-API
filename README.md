<p align="center">
<img src="https://static.wikia.nocookie.net/characterprofile/images/c/c8/BotW_Link.png/revision/latest/scale-to-width-down/340?cb=20170306180639" length=10% width=10%>
</p>
<h1 align="center">Hyrule Compendium API</h1>
<p align="center"><b>An API serving data on all creatures, monsters, materials, equipment, and treasure in <i>The Legend of Zelda: Breath of the Wild</i>.</b><br>
<sub>By <a href="https://github.com/gadhagod">Aarav Borthakur</a></sub></p>
<p align="center">
<img src="https://github.com/gadhagod/Hyrule-Compendium-API/actions/workflows/deployed-api-tests.yml/badge.svg">
</p>

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

To get started, check out the [documentation](http://gadhagod.github.io/Hyrule-Compendium-API).

## Support and Suggestions
If you come across a malfunction or have any suggestions open an [issue](https://github.com/gadhagod/Hyrule-Compendium-API/issues) or a [pull request](https://github.com/gadhagod/Hyrule-Compendium-API/pulls).

## Running locally
Instructions for running locally can be found [here](local/README.md).

## Status
Server status: \
![](https://pyheroku-badge.herokuapp.com/?app=botw-compendium)

Check the latest "test endpoints" workflow run to see if the server status.

## Author
Made with awesomeness by [@gadhagod](https://github.com/gadhagod).
