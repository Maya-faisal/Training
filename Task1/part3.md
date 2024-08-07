# part3

* generate the private and public keys 
  > sudo ssh-keygen 

* copy the public key
  > sudo ssh-copy-id username@host_ip 

* restart ssh
  > systemctl retsart sshd

* in the etc/ssh/ssh_config turn off the password authentication
  
  ![image](https://github.com/user-attachments/assets/25bf3049-f16d-449f-a29f-b2d6f0f23f04)

* enter in the other vm using
  > ssh usename@host_ip



