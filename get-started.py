from pydantic import BaseModel

# Define UserProfile model
class UserProfile(BaseModel):
    name: str
    age: int = 18  # Default value
    email: str
    is_active: bool = True  # Default value

user = UserProfile(name="Tuyen ", age=18, email="tuyen@example.com")
print(user)

# Working with model attributes
print(user.name)
print(user.age)
print(user.email)


user2 = UserProfile(name="Tuyen ", email="tuyen@example.com")
print(user2)