from __future__ import annotations

"""Exact certificate (theorum/129, extended by theorum/130): THE TIṄ RULE-TABLE
ENGINE — the verbal counterpart of theorum/125's table.  One table in which
every sūtra of the bhvādi present system and of its lṛṭ / luṭ / āśīrliṅ / luṅ is a record (number, guard, action), one driver that
applies the table in phase order (lakāra → tiṅ and the lakāra-specific
substitutions → the aṅga (vikaraṇa, guṇa, augments, liṅ's yāsuṭ / sīyuṭ) →
junction sandhi → tripādī), and the certified present-system paradigms of
theorum/64, 95, 96 (bhū, gam, nī parasmaipada in laṭ, laṅ, loṭ, vidhiliṅ) and
theorum/66, 99 (edh, labh ātmanepada in the same four lakāras) as its
ORACLES: 5 roots × 4 lakāras × 9 cells = 180 cells, every row shown
load-bearing on at least one cell.

The affixes come from theorum/82's it-saṁjñā (3.4.78 read through 1.3.2–1.3.9);
the guards read only the state (root, vikaraṇa, affix, lakāra, pada, code).
"""

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Callable

from proof_lab.paninian_it_samjna_compiled import its
from proof_lab.sup_rule_table_engine import GUNA as _GUNA, V, tok

GUNA = {**_GUNA, "ṝ": "ar"}

SOURCES = {
    "3.2.123": "vartamāne laṭ", "3.2.111": "anadyatane laṅ", "3.3.139": "liṅnimitte lṛṅ kriyātipattau", "3.3.162": "loṭ ca", "3.3.161": "vidhinimantraṇāmantraṇādhīṣṭasaṁpraśnaprārthaneṣu liṅ",
    "3.4.77": "lasya", "3.4.78": "tiptasjhisipthasthamibvasmas tātāṁjhathāsāthāṁdhvamiḍvahimahiṅ", "1.3.78": "śeṣāt kartari parasmaipadam", "1.3.12": "anudāttaṅita ātmanepadam",
    "3.1.68": "kartari śap", "3.4.113": "tiṅśitsārvadhātukam", "1.2.4": "sārvadhātukamapit",
    "3.4.79": "ṭita ātmanepadānāṁ ṭere", "3.4.80": "thāsasse", "3.4.85": "loṭo laṅvat", "3.4.86": "eruḥ", "3.4.87": "serhyapicca", "3.4.89": "merniḥ", "3.4.90": "āmetaḥ",
    "3.4.91": "savābhyāṁ vāmau", "3.4.92": "āḍuttamasya picca", "3.4.93": "eta ai", "3.4.99": "nityaṁ ṅitaḥ", "3.4.100": "itaśca", "3.4.101": "tasthasthamipāṁ tāṁtaṁtāmaḥ",
    "3.4.102": "liṅassīyuṭ", "3.4.103": "yāsuṭ parasmaipadeṣūdātto ṅicca", "3.4.105": "jhasya ran", "3.4.106": "iṭo't", "3.4.108": "jherjus", "7.1.3": "jho'ntaḥ",
    "7.3.77": "iṣugamiyamāṁ chaḥ", "6.1.73": "che ca", "7.3.84": "sārvadhātukārdhadhātukayoḥ", "6.1.78": "eco'yavāyāvaḥ", "6.1.65": "ṇo naḥ",
    "6.4.71": "luṅlaṅlṛṅkṣvaḍudāttaḥ", "6.4.72": "āḍajādīnām", "6.1.90": "āṭaśca", "7.3.101": "ato dīrgho yañi", "6.4.105": "ato heḥ",
    "7.2.79": "liṅaḥ salopo'nantyasya", "7.2.80": "ato yeyaḥ", "7.2.81": "āto ṅitaḥ",
    "6.1.87": "ādguṇaḥ", "6.1.88": "vṛddhireci", "6.1.97": "ato guṇe", "6.1.101": "akaḥ savarṇe dīrghaḥ", "6.1.66": "lopo vyorvali",
    "3.3.13": "lṛṭ śeṣe ca", "3.3.15": "anadyatane luṭ", "3.2.110": "luṅ", "3.4.116": "liṅāśiṣi", "3.4.114": "ārdhadhātukaṁ śeṣaḥ", "3.4.104": "kidāśiṣi",
    "3.1.33": "syatāsī lṛluṭoḥ", "3.1.43": "cli luṅi", "3.1.44": "cleḥ sic", "2.4.77": "gātisthāghupābhūbhyaḥ sicaḥ parasmaipadeṣu", "3.1.55": "puṣādidyutādyḷditaḥ parasmaipadeṣu",
    "2.4.85": "luṭaḥ prathamasya ḍāraurasaḥ", "3.4.109": "sijabhyastavidibhyaśca", "7.1.5": "ātmanepadeṣvanataḥ", "3.4.107": "suṭ tithoḥ",
    "7.2.35": "ārdhadhātukasyeḍ valādeḥ", "7.2.10": "ekāca upadeśe'nudāttāt", "7.2.58": "gameriṭ parasmaipadeṣu", "7.2.1": "sici vṛddhiḥ parasmaipadeṣu", "7.3.96": "astisico'pṛkte", "6.4.88": "bhuvo vugluṅliṭoḥ",
    "8.2.26": "jhalo jhali", "8.2.40": "jhaṣastathordho'dhaḥ", "8.4.53": "jhalāṁ jaś jhaśi", "8.4.55": "khari ca", "6.4.143": "ṭeḥ", "7.4.50": "tāsastyorlopaḥ", "7.4.51": "ri ca", "7.4.52": "ha eti",
    "8.2.29": "skoḥ saṁyogādyorante ca", "8.3.59": "ādeśapratyayayoḥ", "8.3.55": "apadāntasya mūrdhanyaḥ", "8.4.41": "ṣṭunā ṣṭuḥ",
    "3.2.115": "parokṣe liṭ", "3.4.115": "liṭ ca", "3.4.82": "parasmaipadānāṁ ṇalatususthalathusaṇalvamāḥ", "1.2.5": "asaṁyogālliṭ kit", "1.1.56": "sthānivadādeśo'nalvidhau",
    "6.1.8": "liṭi dhātoranabhyāsasya", "6.1.1": "ekāco dve prathamasya", "6.1.4": "pūrvo'bhyāsaḥ", "7.4.59": "hrasvaḥ", "7.4.62": "kuhoścuḥ", "7.4.66": "urat", "7.4.73": "bhavateraḥ", "8.4.54": "abhyāse carca",
    "7.2.13": "kṛsṛbhṛvṛstudrusruśruvo liṭi", "7.2.115": "aco ñṇiti", "7.2.116": "ata upadhāyāḥ", "6.4.98": "gamahanajanakhanaghasāṁ lopaḥ kṅityanaṅi", "6.1.77": "iko yaṇaci",
    "3.1.25": "satyāpapāśarūpavīṇātūlaślokasenālomatvacavarmavarṇacūrṇacurādibhyo ṇic", "3.1.32": "sanādyantā dhātavaḥ", "3.1.69": "divādibhyaḥ śyan", "3.1.73": "svādibhyaḥ śnuḥ", "3.1.74": "śruvaḥ śṛ ca", "3.1.77": "tudādibhyaḥ śaḥ",
    "3.1.79": "tanādikṛñbhya uḥ", "3.1.81": "kryādibhyaḥ śnā", "1.3.72": "svaritañitaḥ kartrabhiprāye kriyāphale", "6.1.64": "dhātvādeḥ ṣaḥ saḥ", "7.3.86": "pugantalaghūpadhasya ca", "8.2.77": "hali ca", "7.3.74": "śamāmaṣṭānāṁ dīrghaḥ śyani", "7.3.80": "pvādīnāṁ hrasvaḥ",
    "6.4.110": "ata ut sārvadhātuke", "6.4.108": "nityaṁ karoteḥ", "6.4.107": "lopaścāsyānyatarasyāṁ mvoḥ", "6.4.77": "aci śnudhātubhruvāṁ yvoriyaṅuvaṅau", "6.4.87": "huśnuvoḥ sārvadhātuke", "6.4.112": "śnā'bhyastayorātaḥ", "6.4.113": "ī halyaghoḥ",
    "8.4.1": "raṣābhyāṁ no ṇaḥ samānapade", "8.4.2": "aṭkupvāṅnumvyavāye'pi",
    "2.4.72": "adiprabhṛtibhyaḥ śapaḥ", "2.4.75": "juhotyādibhyaḥ śluḥ", "6.1.10": "ślau", "3.1.78": "rudhādibhyaḥ śnam", "1.1.47": "midaco'ntyātparaḥ", "6.4.111": "śnasorallopaḥ", "7.1.4": "adabhyastāt", "7.1.58": "idito num dhātoḥ", "6.4.23": "śnānnalopaḥ",
    "8.2.38": "dadhastathośca", "8.2.30": "coḥ kuḥ", "8.3.24": "naścāpadāntasya jhali", "8.4.58": "anusvārasya yayi parasavarṇaḥ", "1.1.20": "dādhā ghvadāp",
    "3.1.82": "stanbhustunbhuskanbhuskunbhuskuñbhyaḥ śnuśca", "6.4.24": "aniditāṁ hala upadhāyāḥ kṅiti", "7.3.79": "jñājanorjā", "6.1.16": "grahijyāvayivyadhivaṣṭivicativṛścatipṛcchatibhṛjjatīnāṁ ṅiti ca", "1.1.45": "igyaṇaḥ samprasāraṇam", "6.1.108": "samprasāraṇācca",
    "8.4.40": "stoḥ ścunā ścuḥ", "8.4.44": "śāt", "8.4.39": "kṣubhnā''diṣu ca",
    "7.3.89": "uto vṛddhirluki hali", "7.3.90": "ūrṇotervibhāṣā", "7.3.95": "turustuśamyamaḥ sārvadhātuke", "6.4.81": "iṇo yaṇ", "6.4.82": "eranekāco'saṁyogapūrvasya", "7.4.60": "halādiḥ śeṣaḥ",
    "7.4.75": "nijāṁ trayāṇāṁ guṇaḥ ślau", "7.4.76": "bhṛñāmit", "7.4.77": "artipipartyośca", "7.1.102": "udoṣṭhyapūrvasya", "8.2.41": "ṣaḍhoḥ kaḥ si", "8.3.57": "iṇkoḥ", "6.4.115": "bhiyo'nyatarasyām", "6.4.116": "jahāteśca",
    "6.1.6": "jakṣityādayaḥ ṣaṭ", "7.2.76": "rudādibhyaḥ sārvadhātuke", "7.2.77": "īśaḥ se", "7.2.78": "īḍajanordhve ca", "7.3.93": "bruva īṭ", "7.2.114": "mṛjervṛddhiḥ", "7.4.21": "śīṅaḥ sārvadhātuke guṇaḥ", "7.1.6": "śīṅo ruṭ",
    "6.4.34": "śāsa idaṅhaloḥ", "6.4.114": "iddaridrasya", "6.4.37": "anudāttopadeśavanatitanotyādīnāmanunāsika lopo jhali kṅiti", "7.3.54": "ho hanterñṇinneṣu", "8.2.36": "vraścabhrasjasṛjamṛjayajarājabhrājacchaśāṁ ṣaḥ",
    "8.3.60": "śāsivasighasīnāṁ ca", "8.2.31": "ho ḍhaḥ", "8.2.32": "dāderdhātorghaḥ", "8.2.37": "ekāco baśo bhaṣ jhaṣantasya sdhvoḥ", "8.3.13": "ḍho ḍhe lopaḥ", "6.3.111": "ḍhralope pūrvasya dīrgho'ṇaḥ",
    "7.3.83": "jusi ca", "7.3.100": "adaḥ sarveṣām", "6.1.96": "usyapadāntāt", "6.4.101": "hujhalbhyo herdhiḥ", "6.4.119": "ghvasoreddhāvabhyāsalopaśca", "3.1.83": "halaḥ śnaḥ śānajjhau", "6.4.106": "utaśca pratyayādasaṁyogapūrvāt",
    "6.4.109": "ye ca", "6.4.118": "lopo yi", "7.3.87": "nābhyastasyāci piti sārvadhātuke", "8.4.37": "padāntasya", "7.3.98": "rudaśca pañcabhyaḥ",   # 8.2.24 rāt sasya (theorum/139) withdrawn by theorum/143: the apṛkta s after r is 6.1.68's
    "8.2.23": "saṁyogāntasya lopaḥ", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayorvisarjanīyaḥ",
    # theorum/143: the third pass on the open lane
    "6.1.68": "halṅyābbhyo dīrghāt sutisyapṛktaṁ hal", "8.2.39": "jhalāṁ jaśo 'nte", "8.4.56": "vā 'vasāne", "8.2.73": "tipy anasteḥ", "8.2.74": "sipi dhāto rurvā", "8.2.25": "dhi ca",
    "6.4.36": "hanter jaḥ", "6.4.22": "asiddhavad atrābhāt", "7.3.88": "bhūsuvos tiṅi", "7.3.91": "guṇo 'pṛkte", "7.1.100": "ṝta id dhātoḥ", "1.4.2": "vipratiṣedhe paraṁ kāryam", "8.2.1": "pūrvatrāsiddham",
    # theorum/144: the Dhātupāṭha and the ārdhadhātuka lane
    "2.4.52": "aster bhūḥ", "2.4.53": "bruvo vaciḥ", "7.2.70": "ṛddhanoḥ sye", "6.1.50": "mīnātiminotidīṅāṁ lyapi ca", "6.1.45": "ādeca upadeśe 'śiti", "7.2.37": "graho 'liṭi dīrghaḥ",
    "7.2.44": "svaratisūtisūyatidhūñūdito vā", "7.2.57": "se 'sici kṛtacṛtacchṛdatṛdanṛtaḥ",
    "7.4.25": "akṛtsārvadhātukayor dīrghaḥ", "7.4.28": "riṅ śayagliṅkṣu", "7.4.29": "guṇo 'rtisaṁyogādyoḥ", "7.3.85": "jāgro 'viciṇṇalṅitsu", "6.4.66": "ghumāsthāgāpājahātisāṁ hali", "6.4.67": "er liṅi",
    # theorum/145: liṭ at breadth and lṛṅ
    "3.4.81": "liṭas tajhayor eśirec", "3.1.35": "kāspratyayād ām amantre liṭi", "3.1.36": "ijādeś ca gurumato 'nṛcchaḥ", "3.1.37": "dayāyāsaś ca", "3.1.38": "uṣavidajāgṛbhyo 'nyatarasyām", "3.1.39": "bhīhrībhṛhuvāṁ śluvac ca", "3.1.40": "kṛñ cānuprayujyate liṭi",
    "7.4.70": "ata ādeḥ", "7.4.72": "aśnoteś ca", "7.4.71": "tasmān nuḍ dvihalaḥ", "6.4.78": "abhyāsasyāsavarṇe", "7.4.69": "dīrgha iṇaḥ kiti", "7.4.61": "śarpūrvāḥ khayaḥ", "7.1.34": "āta au ṇalaḥ", "6.4.64": "āto lopa iṭi ca",
    "6.1.17": "liṭy abhyāsasyobhayeṣām", "7.4.67": "dyutisvāpyoḥ samprasāraṇam", "7.3.55": "abhyāsāc ca", "6.4.120": "ata ekahalmadhye 'nādeśāder liṭi", "6.4.121": "thali ca seṭi", "6.4.123": "rādho hiṁsāyām", "6.4.126": "na śasadadavādiguṇānām",
    "7.4.11": "ṛcchatyṝtām", "7.4.12": "śṝdṝprāṁ hrasvo vā", "7.2.61": "acas tāsvat thaly aniṭo nityam", "7.2.62": "upadeśe 'tvataḥ", "7.2.63": "ṛto bhāradvājasya", "2.4.40": "liṭy anyatarasyām", "7.3.58": "vibhāṣā ceḥ",
    # theorum/146: luṅ at breadth
    "8.2.28": "iṭa īṭi", "7.2.3": "vadavrajahalantasyācaḥ", "7.2.4": "neṭi", "7.2.5": "hmyantakṣaṇaśvasajāgṛṇiśvyeditām", "7.2.7": "ato halāder laghoḥ", "3.1.57": "irito vā", "3.1.52": "asyativaktikhyātibhyo 'ṅ", "7.4.20": "vaca um",
    "2.4.37": "luṅsanor ghasḷ", "3.1.45": "śala igupadhād aniṭaḥ ksaḥ", "7.3.73": "lug vā duhadihalihaguhām ātmanepade dantye", "2.4.45": "iṇo gā luṅi", "7.2.73": "yamaramanamātāṁ sak ca", "8.2.27": "hrasvād aṅgāt", "1.2.17": "sthāghvor ic ca",
    "3.1.48": "ṇiśridrusrubhyaḥ kartari caṅ", "7.3.72": "ksasyāci", "3.4.110": "ātaḥ", "7.2.72": "stusudhūñbhyaḥ parasmaipadeṣu", "6.1.11": "caṅi", "7.4.1": "ṇau caṅy upadhāyā hrasvaḥ", "7.4.93": "sanvallaghuni caṅpare 'naglope", "7.4.94": "dīrgho laghoḥ", "1.2.11": "liṅsicāv ātmanepadeṣu",
    "6.4.24": "aniditāṁ hala upadhāyāḥ kṅiti", "2.4.42": "hano vadha liṅi", "6.4.48": "ato lopaḥ", "6.1.15": "vacisvapiyajādīnāṁ kiti", "6.4.2": "halaḥ", "8.3.78": "iṇaḥ ṣīdhvaṁluṅliṭāṁ dho 'ṅgāt", "8.3.79": "vibhāṣeṭaḥ", "3.4.104": "kid āśiṣi", "6.4.51": "ṇer aniṭi", "1.2.11": "liṅsicāv ātmanepadeṣu", "1.2.12": "uś ca",
}

# 3.4.78 in upadeśa; theorum/82 reads the its (p by 1.3.3, ṭ of iṭ by 1.3.3, ṅ of mahiṅ marks the whole list)
TING_P = {"3s": "tip", "3d": "tas", "3p": "jhi", "2s": "sip", "2d": "thas", "2p": "tha", "1s": "mip", "1d": "vas", "1p": "mas"}
TING_A = {"3s": "ta", "3d": "ātām", "3p": "jha", "2s": "thās", "2d": "āthām", "2p": "dhvam", "1s": "iṭ", "1d": "vahi", "1p": "mahi"}
CODES = list(TING_P)
LAKARAS = ("laṭ", "laṅ", "loṭ", "liṅ", "lṛṭ", "luṭ", "āśīrliṅ", "luṅ", "liṭ", "lṛṅ")
LIT_P = {"tip": "a", "tas": "atus", "jhi": "us", "sip": "tha", "thas": "athus", "tha": "a", "mip": "a", "vas": "va", "mas": "ma"}   # 3.4.82 after 1.3.7 / 1.3.3 (ṇal → a, thal → tha)
NO_IT_LIT = {"kṛ", "sṛ", "bhṛ", "vṛ", "stu", "dru", "sru", "śru"}   # 7.2.13 kṛsṛbhṛvṛstudrusruśruvo liṭi
CU = {"k": "c", "kh": "ch", "g": "j", "gh": "jh", "ṅ": "ñ", "h": "j"}
DEASP = {"bh": "b", "ph": "p", "dh": "d", "th": "t", "gh": "g", "kh": "k", "jh": "j", "ch": "c", "ḍh": "ḍ", "ṭh": "ṭ"}
HRASVA = {"ā": "a", "ī": "i", "ū": "u", "ṝ": "ṛ", "e": "i", "ai": "i", "o": "u", "au": "u"}
YAN = {"i": "y", "ī": "y", "u": "v", "ū": "v", "ṛ": "r"}
NGIT_LAK = ("laṅ", "liṅ", "āśīrliṅ", "luṅ", "lṛṅ")      # the ṅit lakāras (3.4.100 itaś ca …; lṛṅ by 3.3.139)
VRDDHI = {"i": "ai", "ī": "ai", "u": "au", "ū": "au", "ṛ": "ār", "ṝ": "ār"}
KHAY = {"k", "kh", "c", "ch", "ṭ", "ṭh", "t", "th", "p", "ph"}
AM_LIT = {"cakāsṛ~", "edha~", "īśa~", "īḍa~", "īra~", "ṝ", "ūrṇuñ", "āsa~", "jāgṛ"}   # 3.1.35 (kās), 3.1.36 (the ijādi gurumat: edh, īś, īḍ, ūrṇu — the vārttika exempting ūrṇu is not read here: its cells are left), 3.1.37 (ās), 3.1.38 (jāgṛ, first alternative)
PUSHADI = {"śamu~", "tamu~", "damu~", "śramu~", "bhramu~", "kṣamu~", "klamu~", "madī~", "puṣa~", "śuṣa~", "tuṣa~", "duṣa~", "ruṣa~"}   # 3.1.55 puṣādi (the gaṇapāṭha's list; declared, the members in the table)
AM_SLU = {"ñibhī", "hrī", "ḍubhṛñ", "hu"}       # 3.1.39 bhīhrībhṛhuvāṁ śluvac ca
JHAL = {"k", "kh", "g", "gh", "c", "ch", "j", "jh", "ṭ", "ṭh", "ḍ", "ḍh", "t", "th", "d", "dh", "p", "ph", "b", "bh", "ś", "ṣ", "s", "h"}
PRESENT = ("laṭ", "laṅ", "loṭ", "liṅ")          # the śap lakāras of theorum/64–99
ARDHA_LAK = ("lṛṭ", "luṭ", "luṅ", "āśīrliṅ", "lṛṅ")   # the ārdhadhātuka lakāras other than liṭ (3.4.114)
TIT = ("laṭ", "loṭ", "lṛṭ", "luṭ", "liṭ")               # ṭit lakāras (3.4.79)
# ---- the Dhātupāṭha (theorum/144): ashtadhyayi.com's dhatu list as packaged with vidyut-prakriya 0.4.0 (MIT), pinned in the repository ----
DHATUPATHA = Path(__file__).resolve().parent.parent / "research" / "panini_grammar" / "DHATUPATHA.tsv"
DHATUPATHA_SHA256 = "bb2013ead0ea536dc7f887164c385c703cb0014ccf6e5af35b87e6d3049ba380"
_SLP = [("ai", "E"), ("au", "O"), ("kh", "K"), ("gh", "G"), ("ch", "C"), ("jh", "J"), ("ṭh", "W"), ("ḍh", "Q"), ("th", "T"), ("dh", "D"), ("ph", "P"), ("bh", "B"),
        ("ā", "A"), ("ī", "I"), ("ū", "U"), ("ṛ", "f"), ("ṝ", "F"), ("ḷ", "x"), ("ṅ", "N"), ("ñ", "Y"), ("ṭ", "w"), ("ḍ", "q"), ("ṇ", "R"), ("ś", "S"), ("ṣ", "z"), ("ṁ", "M"), ("ḥ", "H")]


def slp1(iast: str) -> str:
    out = iast
    for a, b in _SLP:
        out = out.replace(a, b)
    return out


def load_dhatupatha() -> dict[tuple[str, int], list[tuple[str, str]]]:
    """(accent-stripped SLP1 upadeśa, gaṇa) → [(code, upadeśa with accents)]; the accents are the Dhātupāṭha's own marks."""
    if not DHATUPATHA.exists():
        return {}
    by: dict[tuple[str, int], list[tuple[str, str]]] = {}
    for line in DHATUPATHA.read_text(encoding="utf-8").splitlines()[1:]:
        code, dh, _ = line.split("\t")
        by.setdefault((dh.replace("\\", "").replace("^", "").replace("~", ""), int(code.split(".")[0])), []).append((code, dh))
    return by


DHATU_BY = load_dhatupatha()


def dhatu_entry(up_root: str, gana: int):
    key = (slp1(up_root).replace("~", ""), gana)
    hits = DHATU_BY.get(key) or (DHATU_BY.get((key[0], 1)) if up_root == "śru" else None)   # śru is read in bhvādi; 3.1.74 gives it śnu
    return hits[0] if hits else None


def anudatta(up_root: str, gana: int) -> bool | None:
    """7.2.10 ekāca upadeśe 'nudāttāt: the root vowel carries the anudātta mark (\) in the upadeśa → aniṭ. None: no entry."""
    e = dhatu_entry(up_root, gana)
    if e is None:
        return None
    dh = e[1]
    return any(ch == "\\" and dh[i - 1] != "~" for i, ch in enumerate(dh) if i)   # the mark after the ~ it-vowel is the pada accent (1.3.12 / 1.3.72), not 7.2.10's


SET = {"bhū", "edh"}                             # the two seṭ roots theorum/130 declared; superseded by anudatta() (theorum/144), kept for the record
KHAR = {"k", "kh", "c", "ch", "ṭ", "ṭh", "t", "th", "p", "ph", "ś", "ṣ", "s"}
CAR = {"bh": "p", "b": "p", "dh": "t", "d": "t", "gh": "k", "g": "k", "jh": "c", "j": "c", "ḍh": "ṭ", "ḍ": "ṭ"}
JAS = {"bh": "b", "dh": "d", "gh": "g", "jh": "j", "ḍh": "ḍ", "ṣ": "ḍ"}
JHAS = {"bh", "gh", "dh", "jh", "ḍh"}
JAS_ALL = {**JAS, "k": "g", "kh": "g", "c": "j", "ch": "j", "ṭ": "ḍ", "ṭh": "ḍ", "t": "d", "th": "d", "p": "b", "ph": "b"}   # jhal → jaś (8.2.39 / 8.4.53); s before dhi is 8.2.25's
IN = set(V) - {"a", "ā"} | {"h", "y", "v", "r", "l"}   # iṇ
# roots in upadeśa (Dhātupāṭha), pada by 1.3.12 / 1.3.78: ṣ-it labh and anudātta edha~ are ātmanepadin
ROOTS = {"bhū": ("bhū", "P"), "gam": ("gamḷ~", "P"), "nī": ("ṇīñ", "P"), "edh": ("edha~", "A"), "labh": ("ḍulabhaṣ", "A"), "kṛ": ("ḍukṛñ", "U"),
         # theorum/132: the vikaraṇa classes (Dhātupāṭha upadeśa and gaṇa; pada U = ubhaya, the cell's pada is declared with the cell)
         "pac": ("ḍupacaṣ", "U"), "div": ("divu~", "P"), "siv": ("ṣivu~", "P"), "śam": ("śamu~", "P"), "tud": ("tuda~", "U"), "nud": ("ṇuda~", "U"), "cur": ("cura~", "U"),
         # theorum/133: adādi (śap-luk), juhotyādi (ślu), rudhādi (śnam)
         "ad": ("ada~", "P"), "as": ("asa~", "P"), "hu": ("hu", "P"), "dā": ("ḍudāñ", "U"), "dhā": ("ḍudhāñ", "U"),
         "rudh": ("rudhi~r", "U"), "bhid": ("bhidi~r", "U"), "ric": ("rici~r", "U"), "vic": ("vici~r", "U"), "kṣud": ("kṣudi~r", "U"), "chṛd": ("u~chṛdi~r", "U"), "tṛd": ("u~tṛdi~r", "U"), "kṛt": ("kṛtī~", "P"), "hiṁs": ("hisi~", "P"),
         "su": ("ṣuñ", "U"), "ci": ("ciñ", "U"), "śru": ("śru", "P"), "āp": ("āpḷ~", "P"), "śak": ("śakḷ~", "P"), "tan": ("tanu~", "U"), "krī": ("ḍukrīñ", "U"), "pū": ("pūñ", "U"), "lū": ("lūñ", "U")}
# theorum/134: the nasal classes on the grammar-verification branch's quoted 3s tables (research/panini_grammar/nasal_present): key → (upadeśa, gaṇa, pada, forms)
NASAL = {
    "si5": ("ṣiñ", 5, "P", {"3s": "sinoti"}), "mi5": ("ḍumiñ", 5, "P", {"3s": "minoti"}), "stṛ5": ("stṛñ", 5, "P", {"3s": "stṛṇoti"}), "stṛ5A": ("stṛñ", 5, "A", {"3s": "stṛṇute"}),
    "kṛ5": ("kṛñ", 5, "P", {"3s": "kṛṇoti"}), "kṛ5A": ("kṛñ", 5, "A", {"3s": "kṛṇute"}), "dhu5": ("dhuñ", 5, "P", {"3s": "dhunoti"}), "dhu5A": ("dhuñ", 5, "A", {"3s": "dhunute"}),
    "dhū5": ("dhūñ", 5, "P", {"3s": "dhūnoti"}), "dhū5A": ("dhūñ", 5, "A", {"3s": "dhūnute"}), "du5": ("ṭudu", 5, "P", {"3s": "dunoti"}), "rādh5": ("rādha~", 5, "P", {"3s": "rādhnoti"}),
    "sādh5": ("sādha~", 5, "P", {"3s": "sādhnoti"}), "aś5A": ("aśū~", 5, "A", {"3s": "aśnute", "3p": "aśnuvate"}), "stigh5A": ("ṣṭigha~", 5, "A", {"3s": "stighnute"}), "tik5": ("tika~", 5, "P", {"3s": "tiknoti"}),
    "tig5": ("tiga~", 5, "P", {"3s": "tignoti"}), "sagh5": ("ṣagha~", 5, "P", {"3s": "saghnoti"}), "dhṛṣ5": ("ñidhṛṣā~", 5, "P", {"3s": "dhṛṣṇoti"}), "dabh5": ("danbhu~", 5, "P", {"3s": "dabhnoti"}),
    "tṛp5": ("tṛpa~", 5, "P", {"3s": "tṛpnoti"}), "kṣi5": ("kṣi", 5, "P", {"3s": "kṣiṇoti"}),
    "san8": ("ṣaṇu~", 8, "P", {"3s": "sanoti"}), "san8A": ("ṣaṇu~", 8, "A", {"3s": "sanute"}), "kṣaṇ8": ("kṣaṇu~", 8, "P", {"3s": "kṣaṇoti"}), "kṣaṇ8A": ("kṣaṇu~", 8, "A", {"3s": "kṣaṇute"}),
    "kṣiṇ8": ("kṣiṇu~", 8, "P", {"3s": "kṣeṇoti"}), "van8A": ("vanu~", 8, "A", {"3s": "vanute"}), "man8A": ("manu~", 8, "A", {"3s": "manute"}),
    "prī9": ("prīñ", 9, "P", {"3s": "prīṇāti"}), "prī9A": ("prīñ", 9, "A", {"3s": "prīṇīte"}), "śrī9": ("śrīñ", 9, "P", {"3s": "śrīṇāti"}), "śrī9A": ("śrīñ", 9, "A", {"3s": "śrīṇīte"}), "mī9": ("mīñ", 9, "P", {"3s": "mīnāti"}),
    "si9": ("ṣiñ", 9, "P", {"3s": "sināti"}), "si9A": ("ṣiñ", 9, "A", {"3s": "sinīte"}), "sku9": ("skuñ", 9, "P", {"3s": "skunoti"}), "sku9A": ("skuñ", 9, "A", {"3s": "skunute"}),
    "stabh9": ("stanbhu~", 9, "P", {"3s": "stabhnoti"}), "stubh9": ("stunbhu~", 9, "P", {"3s": "stubhnoti"}), "skabh9": ("skanbhu~", 9, "P", {"3s": "skabhnoti"}), "skubh9": ("skunbhu~", 9, "P", {"3s": "skubhnoti"}),
    "yu9": ("yuñ", 9, "P", {"3s": "yunāti"}), "yu9A": ("yuñ", 9, "A", {"3s": "yunīte"}), "knū9": ("knūñ", 9, "P", {"3s": "knūnāti"}), "knū9A": ("knūñ", 9, "A", {"3s": "knūnīte"}), "drū9": ("drūñ", 9, "P", {"3s": "drūṇāti"}), "drū9A": ("drūñ", 9, "A", {"3s": "drūṇīte"}),
    "stṝ9": ("stṝñ", 9, "P", {"3s": "stṛṇāti"}), "stṝ9A": ("stṝñ", 9, "A", {"3s": "stṛṇīte"}), "kṝ9": ("kṝñ", 9, "P", {"3s": "kṛṇāti"}), "kṝ9A": ("kṝñ", 9, "A", {"3s": "kṛṇīte"}), "vṝ9": ("vṝñ", 9, "P", {"3s": "vṛṇāti"}), "vṝ9A": ("vṝñ", 9, "A", {"3s": "vṛṇīte"}),
    "dhū9": ("dhūñ", 9, "P", {"3s": "dhunāti"}), "dhū9A": ("dhūñ", 9, "A", {"3s": "dhunīte"}), "mṝ9": ("mṝ", 9, "P", {"3s": "mṛṇāti"}), "ṝ9": ("ṝ", 9, "P", {"3s": "ṛṇāti"}), "jyā9": ("jyā", 9, "P", {"3s": "jināti", "3d": "jinītaḥ"}),
    "lī9": ("lī", 9, "P", {"3s": "lināti"}), "vlī9": ("vlī", 9, "P", {"3s": "vlināti"}), "jñā9": ("jñā", 9, "P", {"3s": "jānāti"}), "bandh9": ("bandha~", 9, "P", {"3s": "badhnāti"}), "vṛ9A": ("vṛṅ", 9, "A", {"3s": "vṛṇīte"}),
    "manth9": ("mantha~", 9, "P", {"3s": "mathnāti"}), "granth9": ("grantha~", 9, "P", {"3s": "grathnāti"}), "kunth9": ("kuntha~", 9, "P", {"3s": "kuthnāti"}), "mṛd9": ("mṛda~", 9, "P", {"3s": "mṛdnāti"}), "mṛḍ9": ("mṛḍa~", 9, "P", {"3s": "mṛḍṇāti"}),
    "gudh9": ("gudha~", 9, "P", {"3s": "gudhnāti"}), "kuṣ9": ("kuṣa~", 9, "P", {"3s": "kuṣṇāti"}), "kṣubh9": ("kṣubha~", 9, "P", {"3s": "kṣubhnāti", "3d": "kṣubhnītaḥ", "3p": "kṣubhnanti"}), "nabh9": ("ṇabha~", 9, "P", {"3s": "nabhnāti"}),
    "tubh9": ("tubha~", 9, "P", {"3s": "tubhnāti"}), "kliś9": ("kliśū~", 9, "P", {"3s": "kliśnāti"}), "aś9": ("aśa~", 9, "P", {"3s": "aśnāti"}), "dhras9": ("u~dhrasa~", 9, "P", {"3s": "dhrasnāti"}), "iṣ9": ("iṣa~", 9, "P", {"3s": "iṣṇāti"}),
    "viṣ9": ("viṣa~", 9, "P", {"3s": "viṣṇāti"}), "pruṣ9": ("pruṣa~", 9, "P", {"3s": "pruṣṇāti"}), "pluṣ9": ("pluṣa~", 9, "P", {"3s": "pluṣṇāti"}), "puṣ9": ("puṣa~", 9, "P", {"3s": "puṣṇāti"}), "muṣ9": ("muṣa~", 9, "P", {"3s": "muṣṇāti"}),
    "khac9": ("khaca~", 9, "P", {"3s": "khacñāti"}), "grah9": ("graha~", 9, "P", {"3s": "gṛhṇāti", "3d": "gṛhṇītaḥ"}), "grah9A": ("graha~", 9, "A", {"3s": "gṛhṇīte"}),
}
# theorum/135: present_expansion — adādi u- / ā-roots and juhotyādi (research/panini_grammar/present_expansion: Kāśikā / Kaumudī anchors)
NASAL.update({
    "yu2": ("yu", 2, "P", dict(zip(CODES, "yauti yutaḥ yuvanti yauṣi yuthaḥ yutha yaumi yuvaḥ yumaḥ".split()))),
    "ru2": ("ru", 2, "P", {"3s": "rauti", "3p": "ruvanti"}), "tu2": ("tu", 2, "P", {"3s": "tauti"}), "nu2": ("ṇu", 2, "P", {"3s": "nauti"}), "kṣu2": ("ṭukṣu", 2, "P", {"3s": "kṣauti"}),
    "kṣṇu2": ("kṣṇu", 2, "P", {"3s": "kṣṇauti"}), "snu2": ("ṣṇu", 2, "P", {"3s": "snauti"}), "dyu2": ("dyu", 2, "P", {"3s": "dyauti"}),
    "ūrṇu2": ("ūrṇuñ", 2, "P", {"3s": "ūrṇauti", "3d": "ūrṇutaḥ", "3p": "ūrṇuvanti"}), "ūrṇu2A": ("ūrṇuñ", 2, "A", {"3s": "ūrṇute", "3p": "ūrṇuvate"}),
    "stu2": ("ṣṭuñ", 2, "P", {"3s": "stauti", "3p": "stuvanti", "2s": "stauṣi", "1s": "staumi"}), "stu2A": ("ṣṭuñ", 2, "A", {"3d": "stuvāte", "3p": "stuvate", "2s": "stuṣe", "2d": "stuvāthe", "2p": "studhve"}),
    "hnu2A": ("hnuṅ", 2, "A", {"3s": "hnute", "3d": "hnuvāte", "3p": "hnuvate"}),
    "yā2": ("yā", 2, "P", {"3d": "yātaḥ", "3p": "yānti"}), "vā2": ("vā", 2, "P", {"3s": "vāti"}), "bhā2": ("bhā", 2, "P", {"1d": "bhāvaḥ"}), "snā2": ("ṣṇā", 2, "P", {"3s": "snāti"}), "drā2": ("drā", 2, "P", {"3s": "drāti"}),
    "psā2": ("psā", 2, "P", {"3s": "psāti"}), "pā2": ("pā", 2, "P", {"3s": "pāti"}), "lā2": ("lā", 2, "P", {"3s": "lāti"}), "khyā2": ("khyā", 2, "P", {"3s": "khyāti"}), "mā2": ("mā", 2, "P", {"3d": "mātaḥ", "2d": "māthaḥ"}),
    "bhī3": ("ñibhī", 3, "P", {"3s": "bibheti", "3d": "bibhītaḥ", "3p": "bibhyati"}), "hrī3": ("hrī", 3, "P", {"3s": "jihreti", "3d": "jihrītaḥ", "3p": "jihriyati"}),
    "pṝ3": ("pṝ", 3, "P", {"3s": "piparti", "3d": "pipūrtaḥ", "3p": "pipurati", "2s": "piparṣi", "2p": "pipūrtha", "1s": "piparmi", "1d": "pipūrvaḥ", "1p": "pipūrmaḥ"}),
    "pṛ3": ("pṛ", 3, "P", {"3s": "piparti", "3d": "pipṛtaḥ", "3p": "piprati", "2s": "piparṣi", "1s": "piparmi"}),
    "bhṛ3": ("ḍubhṛñ", 3, "P", dict(zip(CODES, "bibharti bibhṛtaḥ bibhrati bibharṣi bibhṛthaḥ bibhṛtha bibharmi bibhṛvaḥ bibhṛmaḥ".split()))),
    "bhṛ3A": ("ḍubhṛñ", 3, "A", dict(zip(CODES, "bibhṛte bibhrāte bibhrate bibhṛṣe bibhrāthe bibhṛdhve bibhre bibhṛvahe bibhṛmahe".split()))),
    "mā3A": ("māṅ", 3, "A", dict(zip(CODES, "mimīte mimāte mimate mimīṣe mimāthe mimīdhve mime mimīvahe mimīmahe".split()))),
    "hā3A": ("o~hāṅ", 3, "A", {"3s": "jihīte", "3d": "jihāte", "3p": "jihate"}), "hā3": ("o~hāk", 3, "P", {"3s": "jahāti", "3d": "jahītaḥ", "3p": "jahati"}),
    "nij3": ("ṇiji~r", 3, "P", dict(zip(CODES, "nenekti neniktaḥ nenijati nenekṣi nenikthaḥ neniktha nenejmi nenijvaḥ nenijmaḥ".split()))),
    "nij3A": ("ṇiji~r", 3, "A", {"3s": "nenikte", "3d": "nenijāte", "3p": "nenijate", "2s": "nenikṣe", "2d": "nenijāthe", "1s": "nenije", "1p": "nenijmahe"}),
    "vij3": ("viji~r", 3, "P", {"3s": "vevekti", "2s": "vevekṣi"}), "vij3A": ("viji~r", 3, "A", {"3s": "vevikte"}),
    "viṣ3": ("viṣḷ~", 3, "P", {"3s": "veveṣṭi", "2s": "vevekṣi", "2d": "veviṣṭhaḥ", "2p": "veviṣṭha"}), "viṣ3A": ("viṣḷ~", 3, "A", {"3s": "veviṣṭe"}),
})
NASAL.update({   # from research/panini_grammar/lexical_present (the two i-roots of adādi)
    "i2": ("iṇ", 2, "P", dict(zip(CODES, "eti itaḥ yanti eṣi ithaḥ itha emi ivaḥ imaḥ".split()))),
    "vī2": ("vī", 2, "P", {"3s": "veti", "3d": "vītaḥ", "3p": "viyanti", "2s": "veṣi", "1s": "vemi"}),
})
NASAL.update({   # theorum/136: the adādi consonant roots (research/panini_grammar/lexical_present: Kāśikā / Kaumudī anchors)
    "han2": ("hana~", 2, "P", dict(zip(CODES, "hanti hataḥ ghnanti haṁsi hathaḥ hatha hanmi hanvaḥ hanmaḥ".split()))),
    "dviṣ2": ("dviṣa~", 2, "P", {"3s": "dveṣṭi"}), "dviṣ2A": ("dviṣa~", 2, "A", {"3s": "dviṣṭe"}),
    "duh2": ("duha~", 2, "P", {"3s": "dogdhi", "3d": "dugdhaḥ", "3p": "duhanti", "2s": "dhokṣi", "2d": "dugdhaḥ", "2p": "dugdha", "1d": "duhvaḥ", "1p": "duhmaḥ"}),
    "duh2A": ("duha~", 2, "A", dict(zip(CODES, "dugdhe duhāte duhate dhukṣe duhāthe dhugdhve duhe duhvahe duhmahe".split()))),
    "dih2": ("diha~", 2, "P", {"3s": "degdhi"}),
    "lih2": ("liha~", 2, "P", {"3s": "leḍhi", "3d": "līḍhaḥ", "3p": "lihanti", "2s": "lekṣi", "2d": "līḍhaḥ", "2p": "līḍha", "1d": "lihvaḥ", "1p": "lihmaḥ"}),
    "lih2A": ("liha~", 2, "A", {"3s": "līḍhe", "3d": "lihāte", "3p": "lihate", "2s": "likṣe", "2p": "līḍhve", "1s": "lihe", "1d": "lihvahe"}),
    "vac2": ("vaca~", 2, "P", {"3s": "vakti", "3d": "vaktaḥ", "3p": "vacanti", "2p": "vaktha", "1p": "vacmaḥ"}),
    "brū2": ("brūñ", 2, "P", dict(zip(CODES, "bravīti brūtaḥ bruvanti bravīṣi brūthaḥ brūtha bravīmi brūvaḥ brūmaḥ".split()))), "brū2A": ("brūñ", 2, "A", {"3s": "brūte", "3d": "bruvāte", "3p": "bruvate"}),
    "śās2": ("śāsu~", 2, "P", dict(zip(CODES, "śāsti śiṣṭaḥ śāsati śāssi śiṣṭhaḥ śiṣṭha śāsmi śiṣvaḥ śiṣmaḥ".split()))),
    "mṛj2": ("mṛjū~", 2, "P", {"3s": "mārṣṭi", "3d": "mṛṣṭaḥ", "3p": "mṛjanti", "2d": "mṛṣṭhaḥ", "2p": "mṛṣṭha", "1s": "mārjmi", "1d": "mṛjvaḥ", "1p": "mṛjmaḥ"}),
    "rud2": ("rudi~r", 2, "P", dict(zip(CODES, "roditi ruditaḥ rudanti rodiṣi rudithaḥ ruditha rodimi rudivaḥ rudimaḥ".split()))),
    "svap2": ("ñiṣvapa~", 2, "P", dict(zip(CODES, "svapiti svapitaḥ svapanti svapiṣi svapithaḥ svapitha svapimi svapivaḥ svapimaḥ".split()))),
    "śvas2": ("śvasa~", 2, "P", {"3s": "śvasiti"}), "an2": ("ana~", 2, "P", {"3s": "aniti"}), "jakṣ2": ("jakṣa~", 2, "P", {"3s": "jakṣiti", "3d": "jakṣitaḥ", "3p": "jakṣati"}),
    "jāgṛ2": ("jāgṛ", 2, "P", dict(zip(CODES, "jāgarti jāgṛtaḥ jāgrati jāgarṣi jāgṛthaḥ jāgṛtha jāgarmi jāgṛvaḥ jāgṛmaḥ".split()))),
    "daridrā2": ("daridrā", 2, "P", dict(zip(CODES, "daridrāti daridritaḥ daridrati daridrāsi daridrithaḥ daridritha daridrāmi daridrivaḥ daridrimaḥ".split()))),
    "cakās2": ("cakāsṛ~", 2, "P", {"3s": "cakāsti", "3p": "cakāsati", "2s": "cakāssi", "2d": "cakāsthaḥ", "2p": "cakāstha", "1s": "cakāsmi", "1d": "cakāsvaḥ", "1p": "cakāsmaḥ"}),
    "śī2A": ("śīṅ", 2, "A", dict(zip(CODES, "śete śayāte śerate śeṣe śayāthe śedhve śaye śevahe śemahe".split()))),
    "sū2A": ("ṣūṅ", 2, "A", dict(zip(CODES, "sūte suvāte suvate sūṣe suvāthe sūdhve suve sūvahe sūmahe".split()))),
    "īr2A": ("īra~", 2, "A", {"3s": "īrte", "3d": "īrāte", "3p": "īrate", "2s": "īrṣe", "1s": "īre", "1d": "īrvahe", "1p": "īrmahe"}),
    "ās2A": ("āsa~", 2, "A", {"3s": "āste"}), "vas2A": ("vasa~", 2, "A", {"3s": "vaste", "2s": "vasse", "2p": "vadhve"}), "kas2A": ("kasa~", 2, "A", {"3s": "kaste"}),
    "kaṁs2A": ("kasi~", 2, "A", {"3s": "kaṁste", "3d": "kaṁsāte", "3p": "kaṁsate"}), "niṁs2A": ("ṇisi~", 2, "A", {"3s": "niṁste", "2s": "niṁsse"}),
    "īś2A": ("īśa~", 2, "A", {"3s": "īṣṭe", "2s": "īśiṣe", "2p": "īśidhve"}), "īḍ2A": ("īḍa~", 2, "A", {"3s": "īṭṭe", "3d": "īḍāte", "3p": "īḍate", "2s": "īḍiṣe", "2p": "īḍidhve", "1d": "īḍvahe", "1p": "īḍmahe"}),
    "kaś2A": ("kaśa~", 2, "A", {"3s": "kaṣṭe", "3d": "kaśāte", "2s": "kakṣe", "2p": "kaḍḍhve"}),
})
RUDADI = {"rudi~r", "ñiṣvapa~", "śvasa~", "ana~", "jakṣa~"}      # 7.2.76 rudādibhyaḥ sārvadhātuke (the five)
JAKSADI = {"jakṣa~", "jāgṛ", "daridrā", "cakāsṛ~", "śāsu~"}       # 6.1.6 jakṣityādayaḥ ṣaṭ (with dīdhī, vevī): abhyasta
SATVA_36 = {"mṛjū~", "kaśa~", "īśa~"}                             # 8.2.36 vraścabhrasjasṛjamṛjayajarājabhrājacchaśāṁ ṣaḥ (the members in the suite)
BHRNAM = {"ḍubhṛñ", "māṅ", "o~hāṅ"}       # 7.4.76 bhṛñām it: bhṛ, māṅ, o~hāṅ
NIJAM = {"ṇiji~r", "viji~r", "viṣḷ~"}      # 7.4.75 nijāṁ trayāṇām
SNU_CA = {"stanbhu~", "stunbhu~", "skanbhu~", "skunbhu~", "skuñ"}          # 3.1.82 (the śnu branch realised)
SAMPRASARANA = {"graha~": "gṛh", "jyā": "ji"}                              # 6.1.16 with 1.1.45 and 6.1.108 (declared list)
KSUBHNADI = {"kṣubha~", "tṛpa~"}                                           # 8.4.39 kṣubhnādi (gaṇapāṭha; declared)
GANA = {"ad": 2, "as": 2, "hu": 3, "dā": 3, "dhā": 3, "rudh": 7, "bhid": 7, "ric": 7, "vic": 7, "kṣud": 7, "chṛd": 7, "tṛd": 7, "kṛt": 7, "hiṁs": 7, "div": 4, "siv": 4, "śam": 4, "tud": 6, "nud": 6, "cur": 10, "su": 5, "ci": 5, "śru": 5, "āp": 5, "śak": 5, "tan": 8, "kṛ": 8, "krī": 9, "pū": 9, "lū": 9}   # declared from the Dhātupāṭha; absent = bhvādi
GHU = {"dā", "dhā"}   # 1.1.20 dādhā ghv adāp
SAM_LIST = {"śam", "tam", "dam", "śram", "bhram", "kṣam", "klam", "mad"}   # 7.3.74 śamām aṣṭānām
PU_LIST = {"pū", "lū", "stṝ", "kṝ", "vṝ", "dhū", "śṝ", "pṝ", "bhṝ", "mṝ", "dṝ", "jṝ", "jhṝ", "dhvṝ", "nṝ", "ṝ", "gṝ", "jyā", "rī", "lī", "vlī", "plī"}   # 7.3.80 pvādi (the Dhātupāṭha sub-list, declared)
VAL = set("kgcjṭḍtdpbyrlvśṣsh") | {"kh", "gh", "ch", "jh", "ṭh", "ḍh", "th", "dh", "ph", "bh", "ṅ", "ñ", "ṇ", "n", "m"} - {"y"}
YAN_INIT = {"y", "v", "r", "l", "ñ", "m", "ṅ", "ṇ", "n", "jh", "bh"}   # yañ (ha ya va ra ṭ, la ṇ, ña ma ṅa ṇa na m, jha bha ñ)


class S:
    def __init__(self, root: str, lak: str, code: str, pada: str | None = None):
        if root in NASAL:
            up, g, pada0, _ = NASAL[root]
        else:
            up, pada0 = ROOTS[root]; g = GANA.get(root, 1)
        pada = pada or pada0
        assert pada in ("P", "A"), f"{root}: the pada of an ubhayapadin is declared with the cell (1.3.72)"
        r = its(up, "dhatu")["remaining"]
        if up.endswith("aṣ") and r.endswith("a"):
            r = r[:-1]   # ḍulabhaṣ, ḍupacaṣ: ḍu (1.3.5) and ṣ (1.3.3) are its; the a of the upadeśa's "bha" / "ca" is enunciative
        self.r = tok(r); self.pada = pada; self.lak = lak; self.code = code
        self.num = code[1]; self.pers = code[0]
        self.ab: list[str] = []            # abhyāsa (6.1.4 pūrvo 'bhyāsaḥ)
        self.ag: list[str] = []            # aṭ / āṭ
        self.it: list[str] = []            # iṭ (7.2.35)
        self.v: list[str] = []             # vikaraṇa (śap; sya / tās of 3.1.33)
        self.pre: list[str] = []           # yāsuṭ / sīyuṭ (part of the tiṅ, 1.1.46)
        upa = (TING_P if pada == "P" else TING_A)[code]
        self.up = upa; self.aff = list(its(upa, "pratyaya", vibhakti=True)["remaining_sounds"])   # 1.3.4 na vibhaktau tusmāḥ (1.4.104 vibhaktiś ca)
        self.pit = upa.endswith("p")       # tip sip mip
        self.root = root; self.gana = g; self.up_root = up
        self.idit = any(k == "i" and v == "1.3.2" for k, v in its(up, "dhatu")["its"].items()) and up.endswith("i~")   # idit (hisi~)
        self.vsit = False                  # the vikaraṇa is śit (sārvadhātuka, 3.4.113) and apit → ṅidvat (1.2.4)
        self.flags: set[str] = set(); self.done: set[str] = set(); self.path: list[str] = []

    # views
    def anga(self): return self.r + self.it + self.v + self.pre
    def form(self): return "".join(self.ag + self.ab + self.r + self.it + self.v + self.pre + self.aff)
    def strong(self):   # the pit sārvadhātuka that is not ṅit (1.2.4 / 3.4.103): the guṇa-licensing ending
        return self.pit and not self.ngit()
    def nxt(self):      # the first sound after the aṅga (yāsuṭ / sīyuṭ included)
        return (self.pre + self.aff)[:1]
    def after_root(self):   # the first token after the root
        return (self.it + self.v + self.pre + self.aff)[:1]
    def kit(self):   # 3.4.104 kid āśiṣi (the yāsuṭ of 3.4.103 is parasmaipada: the ātmanepada sīyuṭ is not kit — ceṣīṣṭa — except, jhal-initial, after the ṛ-final root: 1.2.11 liṅsicāv ātmanepadeṣu with 1.2.12 uś ca, kṛṣīṣṭa; stariṣīṣṭa with iṭ); 1.2.5 asaṁyogāl liṭ kit (the apit liṭ ending after a root not ending in a conjunct; ṇal is pit as tip's substitute, 1.1.56)
        return (self.lak == "āśīrliṅ" and self.P()) or (self.lak == "āśīrliṅ" and self.A() and self.pre[:1] == ["s"] and not self.it and self.r[-1] in ("ṛ", "ṝ")) or (self.lak == "luṅ" and self.A() and self.v == ["s"] and not self.it and (self.r[-1] in ("ṛ", "ṝ") or (self.r[-1] not in V and len(self.r) >= 2 and self.r[-2] in ("i", "u", "ṛ", "ī", "ū", "ṝ")))) or (self.lak == "luṅ" and self.v == ["s", "a"]) or (self.lak == "luṅ" and "1.2.17" in self.done) or (self.lak == "liṭ" and "ām" not in self.flags and not self.pit and (self.r[-1] in V or (len(self.r) >= 2 and self.r[-2] in V)))
    def a_final(self): return bool(self.anga()) and self.anga()[-1] == "a"
    def ngit(self):   # 1.2.4 sārvadhātukam apit; liṅ's yāsuṭ is ṅit by 3.4.103
        return (not self.pit) or (self.lak in ("liṅ", "āśīrliṅ"))
    def P(self): return self.pada == "P"
    def A(self): return self.pada == "A"


YAY = {"k", "kh", "g", "gh", "ṅ", "c", "ch", "j", "jh", "ñ", "ṭ", "ṭh", "ḍ", "ḍh", "ṇ", "t", "th", "d", "dh", "n", "p", "ph", "b", "bh", "m", "y", "r", "l", "v"}
SAVARNA = {**{k: "ṅ" for k in ("k", "kh", "g", "gh", "ṅ")}, **{k: "ñ" for k in ("c", "ch", "j", "jh", "ñ")}, **{k: "ṇ" for k in ("ṭ", "ṭh", "ḍ", "ḍh", "ṇ")}, **{k: "n" for k in ("t", "th", "d", "dh", "n")}, **{k: "m" for k in ("p", "ph", "b", "bh", "m")}, "y": "ṁ", "r": "ṁ", "l": "ṁ", "v": "ṁ"}
NATVA_PASS = set(V) | {"k", "kh", "g", "gh", "ṅ", "p", "ph", "b", "bh", "m", "h", "y", "v", "ṁ"}


def _siyut(s: S) -> bool:
    """The sīyuṭ after 7.2.79 (īy): for 6.4.112 / 6.4.113 it still counts as the hal-initial it was (krīṇīta, gṛhṇīta)."""
    return s.lak == "liṅ" and s.A() and s.pre[:2] == ["ī", "y"]


def _conj_before_final(s: S) -> bool:
    """The root's final vowel is preceded by a conjunct (hrī: yes; bhī: no)."""
    return (len(s.r) >= 3 and s.r[-2] not in V and s.r[-3] not in V) or (len(s.r) >= 2 and s.r[-2] == "kṣ")


def _natva_site(s: S):
    """The n (of śnam in the root, or opening the vikaraṇa) after r / ṛ / ṣ across vowels, ku, pu, not before a jhal."""
    seq = s.r + s.v + s.aff
    full = seq
    if s.up_root in KSUBHNADI:     # 8.4.39 kṣubhnādiṣu ca: no ṇatva (kṣubhnāti, tṛpnoti)
        return None
    for i, x in enumerate(seq):
        if x != "n":
            continue
        nxt = full[i + 1] if i + 1 < len(full) else None
        if nxt is None or nxt in JHAL:
            continue
        j = i - 1
        while j >= 0:
            if seq[j] in ("r", "ṛ", "ṝ", "ṣ") or seq[j].endswith(("ṣ", "r")):   # the kṣ token of kṣud ends in ṣ; the ār token of 6.1.90 ends in r
                return i
            if seq[j] not in NATVA_PASS and not all(ch in NATVA_PASS for ch in seq[j]):   # the ay / av tokens of 6.1.78 are ac + aṭ
                break
            j -= 1
    return None


def _natva_set(s: S) -> None:
    i = _natva_site(s)
    if i < len(s.r): s.r[i] = "ṇ"
    elif i < len(s.r) + len(s.v): s.v[i - len(s.r)] = "ṇ"
    else: s.aff[i - len(s.r) - len(s.v)] = "ṇ"


def _s_after_in(s: S):
    """s-initial segments (iṭ-less sya / tās, sīy / yās, suṭ inside the affix) whose preceding sound is iṇ."""
    segs = [("v", s.v, s.r + s.it), ("pre", s.pre, s.r + s.it + s.v), ("aff", s.aff, s.r + s.it + s.v + s.pre)]
    for name, seg, before in segs:
        if seg[:1] == ["s"] and before and (before[-1] in IN or before[-1] in ("k", "kh", "g", "gh", "ṅ")) and not (name == "aff" and len(seg) == 1):   # 8.3.57 iṇkoḥ; 8.3.55 apadāntasya: not the pada-final s
            yield name, 0
    for i in range(1, len(s.aff) - 1):      # suṭ (3.4.107) inside the affix, never the pada-final s
        if s.aff[i] == "s" and s.aff[i - 1] in IN and "3.4.107" in s.done:
            yield "aff", i


def _satva(s: S) -> None:
    for name, i in list(_s_after_in(s)):
        getattr(s, name)[i] = "ṣ"


def _yas(s: S) -> bool:
    """The yāsuṭ / sīyuṭ of liṅ stands between the root and the ending (the iy of 7.2.81 in the pre segment is not it)."""
    return s.lak == "liṅ" and bool(s.pre)   # in āśīrliṅ the sīyuṭ keeps its s and is read as the jhal it is (dvikṣīṣṭa)


def _aprkta(s: S) -> bool:
    """The apṛkta t / s of tip / sip directly after a hal-final root: 6.1.68 drops it before any tripādī rule sees it (8.2.1)."""
    return len(s.aff) == 1 and s.up in ("tip", "sip") and not s.v and not s.it and not s.pre and bool(s.r) and s.r[-1] not in V


def _set_last_anga(s: S, new: list[str]) -> None:
    if s.pre: s.pre[-1:] = new
    elif s.v: s.v[-1:] = new
    elif s.it: s.it[-1:] = new
    else: s.r[-1:] = new


def rules() -> list[tuple[str, Callable[[S], bool], Callable[[S], Any], str]]:
    R: list = []
    def add(n, g, a, note): R.append((n, g, a, note))
    # ---- phase 1: the lakāra's affix substitutions (3.4) ---------------------------------
    add("6.1.50", lambda s: s.up_root in ("ḍumiñ", "mīñ", "dīṅ") and (s.lak in ARDHA_LAK or (s.lak == "liṭ" and s.pit)) and s.r[-1] in ("i", "ī"), lambda s: s.r.__setitem__(-1, "ā"), "ā for mi, mī, dī before the non-śit (6.1.45 ād eca upadeśe 'śiti extended: māsyati, mātā, mamau); in the kit liṭ the Kaumudī and the generator give mimyatuḥ, and the row stays off there")
    add("2.4.52", lambda s: s.root == "as" and s.lak in ARDHA_LAK + ("liṭ",) and s.r == tok("as"), lambda s: (setattr(s, "r", tok("bhū")), setattr(s, "up_root", "bhū"), setattr(s, "gana", 1)), "bhū for as before the ārdhadhātuka (bhavitā, bhaviṣyati, abhūt, bhūyāt, babhūva)")
    add("2.4.42", lambda s: s.up_root == "hana~" and s.lak in ("āśīrliṅ", "luṅ") and s.r == tok("han"), lambda s: (setattr(s, "r", tok("vadha")), setattr(s, "up_root", "vadha")), "vadha for han in āśīrliṅ and luṅ (vadhyāt, avadhīt)")
    add("6.4.48", lambda s: s.r == tok("vadha") and s.lak in ("āśīrliṅ", "luṅ"), lambda s: s.r.pop(), "the a of vadha dropped before the ārdhadhātuka (vadh-yāt)")
    add("2.4.53", lambda s: s.up_root == "brūñ" and s.lak in ARDHA_LAK + ("liṭ",) and s.r == tok("brū"), lambda s: (setattr(s, "r", tok("vac")), setattr(s, "up_root", "vaca~"), setattr(s, "gana", 2)), "vac for brū before the ārdhadhātuka (vaktā, vakṣyati, uvāca)")
    add("2.4.37", lambda s: s.lak == "luṅ" and s.root == "ad" and s.r == tok("ad"), lambda s: (setattr(s, "r", tok("ghas")), setattr(s, "up_root", "ghasḷ")), "ghasḷ for ad in luṅ (and san): the ḷ makes it take aṅ (aghasat)")
    add("2.4.45", lambda s: s.lak == "luṅ" and s.up_root == "iṇ" and s.r == ["i"], lambda s: (setattr(s, "r", tok("gā")), setattr(s, "up_root", "gā")), "gā for iṇ in luṅ (agāt by 2.4.77)")
    add("3.1.48", lambda s: s.lak == "luṅ" and s.gana == 10 and not s.v and "caṅ" not in s.flags, lambda s: (setattr(s, "v", ["a"]), setattr(s, "vsit", True), s.flags.add("caṅ")), "caṅ for cli after the ṇic-ending (and śri, dru, sru) in kartari: acūcurat")
    add("3.1.52", lambda s: s.lak == "luṅ" and not s.v and (s.r == tok("vac") or s.up_root == "khyā"), lambda s: (setattr(s, "v", ["a"]), setattr(s, "vsit", True), s.flags.add("aṅ")), "aṅ for cli after as, vac, khyā (avocat with 7.4.20, akhyat)")
    add("7.4.20", lambda s: "aṅ" in s.flags and s.r == tok("vac"), lambda s: setattr(s, "r", tok("voc")), "um to vac before aṅ (avocat)")
    add("3.1.55", lambda s: s.lak == "luṅ" and s.P() and not s.v and ("ḷ" in s.up_root or (s.up_root in PUSHADI and s.gana == 4)), lambda s: (setattr(s, "v", ["a"]), setattr(s, "vsit", True), s.flags.add("aṅ")), "aṅ for cli after the puṣādi, dyutādi and the ḷdit root in parasmaipada (agamat, aghasat, āpat, aśakat, aviṣat)")
    add("3.1.57", lambda s: s.lak == "luṅ" and s.P() and not s.v and s.up_root.endswith("i~r"), lambda s: (setattr(s, "v", ["a"]), setattr(s, "vsit", True), s.flags.add("aṅ")), "aṅ optionally for cli after the irit root in parasmaipada (abhidat, arudhat, aricat, akṣudat, anijat, arudat — the aṅ branch realised; the sic branch abhaitsīt recorded)")
    add("3.1.45", lambda s: s.lak == "luṅ" and not s.v and anudatta(s.up_root, s.gana) is True and s.r[-1] in ("ś", "ṣ", "s", "h") and len(s.r) >= 2 and s.r[-2] in ("i", "u", "ṛ"), lambda s: (setattr(s, "v", ["s", "a"]), setattr(s, "vsit", True)), "ksa for cli after the aniṭ śal-final root with an ik penult (adhukṣat, adhikṣat, alikṣat, advikṣat, aklikṣat)")
    add("7.3.72", lambda s: s.v == ["s", "a"] and s.A() and s.aff[:1] and s.aff[0] in V, lambda s: s.v.pop(), "the a of ksa dropped before the vowel-initial ātmanepada affix (adhukṣātām, adhukṣanta, adhukṣi)")
    add("7.3.73", lambda s: s.lak == "luṅ" and s.A() and s.v == ["s", "a"] and s.up_root in ("duha~", "diha~", "liha~", "guhū~") and s.aff[:1] and s.aff[0] in ("t", "th", "dh"), lambda s: setattr(s, "v", []), "luk of ksa optionally after duh, dih, lih, guh in ātmanepada before a dental (adugdha, alīḍha; adhukṣata recorded)")
    add("3.1.44", lambda s: s.lak == "luṅ" and not s.v and "2.4.77" not in s.done and "3.1.55" not in s.done, lambda s: setattr(s, "v", ["s"]), "cli (3.1.43) → sic in luṅ")
    add("2.4.77", lambda s: s.lak == "luṅ" and s.v == ["s"] and s.P() and ("".join(s.r) == "bhū" or s.root in GHU or s.up_root in ("ṣṭhā", "gā") or (s.up_root == "pā" and s.gana == 1)), lambda s: setattr(s, "v", []), "luk of sic after gā, sthā, the ghu, pā (pibati) and bhū in parasmaipada (abhūt, adāt, adhāt, asthāt, agāt; 1.1.63: no sic-conditioned operation on the aṅga)")
    add("1.2.17", lambda s: s.lak == "luṅ" and s.A() and s.v == ["s"] and (s.root in GHU or s.up_root == "ṣṭhā") and s.r[-1:] == ["ā"], lambda s: s.r.__setitem__(-1, "i"), "the sic after sthā and the ghu is kit in ātmanepada and their ā → i (adita, adhita, asthita)")
    add("7.2.72", lambda s: s.lak == "luṅ" and s.P() and s.v == ["s"] and not s.it and s.up_root in ("ṣṭuñ", "ṣuñ", "dhūñ"), lambda s: setattr(s, "it", ["i"]), "iṭ for stu, su, dhū before sic in parasmaipada (astāvīt, asāvīt, adhāvīt)")
    add("7.2.73", lambda s: s.lak == "luṅ" and s.P() and s.v == ["s"] and s.r[-1:] == ["ā"] and not s.it, lambda s: (s.r.append("s"), setattr(s, "it", ["i"])), "sak and iṭ for the ā-final root (and yam, ram, nam) before sic in parasmaipada (abhāsiṣṭām, ayāsīt, amāsiṣṭām, adaridrāsīt)")
    add("3.1.35", lambda s: s.lak == "liṭ" and "ām" not in s.flags and (s.up_root in AM_LIT or s.up_root in AM_SLU or s.gana == 10), lambda s: (s.flags.add("ām"), setattr(s, "aff", tok("ām")), s.flags.add("ām-ślu") if s.up_root in AM_SLU else None), "ām after kās and the ṇic-ending (3.1.35), the ijādi gurumat (3.1.36: edhām), ās (3.1.37), jāgṛ (3.1.38, first alternative) and, ślu-like, bhī hrī bhṛ hu (3.1.39: bibhayām, juhavām); the liṭ of bhū follows by 3.1.40 (kṛ and as recorded)")
    add("3.4.81", lambda s: s.lak == "liṭ" and s.A() and s.up in ("ta", "jha") and "ām" not in s.flags, lambda s: setattr(s, "aff", ["e"] if s.up == "ta" else tok("ire")), "ta → eś, jha → irec in liṭ (dade, dadire)")
    add("3.4.82", lambda s: s.lak == "liṭ" and s.P() and "3.4.82" not in s.done and "ām" not in s.flags, lambda s: setattr(s, "aff", tok(LIT_P[s.up])), "the parasmaipada tiṅ → ṇal atus us thal athus a ṇal va ma in liṭ (ārdhadhātuka, 3.4.115)")
    add("3.1.33", lambda s: s.lak in ("lṛṭ", "luṭ", "lṛṅ") and not s.v, lambda s: setattr(s, "v", tok("sya") if s.lak in ("lṛṭ", "lṛṅ") else tok("tās")), "sya before lṛṭ and lṛṅ (lṛ), tāsi before luṭ (ārdhadhātuka: 3.4.114)")
    add("2.4.72", lambda s: s.gana == 2 and s.lak in PRESENT and "śap-luk" not in s.flags, lambda s: s.flags.add("śap-luk"), "luk of śap after the adādi root (1.1.63: nothing conditioned by śap)")
    add("2.4.75", lambda s: s.gana == 3 and s.lak in PRESENT and "ślu" not in s.flags, lambda s: s.flags.add("ślu"), "ślu of śap after the juhotyādi root")
    add("7.1.58", lambda s: s.idit and "7.1.58" not in s.done, lambda s: s.r.insert(max(i for i, x in enumerate(s.r) if x in V) + 1, "n"), "nuṁ to the idit root (hisi~ → hins), after its last vowel (1.1.47)")
    add("3.1.78", lambda s: s.gana == 7 and s.lak in PRESENT and "śnam" not in s.flags, lambda s: (s.flags.add("śnam"), setattr(s, "vsit", True), setattr(s, "r", s.r[: max(i for i, x in enumerate(s.r) if x in V) + 1] + ["n", "a"] + s.r[max(i for i, x in enumerate(s.r) if x in V) + 1:])), "śnam after the last vowel of the rudhādi root (1.1.47 mid aco 'ntyāt paraḥ; śit, apit: ṅidvat)")
    add("3.1.25", lambda s: s.gana == 10 and "ṇic" not in s.flags, lambda s: (s.flags.add("ṇic"), setattr(s, "r", s.r + ["i"])), "ṇic after the curādi root (the ṇic-ending is the dhātu: 3.1.32); ṇ and c are its")
    add("3.1.69", lambda s: not s.v and s.lak in PRESENT and s.gana == 4, lambda s: (setattr(s, "v", tok("ya")), setattr(s, "vsit", True)), "śyan after a divādi root (śit sārvadhātuka, apit: ṅidvat by 1.2.4)")
    add("3.1.77", lambda s: not s.v and s.lak in PRESENT and s.gana == 6, lambda s: (setattr(s, "v", ["a"]), setattr(s, "vsit", True)), "śa after a tudādi root (śit, apit: ṅidvat — no guṇa, tudati)")
    add("3.1.74", lambda s: not s.v and s.lak in PRESENT and s.root == "śru", lambda s: setattr(s, "r", tok("śṛ")), "śru → śṛ with śnu")
    add("3.1.73", lambda s: not s.v and s.lak in PRESENT and s.gana == 5, lambda s: (setattr(s, "v", tok("nu")), setattr(s, "vsit", True)), "śnu after a svādi root (śit, apit: ṅidvat)")
    add("3.1.79", lambda s: not s.v and s.lak in PRESENT and s.gana == 8, lambda s: setattr(s, "v", ["u"]), "u after a tanādi root and kṛ (no ś: ārdhadhātuka by 3.4.114 — so the root takes guṇa, karoti)")
    add("3.1.82", lambda s: not s.v and s.lak in PRESENT and s.up_root in SNU_CA, lambda s: (setattr(s, "v", tok("nu")), setattr(s, "vsit", True)), "śnu too after stambhu, stumbhu, skambhu, skumbhu, sku (the śnu branch realised; śnā recorded)")
    add("3.1.81", lambda s: not s.v and s.lak in PRESENT and s.gana == 9, lambda s: (setattr(s, "v", tok("nā")), setattr(s, "vsit", True)), "śnā after a kryādi root (śit, apit: ṅidvat)")
    add("3.1.68", lambda s: not s.v and s.lak in PRESENT and not s.flags & {"śap-luk", "ślu", "śnam"}, lambda s: setattr(s, "v", ["a"]), "śap after the root before the sārvadhātuka tiṅ (kartari); not before the ārdhadhātuka (3.4.114, 3.4.116 liṅāśiṣi)")
    add("2.4.85", lambda s: s.lak == "luṭ" and s.pers == "3", lambda s: setattr(s, "aff", {"s": tok("ḍā"), "d": tok("rau"), "p": tok("ras")}[s.num]), "the prathama of luṭ → ḍā, rau, ras (both padas)")
    add("3.4.79", lambda s: s.A() and s.lak in TIT and "ām" not in s.flags and "3.4.79" not in s.done and not (s.lak == "luṭ" and s.pers == "3") and s.up != "thās",
        lambda s: setattr(s, "aff", s.aff[:max(i for i, x in enumerate(s.aff) if x in V)] + ["e"]), "the ṭi of the ātmanepada affix → e after a ṭit lakāra (te, āte, ante, se, dhve, e, vahe, mahe)")
    add("3.4.80", lambda s: s.A() and s.lak in TIT and s.up == "thās" and "ām" not in s.flags, lambda s: setattr(s, "aff", ["s", "e"]), "thās → se")
    add("3.4.108", lambda s: s.P() and s.lak in ("liṅ", "āśīrliṅ") and s.up == "jhi", lambda s: setattr(s, "aff", tok("us")), "jhi → jus in liṅ (the j is it)")
    add("3.4.105", lambda s: s.A() and s.lak in ("liṅ", "āśīrliṅ") and s.up == "jha", lambda s: setattr(s, "aff", tok("ran")), "jha → ran in liṅ")
    add("3.4.110", lambda s: s.P() and s.up == "jhi" and s.lak == "luṅ" and "2.4.77" in s.done and s.r[-1:] == ["ā"], lambda s: setattr(s, "aff", tok("us")), "jhi → jus after the ā-final root whose sic is luk (aduḥ, adhuḥ, asthuḥ, aguḥ)")
    add("3.4.109", lambda s: s.P() and s.up == "jhi" and ((s.lak == "luṅ" and s.v == ["s"]) or (s.lak == "laṅ" and (s.gana == 3 or s.up_root in JAKSADI))), lambda s: setattr(s, "aff", tok("us")), "jhi → jus after sic and, in laṅ, after the abhyasta (anaiṣuḥ, abibhayuḥ, ajuhavuḥ)")
    add("6.1.6", lambda s: s.up_root in JAKSADI and "abhyasta" not in s.flags, lambda s: s.flags.add("abhyasta"), "jakṣ, jāgṛ, daridrā, cakās, śās (dīdhī, vevī) are abhyasta by name")
    add("7.1.4", lambda s: s.aff[:1] == ["jh"] and not s.v and not s.it and (("ślu" in s.flags) or "abhyasta" in s.flags), lambda s: setattr(s, "aff", ["a", "t"] + s.aff[1:]), "jh → at after the abhyasta (juhvati, dadati, dadate; jāgrati, śāsati, daridrati by 6.1.6)")
    add("7.1.5", lambda s: s.A() and s.aff[:1] == ["jh"] and s.anga()[-1:] != ["a"], lambda s: setattr(s, "aff", ["a", "t"] + s.aff[1:]), "jh → at in the ātmanepada after a non-a aṅga (alapsata, aidhiṣata)")
    add("7.1.3", lambda s: s.aff[:1] == ["jh"], lambda s: setattr(s, "aff", ["a", "n", "t"] + s.aff[1:]), "jh → ant")
    add("3.4.100", lambda s: s.P() and s.lak in NGIT_LAK and s.up != "mip" and s.aff[-1] == "i" and s.up in ("tip", "sip", "mip", "jhi"), lambda s: s.aff.pop(), "the i of a ṅit lakāra's parasmaipada affix dropped (laṅ, liṅ)")
    add("3.4.101", lambda s: s.P() and s.lak in NGIT_LAK + ("loṭ",) and s.up in ("tas", "thas", "tha", "mip"),
        lambda s: setattr(s, "aff", {"tas": tok("tām"), "thas": tok("tam"), "tha": tok("ta"), "mip": tok("am")}[s.up]), "tas thas tha mip → tām tam ta am after a ṅit lakāra (loṭ by 3.4.85 laṅvat)")
    add("3.4.99", lambda s: s.P() and s.lak in NGIT_LAK + ("loṭ",) and s.up in ("vas", "mas"), lambda s: s.aff.pop(), "the s of the uttama parasmaipada dropped after a ṅit lakāra (loṭ by 3.4.85)")
    add("3.4.86", lambda s: s.P() and s.lak == "loṭ" and s.aff[-1] == "i" and s.up in ("tip", "jhi"), lambda s: s.aff.__setitem__(-1, "u"), "i → u in loṭ (tu, antu)")
    add("3.4.87", lambda s: s.P() and s.lak == "loṭ" and s.up == "sip", lambda s: (setattr(s, "aff", ["h", "i"]), setattr(s, "pit", False)), "sip → hi in loṭ, and it is apit")
    add("3.4.89", lambda s: s.P() and s.lak == "loṭ" and s.up == "mip", lambda s: setattr(s, "aff", ["n", "i"]), "mip → ni in loṭ")
    add("3.4.90", lambda s: s.A() and s.lak == "loṭ" and s.aff[-1] == "e" and s.up in ("ta", "ātām", "jha", "āthām"), lambda s: setattr(s, "aff", s.aff[:-1] + ["ā", "m"]), "the e (3.4.79) → ām in loṭ (tām, ātām, antām, āthām)")
    add("3.4.91", lambda s: s.A() and s.lak == "loṭ" and s.up in ("thās", "dhvam"), lambda s: setattr(s, "aff", tok("sva") if s.up == "thās" else tok("dhvam")), "se dhve → sva dhvam in loṭ")
    add("3.4.93", lambda s: s.A() and s.lak == "loṭ" and s.aff[-1] == "e" and s.pers == "1", lambda s: s.aff.__setitem__(-1, "ai"), "the e of the uttama → ai in loṭ (ai, vahai, mahai)")
    add("3.4.92", lambda s: s.lak == "loṭ" and s.pers == "1", lambda s: (setattr(s, "aff", ["ā"] + s.aff), setattr(s, "pit", True)), "āṭ to the uttama in loṭ, and it is pit")
    add("3.4.102", lambda s: s.A() and s.lak in ("liṅ", "āśīrliṅ"), lambda s: setattr(s, "pre", tok("sīy")), "sīyuṭ to the tiṅ in liṅ (ātmanepada); the u is for pronunciation")
    add("3.4.103", lambda s: s.P() and s.lak in ("liṅ", "āśīrliṅ"), lambda s: setattr(s, "pre", tok("yās")), "yāsuṭ to the tiṅ in liṅ (parasmaipada), and the liṅ is ṅit")
    add("3.4.106", lambda s: s.A() and s.lak in ("liṅ", "āśīrliṅ") and s.up == "iṭ", lambda s: setattr(s, "aff", ["a"]), "iṭ → at in liṅ")
    add("3.4.107", lambda s: s.lak in ("liṅ", "āśīrliṅ") and (s.A() or s.lak == "liṅ") and s.up != "jhi" and any(x in ("t", "th") for x in s.aff) and "3.4.107" not in s.done, lambda s: s.aff.insert(next(i for i, x in enumerate(s.aff) if x in ("t", "th")), "s"), "suṭ to the t / th of the tiṅ in liṅ (both padas) and in āśīrliṅ ātmanepada (sta, āstām; in vidhiliṅ the s falls again by 7.2.79)")
    add("7.2.79", lambda s: s.lak == "liṅ" and ("s" in s.pre or "s" in s.aff[:-1]), lambda s: (s.pre.remove("s") if "s" in s.pre else None, s.aff.pop(s.aff.index("s")) if "s" in s.aff[:-1] else None), "the non-final s of liṅ's sārvadhātuka dropped (yās → yā, sīy → īy, and the suṭ of 3.4.107)")
    add("7.3.100", lambda s: s.root == "ad" and s.lak == "laṅ" and s.aff in (["t"], ["s"]), lambda s: setattr(s, "aff", ["a"] + s.aff), "aṭ to the apṛkta after ad (ādat, ādaḥ)")
    add("7.3.96", lambda s: s.P() and ((s.lak == "luṅ" and s.v == ["s"]) or (s.lak == "laṅ" and s.root == "as")) and s.aff in (["t"], ["s"]), lambda s: setattr(s, "aff", ["ī"] + s.aff), "īṭ to the apṛkta ending after sic and after as (anaiṣīt, anaiṣīḥ, āsīt, āsīḥ)")
    # ---- phase 2: the aṅga -------------------------------------------------------------------
    add("6.4.71", lambda s: s.lak in ("laṅ", "luṅ", "lṛṅ") and not s.ag and s.r[0] not in V, lambda s: setattr(s, "ag", ["a"]), "aṭ augment to the aṅga in laṅ / luṅ")
    add("6.4.72", lambda s: s.lak in ("laṅ", "luṅ", "lṛṅ") and not s.ag and s.r[0] in V, lambda s: setattr(s, "ag", ["ā"]), "āṭ to the vowel-initial aṅga in laṅ / luṅ")
    add("6.1.90", lambda s: s.ag == ["ā"] and s.r[0] in V, lambda s: (setattr(s, "ag", []), s.r.__setitem__(0, {"a": "ā", "ā": "ā", "i": "ai", "ī": "ai", "e": "ai", "ai": "ai", "u": "au", "ū": "au", "o": "au", "au": "au", "ṛ": "ār", "ṝ": "ār"}[s.r[0]])), "vṛddhi for āṭ + the initial vowel (aidh-)")
    add("6.1.64", lambda s: s.r[0] == "ṣ", lambda s: (s.r.__setitem__(0, "s"), [s.r.__setitem__(i, {"ṭ": "t", "ṭh": "th", "ṇ": "n"}[x]) for i, x in enumerate(s.r) if i and x in ("ṭ", "ṭh", "ṇ")]), "the initial ṣ of the upadeśa → s, and the ṭ / ṭh / ṇ it had conditioned revert (ṣuñ → su, ṣṭigha~ → stigh, ṣaṇu~ → san: nimittāpāye naimittikasyāpy apāyaḥ)")
    add("6.1.65", lambda s: s.r[0] == "ṇ", lambda s: s.r.__setitem__(0, "n"), "the initial ṇ of the upadeśa → n (ṇīñ → nī)")
    add("6.1.10", lambda s: ("ślu" in s.flags or "ām-ślu" in s.flags) and not s.ab, lambda s: setattr(s, "ab", s.r[: next(i for i, x in enumerate(s.r) if x in V) + 1]), "the root doubled under ślu (6.1.1 / 6.1.4: ju-hu, da-dā, da-dhā) and ślu-like before ām (3.1.39: bibhayām)")
    add("6.1.8", lambda s: s.lak == "liṭ" and not s.ab and "ām" not in s.flags, lambda s: setattr(s, "ab", s.r[: next(i for i, x in enumerate(s.r) if x in V) + 1]), "the root's first ekāc doubled before liṭ (6.1.1 ekāco dve prathamasya; the first is the abhyāsa, 6.1.4)")
    add("6.1.17", lambda s: s.lak == "liṭ" and s.ab[:2] in (["v", "a"], ["y", "a"]) and s.up_root in ("vaca~", "brūñ", "ñiṣvapa~", "yaja~", "jyā") or (s.lak == "liṭ" and s.ab[:3] == ["s", "v", "a"] and s.up_root == "ñiṣvapa~") or (s.lak == "liṭ" and s.up_root == "jyā" and s.ab[:2] == ["j", "y"]), lambda s: setattr(s, "ab", [{"v": "u", "y": "i"}[s.ab[0]]] if s.ab[0] in ("v", "y") else (["s", "u"] if s.ab[0] == "s" else ["j", "i"])), "samprasāraṇa of the abhyāsa of the vacyādi / grahyādi in liṭ, with 6.1.108 (uvāca, ūce, jijyau; svap by 7.4.67 dyutisvāpyoḥ: suṣvāpa)")
    add("7.4.61", lambda s: len(s.ab) >= 3 and s.ab[0] in ("s", "ś", "ṣ") and s.ab[1] in KHAY, lambda s: setattr(s, "ab", s.ab[1:]), "after śar the khay is what the abhyāsa keeps (caskambha, tastambha, cuskāva, paspardha)")
    add("7.4.60", lambda s: len(s.ab) > 2 or s.ab[:1] == ["kṣ"], lambda s: setattr(s, "ab", [s.ab[0] if s.ab[0] != "kṣ" else "k", s.ab[-1]]), "only the first consonant of the abhyāsa kept (ji-hrī, ji-hreti; of kṣ the k: cakṣāṇa, cukṣāva)")
    add("7.4.70", lambda s: s.lak == "liṭ" and s.ab in (["a"], ["ā"]) and s.r[:1] in (["a"], ["ā"]) and not s.ag, lambda s: (setattr(s, "ab", []), s.r.__setitem__(0, "ā")) if not (s.r[:2] and s.r[1] not in V and len(s.r) >= 3 and s.r[2] not in V) and s.up_root != "aśū~" else (setattr(s, "ab", ["ā", "n"]), None), "the abhyāsa a (ata ādeḥ) → ā, merging with the root's a by 6.1.101 (āda, āna, āśa); before a root of two consonants and for aś the nuṭ follows (7.4.71 tasmān nuḍ dvihalaḥ, 7.4.72 aśnoteś ca: ānañja, ānaśe)")
    add("7.4.59", lambda s: s.ab[-1:] and s.ab[-1] in HRASVA, lambda s: s.ab.__setitem__(-1, HRASVA[s.ab[-1]]), "the abhyāsa vowel shortened")
    add("7.4.69", lambda s: s.lak == "liṭ" and s.kit() and s.ab == ["i"] and s.up_root == "iṇ", lambda s: s.ab.__setitem__(0, "ī"), "the abhyāsa i of iṇ lengthened before the kit (īyatuḥ, īyuḥ)")
    add("7.4.66", lambda s: s.ab[-1:] == ["ṛ"], lambda s: s.ab.__setitem__(-1, "a"), "ṛ of the abhyāsa → a (ca-kāra)")
    add("7.4.73", lambda s: s.ab[-1:] == ["u"] and "".join(s.r) == "bhū", lambda s: s.ab.__setitem__(-1, "a"), "u of bhū's abhyāsa → a (ba-bhūva)")
    add("7.4.62", lambda s: s.ab[:1] and s.ab[0] in CU, lambda s: s.ab.__setitem__(0, CU[s.ab[0]]), "ku / h of the abhyāsa → cu (ja-gāma, ca-kāra)")
    add("8.4.54", lambda s: s.ab[:1] and s.ab[0] in DEASP, lambda s: s.ab.__setitem__(0, DEASP[s.ab[0]]), "the aspirate of the abhyāsa → car (ba-bhūva)")
    add("7.4.76", lambda s: ("ślu" in s.flags or "ām-ślu" in s.flags) and s.up_root in BHRNAM and s.ab[-1:] in (["ṛ"], ["a"], ["ā"]), lambda s: s.ab.__setitem__(-1, "i"), "i for the abhyāsa vowel of bhṛ, māṅ, o~hāṅ under ślu (bibharti, mimīte, jihīte)")
    add("7.4.77", lambda s: "ślu" in s.flags and s.up_root in ("ṛ", "pṝ", "pṛ") and s.ab[-1:] in (["ṛ"], ["a"], ["ṝ"]), lambda s: s.ab.__setitem__(-1, "i"), "i for the abhyāsa of ṛ and pṝ under ślu (piparti)")
    add("7.4.75", lambda s: "ślu" in s.flags and s.up_root in NIJAM and s.ab[-1:] == ["i"], lambda s: s.ab.__setitem__(-1, "e"), "guṇa of the abhyāsa of nij, vij, viṣ under ślu (nenekti, vevekti, veveṣṭi)")
    add("7.2.13", lambda s: s.lak == "liṭ" and "".join(s.r) in NO_IT_LIT and "7.2.13" not in s.flags, lambda s: s.flags.add("7.2.13"), "no iṭ in liṭ after kṛ, sṛ, bhṛ, vṛ, stu, dru, sru, śru (cakṛva, cakṛṣe, cakartha)")
    add("7.2.35", lambda s: ((s.v[:1] in (["s"], ["t"]) or (s.pre[:1] == ["s"] and s.lak == "āśīrliṅ")) and not s.it and (anudatta(s.up_root, s.gana) is not True or (s.root == "gam" and s.P() and s.v[:1] == ["s"]))) or (s.lak == "liṭ" and "ām" not in s.flags and not s.it and "7.2.13" not in s.flags and (s.aff[:1] in (["v"], ["m"]) or (s.A() and s.aff[:1] in (["s"], ["dh"])) or (s.P() and s.up == "sip" and s.r[-1] != "ṛ"))),
        lambda s: setattr(s, "it", ["i"]), "iṭ before the val-initial ārdhadhātuka (sya, tās, sīyuṭ) for the seṭ root — the root whose upadeśa vowel is not anudātta in the Dhātupāṭha (7.2.10 ekāca upadeśe 'nudāttāt keeps nī, labh, gam, kṛ, dā aniṭ; 7.2.58 gamer iṭ before sya in parasmaipada); before liṭ's va / ma / se / dhve for every root outside 7.2.13 (babhūviva, jagmiva, ninyiva, dadiṣe) and before thal — 7.2.61 / 7.2.62's aniṭ holds only for the ṛ-final root by 7.2.63 ṛto bhāradvājasya (cakartha; ninayitha, jagamitha realised, ninetha / jagantha recorded)")
    add("7.2.70", lambda s: s.v == tok("sya") and not s.it and (s.r[-1] in ("ṛ", "ṝ") or s.up_root == "hana~"), lambda s: setattr(s, "it", ["i"]), "iṭ before sya for the ṛ-final root and han (kariṣyati, bhariṣyati, stariṣyati, haniṣyati)")
    add("7.2.37", lambda s: s.up_root == "graha~" and s.it == ["i"] and s.lak != "liṭ", lambda s: setattr(s, "it", ["ī"]), "the iṭ after grah lengthened outside liṭ (grahīṣyati, grahītā)")
    add("6.4.120", lambda s: s.lak == "liṭ" and (s.kit() or (s.up == "sip" and s.it)) and "ām" not in s.flags and len(s.r) == 3 and s.r[1] == "a" and s.r[0] not in V and s.r[2] not in V and s.ab[:1] == s.r[:1] and s.r[0] != "v" and "".join(s.r) not in ("śas", "dad"), lambda s: (s.r.__setitem__(1, "e"), setattr(s, "ab", [])), "e for the a between single consonants, with the abhyāsa dropped, before the kit liṭ and the seṭ thal (6.4.121: pecatuḥ, pece, lebhe, mene, nebhatuḥ, senatuḥ, pecitha); not when the abhyāsa's initial is a substitute (anādeśādeḥ: cakase, jaghasatuḥ), nor śas, dad, the v-initial (6.4.126)")
    add("6.4.123", lambda s: s.lak == "liṭ" and (s.kit() or (s.up == "sip" and s.it)) and s.up_root == "rādha~" and s.r == tok("rādh"), lambda s: (s.r.__setitem__(1, "e"), setattr(s, "ab", [])), "e for rādh in the sense of hiṁsā (redhatuḥ)")
    add("7.3.77", lambda s: "".join(s.r) == "gam" and s.v == ["a"] and s.lak in PRESENT, lambda s: setattr(s, "r", tok("gach")), "m of gam → ch before the śit śap")
    add("6.1.73", lambda s: (s.r[-1:] == ["ch"] or ((s.ag == ["a"] or (s.ab and s.ab[-1] in ("a", "i", "u", "ṛ"))) and s.r[:1] == ["ch"])) and "6.1.73" not in s.done, lambda s: s.r.insert(len(s.r) - 1 if s.r[-1:] == ["ch"] else 0, "t"), "tuk before ch after a short vowel (gat-ch, a-t-chṛṇat, ca-t-charda)")
    add("8.4.40t", lambda s: any(s.r[i:i + 2] == ["t", "ch"] for i in range(len(s.r) - 1)), lambda s: [s.r.__setitem__(i, "c") for i in range(len(s.r) - 1) if s.r[i:i + 2] == ["t", "ch"]], "the tuk's t → c before ch (stoḥ ścunā ścuḥ: gacch)")
    add("6.4.88", lambda s: "".join(s.r) == "bhū" and s.lak in ("luṅ", "liṭ") and not s.v and s.after_root() and s.after_root()[0] in V, lambda s: s.r.append("v"), "vuk to bhū before a vowel in luṅ / liṭ (abhūvan, babhūva, babhūviva)")
    add("7.2.115", lambda s: s.lak == "liṭ" and s.up == "tip" and "ām" not in s.flags and s.r[-1] in VRDDHI, lambda s: s.r.__setitem__(-1, VRDDHI[s.r[-1]]) if s.r[-1] not in ("ṛ", "ṝ") else setattr(s, "r", s.r[:-1] + ["ā", "r"]), "vṛddhi of the final vowel before the ñit / ṇit ṇal (nai-, kār-, cakāra of kṝ too); thal is pit, not ṇit: guṇa only (cakartha)")
    add("7.2.116", lambda s: s.lak == "liṭ" and s.up == "tip" and "ām" not in s.flags and len(s.r) >= 2 and s.r[-2] == "a" and s.r[-1] not in V, lambda s: s.r.__setitem__(-2, "ā"), "vṛddhi of the penultimate a before ṇal (ja-gāma, uvāca, jaghāna)")
    add("7.4.11", lambda s: s.lak == "liṭ" and s.r[-1:] == ["ṝ"] and "ām" not in s.flags, lambda s: setattr(s, "r", s.r[:-1] + tok("ar")), "guṇa for the ṝ-final root (and ṛcch) in liṭ, kit or not (cakaratuḥ, cakare, paparatuḥ; 7.4.12's optional hrasva papratuḥ recorded)")
    add("7.3.55", lambda s: s.lak == "liṭ" and s.up_root == "hana~" and s.ab and s.r[:1] == ["h"], lambda s: s.r.__setitem__(0, "gh"), "h of han → gh after the abhyāsa (jaghāna, jaghnatuḥ)")
    add("7.1.34", lambda s: s.lak == "liṭ" and s.up in ("tip", "mip") and s.P() and s.r[-1:] == ["ā"] and s.aff == ["a"] and "ām" not in s.flags, lambda s: setattr(s, "aff", ["au"]), "ṇal → au after ā (dadau, dadhau, jahau, papau, mamau, jajñau, sasnau)")
    add("6.4.64", lambda s: s.r[-1:] == ["ā"] and "ām" not in s.flags and ((s.lak == "liṭ" and ((s.kit() and s.nxt() and s.nxt()[0] in V) or s.it)) or (s.lak == "luṅ" and ((s.v == ["a"] and s.vsit) or (not s.v and s.aff[:1] == ["u"])))), lambda s: s.r.pop(), "ā dropped before the kit / ṅit vowel-initial ārdhadhātuka and before iṭ (dadatuḥ, dade, dadire, daditha; akhyat before aṅ, aduḥ before jus)")
    add("6.4.98", lambda s: (s.lak == "liṭ" and s.kit() and "".join(s.r) in ("gam", "ghan")) or (s.up_root == "hana~" and not s.strong() and s.lak in PRESENT and s.nxt() and s.nxt()[0] in V and len(s.r) >= 3), lambda s: s.r.pop(-2), "the upadhā of gam / han dropped before the kit / ṅit vowel-initial ending (jagmatuḥ, jagmiva; ghn-anti; not before the yāsuṭ: hanyāt)")
    add("7.3.54", lambda s: s.up_root == "hana~" and s.r[:2] == ["h", "n"], lambda s: s.r.__setitem__(0, "gh"), "h of han → gh before n (ghnanti)")
    add("7.2.1", lambda s: s.P() and s.lak == "luṅ" and s.v == ["s"] and s.r[-1] in VRDDHI and s.up_root != "jāgṛ", lambda s: s.r.__setitem__(-1, VRDDHI[s.r[-1]]) if s.r[-1] not in ("ṛ", "ṝ") else setattr(s, "r", s.r[:-1] + ["ā", "r"]), "vṛddhi of the final vowel before sic in parasmaipada, with iṭ too (anaiṣīt, akārṣīt, adhāvīt, alāvīt; the apavāda of 7.3.84)")
    add("7.2.3", lambda s: s.P() and s.lak == "luṅ" and s.v == ["s"] and not s.it and s.r[-1] not in V and any(x in ("a", "i", "u", "ṛ") for x in s.r) and s.r[max(i for i, x in enumerate(s.r) if x in V)] in ("a", "i", "u", "ṛ") and s.r[-1] not in ("h", "m", "y") and s.up_root not in ("kṣaṇu~", "śvasa~", "jāgṛ") and "ṇic" not in s.flags, lambda s: s.r.__setitem__(max(i for i, x in enumerate(s.r) if x in V), {"a": "ā", "i": "ai", "u": "au", "ṛ": "ār"}[s.r[max(i for i, x in enumerate(s.r) if x in V)]]), "vṛddhi of the vowel of the hal-final root before sic (apākṣīt, abhāntsīt, anautsīt, amārkṣīt); not before iṭ (7.2.4 neṭi: adevīt), not for the h / m / y-final, kṣaṇ, śvas, jāgṛ, ṇi, śvi, edit (7.2.5: agrahīt, ajāgarīt); 7.2.7's option for the laghu a-root recorded")
    add("7.3.86", lambda s: "7.3.86" not in s.done and (("ṇic" in s.flags and len(s.r) >= 3 and s.r[-2] not in V and s.r[-3] in ("i", "u", "ṛ")) or (((s.v == ["a"] and not s.vsit) or (s.v == ["u"] and s.strong()) or ((s.v[:1] in (["s"], ["t"]) or s.it or (s.lak == "liṭ" and "ām" not in s.flags)) and not s.kit() and "ṇic" not in s.flags) or (s.flags & {"ślu", "śap-luk"} and s.strong() and s.lak in PRESENT and not (s.ab and s.aff[:1] and s.aff[0] in V))) and len(s.r) >= 2 and s.r[-1] not in V and s.r[-2] in ("i", "u", "ṛ"))),
        lambda s: s.r.__setitem__(-3 if "ṇic" in s.flags else -2, GUNA[s.r[-3 if "ṇic" in s.flags else -2]]), "guṇa of the light penultimate before the ṇit ṇic, the pit śap, the ārdhadhātuka u / sya / tās / iṭ (bhetsyati, deviṣyati, rotsyati, dhokṣyati) or the pit tiṅ across the luk / ślu (cur → cor, kṣiṇ → kṣeṇ, nenej-mi, veveṣ-ṭi; not before the ṅidvat śa: tudati; not for the abhyasta before a vowel-initial pit: 7.3.87 nenijāni)")
    add("6.4.67", lambda s: s.lak == "āśīrliṅ" and s.P() and s.r[-1:] == ["ā"] and (s.root in GHU or s.up_root in ("māṅ", "mā", "ṣṭhā", "gā", "pā~", "o~hāk", "ṣo~")), lambda s: s.r.__setitem__(-1, "e"), "e for the ā of ghu, mā, sthā, gā, pā, hā, sā before the kit yāsuṭ of āśīrliṅ (6.4.66's ī is the other hal case: deyāt, dheyāt, meyāt, heyāt; the adādi pā rakṣaṇe is not the pā of the list: pāyāt)")
    add("6.4.66", lambda s: s.lak == "āśīrliṅ" and s.P() and s.r[-1:] == ["ā"] and "6.1.50" in s.done, lambda s: s.r.__setitem__(-1, "ī"), "ī for the ā of 6.1.50's mā (mi, mī) before the hal-initial kit ārdhadhātuka (mīyāt)")
    add("6.4.51", lambda s: "ṇic" in s.flags and s.r[-1:] == ["i"] and not s.it and ((s.lak == "āśīrliṅ" and s.P()) or "caṅ" in s.flags), lambda s: s.r.pop(), "ṇi dropped before the aniṭ ārdhadhātuka (coryāt, acūcurat; corayitā keeps it before iṭ)")
    add("6.1.11", lambda s: "caṅ" in s.flags and not s.ab and "6.4.51" in s.done, lambda s: setattr(s, "ab", s.r[: next(i for i, x in enumerate(s.r) if x in V) + 1]), "the root doubled before caṅ (6.1.1 / 6.1.4: cu-cur)")
    add("7.4.59c", lambda s: "caṅ" in s.flags and s.ab[-1:] and s.ab[-1] in HRASVA, lambda s: s.ab.__setitem__(-1, HRASVA[s.ab[-1]]), "the abhyāsa vowel shortened (7.4.59: cu-)")
    add("7.4.1", lambda s: "caṅ" in s.flags and s.ab and len(s.r) >= 2 and s.r[-2] in ("ā", "ī", "ū", "e", "o", "ai", "au"), lambda s: s.r.__setitem__(-2, {"ā": "a", "ī": "i", "ū": "u", "e": "i", "o": "u", "ai": "i", "au": "u"}[s.r[-2]]), "the penult of the ṇi-aṅga shortened before caṅ (cor → cur)")
    add("7.4.94", lambda s: "caṅ" in s.flags and s.ab and s.ab[-1] in ("a", "i", "u") and s.r[:2] and s.r[0] not in V and s.r[1] in ("a", "i", "u", "ṛ") and "7.4.94" not in s.done, lambda s: s.ab.__setitem__(-1, {"a": "ā", "i": "ī", "u": "ū"}[s.ab[-1]]), "the abhyāsa lengthened before the laghu (7.4.93 sanvallaghuni caṅpare: acūcurat)")
    add("7.3.85", lambda s: s.up_root == "jāgṛ" and s.r[-1:] == ["ṛ"] and ((s.lak == "āśīrliṅ" and s.P()) or s.lak in ARDHA_LAK or "ām" in s.flags), lambda s: setattr(s, "r", s.r[:-1] + tok("ar")), "guṇa for jāgṛ except before vi, ciṇ, ṇal and the ṅit (jāgaryāt, jāgaritā)")
    add("7.4.29", lambda s: s.lak == "āśīrliṅ" and s.P() and s.r[-1:] == ["ṛ"] and (s.r == ["ṛ"] or (len(s.r) >= 3 and s.r[-2] not in V and s.r[-3] not in V)), lambda s: setattr(s, "r", s.r[:-1] + tok("ar")), "guṇa, not riṅ, for ṛ and the conjunct-initial ṛ-root before the liṅ y (staryāt, smaryāt)")
    add("7.4.28", lambda s: s.lak == "āśīrliṅ" and s.P() and s.r[-1:] == ["ṛ"], lambda s: setattr(s, "r", s.r[:-1] + tok("ri")), "riṅ for ṛ before the y of āśīrliṅ (kriyāt, bhriyāt, priyāt; then 7.4.25's dīrgha)")
    add("7.1.100", lambda s: s.r[-1] == "ṝ" and (len(s.r) == 1 or s.r[-2] not in ("p", "ph", "b", "bh", "m", "v")) and ((s.lak == "āśīrliṅ" and s.P()) or (s.lak in PRESENT and not s.strong() and not s.vsit)), lambda s: setattr(s, "r", s.r[:-1] + ["i", "r"]), "ṝ → ir before the kit / ṅit (kīryāt, stīryāt, īryāt with 8.2.77; after a labial 7.1.102's ur: vūryāt)")
    add("7.1.102", lambda s: len(s.r) >= 2 and s.r[-1] == "ṝ" and s.r[-2] in ("p", "ph", "b", "bh", "m", "v") and not (s.strong() and s.lak in PRESENT) and not (s.lak == "laṅ" and s.aff == ["u", "s"]) and not (s.vsit and s.gana == 9) and not ((s.it or s.v[:1] in (["s"], ["t"])) and not s.kit()) and not (s.lak == "āśīrliṅ" and s.A()) and not (s.lak == "liṭ" and not s.kit()), lambda s: setattr(s, "r", s.r[:-1] + ["u", "r"]), "ṝ → ur after a labial (7.1.100 ṝta id dhātoḥ with 7.1.102: pipur-, pipūr- with 8.2.77; pipūryāt before the ṅit yāsuṭ; not before jus, where 7.3.83 is para)")
    add("8.2.77", lambda s: len(s.r) >= 2 and s.r[-1] in ("r", "v") and s.r[-2] in ("i", "u") and (s.v == tok("ya") or (not s.v and s.after_root() and s.after_root()[0] not in V)), lambda s: s.r.__setitem__(-2, {"i": "ī", "u": "ū"}[s.r[-2]]), "the ik before the root-final r / v lengthened before hal (dīvyati, sīvyati, pipūrtaḥ, pipūryāt; pipurati before the vowel)")
    add("7.3.74", lambda s: s.v == tok("ya") and s.root in SAM_LIST and s.r[-2] == "a", lambda s: s.r.__setitem__(-2, "ā"), "the eight śam-roots lengthened before śyan (śāmyati)")
    add("6.4.24", lambda s: (s.vsit or (s.kit() and s.lak == "āśīrliṅ")) and not s.idit and len(s.r) >= 3 and s.r[-2] == "n" and s.r[-1] not in V and s.r[-3] in V, lambda s: s.r.pop(-2), "the penultimate n of a non-idit root dropped before the kit / ṅit (dabhnoti, stabhnoti, badhnāti, mathnāti)")
    add("7.3.79", lambda s: s.v == tok("nā") and "".join(s.r) == "jñā", lambda s: setattr(s, "r", tok("jā")), "jñā → jā before śnā (jānāti)")
    add("6.1.15", lambda s: s.kit() and s.lak in ("āśīrliṅ", "liṭ") and s.r in (tok("vac"), tok("svap")), lambda s: setattr(s, "r", tok("uc") if s.r == tok("vac") else tok("sup")), "samprasāraṇa of vac / svap before the kit (1.1.45, 6.1.108: ucyāt, supyāt; uvāca by 6.1.17 is liṭ's)")
    add("6.1.16", lambda s: (s.vsit or (s.kit() and s.lak in ("āśīrliṅ", "liṭ"))) and s.up_root in SAMPRASARANA and "6.1.16" not in s.done, lambda s: setattr(s, "r", tok(SAMPRASARANA[s.up_root])), "samprasāraṇa of grah / jyā before the ṅit and the kit (1.1.45; with 6.1.108: gṛh-, ji-)")
    add("6.4.2", lambda s: s.lak == "āśīrliṅ" and s.kit() and "6.1.16" in s.done and s.r == tok("ji"), lambda s: s.r.__setitem__(-1, "ī"), "the samprasāraṇa vowel after a hal lengthened (jīyāt; jināti is shortened again by 7.3.80)")
    add("7.3.80", lambda s: s.vsit and s.gana == 9 and (s.root in PU_LIST or s.up_root.rstrip("ñ") in PU_LIST) and s.r[-1] in ("ū", "ṝ", "ī"), lambda s: s.r.__setitem__(-1, {"ū": "u", "ṝ": "ṛ", "ī": "i"}[s.r[-1]]), "the pvādi of the kryādi shortened before the śit (pu-nā-, lu-nā-, stṛ-ṇā-, li-nā-, ṛ-ṇā-; the svādi dhūñ keeps ū: dhūnoti)")
    add("6.4.23", lambda s: "śnam" in s.flags and "6.4.23" not in s.done and any(s.r[i:i + 3] == ["n", "a", "n"] for i in range(len(s.r) - 2)), lambda s: s.r.pop(next(i for i in range(len(s.r) - 2) if s.r[i:i + 3] == ["n", "a", "n"]) + 2), "the root's n (the nuṁ of hiṁs) dropped after śnam (hinasti)")
    add("6.4.111", lambda s: s.lak in PRESENT and not s.strong() and (("śnam" in s.flags and "a" in s.r[1:]) or (s.root == "as" and (s.r[:2] == ["a", "s"] or (s.r[:2] == ["ā", "s"] and "6.1.90" in s.done)))) and "6.4.111" not in s.done and "6.4.111" not in s.flags, lambda s: (s.flags.add("6.4.111"), (s.r.pop(len(s.r) - 1 - s.r[::-1].index("a")) if "śnam" in s.flags else (s.r.pop(0) if s.r[0] == "a" else None))), "the a of śnam and of as dropped before the kit / ṅit sārvadhātuka (runddhaḥ, bhindanti, staḥ, santi)")
    add("7.4.50a", lambda s: s.root == "as" and not s.pre and s.aff[:1] == ["s"] and s.r[-1:] == ["s"], lambda s: s.r.pop(), "the s of as dropped before the s-initial sārvadhātuka (asi; 7.4.50 tāsastyoḥ)")
    add("7.3.98", lambda s: "śap-luk" in s.flags and s.up_root in RUDADI and not s.it and s.lak == "laṅ" and s.aff in (["t"], ["s"]), lambda s: setattr(s, "it", ["ī"]), "īṭ to the apṛkta after rud, svap, śvas, an, jakṣ in laṅ (arodīt; 7.3.99's aṭ is the other branch)")
    add("7.2.76", lambda s: "śap-luk" in s.flags and s.up_root in RUDADI and not s.it and not s.pre and s.aff[:1] and s.aff[0] not in V and s.lak in PRESENT, lambda s: setattr(s, "it", ["i"]), "iṭ for rud, svap, śvas, an, jakṣ before the hal-initial sārvadhātuka (roditi, svapimi); theorum/136 had cited 7.3.98, the īṭ rule of the apṛkta — corrected after the independent-oracle audit (theorum/137)")
    add("7.2.77", lambda s: s.up_root == "īśa~" and (s.aff[:2] == ["s", "e"] or (s.lak == "loṭ" and s.aff in (["s", "v", "a"], tok("dhvam")))) and not s.it, lambda s: setattr(s, "it", ["i"]), "iṭ for īś before se and (by 7.2.78's dhve) before the loṭ sva / dhvam that stand for se / dhve by 3.4.91 (1.1.56 sthānivat: īśiṣe, īśiṣva, īśidhvam); not before the dhvam of laṅ / liṅ (aiḍḍhvam, īśīdhvam)")
    add("7.2.78", lambda s: s.up_root in ("īḍa~", "īśa~", "jana~") and (s.aff == ["dh", "v", "e"] or (s.lak == "loṭ" and s.aff == tok("dhvam")) or (s.up_root == "īḍa~" and (s.aff[:2] == ["s", "e"] or (s.lak == "loṭ" and s.aff == ["s", "v", "a"])))) and not s.it, lambda s: setattr(s, "it", ["i"]), "iṭ for īḍ and jan before dhve and se, and for īś before dhve (īḍiṣe, īḍidhve, īśidhve; the loṭ sva / dhvam by 1.1.56: īḍiṣva, īḍidhvam; not the dhvam of laṅ / liṅ: aiḍḍhvam, īḍīdhvam)")
    add("7.3.93", lambda s: s.up_root == "brūñ" and s.strong() and s.lak in PRESENT and s.aff[:1] and s.aff[0] not in V and not s.it, lambda s: setattr(s, "it", ["ī"]), "īṭ for brū before the hal-initial pit sārvadhātuka (bravīti; not before the ṅit yāsuṭ: brūyāt)")
    add("7.2.114", lambda s: s.up_root == "mṛjū~" and ((s.strong() and s.lak in PRESENT) or ((s.it or s.v[:1] in (["s"], ["t"]) or s.lak == "liṭ") and not s.kit())) and s.r[1] in ("ṛ", "ar", "a"), lambda s: setattr(s, "r", ["m", "ā", "r", "j"]), "vṛddhi of mṛj before the pit sārvadhātuka (mārṣṭi, mārjmi; the apavāda of 7.3.86's guṇa; 1.1.5 before the ṅit yāsuṭ: mṛjyāt)")
    add("7.4.21", lambda s: s.up_root == "śīṅ" and s.r[-1] == "ī" and s.lak in PRESENT, lambda s: s.r.__setitem__(-1, "e"), "guṇa of śī before every sārvadhātuka (śete, śerate, śayāte)")
    add("7.1.6", lambda s: s.up_root == "śīṅ" and s.lak in PRESENT and s.aff[:2] == ["a", "t"] and "7.1.6" not in s.done, lambda s: setattr(s, "aff", ["r"] + s.aff), "ruṭ to the at of jha after śī (śerate)")
    add("6.4.34", lambda s: s.up_root == "śāsu~" and not s.pit and s.lak in PRESENT and s.aff[:1] and s.aff[0] not in V, lambda s: s.r.__setitem__(1, "i"), "ā of śās → i before the hal-initial kit / ṅit (śiṣṭaḥ, śiṣmaḥ)")
    add("6.4.114", lambda s: s.up_root == "daridrā" and not s.strong() and s.lak in PRESENT and s.nxt() and s.nxt()[0] not in V, lambda s: s.r.__setitem__(-1, "i"), "ā of daridrā → i before the hal-initial kit / ṅit (daridritaḥ)")
    add("6.4.36", lambda s: s.up_root == "hana~" and s.aff == ["h", "i"] and s.lak == "loṭ", lambda s: (setattr(s, "r", ["j", "a"]), s.flags.add("6.4.36")), "ja for han before hi (jahi); the ja is asiddhavat for 6.4.105 (6.4.22 asiddhavad atrābhāt), so the hi stays")
    add("6.4.37", lambda s: s.up_root == "hana~" and not s.strong() and s.lak in PRESENT and s.nxt() and s.nxt()[0] in JHAL and len(s.pre + s.aff) > 1 and s.r[-1] == "n", lambda s: s.r.pop(), "the anunāsika of han dropped before the jhal-initial kit / ṅit (hataḥ, hathaḥ; not before the yāsuṭ: hanyātam)")
    add("7.3.91", lambda s: s.up_root == "ūrṇuñ" and s.r[-1:] == ["u"] and s.strong() and s.lak in PRESENT and len(s.aff) == 1 and s.aff[0] not in V, lambda s: s.r.__setitem__(-1, "o"), "guṇa, not 7.3.90's vṛddhi, for ūrṇu before the apṛkta ending (aurṇot, aurṇoḥ)")
    add("7.3.89", lambda s: "śap-luk" in s.flags and s.r[-1:] == ["u"] and s.strong() and s.lak in PRESENT and s.aff[:1] and s.aff[0] not in V and not (s.up_root == "ūrṇuñ" and "7.3.90" in s.flags), lambda s: (s.r.__setitem__(-1, "au"), s.flags.add("7.3.89")), "vṛddhi of the u-final root before the hal-initial pit sārvadhātuka when śap is luk (yauti, stauti, kṣṇauti; ūrṇauti by 7.3.90's first alternative; not before the ṅit yāsuṭ, 1.1.5: stuyāt)")
    add("7.3.84", lambda s: s.r[-1] in GUNA and s.after_root() and not s.kit() and not s.vsit and not (s.up_root == "ṣūṅ" and "śap-luk" in s.flags) and (s.v or s.it or (s.lak == "āśīrliṅ" and s.A()) or (s.lak == "liṭ" and ("ām" in s.flags or (not s.kit() and s.up != "tip"))) or (s.flags & {"ślu", "śap-luk"} and s.strong() and s.lak in PRESENT)), lambda s: setattr(s, "r", s.r[:-1] + tok(GUNA[s.r[-1]])), "guṇa of the root's final ik before the pit śap, the ārdhadhātuka iṭ / sya / tās / u / ṇic, or the pit tiṅ directly after the luk / ślu (bhū → bho, nī → ne, kṛ → kar, cori → core, juhoti; before the ac-initial pit too: bibhayāni, juhavāni, bibharāṇi — 7.3.87 withholds only 7.3.86's laghūpadha guṇa); not before the kit āśīrliṅ nor the ṅidvat śit vikaraṇa (1.1.5, 1.2.4: sunoti, tudati); not for sū before the tiṅ (7.3.88 bhūsuvos tiṅi: suvai); before the sīyuṭ of āśīrliṅ, which is not kit (ceṣīṣṭa, stoṣīṣṭa)")
    add("7.3.84v", lambda s: s.lak in PRESENT and s.v[-1:] == ["u"] and s.strong() and "3.4.87" not in s.done, lambda s: s.v.__setitem__(-1, "o"), "guṇa of the aṅga-final u (śnu, u) before the pit sārvadhātuka (sunoti, karoti, tanoti)")
    add("7.3.83", lambda s: s.lak == "laṅ" and s.aff == ["u", "s"] and s.r[-1] in GUNA and not s.vsit, lambda s: setattr(s, "r", s.r[:-1] + tok(GUNA[s.r[-1]])), "guṇa before jus (abibhayuḥ, ajuhavuḥ, apiparuḥ) — the para rule against 6.4.82 / 6.4.87 / 7.1.102 (1.4.2)")
    add("6.4.110", lambda s: s.root == "kṛ" and s.v == ["u"] and s.lak in PRESENT and not s.strong() and s.r == tok("kar"), lambda s: s.r.__setitem__(1, "u"), "the a of kar → u before the kit / ṅit sārvadhātuka (kurutaḥ, kurvanti, kurute)")
    add("6.4.108", lambda s: s.r == tok("kur") and s.v == ["u"] and s.nxt() and s.nxt()[0] in ("m", "v"), lambda s: setattr(s, "v", []), "the u of karoti always dropped before m / v (kurvaḥ, kurmaḥ; not across the sīyuṭ: kurvīvahi)")
    add("6.4.109", lambda s: s.r == tok("kur") and s.v == ["u"] and s.pre[:1] == ["y"], lambda s: setattr(s, "v", []), "the u of karoti dropped before y (kuryāt)")
    add("6.4.107", lambda s: s.v[-1:] == ["u"] and s.nxt() and s.nxt()[0] in ("m", "v") and s.root != "kṛ" and ((s.v == tok("nu") and s.r[-1] in V) or (s.v == ["u"] and s.r[-2] in V)), lambda s: s.v.pop(), "the u of the affix dropped before m / v when not preceded by a conjunct — optionally; the lopa branch is realised (sunvaḥ, tanmaḥ; sunuvaḥ, tanumaḥ recorded)")
    add("6.4.77", lambda s: s.v == tok("nu") and s.nxt() and s.nxt()[0] in V and s.r[-1] not in V, lambda s: s.v.__setitem__(-1, "uv"), "u of śnu after a conjunct → uvaṅ before a vowel (āpnuvanti, śaknuvaḥ)")
    add("6.4.81", lambda s: s.up_root == "iṇ" and s.r == ["i"] and s.nxt() and s.nxt()[0] in V, lambda s: s.r.__setitem__(-1, "y"), "the i of iṇ → yaṇ before a vowel (yanti; not across the yāsuṭ: iyām, iyuḥ)")
    add("6.4.82", lambda s: s.ab and "ām" not in s.flags and s.r[-1] in ("i", "ī") and not _conj_before_final(s) and s.after_root() and s.after_root()[0] in V and not s.v, lambda s: s.r.__setitem__(-1, "y"), "the i / ī of a polysyllabic aṅga not after a conjunct → yaṇ before a vowel (bibhyati; ninyatuḥ, ninyiva in liṭ)")
    add("6.4.77d", lambda s: not s.v and ((s.lak in PRESENT and (not s.strong() or (s.up_root == "ṣūṅ" and "śap-luk" in s.flags))) or (s.lak == "liṭ" and s.kit() and s.after_root() and s.after_root()[0] in V)) and s.r[-1] in ("i", "ī", "u", "ū") and ((s.lak == "liṭ" and s.after_root() and s.after_root()[0] in V) or (s.nxt() and s.nxt()[0] in V)) and not (s.root == "hu" and "ślu" in s.flags) and not (s.ab and s.r[-1] in ("i", "ī") and not _conj_before_final(s)), lambda s: s.r.__setitem__(-1, {"i": "iy", "ī": "iy", "u": "uv", "ū": "uv"}[s.r[-1]]), "iyaṅ / uvaṅ for the root-final i / u before a vowel (6.4.77 dhātu: yuvanti, stuvanti, ūrṇuvanti, hnuvāte, jihriyati; suvai, where 7.3.88 keeps the guṇa off)")
    add("6.4.87", lambda s: not (s.strong() and s.lak in PRESENT) and s.nxt() and s.nxt()[0] in V and ((s.v == tok("nu") and s.r[-1] in V) or (s.root == "hu" and "ślu" in s.flags and s.r[-1] == "u")), lambda s: s.v.__setitem__(-1, "v") if s.v else s.r.__setitem__(-1, "v"), "u of hu / śnu after a non-conjunct → v before the vowel-initial sārvadhātuka (juhvati, sunvanti, cinvāte, śṛṇvanti)")
    add("6.4.112", lambda s: s.lak in PRESENT and not s.strong() and s.nxt() and ((s.v == tok("nā") and s.nxt()[0] in V and not _siyut(s)) or ((s.ab or "abhyasta" in s.flags) and s.r[-1:] == ["ā"] and ((s.nxt()[0] in V and not _siyut(s)) or (s.root in GHU and s.aff != ["h", "i"])))), lambda s: s.v.pop() if s.v else s.r.pop(), "the ā of śnā and of the abhyasta root dropped before the kit / ṅit sārvadhātuka — before a vowel (krīṇanti, punate, dadati, dadāte) and, for the ghu (1.1.20), before hal too (dattaḥ, dhattaḥ: 6.4.113's ī is aghoḥ; not before hi, where 6.4.119 is para and the lopa would be asiddhavat, 6.4.22: dhehi)")
    add("6.4.118", lambda s: s.up_root in ("o~hāk",) and s.lak == "liṅ" and s.r[-1:] == ["ā"] and s.pre[:1] == ["y"], lambda s: s.r.pop(), "the ā of hā dropped before y (jahyāt)")
    add("6.4.113", lambda s: s.lak in PRESENT and not s.strong() and s.nxt() and (s.nxt()[0] not in V or _siyut(s)) and ((s.v == tok("nā")) or (s.ab and s.r[-1:] == ["ā"] and s.root not in GHU and not s.v)), lambda s: s.v.__setitem__(-1, "ī") if s.v else s.r.__setitem__(-1, "ī"), "the ā of śnā and of the abhyasta non-ghu root → ī before the hal-initial kit / ṅit sārvadhātuka (krīṇītaḥ, punīte, mimīte, jihīte, jahītaḥ)")
    add("7.4.25", lambda s: s.lak == "āśīrliṅ" and s.P() and s.r[-1:] and s.r[-1] in ("i", "u") and s.pre[:1] == ["y"] and "7.4.28" not in s.done and "ṇic" not in s.flags, lambda s: s.r.__setitem__(-1, {"i": "ī", "u": "ū"}[s.r[-1]]), "i / u lengthened before the y-initial ārdhadhātuka that is not kṛt or sārvadhātuka (stūyāt, cīyāt, hūyāt, īyāt); not the i of 7.4.28's riṅ, the later special rule (kriyāt)")
    add("6.1.78v", lambda s: s.v[-1:] and s.v[-1] in ("e", "o") and s.nxt() and s.nxt()[0] in V, lambda s: s.v.__setitem__(-1, {"e": "ay", "o": "av"}[s.v[-1]]), "ec of the vikaraṇa → ay / av before a vowel (aśnavāni, sunavai)")
    add("6.1.78", lambda s: s.r[-1] in ("e", "o", "ai", "au") and s.after_root() and s.after_root()[0] in V, lambda s: setattr(s, "r", s.r[:-1] + {"e": ["ay"], "o": ["av"], "ai": ["ā", "y"], "au": ["ā", "v"]}[s.r[-1]]), "ec → ay / av / āy / āv before a vowel (bhav-a, nay-a, nināy-a)")
    add("7.2.80", lambda s: s.lak == "liṅ" and s.P() and (s.r + s.it + s.v)[-1:] == ["a"] and s.pre == ["y", "ā"], lambda s: setattr(s, "pre", ["i", "y"]), "yā (yās) → iy after a")
    add("7.2.81", lambda s: s.A() and s.a_final() and s.aff[:1] == ["ā"] and s.up in ("ātām", "āthām") and s.ngit() and not s.pre, lambda s: (setattr(s, "pre", ["i", "y"]), setattr(s, "aff", s.aff[1:])), "the ā of the ṅit (1.2.4) ātmanepada affix → iy after a (ātām, āthām)")
    add("6.1.96", lambda s: s.pre == ["y", "ā"] and s.aff == ["u", "s"], lambda s: s.pre.pop(), "the ā of yā before us, not at the end of the pada → pararūpa (adyuḥ, juhuyuḥ)")
    add("6.4.101", lambda s: s.aff == ["h", "i"] and ((s.root == "hu" and "ślu" in s.flags) or (s.anga()[-1] in JHAL)), lambda s: setattr(s, "aff", ["dh", "i"]), "hi → dhi after hu and after a jhal (juhudhi, addhi, runddhi)")
    add("6.4.119", lambda s: (s.aff == ["dh", "i"] or (s.aff == ["h", "i"] and s.root in GHU)) and (s.root in GHU or s.root == "as") and "6.4.119" not in s.done, lambda s: (setattr(s, "r", ["e"] if s.root == "as" else s.r[:-1] + ["e"]), setattr(s, "ab", [])), "the ghu and as → e before dhi, with the abhyāsa dropped (dehi, dhehi, edhi)")
    add("3.1.83", lambda s: s.v in (tok("nā"), tok("nī")) and s.aff == ["h", "i"] and s.r[-1] not in V, lambda s: setattr(s, "v", tok("āna")), "śānac for śnā before hi after a consonant-final root (aśāna, badhāna, gṛhāṇa — then 6.4.105)")
    add("6.4.106", lambda s: s.aff == ["h", "i"] and s.v[-1:] == ["u"] and ((s.v == tok("nu") and s.r[-1] in V) or (s.v == ["u"] and (s.r[-1] in V or (len(s.r) >= 2 and s.r[-2] in V)))), lambda s: setattr(s, "aff", []), "hi → luk after the affix u not preceded by a conjunct (sunu, kuru, tanu, sanu; āpnuhi keeps hi)")
    add("6.4.105", lambda s: s.a_final() and s.aff == ["h", "i"] and "6.4.36" not in s.flags, lambda s: setattr(s, "aff", []), "hi → luk after a (bhava); not after the ja of 6.4.36, which is asiddhavat here (6.4.22: jahi)")
    add("7.3.101", lambda s: s.a_final() and s.aff[:1] and s.aff[0] in YAN_INIT and s.aff[0] != "ā" and "3.4.92" not in s.done, lambda s: _set_last_anga(s, ["ā"]), "a → ā before the yañ-initial sārvadhātuka (mi, vas, mas, vahi, mahi; va, ma)")
    add("8.2.26", lambda s: (s.v == ["s"] and not s.it and s.r[-1] in JHAL and s.aff[:1] and s.aff[0] in JHAL) or (not s.v and not s.it and not _yas(s) and s.r[-1] == "s" and s.aff[:2] == ["dh", "v"]) or (s.v[-1:] == ["s"] and s.lak == "luṭ" and s.aff[:2] == ["dh", "v"]), lambda s: (setattr(s, "v", []) if s.v == ["s"] else (s.v.pop() if s.v else s.r.pop())), "the s dropped between jhal and jhal — the sic (alabdha, alabdhāḥ), the s of vas / tās before dhve (vadhve, labdhādhve)")
    add("8.2.36", lambda s: not _yas(s) and s.up_root in SATVA_36 and s.r[-1] in ("j", "ś") and s.after_root() and s.after_root()[0] in JHAL and not s.it, lambda s: s.r.__setitem__(-1, "ṣ"), "j / ś of the listed roots → ṣ before jhal (mārṣṭi, kaṣṭe, īṣṭe)")
    add("8.3.60", lambda s: not _yas(s) and s.up_root == "śāsu~" and s.r == tok("śis"), lambda s: s.r.__setitem__(-1, "ṣ"), "s of śās (as śis) → ṣ (śiṣṭaḥ, śiṣvaḥ)")
    add("8.2.31", lambda s: not _yas(s) and s.r[-1] == "h" and s.up_root == "liha~" and s.after_root() and s.after_root()[0] in JHAL and not s.it, lambda s: s.r.__setitem__(-1, "ḍh"), "h → ḍh before jhal (liḍh-)")
    add("8.2.32", lambda s: not _yas(s) and s.r[-1] == "h" and s.r[0] == "d" and s.after_root() and s.after_root()[0] in JHAL and not s.it, lambda s: s.r.__setitem__(-1, "gh"), "h of a d-initial root → gh before jhal (dogh-, dugh-)")
    add("8.2.37", lambda s: not _yas(s) and s.r[-1] in JHAS and s.r[0] in ("b", "g", "d", "ḍ") and not s.it and s.after_root() and (s.after_root()[0] == "s" or (not s.v and s.aff[:2] == ["dh", "v"])), lambda s: s.r.__setitem__(0, {"b": "bh", "g": "gh", "d": "dh", "ḍ": "ḍh"}[s.r[0]]), "the initial baś of a monosyllable ending in jhaṣ → bhaṣ before s / dhv (dhokṣi, dhugdhve)")
    add("8.2.38", lambda s: s.root == "dhā" and s.ab == ["d", "a"] and s.r == ["dh"] and s.after_root() and s.after_root()[0] in ("t", "th", "s", "dh"), lambda s: s.ab.__setitem__(0, "dh"), "the d of dhā's abhyāsa → dh before t / th / s / dhv (dhattaḥ, dhatse, dhaddhve)")
    add("8.2.41", lambda s: not _yas(s) and s.r[-1] in ("ṣ", "ḍh") and not s.it and s.after_root()[:1] == ["s"] and not _aprkta(s), lambda s: s.r.__setitem__(-1, "k"), "ṣ / ḍh → k before s (vevekṣi); not before the apṛkta s, which 6.1.68 has already dropped (adveṭ, aleṭ)")
    add("8.2.30", lambda s: s.r[-1] in ("c", "j") and s.after_root() and s.after_root()[0] in JHAL, lambda s: s.r.__setitem__(-1, {"c": "k", "j": "g"}[s.r[-1]]), "cu → ku before jhal (riṇakti, vinakti)")
    add("8.2.40", lambda s: s.r[-1] in JHAS and s.root != "dhā" and s.after_root() and s.after_root()[0] in ("t", "th") and not s.it and not _aprkta(s), lambda s: (s.v if s.v else s.aff).__setitem__(0, "dh"), "t / th → dh after a jhaṣ, not after dhā (labh-dhās, labh-dha, run-dh-dhaḥ; dhattaḥ keeps t); not the apṛkta t, which 6.1.68 drops first (8.2.1: aruṇat, adhok)")
    add("8.4.53", lambda s: s.r[-1] in JAS_ALL and s.r[-1] != "s" and s.after_root() and s.after_root()[0] in ("dh", "d", "b", "g", "j") and not (s.r[-1] == "ḍh" and s.after_root()[0] == "dh") and not _aprkta(s), lambda s: s.r.__setitem__(-1, JAS_ALL[s.r[-1]]), "jhal → jaś before jhaś (labdhā, kaḍ-ḍhve; vagdhi, kṛnddhi, riṅgdhi — 8.4.65's optional lopa recorded); the ḍh + dh of lih is left to 8.4.41 and 8.3.13")
    add("8.4.55", lambda s: s.r[-1] in CAR and s.after_root() and s.after_root()[0] in KHAR and not _aprkta(s), lambda s: s.r.__setitem__(-1, CAR[s.r[-1]]), "jhal → car before khar (lapsya, lapsīṣṭa); not before the apṛkta t, which 6.1.68 drops first (8.2.1: adhok)")
    add("6.4.143", lambda s: s.lak == "luṭ" and s.aff[:1] == ["ḍ"] and s.v[-2:] == ["ā", "s"], lambda s: (setattr(s, "v", s.v[:-2]), s.aff.pop(0)), "the ṭi of the aṅga dropped before the ḍit ḍā (bhavitā, labdhā)")
    add("7.4.51", lambda s: s.v[-1:] == ["s"] and s.lak == "luṭ" and s.aff[:1] == ["r"], lambda s: s.v.pop(), "the s of tās dropped before r (bhavitārau, bhavitāraḥ)")
    add("7.4.50", lambda s: s.v[-1:] == ["s"] and s.lak == "luṭ" and s.aff[:1] == ["s"], lambda s: s.v.pop(), "the s of tās dropped before the s-initial sārvadhātuka (bhavitāsi, labdhāse)")
    add("7.4.52", lambda s: s.v[-1:] == ["s"] and s.lak == "luṭ" and s.aff[:1] == ["e"], lambda s: s.v.__setitem__(-1, "h"), "the s of tās → h before e (labdhāhe)")
    # ---- phase 3: junction -----------------------------------------------------------------
    add("6.1.77", lambda s: ((s.kit() or (s.flags & {"ślu", "abhyasta"} and not s.pit and "ām" not in s.flags)) and s.r[-1] in YAN and s.r[-1] not in ("i", "ī", "u", "ū") and s.after_root() and s.after_root()[0] in V) or (s.v == ["u"] and s.nxt() and s.nxt()[0] in V), lambda s: s.r.__setitem__(-1, YAN[s.r[-1]]) if not (s.v == ["u"] and s.nxt() and s.nxt()[0] in V) else s.v.__setitem__(-1, "v"), "ik → yaṇ before a vowel: the kit liṭ cells (ninyatuḥ, cakratuḥ, ninyiva), the ṛ of the abhyasta before the ṅit vowel (piprati, bibhrati) and the u-vikaraṇa before anti (kurvanti)")
    add("6.4.78", lambda s: s.lak == "liṭ" and s.ab and s.ab[-1] in ("i", "ī", "u", "ū") and s.r[:1] and s.r[0][0] in V and s.r[0][0] != s.ab[-1] and s.r[0][0] not in HRASVA.get(s.ab[-1], ""), lambda s: s.ab.__setitem__(-1, {"i": "iy", "ī": "iy", "u": "uv", "ū": "uv"}[s.ab[-1]]), "iyaṅ / uvaṅ for the abhyāsa vowel before a dissimilar vowel (iyāya, iyeṣa)")
    add("6.1.101a", lambda s: s.lak == "liṭ" and s.ab in (["u"], ["i"]) and s.r[:1] == s.ab, lambda s: (setattr(s, "ab", []), s.r.__setitem__(0, {"u": "ū", "i": "ī"}[s.r[0]])), "the abhyāsa u / i + the root's u / i → the long savarṇa (ūce, ūcatuḥ)")
    add("6.1.87", lambda s: (s.v[-1:] == ["a"] and s.pre[:1] and s.pre[0] in ("i", "ī")) or (s.a_final() and s.aff[:1] and s.aff[0] in ("i", "ī", "u", "ū")),
        lambda s: (s.v.pop(), s.pre.__setitem__(0, "e")) if s.pre[:1] and s.pre[0] in ("i", "ī") else (_set_last_anga(s, []), s.aff.__setitem__(0, GUNA[s.aff[0]])), "a + ik → guṇa (bhave-y, labhe-y, labhe)")
    add("6.1.97", lambda s: s.a_final() and s.aff[:1] and s.aff[0] in ("a", "e", "o") and not s.pre, lambda s: _set_last_anga(s, []), "a + a guṇa vowel (a, e, o) → pararūpa (abhavam; labhe from labha + e)")
    add("6.1.101", lambda s: (s.a_final() and s.aff[:1] == ["ā"]) or (s.anga()[-1:] == ["ā"] and s.aff[:1] in (["a"], ["ā"])) or ((s.r + s.it + s.v)[-1:] == ["ī"] and s.pre[:1] == ["ī"]), lambda s: s.pre.pop(0) if s.pre[:1] == ["ī"] and (s.r + s.it + s.v)[-1:] == ["ī"] else (_set_last_anga(s, ["ā"]), s.aff.pop(0)), "a + ā / ā + a / ī + ī → the long savarṇa (bhavāni, labhāvahai, yānti, dhunīta)")
    add("6.1.88", lambda s: (s.anga()[-1:] and s.anga()[-1] in ("a", "ā") and s.aff[:1] in (["ai"], ["au"]) and not s.pre) or s.aff[:2] == ["ā", "ai"], lambda s: s.aff.pop(0) if s.aff[:2] == ["ā", "ai"] else _set_last_anga(s, []), "a / ā + ai / au → vṛddhi (labhai, labhāvahai; dadau, tasthau)")
    add("6.1.66", lambda s: s.pre[-1:] == ["y"] and s.aff[:1] and s.aff[0] in VAL, lambda s: s.pre.pop(), "y dropped before val (bhavet, bhaveva, labheta, labhete)")
    # ---- phase 4: tripādī -----------------------------------------------------------------
    add("6.1.68", lambda s: not s.v and not s.it and not s.pre and len(s.aff) == 1 and s.aff[0] not in V and s.up in ("tip", "sip") and s.r[-1:] and s.r[-1] not in V, lambda s: s.aff.pop(), "the apṛkta hal (the t / s of tip / sip) dropped after a hal (abhinat, abibhaḥ, ahan, acakāt, adhok; theorum/139 had cited 8.2.23 / 8.2.24 for these — corrected: 8.2.23 is the saṁyogānta rule of abhavan)")
    add("8.2.29", lambda s: s.pre[-1:] == ["s"] and s.aff in (["t"], ["s"]), lambda s: s.pre.pop(), "the s beginning the pada-final conjunct dropped (bhūyāt, bhūyāḥ)")
    add("8.2.23", lambda s: s.aff[-2:] == ["n", "t"], lambda s: s.aff.pop(), "the final of the pada-final conjunct dropped (abhavan)")
    add("8.2.25", lambda s: (not s.v and not s.it and not s.pre and s.r[-1:] == ["s"] and s.aff == ["dh", "i"]) or (s.lak == "luṅ" and s.v == ["s"] and s.aff[:2] == ["dh", "v"]), lambda s: s.r.pop() if not s.v else setattr(s, "v", []), "s dropped before dhi (hindhi, cakādhi) and the sic before dhvam (aceḍhvam, aidhidhvam, akṛḍhvam)")
    add("8.2.27", lambda s: s.lak == "luṅ" and s.v == ["s"] and not s.it and s.r[-1] in ("a", "i", "u", "ṛ") and s.aff[:1] and s.aff[0] in JHAL, lambda s: setattr(s, "v", []), "the sic dropped after a short vowel before jhal (akṛta, akṛthāḥ, adita, adhita)")
    add("8.2.28", lambda s: s.lak == "luṅ" and s.v == ["s"] and s.it and s.aff[:1] == ["ī"], lambda s: (setattr(s, "v", []), setattr(s, "it", [])), "the sic dropped after iṭ before īṭ, the i + ī then one ī by 6.1.101 (adevīt, agrahīt, ānīt, abhāsīt, ajāgarīt)")
    add("8.2.37e", lambda s: not s.aff and not s.v and not s.it and not s.pre and s.r[-1] in JHAS and s.r[0] in ("b", "g", "d", "ḍ"), lambda s: s.r.__setitem__(0, {"b": "bh", "g": "gh", "d": "dh", "ḍ": "ḍh"}[s.r[0]]), "8.2.37 at the end of the pada (ante: adhok, adhek)")
    add("8.2.39", lambda s: not s.aff and not s.v and not s.it and not s.pre and s.r[-1:] and s.r[-1] in JAS_ALL and s.r[-1] != "s", lambda s: s.r.__setitem__(-1, JAS_ALL[s.r[-1]]), "jhal → jaś at the end of the pada (adhog, adveḍ, aleḍ, amārḍ, aruṇad)")
    add("8.2.73", lambda s: not s.aff and not s.v and not s.it and not s.pre and s.r[-1:] == ["s"] and s.up == "tip" and s.root != "as", lambda s: s.r.__setitem__(-1, "d"), "the root-final s → d before tip (its apṛkta t already dropped: ahinad, acakād, aśād)")
    add("8.2.74", lambda s: not s.aff and not s.v and not s.it and not s.pre and s.r[-1:] == ["s"] and s.up == "sip" and s.root != "as", lambda s: s.r.__setitem__(-1, "d"), "the root-final s before sip: ru optionally (acakāḥ, ahinaḥ — recorded), otherwise the d of 8.2.72 (acakād, ahinad: the branch realised)")
    add("8.3.24", lambda s: any(s.r[i] == "n" and i + 1 < len(s.r + s.it + s.v + s.pre + s.aff) and (s.r + s.it + s.v + s.pre + s.aff)[i + 1] in JHAL for i in range(len(s.r))), lambda s: [s.r.__setitem__(i, "ṁ") for i in range(len(s.r)) if s.r[i] == "n" and i + 1 < len(s.r + s.it + s.v + s.pre + s.aff) and (s.r + s.it + s.v + s.pre + s.aff)[i + 1] in JHAL], "n → anusvāra before jhal, not at the end of the pada (hiṁsvaḥ, hiṁsanti, haṁsi, kaṁste; run-dh → ruṁ-dh, read again by 8.4.58)")
    add("8.3.24m", lambda s: s.r[-1:] == ["m"] and s.after_root() and s.after_root()[0] in JHAL, lambda s: s.r.__setitem__(-1, "ṁ"), "the m too (ca) → anusvāra before jhal, not at the end of the pada (gaṁ-tā, read again by 8.4.58: gantā; gamyāt keeps m: y is not jhal)")
    add("8.4.2", lambda s: _natva_site(s) is not None, lambda s: _natva_set(s), "n of the affix / of śnam → ṇ after r / ṛ / ṣ across vowels, ku, pu (8.4.1 with 8.4.2: krīṇāti, śṛṇoti, ruṇaddhi, kṣuṇatti; not the kṣubhnādi, 8.4.39; not at the end of the pada, 8.4.37)")
    add("8.4.40", lambda s: s.v[:1] == ["n"] and s.r[-1] in ("c", "j", "ñ"), lambda s: s.v.__setitem__(0, "ñ"), "n → ñ after cu (khacñāti); not after ś (8.4.44 śāt: aśnāti, kliśnāti)")
    add("8.4.41n", lambda s: s.v[:1] == ["n"] and s.r[-1] in ("ṭ", "ṭh", "ḍ", "ḍh"), lambda s: s.v.__setitem__(0, "ṇ"), "n → ṇ after ṭu (8.4.41: mṛḍṇāti)")
    add("8.4.58", lambda s: any(s.r[i] == "ṁ" and i + 1 < len(s.r + s.it + s.v + s.pre + s.aff) and (s.r + s.it + s.v + s.pre + s.aff)[i + 1] in YAY for i in range(len(s.r))), lambda s: [s.r.__setitem__(i, SAVARNA[(s.r + s.it + s.v + s.pre + s.aff)[i + 1]]) for i in range(len(s.r)) if s.r[i] == "ṁ" and i + 1 < len(s.r + s.it + s.v + s.pre + s.aff) and (s.r + s.it + s.v + s.pre + s.aff)[i + 1] in YAY], "anusvāra → the parasavarṇa nasal before yay (rundhanti, bhindanti; hiṁs keeps the anusvāra before s)")
    add("8.3.59r", lambda s: s.lak == "liṭ" and s.ab and s.ab[-1] in IN and s.r[:1] == ["s"] and s.r[1:2] and s.r[1] not in ("r", "k", "kh", "g", "gh"), lambda s: s.r.__setitem__(0, "ṣ"), "the root-initial s after the abhyāsa's iṇ → ṣ (siṣeva, siṣedha, suṣvāpa, suṣṇāva, tuṣṭāva; sasāra keeps s after a; before the velar the generator keeps s — cuskāva, caskambha — and that reading is followed, recorded)")
    add("8.3.59", lambda s: any(_s_after_in(s)), lambda s: _satva(s), "the s of an affix / augment → ṣ after iṇ or ku (8.3.57 iṇkoḥ: bhaviṣyati, neṣyati, edhiṣīṣṭa, lapsīṣṭa, nenekṣi)")
    add("8.4.41", lambda s: ((s.v[-1:] == ["ṣ"] or (not s.v and not s.it and s.r[-1:] and s.r[-1] in ("ṣ", "ṭ", "ṭh", "ḍ", "ḍh"))) and not s.pre and s.aff[:1] and s.aff[0] in ("t", "th", "dh")) or any(s.aff[i] in ("t", "th") and s.aff[i - 1] == "ṣ" for i in range(1, len(s.aff))) or (not s.it and s.r[-1:] and s.r[-1] in ("ṣ", "ṭ", "ṭh", "ḍ", "ḍh") and s.v[:1] and s.v[0] in ("t", "th", "dh")),
        lambda s: ([s.aff.__setitem__(i, {"t": "ṭ", "th": "ṭh", "dh": "ḍh"}[s.aff[i]]) for i in range(len(s.aff)) if s.aff[i] in ("t", "th", "dh") and (s.aff[i - 1] if i else (s.v[-1:] or s.r[-1:] or [""])[0]) in ("ṣ", "ṭ", "ṭh", "ḍ", "ḍh")], s.v.__setitem__(0, {"t": "ṭ", "th": "ṭh", "dh": "ḍh"}[s.v[0]]) if (not s.it and s.r[-1:] and s.r[-1] in ("ṣ", "ṭ", "ṭh", "ḍ", "ḍh") and s.v[:1] and s.v[0] in ("t", "th", "dh")) else None), "t / th / dh → ṭ / ṭh / ḍh after ṣ / ṭu (lapsīṣṭa, anaiṣṭām, aidhiṣṭhāḥ, dveṣṭi, īṭṭe, līḍhaḥ, kaḍḍhve; the t of tās too: dveṣṭā, leḍhā)")
    add("8.3.78", lambda s: s.A() and s.aff[:2] == ["dh", "v"] and not s.it and s.r[-1] in IN and ((s.lak == "āśīrliṅ" and s.pre[-1:] == ["ī"]) or (s.lak == "liṭ" and "ām" not in s.flags) or (s.lak == "luṅ" and not s.v)), lambda s: s.aff.__setitem__(0, "ḍh"), "the dh of ṣīdhvam, of liṭ's dhve and of luṅ's dhvam → ḍh after the iṇ-final aṅga (bhṛṣīḍhvam, kṛṣīḍhvam, cakṛḍhve, aceḍhvam, akṛḍhvam); after iṭ optionally (8.3.79 vibhāṣeṭaḥ: stariṣīdhvam realised, stariṣīḍhvam recorded)")
    add("8.4.41r", lambda s: "8.3.59r" in s.done and s.r[:2] and s.r[0] == "ṣ" and s.r[1] in ("t", "th", "n"), lambda s: s.r.__setitem__(1, {"t": "ṭ", "th": "ṭh", "n": "ṇ"}[s.r[1]]), "ṣṭutva of the t / n after the root's ṣ (tuṣṭāva, tuṣṭuve, suṣṇāva, tiṣṭighe)")
    add("8.3.13", lambda s: s.r[-1:] == ["ḍh"] and (s.aff[:1] == ["ḍh"] or s.v[:1] == ["ḍh"]), lambda s: s.r.pop(), "ḍh dropped before ḍh (li-ḍhaḥ, le-ḍhā)")
    add("6.3.111", lambda s: "8.3.13" in s.done and s.r[-1] in ("a", "i", "u"), lambda s: s.r.__setitem__(-1, {"a": "ā", "i": "ī", "u": "ū"}[s.r[-1]]), "the aṇ before the dropped ḍh lengthened (līḍhaḥ; leḍhi keeps e)")
    add("8.4.56", lambda s: not s.aff and not s.v and not s.it and not s.pre and s.r[-1:] and s.r[-1] in ("g", "j", "ḍ", "d", "b"), lambda s: s.r.__setitem__(-1, {"g": "k", "j": "c", "ḍ": "ṭ", "d": "t", "b": "p"}[s.r[-1]]), "the jaś → car at pause, optionally: the car branch realised, the jaś (adhog, adveḍ, ahinad) recorded")
    add("8.2.66", lambda s: s.aff[-1:] == ["s"], lambda s: s.aff.__setitem__(-1, "r"), "s → ru at the end of the pada")
    add("8.3.15", lambda s: (s.aff[-1:] == ["r"] and s.up not in ("ran",)) or (not s.aff and not s.v and not s.pre and s.r[-1:] == ["r"]), lambda s: s.aff.__setitem__(-1, "ḥ") if s.aff else s.r.__setitem__(-1, "ḥ"), "r → visarjanīya at pause")
    return R


# rows whose surface effect coincides with another row on this suite (recorded, not counted as vacuous):
SURFACE_COINCIDENT = {"3.1.57": "irito vā is an option and the lane oracle lists both branches (abhidat / abhaitsīt): the row realises the aṅ branch, the generator's first, and no cell breaks without it (theorum/146)", "7.3.73": "lug vā duhadihalihaguhām ātmanepade dantye is an option and the oracle lists both (adugdha / adhukṣata): the luk branch realised, recorded, not load-bearing (theorum/146)", "6.4.2": "halaḥ lengthens the samprasāraṇa i of jyā before the kit yāsuṭ (jīyāt) — the attribution the Kāśikā gives; 7.4.25 would lengthen the same i, so on this table the row is recorded in the path but no cell breaks without it (theorum/144)", "8.4.56": "vā 'vasāne is an option and the open-lane oracle lists both branches (adhok / adhog): the row realises the car branch, the citation form, and no cell of the suite ends in a jaś — so the row is applied and recorded but cannot be load-bearing against a set-valued oracle (theorum/143)", "7.1.58": "the nuṁ of the idit hisi~ is dropped again by 6.4.23 in every śnam cell of the suite (hinasti, hiṁsanti: the anusvāra there is śnam's n); a cell of hiṁs without śnam (hiṁsitum) is not in the suite, so the row is kept, applied and recorded but not counted as load-bearing", "3.4.92": "āṭ before ni / va / ma gives bhavāni, bhavāva, bhavāma; without it 7.3.101's dīrgha gives the same surface (theorum/96 recorded the same); labhai from a + ai by 6.1.88 either way"}
RULES = rules()
IDS = [r[0] for r in RULES]


def conjugate(root: str, lak: str, code: str, off=(), pada=None) -> tuple[str, list[str]]:
    s = S(root, lak, code, pada)
    s.path.append(f"{root} ({s.up_root}, {s.pada}) + {lak} → {s.up} → {''.join(s.aff)}")
    for n, guard, action, note in RULES:
        if n in off:
            continue
        before = (s.form(), frozenset(s.flags), s.pit)
        if guard(s):
            action(s)
            after = (s.form(), frozenset(s.flags), s.pit)
            if after != before:
                s.done.add(n); s.path.append(f"{n} {note}: {s.form()}")
    if "ām" in s.flags:   # 3.1.40 kṛñ cānuprayujyate liṭi: the liṭ of bhū (3.1.40's second alternative, the generator's first) follows the ām-form; kṛ and as recorded
        tail = conjugate("bhū", "liṭ", code, pada="P")[0]
        s.path.append(f"3.1.40 the liṭ of bhū anuprayukta after the ām-form (kṛ / as recorded): {s.form()}{tail}")
        return s.form() + tail, s.path
    return s.form(), s.path


A6 = ["3s", "3d", "3p", "1s", "2s", "1p"]; A4 = ["3s", "3d", "3p", "1s"]; P3 = ["3s", "3d", "3p"]; L5 = ["3s", "3d", "3p", "1d", "1p"]
# the suite: (root, lakāra, cells) — the cells each earlier packet certified
SUITE = [(r, l, CODES) for r in ("bhū", "gam", "nī", "edh", "labh") for l in PRESENT] + [("bhū", "lṛṭ", CODES), ("gam", "lṛṭ", CODES), ("nī", "lṛṭ", CODES), ("labh", "lṛṭ", A6), ("edh", "lṛṭ", A6),
         ("bhū", "luṭ", CODES), ("nī", "luṭ", CODES), ("labh", "luṭ", A6), ("edh", "luṭ", A6),
         ("bhū", "āśīrliṅ", P3), ("gam", "āśīrliṅ", P3), ("nī", "āśīrliṅ", P3), ("labh", "āśīrliṅ", A4), ("edh", "āśīrliṅ", A4),
         ("bhū", "luṅ", CODES), ("gam", "luṅ", CODES), ("nī", "luṅ", CODES), ("labh", "luṅ", A6), ("edh", "luṅ", A6),
         ("bhū", "liṭ", L5), ("gam", "liṭ", L5), ("kṛ", "liṭ", L5, "P"), ("nī", "liṭ", L5)]
# theorum/132: the vikaraṇa classes in laṭ, on the cells of the grammar-verification branch's quoted present tables (research/panini_grammar/vikarana_lat, non_thematic_lat: Kāśikā / Kaumudī anchors)
V_ORACLE = {
    ("pac", "P"): dict(zip(CODES, "pacati pacataḥ pacanti pacasi pacathaḥ pacatha pacāmi pacāvaḥ pacāmaḥ".split())),
    ("pac", "A"): dict(zip(CODES, "pacate pacete pacante pacase pacethe pacadhve pace pacāvahe pacāmahe".split())),
    ("div", "P"): {"3s": "dīvyati"}, ("siv", "P"): {"3s": "sīvyati"}, ("śam", "P"): {"3s": "śāmyati"},
    ("tud", "P"): {"3s": "tudati"}, ("nud", "P"): {"3s": "nudati"}, ("tud", "A"): {"3s": "tudate"}, ("nud", "A"): {"3s": "nudate"}, ("cur", "P"): {"3s": "corayati"},
    ("su", "P"): {"3s": "sunoti", "3d": "sunutaḥ", "3p": "sunvanti", "2s": "sunoṣi", "1s": "sunomi", "1d": "sunvaḥ", "1p": "sunmaḥ"}, ("su", "A"): {"3s": "sunute", "3d": "sunvāte", "1d": "sunvahe"},
    ("ci", "P"): {"3s": "cinoti", "3d": "cinutaḥ", "3p": "cinvanti"}, ("ci", "A"): {"3d": "cinvāte", "3p": "cinvate"},
    ("śru", "P"): {"3s": "śṛṇoti", "3d": "śṛṇutaḥ", "3p": "śṛṇvanti"}, ("āp", "P"): {"3s": "āpnoti", "3d": "āpnutaḥ", "3p": "āpnuvanti", "1d": "āpnuvaḥ"}, ("śak", "P"): {"3s": "śaknoti", "3p": "śaknuvanti", "1d": "śaknuvaḥ", "1p": "śaknumaḥ"},
    ("tan", "P"): {"3s": "tanoti", "1d": "tanvaḥ", "1p": "tanmaḥ"}, ("tan", "A"): {"3s": "tanute"},
    ("kṛ", "P"): {"3s": "karoti", "3d": "kurutaḥ", "3p": "kurvanti", "2s": "karoṣi", "1s": "karomi", "1d": "kurvaḥ", "1p": "kurmaḥ"}, ("kṛ", "A"): {"3s": "kurute"},
    ("krī", "P"): {"3s": "krīṇāti", "3d": "krīṇītaḥ", "3p": "krīṇanti"}, ("krī", "A"): {"3s": "krīṇīte", "3d": "krīṇāte"},
    ("pū", "P"): {"3s": "punāti", "3d": "punītaḥ", "2d": "punīthaḥ"}, ("pū", "A"): {"3s": "punīte", "3p": "punate"},
    ("lū", "P"): {"3s": "lunāti", "3d": "lunītaḥ", "2d": "lunīthaḥ"}, ("lū", "A"): {"3s": "lunīte", "3p": "lunate"},
}
V_ORACLE.update({   # theorum/133: adādi, juhotyādi, rudhādi (research/panini_grammar/exception_lat, abhyasa_lat, snam_lat: Kaumudī / Laghukaumudī anchors)
    ("ad", "P"): {"3s": "atti", "3d": "attaḥ", "3p": "adanti", "2s": "atsi", "2d": "atthaḥ", "2p": "attha", "1s": "admi", "1d": "advaḥ", "1p": "admaḥ"},
    ("as", "P"): {"3d": "staḥ", "3p": "santi", "2s": "asi", "2d": "sthaḥ", "2p": "stha", "1s": "asmi", "1d": "svaḥ", "1p": "smaḥ"},
    ("hu", "P"): {"3s": "juhoti", "3d": "juhutaḥ", "3p": "juhvati"},
    ("dā", "P"): dict(zip(CODES, "dadāti dattaḥ dadati dadāsi datthaḥ dattha dadāmi dadvaḥ dadmaḥ".split())),
    ("dā", "A"): dict(zip(CODES, "datte dadāte dadate datse dadāthe daddhve dade dadvahe dadmahe".split())),
    ("dhā", "P"): {"3d": "dhattaḥ", "2d": "dhatthaḥ", "2p": "dhattha", "1s": "dadhāmi", "1d": "dadhvaḥ", "1p": "dadhmaḥ"},
    ("dhā", "A"): dict(zip(CODES, "dhatte dadhāte dadhate dhatse dadhāthe dhaddhve dadhe dadhvahe dadhmahe".split())),
    ("rudh", "P"): {"3d": "runddhaḥ", "3p": "rundhanti", "2s": "ruṇatsi", "2d": "runddhaḥ", "2p": "runddha", "1s": "ruṇadhmi", "1d": "rundhvaḥ", "1p": "rundhmaḥ"},
    ("rudh", "A"): dict(zip(CODES, "runddhe rundhāte rundhate runtse rundhāthe runddhve rundhe rundhvahe rundhmahe".split())),
    ("bhid", "P"): {"3s": "bhinatti", "3d": "bhinttaḥ", "3p": "bhindanti", "2s": "bhinatsi", "2p": "bhinttha", "1s": "bhinadmi", "1d": "bhindvaḥ", "1p": "bhindmaḥ"},
    ("bhid", "A"): {"3s": "bhintte", "3d": "bhindāte", "3p": "bhindate", "2s": "bhintse", "2d": "bhindāthe", "2p": "bhinddhve", "1s": "bhinde", "1d": "bhindvahe"},
    ("ric", "P"): {"3s": "riṇakti"}, ("vic", "P"): {"3s": "vinakti"}, ("kṣud", "P"): {"3s": "kṣuṇatti"}, ("chṛd", "P"): {"3s": "chṛṇatti"}, ("tṛd", "P"): {"3s": "tṛṇatti"}, ("kṛt", "P"): {"3s": "kṛṇatti"},
    ("hiṁs", "P"): dict(zip(CODES, "hinasti hiṁstaḥ hiṁsanti hinassi hiṁsthaḥ hiṁstha hinasmi hiṁsvaḥ hiṁsmaḥ".split())),
})
SUITE_NASAL = [(k, "laṭ", list(f), pd) for k, (_, _, pd, f) in NASAL.items()]
OPTION_CELLS = {"su.P.1d": "sunuvaḥ", "su.P.1p": "sunumaḥ", "su.A.1d": "sunuvahe", "tan.P.1d": "tanuvaḥ", "tan.P.1p": "tanumaḥ"}   # 6.4.107: the second branch, recorded
SUITE = [(r, l, cs, None) if len(e) == 3 else e for e in SUITE for r, l, cs in [e[:3]]] + [(r, "laṭ", list(cells), pada) for (r, pada), cells in V_ORACLE.items()] + SUITE_NASAL


def paradigm(root: str, lak: str, off=(), cells=None, pada=None) -> dict[str, str]:
    return {c: conjugate(root, lak, c, off, pada)[0] for c in (cells or CODES)}


def oracles() -> dict[str, dict[str, dict[str, str]]]:
    """The certified present-system paradigms, read from the earlier pinned packets."""
    import proof_lab.ting_lat_parasmaipada as T64
    import proof_lab.lat_atmanepada as T66
    import proof_lab.lan_parasmaipada_compiled as T95
    import proof_lab.lot_lin_parasmaipada_compiled as T96
    import proof_lab.atmanepada_lan_lot_lin_compiled as T99
    c58 = {"A": "ā", "H": "ḥ", "U": "ū", "I": "ī"}
    def iast(w): return "".join(c58.get(ch, ch) for ch in w)
    stems = {"bhū": T96.present_stem(T96.BHU), "gam": T96.present_stem(T96.GAM), "nī": T96.present_stem(T96.NI)}
    out: dict = {r: {} for r in ROOTS}
    out["bhū"]["laṭ"] = {c: iast(w) for c, w in T64.ORACLE["bhU"].items()}; out["gam"]["laṭ"] = {c: iast(w) for c, w in T64.ORACLE["gam"].items()}
    out["nī"]["laṭ"] = {"3s": "nayati", "3d": "nayataḥ", "3p": "nayanti", "2s": "nayasi", "2d": "nayathaḥ", "2p": "nayatha", "1s": "nayāmi", "1d": "nayāvaḥ", "1p": "nayāmaḥ"}
    for r in ("bhū", "gam", "nī"):
        out[r]["laṅ"] = dict(T95.ORACLE[r]); out[r]["loṭ"] = T96.paradigm(T96.lot, stems[r], T96.LOT_STAGES); out[r]["liṅ"] = T96.paradigm(T96.lin, stems[r], T96.LIN_STAGES)
    for r in ("edh", "labh"):
        out[r]["laṭ"] = {c: iast(w) for c, w in T66.ORACLE[r].items()}
        out[r]["laṅ"] = T99.paradigm(T99.lan, r, T99.LAN_STAGES); out[r]["loṭ"] = T99.paradigm(T99.lot, r, T99.LOT_STAGES); out[r]["liṅ"] = T99.paradigm(T99.lin, r, T99.LIN_STAGES)
    import proof_lab.lrt_lut_parasmaipada_compiled as T97
    import proof_lab.atmanepada_lrt_lut_compiled as T112
    import proof_lab.asirlin_parasmaipada_compiled as T115
    import proof_lab.asirlin_atmanepada_compiled as T117
    for r in ("bhū", "gam", "nī"):
        out[r]["lṛṭ"] = T97.paradigm(T97.lrt, r, T97.LRT_STAGES)
    for r in ("bhū", "nī"):
        out[r]["luṭ"] = T97.paradigm(T97.lut, r, T97.LUT_STAGES)
    for r in ("labh", "edh"):
        out[r]["lṛṭ"] = dict(T112.ORACLE["lrt"][r]); out[r]["luṭ"] = dict(T112.ORACLE["lut"][r]); out[r]["āśīrliṅ"] = dict(T117.ORACLE[r])
    for r in ("bhū", "gam", "nī"):
        out[r]["āśīrliṅ"] = dict(T115.ORACLE[r])
    import proof_lab.lun_parasmaipada_compiled as T101
    import proof_lab.atmanepada_lun_compiled as T116
    for r in ("bhū", "gam", "nī"):
        out[r]["luṅ"] = dict(T101.ORACLE[r])
    for r in ("labh", "edh"):
        out[r]["luṅ"] = dict(T116.ORACLE[r])
    import proof_lab.lit_parasmaipada_compiled as T102
    for r in ("bhū", "gam", "kṛ", "nī"):
        out[r]["liṭ"] = dict(T102.ORACLE[r])
    return out


OPEN_LANE_FILE = Path(__file__).resolve().parent.parent / "research" / "independent_oracle" / "VIDYUT_OPEN_LANE.json"


def open_lane_oracle() -> dict[str, list[str]]:
    """laṅ / loṭ / vidhiliṅ of classes 2–10: every cell vidyut-prakriya derives for the engine's declared roots (theorum/139).
    A DECLARED oracle of a different grade — an independent generator, not a commentary anchor — kept in the repository as data."""
    if not OPEN_LANE_FILE.exists():
        return {}
    return json.loads(OPEN_LANE_FILE.read_text(encoding="utf-8"))["cells"]


ARDHA_LANE_FILE = Path(__file__).resolve().parent.parent / "research" / "independent_oracle" / "VIDYUT_ARDHADHATUKA_LANE.json"
ARDHA_LANE_LAK = ("lṛṭ", "luṭ", "āśīrliṅ", "liṭ", "luṅ", "lṛṅ")


def ardha_lane_oracle() -> dict[str, list[str]]:
    """lṛṭ / luṭ / āśīrliṅ / liṭ / luṅ / lṛṅ of every declared (root, pada): the generator's cells (theorum/144), the same grade as the open lane."""
    if not ARDHA_LANE_FILE.exists():
        return {}
    return json.loads(ARDHA_LANE_FILE.read_text(encoding="utf-8"))["cells"]


def t3_ardha_lane() -> dict[str, Any]:
    O = ardha_lane_oracle()
    rows = {}
    for key, forms in O.items():
        r, pd, l, c = key.split("|")
        try:
            ours = conjugate(r, l, c, pada=pd)[0]
        except Exception as e:  # noqa: BLE001
            ours = f"ENGINE_ERROR {e}"
        rows[key] = {"ours": ours, "vidyut": forms, "agree": ours in forms}
    by_lak = {l: [sum(1 for k, x in rows.items() if k.split("|")[2] == l and x["agree"]), sum(1 for k in rows if k.split("|")[2] == l)] for l in ARDHA_LANE_LAK}
    claimed = list(ARDHA_LANE_LAK)   # every lakāra closed (theorum/144: lṛṭ, luṭ, āśīrliṅ; theorum/145: lṛṅ, liṭ; theorum/146: luṅ)
    return {"cells": len(rows), "agree": sum(1 for x in rows.values() if x["agree"]), "by_lakara": by_lak, "closed_lakaras": claimed,
            "disagree_in_closed": {k: x for k, x in rows.items() if not x["agree"] and k.split("|")[2] in claimed}, "agreeing_keys": [k for k, x in rows.items() if x["agree"]]}


def t2_open_lane() -> dict[str, Any]:
    O = open_lane_oracle()
    rows = {}
    for key, forms in O.items():
        r, pd, l, c = key.split("|")
        try:
            ours = conjugate(r, l, c, pada=pd)[0]
        except Exception as e:  # noqa: BLE001
            ours = f"ENGINE_ERROR {e}"
        rows[key] = {"ours": ours, "vidyut": forms, "agree": ours in forms}
    n = len(rows); agree = sum(1 for x in rows.values() if x["agree"])
    by_lak = {l: [sum(1 for k, x in rows.items() if k.split("|")[2] == l and x["agree"]), sum(1 for k in rows if k.split("|")[2] == l)] for l in ("laṅ", "loṭ", "liṅ")}
    return {"cells": n, "agree": agree, "by_lakara": by_lak, "disagree": {k: x for k, x in rows.items() if not x["agree"]}, "agreeing_keys": [k for k, x in rows.items() if x["agree"]]}


def t1_suite() -> dict[str, Any]:
    O = oracles()
    def key(r, l, pd): return f"{r}.{l}" + (f".{pd}" if pd else "")
    forms = {key(r, l, pd): paradigm(r, l, cells=cs, pada=pd) for r, l, cs, pd in SUITE}
    def ora(r, l, pd): return NASAL[r][3] if r in NASAL else (V_ORACLE[(r, pd)] if (l == "laṭ" and (r, pd) in V_ORACLE) else O[r][l])
    mism = {f"{key(r, l, pd)}.{c}": (forms[key(r, l, pd)][c], ora(r, l, pd)[c]) for r, l, cs, pd in SUITE for c in cs if forms[key(r, l, pd)][c] != ora(r, l, pd)[c]}
    lane = t2_open_lane(); O2 = open_lane_oracle(); lane3 = t3_ardha_lane(); O3 = ardha_lane_oracle()
    broken: dict[str, list[str]] = {}
    for rid in IDS:
        broken[rid] = [f"{key(r, l, pd)}.{c}" for r, l, cs, pd in SUITE for c in cs if conjugate(r, l, c, off=(rid,), pada=pd)[0] != ora(r, l, pd)[c]]
        if not broken[rid]:   # a row no suite cell loads may still be loaded by an agreeing lane cell (theorum/139, 144)
            for tag, keys, O_ in (("lane:", lane["agreeing_keys"], O2), ("ardha:", lane3["agreeing_keys"], O3)):
                for k in keys:
                    r, pd, l, c = k.split("|")
                    try:
                        if conjugate(r, l, c, off=(rid,), pada=pd)[0] not in O_[k]:
                            broken[rid].append(tag + k); break
                    except Exception:  # noqa: BLE001
                        broken[rid].append(tag + k); break
                if broken[rid]:
                    break
    vacuous = [r for r in IDS if not broken[r] and r not in SURFACE_COINCIDENT]
    cells = sum(len(cs) for _, _, cs, _ in SUITE)
    checks = {"all_908_cells_equal_the_oracles": not mism, "every_rule_row_is_load_bearing_on_the_suite_except_the_declared_surface_coincident": not vacuous}
    paths = {k: conjugate(*k.split("."))[1] for k in ("bhū.laṭ.1s", "gam.laṅ.3p", "nī.loṭ.2s", "bhū.liṅ.3p", "labh.laṭ.3d", "edh.laṅ.1s", "labh.loṭ.1d", "labh.liṅ.3s")}
    return {"checks": checks, "cells": cells, "mismatches": mism, "broken_counts": {r: len(b) for r, b in broken.items()}, "broken": broken, "vacuous_rows": vacuous, "surface_coincident": SURFACE_COINCIDENT, "forms": forms, "paths": paths,
            "open_lane": {"cells": lane["cells"], "agree": lane["agree"], "by_lakara": lane["by_lakara"], "disagree": lane["disagree"]},
            "ardhadhatuka_lane": {"cells": lane3["cells"], "agree": lane3["agree"], "by_lakara": lane3["by_lakara"], "closed_lakaras": lane3["closed_lakaras"], "disagree_in_closed": lane3["disagree_in_closed"]}}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_suite": t1_suite()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_TING_RULE_TABLE_ENGINE_CANDIDATE" if all(checks.values()) else "FAIL_TING_RULE_TABLE_ENGINE_CANDIDATE"
    return {
        "schema": "rkf.ting_rule_table_engine_candidate.v1", "status": status, "sources": SOURCES, "rule_order": IDS, "roots": ROOTS,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                f"one rule table of {len(IDS)} rows (each a quoted sūtra as guard + action) and one driver reproduce the 325 cells of the certified paradigms of bhū, gam, nī, kṛ (parasmaipada) and edh, labh (ātmanepada) — the present system laṭ, laṅ, loṭ, vidhiliṅ (180 cells: theorum/64, 66, 95, 96, 99), the ārdhadhātuka lṛṭ, luṭ, āśīrliṅ, luṅ (125 cells: theorum/97, 101, 112, 115, 116, 117) and liṭ (20 cells: theorum/102) — exactly from the earlier pinned packets, and the 79 laṭ cells of the vikaraṇa classes (pac; div, siv, śam; tud, nud; cur; su, ci, śru, āp, śak; tan, kṛ; krī, pū, lū) and the 101 laṭ cells of adādi (ad, as), juhotyādi (hu, dā, dhā) and rudhādi (rudh, bhid, ric, vic, kṣud, chṛd, tṛd, kṛt, hiṁs), and the 91 quoted cells of 86 further svādi / tanādi / kryādi entries (research/panini_grammar/nasal_present), and the 136 quoted cells of 38 adādi u- / ā- / i-roots and juhotyādi entries (research/panini_grammar/present_expansion, lexical_present), and the 176 quoted cells of 32 adādi consonant-root entries (research/panini_grammar/lexical_present), declared from the grammar-verification branch's quoted present tables (Kāśikā / Kaumudī / Laghukaumudī anchors in research/panini_grammar/vikarana_lat, non_thematic_lat, exception_lat, abhyasa_lat, snam_lat); every row is load-bearing on at least one cell (per-row broken sets recorded)",
                "the sārvadhātuka / ārdhadhātuka split is the lakāra set (3.4.113 / 3.4.114 / 3.4.116): śap only before the present system, sya / tās / sic / aṅ as the vikaraṇa segment, iṭ (7.2.35) as its own segment for the seṭ roots (bhū, edh: declared from the Dhātupāṭha accent; nī, labh aniṭ by 7.2.10; gam by 7.2.58 before sya), the kit of āśīrliṅ (3.4.104) as a predicate that turns 7.3.84 off; 8.3.59 reads the segment boundaries (affix / augment s after iṇ, not the pada-final s: 8.3.55)",
                "luṅ at breadth (theorum/146): 1,854 / 1,854 — the cli substitutes as rows: sic (3.1.44) with 7.3.96's īṭ, aṅ (3.1.55 for the ḷdit and the puṣādi of the fourth class, 3.1.57 irito vā with the aṅ branch realised, 3.1.52 for vac / khyā with 7.4.20's um: agamat, aghasat by 2.4.37, abhidat, arudat, avocat, akhyat, aśamat), ksa (3.1.45 for the aniṭ śal-final root with an ik penult: adhukṣat, alikṣat, advikṣat; 7.3.72 ksasyāci, 7.3.73's luk in ātmanepada: adugdha, alīḍha), caṅ (3.1.48 for the ṇic-ending with 6.4.51, 6.1.11, 7.4.1, 7.4.59, 7.4.93 / 7.4.94: acūcurat), the luk of 2.4.77 widened to gā (2.4.45), sthā, the ghu and pā (adāt, agāt, asthāt) with 3.4.110 (aduḥ); 7.2.1 with iṭ too (adhāvīt, alāvīt), 7.2.3 vadavrajahalantasyācaḥ on the root's last vowel (apākṣīt, abhāntsīt, anautsīt, amārkṣīt) under 7.2.4 neṭi and 7.2.5 (adevīt, agrahīt, ajāgarīt), 7.2.72 (astāvīt, asāvīt), 7.2.73 sak with iṭ for the ā-final (abhāsīt, abhāsiṣṭām, amāsiṣṭām, adaridrāsīt); the ātmanepada kit by 1.2.11 / 1.2.12 (akṛta, abhitta, aruddha, anutta) with 8.2.27 hrasvād aṅgāt and 1.2.17 sthāghvor ic ca (adita, adhita); 8.2.28 iṭa īṭi (adevīt, ānīt), 8.2.25 for the sic before dhvam (aceḍhvam, aidhidhvam) and 8.3.78 (akṛḍhvam); the seṭ root known by an ādeśa (vadha) read as seṭ (avadhīt)",
                "liṭ at breadth and lṛṅ (theorum/145): lṛṅ 1,845 / 1,854 (3.3.139 as a ṅit lakāra with sya: the laṅ rows and 3.1.33 carry it); liṭ 1,797 / 1,849 — 3.4.81 liṭas tajhayor eśirec with 3.4.79 (dade, dadire), the periphrastic liṭ 3.1.35–3.1.40 (cakāsāmbabhūva, corayāmbabhūva, edhāmbabhūva, jāgarāmbabhūva, bibhayāmbabhūva by the ślu-like doubling of 3.1.39; the anuprayoga of bhū realised, kṛ / as recorded), the vowel-initial abhyāsa 7.4.70 / 7.4.71 / 7.4.72 / 6.4.78 / 7.4.69 (āda, ānaśe, iyāya, iyeṣa, īyatuḥ), 7.4.61 śarpūrvāḥ khayaḥ and the kṣ token (caskambha, tuṣṭāva, cakṣāṇa), 6.1.17 with 7.4.67 and 6.1.15 / 6.1.16 in the kit cells (uvāca, ūce, suṣvāpa, jijyau, jagṛhatuḥ), 7.1.34 (dadau), 6.4.64 (dade, dadatuḥ, daditha), 6.4.120–6.4.123 / 6.4.126 (pecatuḥ, lebhe, mene, nebhatuḥ, senatuḥ, redhatuḥ, pecitha; cakase kept by anādeśādeḥ), 7.4.11 / 7.4.12 (cakāra, cakaratuḥ, cakare), 7.3.55 (jaghāna), 7.2.13 as the liṭ iṭ-exception and 7.2.61–7.2.63 for thal (cakartha; ninayitha, jagamitha realised, ninetha / jagantha recorded), 7.2.115 / 7.2.116 restricted to ṇal, 7.3.84 / 7.3.86 in the non-kit cells (ninetha, bibheda), 6.4.77 before the iṭ of the kit cells (dudhuviva, cikriye), 8.3.78 for liṭ's dhve (cakṛḍhve), the root-initial s after the abhyāsa's iṇ with the ṣṭutva inside the root (siṣeva, suṣvāpa, tuṣṭāva, suṣṇāva; not before a velar, the generator's reading: cuskāva), 6.1.73 after the abhyāsa (caccharda); left: jakṣ (no vṛddhi in the generator), stubh / stṛ (the generator's tustumbha, tastaratuḥ against the table's tuṣṭumbha, tastratuḥ — open), ūrṇu (6.1.2 ajāder dvitīyasya not built), i-thal",
                "the ārdhadhātuka lane (theorum/144): lṛṭ / luṭ / āśīrliṅ of every declared (root, pada) on the generator's cells, 1,845 / 1,854 each (the nine of daridrā are a vārttika's, not claimed) — the Dhātupāṭha pinned in the repository (research/panini_grammar/DHATUPATHA.tsv) and 7.2.10 ekāca upadeśe 'nudāttāt read off its accent marks in place of the declared SET list; 2.4.52 aster bhūḥ, 2.4.53 bruvo vaciḥ, 2.4.42 hano vadha liṅi with 6.4.48; 7.2.70 ṛddhanoḥ sye, 7.2.37 graho 'liṭi dīrghaḥ; 7.3.86 before the ārdhadhātuka sya / tās / iṭ (bhetsyati, rotsyati, deviṣyati) and 7.3.84 before the non-kit sīyuṭ (ceṣīṣṭa), 3.4.104 kid āśiṣi read as the yāsuṭ's with 1.2.11 / 1.2.12 for the ṛ-final root (kṛṣīṣṭa); the āśīrliṅ parasmaipada rows 7.4.25, 7.4.28, 7.4.29, 7.1.100, 6.4.66 / 6.4.67, 6.1.15 / 6.1.16 / 6.4.2, 6.4.24 before the kit, 7.3.85, 6.4.51, 6.1.50; 8.3.78 (bhṛṣīḍhvam); the tripādī rows 8.2.31 / 8.2.32 / 8.2.36 / 8.2.37 / 8.2.41 / 8.4.41 / 8.3.13 reading the s of sya / sīyuṭ and the t of tās (dhokṣyati, dvekṣyati, lekṣyati, dveṣṭā, leḍhā); 8.3.24's m clause (gantā); the liṭ / luṅ / lṛṅ columns of the same lane reported as the baseline of the next packets",
                "the open lane, third pass (theorum/143): 5,373 / 5,373 — 6.1.68 halṅyābbhyo dīrghāt sutisyapṛktaṁ hal as the apṛkta rule of the tiṅ (abhinat, ahan, acakāt; theorum/139's 8.2.23 / 8.2.24 attribution corrected, 8.2.24 withdrawn), the pada-end block 8.2.37 (ante) → 8.2.39 jhalāṁ jaśo 'nte → 8.4.56 vā 'vasāne (adhok, adveṭ, aleṭ, amārṭ, aruṇat, avak), 8.2.73 tipy anasteḥ / 8.2.74 sipi dhātor ruvā (ahinat, acakāt; the ru branch recorded), 8.2.25 dhi ca (hindhi, cakādhi), 8.4.53 widened (kṛnddhi, vagdhi, riṅgdhi; 8.4.65 recorded), 6.4.36 hanter jaḥ with 6.4.22 asiddhavad atrābhāt keeping 6.4.105 off (jahi) and 6.4.119 para to 6.4.112 before hi (dhehi, dehi), 7.3.88 bhūsuvos tiṅi (suvai), 7.3.91 guṇo 'pṛkte (aurṇot), 7.3.87 read as the laghūpadha clause only (bibhayāni, juhavāni, bibharāṇi, piparāṇi, jihrayāṇi), 7.3.83 placed as the para rule (1.4.2) against 6.4.82 / 6.4.87 / 7.1.102 (abibhayuḥ, ajuhavuḥ, apiparuḥ), the strong-ending predicate in 7.3.89 / 7.3.93 / 7.2.114 (stuyāt, brūyāt, mṛjyāt), 7.1.100 / 7.1.102 with 8.2.77 across the yāsuṭ (pipūryāt), the next-sound readers in 6.4.37 / 6.4.81 / 6.4.98 / 6.4.108 / 8.2.26 / 8.2.41 / 8.4.41 (hanyātam, iyām, hanyāt, kurvīvahi, kasīdhvam, adveṭ, dviṣyāt, dviṣīta), 6.4.106 for the tanādi u and kṛ (kuru, tanu, sanu), 7.2.77 / 7.2.78 on the loṭ sva / dhvam by 1.1.56 and not on the dhvam of laṅ / liṅ (īśiṣva, īḍidhvam, aiḍḍhvam, īḍīdhvam), the ṇatva reader across the ay / av / ār tokens (bravāṇi, karavāṇi, corayāṇi, ārṇāt), 8.2.40 / 8.4.53 / 8.4.55 not reaching the apṛkta (8.2.1)",
                "the open lane, second pass (theorum/140): the augment rows before the lopa rows (āsva), 7.3.83 after the doubling (ajuhavuḥ), the sīyuṭ counted as hal-initial for 6.4.112 / 6.4.113 after its s has fallen (krīṇīta, gṛhṇīta; dadhīta for the ghu), 7.3.87 (nenijāni), 7.3.98's īṭ for the rudādi apṛkta in laṅ beside 7.2.76's iṭ, 6.4.109 (kuryāt), 6.4.118 (jahyāt), 8.2.29 for the root's s / k before the apṛkta t (acakāt), the tuk after the augment before ch (acchṛṇat), the ṇatva reader reaching the affix under 8.4.37 (bibharāṇi), 6.1.88 on āṭ + ai (aśnavai), ī + ī (dhunīta)",
                "the open lane (theorum/139): laṅ / loṭ / vidhiliṅ of classes 2–10 — the strong-ending predicate (pit and not ṅit, with 3.4.92's āṭ making the loṭ uttama pit) replaces the bare pit test in every guṇa and lopa row, the next-sound readers include the yāsuṭ / sīyuṭ, and nine rows are added (6.1.96 usy apadāntāt, 6.4.101 her dhiḥ, 6.4.119, 7.3.83 jusi ca, 3.4.109 after the abhyasta in laṅ, 8.2.24, 7.3.100, 3.1.83, 6.4.106) with 7.3.96 reaching as; the cells are the independent generator's (VIDYUT_OPEN_LANE.json, a DECLARED oracle of a different grade), reported as a fraction in open_lane and loading rows only where they agree",
                "the adādi consonant roots (theorum/136): nineteen rows — the iṭ / īṭ rows 7.3.98 (roditi, svapimi), 7.3.93 (bravīti), 7.2.77 / 7.2.78 (īśiṣe, īḍidhve); the aṅga rows 6.1.6 (jāgrati, śāsati, daridrati by 7.1.4 and 6.4.112), 6.4.34 with 8.3.60 (śiṣṭaḥ), 6.4.114 (daridritaḥ), 6.4.37 and 6.4.98 with 7.3.54 (hataḥ, ghnanti), 7.2.114 as 7.3.86's apavāda (mārṣṭi), 7.4.21 with 7.1.6 (śete, śerate); the tripādī rows 8.2.31 / 8.2.32 / 8.2.37 (leḍhi, dogdhi, dhokṣi, dhugdhve), 8.2.36 (mārṣṭi, kaṣṭe, īṣṭe), 8.3.13 with 6.3.111 (līḍhaḥ against leḍhi), 8.2.26 widened (vadhve), 8.3.24 / 8.4.58 reading across the affix (haṁsi, hanti), 8.4.41 after ṭu (īṭṭe, kaḍḍhve), 8.4.53 withholding the ḍh + dh of lih for 8.4.41 and 8.3.13",
                "the adādi u-roots and the juhotyādi at breadth (theorum/135): 7.3.89 uto vṛddhir luki hali as a row (yauti, stauti, kṣṇauti; ūrṇauti as 7.3.90's first alternative), the three abhyāsa rows of ślu — 7.4.76 bhṛñām it (bibharti, mimīte, jihīte), 7.4.77 (piparti), 7.4.75 (nenekti, veveṣṭi) — with 7.4.60 now load-bearing (ji-hrī), 7.1.102 before 8.2.77 (pipūrtaḥ / pipurati), the three yaṇ / iyaṅ-uvaṅ rows 6.4.81 (yanti), 6.4.82 (bibhyati; and ninyatuḥ, ninyiva of liṭ now rest on it), 6.4.77's dhātu clause (yuvanti, stuvanti, hnuvāte, jihriyati, viyanti), 6.4.113 generalised to the abhyasta non-ghu ā (mimīte, jahītaḥ), 7.3.86 reading the pit tiṅ across the ślu (nenejmi), 8.2.41 (vevekṣi), 8.3.57's ku clause in the ṣatva reader (nenekṣi), 6.1.101's ā + a (yānti)",
                "the nasal classes at breadth (theorum/134): 86 svādi / tanādi / kryādi entries from the branch's quoted tables ride on the rows of theorum/132 with eight additions — 3.1.82's śnu (first alternative), 6.4.24's nasal-lopa before the ṅidvat vikaraṇa (dabhnoti, badhnāti, mathnāti), 7.3.79, 6.1.16 with 1.1.45 / 6.1.108 (gṛhṇāti, jināti), 8.4.40 under 8.4.44 (khacñāti; aśnāti, kliśnāti), 8.4.41's n (mṛḍṇāti), 8.4.39's kṣubhnādi as a ṇatva exception (kṣubhnāti, tṛpnoti), 6.1.64's reversion of the ṭ / ṇ the ṣ had conditioned (stighnute, sanoti), 7.3.80 restricted to the kryādi pvādi (dhūnoti against dhunāti), 7.3.86 before the ārdhadhātuka u (kṣeṇoti)",
                "adādi / juhotyādi / rudhādi (theorum/133): the luk (2.4.72) and ślu (2.4.75) are flags that keep 3.1.68 off and let 7.3.84 read the pit tiṅ directly (juhoti); ślu doubles by 6.1.10 on the same abhyāsa segment as liṭ (7.4.59, 7.4.62, 8.4.54 shared); śnam (3.1.78) is an infix placed by 1.1.47 inside the root segment, ṅidvat like every śit vikaraṇa; 6.4.111 drops its a and the a of as before the kit / ṅit tiṅ; 6.4.112 is generalised to the abhyasta ā and, for the ghu (1.1.20), before hal (dattaḥ) while 6.4.113's ī stays aghoḥ; 8.2.38 for dhā with 8.2.40 read as adhaḥ; 7.1.4 before 7.1.5 / 7.1.3; the tripādī order 8.3.24 → 8.4.2 → 8.4.58 is what keeps rundhanti's n dental and ruṇaddhi's ṇ retroflex (the n that 8.4.58 restores is asiddha for 8.4.2)",
                "the vikaraṇa classes (theorum/132): the vikaraṇa is a row (3.1.25 ṇic, 3.1.69 śyan, 3.1.73 śnu with 3.1.74, 3.1.77 śa, 3.1.79 u, 3.1.81 śnā) and its ś-it-ness a state predicate: a śit vikaraṇa is sārvadhātuka (3.4.113) and, apit, ṅidvat (1.2.4) — so 7.3.84 / 7.3.86 are off the root (sunoti, tudati) — while the ś-less u and ṇic are ārdhadhātuka (3.4.114) and take the guṇa (karoti, corayati); the aṅga-final u takes 7.3.84 before the pit tiṅ only (sunoti / sunutaḥ); 6.4.110 / 6.4.108 for kṛ, 6.4.107 (lopa branch realised, the other recorded), 6.4.77 / 6.4.87 by the conjunct test, 6.4.112 / 6.4.113 for śnā, 7.3.80 for the pvādi, 8.2.77 / 7.3.74 for śyan, 8.4.2 across the root",
                "liṭ: the abhyāsa is a segment (6.1.8 with 6.1.1 / 6.1.4; 7.4.59, 7.4.62, 7.4.66, 7.4.73, 8.4.54 as rows on it), 1.2.5's kit as a predicate (ṇal pit by 1.1.56 as tip's substitute: vṛddhi 7.2.115 / 7.2.116; the kit cells: 1.1.5, 6.4.98, 6.1.77), 6.4.88's vuk before 7.2.115 (babhūva, not *babhāva), 7.2.13 as a flag that 7.2.35 reads (cakṛva)",
                "bhūyāt: the s of yās is dropped by 8.2.29 (the pada-final conjunct) and kept in bhūyāstām / bhūyāsuḥ; theorum/115 reached the same three forms with 7.2.79 on the 3s cell — the forms agree, the rule attribution differs, and this table's attribution is the one recorded here (7.2.79 is the sārvadhātuka rule and does not reach āśīrliṅ)",
                "the lakāra-specific substitutions of 3.4.77–3.4.113 are rows; the ṅit-ness of the apit sārvadhātuka (1.2.4) and of liṅ (3.4.103) is a state predicate, not a row; 3.4.85 loṭo laṅvat is realised as loṭ in the guards of 3.4.99 / 3.4.101",
                "3.4.92's āṭ makes 7.3.101 vacuous on the loṭ uttama dual / plural (bhavāva by either): the table keeps 7.3.101 off where āṭ fired; 3.4.92 is therefore surface-coincident on this suite and is declared so (not counted as load-bearing, not hidden)",
            ],
            "NOT_claimed": ["cakṣ (caṣṭe: 8.2.29 on kṣ), ṛ (iyarti: iyaṅ on the abhyāsa), niñj / śiñj / piñj / vṛj / pṛc (riṅkte-type cells), vid in its liṭ-shaped laṭ (3.4.83), the 7.3.94 / 7.3.99 īṭ cells of brū and the rudādi in laṅ", "the 7.3.95 īṭ cells (ruvītaḥ, stuvīmaḥ …: an option the branch realises cell by cell), the 6.4.115 / 6.4.116 hrasva cells of bhī and hā (bibhivaḥ, jahithaḥ: optional, realised inconsistently across the branch's cells), kṣṇu / snu beyond 7.3.89", "tṛṇu (the branch anchors tṛṇoti / tṛṇute while 7.3.86 as a row would give tarṇoti: the ground of the attested form is not derived here, the cells are left out), ṛṇu (ṛṇoti / arṇutaḥ) and khav (khaunāti), the śnā branch of 3.1.82 as set-valued output", "the ātmanepada 3s cells of kṣud / chṛd / tṛd / khid / vid (kṣunte …) and of ric / vic (riṅkte), und, añj, tṛh, bhuj, indh (the branch's anchors there need rows not yet in the table), the 3s of as (asti) and the 3s / 3p of dhā (not anchored in the branch's tables)", "the vikaraṇa-class cells beyond those quoted (the full paradigms of su, kṛ, krī …), the 3.1.70 / 3.1.82 options, adādi (śap-luk) and juhotyādi (ślu), rudhādi (śnam), the ātmanepada 1.3.72 ground of each ubhayapadin cell (the pada is declared with the cell), the second branch of 6.4.107 as set-valued output", "7.4.60 halādiḥ śeṣaḥ (no cluster-initial root in the certified liṭ oracle; the row would be vacuous and is not in the table), liṭ ātmanepada (3.4.81), the thal / athus / a cells and 1.2.6 / 7.2.62 options", "the ground for the absence of iṭ before the parasmaipada yāsuṭ (bhūyāt, not *bhaviyāt) is taken from the certified forms of theorum/115, not derived (the 7.2.35 row is guarded off that segment)", "liṭ, lṛṅ, luṭ of gam (not in the earlier oracle), the full ātmanepada paradigms where the earlier packets certified six / four cells (the table is checked on exactly the certified cells)", "the other gaṇas (the vikaraṇas other than śap), ārdhadhātuka lakāras (liṭ, luṭ, lṛṭ, luṅ, āśīrliṅ: theorum/97, 101, 102, 112, 115–117 remain per-packet until they are rows here), the passive (yak), the derived stems (ṇic, san, yaṅ), accent (udātta of 3.4.103 / 6.4.71), RH, YM"],
        },
        "checks": checks, **packets,
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, default=str) + "\n").encode("utf-8")


def certificate_sha256(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--output", default=None); a = ap.parse_args()
    cert = build_certificate()
    print(cert["status"])
    for k, v in cert["t1_suite"]["checks"].items():
        print(f"    t1_suite.{k}: {v}")
    if cert["t1_suite"]["mismatches"]:
        print("    mismatches:", cert["t1_suite"]["mismatches"])
    if cert["t1_suite"]["vacuous_rows"]:
        print("    vacuous:", cert["t1_suite"]["vacuous_rows"])
    print("sha256", certificate_sha256(cert))
    if a.output:
        Path(a.output).write_bytes(canonical_bytes(cert))


if __name__ == "__main__":
    main()
