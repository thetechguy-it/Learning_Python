import requests
import json
import apic_credentials

def login():
    url = f"{apic_credentials.url}/api/aaaLogin.json"

    payload = {
        "aaaUser": {
            "attributes": {
            "name": f"{apic_credentials.username}",
            "pwd": f"{apic_credentials.password}"
            }
        }
    }

    headers = {
      "Content-Type" : f"{apic_credentials.content_type}"
    }

    requests.packages.urllib3.disable_warnings()
    response = requests.post(url,data=json.dumps(payload), headers=headers, verify=False)
    print(f"Status Code is: {response.status_code}")
    response_json = response.json()
    return response_json
   
def get_token():
    response_json = login()
    token = response_json['imdata'][0]['aaaLogin']['attributes']['token']
    return token

def get_version():
    response_json = login()
    version = response_json['imdata'][0]['aaaLogin']['attributes']['version']
    return version

#def get_tenant():
    url = f"{apic_credentials.url}/api/class/fvTenant.json"
    requests.packages.urllib3.disable_warnings()
    response = requests.post(url,data=json.dumps(login.payload), headers=login.headers, verify=False)
    response_json = response.json()
    tenants = url['imdata'][0]['fvTenant']['attributes']['name']
    return tenants
   
def main():
   token = get_token()
   print(f'The token is: {token}\n')
   version = get_version()
   print(f'The token is: {version}\n')
   #tenants = get_tenant()
   #print(f'The tenant name is: {tenants}')


if __name__ == "__main__":
    main()