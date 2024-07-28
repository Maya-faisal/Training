# part1

* First, prepare the physical volumes, I already have a PV in sdb disk 
  > pvcreate /dev/sdb1 

 
* Create a volume group, and set 16M as extends
  > vgcreate -s 16M vg1 /dev/sdb1
  <br />
  *** -s Sets  the  physical  extent  size  on  physical volumes of this volume group  ***

* divide the volume group into a logical volume, each is 50 extents
  > pvcreate -l 50 -n lvm3
  <br />
  *** -l  Gives the number of logical extents to allocate for the new logical volume ***
  *** -n  Sets the name for the new logical volume ***

* make it as ext4 file system
  > mkfs.ext4 /dev/lvm3

* Get the UID of the lvm, and make the mount point directory
  > blkid /dev/vg1/lvm3
  > mkdir -p /mnt/data
  <br />
  *** -p ***

* Add the mounting Entry to fstab file 
  > vi /etc/fstab 
  > UID= <uid>  <mounting point>  <file format>  <defaults>  <dump flag>  <fsck order>
  > UID= UUID="db81e709-a6e7-4a3a-8662-c2da42a1db2c" /mnt/data ext4 defaults 1 2 

* Run mount -a to mount all the file systems in /etc/fstab, including the entry just added
  > mount -a

* check the changes using lsblk


