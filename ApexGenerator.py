import random

legends = ['Ash', 'Ballistic', 'Bangalore','Bloodhound', 'Catalyst', 'Caustic','Crypto','Fuse','Gibraltar','Horizon','Lifeline','Loba','Mad Maggie','Mirage','Newcastle','Octane','Pathfinder','Rampart',
              'Revenant','Seer','Valkyrie','Vantage','Wattson','Wraith']

battle_royal_missions = [
    'Get at least 7 kills and 1800 damage with this legend.',
    'Use at least one sniper rifle throughout the match.', 
    'Use at least two different shotguns throughout the match.',
    'Use only light ammo weapons.',
    'Use only heavy ammo weapons.', 
    'Use only energetic ammo weapons.',
    'Perform 3 executions during the match.',
    'You can kill only performing executions during the match.',
    "Don't use light or heavy ammo weapons throughout the match.",
    'Decrease the field of view in the settings to the minimum (72).',
    'Get at least two kills with a red-tier weapon.',
    'Use the wingman and get at least 1 kill.',
    'Finish the match with at least 2000 damage.',
    'Finsh the match with at least 8 kills.',
    'Craft at least 5 times using the replicator during the match.',
    'Use the first two weapons you come across.',
    "Swap the weapons you're using with those of your opponents (at least one weapon).",
    'Use only shotguns weapons.',
    'Use only shotguns and snipers weapons.'
    "Play without using any sights.",
    'Play with only one weapon.',
    'Use only pistols.'
]

control_missions = [
    'Use the first weapon set.',
    'Use the second weapon set.',
    'Use the third weapon set.',
    'Use the fourth weapon set.',
    'Use the fifth weapon set.',
    'Use only red or gold tier weapons.',
    'Perform 5 executions during the match.',
    'Finish the match with at least 2500 damage.',
    'Finsh the match with at least 15 kills.',
    'Capture at least 4 zones.',
    'You can die a maximum of 8 times during the match.'
]

gun_run_missions = [
    "The match can last a maximum of 7 minutes.",
    'You can die a maximum of 4 times during the match.',
    'Finsh the match with at least 9 kills.',
    'Finish the match with at least 2000 damage.',
    'Kill at least 3 opponents with a punch.'
]

team_deathmatch_missions = [
    'Use the first weapon set.',
    'Use the second weapon set.',
    'Use the third weapon set.',
    'Use the fourth weapon set.',
    'Use the fifth weapon set.',
    'Use only red or gold tier weapons.',
    'Perform 5 executions during the match.',
    'Finish the match with at least 2500 damage.',
    'Finsh the match with at least 15 kills.',
    'You can die a maximum of 5 times during the match.',
    "The match can last a maximum of 7 minutes."
]

print('\n-------------------------------------')
your_legend = random.choice(legends)
print('\nYour legend is: '+str(your_legend))

print('\n-------------------------------------')
print('\nDo you want to add a mission?')
response = input('yes or no: ')

if response == "yes":
    print('\n-------------------------------------')
    print('\nOk, choose the mode: ')
    mode = input('\nBattle Royal - 0 \nControl - 1 \nTeam Deathmatch - 2 \nGun Run - 3 \nSelect the mode: ')
    if mode == str(0):
        mission = random.choice(battle_royal_missions)
        print("\nYour mission in Battle Royal is: ", mission)
    elif mode == str(1):
        mission = random.choice(control_missions)
        print("\nYour mission in Control is: ", mission)
    elif mode == str(2):
        mission = random.choice(team_deathmatch_missions)
        print("\nYour mission in Team Deathmatch is: ", mission)
    elif mode == str(3):
        mission = random.choice(gun_run_missions)
        print("\nYour mission in Gun Run is: ", mission)
    else:
        print("\nPlease response with 0, 1, 2 or 3.")
elif response == 'no':
    print('\nOk, you have no missions')
else:
    print('\nPlease response with yes or no.')