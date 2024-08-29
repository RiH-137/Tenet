import { AccountType } from "./MetaMask";

interface HeaderProps extends AccountType {}

export const Header = ({ address, balance, chainId, network }: HeaderProps) => {
  return (
    <div className="px-6 md:px-12 sm:px-2 bg-white">
      <div className="flex justify-between items-centers">
        <div className="flex-1 px-2 mx-2">
          <span>🟢 {address ?? "Wallet Address"}</span>
        </div>
        <div className="flex gap-8 items-center">
          <div className="flex items-center gap-2">
            <span>{balance ?? "Balance"}</span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width={24}
              height={24}
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"
              />
            </svg>
          </div>
          <div className="flex gap-2 item-center">
            <span>{chainId ?? "Chain ID"}</span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width={24}
              height={24}
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"
              />
            </svg>
          </div>
          <div className="flex gap-2 item-center">
            <span>{network ?? "Network"}</span>
            <svg
              className="svg-icon"
              width={24}
              height={24}
              viewBox="0 0 1024 1024"
              version="1.1"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M1024.26 141.82c0-77.04-62.46-139.5-139.5-139.5s-139.5 62.46-139.5 139.5c0 52.26 28.74 97.8 71.27 121.69l-55.6 246.87c-1.38-0.04-2.77-0.07-4.17-0.07-38.52 0-73.39 15.61-98.63 40.85l-254.64-147a140.05 140.05 0 0 0 3.78-32.34c0-77.04-62.46-139.5-139.5-139.5s-139.5 62.46-139.5 139.5c0 51.45 27.86 96.39 69.32 120.58l-56.9 252.62c-0.4 0-0.79-0.01-1.18-0.01C62.46 745 0 807.46 0 884.5S62.46 1024 139.5 1024 279 961.54 279 884.5c0-51.25-27.65-96.04-68.83-120.29l56.96-252.89c0.21 0 0.43 0.01 0.64 0.01 39.99 0 76.05-16.83 101.48-43.79L622.06 613.5a139.612 139.612 0 0 0-4.79 36.34c0 77.04 62.46 139.5 139.5 139.5s139.5-62.46 139.5-139.5c0-50.15-26.47-94.12-66.2-118.7l56.27-249.82c76.31-0.86 137.92-62.98 137.92-139.5z m-884.5 809.42c-37.19 0-67.42-30.25-67.42-67.42 0-37.19 30.23-67.42 67.42-67.42 37.17 0 67.42 30.23 67.42 67.42 0 37.17-30.25 67.42-67.42 67.42z m128.27-512.67c-37.19 0-67.42-30.25-67.42-67.42 0-37.19 30.23-67.42 67.42-67.42 37.17 0 67.42 30.23 67.42 67.42 0 37.17-30.25 67.42-67.42 67.42z m489 278c-37.19 0-67.42-30.25-67.42-67.42 0-37.19 30.23-67.42 67.42-67.42 37.17 0 67.42 30.23 67.42 67.42 0 37.17-30.25 67.42-67.42 67.42z m128-642.84c37.17 0 67.42 30.23 67.42 67.42 0 37.17-30.25 67.42-67.42 67.42-37.19 0-67.42-30.25-67.42-67.42 0-37.19 30.23-67.42 67.42-67.42z" />
            </svg>
          </div>
        </div>
      </div>
    </div>
  );
};