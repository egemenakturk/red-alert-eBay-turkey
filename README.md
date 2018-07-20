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

5) Open bluetooth and connect with new device

6) Go to terminal

>    `ls /dev/tty.*`

Find new device and copy the adress (Example = /dev/tty.HC-06-SPPDev-1 )

5) Change bluetooth adress below `try` section


### Adding New Device

1) Open bluetooth and connect with new device

2) Go to terminal

>    `ls /dev/tty.*`

Find new device and copy the adress (Example = /dev/tty.HC-06-SPPDev-1 )

3) Go to .py folder and add below `try` section :

>    `new_team_name = serial.Serial('adress_of_device', 9600)`    

4) Add new team name to `teams` array 

5) Edit `def job_results` and `def send_message` `if` section



   