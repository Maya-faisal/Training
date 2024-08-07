# part2

## 2.1
* create a new user "user1"
  > useradd user1 

* set "user1" UID to 601
  > usermod -u 601 user1

* set "user1" password to "redhat"
  > sudo passwd user1

* change "user1" to a non-interactive shell
  > usermod user1 -s /sbin/nologin

## 2.2
* create a new group "TrainingGroup"
  > groupadd TrainingGroup

* add "user1" to the new group
  > usermod -aG TrainingGroup user1

## 2.3
* create new two users "user2" "user3"
  > useradd user{2,3}

* change the passowrd to "redhat" for the new users
  > sudo passwd user{2,3}

* create new group "AdminGroup"
  > groupadd AdminGroup

* add "user2" "user3" to the new group
  > usermod -aG AdminGroup user2 user3

* give user3 root permissions
  > usermod -aG wheel user3 <br />
  
**Members of the wheel group exercise the administrative privileges of root with less potential for damaging the system**
