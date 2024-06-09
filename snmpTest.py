import SnmpOperations
import ipaddress
import threading
import time
from tkinter import *
from tkinter import ttk



oidsname = []
oidsname.append("uptime")
oidsname.append("contact")
oidsname.append("name")
oidsname.append("location")
oidsname.append("systemdescription")
oidsname.append("processnumber")
oidsname.append("ramsize")

uptime = "1.3.6.1.2.1.1.3.0"
contact =  "1.3.6.1.2.1.1.4.0"
name = "1.3.6.1.2.1.1.5.0"
location = "1.3.6.1.2.1.1.6.0"
systemDescription = "1.3.6.1.2.1.1.1.0"
processnumber = "1.3.6.1.2.1.25.1.6.0"
ramsize = "1.3.6.1.2.1.25.2.2.0"

oidarray = []
oidarray.append(uptime)
oidarray.append(contact)
oidarray.append(name)
oidarray.append(location)
oidarray.append(systemDescription)
oidarray.append(processnumber)
oidarray.append(ramsize)


root = None

ipEntry = None
comEntry = None
oidEntry = None

ipLabel = None
comLabel = None
oidLabel = None

getbutton = None

getsingleOIDbutton = None
scanbutton = None
getbutton = None

#chỉ sử dụng except không tốt vì nó bắt tất cả lỗi và  không biết chính xác lỗi ở đâu

def normget(ip, comunitystring):

    if comunitystring == "":
        comunitystring = "public"
    try:
        resultarray = SnmpOperations.get(ip, oidarray, comunitystring)
        j = 0;
        for i in oidarray:
            print(oidsname[j] + ": " + str(resultarray[i]))
            j = j+1
    except:
        print("Không thể lấy thông tin từ địa chỉ này.")


def sendget():
    ipformEntry = ipEntry.get()
    comfromEntry = comEntry.get()

    ipLabel.grid_forget()
    ipEntry.grid_forget()
    comLabel.grid_forget()
    comEntry.grid_forget()
    getbutton.grid_forget()

    print("")
    print("Thông tin về IP cụ thể:")
    print("")
    choosecommand()
    normget(ipformEntry, comfromEntry)

def scannet(network):
    
    try:
        if '/' not in network:
            raise Exception

        print("Quét mạng " + network + " Có thể mất một chút thời gian...")

        i = 0
        threads = []
        for ip in ipaddress.IPv4Network(network):
            threads.append(threading.Thread(target=getThread, args=(str(ip),)))
            threads[i].start()
            i = i+1

        print("Chờ phản hồi từ các host...")
        for k in range(0, 254):
            threads[k].join()
        print("Quét mạng hoàn tất!")


    except:
        print("Có lỗi xảy ra. Vui lòng kiểm tra lại.")


def sendscan():
    ipformEntry = ipEntry.get()

    ipLabel.grid_forget()
    ipEntry.grid_forget()
    getbutton.grid_forget()

    print("")
    print("Quét mạng:")
    print("")
    choosecommand()
    scannet(ipformEntry)


def oidGet(ip, oid, comunitystring):
    if comunitystring == "":
        comunitystring = "public"

    varBinds = resultarrayspecific = SnmpOperations.getsingleoid(ip, oid, comunitystring)
    for varBind in varBinds:
        print(ip + ": " + varBind[1])

def sendOID():
    ipformEntry = ipEntry.get()
    comfromEntry = comEntry.get()
    oidfromEntry = oidEntry.get()

    ipLabel.grid_forget()
    ipEntry.grid_forget()
    comLabel.grid_forget()
    comEntry.grid_forget()
    oidLabel.grid_forget()
    oidEntry.grid_forget()
    getbutton.grid_forget()

    print("")
    print("OID cụ thể:")
    choosecommand()
    oidGet(ipformEntry, oidfromEntry, comfromEntry)

def getThread(iptoscan):
    try:
        SnmpOperations.getsingleoid(iptoscan, oidarray[2], "public", True)
    except:
        #print("Không thể lấy thông tin từ địa chỉ này.")
        pass


def removecommandbuttons():
    getbutton.grid_forget()
    scanbutton.grid_forget()
    getsingleOIDbutton.grid_forget()

def guiGetIn():

    removecommandbuttons()

    global ipLabel
    ipLabel = Label(root, text="IP-Address", bg="white", fg="black")
    ipLabel.grid()
    global ipEntry
    ipEntry = Entry(root)
    ipEntry.grid()

    global comLabel
    comLabel = Label(root, text="community (để trống = public)", bg="white", fg="black")
    comLabel.grid()
    global comEntry
    comEntry = Entry(root)
    comEntry.grid()

    global getbutton
    getbutton = Button(root, text="send", bg="black", fg="white", command=sendget)
    getbutton.grid()


def guiScanIn():

    removecommandbuttons()

    global ipLabel
    ipLabel = Label(root, text="Network (z.B. 192.168.0.0/24)", bg="white", fg="black")
    ipLabel.grid()
    global ipEntry
    ipEntry = Entry(root)
    ipEntry.grid()

    global getbutton
    getbutton = Button(root, text="send", bg="black", fg="white", command=sendscan)
    getbutton.grid()


def guiGetoidIn():

    removecommandbuttons()

    global ipLabel
    ipLabel = Label(root, text="IP-Address", bg="white", fg="black")
    ipLabel.grid()
    global ipEntry
    ipEntry = Entry(root)
    ipEntry.grid()

    global comLabel
    comLabel = Label(root, text="community (để trống = public)", bg="white", fg="black")
    comLabel.grid()
    global comEntry
    comEntry = Entry(root)
    comEntry.grid()

    global oidLabel
    oidLabel = Label(root, text="OID", bg="white", fg="black")
    oidLabel.grid()
    oidLabel.grid()
    global oidEntry
    oidEntry = Entry(root)
    oidEntry.grid()

    global getbutton
    getbutton = Button(root, text="send", bg="black", fg="white", command=sendOID)
    getbutton.grid()


def choosecommand():

    global getbutton
    getbutton = Button(root, text="Get", height="5", width="30", bg="black", fg="white", command=guiGetIn)
    getbutton.grid()

    global scanbutton
    scanbutton = Button(root, text="Scan Network", height="5", width="30", bg="black", fg="white", command=guiScanIn)
    scanbutton.grid()

    global getsingleOIDbutton
    getsingleOIDbutton = Button(root, text="get single OID", height="5", width="30", bg="black", fg="white", command=guiGetoidIn)
    getsingleOIDbutton.grid()


def guiInit():
    
    global root
    root = Tk()
    root.geometry("220x258")
    root.title("SNMP GUI")


    """
    useGuibutton = Button(root, text="sử dụng GUI, bg="black", fg="white", command=choosecommand)
    useGuibutton.grid()
    closeGui = Button(root, text="Đóng gui và sử dụng dòng lệnh", bg="black", fg="white", command=root.destroy)
    closeGui.grid()
    """

    choosecommand()

    root.mainloop()


if __name__ == "__main__":

    choose = input("Bạn muốn sử dụng Gui hay sử dụng dòng lệnh? (GUI = yes/dòng lệnh = no)")

    while True:
        if choose == "yes":
            print("Bây giờ bạn có thể tiếp tục trong cửa sổ GUI. Tuy nhiên, bạn vẫn có thể tìm thấy kết quả đầu ra trong dòng lệnh")
            guiInit()
            quit()
        elif choose == "no":
            while True:
                command = input("Bạn muốn làm gì? Lấy thông tin từ một IP cụ thể (get), quét toàn bộ mạng (scan), một OID cụ thể của một IP (getOID), kết thúc chương trình (quit): ")
                if command == "get" :
                    ip = input("Nhập địa chỉ IP: ")
                    comunitystring = input("Nhập community string (để trống = public): ")
                    normget(ip, comunitystring)
                elif command == "scan":
                    network = input("Nhập địa chỉ mạng với mặt nạ mạng con (ví dụ: 192.168.0.0/24): ")
                    scannet(network)
                elif command == "getOID":
                    ip = input("Nhập địa chỉ IP: ")
                    oid = input("Nhập OID bạn muốn đọc: ")
                    comunitystring = input("Nhập community string (để trống = public): ")
                    oidGet(ip, oid, comunitystring)
                elif command == "quit":
                    quit()
                else:
                    print("Lệnh không hợp lệ. Vui lòng thử lại.")

