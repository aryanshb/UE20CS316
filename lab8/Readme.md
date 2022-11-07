# CNS Lab 8 Firewall Evasion

### PES1UG20CS084

### Aryansh Bhargavan

---

#### Task 0: Get Familiar with the Lab Setup

>![image-20221106102900129](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106102900129.png)
>
>![image-20221106102919985](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106102919985.png)
>
>---



#### Task 1 : Static Port Forwarding

>**`# ssh -L 0.0.0.0:8000:192.168.20.99:23 root@192.168.20.99`**
>
>![image-20221106103921637](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106103921637.png)
>
>**`# telnet 10.8.0.99 8000`**
>
>![image-20221106104040900](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106104040900.png)
>
>![image-20221106104052044](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106104052044.png)
>
>**Questions**
>
>1) How many TCP connections are involved in this entire process. You should run wireshark or tcpdump to capture the network traffic, and then point out all the involved TCP connections from the captured traffic
>
>   >![image-20221106104316340](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106104316340.png)
>   >
>   >![image-20221106104353802](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106104353802.png)
>   >
>   >![image-20221106104411684](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106104411684.png)
>   >
>   >There are 3 TCP connections, between A and router, A1 - A, and A2 - A.
>
>2) Why can this tunnel successfully help users evade the firewall rule specified in the lab setup?
>
>   >This can be explained with this diagram
>   >
>   >![image-20221106105420367](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106105420367.png)
>   >
>   >Since client does not have access to a service, they use an ssh tunnel for data forwarding. As recorded traffic is only between client and the proxy, it evades the firewall. (This is valid only if SSH is also not restricted by firewall as in the case of PESU)
>
>---



#### Task 2: Dynamic Port Forwarding

>**Task 2.1: Setting Up Dynamic Port Forwarding**
>
>>**`# ssh -4 -D 0.0.0.0:8000 root@10.8.0.99 -f -N`**
>>
>>![image-20221106105807346](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106105807346.png)
>>
>>**`# curl -x socks5h://0.0.0.0:8000 http://www.example.com`**
>>
>>![image-20221106105904604](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106105904604.png)
>>
>>**Trying to access blocked website from B1 and B2**
>>
>>![image-20221106110221793](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106110221793.png)
>>
>>![image-20221106110247016](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106110247016.png)
>>
>>**Questions**
>>
>>1) Which computer establishes the actual connection with the intended web server?
>>
>>   >Host B acts as the proxy between client (host b1, b2) and hence establishes the actual connection with intended web server
>>
>>2) How does this computer know which server it should connect to?
>>
>>   >Once the client asks the proxy to connect to a web server, this is first received by the proxy, and then forwarded on behalf of the proxy. The proxy receives request data and acts like a regular computer accessing said request data. The response data is then forwarded to the client, thus accessing data restricted by the firewall.
>>
>>---
>
>**Task 2.2: Testing the Tunnel Using Browser**
>
>>![image-20221106111349599](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106111349599.png)
>>
>>**Questions**
>>
>>1) Run tcpdump on the router-firewall, and point out the traffic involved in the entire port forwarding process
>>
>>   ![image-20221106111825091](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106111825091.png)
>>
>>   **tcpdump on router**
>>
>>   ![image-20221106112003451](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106112003451.png)
>>
>>   We can see that the ssh tunnel is being used
>>
>>2) Break the SSH tunnel, and then try to browse a website. Describe your observation
>>
>>   ![image-20221106112109402](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106112109402.png)
>>
>>   ![image-20221106112127073](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106112127073.png)
>>
>>   Since ssh tunnel has been broken, we are no longer able to access `linkedin.com`
>>
>>---
>
>**Task 2.3: Writing a SOCKS Client Using Python**
>
>>**`# ssh -4 -D 0.0.0.0:8000 root@10.8.0.99 -f -N`**
>>
>>![image-20221106112807554](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106112807554.png)
>>
>>**`# python3 B-Socks-Client.py`**
>>![image-20221106113035683](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106113035683.png)
>>
>>**On Host b1 and b2**
>>
>>![image-20221106113248036](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221106113248036.png)
>>
>>**We can access said website since it is being forwarded using the ssh proxy**
>>
>>---
>
>---

#### Task 3: Comparing SOCKS5 Proxy and VPN

>**SOCKS5**
>
>>- Proxy server
>>- Faster that VPN (Lack of encryption)
>>- Uses SSH
>>- Easy and cheap to set up
>
>**VPN**
>
>>- Also proxy server
>>- Encrypted traffic, so more secure
>>- Also makes it slower (due to encryption)
>>- Makes tunnel preventing IP address to access data that you are accessing
>>- Speed depends on VPN server location also
>>- Costly to set up
>
>---

