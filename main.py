from bank import Bank
from center import Center
from client import Client

center = Center()
client = Client(1, 1337, center)
bank = Bank(10, center)

client.request_certificate()

is_verified = bank.verify_client(client)
print(is_verified)