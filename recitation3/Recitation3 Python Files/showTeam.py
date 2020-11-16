import copy
def show_team_driver(names, team_size):
    show_team(names, team_size, [], 0)

def show_team(names, team_size, result_list, position):
    """
    # Base case 1: we get enough person in the result_list.
    # Base case 2: we have checked all the players.
    
    # Create two branches
    # Branch 1 add current person to result_list
    # Branch 2 does not add current person to result_list(copy)
    # Move on to the next person

    :param names: List[String] -- list of players
    :param team_size: Int -- choose how many players
    :param result_list: List[String] -- Additional list parameter for recursion
    :param position: Int -- Additional index parameter for recursion

    :return: Nothing to return
    :print: All the combinations players
    """
    if len(result_list) == 2:
        print(result_list)
    elif position == len(names):
        return
    else:
        new_result = copy.deepcopy(result_list)
        result_list.append(names[position])
        show_team(names,team_size,new_result,position+1)
        show_team(names,team_size,result_list,position+1)
    

        

    
players = ["Dey", "Ruowen", "Josh", "Kinder", "Mario", "Rock", "LOL"]
show_team_driver(players, 2)

    










