# -*- coding: utf-8 -*-

import sys
import getopt

__doc__ = """
Esto es un ejemplo de script
"""

_IDIOMAS = {
    'af_ZA': 'Afrikaans_South Africa',
    'sq_AL': 'Albanian_Albania',
    'ar_SA': 'Arabic_Saudi Arabia',
    'eu_ES': 'Basque_Spain',
    'be_BY': 'Belarusian_Belarus',
    'bs_BA': 'Bosnian_Bosnia and Herzegovina',
    'bg_BG': 'Bulgarian_Bulgaria',
    'ca_ES': 'Catalan_Spain',
    'hr_HR': 'Croatian_Croatia',
    'zh_CN': 'Chinese_China',
    'zh_TW': 'Chinese_Taiwan',
    'cs_CZ': 'Czech_Czech Republic',
    'da_DK': 'Danish_Denmark',
    'nl_NL': 'Dutch_Netherlands',
    'et_EE': 'Estonian_Estonia',
    'fa_IR': 'Farsi_Iran',
    'ph_PH': 'Filipino_Philippines',
    'fi_FI': 'Finnish_Finland',
    'fr_FR': 'French_France',
    'ga': 'Scottish Gaelic',
    'gl_ES': 'Galician_Spain',
    'ka_GE': 'Georgian_Georgia',
    'de_DE': 'German_Germany',
    'el_GR': 'Greek_Greece',
    'gu': 'Gujarati_India',
    'he_IL': 'Hebrew_Israel',
    'hi_IN': 'Hindi',
    'hu': 'Hungarian_Hungary',
    'is_IS': 'Icelandic_Iceland',
    'id_ID': 'Indonesian_indonesia',
    'it_IT': 'Italian_Italy',
    'ja_JP': 'Japanese_Japan',
    'kn_IN': 'Kannada',
    'km_KH': 'Khmer',
    'ko_KR': 'Korean_Korea',
    'lo_LA': 'Lao_Laos',
    'lt_LT': 'Lithuanian_Lithuania',
    'lat': 'Latvian_Latvia',
    'ml_IN': 'Malayalam_India',
    'mi_NZ': 'Maori',
    'mn': 'Cyrillic_Mongolian',
    'no_NO': 'Norwegian_Norway',
    'nn_NO': 'Norwegian-Nynorsk_Norway',
    'pl': 'Polish_Poland',
    'pt_PT': 'Portuguese_Portugal',
    'pt_BR': 'Portuguese_Brazil',
    'ro_RO': 'Romanian_Romania',
    'ru_RU': 'Russian_Russia',
    'sr_CS': 'Serbian (Cyrillic)_Serbia and Montenegro',
    'sk_SK': 'Slovak_Slovakia',
    'sl_SI': 'Slovenian_Slovenia',
    'es_ES': 'Spanish_Spain',
    'sv_SE': 'Swedish_Sweden',
    'ta_IN': 'English_Australia',
    'th_TH': 'Thai_Thailand',
    'tr_TR': 'Turkish_Turkey',
    'uk_UA': 'Ukrainian_Ukraine',
    'vi_VN': 'Vietnamese_Viet Nam',
    'tlh_TLH': 'Klingon',
}

def main():
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hl", ["help","lang"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
        if o in ("-l", "--lang"):
            if args:
                for arg in args:
                    if arg in _IDIOMAS:
                        print "%s (%s)" % (_IDIOMAS[arg], arg)
                    else:
                        print "ERROR: '%s' no es un idioma reconocido" % arg
            else:
                print _IDIOMAS.keys()
            sys.exit(0)
    # process arguments
    for arg in args:
        process(arg) # process() is defined elsewhere

if __name__ == "__main__":
    main()
