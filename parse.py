# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

def parseStringAdi(string):
    """
    This function recieving string from adi-file, and parse it. Function returning result in Phyton dictionary type, where key - it key from ADI-tag, 		value - information from ADI
    """

    # print(len(string.decode('utf-8')))
    counter = 0
    name = ''
    digitInTagString = ''
    digitInTagDigit = 0
    inTag = ''
    tags = {}
    counterChar = 0
    for i in string:
        try:
            counter = counter + 1;
            if i == '<':
                counterChar = counter
                while string[counterChar] != ':':
                    name = name + string[counterChar]
                    if name == 'EOR':
                        break
                    counterChar = counterChar + 1
                if string[counterChar] == ':':
                    counterChar = counterChar + 1
                    while string[counterChar] != '>':
                        digitInTagString = digitInTagString + string[counterChar]
                        counterChar = counterChar + 1
                # digitInTagDigit=int(digitInTagString)
                while string[counterChar] != '<':
                    if string[counterChar] != ">":
                        inTag = inTag + string[counterChar]
                    if counterChar == len(string) - 1:
                        break
                    else:
                        counterChar = counterChar + 1
                tags.update({name: inTag})
                name = ''
                inTag = ''
        except Exception:
            print("Exception in parse")
    return tags


## Poles which used in programm (they will found into dictionary from file)
def getAllRecord(poles, filename, key=''):
    # poles=['QSO_DATE','TIME_ON','FREQ','CALL','MODE','RST_RCVD','RST_SENT','NAME','QTH']

    key = 0
    allrecord = []
    if key == "import":
        with open(filename, 'r') as fin:
            lines = fin.readlines()
            with open('import_tmp.adi', 'w', encoding='iso-8859-2') as fout:
                fout.writelines(lines)
            filename = 'import_tmp.adi'
    else:
        pass

    file = open(filename, 'r', encoding="utf-8", errors='ignore')

    iterator_string_file = 0
    iterator_records = 0
    for string in file:  # read string from file

        ## For example using string
        # string='<BAND:3>20M <CALL:6>DL1BCL <CONT:2>EU <CQZ:2>14 <DXCC:3>230 <FREQ:9>14.000000 <ITUZ:2>28 <MODE:3>SSB <OPERATOR:6>UR4LGA <PFX:3>DL1 <QSLMSG:19>TNX For QSO TU 73!. <QSO_DATE:8:D>20131011 <TIME_ON:6>184700 <RST_RCVD:2>57 <RST_SENT:2>57 <TIME_OFF:6>184700 <eQSL_QSL_RCVD:1>Y <APP_LOGGER32_QSO_NUMBER:1>1 <EOR>'
        iterator_string_file += 1
        if key == 1 and string != '\n':    # checked key by ready parsing processing (1-ready) and cheked on empty string
            iterator_records += 1
            tags = parseStringAdi(string)  # calling function parse processing/ Function returning all tags from file in Python-Dictionary object

            if tags:

                tags.update({'string_in_file': str(iterator_string_file)})
                tags.update({'records_number': str(iterator_records)})
                for i in range(len(poles)):
                    if poles[i] in tags.keys():  # chek all poles in dictionary
                        pass
                    else:
                        tags.update({poles[i]: ' '})

                allrecord.append(tags)  # add all dictionary in List-object. This List using for found input call in base of QSO (repeat qso)

        # print ('%10s %5s %10s %16s %4s %6s %5s %15s %15s' % (tags.get('QSO_DATE'), tags.get('TIME_ON'),tags.get('FREQ'),tags.get('CALL'),tags.get('MODE'), tags.get('RST_RCVD'),tags.get('RST_SENT'),tags.get('NAME'),tags.get('QTH')))

        if string == "<EOH>\n":  # if we went to end by text header in ADI file (<EOH>) - set key by ready parsing in value = 1
            key = 1
    #print (allrecord)
    file.close()
    #print(allrecord)
    return allrecord
# call=''
# rangevalue=len(allrecord) # How many QSO in base
# print ('\n\n\nAll QSO: '+ str(rangevalue) + '\n')


# call=raw_input('enter CALL: ').upper()
# print ('%10s %5s %10s %16s %8s %8s %8s %15s %15s' % ('QSO_DATE', 'TIME', 'FREQ', 'CALL',
#			'MODE', 'RST_RCVD', 'RST_SENT',	'NAME', 'QTH')
#		   )

# for i in range(rangevalue):

# if allrecord[i]['CALL'].strip() == call :
#	print ('%10s %5s %10s %16s %8s %8s %8s %15s %15s' % (allrecord[i]['QSO_DATE'],
#				allrecord[i]['TIME_ON'], allrecord[i]['FREQ'], allrecord[i]['CALL'],
#				allrecord[i]['MODE'], allrecord[i]['RST_RCVD'], allrecord[i]['RST_SENT'],
#				allrecord[i]['NAME'], allrecord[i]['QTH'])
#			   )
