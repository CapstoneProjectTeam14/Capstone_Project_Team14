# Blockchain based authorization app using react and solidity

### Step 1: Clone the repo
```
git clone https://github.com/Hrishikesh015/auth-app.git
```
### Step 2: Move to the app directory
```
cd auth-app
```
### Step 3: Install necessary dependencies
```
npm i
```
### Step 4: Move to src folder to build the smart contract
```
cd src
truffle build
```
### Step 5: Migrate the contract to get the contract address
```
truffle migrate --reset
```
### Step 6: Run the react app
```
npm start
```
Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

## Steps to setup Metamask and Ganache
1. Install the [Metamask](https://metamask.io/download/) extension
2. Install [Ganache](https://trufflesuite.com/ganache/)
3. Open Ganache, Click on Quickstart, and 10 addresses with each 100 ETH coins will be visible.
4. Open Metamask, Go to settings -> Add networks -> Add network manually and enter the below feilds
    1. Network name: Ganache
    2. New RPC Url: ```http://127.0.0.1:7545```
    3. Chain ID: ```1337```
    4. Click on Save
5. Adding accounts to Metamask from ganache
    1. Open Ganache, click on the key icon of any address copy the private key.
    2. Open Metamask -> select ganache network ->  Click on profile (right top) -> Click on import account -> paste the copied private key.
    3. Now you are able to see 100 ETH coins in your account.
