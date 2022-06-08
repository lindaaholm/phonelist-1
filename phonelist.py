#import sqlite3
#conn = sqlite3.connect("phone.db")

import psycopg2
conn = psycopg2.connect(
    host='localhost',
    database='phone',
    user='phone',
    password='abc123'
    )

print('''Hello and welcome to the phone list, available commands:
  add    - add a phone number
  delete - delete a contact
  list   - list all phone numbers
  quit   - quit the program
  save   - saves new contacts
  help   - list all commands
''')

def read_phonelist(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_phone(C, name, phone, address):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}', '{address}');")
    cur.close()
def delete_phone(C, id):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE id = '{id}';")
    cur.close()
def save_phonelist(C):
    cur = C.cursor()
    try:
        cur.execute("COMMIT;")
    except:
        print("No changes!")
    cur.close()

    

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").upper()
    if cmd == "LIST":
        print(read_phonelist(conn))
    elif cmd == "ADD":
        name = input("  Name: ")
        phone = input("  Phone: ")
        address = input("  Address: ")
        add_phone(conn, name, phone, address)
    elif cmd == "DELETE":
        id = input("  id: ")
        delete_phone(conn, id)
    elif cmd == "QUIT":
        save_phonelist(conn)
        exit()
    elif cmd == 'REMOVE':
        print('Command not recognized')
    elif cmd == 'SAVE':
        save_phonelist(conn)
    elif cmd == 'HELP':
       print('''Hello and welcome to the phone list, available commands:
  add    - add a phone number
  delete - delete a contact
  list   - list all phone numbers
  quit   - quit the program
  save   - saves new contacts
  help   - list all commands
''')
        


