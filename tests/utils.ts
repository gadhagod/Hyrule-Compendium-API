export interface APIImageRequest { filename: string }
export interface Entry {
    name: string
    category: string
    common_locations: string[] // sorry for annoying snake admist a stampede of camels
    [otherOptions: string]: unknown
}