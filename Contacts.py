contacts = []

def get_input(msg): return input(msg).strip()

def add(): 
    contacts.append({
        "store": get_input("Store Name: "),
        "phone": get_input("Phone: "),
        "email": get_input("Email: "),
        "addr": get_input("Address: ")
    })
    print("✓ Added")

def view():
    if not contacts: print("No contacts."); return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['store']} - {c['phone']}")

def search():
    q = get_input("Search by name/phone: ").lower()
    for c in contacts:
        if q in c['store'].lower() or q in c['phone']:
            print(f"{c['store']}, {c['phone']}, {c['email']}, {c['addr']}")
            return
    print("Not found.")

def update():
    name = get_input("Store name to update: ").lower()
    for c in contacts:
        if c['store'].lower() == name:
            c['phone'] = get_input(f"New Phone ({c['phone']}): ") or c['phone']
            c['email'] = get_input(f"New Email ({c['email']}): ") or c['email']
            c['addr'] = get_input(f"New Address ({c['addr']}): ") or c['addr']
            print("✓ Updated")
            return
    print("Not found.")

def delete():
    name = get_input("Store name to delete: ").lower()
    for c in contacts:
        if c['store'].lower() == name:
            contacts.remove(c)
            print("✓ Deleted")
            return
    print("Not found.")

def main():
    menu = {
        "1": add, "2": view, "3": search,
        "4": update, "5": delete, "6": exit
    }
    while True:
        print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
        opt = get_input("Choice: ")
        menu.get(opt, lambda: print("Invalid"))()

main()
