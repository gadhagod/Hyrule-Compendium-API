## Hyrule Compendium Tests
Install dependencies:

    npm install

Test the deployed REST API:

    npm test

Test a local server:
    
    env URL=[url] node_modules/mocha/bin/mocha test/index.ts -r ts-node/register

Execute a specific test:

    node_modules/mocha/bin/mocha test/index.ts -r ts-node/register -g "[test description]"