import botwTests from "./botw";
import totkTests from "./totk";

let url = process.env.URL ?? "https://botw-compendium.herokuapp.com";

describe("v3", () => { 
    describe("botw", () => { botwTests(url) });
    describe("totk", () => { totkTests(url) });
});