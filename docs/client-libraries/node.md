# Node wrapper
The official python library, [*hyrule-compendium*](https://github.com/gadhagod/Hyrule-Compendium-node-client), makes API usage quick to setup and use.

## Installation
From NPM:
```bash
npm init
npm i hyrule-compendium
```
From development build :
```bash
npm init
npm i git+https://github.com/gadhagod/Hyrule-Compendium-node-client
```

## Example usage
```node
const hyrule_compendium = require("hyrule-compendium")

let comp = new hyrule_compendium.compendium

comp.get_all(console.log) # get all entries
comp.get_entry("silver lynel", console.log) # get a specific entry with it's name
comp.get_entry(1, console.log) # get a specific entry with it's ID
comp.get_category("monsters", console.log) # get all entries in a category
comp.download_entry_image("silver_lynel", "dream_pet.png") # download entry image
```

## Documentation

***

#### `compendium`: class
Base class for hyrule-compendium.<br>
Parameters:
* `url`: The base URL for the API.
    - default: "https://botw-compendium.herokuapp.com/api/v2"
    - type: string
* `default_timeout`: Default milliseconds to wait for response for all API calling functions until executing it's argument `error_callback`.
    - default: `10000` (ten seconds)
    - type: number

#### `compendium.get_entry`: function
Gets an entry from the compendium.<br>
Parameters:
* `entry`: The entry to be retrieved.
    - type: string, number
* `callback`: Function to be executed with metadata on the entry.
    - type: function
* `timeout`: Milliseconds to wait for response until executing `error_callback`.
    - type: number
    - default: `compendium.default_timeout`
* `error_callback`: Function to be executed on request errors.
    - type: function
    - default: Throws error

#### `compendium.get_category`: function
Gets all entries from a category in the compendium.<br>
Parameters:
* `category`: The name of the category to be retrieved. Must be one of the compendium categories.
    - type: string
    - notes: must be in `["creatures", "equipment", "materials", "monsters", "treasure"]`
* `callback`: Function to be executed with all entries in the category.
    - type: function
* `timeout`: Milliseconds to wait for response until executing `error_callback`.
    - type: number
    - default: `this.default_timeout`
* `error_callback`: Function to be executed on request errors.
    - type: function
    - default: Throws error
<!---->

Notes: the response schema of `creatures` is different from the others, as it has two sub categories: food and non_food

#### `compendium.get_all`: function
Get all entries from the compendium.<br>
Parameters:
* `callback`: Function to be executed with all items in the compendium with their metadata, nested in categories.
    - type: function
* `timeout`: Milliseconds to wait for response until executing `error_callback`.
    - type: number
    - default: `this.default_timeout`
* `error_callback`: Function to be executed on request errors.
    - type: function
    - default: Throws error

#### `download_entry_image`: function
Download the image of a compendium entry.<br>
Parameters:
* `entry`: The ID or name of the entry of the image to be downloaded.
    - type: str, int
* `output_file`: The output file's path.
    - type: str
    - default: entry's name with a ".png" extension with spaces replaced with underscores
* `callback`: The function to executed with image binary
    - type: function
    - default: `function(){}` (empty function)
* `timeout`: Milliseconds to wait for server response until executing `error_callback`.
    - type: number
    - default: `this.default_timeout`
* `error_callback`: Function to be executed on request errors.
    - type: function
    - default: `function(err){throw err}` (throws error)

***

#### `NoCategoryError`: exception
Raised when a given category does not exist in the compendium.<br>
Parameters:
* `target_category`: Non-existant input category that causes error.
    - type: string

#### `NoEntryError`: exception
Raised when a given entry does not exist in the compendium.<br>
Parameters:
* `target_entry`: Non-existant input entry that causes error.
    - type: string