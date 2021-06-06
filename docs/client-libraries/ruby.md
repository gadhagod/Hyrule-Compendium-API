# Ruby wrapper
The official Ruby wrapper makes API usage quick to setup and use in the Ruby language.

This documentaion applies to version [3.2.0](https://github.com/gadhagod/Hyrule-Compendium-ruby-client/releases/tag/3.2.0).

## Installation
```ruby
gem install Hyrule-Compendium
```
## Example usage
```ruby
require "hyrule_compendium"  # import library
compendium = Hyrule_Compendium.new  # create class instance

compendium.get_entry 1  # get entry with ID
compendium.get_entry "horse"  # get entry with name
compendium.get_category "monsters"  # get category
compendium.get_all  # get everthing
compendium.download_entry_image "lynel", "dream_pet.png"
```

## Documentation

***

#### `Hyrule_Compendium`: class
Base class for the Hyrule-Compendium.  
Parameters:
* `url`: The base URL of the API server
    - type: str
    - default: "http://botw-compendium.herokuapp.com/api/v2"
* `default_timeout`: Default seconds to wait for response for all API calling functions until raising `Net::ReadTimeout`.
    - type: float, int
    - default: `nil` (no timeout)
    - notes: If a API calling function has a parameter `timeout`, it will overide this.

#### `Hyrule_Compendium.get_entry`: function
Gets an entry from the compendium.<br>
Parameters:
* `entry`: The ID or name of the entry to be retrieved.
    - type: str, int
* `timeout`: Seconds to wait for response until raising `Net::ReadTimeout`.
    - type: float, int
    - default: `@default_timeout`

Returns: The entry's metadata.
- type: hash

Raises:
* `NoEntryError` when the entry is not found.

#### `Hyrule_Compendium.get_category`: function
Gets all entries from a category in the compendium.<br>
Parameters:
* `category`: The name of the category to be retrieved. Must be one of the compendium categories.
    - type: string
    - notes: 
        * must be "creatures", "equipment", "materials", "monsters", or "treasure"
        * the category "creatures" has two sub-categories, as keys: "food" and "non_food"
* `timeout`: Seconds to wait for response until raising `Net::ReadTimeout`.
    - type: float, int
    - default: `@default_timeout`

Returns: All entries in the category.
- type: array, hash (for creatures)

Raises: `NoCategoryError` when the category is not found.

#### `Hyrule_Compendium.get_all`: function
Gets all entries from the compendium.<br>
Parameters:
* `timeout`: Seconds to wait for response until raising `Net::ReadTimeout`.
    - type: float, int
    - default: `@default_timeout`

Returns: all items in the compendium with their metadata, nested in categories.
- type: hash

#### `Hyrule_Compendium.download_entry_image`: function
Downloads the image of a compendium entry.<br>
Parameters:
* `entry`: The ID or name of the entry of the image to be downloaded.
    - type: str, int
* `output_file`: The output file's path.
    - type: str
    - default: entry's name with a ".png" extension with spaces replaced with underscores
* `timeout`: Seconds to wait for server response until raising `Net::ReadTimeout`.
    - type: float, int
    - default: `@default_timeout`

#### `NoEntryError`: exception
Raised when a given entry does not exist in the compendium.<br>
Parameters:
* `target_entry`: Non-existant input entry that causes error.
    - type: str, int

#### `NoCategoryError`: exception
Raised when a given category does not exist in the compendium 
Parameters:
* `target_category`: Non-existant input category that causes error.
    - type: str