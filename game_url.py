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
        token_list = self.__game_key.split('-')
        date_location = token_list[-1]
        self.__date_text = date_location[0:8]
        self.__location_code = date_location[8:]

        team_token_list = token_list[0 : len(token_list) - 1]
        team_conference_dict = team_conference.TeamConference.get_team_conference_dict()
        team_name_list = team_conference_dict.keys()

        # Build the team names from right to left.
        second_team_name = '%s-%s' % (team_token_list[-2], team_token_list[-1])
        idx_next_token = len(team_token_list) - 3

        while second_team_name not in team_name_list and idx_next_token >= 0:
            second_team_name = '%s-%s' % (team_token_list[idx_next_token], second_team_name)
            idx_next_token -= 1

        if idx_next_token >= 0:
            team_token_list = team_token_list[0 : idx_next_token + 1]

            first_team_name = '-'.join(team_token_list)

            if first_team_name in team_name_list:
                self.__first_team_name = first_team_name
                self.__second_team_name = second_team_name


    @staticmethod
    def is_division_one(url):
        result = False
        # http://sports.yahoo.com/ncaab/central-pennsylvania-college-knights-radford-highlanders-201412280483
        first_name = ''
        second_name = ''

        game_key = url.replace('http://sports.yahoo.com/ncaab/', '')
        game_key_token_list = game_key.split('-')
        team_name_token_count = len(game_key_token_list) - 1
        team_name_tokens = game_key_token_list[0 : team_name_token_count ]

        # Get a list of valid division one team names.
        team_conference_dict = team_conference.TeamConference.get_team_conference_dict()
        team_name_list = team_conference_dict.keys()

        team_token_list = game_key_token_list[0 : len(game_key_token_list) - 1]
        team_conference_dict = team_conference.TeamConference.get_team_conference_dict()
        team_name_list = team_conference_dict.keys()

        # Build the team names from right to left.
        second_team_name = '%s-%s' % (team_token_list[-2], team_token_list[-1])
        idx_next_token = len(team_token_list) - 3

        while second_team_name not in team_name_list and idx_next_token >= 0:
            second_team_name = '%s-%s' % (team_token_list[idx_next_token], second_team_name)
            idx_next_token -= 1

        if idx_next_token >= 0:
            team_token_list = team_token_list[0 : idx_next_token + 1]

            first_team_name = '-'.join(team_token_list)

            if first_team_name in team_name_list:
                result = True
            else:
                print 'This does not involve two Division One teams:  %s' % game_key

        return result