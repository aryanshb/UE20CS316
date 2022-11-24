# CNS Lab 10 Heartbleed Attack Lab

### PES1UG20CS084

### Aryansh Bhargavan

---

#### Step 1: Configure the DNS server for Attacker machine

>![image-20221117184653596](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221117184653596.png)
>
>---

#### Step 2: Lab Tasks

>**`$ sudo chmod 777 attack.py`**
>
>![image-20221117184911545](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221117184911545.png)
>
>**`$ python attack.py www.heartbleedlabelgg.com`**
>
>![image-20221117185106938](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221117185106938.png)
>
>**Step 2(a): Explore Damage On the Victim Server:**
>
>>![image-20221117185436224](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221117185436224.png)
>
>**Step 2(b): On Attacker machine:**
>
>>Password:
>>
>>![image-20221117185654397](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221117185654397.png)
>>
>>Contents of message:
>>
>>![image-20221117185959456](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221117185959456.png)
>>
>>(subject = hi buddy, body=buddy hi)
>>
>>---
>
>---

#### Step 3/4: Investigate the fundamental cause of the Heartbleed attack

>**`$ python /home/seed/attack.py www.heartbleedlabelgg.com --length 40`**
>
>... on trial and error, i found length 22 gives no extra info
>
>![image-20221117190702443](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20221117190702443.png)
>
>---

#### Step 5: Countermeasure and bug fix

>**`$ sudo apt-get update `**
>**`$ sudo apt-get upgrade`**
>
>---

