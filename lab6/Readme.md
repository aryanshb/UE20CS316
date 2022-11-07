# CNS Lab 6 Remote DNS Cache Poisoning Attack Lab

### PES1UG20CS084

### Aryansh Bhargavan

---



#### Verification of the DNS setup

>**Running**
>
>`dig ns.attacker32.com`
>
>![Screenshot from 2022-10-16 18-35-07](D:\SEM5\CNS_windows\Labs\lab6\Aryansh\task0\Screenshot from 2022-10-16 18-35-07.png)
>
>`dig www.example.com`
>
>![Screenshot from 2022-10-16 18-35-50](D:\SEM5\CNS_windows\Labs\lab6\Aryansh\task0\Screenshot from 2022-10-16 18-35-50.png)
>
>`dig @ns.attacker32.com www.example.com`
>
>![Screenshot from 2022-10-16 18-36-09](D:\SEM5\CNS_windows\Labs\lab6\Aryansh\task0\Screenshot from 2022-10-16 18-36-09.png)
>
>---



#### Task 1: Construct DNS request

>**Running** `python3 generate_dns_query.py`
>
>![Screenshot from 2022-10-16 18-38-10](D:\SEM5\CNS_windows\Labs\lab6\Aryansh\task1\Screenshot from 2022-10-16 18-38-10.png)
>
>**Corresponding Wireshark Capture of the query**
>
>![Screenshot from 2022-10-16 18-38-32](D:\SEM5\CNS_windows\Labs\lab6\Aryansh\task1\Screenshot from 2022-10-16 18-38-32.png)
>
>---



#### Task 2: Spoof DNS Replies

>**Getting ip addresses of NS of `example.com`**
>
>> **Running**
>>
>> `dig NS example.com`
>>
>> ![Screenshot from 2022-10-16 18-46-37](D:\SEM5\CNS_windows\Labs\lab6\Aryansh\task2\Screenshot from 2022-10-16 18-46-37.png)
>>
>> <mark>**We see nameservers `a.iana-servers.net.` and `b.iana-servers.net.` and we use the former**</mark>
>>
>> **`dig +short a a.iana-servers.net.`**
>>
>> ![Screenshot from 2022-10-16 18-46-58](D:\SEM5\CNS_windows\Labs\lab6\Aryansh\task2\Screenshot from 2022-10-16 18-46-58.png)
>
>**Running `python3 generate_dns_reply.py`**
>
>![Screenshot from 2022-10-16 18-48-49](D:\SEM5\CNS_windows\Labs\lab6\Aryansh\task2\Screenshot from 2022-10-16 18-48-49.png)
>
>**Corresponding Wireshark Capture**
>
>![Screenshot from 2022-10-16 18-49-55](D:\SEM5\CNS_windows\Labs\lab6\Aryansh\task2\Screenshot from 2022-10-16 18-49-55.png)
>
>---



#### Task 3: Launch the Kaminsky Attack

>**Compiling `attack.c` on host system and copying it to attacker volume**
>
>![Screenshot from 2022-10-16 18-52-48](D:\SEM5\CNS_windows\Labs\lab6\Aryansh\task3\Screenshot from 2022-10-16 18-52-48.png)
>
>**Running kaminsky attack on attacker terminal**
>
>`./kaminsky`
>
>![Screenshot from 2022-10-16 19-02-21](D:\SEM5\CNS_windows\Labs\lab6\Aryansh\task3\Screenshot from 2022-10-16 19-02-21.png)
>
>**After waiting for 30s, I checked the DNS cache**
>
>![Screenshot from 2022-10-16 19-03-02](D:\SEM5\CNS_windows\Labs\lab6\Aryansh\task3\Screenshot from 2022-10-16 19-03-02.png)
>
>**As we can see, `ns.attacker32.com` has been added to local DNS cache**
>
>---



#### Task 4: Result Verification

>**Running**
>
>`dig www.example.com`
>
>![Screenshot from 2022-10-16 19-04-10](D:\SEM5\CNS_windows\Labs\lab6\Aryansh\task4\Screenshot from 2022-10-16 19-04-10.png)
>
>`dig @ns.attacker32.com www.example.com`
>
>![Screenshot from 2022-10-16 19-04-36](D:\SEM5\CNS_windows\Labs\lab6\Aryansh\task4\Screenshot from 2022-10-16 19-04-36.png)
>
>**We get same output on both, showing that the cache has been poisoned**
>
>---