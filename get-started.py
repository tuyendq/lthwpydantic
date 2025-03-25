from pydantic import BaseModel

# Define UserProfile model
class UserProfile(BaseModel):
    name: str
    age: int
    email: str

user = UserProfile(name="Tuyen ", age=18, email="tuyen@example.com")
print(user)