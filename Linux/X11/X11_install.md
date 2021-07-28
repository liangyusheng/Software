``` shell 
pacman -S xorg

vim /etc/ssh/sshd_config
X11Forwarding yes
X11UseLocalhost no

systemctl restart sshd

# for root user.
cp /home/${user}/.xprofile /home/${user}/.xinitrc /home/${user}/.Xauthority ~

# switch ${user}
xauth list
  arch.localdomain:12  MIT-MAGIC-COOKIE-1  6a953ef1ba468274015d233d781566f1
  arch.localdomain:11  MIT-MAGIC-COOKIE-1  ab9e13d96a96c2401f10c245cae1990b
  arch.localdomain:10  MIT-MAGIC-COOKIE-1  3939b7a0bcb02a58dcb2451831167d13

# switch root. reg last info.
xauth add arch.localdomain:10  MIT-MAGIC-COOKIE-1  3939b7a0bcb02a58dcb2451831167d13

# done.
```
