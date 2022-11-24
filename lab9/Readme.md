# CNS Lab 9 VPN Tunneling Lab

### PES1UG20CS084

### Aryansh Bhargavan

---

#### Task 1: Network Setup

>**`ping server-router`**
>
>![image-20221114214513828](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114214513828.png)
>
>**`ping 192.168.60.5`**
>
>![image-20221114214656964](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114214656964.png)
>
>**`ping 192.168.60.5`**
>
>![image-20221114214856654](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114214856654.png)
>
>**`ping server-router`**
>
>![image-20221114215004546](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114215004546.png)
>
>Corresponding tcpdump
>
>![image-20221114215031399](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114215031399.png)
>
>---

#### Task 2: Create and Configure TUN Interface

>**Task 2.a: Name of the Interface**
>
>>![image-20221114215430837](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114215430837.png)
>>
>>Kill tunnel process: ![image-20221114215519045](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114215519045.png)
>>
>>Changing iface name
>>
>>![image-20221114215900951](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114215900951.png)
>>
>>Running `tun.py`
>>
>>![image-20221114215959912](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114215959912.png)
>>
>>Iface name is **`CS0840`**
>
>**Task 2.b: Set up the TUN Interface**
>
>>![image-20221114220215126](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114220215126.png)
>
>**Task 2.c: Read from the TUN Interface**
>
>>![image-20221114220500363](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114220500363.png)
>>
>>![image-20221114220536898](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114220536898.png)
>
>**Task 2.d: Write to the TUN Interface**
>
>> ![image-20221114224808928](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114224808928.png)
>>
>> ![image-20221114224843745](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114224843745.png)
>
>---

#### Task 3: Send the IP Packet to VPN Server Through a Tunnel

>![image-20221114225243306](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114225243306.png)
>
>![image-20221114225546074](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114225546074.png)
>
>![image-20221114225701663](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114225701663.png)
>
>![image-20221114225709777](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114225709777.png)
>
>![image-20221114225739711](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114225739711.png)
>
>![image-20221114225809851](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114225809851.png)
>
>![image-20221114225830467](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114225830467.png)
>
>---

#### Task 4: Set Up the VPN Server

>![image-20221114230328181](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114230328181.png)
>
>![image-20221114230336905](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114230336905.png)
>
>![image-20221114230349118](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114230349118.png)
>
>---

#### Task 5: Handling Traffic in Both Directions

>![image-20221114231906103](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114231906103.png)
>
>![image-20221114231916312](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114231916312.png)
>
>![image-20221114231932050](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114231932050.png)
>
>**telnet**
>
>![image-20221114232153885](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114232153885.png)
>
>![image-20221114232211611](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114232211611.png)
>
>![image-20221114232240976](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114232240976.png)
>
>---

#### Task 6: Tunnel-Breaking Experiment

>![image-20221114232501646](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114232501646.png)
>
>**after reconnecting to vpn**
>
>![image-20221114232618059](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221114232618059.png)
>
>---



