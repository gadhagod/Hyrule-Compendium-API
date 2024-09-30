import assert from "assert";
import request from "request";
import fs from "fs";
import readChunk from 'read-chunk';
import imageType from 'image-type';
import { APIImageRequest, Entry } from "./types";
import { validateMIMEType } from "validate-image-type";

if (fs.existsSync("out")) {
    fs.rmdirSync("out", { recursive: true });
}
fs.mkdirSync("out");

function makeReq(
    endpoint: string,
    callback: (arg0: any, arg1: any) => void,
    image: false | APIImageRequest = false
) {
    let url = `${(process.env.URL ?? "https://botw-compendium.herokuapp.com") + "/api/v2"}${endpoint}`;
    if (image) {
        request.head(url, (_err: any, res: any) => {
            request(url)
                .pipe(fs.createWriteStream((image as APIImageRequest).filename))
                .on("close", callback);
        });
    } else {
        request(
            {
                url: url,
                jar: true,
                followAllRedirects: false,
            },
            callback
        );
    }
}

describe("v2", () => {

    describe("Server HTTP codes", () => {
        describe("`/entry/<>` endpoint", () => {
            it("should have 410 code", (done) => {
                makeReq("/entry/1", (_err, res) => {
                    assert.equal(res.statusCode, 410, `Entry 1 responded with code ${res.statusCode}`)
                    done()
                })
            });
        });
        describe("`/master_mode/entry/<>` endpoint", () => {
            it("should have 410 code", (done) => {
                makeReq("/master_mode/entry/97", (_err, res) => {
                    assert.equal(res.statusCode, 410, `DLC Entry 97 responded with code ${res.statusCode}`)
                    done()
                })
            });
        });
        describe("`/category/<>` endpoint", () => {
            it("should have 410 code", (done) => {
                makeReq("/category/monsters", (_err, res) => {
                    assert.equal(res.statusCode, 410, `Responded with code ${res.statusCode}`)
                    done()
                })
            });
        });
        describe("`/master_mode` endpoint", () => {
            it("should have 410 code", (done) => {
                makeReq("/master_mode", (_err, res) => {
                    assert.equal(res.statusCode, 410, `DLC Entry 97 responded with code ${res.statusCode}`)
                    done()
                })
            });
        });
        describe("`/` endpoint", () => {
            it("should have 410 code", (done) => {
                makeReq("", (_err, res) => {
                    assert.equal(res.statusCode, 410, `Responded with code ${res.statusCode}`)
                    done()
                })
            });
        });
    });
});