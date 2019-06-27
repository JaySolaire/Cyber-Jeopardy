"# Cyber-Jeopardy" 

This project is designed to increase student involvement in the field of cyber security through the completion of multiple cyber security games. The project consists of a cmdline-interface Jeopardy-style Capture The Flag (CTF) game, coded in C++, and a folder of external files. The game contains multiple puzzles of varying cyber security topics, which the user can complete for points. The user can choose any of the puzzles at any time, and can switch between them at will. By completing each puzzle, the user will be introduced to a new facet of cyber security, which should pique their interest in the field. 

Each puzzle question is assigned a point value based on its level of difficulty, ranging from 100 points to 500 points. The topics that they can choose from are Wireshark, Terminal, Encoding, Scripting, and Misc. Wireshark topics begin with questions on Wireshark filters, and range up to determining the number of UDP packets on the attached pcap. Terminal 100 begins as simple as listing the contents of the current directory, and moves up to changing file permissions at 500 points. The Encoding topic covers different methods of encoding data, including encrypting in base64, hashing, and compressing. The Scripting category tests knowledge of basic scripting with the help of the attached python files. The Misc category includes questions that do not fit in any of the other categories; for example, how to begin Metasploitable in Kali Linux.

Cyber Jeopardy Game Version 1
- Trashed because it was trash
- No, honestly. It was coded in C and the char[] compare required me to set specific array sizes for user answers, which opened up the program to buffer overflow attacks. The Version 1 file is actually just a proof of concept for a C string compare.

Cyber Jeopardy Game Version 2 Updates (aka 1.2 or Cyber_Jeopardy.zip)
- Designed to be OS- nonspecific: functions Windows/UNIX/Linux systems
- Completely independent, no internet required

Cyber Jeopardy Game Version 3 Updates (aka 1.3 or Cyber_Jeopardy2.zip)
- Implemented data collection through the use of a UDP socket. Internet is necessary for this functionality, but not for program functionality. The game can be played with full functionality without internet.
- Non-intrusive; it will attempt to send a UDP datagram for correct and incorrect answers if possible, but if not connected to the internet, it won't bug the user with errors.
- Now OS Specific- Only works on UNIX/Linux Systems

