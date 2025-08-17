## 🚀 Installation
  Step 1: Use the following command in a terminal: ```git clone https://github.com/KanayaPatel/Valuation-Project.git```
  
  Step 2: Use the following command: ```python3.11 venv venv``` to create a python virtual environment (this will take a minute). Then, activate it using ```venv/Scripts/activate```. Both these commands happen in the terminal as well. 

  Step 3: Enter the project folder using ```cd '.\Finance Project\'```. Then, do ```pip install -r "requirements.txt"```, this may take a minute. 

  Step 4: Open the ```app.py``` folder and run it. From the terminal, press CTRL + Left click on the second or third part that says "Running On". This will take you to the actual webpage. 
  
## 🛠 Usage
At this point in time, you shold see a webpage that should look like the following: 

<img width="2559" height="1266" alt="image" src="https://github.com/user-attachments/assets/3c2ed03a-ba94-493c-b503-87fcb633b34a" />

Click on the information button to learn about this project. The webpage should look like this: 

<img width="2559" height="1269" alt="image" src="https://github.com/user-attachments/assets/ba71bf06-7275-476b-8d75-3591f461e421" />

If you wish to go back to the previous page at any time, there is always a button in the top left corner that will take you back to the previous page. After reading, click the "Get Started" button at the bottom of the screen. It will take you to a page to where the magic happens: 

<img width="2558" height="1266" alt="image" src="https://github.com/user-attachments/assets/1b2e1f22-b065-480c-b79c-050805933d56" />

Please read through the instructions and the notes at the bottom. Below will be some examples in the form of screenshots on how to use this predictor. 

## 📊 Examples

For the first field (the Time Period), you get the selection from the following: Day, Month, Year, Year to Date, and Max, as shown below. These selections specify how much data to use in the predictions. That is, if Day is chosen, the predictor will use valuation data within the last day. The more data you use, the better the predictions but the longer the processing time. 


<img width="296" height="482" alt="image" src="https://github.com/user-attachments/assets/aee13e74-f179-4649-be3a-f583e1f8306a" />

For the second field (the Time Amount), you get to input how many Days, Months, or Years worth of data you wish to use for the prediction. Note that you must choose a number that is probable. That is, using the number 1,000,000 will not work. Try using smaller numbers such as 1 or 3 for best results. 

<img width="412" height="137" alt="image" src="https://github.com/user-attachments/assets/726a0f44-bb1f-49c9-aa75-28a55b3b4a1d" />

For the third field (the Data Type), you get the selection from the following: Low, High, Open, Close, Volume. These denote specific valuations. The volume, however, does NOT denote the price of the stock in question, but rather how many stocks are out at the time. 

<img width="194" height="472" alt="image" src="https://github.com/user-attachments/assets/0427e247-ddf1-406a-a397-5565d79a8b0c" />

For the fourth field (the Ticker Symbol), you get to choose a company to predict stock from! Choose any company you wish. However, be careful of using new and upcoming companies, as their data may not exist or the Time Amount chosen may be incorrect. Ensure that there is enough data to make good predictions. NOTE: For the image below, "AAPL" is the Ticker Symbol for Apple.

<img width="408" height="141" alt="image" src="https://github.com/user-attachments/assets/0d972b8c-48aa-4b76-844a-c24c1951b01c" />


## 🤝 Contributing
## 📜 License
## 🚧 Future Improvements
- [ ] Add the ability to save estimates for future use. 
- [ ] Implement login (Username and Password)
- [ ] Implement the ability to use non-Ticker Symbol using companies (such as Samsung)
- [ ] Include a spot to display the error in the estimates. 
