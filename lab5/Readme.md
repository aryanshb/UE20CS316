# CNS Lab 5 Local DNS Cache Poisoning Attack

### PES1UG20CS084

### Aryansh Bhargavan

---

​	

#### Verification of Lab Setup



>**Running** 
>
>`dig ns.attacker32.com`
>
>![Screenshot from 2022-10-14 17-54-35](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task0\Screenshot from 2022-10-14 17-54-35.png)
>
>`dig www.example.com`
>
>![Screenshot from 2022-10-14 17-55-27](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task0\Screenshot from 2022-10-14 17-55-27.png)
>
>`dig @ns.attacker32.com www.example.com`
>
>![Screenshot from 2022-10-14 17-56-01](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task0\Screenshot from 2022-10-14 17-56-01.png)

---

### Attack on DNS

#### Task 1: Directly Spoofing Response to User

>**Running**
>
>`rndc flush`
>
>![Screenshot from 2022-10-14 17-56-49](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task1\Screenshot from 2022-10-14 17-56-49.png)
>
>`dig www.example.com`
>
>![Screenshot from 2022-10-14 17-59-22](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task1\Screenshot from 2022-10-14 17-59-22.png)
>
>---
>
>**Running the task**
>
>`python3 task1.py` on `attacker` and `dig www.example.com` on victim
>
>![Screenshot from 2022-10-16 17-46-25](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task1\Screenshot from 2022-10-16 17-46-25.png)
>
>**Looking at dns cache**![Screenshot from 2022-10-16 17-48-01](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task1\Screenshot from 2022-10-16 17-48-01.png)
>
><mark>**Since the local DNS server is not involved in the spoofing process, the IP address of `example.com` is still accurate **</mark>
>
>---



#### Task 2: DNS Cache Poisoning Attack – Spoofing Answers

>**Running** `rndc flush`
>
>![Screenshot from 2022-10-14 17-56-49](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task1\Screenshot from 2022-10-14 17-56-49.png)
>
>**Running** `python3 task2.py` and `dig www.example.com`
>
>![Screenshot from 2022-10-16 17-51-31](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task2\Screenshot from 2022-10-16 17-51-31.png)
>
>**Spoofed Response**
>
>![Screenshot from 2022-10-16 17-53-08](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task2\Screenshot from 2022-10-16 17-53-08.png)
>
>**Looking at dns cache**
>
>![Screenshot from 2022-10-16 17-53-37](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task2\Screenshot from 2022-10-16 17-53-37.png)
>
><mark>**This time, DNS gets poisoned since the spoofed reply came to local DNS before the actual reply**</mark>
>
>---



#### Task 3: Spoofing NS Records

>**Running** `rndc flush`
>
>![Screenshot from 2022-10-14 17-56-49](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task1\Screenshot from 2022-10-14 17-56-49.png)
>
>**Running** `python3 task3.py` and `dig www.example.com`
>
>![Screenshot from 2022-10-16 18-17-48](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task3\Screenshot from 2022-10-16 18-17-48.png)
>
>**Spoofed Response**
>
>![Screenshot from 2022-10-16 18-18-43](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task3\Screenshot from 2022-10-16 18-18-43.png)
>
>**If we query some other subdomain under `example.com` domain, we get the spoofed IP address `1.2.3.6`**
>
>![Screenshot from 2022-10-16 18-20-37](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task3\Screenshot from 2022-10-16 18-20-37.png)
>
>**Checking dns cache**
>
>![Screenshot from 2022-10-16 18-20-52](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task3\Screenshot from 2022-10-16 18-20-52.png)
>
>---



#### Task 4: Spoofing NS Records for Another Domain

>**Running** `rndc flush`
>
>![Screenshot from 2022-10-14 17-56-49](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task1\Screenshot from 2022-10-14 17-56-49.png)
>
>**Running** `python3 task4.py` and `dig www.example.com`
>
>![Screenshot from 2022-10-16 18-02-36](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task4\Screenshot from 2022-10-16 18-02-36.png)
>
>**Spoofed response**
>
>![Screenshot from 2022-10-16 18-07-29](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task4\Screenshot from 2022-10-16 18-07-29.png)
>
><mark>**Response contains answer as spoofed IP address since the queries are forwarded to the attacker's nameserver**</mark>
>
>**Checking Cache**
>
> ![Screenshot from 2022-10-16 18-11-13](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task4\Screenshot from 2022-10-16 18-11-13.png)
>
><mark>**Since the spoofed NS record for `google.com` is considered out of zone, it is not cached by the DNS server**</mark>
>
>---



#### Task 5: Spoofing Records in the Additional Section

>**Running** `rndc flush`
>
>![Screenshot from 2022-10-14 17-56-49](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task1\Screenshot from 2022-10-14 17-56-49.png)
>
>**Running** `python3 task5.py` and `dig www.example.com`
>
>![Screenshot from 2022-10-16 18-22-10](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task5\Screenshot from 2022-10-16 18-22-10.png)
>
>**Spoofed Reply containing records in additional section**
>
>![Screenshot from 2022-10-16 18-22-25](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task5\Screenshot from 2022-10-16 18-22-25.png)
>
>**Checking DNS Cache**
>
>![Screenshot from 2022-10-16 18-24-06](D:\SEM5\CNS_windows\Labs\lab5\Aryansh\task5\Screenshot from 2022-10-16 18-24-06.png)
>
><mark>**All the content in the additional section is regarded out of zone and is hence discarded by local dns and not cached**</mark>
