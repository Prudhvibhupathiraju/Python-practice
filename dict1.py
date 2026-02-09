dict1 ={
  "username": "alpha_user92",
  "session_id": "7f3k9x21",
  "login_attempts": 4,
  "is_active": True,
  "account_balance": 1587.45,
  "country": "India",
  "preferred_language": "English",
  "subscription_plan": "Premium",
  "last_login": "2026-02-09T10:14:22",
  "device_type": "Laptop"
}

# print(dict1["is_active"])
# dict1["State"] = "Andhra Pradesh"
# print(dict1["State"])
# print(dict1)
# dict1["login_attempts"] = 5
# print(dict1["login_attempts"])

# for key in dict1:
#     print(f"{key} : {dict1[key]}")

# data = {
#     "name": "Ravi",
#     "age": 25,
#     "skills": ["Linux", "Python", "AWS"],
#     "projects": ["Server Automation", "Monitoring Setup"]
# }

# print(data["skills"][1])

# students = [
#     ["Ravi", 25, ["Linux", "Python"]],
#     ["Kiran", 27, ["AWS", "Docker"]]
# ]

# print(students[0][2][0])

travel_log = {
    "India": {
        "cities_visited": ["Hyderabad", "Bangalore", "Chennai"],
        "total_visits": 5
    },
    "USA": {
        "cities_visited": ["New York", "Chicago", "San Francisco"],
        "total_visits": 2
    },
    "UAE": {
        "cities_visited": ["Dubai", "Abu Dhabi"],
        "total_visits": 3
    }
}

print(travel_log["USA"]["cities_visited"][2])