
# Create Categories
curl -X POST "http://127.0.0.1:8000/v1/categories/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"id\":0,\"name\":\"Salary\"}"
curl -X POST "http://127.0.0.1:8000/v1/categories/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"id\":1,\"name\":\"Extra Income\"}"
curl -X POST "http://127.0.0.1:8000/v1/categories/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"id\":2,\"name\":\"Home\"}"
curl -X POST "http://127.0.0.1:8000/v1/categories/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"id\":3,\"name\":\"Groceries\"}"