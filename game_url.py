import team_conference

class GameUrl:
    def __init__(self, url):
        self.__url = url
        self.__game_key = ''
        self.__first_team_name = ''
        self.__second_team_name = ''
        self.__date_text = ''
        self.__location_code = ''
        self.__parse()
        
    @property
    def date_text(self):
        return self.__date_text
    
    @property
    def first_team_name(self):
        return self.__first_team_name
    
    @property
    def game_key(self):
        return self.__game_key

    @property
    def location_code(self):
        return self.__location_code

    @property
    def second_team_name(self):
        return self.__second_team_name

    def __parse(self):
        # url looks like this:
        # url = 'http://sports.yahoo.com/ncaab/temple-owls-villanova-wildcats-201412140617
        # components are:
        # game_key:  temple-owls-villanova-wildcats-201412140617
        # team dict { 'visitor': 'temple-owls', 'home' : 'villanova-wildcats' }
        # date:  20141214
        # location code:  0617

        self.__game_key = self.__url.replace('http://sports.yahoo.com/ncaab/', '')
        team_token_list = self.__game_key.split('-')
        date_location = team_token_list[-1]
        self.__date_text = date_location[0:8]
        self.__location_code = date_location[8:]

        team_conference_dict = team_conference.TeamConference.get_team_conference_dict()
        team_name_list = team_conference_dict.keys()
        first_team_name = '%s-%s' % (team_token_list[0], team_token_list[1])
        tokens_used = 2
        while first_team_name not in team_name_list:
            first_team_name = '%s-%s' % (first_team_name, team_token_list[tokens_used])
            tokens_used += 1

        self.__first_team_name = first_team_name
        second_team_name_token_list = team_token_list[tokens_used : len(team_token_list) - 1]
        self.__second_team_name = '-'.join(second_team_name_token_list)