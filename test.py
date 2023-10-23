from cloudflare_apis import CloudflareAPIs
from aws_apis import AWSAPIs

cloudflare = CloudflareAPIs()
aws = AWSAPIs()

# Get specific zone_identifier with zone name

# result = cloudflare.get_firewall_rules('motivetag.com')
# print(result)

# Create firewall rules
# data = {}
# result = cloudflare.create_firewall_rules('motivetag.com', data)
# print(result)



result2 = aws.get_hosted_zones()
print(result2)