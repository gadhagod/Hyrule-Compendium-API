import request, { Response } from "request";
import { fail } from "assert";
import { Callback } from "../types";
import getType from "image-type";
import assert from "assert";

export enum Game { botw, totk }

/**
 * @since v3
 */
abstract class Tester {
    private serverUrl: string;
    private game: Game;

    constructor(url: string, game: Game) {
        this.serverUrl = url;
        this.game = game;
    }

    protected getRouteUrl(urlExtension?: string): string {
        return `${this.serverUrl}${urlExtension}?game=${Game[this.game]}`;
    }

    protected makeRequest(
        urlExtension: string, 
        successCallback: Callback.SuccessCallback, 
        errorCallback: Callback.ErrorCallback,
        encoding: string = "utf-8"
    ) {
        request(
            {
                url: this.getRouteUrl(urlExtension),
                encoding: encoding,
            }, 
            (err, res: Response) => {
                if (err || res.statusCode !== 200) {
                    errorCallback(res, err)
                    try {
                        successCallback(res)
                    } catch (err) {
                        errorCallback(res, err);
                    }
                } else {
                    successCallback(res);
                }
            }
        );
    }

    static fail: Callback.ErrorCallback = (res, err) => {
        fail(`ERROR: \nURL: ${res.request.href}\nStatus code: ${res.statusCode}\nError: ${err}`);
    }
}

export class ImageTester extends Tester {
    private serverExtension: string;

    constructor(serverUrl: string, serverExtension: string, game: Game) {
        super(serverUrl, game);
        this.serverExtension = serverExtension;
    }

    static validateImage(
        entryId: number,
        imageContent: Buffer, 
        successCallback: () => void, 
        errorCallback: Callback.Image.ValidateErrorCallback,
    ) {
        try {
            let imgData = getType(imageContent);
            if (imgData.mime === "image/png") {
                successCallback();
            } else {
                errorCallback(`ERR: Entry ${entryId} (200 status code); Image type is ${imgData.mime}`);
            }
        } catch (err) {
            errorCallback(`ERR: Entry ${entryId} (200 status code); ${err}`);
        }
    }

    protected makeRequest(urlExtension: string, successCallback: Callback.SuccessCallback, errorCallback: Callback.ErrorCallback) {
        super.makeRequest(
            this.serverExtension + urlExtension, 
            successCallback, 
            errorCallback, 
            null
        );
    }

    /**
     * @precondition ImageTester.createImageDir()
     */
    getImage(
        imageRoute: string, 
        successCallback: Callback.Image.GetSuccessCallback, 
        errorCallback: Callback.ErrorCallback
    ) {
        this.makeRequest(
            imageRoute, 
            (res) => {
                try {
                    successCallback(res.body);
                } catch (err) {
                    errorCallback(res, err);
                }
            },
            errorCallback
        );
    }
}

class ApiTester extends Tester {
    private version: number;
    private _serverExtension: string;

    constructor(version: number, serverUrl: string, route: string, game: Game) {
        super(serverUrl, game);
        if (version < 3) {
            throw "ERROR: ApiTester class only works for v3 and up";
        }
        this.version = version;
        this._serverExtension = `/api/v${version}${route}`;
    }

    protected makeRequest(urlExtension: string, successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback) {
        super.makeRequest(
            urlExtension,
            (res) => {
                if (res.statusCode !== 200) {
                    errorCallback(res, res.statusCode);
                } else {
                    try {
                        successCallback(JSON.parse(res.body)["data"]);
                    } catch (err) {
                        errorCallback(res, err);
                    }
                }
            },
            errorCallback
        )
    }

    get serverExtension() : string {
        return this._serverExtension;
    }

    static assertHasAttrs(data: {}, attrs?: string[], id?: number | string) {
        if (!(
            Object.keys(data).includes("name") &&
            Object.keys(data).length == attrs.length &&
            (() => {
                for (let i = 0; i < attrs.length; i++) {
                    if (!Object.keys(data).includes(attrs[i])) {
                        return false;
                    }
                }
                return true;
            })())
        ) {
            assert.fail(
                `${(id ? `${id}: ` : "")}[${Object.keys(data)}] doesn't contain '${attrs.slice(0, -1).join("', '")}', or '${attrs[attrs.length - 1]}'`
            );
        };
    }

    static assertHasNestedAttrs(data: {}, key: string, nestedAttrs: string[], id?: number | string) {
        if (!(Object.keys(data).includes(key) && Object.keys(data[key]).length == nestedAttrs.length && (() => {
            let keys = Object.keys(data[key]);
            for (let i = 0; i < nestedAttrs.length; i++) {
                if (!keys.includes(nestedAttrs[i])) {
                    return false;
                }
                return true;
            }
        })())) {
            console.log(Object.keys(data).includes(key))
            assert.fail(
                `${(id ? `${id}: ` : "")}attribute '${key}' doesn't contain '${nestedAttrs.slice(0, -1).join("', '")}', or '${nestedAttrs[nestedAttrs.length - 1]}'`
            );
        };
    }
}

export class CompendiumTester extends ApiTester {
    private readonly imageTester: ImageTester;

    constructor(version: number, serverUrl: string, game: Game) {
        super(version, serverUrl, "/compendium", game);
        this.imageTester = new ImageTester(serverUrl, this.serverExtension, game);
    }
    getEntry(entryIdOrName: string | number, successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback) {
        this.makeRequest(`/entry/${entryIdOrName}`, successCallback, errorCallback);
    }
    getCategory(categoryName: string, successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback) {
        this.makeRequest(`/category/${categoryName}`, successCallback, errorCallback);
    }
    getAllEntries(successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback) {
        this.makeRequest("/all", successCallback, errorCallback);
    }
    getMasterModeEntry(entryIdOrName: string | number, successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback) {
        this.makeRequest(`/master_mode/entry/${entryIdOrName}`, successCallback, errorCallback);
    }
    getAllMasterModeEntries(successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback) {
        this.makeRequest("/master_mode/all", successCallback, errorCallback);
    }
    getEntryImage(entryIdOrName: string | number, successCallback: Callback.Image.GetSuccessCallback, errorCallback: Callback.ErrorCallback) {
        this.imageTester.getImage(
            `/entry/${entryIdOrName}/image`, 
            successCallback, 
            errorCallback
        );
    }

    protected makeRequest(urlExtension: string, successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback): void {
        super.makeRequest(
            this.serverExtension + urlExtension,
            successCallback,
            errorCallback
        )
    }

    static assertHasAttrs(entryData: {id: number}, expectedCategoryAttrs: string[]) {
        return (
            super.assertHasAttrs(
                entryData,
                ["name", "category", "common_locations", "description", "id", "image", "dlc"].concat(expectedCategoryAttrs),
                entryData.id
            )
        );
    }
}

export class RegionTester extends ApiTester {
    constructor(version: number, serverUrl: string, game: Game.botw) {
        super(version, serverUrl, "/regions", game);
    }
    getRegion(regionName: string, successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback) {
        this.makeRequest(`/${regionName}`, successCallback, errorCallback);
    }
    getAllRegions(successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback) {
        this.makeRequest("/all", successCallback, errorCallback);
    }
    protected makeRequest(urlExtension: string, successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback): void {
        super.makeRequest(
            this.serverExtension + urlExtension,
            successCallback,
            errorCallback
        )
    }

    static assertHasAttrs(categoryData: {name: string}): void {
        super.assertHasAttrs(
            categoryData,
            ["dlc_shrines", "name", "shrines", "settlements"],
            categoryData.name
        )
    }
}