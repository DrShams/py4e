import socket
import re
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #class socket.socket
mysock.connect( ('data.pr4e.org', 80) )
#Go and get REQUEST FROM wsl or CMD is not working
command_b = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()# class 'bytes' #UTF encoded data
#its the same if I send via commane line
    #telnet data.pr4e.org 80
        # GET http://data.pr4e.org/romeo.txt HTTP/1.0
        # \r\n\r\n means pres Enter Enter
mysock.send(command_b)
#1 OPEN FILE RETRIEVE THE DATA AND PUT THE DATA TO THE TXT.FILE
handle = open('theory_sockets_retrieve.txt','w')
while True:
    data_b = mysock.recv(512)
    # class 'bytes'
    # recieve characters if code Response 200 and only 512 characters actually receive 544 characters but where 32?
    # 535 characters without some trash we intercept
    # put that characters on the data which data
    # do again watch if previous data not already store and add remaining 31 characters
    if (len(data_b) < 1 ):    #if we don't receive any data
        break
    data_u = data_b.decode()
    print(data_u,end='') #after 512 characters add ''- nothing to conc data with each other
    handle.write(data_u) #1 PUT THE DATA TO THE TXT FILE
mysock.close()
handle.close #1 CLOSE THAT FILE cause it opened in w(Write) mode

#2 OPEN THAT FILE AGAIN IN r(Read) MODE AND FIND THE VALUES FOR THE KEYS WHICH WE KNOW
handle = open('theory_sockets_retrieve.txt','r')
#print(type(handle),type(data.decode()))
    #class '_io.TextIOWrapper' and 'str'
for line in handle:
    line = line.rstrip()
    #stuffs = re.findall('Last-Modified: (.*)',line)
    stuffs = re.findall('ETag: (.*)',line)
    #stuffs = re.findall('Content-Length: (.*)',line)
    #stuffs = re.findall('Cache-Control: (.*)',line)
    #stuffs = re.findall('Content-Type: (.*)',line)
    if len(stuffs) == 0 : continue      #if we have only 0 matches on the line skip it
    print('ETag',stuffs[0])
    #for stuff in range(len(stuffs)):    #range(len(stuffs)) return count of number between each line
    #    num = int(stuffs[stuff])
    #    numlist.append(num)
handle.close
