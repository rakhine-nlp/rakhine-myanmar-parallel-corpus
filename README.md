{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 TimesNewRomanPSMT;\f1\fnil\fcharset0 AppleColorEmoji;\f2\fnil\fcharset77 NotoSerifMyanmar-Regular;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red109\green109\blue109;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c50196\c50196\c50196;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid101\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid2}
{\list\listtemplateid3\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid201\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid3}
{\list\listtemplateid4\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid301\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid4}
{\list\listtemplateid5\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid401\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid5}
{\list\listtemplateid6\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid501\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid6}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}{\listoverride\listid3\listoverridecount0\ls3}{\listoverride\listid4\listoverridecount0\ls4}{\listoverride\listid5\listoverridecount0\ls5}{\listoverride\listid6\listoverridecount0\ls6}}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # 
\f1 \uc0\u55356 \u57104 
\f0  Rakhine \'96 Myanmar Parallel Corpus\
\
This repository contains a parallel dataset for **Rakhine \uc0\u8596  Myanmar language machine translation** and NLP research.\
\
It is designed for:\
- Machine Translation (MT)\
- Language modeling\
- NLP research\
- Dialect analysis (Rakhine Burmese)\
\
---\
\
# 
\f1 \uc0\u55357 \u56524 
\f0  Project Overview\
\
Rakhine language is a major dialect/language variety in Myanmar, but digital language resources are still limited.\
\
This project aims to build:\
- 
\f1 \uc0\u55357 \u56538 
\f0  Parallel sentence corpus (Rakhine \uc0\u8596  Myanmar)\
- 
\f1 \uc0\u55358 \u56800 
\f0  Training data for AI translation models\
- 
\f1 \uc0\u55357 \u56586 
\f0  Future speech + text datasets\
\
---\
\
# 
\f1 \uc0\u55357 \u56513 
\f0  Dataset Structure\
\pard\pardeftab720\partightenfactor0
\cf0 \expnd0\expndtw0\kerning0
\
rakhine-myanmar-parallel-corpus/\
\uc0\u9474 \
\uc0\u9500 \u9472 \u9472  data/\
\uc0\u9474  \u9500 \u9472 \u9472  train.csv\
\uc0\u9474  \u9500 \u9472 \u9472  dev.csv\
\uc0\u9474  \u9500 \u9472 \u9472  test.csv\
\uc0\u9474 \
\uc0\u9500 \u9472 \u9472  raw_data/\
\uc0\u9474  \u9500 \u9472 \u9472  rakhine_text.txt\
\uc0\u9474  \u9500 \u9472 \u9472  myanmar_text.txt\
\uc0\u9474 \
\uc0\u9500 \u9472 \u9472  scripts/\
\uc0\u9474  \u9500 \u9472 \u9472  align_sentences.py\
\uc0\u9474  \u9500 \u9472 \u9472  clean_data.py\
\uc0\u9474 \
\uc0\u9500 \u9472 \u9472  README.md\
\uc0\u9500 \u9472 \u9472  LICENSE\
\
\
---\
\
# 
\f1 \uc0\u55357 \u56522 
\f0  Data Format\
\
## CSV format (parallel sentences)\
\
| rakhine | myanmar |\
|---------|---------|\
| 
\f2 \uc0\u4100 \u4139 
\f0  
\f2 \uc0\u4101 \u4140 \u4152 \u4117 \u4156 \u4142 \u4152 \u4119 \u4155 \u4140 \u4122 \u4154 
\f0  | 
\f2 \uc0\u4100 \u4139 
\f0  
\f2 \uc0\u4101 \u4140 \u4152 \u4117 \u4156 \u4142 \u4152 \u4117 \u4156 \u4142 
\f0  |\
| 
\f2 \uc0\u4116 \u4100 \u4154 
\f0  
\f2 \uc0\u4103 \u4140 \u4121 \u4158 \u4140 \u4124 \u4146 
\f0  | 
\f2 \uc0\u4126 \u4100 \u4154 
\f0  
\f2 \uc0\u4120 \u4122 \u4154 \u4121 \u4158 \u4140 \u4124 \u4146 
\f0  |\
\
---\
\
# 
\f1 \uc0\u9881 \u65039 
\f0  How to Build Dataset\
\
### 1. Prepare raw text files\
- `raw_data/rakhine_text.txt`\
- `raw_data/myanmar_text.txt`\
\
### 2. Run alignment script\
```bash\
python scripts/align_sentences.py\
\
\pard\pardeftab720\sa280\partightenfactor0
\cf0 3. Output generated:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf0 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
data/train.csv\
\pard\pardeftab720\partightenfactor0
\cf3 \
\pard\pardeftab720\sa321\partightenfactor0

\f1 \cf0 \uc0\u55358 \u56800 
\f0  Use Cases\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls2\ilvl0\cf0 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Neural Machine Translation (NMT)\
\ls2\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Chatbot training\
\ls2\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Dialect comparison (Rakhine vs Standard Burmese)\
\ls2\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Language preservation\
\pard\pardeftab720\partightenfactor0
\cf3 \
\pard\pardeftab720\sa321\partightenfactor0

\f1 \cf0 \uc0\u55357 \u56960 
\f0  Future Improvements\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls3\ilvl0\cf0 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Add English translation layer (Rakhine \uc0\u8596  Myanmar \u8596  English)\
\ls3\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Add speech dataset (audio + transcription)\
\ls3\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Improve alignment using semantic similarity models\
\ls3\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Expand dataset to 10,000+ sentence pairs\
\pard\pardeftab720\partightenfactor0
\cf3 \
\pard\pardeftab720\sa321\partightenfactor0

\f1 \cf0 \uc0\u9888 \u65039 
\f0  Limitations\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls4\ilvl0\cf0 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Initial dataset is rule-based aligned (line-by-line)\
\ls4\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Sentence quality depends on manual curation\
\ls4\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Advanced semantic alignment is recommended for large-scale training\
\pard\pardeftab720\partightenfactor0
\cf3 \
\pard\pardeftab720\sa321\partightenfactor0

\f1 \cf0 \uc0\u55357 \u56540 
\f0  License\
\pard\pardeftab720\sa240\partightenfactor0
\cf0 This dataset is intended for research and open-source NLP development.\
Suggested license:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls5\ilvl0\cf0 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Creative Commons Attribution 4.0 (CC BY 4.0)\
\pard\pardeftab720\partightenfactor0
\cf3 \
\pard\pardeftab720\sa321\partightenfactor0

\f1 \cf0 \uc0\u55358 \u56605 
\f0  Contribution\
\pard\pardeftab720\sa240\partightenfactor0
\cf0 Contributions are welcome:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls6\ilvl0\cf0 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Add new sentence pairs\
\ls6\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Improve translations\
\ls6\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Fix alignment issues\
\ls6\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Add dialect variations\
\pard\pardeftab720\partightenfactor0
\cf3 \
\pard\pardeftab720\sa321\partightenfactor0

\f1 \cf0 \uc0\u55356 \u57101 
\f0  Goal\
\pard\pardeftab720\sa240\partightenfactor0
\cf0 To support digital preservation and AI development for the Rakhine language and its dialects.\
\pard\pardeftab720\partightenfactor0
\cf3 \
\pard\pardeftab720\sa321\partightenfactor0

\f1 \cf0 \uc0\u55357 \u56556 
\f0  Contact\
\pard\pardeftab720\sa240\partightenfactor0
\cf0 If you are contributing to Rakhine NLP or language technology projects, collaboration is welcome.\
}