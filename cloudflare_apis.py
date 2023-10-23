import requests, json, os, sys, dotenv

dotenv.load_dotenv()

class CloudflareAPIs():
    def __init__(self):
        self.base_url = 'https://api.cloudflare.com/client/v4/'
        self.headers = {
            'X-Auth-Email': os.getenv('CLOUDFLARE_EMAIL'),
            'X-Auth-Key': os.getenv('CLOUDFLARE_KEY'),
            'Content-Type': 'application/json'
        }
            
    #Basic DNS management API
    def list_zones(self):
        # 此步驟可以取得所有的 zone_identifier 或是你可以從 Cloudflare Domain Overview 頁面取得 
        url = self.base_url + 'zones'
        response = requests.get(url, headers=self.headers)
        return response.json()


    def list_dns_records(self, zone_name):
        zone_identifier = self.get_zones_identifier(zone_name)
        url = self.base_url + f'zones/{zone_identifier}/dns_records'
        response = requests.get(url, headers=self.headers)
        data = {}
        for a_record in response.json()['result']:
            data[a_record['name']] = a_record['content']
        return data

    def get_zones_identifier(self, zone_name):
        list_zones = self.list_zones()
        for zone in list_zones['result']:
            if zone['name'] == zone_name:
                return zone['id']
        return None
    
    
    # Custom hostname API
    # 列出一個域名下的所有自訂域名
    def list_custom_hostnames(self, zone_name):
        zone_identifier = self.get_zones_identifier(zone_name)
        url = self.base_url + f'zones/{zone_identifier}/custom_hostnames'
        response = requests.get(url, headers=self.headers)
        return response.json()

    # WAF API
    def get_firewall_rules(self, zone_name):
        zone_identifier = self.get_zones_identifier(zone_name)
        url = self.base_url + f'zones/{zone_identifier}/firewall/rules'
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def create_firewall_rules(self, zone_name, data):
        zone_identifier = self.get_zones_identifier(zone_name)
        url = self.base_url + f'zones/{zone_identifier}/firewall/rules'
        response = requests.post(url, headers=self.headers, data=json.dumps(data))
        return response.json()
    

