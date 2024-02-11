def binary_calc(brekip):
    
    bintable = [128,64,32,16,8,4,2,1]
    ipbin = [0,0,0,0,0,0,0,0]
    finipbin=[]
    value=0
    
    for i in brekip:
        value =i
        for j in range(len(bintable)):
            if value >= bintable[j]:
                value = value-bintable[j]
                ipbin[j]=1
            else:
                ipbin[j]=0
            
            finipbin.append(ipbin[j])
        
        finipbin.append(".")

    return finipbin
                
    
def ipclass(ip,brekip,binary):
    if brekip[0] >= 1 and brekip[0] < 127:
       print(f"IP {ip} Is A Class A Ip Address\nIP binary : {binary}")

    elif brekip[0] >= 128 and brekip[0] <= 191:
        print(f"IP {ip} Is A Class B Ip Address\nIP binary : {binary}")

    elif brekip[0] >= 192 and brekip[0] <= 223:
        print(f"IP {ip} Is A Class C Ip Address\nIP binary : {binary}")

    elif brekip[0] >= 224 and brekip[0] <= 239:
        print(f"IP {ip} Is A Class D Ip Address\nIP binary : {binary}")

    elif brekip[0] >= 240 and brekip[0] <= 254:
        print(f"IP {ip} Is A Class E Ip Address\nIP binary : {binary}")

    else:
        print(f"ip {ip} Is an Invalid Ip Address")
    
ip=input("Enter Ip Address : ")
brekip=ip.split(".")
brekip = [int(i) for i in brekip]

binaryip=binary_calc(brekip)
binary = ''.join(str(x) for x in binaryip)

clas=ipclass(ip,brekip,binary)

