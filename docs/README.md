<script src="index.js"></script>
<center>
    <img id="logo" src="assets/light_logo.png" length=10% width=10%>
    <h1>Hyrule Compendium API</h1>
    <strong>An API serving data on all in-game items and regions in <i>Breath of the Wild</i> and <i>Tears of the Kingdom</i></strong><br>
</center>
<hr>


# Concept
The Hyrule compendium is an encyclopedia of all the in-game interactive items in the world of Hyrule. With this brilliant API, you can access its data and embed it into your own application. 

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

To get started, take a look at the [Compendium API docs](compendium-api) or the [Regions API docs](regions-api).