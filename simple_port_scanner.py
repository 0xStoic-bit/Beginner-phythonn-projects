import socket

def  portScanner(targetHost,targetPort):
    for port in targetPort:
        try:
            soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            soc.settimeout(0.5)  # bağlantı zaman aşımı
            result = soc.connect_ex((targetHost , port))

            if result == 0:
                print(f'Port {port} Açık')

            else:
                print(f'Port {port} Kapalı')


                soc.close()

        except KeyboardInterrupt:
            print('Tarama işlemi iptal edildi ')
            break
        except socket.error:
            print('Bağlantı sağlanamadı')
            break

targetHost = "141.136.23.22"
targetPort  = [80,8080,23,22,21,3389,95,93,995,444,443]

portScanner(targetHost,targetPort)
