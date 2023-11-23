# 
# 512352
# [0-255].[0-255].[0-255].[0-255]
# 5.1.23.52
# 5.1.235.2
# 51.2.3.52
# 512352

def is_valid_octet(oct):
    if not (int(oct)<=255 and int(oct)>=0):
         return False
    elif oct[0] == "0" and oct != "0":
         return False
    else:
        return True

def generate_ips(st):
    for i in range(1,len(st)):
        for j in range(i+1,len(st)):
            for k in range(j+1,len(st)):
                if is_valid_octet(st[0:i]) and is_valid_octet(st[i:j]) and is_valid_octet(st[j:k]) and is_valid_octet(st[k:]):
                    print(f"{st[0:i]}.{st[i:j]}.{st[j:k]}.{st[k:]}")

generate_ips("1212121")