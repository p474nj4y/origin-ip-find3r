import socket 
import pyfiglet

xdxd = pyfiglet.figlet_format("ORIGIN-IP\nFIND3r ", font = "slant")
print(xdxd) 
ydyd = pyfiglet.figlet_format("Coded w/ <3 By - @p474nj4y", font = "digital" )
print(ydyd)


def get_ip(domain):
    try:
        originip = socket.gethostbyname(domain)
        return originip
    except socket.gaierror as e :
        print("sorry but we can't found any ip address !!,{e}")

if __name__ == "__main__" :
    orgdomain = input("enter domain name please : ")
    getip = get_ip(orgdomain)
    print(f"ORIGIN IP FOUND FOR {orgdomain} is {getip}")
