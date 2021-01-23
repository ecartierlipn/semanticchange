# This directory contains data files (tsc, csv and xlsx files) and scripts (py and ipynb files) to generate semantic lexical change candidate words

If you don't care of how all is done, go straight to **Semantic change candidate words** for files to work with (for manual validation of word candidates).


## Data files
### Frantext frequency lists
`frantext_1800-1850_all_freq.csv` : output file from Frantext web interface for corpus 1800-1850
`frantext_1950-2000_all_freq.csv` : output file from Frantext web interface for corpus 1950-2000

`frantext_1800-1850_all.xlsx` : output file from parsing csv file above (Frantext 1800-1850) - see `generate_goldstandard_candidates_from_wiktionnaire_frantext.py`(or ipynb) (part A)
`frantext_1950-2000_all.xlsx` : output file from parsing csv file above (Frantext 1800-1850) - see `generate_goldstandard_candidates_from_wiktionnaire_frantext.py`(or ipynb) (part A)

### Wiktionnary Files
Note that to generate theses files you need to download Glawi : http://redac.univ-tlse2.fr/lexiques/glawi.html
`wiktionnary_adjectif_def.tsv` : adjectives from Glawi xml files (with word, pos, usage notes and definition, one sense per line, tsv format). generated with `extractWiktionnaire_n_v_adj.py`
`wiktionnary_nom_def.tsv` : nouns from Glawi xml files (with word, pos, usage notes and definition, one sense per line, tsv format). generated with `extractWiktionnaire_n_v_adj.py`
`wiktionnary_verbs_def.tsv` : verbs from Glawi xml files (with word, pos, usage notes and definition, one sense per line, tsv format). generated with `extractWiktionnaire_n_v_adj.py`

### **Semantic change candidate words**
`verbes_a_choisir_dico-rey.xlsx` : candidate verbs for semantic change (present in dictionnaire historique du français and Frantext frequency above 50). See `generate_goldstandard_candidates_from_dicorey_frantext.py` (or .ipynb)
`verbes_a_choisir_wiktionnaire.xlsx` : candidate verbs (word, senses number, freq1850, freq1950) for semantic change (1 to 5 senses in wiktionary and Frantext frequency above 50). See `generate_goldstandard_candidates_from_wiktionnaire_frantext.py` (or .ipynb)
`verbes_a_choisir_wiktionnaire_complete.xlsx` : candidate verbs for semantic change (word, senses number, freq1850, freq1950, definitions) (1 to 5 senses in wiktionary and Frantext frequency above 50). See `generate_goldstandard_candidates_from_wiktionnaire_frantext.py` (or .ipynb)

`noms_a_choisir_dico-rey.xlsx` : candidate nouns for semantic change (present in dictionnaire historique du français and Frantext frequency above 50). See `generate_goldstandard_candidates_from_dicorey_frantext.py` (or .ipynb)
`noms_a_choisir_wiktionnaire.xlsx` : candidate nouns (word, senses number, freq1850, freq1950) for semantic change (1 to 5 senses in wiktionary and Frantext frequency above 50). See `generate_goldstandard_candidates_from_wiktionnaire_frantext.py` (or .ipynb)
`noms_a_choisir_wiktionnaire_complete.xlsx` : candidate nouns for semantic change (word, senses number, freq1850, freq1950, definitions) (1 to 5 senses in wiktionary and Frantext frequency above 50). See `generate_goldstandard_candidates_from_wiktionnaire_frantext.py` (or .ipynb)

## Script files
`extractWiktionnaire_n_v_adj.py` : script  to generate synthesis of Glawi xml wiktionary for n, adj and v (see Wiktionnary files above)
`generate_goldstandard_candidates_from_dicorey_frantext.ipynb` : script to generate Semantic change candidate words from Dict. historique du français (see Semantic change candidate words files above)
`generate_goldstandard_candidates_from_wiktionnaire_frantext.ipynb` : notebook to generate Semantic change candidate words from wiktionary (see Semantic change candidate words files above)
`generate_goldstandard_candidates_from_wiktionnaire_frantext.py` : the same as above, command line python format
