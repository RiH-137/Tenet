import { UTApi } from "uploadthing/server";
 
export const utapi = new UTApi();
export async function deleteFile(fileUrl: string) {
        const response = await utapi.deleteFiles(fileUrl)
        if(response.success) return true
        return false   
}