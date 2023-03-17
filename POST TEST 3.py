import os
import pwinput
os.system("cls")

admin = {"username": ["admin"],
        "pw": ["admin"]}

#class node
class node(object):
    def __init__(self, data = None, next_node = None):
        self.nama = data["nama"]
        self.hp = data["hp"]
        self.email = data["email"]
        self.next_node = next_node

#class linked list
class linkedlist(object):
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def add(self, data):
        new_node = node(data)
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
    
    def show(self):
        os.system("cls")
        print("Node => Next Node")
        print("="*40)
        print("")
        current_node = self.head
        if (self.head is None):
            print("\tEMPTY")
        else:
            while current_node is not None:
                print("\tNama: {}\n\tNo.HP: {}\n\tEmail: {}".format(current_node.nama, current_node.hp, current_node.email))
                if (current_node.next_node is not None):
                    print("=>")
                current_node = current_node.next_node
    
    def delete(self):
        os.system("cls")
        nama = input("Nama yang ingin dihapus: ")
        print("")
        if self.head == None:
            print("\tEMPTY")
            return
        current_node = self.head
        if self.head.nama == nama:
            self.head = self.head.next_node
            print("{} TERHAPUS".format(nama))
            return
        if self.tail.nama == nama:
            while current_node.next_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = self.tail.next_node
            self.tail = current_node
            print("{} TERHAPUS".format(nama))
            return
        if current_node.next_node is not None and current_node.next_node.nama == nama:
            current_node.next_node = current_node.next_node.next_node
            print("{} TERHAPUS".format(nama))
            return
        while current_node is not None and current_node.nama != nama or current_node.next_node is not None and current_node.next_node.nama != nama:
            print("{} NOT FOUND".format(nama))
            return

    def menu(self):
        while True:
            os.system("cls")
            print("="*40)
            print("|      LIST DATA PELANGGAN MEMBER      |")
            print("="*40)
            print("1. Tampilkan Member")
            print("2. Tambah Member")
            print("3. Hapus Member")
            print("4. Keluar Program")
            print("="*40)
            pilih = input("\tPilih Opsi: ")
            if (pilih == "1"):
                self.show()
                print("")
                print("="*40)
                x = input("'Enter'")
            elif (pilih == "2"):
                os.system("cls")
                nama = str(input("Masukkan Nama: "))
                if all(i.isspace() for i in nama):
                    print("\n\tINPUTAN DATA KOSONG")
                    print("")
                    print("="*40)
                    x = input("'Enter'")
                    l.menu()
                else:
                    hp = input("Masukkan No.HP: ")
                    email = str(input("Masukkan Email: "))
                    self.add({
                    "nama": nama,
                    "hp": hp,
                    "email": email
                    })
            elif (pilih == "3"):
                self.delete()
                print("")
                print("="*40)
                x = input("'Enter'")
            elif (pilih == "4"):
                exit()

while True:
    ua = input("Input Username: ")
    pwa = pwinput.pwinput(prompt = "Input Password: ")
    try:
        log1 = admin.get("username").index(ua)
        if ua == admin.get("username")[log1] and pwa == admin.get("pw")[log1]:
            l = linkedlist()
            l.menu()
        else:
            print("\tPASSWORD SALAH")
            print("")
    except ValueError:
        print("\tUSERNAME SALAH")
        print("")