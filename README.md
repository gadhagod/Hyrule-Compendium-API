### WARNING: v1 and v2 are being discontinued on September 29, 2024. Please see the [migration guide](https://github.com/gadhagod/Hyrule-Compendium-API/issues/46) to update your applications.

***

<p align="center">
<img src="docs/assets/light_logo.png" length=10% width=10%>
</p>
<h1 align="center">Hyrule Compendium API</h1>
<p align="center"><b>An API serving data on all in-game items and regions in <i>Breath of the Wild</i> and <i>Tears of the Kingdom</i></b><br><br>
    <a href="https://github.com/gadhagod/Hyrule-Compendium-API/actions/workflows/deployed-api-tests.yml">
        <img src="https://github.com/gadhagod/Hyrule-Compendium-API/actions/workflows/deployed-api-tests.yml/badge.svg">
    </a>
</p>

***

## Concept
The Hyrule compendium is an encyclopedia of all the in-game interactive items in the world of Hyrule. With this brilliant API, you can access its data and embed it into your own application. 

You can see a specific item, all items in a category, or all data in our database.
Here is an example request and response, retrieving data on the white-maned lynel:

    $ curl https://botw-compendium.herokuapp.com/api/v3/entry/white-maned_lynel
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
            "image": "https://botw-compendium.herokuapp.com/api/v3/entry/white-maned_lynel/image"
        }
    }

To get started, check out the [documentation](http://gadhagod.github.io/Hyrule-Compendium-API).

## Support and Suggestions
If you come across a malfunction or have any suggestions open an [issue](https://github.com/gadhagod/Hyrule-Compendium-API/issues) or a [pull request](https://github.com/gadhagod/Hyrule-Compendium-API/pulls).

## Running locally
Instructions for running locally can be found [https://gadhagod.github.io/Hyrule-Compendium-API/#/self-hosting].
