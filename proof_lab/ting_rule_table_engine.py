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
from proof_lab.sup_rule_table_engine import GUNA, V, tok

SOURCES = {
    "3.2.123": "vartamāne laṭ", "3.2.111": "anadyatane laṅ", "3.3.162": "loṭ ca", "3.3.161": "vidhinimantraṇāmantraṇādhīṣṭasaṁpraśnaprārthaneṣu liṅ",
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
    "8.2.23": "saṁyogāntasya lopaḥ", "8.2.66": "sasajuṣo ruḥ", "8.3.15": "kharavasānayorvisarjanīyaḥ",
}

# 3.4.78 in upadeśa; theorum/82 reads the its (p by 1.3.3, ṭ of iṭ by 1.3.3, ṅ of mahiṅ marks the whole list)
TING_P = {"3s": "tip", "3d": "tas", "3p": "jhi", "2s": "sip", "2d": "thas", "2p": "tha", "1s": "mip", "1d": "vas", "1p": "mas"}
TING_A = {"3s": "ta", "3d": "ātām", "3p": "jha", "2s": "thās", "2d": "āthām", "2p": "dhvam", "1s": "iṭ", "1d": "vahi", "1p": "mahi"}
CODES = list(TING_P)
LAKARAS = ("laṭ", "laṅ", "loṭ", "liṅ", "lṛṭ", "luṭ", "āśīrliṅ", "luṅ", "liṭ")
LIT_P = {"tip": "a", "tas": "atus", "jhi": "us", "sip": "tha", "thas": "athus", "tha": "a", "mip": "a", "vas": "va", "mas": "ma"}   # 3.4.82 after 1.3.7 / 1.3.3 (ṇal → a, thal → tha)
NO_IT_LIT = {"kṛ"}   # 7.2.13 kṛsṛbhṛvṛstudrusruśruvo liṭi
CU = {"k": "c", "kh": "ch", "g": "j", "gh": "jh", "ṅ": "ñ", "h": "j"}
DEASP = {"bh": "b", "ph": "p", "dh": "d", "th": "t", "gh": "g", "kh": "k", "jh": "j", "ch": "c", "ḍh": "ḍ", "ṭh": "ṭ"}
HRASVA = {"ā": "a", "ī": "i", "ū": "u", "ṝ": "ṛ", "e": "i", "ai": "i", "o": "u", "au": "u"}
YAN = {"i": "y", "ī": "y", "u": "v", "ū": "v", "ṛ": "r"}
NGIT_LAK = ("laṅ", "liṅ", "āśīrliṅ", "luṅ")      # the ṅit lakāras (3.4.100 itaś ca …)
VRDDHI = {"i": "ai", "ī": "ai", "u": "au", "ū": "au", "ṛ": "ār"}
JHAL = {"k", "kh", "g", "gh", "c", "ch", "j", "jh", "ṭ", "ṭh", "ḍ", "ḍh", "t", "th", "d", "dh", "p", "ph", "b", "bh", "ś", "ṣ", "s", "h"}
PRESENT = ("laṭ", "laṅ", "loṭ", "liṅ")          # the śap lakāras of theorum/64–99
TIT = ("laṭ", "loṭ", "lṛṭ", "luṭ")               # ṭit lakāras (3.4.79)
SET = {"bhū", "edh"}                             # seṭ by the Dhātupāṭha accent (udātta in upadeśa); nī, labh, gam are anudāttet → aniṭ by 7.2.10 (declared)
KHAR = {"k", "kh", "c", "ch", "ṭ", "ṭh", "t", "th", "p", "ph", "ś", "ṣ", "s"}
CAR = {"bh": "p", "b": "p", "dh": "t", "d": "t", "gh": "k", "g": "k", "jh": "c", "j": "c", "ḍh": "ṭ", "ḍ": "ṭ"}
JAS = {"bh": "b", "dh": "d", "gh": "g", "jh": "j", "ḍh": "ḍ"}
JHAS = {"bh", "gh", "dh", "jh", "ḍh"}
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
    def form(self): return "".join(self.ab + self.ag + self.r + self.it + self.v + self.pre + self.aff)
    def after_root(self):   # the first token after the root
        return (self.it + self.v + self.pre + self.aff)[:1]
    def kit(self):   # 3.4.104 kid āśiṣi; 1.2.5 asaṁyogāl liṭ kit (the apit liṭ ending after a root not ending in a conjunct; ṇal is pit as tip's substitute, 1.1.56)
        return self.lak == "āśīrliṅ" or (self.lak == "liṭ" and not self.pit and self.r[-1] in V or (self.lak == "liṭ" and not self.pit and len(self.r) >= 2 and self.r[-2] in V))
    def a_final(self): return bool(self.anga()) and self.anga()[-1] == "a"
    def ngit(self):   # 1.2.4 sārvadhātukam apit; liṅ's yāsuṭ is ṅit by 3.4.103
        return (not self.pit) or (self.lak in ("liṅ", "āśīrliṅ"))
    def P(self): return self.pada == "P"
    def A(self): return self.pada == "A"


YAY = {"k", "kh", "g", "gh", "ṅ", "c", "ch", "j", "jh", "ñ", "ṭ", "ṭh", "ḍ", "ḍh", "ṇ", "t", "th", "d", "dh", "n", "p", "ph", "b", "bh", "m", "y", "r", "l", "v"}
SAVARNA = {**{k: "ṅ" for k in ("k", "kh", "g", "gh", "ṅ")}, **{k: "ñ" for k in ("c", "ch", "j", "jh", "ñ")}, **{k: "ṇ" for k in ("ṭ", "ṭh", "ḍ", "ḍh", "ṇ")}, **{k: "n" for k in ("t", "th", "d", "dh", "n")}, **{k: "m" for k in ("p", "ph", "b", "bh", "m")}, "y": "ṁ", "r": "ṁ", "l": "ṁ", "v": "ṁ"}
NATVA_PASS = set(V) | {"k", "kh", "g", "gh", "ṅ", "p", "ph", "b", "bh", "m", "h", "y", "v", "ṁ"}


def _natva_site(s: S):
    """The n (of śnam in the root, or opening the vikaraṇa) after r / ṛ / ṣ across vowels, ku, pu, not before a jhal."""
    seq = s.r + s.v
    full = seq + s.aff
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
            if seq[j] in ("r", "ṛ", "ṝ", "ṣ") or seq[j].endswith("ṣ"):   # the kṣ token of kṣud ends in ṣ
                return i
            if seq[j] not in NATVA_PASS:
                break
            j -= 1
    return None


def _natva_set(s: S) -> None:
    i = _natva_site(s)
    if i < len(s.r): s.r[i] = "ṇ"
    else: s.v[i - len(s.r)] = "ṇ"


def _s_after_in(s: S):
    """s-initial segments (iṭ-less sya / tās, sīy / yās, suṭ inside the affix) whose preceding sound is iṇ."""
    segs = [("v", s.v, s.r + s.it), ("pre", s.pre, s.r + s.it + s.v), ("aff", s.aff, s.r + s.it + s.v + s.pre)]
    for name, seg, before in segs:
        if seg[:1] == ["s"] and before and before[-1] in IN and not (name == "aff" and len(seg) == 1):   # 8.3.55 apadāntasya: not the pada-final s
            yield name, 0
    for i in range(1, len(s.aff)):          # suṭ (3.4.107) inside the affix
        if s.aff[i] == "s" and s.aff[i - 1] in IN and "3.4.107" in s.done:
            yield "aff", i


def _satva(s: S) -> None:
    for name, i in list(_s_after_in(s)):
        getattr(s, name)[i] = "ṣ"


def _set_last_anga(s: S, new: list[str]) -> None:
    if s.pre: s.pre[-1:] = new
    elif s.v: s.v[-1:] = new
    elif s.it: s.it[-1:] = new
    else: s.r[-1:] = new


def rules() -> list[tuple[str, Callable[[S], bool], Callable[[S], Any], str]]:
    R: list = []
    def add(n, g, a, note): R.append((n, g, a, note))
    # ---- phase 1: the lakāra's affix substitutions (3.4) ---------------------------------
    add("3.1.44", lambda s: s.lak == "luṅ" and not s.v and "2.4.77" not in s.done and "3.1.55" not in s.done, lambda s: setattr(s, "v", ["s"]), "cli (3.1.43) → sic in luṅ")
    add("2.4.77", lambda s: s.lak == "luṅ" and s.v == ["s"] and s.P() and "".join(s.r) == "bhū", lambda s: setattr(s, "v", []), "luk of sic after bhū in parasmaipada (1.1.63: no sic-conditioned operation on the aṅga)")
    add("3.1.55", lambda s: s.lak == "luṅ" and s.v == ["s"] and s.P() and "".join(s.r) == "gam", lambda s: setattr(s, "v", ["a"]), "aṅ for cli after the ḷdit gamḷ~ in parasmaipada")
    add("3.4.82", lambda s: s.lak == "liṭ" and s.P() and "3.4.82" not in s.done, lambda s: setattr(s, "aff", tok(LIT_P[s.up])), "the parasmaipada tiṅ → ṇal atus us thal athus a ṇal va ma in liṭ (ārdhadhātuka, 3.4.115)")
    add("3.1.33", lambda s: s.lak in ("lṛṭ", "luṭ") and not s.v, lambda s: setattr(s, "v", tok("sya") if s.lak == "lṛṭ" else tok("tās")), "sya before lṛṭ, tāsi before luṭ (ārdhadhātuka: 3.4.114)")
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
    add("3.4.79", lambda s: s.A() and s.lak in TIT and "3.4.79" not in s.done and not (s.lak == "luṭ" and s.pers == "3"),
        lambda s: setattr(s, "aff", s.aff[:max(i for i, x in enumerate(s.aff) if x in V)] + ["e"]), "the ṭi of the ātmanepada affix → e after a ṭit lakāra (te, āte, ante, se, dhve, e, vahe, mahe)")
    add("3.4.80", lambda s: s.A() and s.lak in TIT and s.up == "thās", lambda s: setattr(s, "aff", ["s", "e"]), "thās → se")
    add("3.4.109", lambda s: s.P() and s.lak == "luṅ" and s.v == ["s"] and s.up == "jhi", lambda s: setattr(s, "aff", tok("us")), "jhi → jus after sic (anaiṣuḥ)")
    add("7.1.4", lambda s: s.aff[:1] == ["jh"] and "ślu" in s.flags, lambda s: setattr(s, "aff", ["a", "t"] + s.aff[1:]), "jh → at after the abhyasta (juhvati, dadati, dadate)")
    add("7.1.5", lambda s: s.A() and s.aff[:1] == ["jh"] and s.anga()[-1:] != ["a"], lambda s: setattr(s, "aff", ["a", "t"] + s.aff[1:]), "jh → at in the ātmanepada after a non-a aṅga (alapsata, aidhiṣata)")
    add("7.1.3", lambda s: s.aff[:1] == ["jh"], lambda s: setattr(s, "aff", ["a", "n", "t"] + s.aff[1:]), "jh → ant")
    add("3.4.100", lambda s: s.P() and s.lak in NGIT_LAK and s.aff[-1] == "i" and s.up in ("tip", "sip", "mip", "jhi"), lambda s: s.aff.pop(), "the i of a ṅit lakāra's parasmaipada affix dropped (laṅ, liṅ)")
    add("3.4.101", lambda s: s.P() and s.lak in NGIT_LAK + ("loṭ",) and s.up in ("tas", "thas", "tha", "mip"),
        lambda s: setattr(s, "aff", {"tas": tok("tām"), "thas": tok("tam"), "tha": tok("ta"), "mip": tok("am")}[s.up]), "tas thas tha mip → tām tam ta am after a ṅit lakāra (loṭ by 3.4.85 laṅvat)")
    add("3.4.99", lambda s: s.P() and s.lak in NGIT_LAK + ("loṭ",) and s.up in ("vas", "mas"), lambda s: s.aff.pop(), "the s of the uttama parasmaipada dropped after a ṅit lakāra (loṭ by 3.4.85)")
    add("3.4.86", lambda s: s.P() and s.lak == "loṭ" and s.aff[-1] == "i" and s.up in ("tip", "jhi"), lambda s: s.aff.__setitem__(-1, "u"), "i → u in loṭ (tu, antu)")
    add("3.4.87", lambda s: s.P() and s.lak == "loṭ" and s.up == "sip", lambda s: (setattr(s, "aff", ["h", "i"]), setattr(s, "pit", False)), "sip → hi in loṭ, and it is apit")
    add("3.4.89", lambda s: s.P() and s.lak == "loṭ" and s.up == "mip", lambda s: setattr(s, "aff", ["n", "i"]), "mip → ni in loṭ")
    add("3.4.90", lambda s: s.A() and s.lak == "loṭ" and s.aff[-1] == "e" and s.up in ("ta", "ātām", "jha", "āthām"), lambda s: setattr(s, "aff", s.aff[:-1] + ["ā", "m"]), "the e (3.4.79) → ām in loṭ (tām, ātām, antām, āthām)")
    add("3.4.91", lambda s: s.A() and s.lak == "loṭ" and s.up in ("thās", "dhvam"), lambda s: setattr(s, "aff", tok("sva") if s.up == "thās" else tok("dhvam")), "se dhve → sva dhvam in loṭ")
    add("3.4.93", lambda s: s.A() and s.lak == "loṭ" and s.aff[-1] == "e" and s.pers == "1", lambda s: s.aff.__setitem__(-1, "ai"), "the e of the uttama → ai in loṭ (ai, vahai, mahai)")
    add("3.4.92", lambda s: s.lak == "loṭ" and s.pers == "1", lambda s: setattr(s, "aff", ["ā"] + s.aff), "āṭ to the uttama in loṭ, and it is pit")
    add("3.4.102", lambda s: s.A() and s.lak in ("liṅ", "āśīrliṅ"), lambda s: setattr(s, "pre", tok("sīy")), "sīyuṭ to the tiṅ in liṅ (ātmanepada); the u is for pronunciation")
    add("3.4.103", lambda s: s.P() and s.lak in ("liṅ", "āśīrliṅ"), lambda s: setattr(s, "pre", tok("yās")), "yāsuṭ to the tiṅ in liṅ (parasmaipada), and the liṅ is ṅit")
    add("3.4.105", lambda s: s.A() and s.lak in ("liṅ", "āśīrliṅ") and s.up == "jha", lambda s: setattr(s, "aff", tok("ran")), "jha → ran in liṅ")
    add("3.4.106", lambda s: s.A() and s.lak in ("liṅ", "āśīrliṅ") and s.up == "iṭ", lambda s: setattr(s, "aff", ["a"]), "iṭ → at in liṅ")
    add("3.4.107", lambda s: s.A() and s.lak == "āśīrliṅ" and any(x in ("t", "th") for x in s.aff), lambda s: s.aff.insert(next(i for i, x in enumerate(s.aff) if x in ("t", "th")), "s"), "suṭ to the t / th of the tiṅ in āśīrliṅ (sta, āstām)")
    add("3.4.108", lambda s: s.P() and s.lak in ("liṅ", "āśīrliṅ") and s.up == "jhi", lambda s: setattr(s, "aff", tok("us")), "jhi → jus in liṅ (the j is it)")
    # ---- phase 2: the aṅga -------------------------------------------------------------------
    add("6.1.64", lambda s: s.r[0] == "ṣ", lambda s: (s.r.__setitem__(0, "s"), [s.r.__setitem__(i, {"ṭ": "t", "ṭh": "th", "ṇ": "n"}[x]) for i, x in enumerate(s.r) if i and x in ("ṭ", "ṭh", "ṇ")]), "the initial ṣ of the upadeśa → s, and the ṭ / ṭh / ṇ it had conditioned revert (ṣuñ → su, ṣṭigha~ → stigh, ṣaṇu~ → san: nimittāpāye naimittikasyāpy apāyaḥ)")
    add("6.1.65", lambda s: s.r[0] == "ṇ", lambda s: s.r.__setitem__(0, "n"), "the initial ṇ of the upadeśa → n (ṇīñ → nī)")
    add("6.1.10", lambda s: "ślu" in s.flags and not s.ab, lambda s: setattr(s, "ab", s.r[: next(i for i, x in enumerate(s.r) if x in V) + 1]), "the root doubled under ślu (6.1.1 / 6.1.4: ju-hu, da-dā, da-dhā)")
    add("6.1.8", lambda s: s.lak == "liṭ" and not s.ab, lambda s: setattr(s, "ab", s.r[: next(i for i, x in enumerate(s.r) if x in V) + 1]), "the root's first ekāc doubled before liṭ (6.1.1 ekāco dve prathamasya; the first is the abhyāsa, 6.1.4)")
    add("7.4.59", lambda s: s.ab[-1:] and s.ab[-1] in HRASVA, lambda s: s.ab.__setitem__(-1, HRASVA[s.ab[-1]]), "the abhyāsa vowel shortened")
    add("7.4.66", lambda s: s.ab[-1:] == ["ṛ"], lambda s: s.ab.__setitem__(-1, "a"), "ṛ of the abhyāsa → a (ca-kāra)")
    add("7.4.73", lambda s: s.ab[-1:] == ["u"] and "".join(s.r) == "bhū", lambda s: s.ab.__setitem__(-1, "a"), "u of bhū's abhyāsa → a (ba-bhūva)")
    add("7.4.62", lambda s: s.ab[:1] and s.ab[0] in CU, lambda s: s.ab.__setitem__(0, CU[s.ab[0]]), "ku / h of the abhyāsa → cu (ja-gāma, ca-kāra)")
    add("8.4.54", lambda s: s.ab[:1] and s.ab[0] in DEASP, lambda s: s.ab.__setitem__(0, DEASP[s.ab[0]]), "the aspirate of the abhyāsa → car (ba-bhūva)")
    add("7.2.13", lambda s: s.lak == "liṭ" and s.aff[:1] in (["v"], ["m"]) and "".join(s.r) in NO_IT_LIT, lambda s: s.flags.add("7.2.13"), "no iṭ in liṭ after kṛ, sṛ, bhṛ, vṛ, stu, dru, sru, śru (cakṛva)")
    add("7.2.35", lambda s: ((s.v[:1] in (["s"], ["t"]) or (s.pre[:1] == ["s"] and s.lak == "āśīrliṅ")) and not s.it and ("".join(s.r) in SET or ("".join(s.r) == "gam" and s.P() and s.v[:1] == ["s"]))) or (s.lak == "liṭ" and s.aff[:1] in (["v"], ["m"]) and not s.it and "7.2.13" not in s.flags),
        lambda s: setattr(s, "it", ["i"]), "iṭ before the val-initial ārdhadhātuka (sya, tās, sīyuṭ) for the seṭ root (7.2.10 keeps nī, labh aniṭ; 7.2.58 gamer iṭ before sya in parasmaipada); before liṭ's va / ma for every root outside 7.2.13 (babhūviva, jagmiva, ninyiva)")
    add("7.3.77", lambda s: "".join(s.r) == "gam" and s.v == ["a"] and s.lak in PRESENT, lambda s: setattr(s, "r", tok("gach")), "m of gam → ch before the śit śap")
    add("6.1.73", lambda s: s.r[-1:] == ["ch"] and "6.1.73" not in s.done, lambda s: s.r.insert(len(s.r) - 1, "c"), "tuk before ch")
    add("6.4.88", lambda s: "".join(s.r) == "bhū" and s.lak in ("luṅ", "liṭ") and not s.v and s.after_root() and s.after_root()[0] in V, lambda s: s.r.append("v"), "vuk to bhū before a vowel in luṅ / liṭ (abhūvan, babhūva, babhūviva)")
    add("7.2.115", lambda s: s.lak == "liṭ" and s.pit and s.r[-1] in VRDDHI, lambda s: s.r.__setitem__(-1, VRDDHI[s.r[-1]]) if s.r[-1] != "ṛ" else setattr(s, "r", s.r[:-1] + ["ā", "r"]), "vṛddhi of the final vowel before the ñit / ṇit ṇal (nai-, kār-)")
    add("7.2.116", lambda s: s.lak == "liṭ" and s.pit and len(s.r) >= 2 and s.r[-2] == "a" and s.r[-1] not in V, lambda s: s.r.__setitem__(-2, "ā"), "vṛddhi of the penultimate a before ṇal (ja-gāma)")
    add("6.4.98", lambda s: s.lak == "liṭ" and s.kit() and "".join(s.r) == "gam", lambda s: s.r.pop(-2), "the upadhā of gam dropped before the kit ending (jagmatuḥ, jagmiva)")
    add("7.2.1", lambda s: s.P() and s.lak == "luṅ" and s.v == ["s"] and s.r[-1] in VRDDHI, lambda s: s.r.__setitem__(-1, VRDDHI[s.r[-1]]), "vṛddhi before sic in parasmaipada (nai-ṣ-; the apavāda of 7.3.84)")
    add("7.3.86", lambda s: "7.3.86" not in s.done and (("ṇic" in s.flags and len(s.r) >= 3 and s.r[-2] not in V and s.r[-3] in ("i", "u", "ṛ")) or (((s.v == ["a"] and not s.vsit) or s.v == ["u"]) and len(s.r) >= 2 and s.r[-1] not in V and s.r[-2] in ("i", "u", "ṛ"))),
        lambda s: s.r.__setitem__(-3 if "ṇic" in s.flags else -2, GUNA[s.r[-3 if "ṇic" in s.flags else -2]]), "guṇa of the light penultimate before the ṇit ṇic, the pit śap or the ārdhadhātuka u (cur → cor, kṣiṇ → kṣeṇ; not before the ṅidvat śa: tudati, not *todati)")
    add("8.2.77", lambda s: s.v == tok("ya") and s.r[-1] in ("r", "v") and s.r[-2] in ("i", "u"), lambda s: s.r.__setitem__(-2, {"i": "ī", "u": "ū"}[s.r[-2]]), "the ik before the root-final r / v lengthened before hal (dīvyati, sīvyati)")
    add("7.3.74", lambda s: s.v == tok("ya") and s.root in SAM_LIST and s.r[-2] == "a", lambda s: s.r.__setitem__(-2, "ā"), "the eight śam-roots lengthened before śyan (śāmyati)")
    add("6.4.24", lambda s: s.vsit and not s.idit and len(s.r) >= 3 and s.r[-2] == "n" and s.r[-1] not in V and s.r[-3] in V, lambda s: s.r.pop(-2), "the penultimate n of a non-idit root dropped before the kit / ṅit (dabhnoti, stabhnoti, badhnāti, mathnāti)")
    add("7.3.79", lambda s: s.v == tok("nā") and "".join(s.r) == "jñā", lambda s: setattr(s, "r", tok("jā")), "jñā → jā before śnā (jānāti)")
    add("6.1.16", lambda s: s.vsit and s.up_root in SAMPRASARANA and "6.1.16" not in s.done, lambda s: setattr(s, "r", tok(SAMPRASARANA[s.up_root])), "samprasāraṇa of grah / jyā before the ṅit (1.1.45; with 6.1.108: gṛh-, ji-)")
    add("7.3.80", lambda s: s.vsit and s.gana == 9 and (s.root in PU_LIST or s.up_root.rstrip("ñ") in PU_LIST) and s.r[-1] in ("ū", "ṝ", "ī"), lambda s: s.r.__setitem__(-1, {"ū": "u", "ṝ": "ṛ", "ī": "i"}[s.r[-1]]), "the pvādi of the kryādi shortened before the śit (pu-nā-, lu-nā-, stṛ-ṇā-, li-nā-, ṛ-ṇā-; the svādi dhūñ keeps ū: dhūnoti)")
    add("6.4.23", lambda s: "śnam" in s.flags and "6.4.23" not in s.done and any(s.r[i:i + 3] == ["n", "a", "n"] for i in range(len(s.r) - 2)), lambda s: s.r.pop(next(i for i in range(len(s.r) - 2) if s.r[i:i + 3] == ["n", "a", "n"]) + 2), "the root's n (the nuṁ of hiṁs) dropped after śnam (hinasti)")
    add("6.4.111", lambda s: s.lak in PRESENT and not s.pit and (("śnam" in s.flags and "a" in s.r[1:]) or (s.root == "as" and s.r[:1] == ["a"])) and "6.4.111" not in s.done, lambda s: s.r.pop(len(s.r) - 1 - s.r[::-1].index("a")) if "śnam" in s.flags else s.r.pop(0), "the a of śnam and of as dropped before the kit / ṅit sārvadhātuka (runddhaḥ, bhindanti, staḥ, santi)")
    add("7.4.50a", lambda s: s.root == "as" and s.aff[:1] == ["s"] and s.r[-1:] == ["s"], lambda s: s.r.pop(), "the s of as dropped before the s-initial sārvadhātuka (asi; 7.4.50 tāsastyoḥ)")
    add("7.3.84", lambda s: s.r[-1] in GUNA and s.after_root() and not s.kit() and not s.vsit and (s.v or s.it or (s.flags & {"ślu", "śap-luk"} and s.pit and s.lak in PRESENT)), lambda s: setattr(s, "r", s.r[:-1] + tok(GUNA[s.r[-1]])), "guṇa of the root's final ik before the pit śap, the ārdhadhātuka iṭ / sya / tās / u / ṇic, or the pit tiṅ directly after the luk / ślu (bhū → bho, nī → ne, kṛ → kar, cori → core, juhoti); not before the kit āśīrliṅ nor the ṅidvat śit vikaraṇa (1.1.5, 1.2.4: sunoti, tudati)")
    add("7.3.84v", lambda s: s.lak in PRESENT and s.v[-1:] == ["u"] and s.pit and "3.4.87" not in s.done, lambda s: s.v.__setitem__(-1, "o"), "guṇa of the aṅga-final u (śnu, u) before the pit sārvadhātuka (sunoti, karoti, tanoti)")
    add("6.4.110", lambda s: s.root == "kṛ" and s.v == ["u"] and s.lak in PRESENT and not s.pit and s.r == tok("kar"), lambda s: s.r.__setitem__(1, "u"), "the a of kar → u before the kit / ṅit sārvadhātuka (kurutaḥ, kurvanti, kurute)")
    add("6.4.108", lambda s: s.r == tok("kur") and s.v == ["u"] and s.aff[:1] and s.aff[0] in ("m", "v"), lambda s: setattr(s, "v", []), "the u of karoti always dropped before m / v (kurvaḥ, kurmaḥ)")
    add("6.4.107", lambda s: s.v[-1:] == ["u"] and s.aff[:1] and s.aff[0] in ("m", "v") and s.root != "kṛ" and ((s.v == tok("nu") and s.r[-1] in V) or (s.v == ["u"] and s.r[-2] in V)), lambda s: s.v.pop(), "the u of the affix dropped before m / v when not preceded by a conjunct — optionally; the lopa branch is realised (sunvaḥ, tanmaḥ; sunuvaḥ, tanumaḥ recorded)")
    add("6.4.77", lambda s: s.v == tok("nu") and s.aff[:1] and s.aff[0] in V and s.r[-1] not in V, lambda s: s.v.__setitem__(-1, "uv"), "u of śnu after a conjunct → uvaṅ before a vowel (āpnuvanti, śaknuvaḥ)")
    add("6.4.87", lambda s: s.aff[:1] and s.aff[0] in V and ((s.v == tok("nu") and s.r[-1] in V) or (s.root == "hu" and "ślu" in s.flags)), lambda s: s.v.__setitem__(-1, "v") if s.v else s.r.__setitem__(-1, "v"), "u of hu / śnu after a non-conjunct → v before the vowel-initial sārvadhātuka (juhvati, sunvanti, cinvāte, śṛṇvanti)")
    add("6.4.112", lambda s: not s.pit and s.aff[:1] and ((s.v == tok("nā") and s.aff[0] in V) or (s.ab and s.r[-1:] == ["ā"] and (s.aff[0] in V or s.root in GHU))), lambda s: s.v.pop() if s.v else s.r.pop(), "the ā of śnā and of the abhyasta root dropped before the kit / ṅit sārvadhātuka — before a vowel (krīṇanti, punate, dadati, dadāte) and, for the ghu (1.1.20), before hal too (dattaḥ, dhattaḥ: 6.4.113's ī is aghoḥ)")
    add("6.4.113", lambda s: s.v == tok("nā") and s.aff[:1] and s.aff[0] not in V and not s.pit, lambda s: s.v.__setitem__(-1, "ī"), "the ā of śnā → ī before the hal-initial kit / ṅit sārvadhātuka (krīṇītaḥ, punīte)")
    add("8.3.24", lambda s: any(s.r[i] == "n" and s.r[i + 1] in JHAL for i in range(len(s.r) - 1)), lambda s: [s.r.__setitem__(i, "ṁ") for i in range(len(s.r) - 1) if s.r[i] == "n" and s.r[i + 1] in JHAL], "n → anusvāra before jhal, not at the end of the pada (hiṁsvaḥ, hiṁsanti; run-dh → ruṁ-dh, read again by 8.4.58)")
    add("8.4.2", lambda s: _natva_site(s) is not None, lambda s: _natva_set(s), "n of the affix / of śnam → ṇ after r / ṛ / ṣ across vowels, ku, pu (8.4.1 with 8.4.2: krīṇāti, śṛṇoti, ruṇaddhi, kṣuṇatti)")
    add("8.4.40", lambda s: s.v[:1] == ["n"] and s.r[-1] in ("c", "j", "ñ"), lambda s: s.v.__setitem__(0, "ñ"), "n → ñ after cu (khacñāti); not after ś (8.4.44 śāt: aśnāti, kliśnāti)")
    add("8.4.41n", lambda s: s.v[:1] == ["n"] and s.r[-1] in ("ṭ", "ṭh", "ḍ", "ḍh"), lambda s: s.v.__setitem__(0, "ṇ"), "n → ṇ after ṭu (8.4.41: mṛḍṇāti)")
    add("8.4.58", lambda s: any(s.r[i] == "ṁ" and s.r[i + 1] in YAY for i in range(len(s.r) - 1)), lambda s: [s.r.__setitem__(i, SAVARNA[s.r[i + 1]]) for i in range(len(s.r) - 1) if s.r[i] == "ṁ" and s.r[i + 1] in YAY], "anusvāra → the parasavarṇa nasal before yay (rundhanti, bhindanti; hiṁs keeps the anusvāra before s)")
    add("6.1.78", lambda s: s.r[-1] in ("e", "o", "ai", "au") and s.after_root() and s.after_root()[0] in V, lambda s: setattr(s, "r", s.r[:-1] + {"e": ["ay"], "o": ["av"], "ai": ["ā", "y"], "au": ["ā", "v"]}[s.r[-1]]), "ec → ay / av / āy / āv before a vowel (bhav-a, nay-a, nināy-a)")
    add("6.4.71", lambda s: s.lak in ("laṅ", "luṅ") and not s.ag and s.r[0] not in V, lambda s: setattr(s, "ag", ["a"]), "aṭ augment to the aṅga in laṅ / luṅ")
    add("6.4.72", lambda s: s.lak in ("laṅ", "luṅ") and not s.ag and s.r[0] in V, lambda s: setattr(s, "ag", ["ā"]), "āṭ to the vowel-initial aṅga in laṅ / luṅ")
    add("6.1.90", lambda s: s.ag == ["ā"] and s.r[0] in V, lambda s: (setattr(s, "ag", []), s.r.__setitem__(0, {"a": "ā", "i": "ai", "e": "ai", "u": "au", "o": "au"}[s.r[0]])), "vṛddhi for āṭ + the initial vowel (aidh-)")
    add("7.2.79", lambda s: s.lak == "liṅ" and "s" in s.pre, lambda s: s.pre.remove("s"), "the non-final s of liṅ's sārvadhātuka dropped (yās → yā, sīy → īy)")
    add("7.2.80", lambda s: s.lak == "liṅ" and s.P() and s.v == ["a"] and s.pre == ["y", "ā"], lambda s: setattr(s, "pre", ["i", "y"]), "yā (yās) → iy after a")
    add("7.2.81", lambda s: s.A() and s.a_final() and s.aff[:1] == ["ā"] and s.up in ("ātām", "āthām") and s.ngit() and not s.pre, lambda s: (setattr(s, "pre", ["i", "y"]), setattr(s, "aff", s.aff[1:])), "the ā of the ṅit (1.2.4) ātmanepada affix → iy after a (ātām, āthām)")
    add("6.4.105", lambda s: s.a_final() and s.aff == ["h", "i"], lambda s: setattr(s, "aff", []), "hi → luk after a (bhava)")
    add("7.3.101", lambda s: s.a_final() and s.aff[:1] and s.aff[0] in YAN_INIT and s.aff[0] != "ā" and "3.4.92" not in s.done, lambda s: _set_last_anga(s, ["ā"]), "a → ā before the yañ-initial sārvadhātuka (mi, vas, mas, vahi, mahi; va, ma)")
    add("7.3.96", lambda s: s.P() and s.lak == "luṅ" and s.v == ["s"] and s.aff in (["t"], ["s"]), lambda s: setattr(s, "aff", ["ī"] + s.aff), "īṭ to the apṛkta ending after sic (anaiṣīt, anaiṣīḥ)")
    add("8.2.26", lambda s: s.v == ["s"] and not s.it and s.r[-1] in JHAL and s.aff[:1] and s.aff[0] in JHAL, lambda s: setattr(s, "v", []), "the s (sic) dropped between jhal and jhal (alabdha, alabdhāḥ)")
    add("8.2.38", lambda s: s.root == "dhā" and s.ab == ["d", "a"] and s.r == ["dh"] and s.after_root() and s.after_root()[0] in ("t", "th", "s", "dh"), lambda s: s.ab.__setitem__(0, "dh"), "the d of dhā's abhyāsa → dh before t / th / s / dhv (dhattaḥ, dhatse, dhaddhve)")
    add("8.2.30", lambda s: s.r[-1] in ("c", "j") and s.after_root() and s.after_root()[0] in JHAL, lambda s: s.r.__setitem__(-1, {"c": "k", "j": "g"}[s.r[-1]]), "cu → ku before jhal (riṇakti, vinakti)")
    add("8.2.40", lambda s: s.r[-1] in JHAS and s.root != "dhā" and s.after_root() and s.after_root()[0] in ("t", "th") and not s.it, lambda s: (s.v if s.v else s.aff).__setitem__(0, "dh"), "t / th → dh after a jhaṣ, not after dhā (labh-dhās, labh-dha, run-dh-dhaḥ; dhattaḥ keeps t)")
    add("8.4.53", lambda s: s.r[-1] in JAS and s.after_root() and s.after_root()[0] in ("dh", "d", "b", "g", "j"), lambda s: s.r.__setitem__(-1, JAS[s.r[-1]]), "jhal → jaś before jhaś (labdhā)")
    add("8.4.55", lambda s: s.r[-1] in CAR and s.after_root() and s.after_root()[0] in KHAR, lambda s: s.r.__setitem__(-1, CAR[s.r[-1]]), "jhal → car before khar (lapsya, lapsīṣṭa)")
    add("6.4.143", lambda s: s.lak == "luṭ" and s.aff[:1] == ["ḍ"] and s.v[-2:] == ["ā", "s"], lambda s: (setattr(s, "v", s.v[:-2]), s.aff.pop(0)), "the ṭi of the aṅga dropped before the ḍit ḍā (bhavitā, labdhā)")
    add("7.4.51", lambda s: s.v[-1:] == ["s"] and s.lak == "luṭ" and s.aff[:1] == ["r"], lambda s: s.v.pop(), "the s of tās dropped before r (bhavitārau, bhavitāraḥ)")
    add("7.4.50", lambda s: s.v[-1:] == ["s"] and s.lak == "luṭ" and s.aff[:1] == ["s"], lambda s: s.v.pop(), "the s of tās dropped before the s-initial sārvadhātuka (bhavitāsi, labdhāse)")
    add("7.4.52", lambda s: s.v[-1:] == ["s"] and s.lak == "luṭ" and s.aff[:1] == ["e"], lambda s: s.v.__setitem__(-1, "h"), "the s of tās → h before e (labdhāhe)")
    # ---- phase 3: junction -----------------------------------------------------------------
    add("6.1.77", lambda s: (s.kit() and s.r[-1] in YAN and s.after_root() and s.after_root()[0] in V) or (s.v == ["u"] and s.aff[:1] and s.aff[0] in V), lambda s: s.r.__setitem__(-1, YAN[s.r[-1]]) if not (s.v == ["u"] and s.aff[:1] and s.aff[0] in V) else s.v.__setitem__(-1, "v"), "ik → yaṇ before a vowel: the kit liṭ cells (ninyatuḥ, cakratuḥ, ninyiva) and the u-vikaraṇa before anti (kurvanti)")
    add("6.1.87", lambda s: (s.v[-1:] == ["a"] and s.pre[:1] and s.pre[0] in ("i", "ī")) or (s.a_final() and s.aff[:1] and s.aff[0] in ("i", "ī", "u", "ū")),
        lambda s: (s.v.pop(), s.pre.__setitem__(0, "e")) if s.pre[:1] and s.pre[0] in ("i", "ī") else (_set_last_anga(s, []), s.aff.__setitem__(0, GUNA[s.aff[0]])), "a + ik → guṇa (bhave-y, labhe-y, labhe)")
    add("6.1.97", lambda s: s.a_final() and s.aff[:1] and s.aff[0] in ("a", "e", "o") and not s.pre, lambda s: _set_last_anga(s, []), "a + a guṇa vowel (a, e, o) → pararūpa (abhavam; labhe from labha + e)")
    add("6.1.101", lambda s: s.a_final() and s.aff[:1] == ["ā"], lambda s: (_set_last_anga(s, ["ā"]), s.aff.pop(0)), "a + ā → the long savarṇa (bhavāni, labhāvahai)")
    add("6.1.88", lambda s: s.anga()[-1:] and s.anga()[-1] in ("a", "ā") and s.aff[:1] == ["ai"] and not s.pre, lambda s: _set_last_anga(s, []), "a / ā + ai → vṛddhi (labhai, labhāvahai)")
    add("6.1.66", lambda s: s.pre[-1:] == ["y"] and s.aff[:1] and s.aff[0] in VAL, lambda s: s.pre.pop(), "y dropped before val (bhavet, bhaveva, labheta, labhete)")
    # ---- phase 4: tripādī -----------------------------------------------------------------
    add("8.2.29", lambda s: s.pre[-1:] == ["s"] and s.aff == ["t"], lambda s: s.pre.pop(), "the s beginning the pada-final conjunct dropped (bhūyāt)")
    add("8.2.23", lambda s: s.aff[-2:] == ["n", "t"], lambda s: s.aff.pop(), "the conjunct-final t dropped at the end of the pada (abhavan)")
    add("8.3.59", lambda s: any(_s_after_in(s)), lambda s: _satva(s), "the s of an affix / augment → ṣ after iṇ (bhaviṣyati, neṣyati, edhiṣīṣṭa, lapsīṣṭa)")
    add("8.4.41", lambda s: (s.v[-1:] == ["ṣ"] and s.aff[:1] and s.aff[0] in ("t", "th")) or any(s.aff[i] in ("t", "th") and s.aff[i - 1] == "ṣ" for i in range(1, len(s.aff))),
        lambda s: [s.aff.__setitem__(i, {"t": "ṭ", "th": "ṭh"}[s.aff[i]]) for i in range(len(s.aff)) if s.aff[i] in ("t", "th") and (s.aff[i - 1] if i else (s.v[-1:] or [""])[0]) == "ṣ"], "t / th → ṭ / ṭh after ṣ (lapsīṣṭa, anaiṣṭām, aidhiṣṭhāḥ)")
    add("8.2.66", lambda s: s.aff[-1:] == ["s"], lambda s: s.aff.__setitem__(-1, "r"), "s → ru at the end of the pada")
    add("8.3.15", lambda s: s.aff[-1:] == ["r"] and s.up not in ("ran",), lambda s: s.aff.__setitem__(-1, "ḥ"), "r → visarjanīya at pause")
    return R


# rows whose surface effect coincides with another row on this suite (recorded, not counted as vacuous):
SURFACE_COINCIDENT = {"7.1.58": "the nuṁ of the idit hisi~ is dropped again by 6.4.23 in every śnam cell of the suite (hinasti, hiṁsanti: the anusvāra there is śnam's n); a cell of hiṁs without śnam (hiṁsitum) is not in the suite, so the row is kept, applied and recorded but not counted as load-bearing", "3.4.92": "āṭ before ni / va / ma gives bhavāni, bhavāva, bhavāma; without it 7.3.101's dīrgha gives the same surface (theorum/96 recorded the same); labhai from a + ai by 6.1.88 either way"}
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


def t1_suite() -> dict[str, Any]:
    O = oracles()
    def key(r, l, pd): return f"{r}.{l}" + (f".{pd}" if pd else "")
    forms = {key(r, l, pd): paradigm(r, l, cells=cs, pada=pd) for r, l, cs, pd in SUITE}
    def ora(r, l, pd): return NASAL[r][3] if r in NASAL else (V_ORACLE[(r, pd)] if (l == "laṭ" and (r, pd) in V_ORACLE) else O[r][l])
    mism = {f"{key(r, l, pd)}.{c}": (forms[key(r, l, pd)][c], ora(r, l, pd)[c]) for r, l, cs, pd in SUITE for c in cs if forms[key(r, l, pd)][c] != ora(r, l, pd)[c]}
    broken: dict[str, list[str]] = {}
    for rid in IDS:
        broken[rid] = [f"{key(r, l, pd)}.{c}" for r, l, cs, pd in SUITE for c in cs if conjugate(r, l, c, off=(rid,), pada=pd)[0] != ora(r, l, pd)[c]]
    vacuous = [r for r in IDS if not broken[r] and r not in SURFACE_COINCIDENT]
    cells = sum(len(cs) for _, _, cs, _ in SUITE)
    checks = {"all_596_cells_equal_the_oracles": not mism, "every_rule_row_is_load_bearing_on_the_suite_except_the_declared_surface_coincident": not vacuous}
    paths = {k: conjugate(*k.split("."))[1] for k in ("bhū.laṭ.1s", "gam.laṅ.3p", "nī.loṭ.2s", "bhū.liṅ.3p", "labh.laṭ.3d", "edh.laṅ.1s", "labh.loṭ.1d", "labh.liṅ.3s")}
    return {"checks": checks, "cells": cells, "mismatches": mism, "broken_counts": {r: len(b) for r, b in broken.items()}, "broken": broken, "vacuous_rows": vacuous, "surface_coincident": SURFACE_COINCIDENT, "forms": forms, "paths": paths}


def build_certificate() -> dict[str, Any]:
    packets = {"t1_suite": t1_suite()}
    checks = {f"{k}_all_checks": all(v["checks"].values()) for k, v in packets.items()}
    status = "PASS_TING_RULE_TABLE_ENGINE_CANDIDATE" if all(checks.values()) else "FAIL_TING_RULE_TABLE_ENGINE_CANDIDATE"
    return {
        "schema": "rkf.ting_rule_table_engine_candidate.v1", "status": status, "sources": SOURCES, "rule_order": IDS, "roots": ROOTS,
        "claim_boundary": {
            "proved_by_exact_finite_certificate": [
                f"one rule table of {len(IDS)} rows (each a quoted sūtra as guard + action) and one driver reproduce the 325 cells of the certified paradigms of bhū, gam, nī, kṛ (parasmaipada) and edh, labh (ātmanepada) — the present system laṭ, laṅ, loṭ, vidhiliṅ (180 cells: theorum/64, 66, 95, 96, 99), the ārdhadhātuka lṛṭ, luṭ, āśīrliṅ, luṅ (125 cells: theorum/97, 101, 112, 115, 116, 117) and liṭ (20 cells: theorum/102) — exactly from the earlier pinned packets, and the 79 laṭ cells of the vikaraṇa classes (pac; div, siv, śam; tud, nud; cur; su, ci, śru, āp, śak; tan, kṛ; krī, pū, lū) and the 101 laṭ cells of adādi (ad, as), juhotyādi (hu, dā, dhā) and rudhādi (rudh, bhid, ric, vic, kṣud, chṛd, tṛd, kṛt, hiṁs), and the 91 quoted cells of 86 further svādi / tanādi / kryādi entries (research/panini_grammar/nasal_present), declared from the grammar-verification branch's quoted present tables (Kāśikā / Kaumudī / Laghukaumudī anchors in research/panini_grammar/vikarana_lat, non_thematic_lat, exception_lat, abhyasa_lat, snam_lat); every row is load-bearing on at least one cell (per-row broken sets recorded)",
                "the sārvadhātuka / ārdhadhātuka split is the lakāra set (3.4.113 / 3.4.114 / 3.4.116): śap only before the present system, sya / tās / sic / aṅ as the vikaraṇa segment, iṭ (7.2.35) as its own segment for the seṭ roots (bhū, edh: declared from the Dhātupāṭha accent; nī, labh aniṭ by 7.2.10; gam by 7.2.58 before sya), the kit of āśīrliṅ (3.4.104) as a predicate that turns 7.3.84 off; 8.3.59 reads the segment boundaries (affix / augment s after iṇ, not the pada-final s: 8.3.55)",
                "the nasal classes at breadth (theorum/134): 86 svādi / tanādi / kryādi entries from the branch's quoted tables ride on the rows of theorum/132 with eight additions — 3.1.82's śnu (first alternative), 6.4.24's nasal-lopa before the ṅidvat vikaraṇa (dabhnoti, badhnāti, mathnāti), 7.3.79, 6.1.16 with 1.1.45 / 6.1.108 (gṛhṇāti, jināti), 8.4.40 under 8.4.44 (khacñāti; aśnāti, kliśnāti), 8.4.41's n (mṛḍṇāti), 8.4.39's kṣubhnādi as a ṇatva exception (kṣubhnāti, tṛpnoti), 6.1.64's reversion of the ṭ / ṇ the ṣ had conditioned (stighnute, sanoti), 7.3.80 restricted to the kryādi pvādi (dhūnoti against dhunāti), 7.3.86 before the ārdhadhātuka u (kṣeṇoti)",
                "adādi / juhotyādi / rudhādi (theorum/133): the luk (2.4.72) and ślu (2.4.75) are flags that keep 3.1.68 off and let 7.3.84 read the pit tiṅ directly (juhoti); ślu doubles by 6.1.10 on the same abhyāsa segment as liṭ (7.4.59, 7.4.62, 8.4.54 shared); śnam (3.1.78) is an infix placed by 1.1.47 inside the root segment, ṅidvat like every śit vikaraṇa; 6.4.111 drops its a and the a of as before the kit / ṅit tiṅ; 6.4.112 is generalised to the abhyasta ā and, for the ghu (1.1.20), before hal (dattaḥ) while 6.4.113's ī stays aghoḥ; 8.2.38 for dhā with 8.2.40 read as adhaḥ; 7.1.4 before 7.1.5 / 7.1.3; the tripādī order 8.3.24 → 8.4.2 → 8.4.58 is what keeps rundhanti's n dental and ruṇaddhi's ṇ retroflex (the n that 8.4.58 restores is asiddha for 8.4.2)",
                "the vikaraṇa classes (theorum/132): the vikaraṇa is a row (3.1.25 ṇic, 3.1.69 śyan, 3.1.73 śnu with 3.1.74, 3.1.77 śa, 3.1.79 u, 3.1.81 śnā) and its ś-it-ness a state predicate: a śit vikaraṇa is sārvadhātuka (3.4.113) and, apit, ṅidvat (1.2.4) — so 7.3.84 / 7.3.86 are off the root (sunoti, tudati) — while the ś-less u and ṇic are ārdhadhātuka (3.4.114) and take the guṇa (karoti, corayati); the aṅga-final u takes 7.3.84 before the pit tiṅ only (sunoti / sunutaḥ); 6.4.110 / 6.4.108 for kṛ, 6.4.107 (lopa branch realised, the other recorded), 6.4.77 / 6.4.87 by the conjunct test, 6.4.112 / 6.4.113 for śnā, 7.3.80 for the pvādi, 8.2.77 / 7.3.74 for śyan, 8.4.2 across the root",
                "liṭ: the abhyāsa is a segment (6.1.8 with 6.1.1 / 6.1.4; 7.4.59, 7.4.62, 7.4.66, 7.4.73, 8.4.54 as rows on it), 1.2.5's kit as a predicate (ṇal pit by 1.1.56 as tip's substitute: vṛddhi 7.2.115 / 7.2.116; the kit cells: 1.1.5, 6.4.98, 6.1.77), 6.4.88's vuk before 7.2.115 (babhūva, not *babhāva), 7.2.13 as a flag that 7.2.35 reads (cakṛva)",
                "bhūyāt: the s of yās is dropped by 8.2.29 (the pada-final conjunct) and kept in bhūyāstām / bhūyāsuḥ; theorum/115 reached the same three forms with 7.2.79 on the 3s cell — the forms agree, the rule attribution differs, and this table's attribution is the one recorded here (7.2.79 is the sārvadhātuka rule and does not reach āśīrliṅ)",
                "the lakāra-specific substitutions of 3.4.77–3.4.113 are rows; the ṅit-ness of the apit sārvadhātuka (1.2.4) and of liṅ (3.4.103) is a state predicate, not a row; 3.4.85 loṭo laṅvat is realised as loṭ in the guards of 3.4.99 / 3.4.101",
                "3.4.92's āṭ makes 7.3.101 vacuous on the loṭ uttama dual / plural (bhavāva by either): the table keeps 7.3.101 off where āṭ fired; 3.4.92 is therefore surface-coincident on this suite and is declared so (not counted as load-bearing, not hidden)",
            ],
            "NOT_claimed": ["tṛṇu (the branch anchors tṛṇoti / tṛṇute while 7.3.86 as a row would give tarṇoti: the ground of the attested form is not derived here, the cells are left out), ṛṇu (ṛṇoti / arṇutaḥ) and khav (khaunāti), the śnā branch of 3.1.82 as set-valued output", "the ātmanepada 3s cells of kṣud / chṛd / tṛd / khid / vid (kṣunte …) and of ric / vic (riṅkte), und, añj, tṛh, bhuj, indh (the branch's anchors there need rows not yet in the table), the 3s of as (asti) and the 3s / 3p of dhā (not anchored in the branch's tables)", "the vikaraṇa-class cells beyond those quoted (the full paradigms of su, kṛ, krī …), the 3.1.70 / 3.1.82 options, adādi (śap-luk) and juhotyādi (ślu), rudhādi (śnam), the ātmanepada 1.3.72 ground of each ubhayapadin cell (the pada is declared with the cell), the second branch of 6.4.107 as set-valued output", "7.4.60 halādiḥ śeṣaḥ (no cluster-initial root in the certified liṭ oracle; the row would be vacuous and is not in the table), liṭ ātmanepada (3.4.81), the thal / athus / a cells and 1.2.6 / 7.2.62 options", "the ground for the absence of iṭ before the parasmaipada yāsuṭ (bhūyāt, not *bhaviyāt) is taken from the certified forms of theorum/115, not derived (the 7.2.35 row is guarded off that segment)", "liṭ, lṛṅ, luṭ of gam (not in the earlier oracle), the full ātmanepada paradigms where the earlier packets certified six / four cells (the table is checked on exactly the certified cells)", "the other gaṇas (the vikaraṇas other than śap), ārdhadhātuka lakāras (liṭ, luṭ, lṛṭ, luṅ, āśīrliṅ: theorum/97, 101, 102, 112, 115–117 remain per-packet until they are rows here), the passive (yak), the derived stems (ṇic, san, yaṅ), accent (udātta of 3.4.103 / 6.4.71), RH, YM"],
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
