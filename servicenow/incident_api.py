import requests
from requests.auth import HTTPBasicAuth

instance='dev321797'

user='admin'

pwd='yxRt7MF/W^1z'

url=f'https://{instance}.service-now.com/api/now/table/incident'

payload = {
    "short_description":"CloudOps Application Failure",
    "description":"Application failure detected by monitoring system",
    "urgency":"1",
    "impact":"1"
}

response=requests.post(
    url,
    auth=HTTPBasicAuth(user,pwd),
    json=payload
)

print(response.status_code)
print(response.text)
