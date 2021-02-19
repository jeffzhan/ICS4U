import csv

def create_pick(picks):
    pick_and_date = {}

    with open(picks, encoding='utf8') as fileIn:
        fileIn.readline()

        reader = csv.reader(fileIn)

        for line in reader:
            match_id = int(line[4])
            date = line[0]
            team1 = line[1]
            team2 = line[2]
            team1_pick = line[14]
            team2_pick = line[15]
            leftover_pick = line[16]

            if match_id not in pick_and_date:
                pick_and_date[match_id] = {}

            pick_and_date[match_id]['date'] = date
            pick_and_date[match_id][team1_pick] = team1
            pick_and_date[match_id][team2_pick] = team2
            pick_and_date[match_id][leftover_pick] = 'No one'

    return pick_and_date
    #{2340454: {'date': '2020-03-18', 'Dust2': 'TeamOne', 'Inferno': 'Recon 5', 'Mirage': 'No one'}



def add_mvp(players, info_dict):
    
    with open(players, encoding='utf8') as fileIn:
        fileIn.readline()

        reader = csv.reader(fileIn)
        
        for line in reader:
            match_id = int(line[6])

            player_name = line[1]
            player_rating = float(line[22])
            
            if match_id in info_dict:
                if 'pNames' not in info_dict[match_id]:
                    info_dict[match_id]['pNames'] = []
                    info_dict[match_id]['pRatings'] = []
                info_dict[match_id]['pNames'].append(player_name)
                info_dict[match_id]['pRatings'].append(player_rating)

    return info_dict



def add_main_info(results, info_dict):
    final_dict = {}

    with open(results, encoding='utf8') as fileIn:
        fileIn.readline()

        reader = csv.reader(fileIn)

        for line in reader:
            match_id = int(line[13])
      
            teams = [line[1], line[2]]
            winnerId = int(line[6]) - 1

            teams = [teams[winnerId], teams[winnerId - 1]]

            score = [int(line[4 + winnerId]), int(line[5 - winnerId])]
            mapPlayed = line[3]

            if match_id in info_dict:
                
                for team in teams:
                    teamIndex = teams.index(team)
                    
                    if team not in final_dict: #adding team to final_dict
                        final_dict[team] = {}
                    
                    if mapPlayed not in final_dict[team]: #adding map to team in final_dict
                        final_dict[team][mapPlayed] = {}

                    if match_id not in final_dict[team][mapPlayed]: #adding match to map for team in final_dict
                        final_dict[team][mapPlayed][match_id] = []

                    win_or_lose = ['Won', 'Lost'] #index 0 will be winning team with teamIndex

                    nest = info_dict[match_id]
                    
                    if mapPlayed in nest: #who picked map
                        team_who_picked_map = nest[mapPlayed]
                    else:
                        team_who_picked_map = 'No One'

                    if 'pNames' in nest: #if there is an mvp
                        mvpRating = max(nest['pRatings']) #get max rating from list of ratings in match
                        mvPlayer = nest['pNames'][nest['pRatings'].index(mvpRating)] #index of player name will be same as index of his/her rating
                        mvp = [mvPlayer, mvpRating] #mvp = list
                    else:
                        mvp = 'MVP Unavailable'
                        
                    final_dict[team][mapPlayed][match_id] = [win_or_lose[teamIndex], f'{score[teamIndex]}:{score[teamIndex-1]}', teams[teamIndex-1], f'{team_who_picked_map}\'s Pick', mvp, nest['date']]
                        
    return final_dict



def print_dict(team_dict):
    tab = ' ' * 3
    
    for team in team_dict:
        print(f'{{{team}:')
        for mapPlayed in team_dict[team]:
            print(f'{tab}{{{mapPlayed}:')
            for match in team_dict[team][mapPlayed]:
                print(f'{tab*2}{{{match}:')
                print(f'{tab*3}{team_dict[team][mapPlayed][match]} }}')
                #print(f'{tab*2}}}')
            print(f'{tab}}}')
        print(f'}}\n')


        
##MAIN
info_dict = create_pick("picks.csv")
info_dict = add_mvp("players.csv", info_dict)
info_dict = add_main_info("results.csv", info_dict)
print_dict(info_dict)

