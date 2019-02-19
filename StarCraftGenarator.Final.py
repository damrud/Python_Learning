import random

race = input('Zerg, Terran or Protos? \n')
race = race.lower()
racelist = ['terran', 'protoss', 'zerg']
time = ''
while race not in racelist:
    race = input('Choose a race! Zerg, Terran or Protos? \n')


while not time.isdigit():
    print ('Its not a fucking number!')
    time = input('Now please provide time (in minutes) for how long game build order should be prepared \n')

time = int(time)
time_1 = time * 60
time_2 = 0

terran1 = ['Scv', 'Marine', 'Medivac', 'Basnhee', 'Maruder', 'Comand Center', 'Supply Depot', 'baracks', 'Starport', 'Enginering Bay'] 
zerg1 = ['Drone', 'Zergling', 'Hydralisk', 'Mutalisk', 'Ultralisk', 'Hatchery', 'Overlord', 'Spawnig Pool', 'Hydralisk Den', 'Ultralisk Den']
protos1 = ['Probe', 'Zelot', 'Stalker', 'Immortal', 'Carrier', 'Nexus', 'Pylon', 'Gateway', 'Robotics Bay', 'Stargate']

while time_2 <= time_1:
    minutes = time_2//60
    seconds = time_2%60
    if race == 'zerg':
        print("[{}:{:02d}] {}" .format(minutes, seconds, random.choice(zerg1)))
    elif race == 'terran':
        print("[{}:{:02d}] {}" .format(minutes, seconds,random.choice(terran1)))
    elif race == 'protos':
        print("[{}:{:02d}] {}" .format(minutes, seconds, random.choice(protos1)))
    time_2 = time_2 + 5

print('\nGG! IMBA WINS!')
