ud2indo = {
    ('AdpType', 'Post'): {'Post'},
    ('AdvType', 'Deg'): {'Deg'},
    ('Aspect', 'Imp'): {'Imp'},
    ('Aspect', 'Perf'): {'Perf'},
    ('Case', 'Acc'): {'Obl'},
    ('Case', 'Acc,Dat'): {'Obl', 'Dat'},
    ('Case', 'Acc,Erg'): {'Obl', 'Erg'},
    ('Case', 'Acc,Gen'): {'Obl', 'Gen'},
    ('Case', 'Acc,Ine'): {'Obl', 'Ine'},
    ('Case', 'Acc,Ins'): {'Obl', 'Ins'},
    ('Case', 'Nom'): {'Dir'},
    ('Echo', 'Rdp'): {'Echo'},
    ('Foreign', 'Yes'): {'Foreign'},
    ('Gender', 'Fem'): {'Fem'},
    ('Gender', 'Masc'): {'Masc'},
    ('Mood', 'Imp'): {'Imp'},
    ('Mood', 'Ind'): {'Ind'},
    ('Mood', 'Sub'): {'Sub'},
    ('NumType', 'Card'): {'Card'},
    ('NumType', 'Ord'): {'Ord'},
    ('Number', 'Plur'): {'Pl'},
    ('Number', 'Sing'): {'Sg'},
    ('Person', '1'): {'1st'},
    ('Person', '2'): {'2nd'},
    ('Person', '3'): {'3rd'},
    ('Polarity', 'Neg'): {'Neg'},
    ('Polite', 'Form'): {'Frm'},
    ('Polite', 'Infm'): {'Fam'},
    ('Poss', 'Yes'): {'Poss'},
    ('PronType', 'Dem'): {'Dem'},
    ('PronType', 'Ind'): {'Ind'},
    ('PronType', 'Int'): {'Int'},
    ('PronType', 'Neg'): {'Neg'},
    ('PronType', 'Prs'): {'Prs'},
    ('Tense', 'Fut'): {'Fut'},
    ('Tense', 'Past'): {'Past'},
    ('Tense', 'Pres'): {'Pres'},
    ('VerbForm', 'Conv'): {'Conv'},
    ('VerbForm', 'Fin'): {'Fin'},
    ('VerbForm', 'Inf'): {'Inf'},
    ('VerbForm', 'Part'): {'Part'},
    ('Voice', 'Act'): {'Act'},
    ('Voice', 'Pass'): {'Pass'},
    ('_',): {},
}

ud2indo = {k: frozenset(v) for (k, v) in ud2indo.items()}
