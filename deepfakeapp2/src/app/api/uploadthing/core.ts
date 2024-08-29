import { createUploadthing, type FileRouter } from "uploadthing/next";
const f = createUploadthing();
export const ourFileRouter = {
  attachment: f( {video: { maxFileSize: "128MB" }} )
    .middleware(async ({ req }) => {
      return { Id: 125 };
    })
    .onUploadComplete(async ({ metadata, file }) => {
      console.log("Upload complete for userId:", metadata.Id);

      console.log("file url", file.url);
      return { fileUrl: file.url };
    }),
} satisfies FileRouter;

export type OurFileRouter = typeof ourFileRouter;
