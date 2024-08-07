# part1

* First, prepare the physical volumes, I already have a PV in sdb disk 
  > pvcreate /dev/sdb1 

 
* Create a volume group, and set 16M as extends
  > vgcreate -s 16M vg1 /dev/sdb1

  **-s Sets  the  physical  extent  size  on  physical volumes of this volume group**
  <br />

* divide the volume group into a logical volume, each is 50 extents
  > lvcreate -n lvm3 -l 50 vg1

  **-l  Gives the number of logical extents to allocate for the new logical volume** <br />
  **-n  Sets the name for the new logical volume**
   <br />
   
* make it as ext4 file system
  > mkfs.ext4 /dev/vg1/lvm3

* Get the UID of the lvm, and make the mount point directory
  > blkid /dev/vg1/lvm3 <br />
  > mkdir -p /mnt/data

* Add the mounting Entry to fstab file, to mount automatically when reboot
  > vi /etc/fstab <br />
  > UUID=db81e709-a6e7-4a3a-8662-c2da42a1db2c /mnt/data ext4 defaults 1 2 

* Run mount -a to mount all the file systems in /etc/fstab, including the entry just added
  > mount -a

* check the changes using lsblk
  
  ![Capture2](https://github.com/user-attachments/assets/14a7d51a-a683-4304-ab3e-f706f5d7551e)

