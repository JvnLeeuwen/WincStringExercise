# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'
# Add your code after this line
# create variables with scorers names
scorer_goal_0 = 'Ruud Gullit'
scorer_goal_1 = 'Marco van Basten'
# create variables with time code of goals
goal_0 = 32
goal_1 = 54
# create variable for short goal summary
scorers = scorer_goal_0+" "+str(goal_0)+", "+scorer_goal_1+" "+str(goal_1)
# create variable for long goal summary
report = f'{scorer_goal_0} scored in the {goal_0}nd minute\n{scorer_goal_1} scored in the {goal_1}th minute'
print(report)
# create a player variables
player = "Arnold Mühren"
first_name = player[:player.find(" ")]
last_name_len = len(player)-player.find(" ")-1
last_name = player[player.find(" ")+1:len(player)]
name_short = first_name[0:1]+". "+last_name
# let's chant
chant = (first_name+"! ")*(len(first_name)-1)+(first_name+"!")
good_chant = chant[len(chant)-1:len(chant)]!=" "
