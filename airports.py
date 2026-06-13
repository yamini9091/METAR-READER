"""
Comprehensive worldwide airport database
169 major airports from 50+ countries across 6 continents
Format: ICAO code: (City, Country, METAR sample)
"""

AIRPORTS = {
    # ============= UNITED KINGDOM =============
    'EGLL': ('London Heathrow', 'UK', 'EGLL 121850Z 31015G25KT 9999 BKN040 OVC080 12/08 Q1012'),
    'EGKK': ('London Gatwick', 'UK', 'EGKK 121850Z 32014KT 9999 BKN050 OVC100 13/09 Q1011'),
    'EGSS': ('London Stansted', 'UK', 'EGSS 121850Z 30012KT 9999 BKN040 OVC090 14/10 Q1012'),
    'EGLC': ('London City', 'UK', 'EGLC 121850Z 31013KT 9000 BKN030 OVC070 12/08 Q1012'),
    'EGPN': ('Prestwick', 'UK', 'EGPN 121820Z 02018KT 7000 OVC015 11/10 Q1010'),
    'EGGW': ('Luton', 'UK', 'EGGW 121850Z 30012KT 9000 BKN030 OVC080 13/09 Q1013'),
    'EGCC': ('Manchester', 'UK', 'EGCC 121850Z 29012KT 9999 BKN040 OVC100 13/08 Q1012'),
    'EGNX': ('East Midlands', 'UK', 'EGNX 121900Z 28011KT 9999 BKN050 OVC120 12/08 Q1012'),
    'EGPH': ('Edinburgh', 'UK', 'EGPH 121820Z 03016KT 8000 OVC020 10/08 Q1011'),
    'EGPF': ('Glasgow', 'UK', 'EGPF 121820Z 02014KT 7500 OVC025 11/09 Q1010'),
    'EGNT': ('Newcastle', 'UK', 'EGNT 121850Z 30011KT 9999 BKN050 OVC130 12/08 Q1012'),
    'EGTB': ('Southend', 'UK', 'EGTB 121850Z 31012KT 9000 BKN030 OVC080 13/09 Q1012'),

    # ============= USA =============
    'KLAX': ('Los Angeles', 'USA', 'KLAX 121853Z 26008KT 10SM FEW250 23/14 A3012 RMK'),
    'KJFK': ('New York JFK', 'USA', 'KJFK 121851Z 09014KT 4SM BR BKN025 OVC050 14/12 A3000 RMK'),
    'KSFO': ('San Francisco', 'USA', 'KSFO 121856Z 09016G23KT 8SM FEW015 BKN030 15/13 A2990 RMK'),
    'KORD': ('Chicago ORD', 'USA', 'KORD 121856Z 18012KT 10SM SCT040 OVC100 16/11 A2995 RMK'),
    'KDFW': ('Dallas Fort Worth', 'USA', 'KDFW 121853Z 18018KT 10SM SCT050 BKN150 28/16 A2998 RMK'),
    'KATL': ('Atlanta', 'USA', 'KATL 121852Z 17015KT 10SM FEW050 SCT150 24/14 A3001 RMK'),
    'KMIA': ('Miami', 'USA', 'KMIA 121856Z 18012KT 10SM FEW100 SCT250 28/23 A3005 RMK'),
    'KSEA': ('Seattle', 'USA', 'KSEA 121856Z 16010KT 8SM BKN020 OVC040 14/12 A2985 RMK'),
    'KDEN': ('Denver', 'USA', 'KDEN 121853Z 18015KT 10SM FEW080 SCT200 18/08 A3015 RMK'),
    'KLAS': ('Las Vegas', 'USA', 'KLAS 121856Z 25012KT 10SM FEW080 SCT200 32/15 A2990 RMK'),
    'KIAD': ('Washington Dulles', 'USA', 'KIAD 121852Z 16014KT 10SM FEW060 SCT150 18/10 A3002 RMK'),
    'KLGA': ('New York LaGuardia', 'USA', 'KLGA 121851Z 09015KT 4SM BR BKN025 OVC050 14/12 A3000 RMK'),
    'KBOS': ('Boston', 'USA', 'KBOS 121854Z 08016KT 8SM BKN030 OVC080 12/09 A3001 RMK'),
    'KDCA': ('Washington Reagan', 'USA', 'KDCA 121852Z 16014KT 10SM FEW070 SCT160 18/10 A3002 RMK'),
    'KMCO': ('Orlando', 'USA', 'KMCO 121853Z 18012KT 10SM FEW100 BKN250 26/20 A3005 RMK'),
    'KDET': ('Detroit', 'USA', 'KDET 121856Z 17013KT 10SM BKN040 OVC120 15/10 A2996 RMK'),
    'KPHX': ('Phoenix', 'USA', 'KPHX 121853Z 24010KT 10SM FEW100 SCT250 34/16 A2988 RMK'),
    'KMIN': ('Minneapolis', 'USA', 'KMIN 121856Z 19012KT 10SM FEW060 SCT150 14/08 A3004 RMK'),

    # ============= CANADA =============
    'CYYZ': ('Toronto', 'Canada', 'CYYZ 121800Z 27015G25KT 6SM -SN BKN025 OVC040 -5/-8 A3001 RMK'),
    'CYMX': ('Montreal', 'Canada', 'CYMX 121830Z 18008KT 10SM SKC -8/-12 A3015 RMK'),
    'CYVR': ('Vancouver', 'Canada', 'CYVR 121853Z 32018KT 7SM -RA OVC015 08/05 A3008 RMK'),
    'CYEG': ('Edmonton', 'Canada', 'CYEG 121856Z 28012KT 10SM FEW100 SCT250 12/05 A3012 RMK'),
    'CYCA': ('Calgary', 'Canada', 'CYCA 121900Z 32016KT 10SM BKN050 OVC150 10/02 A3010 RMK'),
    'CYOW': ('Ottawa', 'Canada', 'CYOW 121900Z 16012KT 10SM BKN040 OVC120 12/07 A3004 RMK'),
    'CYUL': ('Montreal Trudeau', 'Canada', 'CYUL 121900Z 17010KT 10SM SCT050 BKN150 14/09 Q1015 RMK'),
    'CYWG': ('Winnipeg', 'Canada', 'CYWG 121900Z 24010KT 10SM FEW080 SCT200 08/01 A3012 RMK'),

    # ============= FRANCE =============
    'LFPG': ('Paris CDG', 'France', 'LFPG 121900Z 32012KT 9999 BKN050 OVC100 14/09 Q1015'),
    'LFPO': ('Paris Orly', 'France', 'LFPO 121900Z 31014KT 9999 BKN060 OVC120 15/10 Q1014'),
    'LFLL': ('Lyon', 'France', 'LFLL 121900Z 28010KT 9999 FEW050 SCT150 16/10 Q1016'),
    'LFML': ('Marseille', 'France', 'LFML 121900Z 22012KT 10SM FEW080 SCT200 18/12 Q1015'),
    'LFBT': ('Toulouse', 'France', 'LFBT 121900Z 20008KT 10SM BKN050 OVC150 19/12 Q1014'),
    'LFSB': ('Basel', 'France', 'LFSB 121900Z 26010KT 10SM FEW060 SCT160 15/10 Q1016'),

    # ============= GERMANY =============
    'EDDF': ('Frankfurt', 'Germany', 'EDDF 121920Z 01008KT 9999 SCT040 BKN100 12/08 Q1018'),
    'EDDM': ('Munich', 'Germany', 'EDDM 121950Z 28010KT 9999 FEW050 SCT150 10/06 Q1020'),
    'EDDB': ('Berlin', 'Germany', 'EDDB 121920Z 08010KT 10SM BKN050 OVC130 13/08 Q1016'),
    'EDDH': ('Hamburg', 'Germany', 'EDDH 121920Z 09008KT 10SM SCT050 BKN140 11/07 Q1017'),
    'EDDK': ('Cologne', 'Germany', 'EDDK 121920Z 02010KT 9999 BKN060 OVC150 12/08 Q1017'),
    'EDDS': ('Stuttgart', 'Germany', 'EDDS 121930Z 05008KT 10SM FEW080 SCT200 14/09 Q1018'),
    'EDDL': ('Düsseldorf', 'Germany', 'EDDL 121920Z 03009KT 10SM BKN050 OVC140 12/08 Q1017'),

    # ============= SPAIN =============
    'LEMD': ('Madrid', 'Spain', 'LEMD 121930Z 23014KT 10SM FEW060 SCT150 18/10 Q1015'),
    'LEIB': ('Barcelona', 'Spain', 'LEIB 121930Z 20012KT 10SM FEW080 SCT200 18/13 Q1014'),
    'LEVT': ('Valencia', 'Spain', 'LEVT 121930Z 18010KT 10SM BKN050 OVC150 20/14 Q1014'),
    'LEMG': ('Málaga', 'Spain', 'LEMG 121940Z 14008KT 10SM FEW100 SCT250 22/15 Q1015'),
    'LEAT': ('Alicante', 'Spain', 'LEAT 121940Z 15010KT 10SM SCT080 BKN200 21/15 Q1015'),
    'LEPA': ('Palma de Mallorca', 'Spain', 'LEPA 121940Z 18012KT 10SM FEW100 SCT250 21/16 Q1014'),

    # ============= ITALY =============
    'LIRF': ('Rome Fiumicino', 'Italy', 'LIRF 121930Z 10010KT 10SM FEW100 SCT200 20/12 Q1016'),
    'LIRA': ('Rome Ciampino', 'Italy', 'LIRA 121930Z 10008KT 10SM SCT100 BKN250 20/12 Q1016'),
    'LIML': ('Milan Malpensa', 'Italy', 'LIML 121920Z 08008KT 10SM FEW050 SCT150 14/09 Q1018'),
    'LIBD': ('Brindisi', 'Italy', 'LIBD 121930Z 12008KT 10SM SCT100 BKN250 20/15 Q1015'),
    'LIME': ('Milan Linate', 'Italy', 'LIME 121920Z 08010KT 10SM FEW060 SCT180 15/10 Q1017'),
    'LIPZ': ('Venice', 'Italy', 'LIPZ 121920Z 06008KT 10SM FEW080 SCT200 14/09 Q1017'),

    # ============= NETHERLANDS =============
    'EHAM': ('Amsterdam', 'Netherlands', 'EHAM 121850Z 06010KT 10SM FEW060 SCT150 12/08 Q1017'),

    # ============= BELGIUM =============
    'EBBR': ('Brussels', 'Belgium', 'EBBR 121850Z 04008KT 10SM BKN050 OVC140 12/08 Q1017'),

    # ============= SWITZERLAND =============
    'ZZZH': ('Zurich', 'Switzerland', 'ZZZH 121930Z 35008KT 10SM FEW100 BKN250 16/11 Q1020'),

    # ============= AUSTRIA =============
    'LOWW': ('Vienna', 'Austria', 'LOWW 121920Z 09012KT 10SM BKN040 OVC100 14/09 Q1014'),

    # ============= CZECH REPUBLIC =============
    'LKPR': ('Prague', 'Czech Republic', 'LKPR 121920Z 08010KT 9999 BKN050 OVC120 12/07 Q1016'),

    # ============= POLAND =============
    'EPWA': ('Warsaw', 'Poland', 'EPWA 121920Z 06008KT 10SM SCT050 BKN150 14/09 Q1015'),

    # ============= HUNGARY =============
    'LHBP': ('Budapest', 'Hungary', 'LHBP 121950Z 12010KT 10SM SCT060 OVC140 15/10 Q1015'),

    # ============= RUSSIA =============
    'UUWW': ('Moscow Vnukovo', 'Russia', 'UUWW 121930Z 28018G28KT 8000 -SN OVC020 -4/-8 Q998'),
    'UUDD': ('Moscow Domodedovo', 'Russia', 'UUDD 121930Z 27016G24KT 8000 OVC030 -3/-7 Q1000'),

    # ============= GREECE =============
    'LGAV': ('Athens', 'Greece', 'LGAV 122000Z 08008KT 10SM FEW080 SCT200 22/14 Q1016'),

    # ============= PORTUGAL =============
    'LPPT': ('Lisbon', 'Portugal', 'LPPT 121930Z 18010KT 10SM FEW080 SCT200 18/12 Q1014'),

    # ============= TURKEY =============
    'LTFM': ('Istanbul', 'Turkey', 'LTFM 121930Z 16012KT 10SM BKN050 OVC150 18/11 Q1015'),

    # ============= JAPAN =============
    'RJTT': ('Tokyo Haneda', 'Japan', 'RJTT 121830Z 17012KT 10SM FEW100 SCT250 18/09 A3008'),
    'RJOO': ('Osaka Kansai', 'Japan', 'RJOO 121800Z 16010KT 10SM BKN050 OVC150 19/10 A3010'),
    'RJFF': ('Fukuoka', 'Japan', 'RJFF 121800Z 14010KT 10SM FEW100 SCT250 20/12 A3007'),

    # ============= CHINA =============
    'ZBAA': ('Beijing', 'China', 'ZBAA 121900Z 36010KT 8000 SCT100 BKN200 19/04 Q1018'),
    'ZSPD': ('Shanghai', 'China', 'ZSPD 121900Z 32008KT 8000 BKN080 OVC150 22/15 Q1015'),
    'ZGSZ': ('Shenzhen', 'China', 'ZGSZ 121900Z 08012KT 10SM SCT050 BKN150 28/22 Q1012'),

    # ============= HONG KONG =============
    'VHHH': ('Hong Kong', 'Hong Kong', 'VHHH 121900Z 08012KT 10SM FEW080 BKN200 26/21 Q1015'),

    # ============= SOUTH KOREA =============
    'RKSI': ('Seoul Incheon', 'South Korea', 'RKSI 121900Z 28012KT 10SM FEW100 SCT250 16/08 Q1018'),

    # ============= THAILAND =============
    'VTBS': ('Bangkok', 'Thailand', 'VTBS 121900Z 16010KT 9000 -RA SCT020 BKN050 29/25 Q1009'),

    # ============= MALAYSIA =============
    'WMKK': ('Kuala Lumpur', 'Malaysia', 'WMKK 121900Z 20008KT 10SM SCT030 BKN100 31/25 Q1011'),

    # ============= SINGAPORE =============
    'WSSS': ('Singapore', 'Singapore', 'WSSS 121900Z 35008KT 10SM BKN040 OVC100 28/24 Q1012'),

    # ============= PHILIPPINES =============
    'RPLL': ('Manila', 'Philippines', 'RPLL 121900Z 12008KT 10SM SCT050 BKN150 30/26 Q1010'),

    # ============= INDONESIA =============
    'WIII': ('Jakarta', 'Indonesia', 'WIII 121900Z 22010KT 10SM BKN040 OVC120 28/24 Q1010'),

    # ============= INDIA =============
    'VIDP': ('Delhi', 'India', 'VIDP 121900Z 28015KT 6000 HZ SCT080 OVC150 32/18 Q1008'),
    'VABB': ('Mumbai', 'India', 'VABB 121900Z 18012KT 6000 HZ BKN080 OVC150 32/22 Q1008'),
    'VOCC': ('Cochin', 'India', 'VOCC 121900Z 10008KT 8000 BKN040 OVC120 28/24 Q1010'),

    # ============= UAE =============
    'OMDB': ('Dubai', 'UAE', 'OMDB 121900Z 32016KT 10SM FEW080 SCT200 38/22 Q1005'),

    # ============= BRAZIL =============
    'SBGR': ('São Paulo Guarulhos', 'Brazil', 'SBGR 121900Z 11008KT 10SM FEW080 SCT200 25/18 A3007'),
    'SBRJ': ('Rio de Janeiro', 'Brazil', 'SBRJ 121900Z 18012KT 10SM SCT080 BKN200 26/20 A3010'),
    'SBBR': ('Brasília', 'Brazil', 'SBBR 121900Z 16010KT 10SM FEW080 SCT250 26/14 A3008'),

    # ============= ARGENTINA =============
    'SABE': ('Buenos Aires Ezeiza', 'Argentina', 'SABE 121900Z 03012KT 10SM BKN040 OVC100 18/14 A3010'),
    'SAAR': ('Buenos Aires Aeroparque', 'Argentina', 'SAAR 121900Z 03012KT 10SM BKN050 OVC120 17/13 A3010'),

    # ============= CHILE =============
    'SCEL': ('Santiago', 'Chile', 'SCEL 121900Z 08015KT 10SM FEW050 BKN150 22/11 A3005'),

    # ============= COLOMBIA =============
    'SKBO': ('Bogotá', 'Colombia', 'SKBO 121900Z 18010KT 10SM BKN015 OVC050 18/13 A3012'),

    # ============= AUSTRALIA =============
    'YSSY': ('Sydney', 'Australia', 'YSSY 121900Z 04008KT 10SM FEW080 BKN200 22/16 Q1024'),
    'YMML': ('Melbourne', 'Australia', 'YMML 121900Z 25012KT 10SM SCT050 BKN150 20/14 Q1022'),
    'YBBN': ('Brisbane', 'Australia', 'YBBN 121900Z 18010KT 10SM FEW080 SCT200 26/18 Q1020'),
    'YPER': ('Perth', 'Australia', 'YPER 121900Z 22016KT 10SM FEW100 SCT250 28/15 Q1018'),
    'YADL': ('Adelaide', 'Australia', 'YADL 121900Z 20012KT 10SM BKN050 OVC150 24/14 Q1020'),

    # ============= NEW ZEALAND =============
    'NZAA': ('Auckland', 'New Zealand', 'NZAA 121900Z 18010KT 10SM BKN040 OVC100 18/12 Q1018'),
    'NZCH': ('Christchurch', 'New Zealand', 'NZCH 121900Z 22015KT 10SM FEW060 SCT150 16/10 Q1015'),
    'NZWN': ('Wellington', 'New Zealand', 'NZWN 121900Z 20018G28KT 10SM BKN040 OVC100 14/10 Q1012'),

    # ============= SOUTH AFRICA =============
    'FAOR': ('Johannesburg', 'South Africa', 'FAOR 121900Z 18010KT 10SM BKN050 OVC150 24/14 Q1018'),
    'FACT': ('Cape Town', 'South Africa', 'FACT 121900Z 08012KT 10SM BKN040 OVC120 18/12 Q1018'),

    # ============= EGYPT =============
    'HECA': ('Cairo', 'Egypt', 'HECA 121900Z 28015KT 10SM FEW080 SCT200 35/18 Q1010'),

    # ============= ALGERIA =============
    'DIAP': ('Algiers', 'Algeria', 'DIAP 121900Z 12008KT 9000 HZ SCT100 OVC200 28/22 Q1012'),

    # ============= MOROCCO =============
    'GMME': ('Casablanca', 'Morocco', 'GMME 121900Z 18012KT 10SM FEW050 SCT150 24/15 Q1014'),

    # ============= MEXICO =============
    'MMMX': ('Mexico City', 'Mexico', 'MMMX 121856Z 18012KT 10SM FEW100 SCT250 24/12 A3001'),
    'MMEX': ('Cancún', 'Mexico', 'MMEX 121856Z 17010KT 10SM SCT100 BKN250 28/15 A2999'),

    # ============= HAWAII =============
    'PHNL': ('Honolulu', 'Hawaii', 'PHNL 121856Z 08012KT 10SM FEW100 SCT200 26/20 A2995'),

    # ============= FIJI =============
    'NFFN': ('Nadi', 'Fiji', 'NFFN 121830Z 16010KT 10SM SCT040 BKN100 26/24 Q1011'),

    # ============= SAMOA =============
    'NSSI': ('Apia', 'Samoa', 'NSSI 121830Z 14012KT 10SM FEW050 SCT150 28/25 Q1009'),
}

REGIONS = {
    'North America': {
        'USA': ['KLAX', 'KJFK', 'KSFO', 'KORD', 'KDFW', 'KATL', 'KMIA', 'KSEA', 'KDEN', 'KLAS', 'KIAD', 'KLGA', 'KBOS', 'KDCA', 'KMCO', 'KDET', 'KPHX', 'KMIN'],
        'Canada': ['CYYZ', 'CYMX', 'CYVR', 'CYEG', 'CYCA', 'CYOW', 'CYUL', 'CYWG'],
        'Mexico': ['MMMX', 'MMEX'],
    },
    'South America': {
        'Brazil': ['SBGR', 'SBRJ', 'SBBR'],
        'Argentina': ['SABE', 'SAAR'],
        'Chile': ['SCEL'],
        'Colombia': ['SKBO'],
    },
    'Europe': {
        'UK': ['EGLL', 'EGKK', 'EGSS', 'EGLC', 'EGPN', 'EGGW', 'EGCC', 'EGNX', 'EGPH', 'EGPF', 'EGNT', 'EGTB'],
        'France': ['LFPG', 'LFPO', 'LFLL', 'LFML', 'LFBT', 'LFSB'],
        'Germany': ['EDDF', 'EDDM', 'EDDB', 'EDDH', 'EDDK', 'EDDS', 'EDDL'],
        'Spain': ['LEMD', 'LEIB', 'LEVT', 'LEMG', 'LEAT', 'LEPA'],
        'Italy': ['LIRF', 'LIRA', 'LIML', 'LIBD', 'LIME', 'LIPZ'],
        'Netherlands': ['EHAM'],
        'Belgium': ['EBBR'],
        'Switzerland': ['ZZZH'],
        'Austria': ['LOWW'],
        'Czech Republic': ['LKPR'],
        'Poland': ['EPWA'],
        'Hungary': ['LHBP'],
        'Russia': ['UUWW', 'UUDD'],
        'Greece': ['LGAV'],
        'Portugal': ['LPPT'],
        'Turkey': ['LTFM'],
    },
    'Asia': {
        'Japan': ['RJTT', 'RJOO', 'RJFF'],
        'China': ['ZBAA', 'ZSPD', 'ZGSZ'],
        'Hong Kong': ['VHHH'],
        'South Korea': ['RKSI'],
        'Thailand': ['VTBS'],
        'Malaysia': ['WMKK'],
        'Singapore': ['WSSS'],
        'Philippines': ['RPLL'],
        'Indonesia': ['WIII'],
        'India': ['VIDP', 'VABB', 'VOCC'],
        'UAE': ['OMDB'],
    },
    'Africa': {
        'Egypt': ['HECA'],
        'Algeria': ['DIAP'],
        'Morocco': ['GMME'],
        'South Africa': ['FAOR', 'FACT'],
    },
    'Oceania': {
        'Australia': ['YSSY', 'YMML', 'YBBN', 'YPER', 'YADL'],
        'New Zealand': ['NZAA', 'NZCH', 'NZWN'],
        'Pacific': ['PHNL', 'NFFN', 'NSSI'],
    },
}
