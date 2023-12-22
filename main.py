import numpy as np 
import requests
import time
import xlwings as xw

def main():
    #x = np.linspace(0,2*np.pi,100)
    #y = np.sin(x)
    # Specifying a sheet
    ws = xw.Book("row_data2022-279-1-1.xlsx").sheets['in']
    # Selecting data from range
    y = ws.range("D9:D1200").value

    i = 0
    while i < len(y):
        url  = f"http://127.0.0.1:5000/post/{y[i]}" 

        response = requests.get(url)

        if response.status_code != 200:
            print("Error", response.status_code)
        time.sleep(0.1)
        i = (i+1)

if __name__ == "__main__":
    main()