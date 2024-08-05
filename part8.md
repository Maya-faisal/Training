# part8

## 8.1

* first, check the firewall status
  > systemctl status firewalld

* activate it if it was not activated using 
  > systemctl enable firewalld
  > systemctl start firewalld

* open port 80 and 443, using the firewall-cmd, and make the changes permanent using --parmanent 

  > firewall-cmd --permanent --add-port 80 <br />
  > firewall-cmd --permanent --add-port 443


* reload the firewall
  > firewall-cmd --reload


> [!NOTE]
> changes are made to the default zone, which is "public" by firewall-cmd --get-default-zone 


* This part can be done also using the iptables. first, check the status of the iptables
  > systemctl status iptables

* Add an Entry to the INPUT chain to handle the incoming packets, and Accept packets from port 80 and 443
  > iptables -I INPUT -p tcp --dport 80 -j ACCEPT 
  > iptables -I INPUT -p tcp --dport 443 -j ACCEPT

* make the changes pemanent by saving the changes to the iptables configuration file
  > sudo iptables-save > /etc/sysconfig/iptables

## 8.2

* to Block ssh connection for your colleague ip to the VM, you need his ip , and add the following rule to the iptables
  > iptables -I INPUT -p tcp --dport 22  --source ip -j REJECT


