from faker import Faker

fake = Faker()

# name = fake.name()
# address = fake.address()
# text = fake.text()

# print(name)
# print(address)
# print(text)

names = []

for i in range(10):
    names.append(fake.name())

print(names)