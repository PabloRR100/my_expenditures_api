
# Create Categories
curl -X POST "http://localhost:8000/categories/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"id\":0,\"name\":\"Salary\"}"
curl -X POST "http://localhost:8000/categories/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"id\":1,\"name\":\"Extra Income\"}"
curl -X POST "http://localhost:8000/categories/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"id\":2,\"name\":\"Home\"}"
curl -X POST "http://localhost:8000/categories/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"id\":3,\"name\":\"Groceries\"}"
