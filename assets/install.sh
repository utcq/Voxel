sudo rm -r /usr/lib/voxel
sudo git clone https://github.com/UnityTheCoder/Voxel /usr/lib/voxel
make -C /usr/lib/voxel setup
sudo rm /usr/bin/vxc
sudo ln -s /usr/lib/voxel/voxel /usr/bin/vxc
