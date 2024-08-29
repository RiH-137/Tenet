"use client";
import React, { useEffect } from "react";
import { useCallback, useState } from "react";
import { ethers } from "ethers";
import Image from "next/image";
import { Header } from "./Header";
import Home from "@/app/page";
export interface AccountType {
  address?: string;
  balance?: string;
  chainId?: string;
  network?: string;
}

const MetaMask = () => {
  const [accountData, setAccountData] = useState<AccountType>({});
  const [message, setMessage] = useState<string>("");
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

  const _sendMessageToMetaMask = useCallback(async () => {
    const ethereum = await window.ethereum;
    const signer = await new ethers.BrowserProvider(ethereum).getSigner();
    try {
      await signer.signMessage(message);
      setMessage("");
    } catch (error) {
      alert("User denied message signature.");
    }
  }, [message]);

  const _onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setMessage(e.target.value);
  };

  

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
    <div
      className={`h-full flex flex-col before:from-white after:from-sky-200 py-2`}
    >
      <Header {...accountData} />
      <div className="flex flex-col h-[40vh] justify-center items-center">
        <div className="grid gap-4">
          <Image
            src="https://upload.wikimedia.org/wikipedia/commons/b/b2/Tenet_logo.png"
            alt="Tenet"
            width={320}
            height={140}
            priority
          />
          {!accountData?.address && 
            <button
              onClick={_connectToMetaMask}
              className="bg-black text-white p-4 rounded-lg"
            >
              Connect to MetaMask
            </button>
}
        </div>
      </div>
    </div>
  );
};

export default MetaMask;
