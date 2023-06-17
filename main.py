import os.path
import os, time

key = 121 #kunci hexa
####kunci = random.randint(0,1000) #random integer
def toHex(d):
    return f"{d:0{2}X}".upper() #return to hexa

def decode(text):
    decoded = []
    for line in text.split('\n'):
        if "=" in line:
            i = line.index("=")
            decoded_text = ""
            for enc in [line[i+1:][j:j+2] for j in range(0,len(line[i+1:]),2)]:
                try:
                    decoded_text += chr(int(enc,16)^key)
                except ValueError:
                    decoded_text += '.'
            decoded.append(line[:i] + "=" + decoded_text)
        else:
            decoded.append(line)
    return "\n".join(decoded)
def encrypt(text):
    encoded = []
    for line in text.split('\n'):
        try:
            i = line.index("=")
            encoded.append(line[:i] + "="+ "".join(toHex(ord(dec)^key) for dec in line[i + 1:]))
        except ValueError:
            encoded.append(line)
    return "\n".join(encoded)

"""def writeFile(text, selfpath):
    file = f"{kunci}_{selfpath}.ini"
    if not os.path.exists(file):
        with open(file, "w") as fn:
            fn.write(f"{text}")
            fn.close()
            print(f"{file} Created!")
    else:
        with open(file, "w") as fn:
            fn.write(f"{text}")
            fn.close()
            print(f"{file} Created!")"""

def main():
    print("\n[S] SkyUniverse PUBG Encryptor and Decryptor Tools")
    print(">> Menu's are availables\n[1] Encrypt\n[2] Decrypt")
    menu = input("Choose menu you want to use => ")
    if menu in ["1",1,"Encrypt"]:
        enc = input("Masukan teks yang ingin di Enkripsi: ")
        if enc.startswith("+CVars="):
            print(encrypt(enc))
            repeatOnMenu()
        else:
            print("Please starswith `+CVars=`!")
    elif menu in ["2", 2, "Decrypt"]:
        dec = input("Masukan teks yang ingin di Enkripsi: ")
        if dec.startswith("+CVars="):
            print(decode(dec))
            repeatOnMenu()
        else:
            print("Please starswith `+CVars=`!")
    else:
        print("[System Warning] Select valid menu!")
        repeatOnMenu()

def repeatOnMenu():
    repeat = input("[S] You want use this program? (YES/NO)? ")
    if repeat == "YES":
        os.system("clear")
        main()
    else:
        os.system("exit")

if __name__ == "__main__":
    main()
