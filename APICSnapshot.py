#python 3

"""
1. logs onto the APIC and generates a cookie

2. saves a snapshot referencing the change number
"""

import requests
import json
import credentials
requests.packages.urllib3.disable_warnings()
 
def get_cookies():
    url = f'{credentials.host}/api/aaaLogin.json'
    auth = {'aaaUser': {'attributes': {'name': credentials.username, 'pwd': credentials.password}}}
    authenticate = requests.post(url, data=json.dumps(auth), verify=False)
    return authenticate.cookies
    
def create_snapshot(cookies):
    url = f'{credentials.host}/api/node/mo/uni/fabric/configexp-defaultOneTime.json'
    snapShotRef = input('\nPlease type your change ref and user ID:' )
    payload = {
            'configExportP': {
                        'attributes': {
                                    'dn': 'uni/fabric/configexp-defaultOneTime',
                                    'name': 'defaultOneTime',
                                    'snapshot': 'true',
                                    'adminSt': 'triggered',
                                    'rn': 'configexp-defaultOneTime',
                                    'status': 'created,modified'
                        }
            }
}
    payload['configExportP']['attributes']['descr'] = snapShotRef    
    result = requests.post(url, data=json.dumps(payload), verify=False, cookies=cookies)
    #text = json.loads(result.text)
    code = result.status_code
    if code == 200:
        print(f'\nReturn 200, {snapShotRef} added.')
    else:
        print(f'\nReturn {code}, task failed.')

if __name__ == '__main__':
    cookies = get_cookies()
    create_snapshot(cookies)
