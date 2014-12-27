from datetime import date, timedelta
import game_url
import xml.etree.ElementTree
from optparse import OptionParser
import urllib

def get_box_score_content(url):
    # Pull in content from the URL.
    response = urllib.urlopen(url)
    url_content = response.read()

    # A box score starts and ends with these.
    target_start = '<h4 '
    target_end = '</table>'

    content_section_list = get_content_section_list(url_content, target_start,
                                                    target_end)

    for section in content_section_list:
        start_index = section['start_index']
        length = section['length']
        box_score_content = url_content[start_index : start_index + length]
        table_start = '<table'
        thead_start = '<thead'
        idx_table_start =  box_score_content.find(table_start, 0)
        idx_thead_start = box_score_content.find(thead_start, 0)
        header_text = box_score_content[0 : idx_table_start]
        table_text = '%s%s' % ('<table>', box_score_content[idx_thead_start : ])

        # Parse the school name out of the header.
        # Step over the target start and find the next '>'.
        idx_name_start = box_score_content.find( '>', len(target_start)) + 1
        idx_name_end = box_score_content.find('<', idx_name_start)
        school_name = box_score_content[idx_name_start : idx_name_end]
        print school_name

        # Parse the box score content.
        root = xml.etree.ElementTree.fromstring(table_text)
        print str(root)


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

def get_conference_game_url_list(conference_url):
    game_url_list = []

    # Pull in content from the URL.
    response = urllib.urlopen(conference_url)
    content = response.read()

    # Look for instances of data-url, as in
    # data-url="/ncaab/rice-owls-washington-state-cougars-201411280632/"
    found_target_list = []
    target = 'data-url'
    idx_found = 0
    while True:
        idx_found = content.find(target, idx_found)
        if idx_found >= 0:
            found_target_list.append(idx_found)
            # Step beyond.
            idx_found += 1
        else:
            break

    # Parse URL from content.
    for start_index in found_target_list:
        url = parse_game_url(content, start_index )
        if len(url) > 0:
            game_url_list.append(url)

    return game_url_list

def get_conference_url_dict(datestamp):
    """ Returns a dictionary of URLs to visit to obtain the results of a conference-day.
        Use this url to look up results for each conference-day combination.
        Look up by conference because yahoo is fussy about getting too much data,
        and they don't (yet) seem to fuss about pulling a conference's data
        for a day.
    """
    conference_url_dict = {}

    # Get the sorted conference names and their Yahoo codes.
    conference_code_dict = get_conference_code_dict()
    conference_name_list = sorted(conference_code_dict.keys())
    for conference_name in conference_name_list:
        # print conference_name
        conference_code = conference_code_dict[conference_name]
        url = str.format('http://sports.yahoo.com/college-basketball/scoreboard/?date={0}&conf={1}',
                         datestamp, conference_code)
        conference_url_dict[conference_name] = url

    return conference_url_dict

def get_content_section_list(content, target_start, target_end):
    idx_search = 0
    idx_found = 0
    idx_start = 0

    content_section_list = []

    while idx_found >= 0:
        # Find the start of the section.
        idx_found = content.find(target_start, idx_search)
        if idx_found >= 0:
            item_start_index = idx_found
            # Step over and resume search.
            idx_search = idx_found + len(target_start)

            # Find the end of the section.
            idx_found = content.find(target_end, idx_search)
            if idx_found >= 0:
                # Calculate index of next search.
                idx_search = idx_found + len(target_end)

                # Record results of search.
                content_section = {}
                content_section['start_index'] = item_start_index
                content_section['length'] = idx_search - item_start_index
                content_section_list.append(content_section)

    return content_section_list

def get_data_url_list(datestamp):
    """
    Iterates conference-combinations to get the data urls for each game played
    for a given date.
    """
    data_url_list = []
    conference_url_dict = get_conference_url_dict(datestamp)
    conference_name_list = sorted(conference_url_dict.keys())
    for conference_name in conference_name_list:
        print 'conference: ', conference_name
        conference_url = conference_url_dict[conference_name]
        conference_game_url_list = get_conference_game_url_list(conference_url)
        for game_url in conference_game_url_list:
            print game_url
            data_url_list.append(game_url)

    return sorted(set(data_url_list))

def parse_game_url(content, start_index):
    """
    start_index is the index of the 'd' in data-url, as in
    data-url="/ncaab/rice-owls-washington-state-cougars-201411280632/"
    """
    game_url = ''

    # Find the index of the next double quote.
    target = '"'
    quote_idx_list = []
    idx = start_index
    for i in range(0,2):
        idx = content.find(target, idx)
        if idx > 0:
            quote_idx_list.append(idx)
            idx += 1
        else:
            break

    # At this point, if we have two quotes, we can get the url.

    header = 'http://sports.yahoo.com'
    guts = ''
    if len(quote_idx_list) == 2:
        guts = content[(quote_idx_list[0] + 1) : (quote_idx_list[1] - 1)]
        game_url = header + guts
        print game_url

    return game_url

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

    #data_url_list = get_data_url_list(datestamp)
    print "\nURL List:"
    #for url in data_url_list:
    #    print url
    url = 'http://sports.yahoo.com/ncaab/temple-owls-villanova-wildcats-201412140617'
    get_box_score_content(url)

main()

