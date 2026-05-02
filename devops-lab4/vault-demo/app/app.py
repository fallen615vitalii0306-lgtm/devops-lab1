import os

print("Reading secret safely...")
secret = os.getenv("MY_SECRET", "not found")
print("Secret masked: ********")
