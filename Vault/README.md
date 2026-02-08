# Mini-Vault

I've created python code to allow for file transfering between two different computers using a TCP connection. 
There are two distinct programs, the client and the server. The server runs on a Linux VM within my machine. It will 
split large files in to 1024 byte chunks to send the data of larger files to prevent overloading the ram of the server. 
The most important part of the code is the handshake logic inside the send_file and receive_file functions. First, the 
intent to share data is agreed upon between the client and server, then the file size is sent for the server's sake, 
then the data stream is sent. The logic is reversed for the recieve_file functions. 

## Instructions for Build and Use

[Software Demo](https://youtu.be/HMMbOiqzsKo)

Steps to build and/or run the software:

1. Download and install the VM VirtualBox software for the host.
2. Create a new Ubuntu Linux VM and allocate at least 4GB of RAM to it.
3. Configure the VM's network adapter to use the "NAT" setting in the Network menu.
4. Open the Port Forwarding settings in VirtualBox and match the host to guest.
5. Boot the VM using an Ubuntu ISO file and complete the full os installation.
6. Transfer the server.py script to the Ubuntu VM.
7. Edit the server.py script on the VM to listen on HOST = '0.0.0.0' so it accepts external connections.
8. Open the Ubuntu Terminal and run "server.py" to start the server.
9. Open and run the client.py script in your IDE on the Windows host machine to initiate the connection.

Instructions for using the software:

1. Place any files to upload into the client_data folder on your Windows machine.
2. Run the client.py script to establish a connection with the port.
3. Type the command SAVE <filename> to upload a file from your local folder to the server.
4. Type the command READ <filename> to request and download a file from the server to your machine.
5. Type the command EXIT to close the network connection and end the program.

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python 3
* Python Libraries socket and os
* Oracle CM VirtualBox
* Ubuntu 
* IDE of your choice

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Google Gemini](gemini.google.com)
* [Python Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)
* [Real Python: Sockets](https://realpython.com/python-sockets/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] I want to learn how to encrypt the data being sent and received.
* [ ] I could create a secure login handshake that requires a username and password.
* [ ] I could add a visual progress indicator for large file transfers.