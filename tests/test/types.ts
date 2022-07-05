import { PathOrFileDescriptor } from "fs";
import { Response } from "request";

export interface APIImageRequest { filename: string };
export interface Entry {
    name: string
    category: string
    common_locations: string[] // sorry for annoying snake admist a stampede of camels
    [otherOptions: string]: unknown
};
export namespace Callback {
    export namespace Api {
        export type SuccessCallback = (data: any) => void;
    }
    export namespace Image {
        export type SuccessCallback = (path: PathOrFileDescriptor) => void;
    }
    export type SuccessCallback = (res: Response) => void;
    export type ErrorCallback = (res: Response, err: any) => void;
}