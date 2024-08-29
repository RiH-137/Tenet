import { UTApi } from "uploadthing/server";
import { NextResponse, NextRequest } from "next/server";
const utapi = new UTApi();
export async function POST(req: NextRequest) {
  try {
    const { fileurl } = await req.json();
    const user = {id:125}
    if (user?.id) {

      const response = await utapi.deleteFiles(extractFilename(fileurl));
      if (response.success) return NextResponse.json({ success: true }, { status: 200 });
      return NextResponse.json({ success: false }, { status: 200 });
    }
    return NextResponse.json({ message: "Unauthorized" }, { status: 401 });
  } catch (error) {
    console.log("error from get current user");
    return NextResponse.json(error);
  }
}
const extractFilename = (url:string) => {
  const parts = url.split('/');
  return parts[parts.length - 1];
};