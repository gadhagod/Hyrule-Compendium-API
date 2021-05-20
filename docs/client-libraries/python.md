# Python wrapper
The official python library, [*pyrule compendium*](https://github.com/gadhagod/pyrule-compendium), makes API usage quick to setup and use.

## Installation
With pip:
```bash
pip3 install pyrule-compendium
```
Install development build:
```bash
pip3 install git+https://github.com/gadhagod/pyrule-compendium
```

## Example usage
```python
from pyrule_compendium import compendium

comp = compendium()

print(comp.get_all()) # get all entries
print(comp.get_entry("silver lynel")) # get a specific entry with it's name
print(comp.get_entry(1)) # get a specific entry with it's ID
print(comp.get_category("monsters")) # get all entries in a category
comp.get_image("silver lynel").download() # download entry image
```

## Documentation

***

#### `compendium`: class
Base class for pyrule compendium. <br>
Parameters:
* `url`: The base URL for the API.
    - default: "https://botw-compendium.herokuapp.com/api/v2"
    - type: string
* `default_timeout`: Default seconds to wait for response for all API calling functions until raising `requests.exceptions.ReadTimeout`
    - default: `None` (no timeout)
    - type: integer, float, tuple (for connect and read timeouts)
    - notes: If a API calling function has a parameter `timeout`, it will overide this

#### `compendium.get_entry`: function
Gets an entry from the compendium. <br>
Parameters:
* `entry`: The entry to be retrieved.
    - type: str, int
* `timeout`: Seconds to wait for response until raising `requests.exceptions.ReadTimeout`
    - default: `compendium.default_timeout`
    - type: integer, float, tuple (for connect and read timeouts) <br><br>
<!---->

Returns: Metadata on the entry 
- type: dict

#### `compendium.get_category`: function
Gets all entries from a category in the compendium. \
Parameters:
* `category`: The name of the category to be retrieved. Must be one of the compendium categories.
    - type: str
    - notes: must be in ["creatures", "equipment", "materials", "monsters", "treasure"]
* `timeout`: Seconds to wait for response until raising `requests.exceptions.ReadTimeout`
    - default: `compendium.default_timeout`
    - type: int, float, tuple (for connect and read timeouts)

<!---->
Returns: All entries in the category. 
- type: list, dict (for creatures)
- notes: the response schema of `creatures` is different from the others, as it has two sub categories: `food` and `non_food` as keys

#### `compendium.get_all`: function
Gets all entries from the compendium.<br>
Parameters:
* `timeout`: Seconds to wait for response until raising `requests.exceptions.ReadTimeout`
    - default: `self.default_timeout`
    - type: integer, float, tuple (for connect and read timeouts)
<!---->

Returns: all items in the compendium with their metadata nested in categories.
- type: dict

#### `compendium.get_image`: function
Retrieves the image of a compendium entry.<br>
Parameters:
    * `entry`: Entry image object
        - type: `objects.entry_image`
<!---->

Returns: Entry image object
    - type: `objects.entry_image`

***

#### `exceptions.NoCategoryError`: exception
Raised when a given category does not exist in the compendium.<br>
Parameters:
* `target_category`: Non-existant input category that causes error.
    - type: string

#### `exceptions.NoEntryError`: exception
Raised when a given entry does not exist in the compendium.<br>
Parameters:
* `target_entry`: Non-existant input entry that causes error.
    - type: string