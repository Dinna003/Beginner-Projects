import requests

url = 'http://host1.open.uom.lk:8080/'

updated_entity = {
        "productName":"Araliya Basmathi Rice",
        "description":"White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
        "category":"Rice",
        "brand":"Araliya",
        "expiredDate":"2023.05.04",
        "manufacturedDate":"2022.02.20",
        "batchNumber":324567,
        "unitPrice":1020,
        "quantity":200,
        "createdDate":"2022.02.24"
}

response = requests.put(f"{url}/api/products", json=updated_entity)

print(response.json())