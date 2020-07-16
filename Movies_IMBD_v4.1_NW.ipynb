{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {
    "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
    "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5",
    "colab": {},
    "colab_type": "code",
    "id": "U2D2gTdJVp90"
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "from collections import Counter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {
    "_cell_guid": "79c7e3d0-c299-4dcb-8224-4455121ee9b0",
    "_uuid": "d629ff2d2480ee46fbb7e2d37f6b5fab8052498a",
    "colab": {},
    "colab_type": "code",
    "id": "oyGfxL3eVp9-"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>imdb_id</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>original_title</th>\n",
       "      <th>cast</th>\n",
       "      <th>director</th>\n",
       "      <th>tagline</th>\n",
       "      <th>overview</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>release_date</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>955</th>\n",
       "      <td>tt0280760</td>\n",
       "      <td>9000000</td>\n",
       "      <td>4777465</td>\n",
       "      <td>Igby Goes Down</td>\n",
       "      <td>Kieran Culkin|Claire Danes|Jeff Goldblum|Jared...</td>\n",
       "      <td>Burr Steers</td>\n",
       "      <td>Insanity is relative.</td>\n",
       "      <td>A young man's peculiar upbringing renders him ...</td>\n",
       "      <td>97</td>\n",
       "      <td>Comedy|Drama</td>\n",
       "      <td>United Artists</td>\n",
       "      <td>9/13/2002</td>\n",
       "      <td>6.5</td>\n",
       "      <td>2002</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1642</th>\n",
       "      <td>tt0360201</td>\n",
       "      <td>31000000</td>\n",
       "      <td>41512007</td>\n",
       "      <td>Wimbledon</td>\n",
       "      <td>Kirsten Dunst|Paul Bettany|Sam Neill|James McA...</td>\n",
       "      <td>Richard Loncraine</td>\n",
       "      <td>She's the golden girl. He's the longshot. It's...</td>\n",
       "      <td>A pro tennis player has lost his ambition and ...</td>\n",
       "      <td>98</td>\n",
       "      <td>Comedy|Romance</td>\n",
       "      <td>Universal Pictures</td>\n",
       "      <td>9/13/2004</td>\n",
       "      <td>5.7</td>\n",
       "      <td>2004</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1793</th>\n",
       "      <td>tt0770772</td>\n",
       "      <td>11000000</td>\n",
       "      <td>13196245</td>\n",
       "      <td>I Think I Love My Wife</td>\n",
       "      <td>Chris Rock|Kerry Washington|Gina Torres|Steve ...</td>\n",
       "      <td>Chris Rock</td>\n",
       "      <td>In marriage no one can hear you scream.</td>\n",
       "      <td>Richard Cooper (Rock) is a married man and fat...</td>\n",
       "      <td>90</td>\n",
       "      <td>Comedy|Romance</td>\n",
       "      <td>Fox Searchlight Pictures</td>\n",
       "      <td>3/16/2007</td>\n",
       "      <td>5.3</td>\n",
       "      <td>2007</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>841</th>\n",
       "      <td>tt1596346</td>\n",
       "      <td>18000000</td>\n",
       "      <td>47088990</td>\n",
       "      <td>Soul Surfer</td>\n",
       "      <td>AnnaSophia Robb|Helen Hunt|Lorraine Nicholson|...</td>\n",
       "      <td>Sean McNamara</td>\n",
       "      <td>When you come back from a loss, beat the odds,...</td>\n",
       "      <td>Soul Surfer is the inspiring true story of tee...</td>\n",
       "      <td>106</td>\n",
       "      <td>Action|Drama</td>\n",
       "      <td>Mandalay Pictures|TriStar Pictures|Brookwell-M...</td>\n",
       "      <td>4/8/2011</td>\n",
       "      <td>6.9</td>\n",
       "      <td>2011</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1284</th>\n",
       "      <td>tt1747958</td>\n",
       "      <td>25500000</td>\n",
       "      <td>2415472</td>\n",
       "      <td>Blood Ties</td>\n",
       "      <td>Clive Owen|Billy Crudup|Marion Cotillard|Mila ...</td>\n",
       "      <td>Guillaume Canet</td>\n",
       "      <td>Crime runs in the family.</td>\n",
       "      <td>Two brothers, on either side of the law, face ...</td>\n",
       "      <td>128</td>\n",
       "      <td>Thriller|Crime|Drama</td>\n",
       "      <td>Wild Bunch|LGM Productions|Les Productions du ...</td>\n",
       "      <td>8/22/2013</td>\n",
       "      <td>5.8</td>\n",
       "      <td>2013</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        imdb_id    budget   revenue          original_title  \\\n",
       "955   tt0280760   9000000   4777465          Igby Goes Down   \n",
       "1642  tt0360201  31000000  41512007               Wimbledon   \n",
       "1793  tt0770772  11000000  13196245  I Think I Love My Wife   \n",
       "841   tt1596346  18000000  47088990             Soul Surfer   \n",
       "1284  tt1747958  25500000   2415472              Blood Ties   \n",
       "\n",
       "                                                   cast           director  \\\n",
       "955   Kieran Culkin|Claire Danes|Jeff Goldblum|Jared...        Burr Steers   \n",
       "1642  Kirsten Dunst|Paul Bettany|Sam Neill|James McA...  Richard Loncraine   \n",
       "1793  Chris Rock|Kerry Washington|Gina Torres|Steve ...         Chris Rock   \n",
       "841   AnnaSophia Robb|Helen Hunt|Lorraine Nicholson|...      Sean McNamara   \n",
       "1284  Clive Owen|Billy Crudup|Marion Cotillard|Mila ...    Guillaume Canet   \n",
       "\n",
       "                                                tagline  \\\n",
       "955                               Insanity is relative.   \n",
       "1642  She's the golden girl. He's the longshot. It's...   \n",
       "1793            In marriage no one can hear you scream.   \n",
       "841   When you come back from a loss, beat the odds,...   \n",
       "1284                          Crime runs in the family.   \n",
       "\n",
       "                                               overview  runtime  \\\n",
       "955   A young man's peculiar upbringing renders him ...       97   \n",
       "1642  A pro tennis player has lost his ambition and ...       98   \n",
       "1793  Richard Cooper (Rock) is a married man and fat...       90   \n",
       "841   Soul Surfer is the inspiring true story of tee...      106   \n",
       "1284  Two brothers, on either side of the law, face ...      128   \n",
       "\n",
       "                    genres                               production_companies  \\\n",
       "955           Comedy|Drama                                     United Artists   \n",
       "1642        Comedy|Romance                                 Universal Pictures   \n",
       "1793        Comedy|Romance                           Fox Searchlight Pictures   \n",
       "841           Action|Drama  Mandalay Pictures|TriStar Pictures|Brookwell-M...   \n",
       "1284  Thriller|Crime|Drama  Wild Bunch|LGM Productions|Les Productions du ...   \n",
       "\n",
       "     release_date  vote_average  release_year  \n",
       "955     9/13/2002           6.5          2002  \n",
       "1642    9/13/2004           5.7          2004  \n",
       "1793    3/16/2007           5.3          2007  \n",
       "841      4/8/2011           6.9          2011  \n",
       "1284    8/22/2013           5.8          2013  "
      ]
     },
     "execution_count": 172,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.read_csv('movie_bd_v5.csv')\n",
    "data.sample(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "CoYUnagMVp-C"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>runtime</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1.889000e+03</td>\n",
       "      <td>1.889000e+03</td>\n",
       "      <td>1889.000000</td>\n",
       "      <td>1889.000000</td>\n",
       "      <td>1889.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>5.431083e+07</td>\n",
       "      <td>1.553653e+08</td>\n",
       "      <td>109.658549</td>\n",
       "      <td>6.140762</td>\n",
       "      <td>2007.860773</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>4.858721e+07</td>\n",
       "      <td>2.146698e+08</td>\n",
       "      <td>18.017041</td>\n",
       "      <td>0.764763</td>\n",
       "      <td>4.468841</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>5.000000e+06</td>\n",
       "      <td>2.033165e+06</td>\n",
       "      <td>63.000000</td>\n",
       "      <td>3.300000</td>\n",
       "      <td>2000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.000000e+07</td>\n",
       "      <td>3.456058e+07</td>\n",
       "      <td>97.000000</td>\n",
       "      <td>5.600000</td>\n",
       "      <td>2004.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.800000e+07</td>\n",
       "      <td>8.361541e+07</td>\n",
       "      <td>107.000000</td>\n",
       "      <td>6.100000</td>\n",
       "      <td>2008.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>7.200000e+07</td>\n",
       "      <td>1.782626e+08</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>6.600000</td>\n",
       "      <td>2012.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>3.800000e+08</td>\n",
       "      <td>2.781506e+09</td>\n",
       "      <td>214.000000</td>\n",
       "      <td>8.100000</td>\n",
       "      <td>2015.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             budget       revenue      runtime  vote_average  release_year\n",
       "count  1.889000e+03  1.889000e+03  1889.000000   1889.000000   1889.000000\n",
       "mean   5.431083e+07  1.553653e+08   109.658549      6.140762   2007.860773\n",
       "std    4.858721e+07  2.146698e+08    18.017041      0.764763      4.468841\n",
       "min    5.000000e+06  2.033165e+06    63.000000      3.300000   2000.000000\n",
       "25%    2.000000e+07  3.456058e+07    97.000000      5.600000   2004.000000\n",
       "50%    3.800000e+07  8.361541e+07   107.000000      6.100000   2008.000000\n",
       "75%    7.200000e+07  1.782626e+08   120.000000      6.600000   2012.000000\n",
       "max    3.800000e+08  2.781506e+09   214.000000      8.100000   2015.000000"
      ]
     },
     "execution_count": 173,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1889 entries, 0 to 1888\n",
      "Data columns (total 14 columns):\n",
      " #   Column                Non-Null Count  Dtype  \n",
      "---  ------                --------------  -----  \n",
      " 0   imdb_id               1889 non-null   object \n",
      " 1   budget                1889 non-null   int64  \n",
      " 2   revenue               1889 non-null   int64  \n",
      " 3   original_title        1889 non-null   object \n",
      " 4   cast                  1889 non-null   object \n",
      " 5   director              1889 non-null   object \n",
      " 6   tagline               1889 non-null   object \n",
      " 7   overview              1889 non-null   object \n",
      " 8   runtime               1889 non-null   int64  \n",
      " 9   genres                1889 non-null   object \n",
      " 10  production_companies  1889 non-null   object \n",
      " 11  release_date          1889 non-null   object \n",
      " 12  vote_average          1889 non-null   float64\n",
      " 13  release_year          1889 non-null   int64  \n",
      "dtypes: float64(1), int64(4), object(9)\n",
      "memory usage: 206.7+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "DTIt7ezGVp-G"
   },
   "source": [
    "# Предобработка"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "jNb40DwKVp-H"
   },
   "outputs": [],
   "source": [
    "answers = {} # создадим словарь для ответов\n",
    "\n",
    "# тут другие ваши предобработки колонок например:\n",
    "\n",
    "#the time given in the dataset is in string format.\n",
    "#So we need to change this in datetime format\n",
    "# ...\n",
    "data['release_date'] = pd.to_datetime(data['release_date'])\n",
    "data['profit'] = data['revenue'] - data['budget']\n",
    "\n",
    "def frequent_genre(df):\n",
    "    c = Counter()\n",
    "    for i in range(len(df)):\n",
    "        for j in df.iloc[i].genres.split('|'):\n",
    "            c[j] += 1\n",
    "    return c.most_common(1)\n",
    "\n",
    "def profit_genre(df):\n",
    "    c = Counter()\n",
    "    for i in range(len(df)):\n",
    "        for y in df.iloc[i].genres.split('|'):\n",
    "            c[y] += 1\n",
    "    return c.most_common(1)\n",
    "\n",
    "def director_revenue(df):\n",
    "    c = Counter()\n",
    "    for i in range(len(df)):\n",
    "        for j in df.loc[i].director.split('|'):\n",
    "            c[j] += df.loc[i].revenue\n",
    "    return c.most_common(1)\n",
    "\n",
    "def director_action(df):\n",
    "    c = Counter()\n",
    "    for i in range(len(df)):\n",
    "        for j in df.iloc[i].director.split('|'):\n",
    "            if 'Action' in df.iloc[i].genres:\n",
    "                c[j] += 1\n",
    "    return c.most_common(1)\n",
    "\n",
    "def actors_revenue_2012(df):\n",
    "    c = Counter()\n",
    "    for i in range(len(df)):\n",
    "        for j in df.iloc[i].cast.split('|'):\n",
    "            c[j] += df.iloc[i].revenue\n",
    "    return c.most_common(1)\n",
    "\n",
    "def high_value_actor(df):\n",
    "    c = Counter()\n",
    "    for i in range(len(df)):\n",
    "        for j in df.iloc[i].cast.split('|'):\n",
    "            c[j] += 1\n",
    "    return c.most_common(1)\n",
    "\n",
    "def nc_genre(df):\n",
    "    c = Counter()\n",
    "    for i in range(len(data)):\n",
    "        for j in data.iloc[i].genres.split('|'):\n",
    "            if 'Nicolas Cage' in data.iloc[i].cast:\n",
    "                c[j] +=1\n",
    "    return c.most_common(1)\n",
    "\n",
    "def profit_year(df):\n",
    "    c = Counter()\n",
    "    for x in df.release_year.unique():\n",
    "        c[x] = data[data.release_year == x].revenue.sum()\n",
    "    return c.most_common(1)\n",
    "\n",
    "def longest_title_studio(df):\n",
    "    lenth = Counter()\n",
    "    amount = Counter()\n",
    "    for x in range(len(df)):\n",
    "        for y in df.iloc[x].production_companies.split('|'):\n",
    "            lenth[y] += len(data.iloc[x].original_title)\n",
    "            amount[y] +=1\n",
    "    for x in lenth.keys():\n",
    "        lenth[x] = lenth[x] / amount[x]\n",
    "    return lenth.most_common(1)\n",
    "\n",
    "def more_words_studio(df):\n",
    "    lenth = Counter()\n",
    "    amount = Counter()\n",
    "    for x in range(len(data)):\n",
    "        for y in df.iloc[x].production_companies.split('|'):\n",
    "            lenth[y] += len(df.iloc[x].overview)\n",
    "            amount[y] +=1\n",
    "    for x in lenth.keys():\n",
    "        lenth[x] = lenth[x] / amount[x]\n",
    "    return lenth.most_common(1)\n",
    "\n",
    "def best_percent_movies(df):\n",
    "    best_movies = []\n",
    "    for x in range(int(len(df) * 0.01 //1)):\n",
    "        best_movies.append(data.sort_values(by='vote_average', ascending = False).original_title.iloc[x])\n",
    "    return best_movies"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "YxZaH-nPVp-L"
   },
   "source": [
    "# 1. У какого фильма из списка самый большой бюджет?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "Nd-G5gX6Vp-M"
   },
   "source": [
    "Использовать варианты ответов в коде решения запрещено.    \n",
    "Вы думаете и в жизни у вас будут варианты ответов?)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "uVnXAY5RVp-O"
   },
   "outputs": [],
   "source": [
    "# в словарь вставляем номер вопроса и ваш ответ на него\n",
    "# Пример: \n",
    "answers['1'] = '2. Spider-Man 3 (tt0413300)'\n",
    "# запишите свой вариант ответа\n",
    "answers['1'] = 'Pirates of the Caribbean: On Stranger Tides'\n",
    "# если ответили верно, можете добавить комментарий со значком \"+\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "dZwb3m28Vp-S"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "723    Pirates of the Caribbean: On Stranger Tides\n",
       "Name: original_title, dtype: object"
      ]
     },
     "execution_count": 177,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# тут пишем ваш код для решения данного вопроса:\n",
    "data[data.budget == data.budget.max()].original_title"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "K7L3nbRXVp-X"
   },
   "source": [
    "ВАРИАНТ 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "OGaoQI7rVp-X"
   },
   "outputs": [],
   "source": [
    "# можно добавлять разные варианты решения"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "FNRbbI3vVp-c"
   },
   "source": [
    "# 2. Какой из фильмов самый длительный (в минутах)?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "vHAoEXNTVp-d"
   },
   "outputs": [],
   "source": [
    "# думаю логику работы с этим словарем вы уже поняли, \n",
    "# по этому не буду больше его дублировать\n",
    "answers['2'] = 'Gods and Generals'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "ot-VX2XrVp-g"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1157    Gods and Generals\n",
       "Name: original_title, dtype: object"
      ]
     },
     "execution_count": 180,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data.runtime == data.runtime.max()].original_title"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "bapLlpW8Vp-k"
   },
   "source": [
    "# 3. Какой из фильмов самый короткий (в минутах)?\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "YBxaSHuAVp-l"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "768    Winnie the Pooh\n",
       "Name: original_title, dtype: object"
      ]
     },
     "execution_count": 181,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data['runtime'] == data['runtime'].min()].original_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['3'] = 'Winnie the Pooh'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "TfQbxbfNVp-p"
   },
   "source": [
    "# 4. Какова средняя длительность фильмов?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "5K6dKZYVVp-q"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "109.6585494970884"
      ]
     },
     "execution_count": 183,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.runtime.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['4'] = 110"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "r5TvbnT_Vp-u"
   },
   "source": [
    "# 5. Каково медианное значение длительности фильмов? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "iBROplKnVp-v"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "107.0"
      ]
     },
     "execution_count": 185,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.runtime.median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['5'] = 107"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "39P-deDSVp-y"
   },
   "source": [
    "# 6. Какой самый прибыльный фильм?\n",
    "#### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "239    Avatar\n",
       "Name: original_title, dtype: object"
      ]
     },
     "execution_count": 187,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data['profit'] == data['profit'].max()].original_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['6'] = 'Avatar'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "M99JmIX4Vp-2"
   },
   "source": [
    "# 7. Какой фильм самый убыточный? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "w-D2m4XPVp-3"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1245    The Lone Ranger\n",
       "Name: original_title, dtype: object"
      ]
     },
     "execution_count": 189,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data['profit'] == data['profit'].min()].original_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['7'] = 'The Lone Ranger'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "wEOM5ERVVp-6"
   },
   "source": [
    "# 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "y00_7HD6Vp-7"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1478"
      ]
     },
     "execution_count": 191,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(data[data.revenue > data.budget])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['8'] = 1478"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "xhpspA9KVp_A"
   },
   "source": [
    "# 9. Какой фильм оказался самым кассовым в 2008 году?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "MoUyQr9RVp_B"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The Dark Knight'"
      ]
     },
     "execution_count": 193,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[(data.release_year == 2008)].sort_values(by='revenue', ascending = False).original_title.iloc[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['9'] = 'The Dark Knight'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "Zi4hDKidVp_F"
   },
   "source": [
    "# 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "XqyRmufJVp_F"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The Lone Ranger'"
      ]
     },
     "execution_count": 195,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[(data.release_year >= 2012) & (data.release_year <= 2014)].sort_values(by='profit').original_title.iloc[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['10'] = 'The Lone Ranger'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "EA7Sa9dkVp_I"
   },
   "source": [
    "# 11. Какого жанра фильмов больше всего?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "zsJAwJ8QVp_J"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Drama', 782)]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# эту задачу тоже можно решать разными подходами, попробуй реализовать разные варианты\n",
    "# если будешь добавлять функцию - выноси ее в предобработку что в начале\n",
    "display(frequent_genre(data))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['11'] = 'Drama'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "Ax6g2C8SVp_M"
   },
   "source": [
    "ВАРИАНТ 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "otO3SbrSVp_N"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "T9_bPWpkVp_Q"
   },
   "source": [
    "# 12. Фильмы какого жанра чаще всего становятся прибыльными? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 199,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "Tmt8MaK1Vp_R"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Drama', 782)]"
      ]
     },
     "execution_count": 199,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "profit_genre(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['12'] = 'Drama'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "0F23bgsDVp_U"
   },
   "source": [
    "# 13. У какого режиссера самые большие суммарные кассовые сбооры?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "K6Z3J8ygVp_X"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Peter Jackson', 6490593685)]"
      ]
     },
     "execution_count": 201,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "director_revenue(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['13'] = 'Peter Jackson'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "PsYC9FgRVp_a"
   },
   "source": [
    "# 14. Какой режисер снял больше всего фильмов в стиле Action?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "wd2M-wHeVp_b"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Robert Rodriguez', 9)]"
      ]
     },
     "execution_count": 203,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "director_action(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['14'] = 'Robert Rodriguez'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "PQ0KciD7Vp_f"
   },
   "source": [
    "# 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "aga62oeKVp_g"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Chris Hemsworth', 2027450773)]"
      ]
     },
     "execution_count": 205,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "actors_revenue_2012(data[data.release_year == 2012])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['15'] = 'Chris Hemsworth'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "mWHyyL7QVp_j"
   },
   "source": [
    "# 16. Какой актер снялся в большем количестве высокобюджетных фильмов?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "qQtmHKTFVp_k"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Matt Damon', 18)]"
      ]
     },
     "execution_count": 207,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "high_value_actor(data[data.budget > data.budget.mean()])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['16'] = 'Matt Damon'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "NIh6AaW5Vp_n"
   },
   "source": [
    "# 17. В фильмах какого жанра больше всего снимался Nicolas Cage? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "H74SJDIBVp_n"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Action', 17)]"
      ]
     },
     "execution_count": 209,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nc_genre(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['17'] = 'Action'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "RqOmPRfWVp_q"
   },
   "source": [
    "# 18. Самый убыточный фильм от Paramount Pictures"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "9E_B0Y96Vp_r"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'K-19: The Widowmaker'"
      ]
     },
     "execution_count": 211,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data.production_companies.str.contains('Paramount Pictures')].sort_values(by='profit').original_title.iloc[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['18'] = 'K-19: The Widowmaker'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "vS8Ur6ddVp_u"
   },
   "source": [
    "# 19. Какой год стал самым успешным по суммарным кассовым сборам?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "Dnbt4GdIVp_v"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(2015, 25449202382)]"
      ]
     },
     "execution_count": 213,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "profit_year(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['19'] = '2015'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "JAzJh4QAVp_z"
   },
   "source": [
    "# 20. Какой самый прибыльный год для студии Warner Bros?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "wgVu02DEVp_0"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(2014, 3243064519)]"
      ]
     },
     "execution_count": 215,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c = Counter()\n",
    "for x in data.release_year.unique():\n",
    "    c[x] = data[(data.release_year == x) & (data.production_companies.str.contains('Warner Bros'))].revenue.sum()\n",
    "c.most_common(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['20'] = '2014'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "8Im1S2HRVp_4"
   },
   "source": [
    "# 21. В каком месяце за все годы суммарно вышло больше всего фильмов?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "lev6TH7gVp_4"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(2014, 3243064519)]"
      ]
     },
     "execution_count": 217,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "months = Counter()\n",
    "for x in range(len(data)):\n",
    "    months[data.iloc[x].release_date.month] +=1\n",
    "c.most_common(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['21'] = 'Сентябрь'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "uAJsZ_NeVp_7"
   },
   "source": [
    "# 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "Aa-hEREoVp_8"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "450"
      ]
     },
     "execution_count": 219,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "months[6]+months[7]+months[8]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 220,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['22'] = 450"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "G94ppOY1VqAA"
   },
   "source": [
    "# 23. Для какого режиссера зима – самое продуктивное время года? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Peter Jackson', 7)]"
      ]
     },
     "execution_count": 221,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c = Counter()\n",
    "for x in range(len(data)):\n",
    "    if data.iloc[x].release_date.month == 12 or data.iloc[x].release_date.month == 1 or data.iloc[x].release_date.month == 2:\n",
    "        c[data.iloc[x].director] += 1\n",
    "c.most_common(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 222,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['23'] = 'Peter Jackson'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "RBo0JVjVVqAF"
   },
   "source": [
    "# 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 223,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Four By Two Productions', 83.0)]"
      ]
     },
     "execution_count": 223,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "longest_title_studio(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['24'] = 'Four By Two Productions'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "9G0hbvR7VqAK"
   },
   "source": [
    "# 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 225,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "Ge2GsLNxVqAK"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Midnight Picture Show', 1000.0)]"
      ]
     },
     "execution_count": 225,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "more_words_studio(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 226,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['25'] = 'Midnight Picture Show'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "FJ1AFt90VqAP"
   },
   "source": [
    "# 26. Какие фильмы входят в 1 процент лучших по рейтингу? \n",
    "по vote_average"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "8qmJVq4CVqAQ"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['The Dark Knight',\n",
       " 'Interstellar',\n",
       " 'The Imitation Game',\n",
       " 'Inside Out',\n",
       " 'Room',\n",
       " 'The Wolf of Wall Street',\n",
       " 'Gone Girl',\n",
       " '12 Years a Slave',\n",
       " 'Guardians of the Galaxy',\n",
       " 'The Lord of the Rings: The Return of the King',\n",
       " 'Memento',\n",
       " 'Inception',\n",
       " 'The Pianist',\n",
       " 'The Grand Budapest Hotel',\n",
       " 'Her',\n",
       " 'Spotlight',\n",
       " 'Big Hero 6',\n",
       " 'The Fault in Our Stars']"
      ]
     },
     "execution_count": 227,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "best_percent_movies(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 228,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['26'] = ['Inside Out', 'The Dark Knight', '12 Years a Slave']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "MdXsUXbCVqAV"
   },
   "source": [
    "# 27. Какие актеры чаще всего снимаются в одном фильме вместе?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 229,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Daniel Radcliffe Emma Watson     8\n",
       "Daniel Radcliffe Rupert Grint    8\n",
       "Rupert Grint Emma Watson         7\n",
       "Name: actor_combinations, dtype: int64"
      ]
     },
     "execution_count": 229,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from itertools import combinations\n",
    "actor_list = data.cast.str.split('|').tolist()\n",
    "combo_list=[]\n",
    "for i in actor_list:\n",
    "    for j in combinations(i, 2):\n",
    "        combo_list.append(' '.join(j))\n",
    "combo_list = pd.DataFrame(combo_list)\n",
    "combo_list.columns = ['actor_combinations']\n",
    "combo_list.actor_combinations.value_counts().head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 230,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['27'] = 'Daniel Radcliffe Emma Watson'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "U0nONFnGVqAX"
   },
   "source": [
    "# Submission"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 231,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "IfcaRO9-VqAX",
    "outputId": "0f132912-32bb-4196-c98c-abfbc4ad5a5f"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'1': 'Pirates of the Caribbean: On Stranger Tides',\n",
       " '2': 'Gods and Generals',\n",
       " '3': 'Winnie the Pooh',\n",
       " '4': 110,\n",
       " '5': 107,\n",
       " '6': 'Avatar',\n",
       " '7': 'The Lone Ranger',\n",
       " '8': 1478,\n",
       " '9': 'The Dark Knight',\n",
       " '10': 'The Lone Ranger',\n",
       " '11': 'Drama',\n",
       " '12': 'Drama',\n",
       " '13': 'Peter Jackson',\n",
       " '14': 'Robert Rodriguez',\n",
       " '15': 'Chris Hemsworth',\n",
       " '16': 'Matt Damon',\n",
       " '17': 'Action',\n",
       " '18': 'K-19: The Widowmaker',\n",
       " '19': '2015',\n",
       " '20': '2014',\n",
       " '21': 'Сентябрь',\n",
       " '22': 450,\n",
       " '23': 'Peter Jackson',\n",
       " '24': 'Four By Two Productions',\n",
       " '25': 'Midnight Picture Show',\n",
       " '26': ['Inside Out', 'The Dark Knight', '12 Years a Slave'],\n",
       " '27': 'Daniel Radcliffe Emma Watson'}"
      ]
     },
     "execution_count": 231,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# в конце можно посмотреть свои ответы к каждому вопросу\n",
    "answers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "SiRmHPl8VqAd"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27"
      ]
     },
     "execution_count": 232,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# и убедиться что ни чего не пропустил)\n",
    "len(answers)"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "name": "Copy of [SF-DST] Movies IMBD v4.1 TEMPLATE.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
