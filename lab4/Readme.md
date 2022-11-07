# CNS Lab 4 TCP Attack  

### PES1UG20CS084

### Aryansh Bhargavan

---

### Task 1: SYN Flooding Attack

>#### Task 1.1 (Python)
>
>>- Viewing size of victim's queue and turning off SYN cookie
>>
>>![image-20220925142944007](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925142944007.png)
>>
>>- Current queue usage
>>
>>  ![image-20220925143033496](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925143033496.png)
>>
>>**Task 1.1 Launching Attack using Python**
>>
>>>**Executing `synflood.py`**
>>>
>>>> while attack is running, checking connection queue:
>>>>
>>>> ![image-20220925144444230](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925144444230.png)
>>>
>>>Now that the attack is done, we try to telnet into the machine from `User-1`
>>>
>>>![image-20220925145045616](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925145045616.png)
>>>
>>>- We are able to telnet into the machine since `10.9.0.6` is already cached, so reserved slots are used.
>>>- Lowering our `syn backlog`
>>>
>>>![image-20220925145241556](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925145241556.png)
>>>
>>>- Removing effect of reserved slots mitigation method
>>>
>>>![image-20220925145615715](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925145615715.png)
>>
>>**Retrying the SYN Flood attack`**
>>
>>>![image-20220925151431570](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925151431570.png)
>>>
>>>Now the attack works
>
>#### Task 1.2  (C)
>
>>> Launching attack
>>>
>>> ![image-20220925151655804](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925151655804.png)
>>>
>>> Attempting telnet connection to victim
>>>
>>> ![image-20220925153200871](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925153200871.png)

---

### Task 2: TCP RST Attacks on Telnet Connections

>Telnetting into `Victim` from `User-1`
>
>![image-20220925171403992](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925171403992.png)
>
>Wireshark capture for the same
>
>![image-20220925171339845](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925171339845.png)
>
>Checking the last packet for source port and next seq number (highlighted)
>
>![image-20220925172231698](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925172231698.png)
>
>After filling the values and typing `ls` this is the wireshark capture
>
>![image-20220925173523110](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925173523110.png)
>
>A reset packet has been sent, terminating the TCP connection hence ending the telnet connection.
>
>![image-20220925173631302](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925173631302.png)
>
>---
>
>Running `reset_auto.py` performs similar results:
>
>Given below is the wireshark capture:
>
>![image-20220925172941544](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925172941544.png)

---

### Task 3: TCP Session Hijacking

>Using command `cat "secret123" > secret` I created a secret file on the victim machine remotely (from the telnet connection established between the victim and user).
>
>I then established a new connection and this is the wireshark capture for the same:
>
>![image-20220925175039935](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925175039935.png)
>
>- `source port: 39134 ` 
>
>- `destination port: 23` 
>- `next sequence number: 696167167` 
>- `acknowledgement number: 0`
>- `iface: br-57ad098dae2a`
>
>
>
>**Launching the attack**
>
>![image-20220925183711009](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925183711009.png)
>
>Contents of secret file:
>
>![image-20220925183758781](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925183758781.png)
>
>> notice contents at the bottom : `secret123` 

---

### Task 4: Creating Reverse Shell using TCP Session Hijacking

>First we telnet into `victim` from `User-1`
>
>![image-20220925213622308](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925213622308.png)
>
>Running the netcat server and executing `reverse.py`
>
>![image-20220925213714948](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925213714948.png)
>
>After typing `ls` a few times, reverse shell shows up on attacker machine
>
>![image-20220925214104589](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925214104589.png)
>
>Now we can view the secret file
>
>![image-20220925214357515](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220925214357515.png)
>
>

