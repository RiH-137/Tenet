"use client";
import React, { useEffect } from "react";
import { useCallback, useState } from "react";
import { ethers } from "ethers";
import Image from "next/image";
import { Header } from "@/components/Header";
import { BadgeCheck, ShieldX, Upload } from "lucide-react";
import axios from "axios";
import { UploadButton } from "@/utils/uploadthing";
export interface AccountType {
  address?: string;
  balance?: string;
  chainId?: string;
  network?: string;
}

export default function Home() {
  const [accountData, setAccountData] = useState<AccountType>({});
  // const [message, setMessage] = useState<string>("");
  const [removing, setRemoving] = useState(false);
  const [fileurl, setFileUrl] = useState<string | undefined>(undefined);
  // const [sending, setSending] = React.useState(false);
  // const [uploading, setUploading] = React.useState(false);
  const clearClip = async () => {
    if (fileurl) {
      setRemoving(true);
      const res = await axios.post("/api/utapi", { fileurl });
      if (res.data.success) {
        setFileUrl(undefined);
      }
      setRemoving(false);
    }
  };
  const _connectToMetaMask = useCallback(async () => {
    const ethereum = window.ethereum;
    if (typeof ethereum !== "undefined") {
      try {
        const accounts = await ethereum.request({
          method: "eth_requestAccounts",
        });
        const address = accounts[0];
        const provider = new ethers.BrowserProvider(ethereum);
        const balance = await provider.getBalance(address);
        const network = await provider.getNetwork();
        const accountInfo: AccountType = {
          address,
          balance: ethers.formatEther(balance),
          chainId: network.chainId.toString(),
          network: network.name,
        };
        setAccountData(accountInfo);

        // Store the account information in local storage
        localStorage.setItem("accountData", JSON.stringify(accountInfo));
      } catch (error: Error | any) {
        alert(`Error connecting to MetaMask: ${error?.message ?? error}`);
      }
    } else {
      alert("MetaMask not installed");
    }
  }, []);

  // const _sendMessageToMetaMask = useCallback(async () => {
  //   const ethereum = await window.ethereum;
  //   const signer = await new ethers.BrowserProvider(ethereum).getSigner();
  //   try {
  //     await signer.signMessage(message);
  //     setMessage("");
  //   } catch (error) {
  //     alert("User denied message signature.");
  //   }
  // }, [message]);

  // const _onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
  //   setMessage(e.target.value);
  // };

  const _checkAccount = useCallback(async () => {
    const ethereum = window.ethereum;
    if (typeof ethereum !== "undefined") {
      const accounts = await ethereum.request({ method: "eth_accounts" });
      if (accounts.length === 0) {
        setAccountData({});
        localStorage.removeItem("accountData");
      } else if (accounts[0] !== accountData.address) {
        _connectToMetaMask();
      }
    }
  }, [accountData.address, _connectToMetaMask]);

  useEffect(() => {
    const storedAccountData = localStorage.getItem("accountData");
    if (storedAccountData) {
      setAccountData(JSON.parse(storedAccountData));
      _connectToMetaMask();
    }

    const accountCheckInterval = setInterval(_checkAccount, 1000);
    return () => clearInterval(accountCheckInterval);
  }, [_checkAccount, _connectToMetaMask]);

  return (
    <>
      <div
        className={`h-full flex flex-col before:from-white after:from-sky-200 py-2`}
      >
        <Header {...accountData} />
        <div className="flex flex-col min-h-[90vh] justify-center items-center my-4">
          <div className="flex flex-col justify-center items-center gap-10">
            <Image
              src="https://upload.wikimedia.org/wikipedia/commons/b/b2/Tenet_logo.png"
              alt="Tenet"
              width={320}
              height={140}
              priority
            />
            {accountData?.address ? (
              <>
                <div className=" w-[60vw] p-2 shadow-lg min-h-fit border-2 border-dotted border-gray-400 gap-4 flex flex-col justify-center items-center">
                  <div className="text-xl ">
                    Check legitimacy of the{" "}
                    <span className="font-bold text-[#27272A]"> CLIP</span>
                  </div>
                  <div className=" flex justify-center items-center p-4">
                    <button className="p-3 bg-[#FAFAFA] rounded-lg shadow-md flex justify-center gap-2">
                      Upload Clip <Upload />{" "}
                    </button>
                  </div>
                  <div className="text-sm">
                    clip size limit <span className="font-bold">*50MB</span>
                  </div>
                  <div className="flex justify-center w-full my-2 items-center gap-4">
          <span className="flex justify-center items-center flex-col-reverse gap-2">DeepFake <ShieldX enableBackground={"red"}/></span> <span className="flex-col-reverse flex gap-2 justify-center items-center">Original <BadgeCheck  color="green" /></span>
        </div>
                </div>
                
              </>
            ) : (
              <button
                onClick={_connectToMetaMask}
                className="bg-black text-white p-4 rounded-lg"
              >
                Connect to MetaMask
              </button>
            )}
          </div>
        </div>
      </div>
    </>
  );
}
