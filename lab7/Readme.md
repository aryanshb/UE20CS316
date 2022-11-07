# CNS Lab 7 Firewall Exploration

### PES1UG20CS084

### Aryansh Bhargavan

---

#### Task 1: Implementing a Simple Firewall

>**Task 1.A: Implement a Simple Kernel Module**
>
>![image-20221029153352905](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029153352905.png)
>
>![image-20221029153409671](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029153409671.png)
>
>**Explanation**:
>
>---

>**Task 1.B: Implement a Simple Firewall Using Netfilter**
>
>1. > ---
>   >
>   > `dig @8.8.8.8 www.example.com`
>   >
>   > ![image-20221029155002566](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029155002566.png)
>   >
>   > **On another terminal**:![image-20221029155051159](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029155051159.png)
>   >
>   > ![image-20221029155346074](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029155346074.png)
>   >
>   > **Adding filters**
>   >
>   > ![image-20221029155544650](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029155544650.png)
>   >
>   > <mark>**We can see that packet is being dropped since filter was added against `google.com` hence dig does not show any response**</mark>
>   >
>   >
>   > ---
>
>2. >---
>   >
>   >**Uncommenting - `obj-m += seedPrint.o` and commenting the other two**
>   >
>   >![image-20221029160206529](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029160206529.png)
>   >
>   >**Making and running ` dig @8.8.8.8 www.example.com`**
>   >
>   >![image-20221029161157679](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029161157679.png)
>   >
>   ><mark>**This does not drop the packets, instead it just prints filtered packets**</mark>
>   >
>   >---
>
>3. >**Uncommenting - `obj-m += seedBlock.o` and commenting the other two**
>   >
>   >![image-20221029163046267](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029163046267.png)
>   >
>   >**Preforming Make and loading the Module**
>   >
>   >![image-20221029164845922](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029164845922.png)
>   >
>   >**Attempting to Ping and telnet into `10.9.0.1`**
>   >
>   >![image-20221029165038763](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029165038763.png)
>   >
>   ><mark>**Due to the addition of the filter, ping and telnet have been dropped**</mark>
>   >
>   >
>   >---
>
>---

#### Task 2: Experimenting with Stateless Firewall Rules

>**Task 2.A: Protecting the Router**
>
>>`iptables -t filter -L -n`
>>
>>![image-20221029170904411](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029170904411.png)
>>
>>`# iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT `
>>
>>`# iptables -A OUTPUT -p icmp --icmp-type echo-reply -j ACCEPT `
>>
>>`# iptables -P OUTPUT DROP `
>>
>>`# iptables -P INPUT DROP `
>>
>>`# iptables -t filter -L -n`
>>
>>![image-20221029171019671](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029171019671.png)
>>
>>`ping seed-router`
>>
>>![image-20221029171212665](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029171212665.png)
>>
>>`telnet seed-router`
>>
>>![image-20221029171507224](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029171507224.png)
>>
>><mark>**We are able to ping the router since ICMP request and reply have been allowed but since there is no rule for TCP (Used by telnet) it is filtered; i.e packets are being blocked**</mark>
>>
>>
>>---
>
>**Task 2.B: Protecting the Internal Network**
>
>>**Setting Rules**
>>
>>![image-20221029173025651](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029173025651.png)
>>
>>**Testing**
>>
>>1. Outside hosts cannot ping internal hosts.
>>
>>   ![image-20221029173940741](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029173940741.png)
>>
>>2. Outside hosts can ping the router
>>
>>   ![image-20221029174022440](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029174022440.png)
>>
>>3. Internal hosts can ping Outside Hosts
>>
>>   ![image-20221029174643551](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029174643551.png)
>>
>>4. All other packets between the internal and external networks should be blocked.
>>
>>   ![image-20221029174610265](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029174610265.png)
>>
>>---
>
>**Task 2.C: Protecting Internal Servers**
>
>>**Setting the rules**
>>
>>![image-20221029174927092](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029174927092.png)
>>
>>1. Checking Telnet
>>
>>   ![image-20221029175050714](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029175050714.png)
>>
>>2. Outside hosts cannot access other internal servers.
>>
>>   ![image-20221029175827324](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029175827324.png)
>>
>>3. Internal hosts can access all the internal servers.
>>
>>   ![image-20221029175910654](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029175910654.png)
>>
>>   ![image-20221029175938275](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029175938275.png)
>>
>>4. Internal hosts cannot access external servers
>>
>>   ![image-20221029180307198](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029180307198.png)
>>
>>---
>
>---

#### Task 3: Connection Tracking and Stateful Firewall

>**Task 3.A: Experiment with the Connection Tracking**
>
>>**ICMP**
>>
>>![image-20221029183815629](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029183815629.png)
>>
>>TTL decreases from 28 to 0.
>>
>>**UDP**
>>
>>![image-20221029184150585](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029184150585.png)
>>
>>![image-20221029184207855](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029184207855.png)
>>
>>TTL decreases from 28 until it is expired
>>
>>**TCP**
>>
>>![image-20221029185548087](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029185548087.png)
>>
>>![image-20221029185557102](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029185557102.png)
>>
>>TTL for TCP is 5 days, but decreases the same way
>>
>>
>>---
>
>**Task 3.B: Setting Up a Stateful Firewall**
>
>>**Setting Rules**
>>
>>![image-20221029190040196](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029190040196.png)
>>
>>**Checking rules**
>>
>>1. Checking telnet
>>
>>   ![image-20221029190132798](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029190132798.png)
>>
>>2. Outside hosts cannot access other internal servers.
>>
>>   ![image-20221029190738196](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029190738196.png)
>>
>>3. a
>>
>>   ![image-20221029190810757](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029190810757.png)
>>
>>   ![image-20221029191018843](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029191018843.png)
>>
>>4. Internal hosts can access all the internal servers
>>
>>   ![image-20221029191102456](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029191102456.png)
>>
>>---
>
>---

#### Task 4: Limiting Network Traffic

>**Setting Rules and pinging host `192.168.60.5`**
>
>![image-20221029192636423](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029192636423.png)
>
>Some packets not following the rule are dropped, hence we can see the 73.9% packet loss
>
>**Using and pinging host `192.168.60.5`**
>
>![image-20221029192314195](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029192314195.png)
>Packets not dropped since there is no rule telling the firewall to drop them even though the ping is a burst request
>
>---

#### Task 5: Load Balancing

>**Setting up the rules**
>
>![image-20221029192904845](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029192904845.png)
>
>**Round Robin**
>
>![image-20221029194108351](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029194108351.png)
>
>**Random Mode**
>
>Rules:![image-20221029194826915](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029194826915.png)
>
>![image-20221029195401838](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221029195401838.png)
>
>Packets are sent randomly



