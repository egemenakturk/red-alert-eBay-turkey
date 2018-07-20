# Red-Alert-eBay


### Changing Source Machine




1) Machine ssh-key need to added to git-lab project

2) Python3 path need to added into .bash_profile

>   `which python3` shows the path of python3

>   `nano .bash_profile`

>   insert `export PYTHONPATH='path comes here':$PYTHONPATH`

3) To Terminal

>    `pip3 install requests`
    
>    `pip3 install serial`
    
>    `pip3 install pyserial`

4) Now we need to schedule the program
    
>    to terminal `crontab -e` 
>    insert `*/5 * * * 1-5 /Users/$USER/red-alert/RedAlert-eBay`
   