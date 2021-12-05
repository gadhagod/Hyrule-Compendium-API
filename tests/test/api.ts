const assert = require("assert");
const request = require("request");
const fs = require("fs")
const validateMIMEType = require("validate-image-type").validateMIMEType
import { APIImageRequest, Entry } from "../utils"

if (fs.existsSync("out")){
    fs.rmdirSync("out", { recursive: true });
}
fs.mkdirSync("out");

console.log("Using base URL " + (process.env.URL ?? "https://botw-compendium.herokuapp.com/api/v2"))

function make_req(endpoint: string, callback: (arg0: any, arg1: any) => void, image: false|APIImageRequest=false) {
    let url = `${process.env.URL ?? "https://botw-compendium.herokuapp.com/api/v2"}${endpoint}`
    if (image) {
        request.head(url, (_err: any, res: any) => {
            request(url).pipe(fs.createWriteStream((image as APIImageRequest).filename)).on("close", callback)
        });
    } else {
        request({
            url: url,
            jar: true,
            followAllRedirects: false
        }, callback)
    }
}

describe("Server HTTP codes", () => {
    describe("`/entry/<>` endpoint", () => {
        it("should have 200 code", (done) => {
            make_req("/entry/1", (_err, res) => {
                assert.equal(res.statusCode, 200, `Entry 1 responded with code ${res.statusCode}`)
                done()
            })
        });
    });
    describe("`/category/<>` endpoint", () => {
        it("should have 200 code", (done) => {
            make_req("/category/monsters", (_err, res) => {
                assert.equal(res.statusCode, 200, `Responded with code ${res.statusCode}`)
                done()
            })
        });
    });
    describe("`/` endpoint", () => {
        it("should have 200 code", (done) => {
            make_req("", (_err, res) => {
                assert.equal(res.statusCode, 200, `Responded with code ${res.statusCode}`)
                done()
            })
        });
    });
});

describe("API response contents", () => {
    describe("Entries", () => {
        describe("Creature entry", () => {
            let entry = "thunderwing butterfly"
            it("should have expected fields", (done) => {
                make_req(`/entry/${entry}`, (_err, res) => {
                    assert.deepEqual(
                        Object.keys(
                            JSON.parse(res.body).data
                        ), 
                        ["category", "common_locations", "cooking_effect", "description", "hearts_recovered", "id", "image", "name"], 
                        `Responded with incorrect fields.`
                    )
                    done()
                })
            });
            it("should have working image", (done) => {
                make_req(`/entry/${entry}/image`, () => {
                    let result = validateMIMEType(`out/${entry}.png`, {allowMimeTypes: ["image/png"]})
                    assert.equal(result.ok, true, result.error)
                    done()
                }, {filename: `out/${entry}.png`})
            });
        }); 
        describe("Equipment entry", () => {
            let entry = "golden claymore"
            it("should have expected fields", (done) => {
                make_req(`/entry/${entry}`, (_err, res) => {
                    assert.deepEqual(
                        Object.keys(
                            JSON.parse(res.body).data
                        ), 
                        ["attack", "category", "common_locations", "defense", "description", "id", "image", "name"], 
                        `Responded with incorrect fields.`
                    )
                    done()
                })
            });
            it("should have working image", (done) => {
                make_req(`/entry/${entry}/image`, () => {
                    let result = validateMIMEType(`out/${entry}.png`, {allowMimeTypes: ["image/png"]})
                    assert.equal(result.ok, true, result.error)
                    done()
                }, {filename: `out/${entry}.png`})
            });
        });
        describe("Material entry", () => {
            let entry = "palm fruit"
            it("should have expected fields", (done) => {
                make_req(`/entry/${entry}`, (_err, res) => {
                    assert.deepEqual(
                        Object.keys(
                            JSON.parse(res.body).data
                        ), 
                        ["category", "common_locations", "cooking_effect", "description", "hearts_recovered", "id", "image", "name"], 
                        `Responded with incorrect fields.`
                    )
                    done()
                })
            });
            it("should have working image", (done) => {
                make_req(`/entry/${entry}/image`, () => {
                    let result = validateMIMEType(`out/${entry}.png`, {allowMimeTypes: ["image/png"]})
                    assert.equal(result.ok, true, result.error)
                    done()
                }, {filename: `out/${entry}.png`})
            });
        });
        describe("Monster entry", () => {
            let entry = "molduga"
            it("should have expected fields", (done) => {
                make_req(`/entry/${entry}`, (_err, res) => {
                    assert.deepEqual(
                        Object.keys(
                            JSON.parse(res.body).data
                        ), 
                        ["category", "common_locations", "description", "drops", "id", "image", "name"], 
                        `Responded with incorrect fields.`
                    )
                    done()
                })
            });
            it("should have working image", (done) => {
                make_req(`/entry/${entry}/image`, () => {
                    let result = validateMIMEType(`out/${entry}.png`, {allowMimeTypes: ["image/png"]})
                    assert.equal(result.ok, true, result.error)
                    done()
                }, {filename: `out/${entry}.png`})
            });
        });
        describe("Treasure entry", () => {
            let entry = "molduga"
            it("should have expected fields", (done) => {
                make_req(`/entry/${entry}`, (_err, res) => {
                    assert.deepEqual(
                        Object.keys(
                            JSON.parse(res.body).data
                        ), 
                        ["category", "common_locations", "description", "drops", "id", "image", "name"], 
                        `Responded with incorrect fields.`
                    )
                    done()
                })
            });
            it("should have working image", (done) => {
                make_req(`/entry/${entry}/image`, () => {
                    let result = validateMIMEType(`out/${entry}.png`, {allowMimeTypes: ["image/png"]})
                    assert.equal(result.ok, true, result.error)
                    done()
                }, {filename: `out/${entry}.png`})
            });
        });
    });

    describe("Categories", () => {
        describe("Creature category", () => {
            it("should have correct of # sub-categories", (done) => {
                make_req("/category/creatures", (_err, res) => {
                    assert.equal(
                        Object.keys(JSON.parse(res.body).data).length,
                        2
                    )
                    done()
                })
            });
            it("should have correct of # entries", (done) => {
                make_req("/category/creatures", (_err, res) => {
                    assert.equal(
                        Object.keys(JSON.parse(res.body).data.non_food).length + Object.keys(JSON.parse(res.body).data.food).length,
                        83
                    )
                    done()
                })
            });
            it("entries should be of category", (done) => {
                make_req("/category/creatures", (_err, res) => {
                    try {
                        var entries = Object.assign(JSON.parse(res.body).data.food, JSON.parse(res.body).data.non_food)
                    } catch (err) {
                        if (err.name == "SyntaxError") {
                            assert.fail("Subcategories non-existant")
                        } else {
                            throw err
                        }
                    }
                    entries.forEach((e: Entry)  => assert.equal(e.category, "creatures"))
                    done()
                })
            });
        });
        describe("Equipment category", () => {
            it("should have correct of # entries", (done) => {
               make_req("/category/equipment", (_err, res) => {
                   var entries = JSON.parse(res.body).data
                    assert.equal(
                       Object.keys(entries).length,
                       185
                    )
                    done()
               }) 
            });
            it("entries should be of category", (done) => {
                make_req("/category/equipment", (_err, res) => {
                    var entries = JSON.parse(res.body).data
                    entries.forEach((e: Entry)  => assert.equal(e.category, "equipment"))
                    done()
                })
            });
        });
        describe("Materials category", () => {
            it("should have correct of # entries", (done) => {
                make_req("/category/materials", (_err, res) => {
                    var entries = JSON.parse(res.body).data
                    assert.equal(
                        Object.keys(entries).length,
                        36
                    )
                    done()
                }) 
             });
             it("entries should be of category", (done) => {
                make_req("/category/materials", (_err, res) => {
                    var entries = JSON.parse(res.body).data
                    entries.forEach((e: Entry)  => assert.equal(e.category, "materials"))
                    done()
                })
            });
        });
        describe("Monsters category", () => {
            it("should have correct of # entries", (done) => {
                make_req("/category/monsters", (_err, res) => {
                    var entries = JSON.parse(res.body).data
                    assert.equal(
                        Object.keys(entries).length,
                        81
                    )
                    done()
                }) 
             });
             it("entries should be of category", (done) => {
                make_req("/category/monsters", (_err, res) => {
                    var entries = JSON.parse(res.body).data
                    entries.forEach((e: Entry)  => assert.equal(e.category, "monsters"))
                    done()
                })
            });
        });
        describe("Treasure category", () => {
            it("should have correct of # entries", (done) => {
                make_req("/category/treasure", (_err, res) => {
                    var entries = JSON.parse(res.body).data
                    assert.equal(
                        Object.keys(entries).length,
                        4
                    )
                    done()
                }) 
             });
             it("entries should be of category", (done) => {
                make_req("/category/treasure", (_err, res) => {
                    var entries = JSON.parse(res.body).data
                    entries.forEach((e: Entry)  => assert.equal(e.category, "treasure"))
                    done()
                })
            });
        });
        describe("All data", () => {
            it("should have correct of # entries", (done) => {
                make_req("", (_err, res) => {
                    let data = JSON.parse(res.body).data
                    assert.equal(
                        data.creatures.food.length + data.creatures.non_food.length + data.equipment.length + data.materials.length + data.monsters.length + data.treasure.length,
                        389
                    )
                    done()
                })
            });
            it("should have correct of # categories", (done) => {
                make_req("", (_err, res) => {
                    assert.equal(
                        Object.keys(JSON.parse(res.body).data).length,
                        5
                    )
                    done()
                })
            });
        }); 
    });
});

fs.rmdirSync("out", { recursive: true });