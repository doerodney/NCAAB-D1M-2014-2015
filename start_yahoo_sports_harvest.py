from datetime import date, timedelta
from optparse import OptionParser

def get_conference_code_dict():
    conference_code_dict = {
     'America East': 99,
     'Atlantic Coast': 6,
     'Atlantic Ten': 101,
     'Atlantic Sun': 107,
     'American Athletic': 201,
     'Big 12': 103,
     'Big East': 102,
     'Big Sky': 15,
     'Big South': 16,
     'Big Ten': 3,
     'Big West': 8,
     'Colonial Athletic': 17,
     'Conference USA': 1,
     'Horizon League': 34,
     'Independents': 35,
     'Ivy League': 18,
     'Metro Atlantic Athletic': 19,
     'Mid-American': 20,
     'Mid-Eastern': 31,
     'Missouri Valley': 21,
     'Mountain West': 112,
     'Northeast': 32,
     'Ohio Valley': 23,
     'Pac-12':  2,
     'Patriot League': 24,
     'Southeastern': 10,
     'Southland': 28,
     'Southwestern Athletic': 105,
     'Summit': 194,
     'Sun Belt': 5,
     'West Coast': 110,
     'Western Athletic': 111
    }
    return conference_code_dict

def get_conference_day_url_list(datestamp):
    """ Returns a list of URLs for the results of a conference-day.
        Use this url to look up results for each conference-day combination.
    """
    conference_day_url_list = []
    # Get the sorted conference names and their Yahoo codes.
    conference_code_dict = get_conference_code_dict()
    conference_name_list = sorted(conference_code_dict.keys())
    for conference_name in conference_name_list:
        # print conference_name
        conference_code = conference_code_dict[conference_name]
        url = str.format('http://sports.yahoo.com/college-basketball/scoreboard/?date={0}&conf={1}',
                         datestamp, conference_code)
        conference_day_url_list.append(url)

    return conference_day_url_list

def get_day_data_url_list(datestamp):
    """
    Iterates conference-combinations to get the data urls for each game played.
    """
    day_data_url_list = []
    conference_day_url_list = get_conference_day_url_list(datestamp)
    for conference_day_url in conference_day_url_list:
        print conference_day_url


def main():
    # Get year, month, day args for yesterday.
    yesterday = date.today() - timedelta(1)
    year = yesterday.year
    month = yesterday.month
    day = yesterday.day

    parser = OptionParser()
    parser.add_option('-y', '--year', dest='year',
                      help='Year of data to acquire.', default='')
    parser.add_option('-m', '--month', dest='month',
                      help='Month of data to acquire.',
                      default='')
    parser.add_option('-d', '--day', dest='day',
                      help='Day of data to acquire.',
                      default='')

    # Get year month day from options.
    (options, args) = parser.parse_args()
    if options.year != '':
        year = int(options.year)
    if options.month != '':
        month = int(options.month)
    if options.day != '':
        day = int(options.day)

    # If year, month, day args are not fully defined, use yesterday.
    if year == None or month == None or day == None:
        yesterday = date.today() - timedelta(1)
        year = yesterday.year
        month = yesterday.month
        day = yesterday.day

    datestamp = str.format('{0}-{1}-{2}',
        str(year), str(month).zfill(2), str(day).zfill(2))
    print 'Acquiring data for ', datestamp

    day_data_url_list = get_day_data_url_list(datestamp)

main()

