import os
if os.getenv("DB_PASSWORD") != None:            #Create ENV var first
    print("Password retrieved successfully")

else: 
    print("Password not found")