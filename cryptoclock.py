import tkinter
from PIL import ImageTk,Image
import sys
import datetime
import requests

# Class that displays the current time, Bitcoin price, and Ether price.
class Clock:
    
    # Function to initialize the clock.
    def __init__(self, parent):
        self.btc_img = ImageTk.PhotoImage(Image.open("btc_logo.png").resize((50,50)))
        self.eth_img = ImageTk.PhotoImage(Image.open("eth-diamond.png").resize((35,50)))
        self.clock_label = tkinter.Label(parent, text = datetime.datetime.now().strftime("%H:%M"), font = "Areal 65", foreground="white", background="black")
        self.clock_label.pack(fill=tkinter.X)
        self.label_btc = tkinter.Label(parent, image=self.btc_img, background="Black")
        self.label_btc.pack(side=tkinter.LEFT, padx=(10,0), pady=(0,10))
        self.btc_price_label = tkinter.Label(parent, text = 'NA', font = "Areal 16", foreground="white", background="black")
        self.btc_price_label.pack(side=tkinter.LEFT, pady=(0,10))
        self.label_eth = tkinter.Label(parent, image=self.eth_img, background="Black")
        self.eth_price_label = tkinter.Label(parent, text = 'NA', font = "Areal 16", foreground="white", background="black")
        self.eth_price_label.pack(side=tkinter.RIGHT, padx=(0,10), pady=(0,10))
        self.label_eth.pack(side=tkinter.RIGHT, padx=(50,10), pady=(0,10))
        # Try to get the current price of Bitcoin in USD from Coinbase.
        try:
            r = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy', timeout=(3,3))
            json_parse = r.json()
            self.btc_price_label.configure(text = '$' + json_parse["data"]["amount"], font = "Areal 16", foreground="white", background="black")
        except:
            print("Failed to get BTC price.")
        # Try to get the current price of Ether in USD from Coinbase.
        try:
            r = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/buy', timeout=(3,3))
            json_parse = r.json()
            self.eth_price_label.configure(text = '$' + json_parse["data"]["amount"], font = "Areal 16", foreground="white", background="black")
        except:
            print("Failed to get ETH price.")
        # Refresh the clock after 2 seconds.
        self.clock_label.after(2000, self.refresh_label)
    
    # Function to refresh the clock.
    def refresh_label(self):
        self.clock_label.configure(text = datetime.datetime.now().strftime("%H:%M"), font = "Areal 65", foreground="white", background="black")
        try:
            # Try to get the current price of Bitcoin in USD from Coinbase.
            r = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy', timeout=(3,3))
            json_parse = r.json()
            self.btc_price_label.configure(text = '$' + json_parse["data"]["amount"], font = "Areal 16", foreground="white", background="black")
        except:
            print("Failed to get BTC price.")
        # Try to get the current price of Ether in USD from Coinbase.
        try:
            r = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/buy', timeout=(3,3))
            json_parse = r.json()
            self.eth_price_label.configure(text = '$' + json_parse["data"]["amount"], font = "Areal 16", foreground="white", background="black")
        except:
            print("Failed to get ETH price.")
        self.clock_label.after(2000, self.refresh_label)

if __name__ == "__main__":
    window = tkinter.Tk()
    running_clock = Clock(window)
    window.title("Cryptoclock")
    window.configure(background="black")
    
    # Function to exit the program.
    def close(event):
        sys.exit()
    
    # Call exit funtion when the Escape key is pressed.
    window.bind('<Escape>', close)
    window.mainloop()
