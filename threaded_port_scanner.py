import threading
import queue
import socket
import time

printlock=threading.Lock()
q=queue.Queue()
start=time.time()
server=input("enter ip or domain name - ")
openports=0
openlist=[]

def pscan(port):
	try:
		new_soc=socket.create_connection((server,port),0.1)
		#new_sock.close()
		return True
	except:
		return False
def threader():
        for c in range(500):
                worker=q.get()
                work(worker)
                q.task_done()

def work(v):
	if pscan(v):
		global openports,openlist
		with printlock:
			print("port ",v,"is open")
			openports+=1
			openlist.append(v)
	else:
		with printlock:
			print("port ",v,"is closed")

print("port scanner started")

for worker in range(1000):
        q.put(worker)
for x in range(10):
        t=threading.Thread(target=threader)
        t.start()
q.join()
print("total time taken = ",time.time()-start)
print("Total ports open= ",openports,"\nOpen ports -",openlist)
writetofile=server," has ",openlist," ports open \n"
with open('open ports','a') as ff:
	ff.write(str(writetofile))
print("saved to file 'open ports' ",writetofile)

