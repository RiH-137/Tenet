import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
const inter = Inter({ subsets: ["latin"] });


export const metadata: Metadata = {
  title: "Home",
  description: "Deepfake Detection By Team Tenet",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  
  return (
    <html lang="en">
      <body className={`flex min-h-screen flex-col w-full bg-[#ECFEFF]`+ inter.className}>
        {children}
      </body>
    </html>
  );
}
