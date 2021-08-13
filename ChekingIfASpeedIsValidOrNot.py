# author : Sarvin Nami
speed = int(input('Please enter your current speed : '))
speed_hour = speed/60
if speed_hour >= 0 and speed_hour < 50 :
    print('Oh your speed is very low! Speed up!')
elif speed_hour >= 50 and speed_hour < 100 :
    print('You are a carefull driver!')
elif speed_hour >= 100 and speed_hour < 150 :
    print('You are a cool driver. be carefull.')
elif speed_hour >= 150 :
    print('You seem to be a rally racer! Good lock!')
else :
    print('Sorry your speed is not acceptable.')
