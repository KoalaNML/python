import requests
import sys 

try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    thisdict = response.json()
    rate = thisdict["bpi"]["USD"]["rate_float"]
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    amount = rate * float(sys.argv[1])
    print(f"${amount:,.4f}") 

except requests.RequestException:
    sys.exit("RequestException")

except ValueError:
    sys.exit("Command-line argument is not a number")