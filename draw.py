from random import choice

group_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
gear_list = [1, 2, 3, 4]
team_nation_dict = {
    'Real Madrid': 'Spain', 'Barca': 'Spain', 'Bayern Munich': 'Germany', 'Benfica' : 'Portugal',
    'Paris Saint-Germain':'France','Juventus':'Italy','CSKA Moscow':'Russia_Ukraine','Leicester City':'England',
    'Athletic Madrid':'Spain','Dortmund':'Germany','Arsenal':'England','Manchester City':'England',
    'Sevilla':'Spain','Porto':'Portugal','Napoli':'Italy','Leverkusen':'Germany',
    'Basel':'Switzerland','Tottenham Hotspur':'England','FC Dinamo Kyiv':'Russia_Ukraine','Lyon':'France',
    'Sporting Lisbon':'Portugal','PSV':'Netherlands','Brugge':'Belgium','Monchengladbach':'Germany',
    'Celtic':'Scotland','Monaco':'France','Besiktas JK':'Turkey','LegiaWarszawa':'Poland',
    'PFC Ludogorets Razgrad':'Bulgaria','Dinamo Zagreb':'Croatia','Copenhagen':'Denmark','FC Rostov':'Russia_Ukraine'}
team_gear = [
    ['Real Madrid','Barca','Bayern Munich','Benfica','Paris Saint-Germain','Juventus','CSKA Moscow','Leicester City'],
    ['Athletic Madrid','Dortmund','Arsenal','Manchester City','Sevilla','Porto','Napoli','Leverkusen'],
    ['Basel','Tottenham Hotspur','FC Dinamo Kyiv','Lyon','Sporting Lisbon','PSV','Brugge','Monchengladbach'],
    ['Celtic','Monaco','Besiktas JK','LegiaWarszawa','PFC Ludogorets Razgrad','Dinamo Zagreb','Copenhagen','FC Rostov']
]

while True:
    try:
        group_nation = {}
        result = {}

        for gear in gear_list:
            not_draw_teams = list(team_gear[gear-1])
            for group in group_list:
                # get which team can draw in the group
                team_list = []
                if group in group_nation:
                    for team in not_draw_teams:
                        if team_nation_dict[team] not in group_nation[group]:
                            team_list.append(team)
                else:
                    team_list = not_draw_teams

                 # draw the team
                _res = choice(team_list)
                not_draw_teams.remove(_res)
                if group not in result:
                    result[group] = []
                result[group].append(_res)
                if group not in group_nation:
                    group_nation[group] = []
                group_nation[group].append(team_nation_dict[_res])
    except IndexError:
        continue
    for group in group_list:
        print('group{}:{}'.format(group,','.join(result[group])))
    break
