import assert from "assert";
import { CompendiumTester, ImageTester, RegionTester } from "./util";

let config = {
    version: 3,
    serverUrl: process.env.URL ?? "https://botw-compendium.herokuapp.com"
}

const compendium = new CompendiumTester(config.version, config.serverUrl);
const regions = new RegionTester(config.version, config.serverUrl);

describe("v3", () => {
    describe("compendium", () => {
        describe("standard", () => {
            describe("entries", () => {
                describe("all standard entries", () => {
                    it("should have 5 categories", (done) => {
                        compendium.getAllEntries((data) => {
                            assert.equal(Object.keys(data).length, 5);
                            done();
                        }, CompendiumTester.fail);
                    });
                    it("should have 389 entries", (done) => {
                        compendium.getAllEntries((data) => {
                            let numOfEntries = 0;
                            console.log(data.length)
                            for (let i = 0; i < Object.keys(data).length; i++) {
                                if (Object.keys(data)[i] === "creatures") {
                                    numOfEntries += data["creatures"]["food"].length;
                                    numOfEntries += data["creatures"]["non_food"].length;
                                } else {
                                    numOfEntries += data[Object.keys(data)[i]].length;
                                }
                            }
                            assert.equal(numOfEntries, 389);
                            done();
                        }, CompendiumTester.fail);
                    });
                });
                describe("creature entry (non_food)", () => {
                    it("should have correct fields", (done) => {
                        compendium.getEntry(Math.floor(Math.random() * (47 - 1)) + 1, (data) => {
                            let expectedAdditionalAttrs = ["drops"];
                            let expectedNumOfFields = 6 + expectedAdditionalAttrs.length;
                            CompendiumTester.assertHasAttrs(
                                data, 
                                expectedAdditionalAttrs
                            ); 
                            assert.equal(
                                Object.keys(data).length, 
                                expectedNumOfFields, 
                                `Entry ${data.id}; ${Math.abs(Object.keys(data).length - expectedNumOfFields)} extra/less field(s). \nExpected: [${Object.keys(data)}].length === ${expectedNumOfFields}`
                            );
                            done();
                        }, CompendiumTester.fail);
                    });
                });
                describe("creature entry (food)", () => {
                    it("should have correct fields", (done) => {
                        compendium.getEntry(Math.floor(Math.random() * (83 - 48)) + 48, (data) => {
                            let expectedAdditionalAttrs = ["hearts_recovered", "cooking_effect"];
                            let expectedNumOfFields = 6 + expectedAdditionalAttrs.length;
                            CompendiumTester.assertHasAttrs(
                                data, 
                                expectedAdditionalAttrs
                            ); 
                            assert.equal(
                                Object.keys(data).length, 
                                expectedNumOfFields, 
                                `Entry ${data.id}; ${Math.abs(Object.keys(data).length - expectedNumOfFields)} extra/less field(s). \nExpected: [${Object.keys(data)}].length === ${expectedNumOfFields}`
                            );
                            done();
                        }, CompendiumTester.fail);
                    });
                });
                describe("equipment entry", () => {
                    it("should have correct fields", (done) => {
                        compendium.getEntry(Math.floor(Math.random() * (385 - 201)) + 201, (data) => {
                            let expectedAdditionalAttrs = ["attack", "defense"];
                            let expectedNumOfFields = 6 + expectedAdditionalAttrs.length;
                            CompendiumTester.assertHasAttrs(
                                data, 
                                expectedAdditionalAttrs
                            ); 
                            assert.equal(
                                Object.keys(data).length, 
                                expectedNumOfFields, 
                                `Entry ${data.id}; ${Math.abs(Object.keys(data).length - expectedNumOfFields)} extra/less field(s). \nExpected: [${Object.keys(data)}].length === ${expectedNumOfFields}`
                            );
                            done();
                        }, CompendiumTester.fail);
                    });
                });
                describe("material entry", () => {
                    it("should have correct fields", (done) => {
                        compendium.getEntry(Math.floor(Math.random() * (200 - 165)) + 165, (data) => {
                            let expectedAdditionalAttrs = ["hearts_recovered", "cooking_effect"];
                            let expectedNumOfFields = 6 + expectedAdditionalAttrs.length;
                            CompendiumTester.assertHasAttrs(
                                data, 
                                expectedAdditionalAttrs
                            ); 
                            assert.equal(
                                Object.keys(data).length, 
                                expectedNumOfFields, 
                                `Entry ${data.id}; ${Math.abs(Object.keys(data).length - expectedNumOfFields)} extra/less field(s). \nExpected: [${Object.keys(data)}].length === ${expectedNumOfFields}`
                            );
                            done();
                        }, CompendiumTester.fail);
                    });
                });
                describe("monster entry", () => {
                    it("should have correct fields", (done) => {
                        compendium.getEntry(Math.floor(Math.random() * (164 - 84)) + 84, (data) => {
                            let expectedAdditionalAttrs = ["drops"];
                            let expectedNumOfFields = 6 + expectedAdditionalAttrs.length;
                            CompendiumTester.assertHasAttrs(
                                data, 
                                expectedAdditionalAttrs
                            ); 
                            assert.equal(
                                Object.keys(data).length, 
                                expectedNumOfFields, 
                                `Entry ${data.id}; ${Math.abs(Object.keys(data).length - expectedNumOfFields)} extra/less field(s). \nExpected: [${Object.keys(data)}].length === ${expectedNumOfFields}`
                            );
                            done();
                        }, CompendiumTester.fail);
                    });
                });
                describe("treasure entry", () => {
                    it("should have correct fields", (done) => {
                        compendium.getEntry(Math.floor(Math.random() * (389 - 386)) + 386, (data) => {
                            let expectedAdditionalAttrs = ["drops"];
                            let expectedNumOfFields = 6 + expectedAdditionalAttrs.length;
                            CompendiumTester.assertHasAttrs(
                                data, 
                                expectedAdditionalAttrs
                            ); 
                            assert.equal(
                                Object.keys(data).length, 
                                expectedNumOfFields, 
                                `Entry ${data.id}; ${Math.abs(Object.keys(data).length - expectedNumOfFields)} extra/less field(s). \nExpected: [${Object.keys(data)}].length === ${expectedNumOfFields}`
                            );
                            done();
                        }, CompendiumTester.fail);
                    });
                });
            });
            describe("categories", () => {
                describe("creatures", () => {
                    it("should have 2 sub-categories", (done) =>{
                        compendium.getCategory("creatures", (data) => {
                            assert.equal(Object.keys(data).length, 2);
                            done();
                        }, CompendiumTester.fail);
                    });
                    it("should have 52 entries", (done) =>{
                        compendium.getCategory("creatures", (data) => {
                            assert.equal(
                                data["non_food"].length + data["non_food"].length,
                                94
                            );
                            done();
                        }, CompendiumTester.fail);
                    });
                });
                describe("equipment", () => {
                    it("should have 185 entries", (done) =>{
                        compendium.getCategory("equipment", (data) => {
                            assert.equal(
                                data.length,
                                185
                            );
                            done();
                        }, CompendiumTester.fail);
                    });
                });
                describe("materials", () => {
                    it("should have 36 entries", (done) =>{
                        compendium.getCategory("materials", (data) => {
                            assert.equal(
                                data.length,
                                36
                            );
                            done();
                        }, CompendiumTester.fail);
                    });
                });
                describe("monsters", () => {
                    it("should have 81 entries", (done) =>{
                        compendium.getCategory("monsters", (data) => {
                            assert.equal(
                                data.length,
                                81
                            );
                            done();
                        }, CompendiumTester.fail);
                    });
                });
                describe("treasure", () => {
                    it("should have 4 entries", (done) => {
                        compendium.getCategory("treasure", (data) => {
                            assert.equal(
                                data.length,
                                4
                            );
                            done();
                        }, CompendiumTester.fail);
                    });
                });
            });
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
        });
        describe("dlc", () => {
            describe("entries", () => {
                it("should have 5 entries", (done) => {
                    compendium.getAllMasterModeEntries((data) => {
                        assert.equal(
                            data.length,
                            5
                        );
                        done();
                    }, CompendiumTester.fail);
                });
                it("should have correct fields", (done) => {
                    compendium.getEntry(Math.floor(Math.random() * (164 - 84)) + 84, (data) => {
                        let expectedAdditionalAttrs = ["drops"];
                        let expectedNumOfFields = 6 + expectedAdditionalAttrs.length;
                        CompendiumTester.assertHasAttrs(
                            data, 
                            expectedAdditionalAttrs
                        ); 
                        assert.equal(
                            Object.keys(data).length, 
                            expectedNumOfFields, 
                            `Entry ${data.id}; ${Math.abs(Object.keys(data).length - expectedNumOfFields)} extra/less field(s). \nExpected: [${Object.keys(data)}].length === ${expectedNumOfFields}`
                        );
                        done();
                    }, CompendiumTester.fail);
                });
            })
            describe("images", () => {
                it("should be png", (done) => {
                    let entryId = Math.floor(Math.random() * (129 - 97)) + 97;
                    compendium.getEntryImage(entryId, (content) => {
                        ImageTester.validateImage(entryId, content as Buffer, done, (err) => {
                            throw err;
                        });
                    }, CompendiumTester.fail);
                });
            });
        });
    });
    
    describe("regions", () => {
        let expectedReigonNames = ["hebra", "central", "eldin", "hateno", "ridgeland", "gerudo", "wasteland", "tabantha", "dueling peaks", "lake", "great plateau", "woodland", "akkala", "lanayru", "faron"]
        describe("get all regions", () => {
            it(`should have correct regions`, (done) => {
                regions.getAllRegions((data) => {
                    assert.equal(data.length, expectedReigonNames.length, `STATUS CODE: 200; Expected regions do not match recieved regions`);
                    for (let i = 0; i < expectedReigonNames.length; i++) {
                        if (!data.includes(expectedReigonNames[i])) {
                            assert.fail(`STATUS CODE: 200; Expected regions do not match recieved regions`)
                        }
                    }
                    done()
                }, RegionTester.fail);
            });
        });
        describe("get single region", () => {
            it("should have correct fields", (done) => {
                regions.getRegion(expectedReigonNames[Math.floor(Math.random() * expectedReigonNames.length)], (data) => {
                    RegionTester.assertHasAttrs(data);
                    done();
                }, RegionTester.fail);
            })
        });
    });
});