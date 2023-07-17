sex = [
    r"sex",
    r"promiscu(ous|ity)",
    r" porn ",
    r"pornograph(y|ic)"
    r"erotic",
    r"lgbt",
    r"lesbian",
    r"gay",
    r"bisexual",
    r"trans(gender|sexual)",
    r"queer",
    r"non ?binary"
]

financial = [
    r'poor',
    r'poverty',
    r'struggl(ing|er)',
    r'wealth(y|iest)',
    r'gambl(ing|er)',
    r'betting',
    r' credit ?(level|score|crunched)?',
    r'(un)?insured',
    r'insurance',
    r'shallow pocket',
    r'urban survivor',
    r'tight money',
    r'tough times',
    r'retir(ement|int|ee)',
    r'royalty',
    r'diamonds',
    r'pearls',
    r'champagne',
    r'luxury',
]

latent_racism = [
    r'ethnic',
    r'migra(nt|ted|tion)',
    r'minorit(y|ies)',
    r'multicultural',
    r'caucasian',
    r'african',
    r'hispanic',
    r'latin(o|a)',
    r'arabic',
    r'middle east',
    r'asian',
    r'african american',
    r'indian',
    r'pacific islander',
    r'white',
    r'native',
]

religion = [
    r'religio(n|ous)',
    r' faith',
    r'christian',
    r'catholic',
    r'protestant',
    r'muslim',
    r'islam',
    r' jew',
    r'judais',
    r'buddhis[tm]',
    r'hinduis[tm]',
    r'atheis[tm]',
    r'spiritual',
    r'church',
    r'mosque',
    r'synagog',
    r'temple',
]

health = [
    r'disease',  # treatment general
    r'illness',
    r'pain',
    r'fatigue',
    r'surgery',
    r'arthritis',
    r'hypertension',
    r'fibromyalgia',
    r'pancrea(s|tic)',
    r'sleep apnea',
    r'migraine',
    r'asthma',
    r' dvt ',
    r'kidney disease',
    r'constipat(ion|ed)',
    r' copd ',
    r'smok(ing|er)',
    r'injur(ed|y)',

    r'obes(e|ity)',  # Obesity/heart
    r'(over)?weight( loss)?',
    r'diabet(es|ic)',
    r'atrial fibrillation',
    r'blood (pressure|clot)',
    r'heart (disease|failure|condition)',
    r'stroke',
    r'coronary',
    r'artery',
    r' dvt ',

    r'alzheimer',  # Neurodegenerative
    r'dementia',
    r'parkinson',
    r' ms ',
    r'multiple (sclerosis|sklerose)',
    r'huntington',
    r'cerebral palsy',


    r'cancer',  # Cancer and rel.
    r'tobacco',
    r'respiratory',
    r'leukemia',
    r'lymphoma',
    r'tumor',


    r'pregnan(t|cy)',  # sexual health
    r'matern(al|ity)',
    r'abort(ion|ed)',
    r'family planning',
    r'parent(hood)?',
    r'miscarriage',
    r'menopause',
    r'(in)?fertil(e|ity)',
    r'ovulat(e|ion)',
    r'viagra',
    r'erectile dysfunction',
    r'contracepti(ve|ion)',
    r'urinary tract infection',
    r' uti ',
    r'menstrua(l|ting|te)',

    r'hearing (aid|loss)',  # disabilities
    r' deaf(ness)? ',
    r'paraplegi[aec]',
    r'disab(led|ility)',
    r'blind',
    r'impair(ment|ed)',



    r'autis(m|tic)',  # psychological
    r' adh(d|s) ',
    r'anxiety',
    r'psych(olog|iatr)',
    r'depress(ed|ion)',
    r'mental',
    r'addict',
    r'alcohol',
    r'drugs',
    r'cannabis',
    r'painkiller',
    r'opioid',
    r'abuse',
    r'bipolar',
    r'disorder',
    r'schizoph',
    r'panic',
    r'insomnia',
    r'sleep disorder',
]

personality = [
    r'tattoo',
    r'hipster',
    r'dog owner',
    r'trendy moms',
    r'pension',
    r'aspirations',
    r'dreams',
    r'happiness',
    r' lov(e|ing) ',
    r'lone wolve',
    r'emotional',
    r'rebellious',
    r'self image',
    r'concerned'
    r'confident',
    r'social',
    r'status shopper',
    r'extraver(sion|t)',
    r'neuroticis(m|t',
    r'openness',
    r'conscientious(ness)?',
    r'agreeable(ness)?',
    r'general attitude',
    r'dealing with stress',
    r'romantic',
    r'divorce'
]


political = [
    r'unionized',
    r'(labor|trade) union',
    r'politic',

    r'advoca(cy|te)',  # advocacy
    r'support(er)?',
    r' vot(er|ed|ing) ',
    r'newspaper',
    r'subscri(ber|ption)',

    r'conservative',  # political orientation
    r'liberal',
    r'progressive',
    r'communis[tm]',
    r'socialis[tm]',
    r'centris[tm]',
    r'(left|right) wing',
    r'secular',
    r'democra(t|cy)',
    r'radical',
    r'authoritarian',

    r'terror',  # specific subjects
    r'marijuana',
    r' weed ',
    r'cannabis'
    r'gun (control|rights)',
    r'equality',
    r'immigra(nt|tion)',
    r'aslyum',
    r'environment(al)?',
    r'conservation',
    r'organized labor',
    r'pro (choice|life)',
    r'animal rights',
    r'defund police',
    r'black lives matter',
    r' blm ',
    r'polic(y|ies)',
    r'military',
    r'ukraine',
    r'russia',
    r'police',
    r'crim(e|inal)',
    r'covid',
    r'corona',
]
