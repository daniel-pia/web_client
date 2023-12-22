import numpy as np 
import requests
import time

def main():
    x = np.linspace(0,2*np.pi,100)
    y = np.sin(x)

    i = 0
    while True:
        url  = f"http://127.0.0.1:5000/post/{y[i]}"

        response = requests.get(url)

        if response.status_code != 200:
            print("Error", response.status_code)
        time.sleep(1)
        i = (i+1)%100

if __name__ == "__main__":
    main()