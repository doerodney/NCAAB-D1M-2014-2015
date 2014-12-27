class TeamHomeCourt:
    def __init__(self):
        pass

    @staticmethod
    def get_team_home_court_code(team_name):
        code = ''
        dict = TeamHomeCourt.get_team_home_court_code_dict()
        if team_name in dict.keys():
            code = dict[team_name]

        return code

    @staticmethod
    def get_team_home_court_code_dict():
        team_home_court_code_dict = {
            'abilene-christian-wildcats': '0036',
            'air-force-falcons': '0002',
            'akron-zips': '0003',
            'alabama-am-bulldogs': '1037',
            'alabama-crimson-tide': '0006',
            'alabama-state-hornets': '0008',
            'albany-great-danes': '1176',
            'alcorn-state-braves': '0010',
            'american-university-eagles': '0014',
            'appalachian-state-mountaineers': '0016',
            'arizona-state-sun-devils': '0018',
            'arizona-wildcats': '0017',
            'arkansas-razorbacks': '0019',
            'arkansas-state-red-wolves': '0022',
            'army-black-knights': '0024',
            'auburn-tigers': '0028',
            'austin-peay-governors': '0032',
            'ball-state-cardinals': '0046',
            'baylor-bears': '0050',
            'belmont-bruins': '0047',
            'bethune-cookman-wildcats': '0052',
            'binghamton-bearcats': '1286',
            'boise-state-broncos': '0057',
            'boston-college-eagles': '0058',
            'boston-university-terriers': '0059',
            'bowling-green-falcons': '0061',
            'bradley-braves': '0062',
            'brown-bears': '0064',
            'bryant-bulldogs': '1594',
            'bucknell-bison': '0066',
            'buffalo-bulls': '0071',
            'butler-bulldogs': '0067',
            'byu-cougars': '0068',
            'california-golden-bears': '0095',
            'cal-poly-mustangs': '0094',
            'cal-state-fullerton-titans': '0219',
            'cal-state-northridge-matadors': '0419',
            'campbell-fighting-camels': '0096',
            'canisius-golden-griffins': '0097',
            'central-arkansas-bears': '1262',
            'central-connecticut-state-blue-devils': '0102',
            'central-michigan-chippewas': '0104',
            'charleston-cougars': '0107',
            'charleston-southern-buccaneers': '0111',
            'charlotte-49ers': '0395',
            'chattanooga-mocs': '0581',
            'chicago-state-cougars': '0112',
            'cincinnati-bearcats': '0116',
            'citadel-bulldogs': '0134',
            'clemson-tigers': '0120',
            'cleveland-state-vikings': '0121',
            'coastal-carolina-chanticleers': '0122',
            'colgate-raiders': '0124',
            'colorado-buffaloes': '0125',
            'colorado-state-rams': '0126',
            'columbia-lions': '0127',
            'connecticut-huskies': '0129',
            'coppin-state-eagles': '0130',
            'cornell-big-red': '0131',
            'creighton-bluejays': '0133',
            'csu-bakersfield-roadrunners': '1105',
            'dartmouth-big-green': '0155',
            'davidson-wildcats': '0156',
            'dayton-flyers': '0157',
            'delaware-fightin-blue-hens': '0159',
            'delaware-state-hornets': '0160',
            'denver-pioneers': '0163',
            'depaul-blue-demons': '0164',
            'detroit-titans': '0165',
            'drake-bulldogs': '0170',
            'drexel-dragons': '0172',
            'duke-blue-devils': '0173',
            'duquesne-dukes': '0174',
            'east-carolina-pirates': '0178',
            'eastern-illinois-panthers': '0179',
            'eastern-kentucky-colonels': '0180',
            'eastern-michigan-eagles': '0181',
            'eastern-washington-eagles': '0184',
            'elon-phoenix': '0195',
            'evansville-aces': '0193',
            'fairfield-stags': '0201',
            'fairleigh-dickinson-knights': '0200',
            'fgcu-eagles': '1383',
            'fiu-golden-panthers': '0212',
            'florida-am-rattlers': '0211',
            'florida-atlantic-owls': '0221',
            'florida-gators': '0210',
            'florida-state-seminoles': '0213',
            'fordham-rams': '0214',
            'fresno-state-bulldogs': '0217',
            'furman-paladins': '0220',
            'gardner-webb-runnin-bulldogs': '1048',
            'george-mason-patriots': '0228',
            'georgetown-hoyas': '0229',
            'george-washington-colonials': '0227',
            'georgia-bulldogs': '0230',
            'georgia-southern-eagles': '0226',
            'georgia-state-panthers': '0231',
            'georgia-tech-yellow-jackets': '0232',
            'gonzaga-bulldogs': '0233',
            'grambling-state-tigers': '0234',
            'grand-canyon-antelopes': '0237',
            'green-bay-phoenix': '0652',
            'hampton-pirates': '0702',
            'hartford-hawks': '0244',
            'harvard-crimson': '0245',
            'hawaii-rainbow-warriors': '0246',
            'high-point-panthers': '1112',
            'hofstra-pride': '0252',
            'holy-cross-crusaders': '0253',
            'houston-baptist-huskies': '0255',
            'houston-cougars': '0254',
            'howard-bison': '0256',
            'idaho-state-bengals': '0265',
            'idaho-vandals': '0263',
            'illinois-fighting-illini': '0267',
            'illinois-state-redbirds': '0269',
            'incarnate-word-cardinals': '1528',
            'indiana-hoosiers': '0271',
            'indiana-state-sycamores': '0274',
            'iona-gaels': '0275',
            'iowa-hawkeyes': '0276',
            'iowa-state-cyclones': '0277',
            'ipfw-mastodons': '0932',
            'iupui-jaguars': '1090',
            'jackson-state-tigers': '0280',
            'jacksonville-dolphins': '0281',
            'jacksonville-state-gamecocks': '0284',
            'james-madison-dukes': '0282',
            'kansas-jayhawks': '0287',
            'kansas-state-wildcats': '0288',
            'kennesaw-state-owls': '1374',
            'kent-state-golden-flashes': '0291',
            'kentucky-wildcats': '0292',
            'lafayette-leopards': '0298',
            'lamar-cardinals': '0299',
            'la-salle-explorers': '0301',
            'lehigh-mountain-hawks': '0303',
            'liberty-flames': '0306',
            'lipscomb-bisons': '1281',
            'liu-brooklyn-blackbirds': '0309',
            'long-beach-state-49ers': '0311',
            'longwood-lancers': '1219',
            'louisiana-monroe-warhawks': '0399',
            'louisiana-ragin-cajuns': '0550',
            'louisiana-tech-bulldogs': '0313',
            'louisville-cardinals': '0314',
            'loyola-chicago-ramblers': '0316',
            'loyola-maryland-greyhounds': '0318',
            'loyola-marymount-lions': '0317',
            'lsu-tigers': '0319',
            'maine-black-bears': '0334',
            'manhattan-jaspers': '0335',
            'marist-red-foxes': '0338',
            'marquette-golden-eagles': '0339',
            'marshall-thundering-herd': '0341',
            'maryland-eastern-shore-hawks': '0347',
            'maryland-terrapins': '0343',
            'massachusetts-lowell-river-hawks': '1543',
            'massachusetts-minutemen': '0344',
            'mcneese-state-cowboys': '0345',
            'memphis-tigers': '0349',
            'mercer-bears': '0350',
            'miami-fl-hurricanes': '0355',
            'miami-oh-redhawks': '0356',
            'michigan-state-spartans': '0358',
            'michigan-wolverines': '0357',
            'middle-tennessee-blue-raiders': '0359',
            'milwaukee-panthers': '0654',
            'minnesota-golden-gophers': '0363',
            'mississippi-state-bulldogs': '0366',
            'mississippi-valley-state-delta-devils': '0364',
            'missouri-state-bears': '0551',
            'missouri-tigers': '0367',
            'monmouth-hawks': '0370',
            'montana-grizzlies': '0372',
            'montana-state-bobcats': '0373',
            'morehead-state-eagles': '0375',
            'morgan-state-bears': '0376',
            'mount-st-marys-mountaineers': '0378',
            'murray-state-racers': '0381',
            'navy-midshipmen': '0392',
            'nebraska-cornhuskers': '0400',
            'nebraska-omaha-mavericks': '1337',
            'nevada-wolf-pack': '0402',
            'new-hampshire-wildcats': '0403',
            'new-mexico-lobos': '0404',
            'new-mexico-state-aggies': '0405',
            'new-orleans-privateers': '0406',
            'niagara-purple-eagles': '0408',
            'nicholls-colonels': '0409',
            'njit-highlanders': '1186',
            'norfolk-state-spartans': '1052',
            'north-carolina-at-aggies': '0410',
            'north-carolina-central-eagles': '0907',
            'north-carolina-state-wolfpack': '0411',
            'north-carolina-tar-heels': '0413',
            'north-dakota': '1279',
            'north-dakota-state-bison': '1455',
            'northeastern-huskies': '0416',
            'northern-arizona-lumberjacks': '0420',
            'northern-colorado-bears': '0425',
            'northern-illinois-huskies': '0417',
            'northern-kentucky-norse': '1506',
            'north-florida-ospreys': '0434',
            'north-texas-mean-green': '0415',
            'northwestern-state-demons': '0422',
            'northwestern-wildcats': '0421',
            'notre-dame-fighting-irish': '0423',
            'oakland-golden-grizzlies': '0441',
            'ohio-bobcats': '0442',
            'ohio-state-buckeyes': '0443',
            'oklahoma-sooners': '0444',
            'oklahoma-state-cowboys': '0446',
            'old-dominion-monarchs': '0447',
            'ole-miss-rebels': '0365',
            'oral-roberts-golden-eagles': '0448',
            'oregon-ducks': '0449',
            'oregon-state-beavers': '0450',
            'pacific-tigers': '0455',
            'penn-quakers': '0460',
            'penn-state-nittany-lions': '0459',
            'pepperdine-waves': '0461',
            'pittsburgh-panthers': '0465',
            'portland-pilots': '0467',
            'portland-state-vikings': '1033',
            'prairie-view-am-panthers': '0468',
            'presbyterian-blue-hose': '0470',
            'princeton-tigers': '0471',
            'providence-friars': '0472',
            'purdue-boilermakers': '0474',
            'quinnipiac-bobcats': '1115',
            'radford-highlanders': '0483',
            'rhode-island-rams': '0485',
            'rice-owls': '0486',
            'richmond-spiders': '0487',
            'rider-broncs': '0488',
            'robert-morris-colonials': '0489',
            'rutgers-scarlet-knights': '0492',
            'sacramento-state-hornets': '0494',
            'sacred-heart-pioneers': '1118',
            'saint-francis-u-red-flash': '0533',
            'saint-josephs-hawks': '0535',
            'saint-louis-billikens': '0536',
            'saint-marys-gaels': '0538',
            'saint-peters-peacocks': '0543',
            'samford-bulldogs': '0496',
            'sam-houston-state-bearkats': '0495',
            'san-diego-state-aztecs': '0498',
            'san-diego-toreros': '0497',
            'san-francisco-dons': '0499',
            'san-jose-state-spartans': '0500',
            'santa-clara-broncos': '0502',
            'savannah-state-tigers': '1066',
            'seattle-redhawks': '0507',
            'seton-hall-pirates': '0508',
            'siena-saints': '0512',
            'siue-cougars': '1196',
            'smu-mustangs': '0515',
            'south-alabama-jaguars': '0524',
            'south-carolina-gamecocks': '0525',
            'south-carolina-state-bulldogs': '0517',
            'south-dakota-coyotes': '1458',
            'south-dakota-state-jackrabbits': '1472',
            'southeastern-louisiana-lions': '0506',
            'southeast-missouri-state-redhawks': '0509',
            'southern-illinois-salukis': '0528',
            'southern-miss-golden-eagles': '0521',
            'southern-university-jaguars': '0241',
            'southern-utah-thunderbirds': '0522',
            'south-florida-bulls': '0526',
            'stanford-cardinal': '0545',
            'st-bonaventure-bonnies': '0531',
            'stephen-f-austin-lumberjacks': '0547',
            'stetson-hatters': '0548',
            'st-francis-brooklyn-terriers': '0532',
            'st-johns-red-storm': '0534',
            'stony-brook-seawolves': '0569',
            'syracuse-orange': '0553',
            'tcu-horned-frogs': '0576',
            'temple-owls': '0577',
            'tennessee-state-tigers': '0582',
            'tennessee-tech-golden-eagles': '0583',
            'tennessee-volunteers': '0580',
            'texas-am-aggies': '0587',
            'texas-am-corpus-christi-islanders': '1231',
            'texas-longhorns': '0585',
            'texas-pan-american-broncs': '0601',
            'texas-southern-tigers': '0591',
            'texas-state-bobcats': '0552',
            'texas-tech-red-raiders': '0592',
            'toledo-rockets': '0594',
            'towson-tigers': '0595',
            'troy-trojans': '0596',
            'tulane-green-wave': '0598',
            'tulsa-golden-hurricane': '0599',
            'uab-blazers': '0034',
            'ualr-trojans': '0020',
            'uapb-golden-lions': '0035',
            'uc-davis-aggies': '0088',
            'ucf-knights': '0103',
            'uc-irvine-anteaters': '0089',
            'ucla-bruins': '0606',
            'uc-riverside-highlanders': '1240',
            'uc-santa-barbara-gauchos': '0501',
            'uic-flames': '0268',
            'umbc-retrievers': '0346',
            'umkc-kangaroos': '0368',
            'unc-asheville-bulldogs': '0393',
            'uncw-seahawks': '0398',
            'uni-panthers': '0418',
            'unlv-runnin-rebels': '0401',
            'usc-trojans': '0609',
            'usc-upstate-spartans': '1203',
            'utah-runnin-utes': '0610',
            'utah-state-aggies': '0611',
            'utah-valley-wolverines': '1424',
            'ut-arlington-mavericks': '0588',
            'utep-miners': '0589',
            'ut-martin-skyhawks': '0578',
            'utsa-roadrunners': '0584',
            'valparaiso-crusaders': '0614',
            'vanderbilt-commodores': '0615',
            'vcu-rams': '0613',
            'vermont-catamounts': '0616',
            'villanova-wildcats': '0617',
            'virginia-cavaliers': '0618',
            'virginia-tech-hokies': '0620',
            'vmi-keydets': '0621',
            'wagner-seahawks': '0627',
            'wake-forest-demon-deacons': '0628',
            'washington-huskies': '0630',
            'washington-state-cougars': '0632',
            'weber-state-wildcats': '0633',
            'western-carolina-catamounts': '0644',
            'western-illinois-leathernecks': '0638',
            'western-kentucky-hilltoppers': '0639',
            'western-michigan-broncos': '0640',
            'west-virginia-mountaineers': '0636',
            'wichita-state-shockers': '0648',
            'william-and-mary-tribe': '0658',
            'winthrop-eagles': '0649',
            'wisconsin-badgers': '0657',
            'wofford-terriers': '0659',
            'wright-state-raiders': '0660',
            'wyoming-cowboys': '0661',
            'xavier-musketeers': '0682',
            'yale-bulldogs': '0684',
            'youngstown-state-penguins': '0685'
        }

        return team_home_court_code_dict

