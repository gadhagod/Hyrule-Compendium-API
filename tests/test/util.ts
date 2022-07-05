import request, { Response } from "request";
import { writeFileSync, mkdirSync, rmdirSync, existsSync, rmSync } from "fs";
import { Callback } from "./types";

class Tester {
    private serverUrl: string;

    constructor(url: string) {
        this.serverUrl = url;
    }

    protected getRouteUrl(urlExtension?: string): string {
        return `${this.serverUrl}${urlExtension}`;
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
                encoding: encoding
            }, 
            (err, res: Response) => {
                if (err || res.statusCode !== 200) {
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
}

class ImageTester extends Tester {
    private static imageCount = 0;
    private _imageDir: string;
    private serverExtension = "";

    constructor(serverUrl: string, serverExtension: string) {
        super(serverUrl);
        this.serverExtension = serverExtension;
        if (existsSync(`${__dirname}/.img`)) {
            ImageTester.rmImageDir(`.img`);
        }
        ImageTester.createImageDir(".img");
    }

    private static createImageDir(dirName: string) : string {
        let path = `${__dirname}/${dirName}`;
        mkdirSync(path);
        return path;
    }

    static rmImageDir(dirName: string) {
        rmdirSync(`${__dirname}/${dirName}`);
    }

    static downloadImage(dirPath: string, body: Buffer) : string {
        console.log(body)
        ImageTester.imageCount++;
        let filePath = `${dirPath}/${ImageTester.imageCount}.png`;
        writeFileSync(filePath, body);
        return filePath;
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
        successCallback: Callback.Image.SuccessCallback, 
        errorCallback: Callback.ErrorCallback
    ) {
        this.makeRequest(
            imageRoute, 
            (res) => {
                try {
                    successCallback(ImageTester.downloadImage(this._imageDir, res.body));
                } catch (err) {
                    errorCallback(res, err);
                }
            },
            errorCallback
        );
    }

    get imageDir() : string {
        return this._imageDir;
    }
}

class ApiTester extends Tester {
    private version: number;
    private baseUrl: string;
    private _serverExtension: string;

    constructor(version: number, serverUrl: string, route: string) {
        super(serverUrl);
        if (version < 3) {
            throw "ERROR: ApiTester class only works for v3 and up";
        }
        this.version = version;
        this._serverExtension = `/api/v${version}/${route}`;
        this.baseUrl = `${serverUrl}${this._serverExtension}`;
    }

    protected makeRequest(urlExtension: string, successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback) {
        super.makeRequest(
            urlExtension,
            (res) => {
                if (res.statusCode !== 200) {
                    errorCallback(res, res.statusCode);
                } else {
                    try {
                        successCallback(JSON.parse(res.body));
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
}

export class CompendiumTester extends ApiTester {
    private imageTester: ImageTester;

    protected makeRequest(urlExtension: string, successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback): void {
        super.makeRequest(
            this.serverExtension + urlExtension,
            successCallback,
            errorCallback
        )
    }

    constructor(version: number, serverUrl: string) {
        super(version, serverUrl, "compendium");
        this.imageTester = new ImageTester(serverUrl, this.serverExtension);
    }
    getEntry(entryIdOrName: string | number, successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback) {
        this.makeRequest(`/entry/${entryIdOrName}`, successCallback, errorCallback);
    }
    getCategory(successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback, categoryName: string) {
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
    getEntryImage(entryIdOrName: string | number, successCallback: Callback.Image.SuccessCallback, errorCallback: Callback.ErrorCallback) {
        this.imageTester.getImage(
            `/entry/${entryIdOrName}/image`, 
            successCallback, 
            errorCallback
        );
        
    }
}

export class RegionTester extends ApiTester {
    constructor(version: number, serverUrl: string) {
        super(version, serverUrl, "regions");
    }
    getRegion(regionName: string, successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback) {
        this.makeRequest(`/region/${regionName}`, successCallback, errorCallback);
    }
    getAllRegions(successCallback: Callback.Api.SuccessCallback, errorCallback: Callback.ErrorCallback) {
        this.makeRequest("/region/all", successCallback, errorCallback);
    }
}