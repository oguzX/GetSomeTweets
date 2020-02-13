# dict = ['Trakya']


dictionary = {
    'Organization':{
        'tag':'Organization',
        'words':[
            'edirne belediye başkanlığı',
            'disk trakya bölge temsilciliği',
            'bahçeşehir koleji bilim ve teknoloji lisesi',
            'denizlispor',
            'fenerbahçe',
            'osmanlı devleti',
            'galatasaray',
            'ak parti edirne il gençlik kolları başkanlığı',
            'kadın emek pazarı',
            'okul aile birliği',
            'keşan satranç şenliği',
            'kadın kolektifi',
            'fetö',
            'kariyer ve marka etkinliği trakya plus',
            'trakya tarımsal araştırma enstitüsü',
            'chp',
            'edirne yağ',
            'kalkınma ajansı'
        ]
    },
    'Location':{
        'tag':'Location',
        'words':[
            'edirne',
            'selimiye camii',
            'aydın',
            'mersin',
            'merkez',
            'i̇stanbul',
            'ankara',
            'bolu',
            'kars',
            'muğla',
            'izmir',
            'hatay',
            'gümüşhane',
            'trabzon',
            'kırklareli',
            'çerkezköy',
            'trakya',
            'silivri',
            'rumeli hisarı',
            'saray',
            'çorlu',
            'kırklareli',
            'avrupa',
            'karaağaç',
            'elazığ',
            'almanya',
            'kktc',
            'yunanistan',
            'yozgat',
            'meriç nehri',
            'tekirdağ',
            'saraçlar caddesi',
            'cebelitarık boğazı',
            'üç şerefeli cami',
            'anıtkabirde',
            'beylerbeyi cami',
            'edirne eski sarayı',
            'tem akşemsettin viyadüğü',
            'tunceli',
            'trakya üniversitesi eğitim fakültesi ',
            'd100',
            'tem istoç'
        ]
    },
    'Gender':{
        'tag':'Gender',
        'words':[
            'kadın',
            'erkek'
        ]
    },
    'SpecialName':{
        'tag':'Person',
        'words':[
            'atatürk',
            'Süleyman Seba',
            'recep tayyip erdoğan',
            'recep gürkan',
            'emre',
            'selahattin demirtaş',
            'enver paşa',
            'fevzi pekcanlı',
            'gedik ahmed paşa',
            'sezai güler',
            'sultan 2. mehmed',
            'fatih',
            'ekrem canalp',
            'hidayet',
            'ekrem i̇mamoğlu',
            'nevzat bilgic',
            'olgun birbey şahinbaş',
            'arzu çerkezoğlu',
            'mimar sinan',
            'i̇smail güner'

        ]
    },
    'Date':{
        'tag':'Date',
        'words':[
            'aralik',
            'ocak',
            'subat',
            'mart',
            'nisan',
            'mayis',
            'haziran',
            'temmuz',
            'agustos',
            'eylul',
            'ekim',
            'kasim',
            'çarşamba'

        ]
    },
    'Numeric':{
      'tag':'Numeric'
    },
    'banned':{
        'tag':'Banned',
        'words':[
            've',
            'veya'
        ]
    },
    'Unknown':{
        'tag':'unknown'
    },
    'Rules':{
        'tag':'rules',
        'words':{
            'Dr':{
                'get':'after',
                'length':1
            },
            'Sn':{
                'get':'after',
                'length':1
            },
        }
    }
}