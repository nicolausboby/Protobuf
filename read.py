import AddressBook_pb2 as ab
import sys

# Iterates though all people in the AddressBook and prints info about them.
def ListPeople(address_book):
    for person in address_book.people:
        print("Person ID:", person.id)
        print("  Name:", person.name)
        try:
            print("  E-mail address:", person.email)
        except ValueError:
            print(" no email provided")

        for phone_number in person.phones:
            if phone_number.type == ab.Person.MOBILE:
                print("  Mobile phone #: ", phone_number.number)
            elif phone_number.type == ab.Person.HOME:
                print("  Home phone #: ", phone_number.number)
            elif phone_number.type == ab.Person.WORK:
                print("  Work phone #: ", phone_number.number)

#   Main procedure:  Reads the entire address book from a file and prints all
#   the information inside.

if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
    sys.exit(-1)

address_book = ab.AddressBook()

# Read the existing address book.
f = open(sys.argv[1], "rb")
address_book.ParseFromString(f.read())
f.close()

print("Address Book ", sys.argv[1])
ListPeople(address_book)
