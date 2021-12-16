# 1010-final-Poofycloud


## 1. Describe the problem(s) and the solution(s) you came up with in terms of how you chose to write your code

One of the biggest problems I faced in this project was being able to start the darn thing. It absolutely refused to first allow me to download the library via pip, telling me that I needed to update my pip version. I did, but then it was telling me I had to update it to the very same pip version I had it at. So then, after many github and stackoverflow searches, I eventually came down to an issue with my text editor not being at the proper configuration to install the library. I had to do a quick installation for a specific update for C++ code in my VS Code Editor, which allowed the pip web3 installation to finally work.

My second issue was when I would attempt to call upon the library to import the web3 package from it. One part of it was my own mistake where the import was a capitalization of the same name as the library (not very diverse in naming). My second would be when it would say that there was a ModuleNotFoundError, which was tricky since my library was already installed and I would type the code correctly, usually this would mean having to run the library in my command prompt to see if it is communicating properly or reinstall it to give a fresh response.

Something I could not resolve was to find something called an abi, which is essential for certain code to contact one another, but through the channels I was supposed to receive them from, they would not show it, and the tutorials seem to skip over how to find it, so I had no choice but to cut my token.py code short and continue onto bigger fish.

## 2. Tell us about your process in terms of strategizing, implementing, and testing your code. How was this the same or new compared with other homework assignments?

In terms of planning, I have been reading quite a lot about web3 programming and knew that there was a platform for testing out a smart contract without losing real cryptocurrency. I downloaded a software called Ganache which acts as a dummy blockchain and crypto for development purposes. This was very useful as I could manage each account and verify if the transaction was successful. For the majority of this project I relied on tutorials to carry the heavy lifting, especially if I didn't want to make a poor mistake as actually authorizing my digital wallet to be used. I even played with making a brand new wallet to see how it would read it.

This was all new to me in comparison to other homework assignments as this was something that could affect people if published for financial use. To strategize, I followed step-by-step tutorials that go in detail for the purpose of each line of code. Implementing it was straight forward as most of everything was already defined in the library itself. 

## 3. What questions or difficulties came up along the way and how you did you go about addressing those?

My questions correlate more within understanding how this basic form of a smart contract is used more contingently with dApps (or decentralized applications) and how professional smart contracts would compare to this one. I want to know how else this could be used.

Something that I wanted to do initially that I couldn't figure out was setting up a virtual environment, which was what every blog and tutorial was highly recommending, if not demanding when following along. What really are virtual environments and what are their uses if they are so important in cases like this?

## 4. What did you learn?

I feel like I learned a lot from this project in such short time, not only through the issues I faced, but in the learning in how to create a smart contract for Ethereum. I feel like I have a much stronger understanding on the relationship between cryptocurrency and the blockchain through how it is so easily transported in probably 20 lines of code or less. Something that I definitely see though is an extreme necessity for security, especially when private keys are being saved on these programs. Safety is a huge demand in the web3/ blockchain space, which is why you can apparently find quite a number of job postings for smart contract security developers! Through all my research in this space, I feel more curious to learn programming and see what can be done in the current, centralized space we thrive in.

Something that was notably interesting to learn was the different elements and terms that reside within this kind of coding. I never knew there was a term for the smallest measurements of cryptocurrency size called Wei, which is the standard unit of measurement that used for most blockchain programming, followed by measurements like gwei, a somewhat bigger unit than wei. the wei is practically like a penny to a $100 dollar bill for cryptocurrency. Throughout this project I got to learn about two other resources need for connecting to a blockchain. You have to create an account with services like Alchemy or Infura in order to contact a node that is connected to the blockchain network.

And if I may add, I am super surprised how open the world is with its resources for learning just about every kind of technology out there, especially when wanting to learn how to code, I found an overwhelming amount of resources all across the web!!!
