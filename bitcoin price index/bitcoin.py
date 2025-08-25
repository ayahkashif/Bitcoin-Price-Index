# specify as a command-line argument the number of Bitcoins, n
# If n cannot be converted to a float, the program should exit via sys.exit with an error message
# rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey
# Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator
# print(f"${amount:,.4f}")

import sys
import requests

def main():
    b_price = get_price()
    num = get_number()
    price = b_price * num
    print(f"${price:,.4f}")

def get_number():
    while True:
        if len(sys.argv) == 2:
            if sys.argv[1].isdigit():
                return float(sys.argv[1])
            else:
                if "." in sys.argv[1]:
                    return float(sys.argv[1])
                else:
                    sys.exit("Command-line argument is not a number")
        elif len(sys.argv) < 2:
            sys.exit("Missing command-line argument")

def get_price():
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=441316c191c15d673fdc31c432ecbc2953af87ef6c78f932e9e208bf3cca5254")
    o = response.json()
    result = o["data"]
    return float(result["priceUsd"])

if __name__ == "__main__":
    main()
