# redAlert-eBay

**Changing Source Machine**

1) Machine ssh-key need to added to git-lab project
2) Python3 path need to added into .bash_profile

    >which python3 shows the path of python3
    'nano .bash_profile'
    insert export PYTHONPATH='path comes here':$PYTHONPATH
3) 
    'pip3 install requests'
    'pip3 install serial'
    'pip3 install pyserial'
to terminal

4) 
    'crontab -e' to terminal and insert '*/5 * * * 1-5 /Users/$USER/red-alert/RedAlert-eBay'
   