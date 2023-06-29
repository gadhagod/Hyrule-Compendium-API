# Self Hosting 

### Overview

Hyrule Compendium API is supported by the following technologies:

* [Flask](https://flask.palletsprojects.com) (web framework)
* [Rockset](https://rockset.com/docs) (database)
* [Mocha](https://mochajs.org) (testing framework)
* [Docsify](https://docsify.js.org/) (documentation generator)

To get started, clone the [source repository](https://github.com/gadhagod/Hyrule-Compendium-API).

```bash
$ git clone https://github.com/gadhagod/Hyrule-Compendium-API
```

This project uses Python 3.9, but it may work with other 3.x versions. Check what version of python you are using:
```
$ python3 --version
```

Install the python requirements.
```bash
$ python3 -m pip install -r requirements.txt
```

### Loading the data
Before you can run the Flask server, you must load the raw JSON data into Rockset collections.

Start by creating an API key at the [Rockset console](https://console.rockset.com/apikeys). The API key needs to have read and write access. Store your API key in the environment variable `RS2_TOKEN`:

```bash
$ export RS2_TOKEN="<api key>"
```

Check what Rockset API server to use ([use this table for reference](https://rockset.com/docs/rest-api/#introduction)). If your region is not `us-west-2`, you must set the environment variable `RS2_SERVER`:

```bash
$ export RS2_SERVER="<api server (without 'https://')>" 
```

The [`load_data.py`](https://github.com/gadhagod/Hyrule-Compendium-API/blob/master/scripts/load_data.py) script creates the necessary workspaces and collections and adds the data from the `db` directory into the collections. Run the program from the root directory:

```bash
$ python3 scripts/load_data.py
```

This command can also be used for updating the collections later.

### Starting the server
Make sure your `RS2_TOKEN` environment variable is exported.

To run in development mode:

```bash
$ python3 server.py
```

The app will be running on port 5000, accessible at `http://127.0.0.1:5000`.

To run in production mode, first create your v2 collections. Then:
```bash
$ sh run.sh
```

The app will be running on port 8000, available at `http://127.0.0.1:8000`.

### Testing
The tests run on Node.js v15, but may work with more recent versions. If needed, install [Node.js](https://nodejs.org/en/download). Check which version Node.js you are using:
```bash
$ node --version
```

Navigate to the `tests` directory.
```bash
$ cd tests
```

Install the Node.js dependencies:
```bash
$ npm i
```

Run the tests:
```bash
npm run test:v3
```

### Documentation
The documentation is built on [Docsify](https://docsify.js.org).

Navigate to the `docs` directory:
```bash
cd docs
```

Install the dependencies:
```bash
npm i
```

Start the server:
```bash
npm start
```