import os
if os.getenv("DB_PASSWORD") != None:
    print("Password retrieved successfully")

else: 
    print("Password not found")