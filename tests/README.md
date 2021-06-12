## Hyrule Compendium Tests
Install dependencies:

    npm install

Run all tests:

    npm test

Test the deployed API:

    npm run test:api

Test a local server:
    
    env URL=[url] node_modules/mocha/bin/mocha

Test documentation files:

    npm run test:docs

### Important
* All tests assume you are in the `tests/` directory of this repo.