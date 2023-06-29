import { 
    CompendiumTester, 
    // ImageTester,
    // RegionTester, 
    Game 
} from "./util";
import assert from "assert";

export default function (serverUrl: string) {
    const compendium = new CompendiumTester(3, serverUrl, Game.totk);

    describe("compendium", () => {
        describe("entries", () => {
            describe("all standard entries", () => {
                it("should have correct categories", (done) => {
                    var categories = new Set<String>();
                    compendium.getAllEntries((data) => {
                        for (let entry of data) {
                            categories.add(entry["category"]);
                        }
                        assert.equal(categories.size, 5);
                        assert(categories.has("creatures"));
                        assert(categories.has("equipment"));
                        assert(categories.has("materials"));
                        assert(categories.has("monsters"));
                        assert(categories.has("treasure"));
                        done();
                    }, CompendiumTester.fail);
                });
                it("should have 509 entries", (done) => {
                    compendium.getAllEntries((data) => {
                        let numOfEntries = Object.keys(data).length;
                        assert.equal(numOfEntries, 509);
                        done();
                    }, CompendiumTester.fail);
                });
            });
            describe("creature entry (non_food)", () => {
                it("should have correct fields", (done) => {
                    compendium.getEntry(Math.floor(Math.random() * (52 - 1)) + 1, (data) => {
                        let expectedAdditionalAttrs = ["drops", "edible"];
                        CompendiumTester.assertHasAttrs(
                            data, 
                            expectedAdditionalAttrs
                        ); 
                        
                        done();
                    }, CompendiumTester.fail);
                });
            });
            describe("creature entry (food)", () => {
                it("should have correct fields", (done) => {
                    compendium.getEntry(Math.floor(Math.random() * (92 - 53)) + 53, (data) => {
                        let expectedAdditionalAttrs = ["hearts_recovered", "edible", "cooking_effect"];
                        CompendiumTester.assertHasAttrs(
                            data, 
                            expectedAdditionalAttrs
                        ); 
                        
                        done();
                    }, CompendiumTester.fail);
                });
            });
            describe("monster entry", () => {
                it("should have correct fields", (done) => {
                    compendium.getEntry(Math.floor(Math.random() * (202 - 93)) + 93, (data) => {
                        let expectedAdditionalAttrs = ["drops"];
                        CompendiumTester.assertHasAttrs(
                            data, 
                            expectedAdditionalAttrs
                            ); 
                            done();
                        }, CompendiumTester.fail);
                });
            });
            describe("material entry", () => {
                it("should have correct fields", (done) => {
                    compendium.getEntry(Math.floor(Math.random() * (328 - 203)) + 203, (data) => {
                        let expectedAdditionalAttrs = ["hearts_recovered", "cooking_effect", "fuse_attack_power"];
                        CompendiumTester.assertHasAttrs(
                            data, 
                            expectedAdditionalAttrs
                        ); 
                        done();
                    }, CompendiumTester.fail);
                });
            });
            describe("equipment entry", () => {
                it("should have correct fields", (done) => {
                    compendium.getEntry(Math.floor(Math.random() * (503 - 329)) + 329, (data) => {
                        let expectedAdditionalAttrs = ["properties"];
                        CompendiumTester.assertHasAttrs(
                            data, 
                            expectedAdditionalAttrs
                        ); 
                        CompendiumTester.assertHasNestedAttrs(
                            data, 
                            "properties", 
                            ["attack", "defense", "effect", "type"]
                        );
                        done();
                    }, CompendiumTester.fail);
                });
            });
            describe("treasure entry", () => {
                it("should have correct fields", (done) => {
                    compendium.getEntry(Math.floor(Math.random() * (509 - 504)) + 504, (data) => {
                        let expectedAdditionalAttrs = ["drops"];
                        CompendiumTester.assertHasAttrs(
                            data, 
                            expectedAdditionalAttrs
                        ); 
                        done();
                    }, CompendiumTester.fail);
                });
            });
        });
        describe("categories", () => {
            describe("creatures", () => {
                it("should have 83 entries", (done) =>{
                    compendium.getCategory("creatures", (data) => {
                        assert.equal(
                            data.length,
                            92
                        );
                        done();
                    }, CompendiumTester.fail);
                });
            });
            describe("monsters", () => {
                it("should have 110 entries", (done) =>{
                    compendium.getCategory("monsters", (data) => {
                        assert.equal(
                            data.length,
                            110
                        );
                        done();
                    }, CompendiumTester.fail);
                });
            });
            describe("materials", () => {
                it("should have 126 entries", (done) =>{
                    compendium.getCategory("materials", (data) => {
                        assert.equal(
                            data.length,
                            126
                        );
                        done();
                    }, CompendiumTester.fail);
                });
            });
            describe("equipment", () => {
                it("should have 175 entries", (done) =>{
                    compendium.getCategory("equipment", (data) => {
                        assert.equal(
                            data.length,
                            175
                        );
                        done();
                    }, CompendiumTester.fail);
                });
            });
            
            describe("treasure", () => {
                it("should have 6 entries", (done) => {
                    compendium.getCategory("treasure", (data) => {
                        assert.equal(
                            data.length,
                            6
                        );
                        done();
                    }, CompendiumTester.fail);
                });
            });
        });
        /*
        describe("images", () => {
            it("should be png", (done) => {
                let entryId = Math.floor(Math.random() * (389 - 386)) + 386;
                compendium.getEntryImage(entryId, (content) => {
                    ImageTester.validateImage(entryId, content as Buffer, done, (err) => {
                        throw err;
                    });
                }, CompendiumTester.fail);
            });
        });
        */
    });
}