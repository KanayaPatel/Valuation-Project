## 🚀 Installation
  Step 1: Use the following command in a terminal: ```git clone https://github.com/KanayaPatel/Valuation-Project.git```
  
  Step 2: Use the following command: ```python3.11 venv venv``` to create a python virtual environment (this will take a minute). Then, activate it using ```venv/Scripts/activate```. Both these commands happen in the terminal as well. 

  Step 3: Enter the project folder using ```cd '.\Finance Project\'```. Then, do ```pip install -r "requirements.txt"```, this may take a minute. 

  Step 4: Open the ```app.py``` folder and run it. From the terminal, press CTRL + Left click on the second or third part that says "Running On". This will take you to the actual webpage. 
  
## 🛠 Usage
At this point in time, you shold see a webpage that should look like the following: 

<img width="2559" height="1266" alt="image" src="https://github.com/user-attachments/assets/3c2ed03a-ba94-493c-b503-87fcb633b34a" />

Click on the information button to learn about this project. The webpage should look like this: 

<img width="2558" height="1271" alt="image" src="https://github.com/user-attachments/assets/5c7a5750-754c-44bd-899f-fa0c29c36b4e" />

If you wish to go back to the previous page at any time, there is always a button in the top left corner that will take you back to the previous page. After reading, click the "Get Started" button at the bottom of the screen. It will take you to a page to where the magic happens: 

<img width="2558" height="1272" alt="image" src="https://github.com/user-attachments/assets/34881689-235b-4134-a1da-5f13117aa0fb" />

Please read through the instructions and the notes at the bottom. Below will be some examples in the form of screenshots on how to use this predictor. 

## 📊 Examples

For the first field (the Time Period), you get the selection from the following: Day, Month, Year, Year to Date, and Max, as shown below. These selections specify how much data to use in the predictions. That is, if Day is chosen, the predictor will use valuation data within the last day. The more data you use, the better the predictions but the longer the processing time. 


<p align='center'><img width="296" height="482" alt="image" src="https://github.com/user-attachments/assets/aee13e74-f179-4649-be3a-f583e1f8306a" /></p>

For the second field (the Time Amount), you get to input how many Days, Months, or Years worth of data you wish to use for the prediction. Note that you must choose a number that is probable. That is, using the number 1,000,000 will not work. Try using smaller numbers such as 1 or 3 for best results. 

<p align='center'><img width="412" height="137" alt="image" src="https://github.com/user-attachments/assets/726a0f44-bb1f-49c9-aa75-28a55b3b4a1d" /></p>

For the third field (the Data Type), you get the selection from the following: Low, High, Open, Close, Volume. These denote specific valuations. The volume, however, does NOT denote the price of the stock in question, but rather how many stocks are out at the time. 

<p align='center'><img width="194" height="472" alt="image" src="https://github.com/user-attachments/assets/0427e247-ddf1-406a-a397-5565d79a8b0c" /></p>

For the fourth field (the Ticker Symbol), you get to choose a company to predict stock from! Choose any company you wish. However, be careful of using new and upcoming companies, as their data may not exist or the Time Amount chosen may be incorrect. Ensure that there is enough data to make good predictions. NOTE: For the image below, "AAPL" is the Ticker Symbol for Apple.

<p align='center'><img width="408" height="141" alt="image" src="https://github.com/user-attachments/assets/0d972b8c-48aa-4b76-844a-c24c1951b01c" /></p>

Here is an image of all fields being filled as well as there being an output! Note that the current values are stored temporarily in their respective tables. In the case of you choosing 'volume' as the data type, ignore the label (USD) and interpret the value given as a number of stocks. 

<img width="2556" height="1271" alt="image" src="https://github.com/user-attachments/assets/7eb914e3-a2c0-4ffc-8157-269a14d954ed" />

This is what it looks like after pressing "Next Step": 

<img width="2544" height="1269" alt="image" src="https://github.com/user-attachments/assets/a3e5c7e7-ffef-4fa9-80d6-2af095f57a55" />

## 🤝 Contributing
You can contribute in several ways:
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 📝 Improving documentation
- 🔧 Submitting code via Pull Requests
  
## 📜 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## 🚧 Future Improvements
- [ ] Add the ability to save estimates for future use. 
- [ ] Implement login (Username and Password)
- [ ] Implement the ability to use non-Ticker Symbol using companies (such as Samsung)
- [ ] Include a spot to display the error in the estimates. 
