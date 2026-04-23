import requests

headers= {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZXhwIjoxNzc3MDQ1Nzg1fQ.2BDl_bELAU7sB8Rp3mRQT72alII1Mn6S5Dzy1jjw3rg"
}

requisicao= requests.get("http://127.0.0.1:8000/auth/refresh",headers=headers)
print(requisicao)
print(requisicao.json())