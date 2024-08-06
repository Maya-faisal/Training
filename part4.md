# part4

* copy /etc/fstab to /var/tmp
  > cp /etc/fstab  /var/tmp

* apply ACL to allow user1 to read and write
  > setfacl -m u:user1:rw /var/tmp/fstab

* apply ACL to prevent user2 from reading, writing and executing
  > setacfl -m u:user2:- /var/tmp/fstab

**use ACLs for customized permissions**

![image](https://github.com/user-attachments/assets/42845451-2fc3-4374-b603-1768b0ad0e72)
