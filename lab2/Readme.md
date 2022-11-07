# Sniffing and Spoofing using PCAP Library 

## CNS Lab2

### Aryansh Bhargavan

### PES1UG20CS084

---



- #### Task 2.1 A : Understanding how a Sniffer Works

  - ` Question 1: Please use your own words to describe the sequence of the library calls that are essential for sniffer programs. This is meant to be a summary, not detailed explanation like the one in the tutorial`
    -  First we open a live pcap session with a specific interface name                                            `pcap_open_live()`
    - We then set traffic filter as ``icmp`  and convert to Berkley Packet Filter pseudo code        `pcap_compile()`
    - Then we begin capturing packets and execute the sniff                                                          `lol`
  - `Question 2: Why do you need the root privilege to run sniffex? Where does the program fail if executed without the root privilege?`
    - Since a Network Interface is being accessed, root privileges are required.
    - ![image-20220902140535271](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220902140535271.png)
  - `Question 3: Please turn on and turn off the promiscuous mode in your sniffer program. The value 1 of the third parameter in the pcap_open_live() function turns on the promiscuous mode (use 0 to turn it off). Can you demonstrate the difference when this mode is on and off? Change the code given in line 69 of Task2.1A.c file to the following : handle = pcap_open_live("br-****", BUFSIZ, 0, 1000, errbuf);`
    - Promiscous mode turned off:![image-20220830221815312](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220830221815312.png)
    - Promiscous mode turned on:
      - I get the same output with both promiscous mode turned on or off since no other activity is happening in my host machine (Since I am not using a VM, and running the docker containers on windows). If I used this on my VM, then host traffic would also be captured, along with the ping request I made on `seed-host` 
      - ![image-20220831195139693](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220831195139693.png)

---

- #### Task 2.1 B : Writing Filters

  - `Question: Capture the ICMP packets between two specific hosts`

    - ![image-20220902142654056](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220902142654056.png)

    - traffic between `10.9.0.5` and `10.9.0.6` has been captured using the filter 

      ​										`proto ICMP and (host 10.9.0.5 and 10.9.0.6)` 

  - `Question: Capture the TCP packets that have a destination port range from to sort 10 - 100 `

    - ![image-20220902143318797](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220902143318797.png)
    - traffic from ports `10-100`  have been captured using the filter `tcp dst portrange 10-100`

---

- #### Task 2.1 C : Sniffing Passwords

  - ![image-20220902143708312](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220902143708312.png)
    - TCP Packets have been sniffed on port 23 and 

---

- #### Task 2.2 : Spoofing

  - `Question: Spoof an ICMP Request`
    - ![image-20220902144446371](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220902144446371.png)
  - `Question :  Using the raw socket programming, do you have to calculate the checksum for the IP header?`
    - Yes, In this case, we are calculating checksum in the `in_chksum()` function 

---

- #### Task 2.3 : Sniffing and Spoofing

  - ![image-20220902145805667](C:\Users\Aryansh\AppData\Roaming\Typora\typora-user-images\image-20220902145805667.png)
    - A raw socket (IP) is set up 
    - We observe that a reply from 1.2.3.4 is being received even though it does not exist, this shows that the sniffing and consequent spoofing was successful. 

---