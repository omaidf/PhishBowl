import nmap

ip = "191.6.198.91"
nm = NmapProcess(ip, options="-p 1-1000")
rc = nm.run()

nm = nmap.PortScanner()
nm.scan(ip,'22-9000')
print(nm.csv())