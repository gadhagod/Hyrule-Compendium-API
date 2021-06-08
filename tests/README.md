## Hyrule Compendium Tests
Install dependencies:

    npm install

Run all tests:

    npm test

Test the deployed API:

    npm test test/api.ts

Test a local server:
    
    env URL=[url] node_modules/mocha/bin/mocha test/api.ts

Test documentation files:

    sh test/docs.sh

### Important
* All tests assume you are in the `tests/` directory of this repo.