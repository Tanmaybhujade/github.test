{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np \n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns \n",
    "from ipywidgets import interact\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the shape of the data set  (2200, 8)\n"
     ]
    }
   ],
   "source": [
    "print (\"the shape of the data set \", data.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled":true
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
       "      <th>N</th>\n",
       "      <th>P</th>\n",
       "      <th>K</th>\n",
       "      <th>temperature</th>\n",
       "      <th>humidity</th>\n",
       "      <th>ph</th>\n",
       "      <th>rainfall</th>\n",
       "      <th>label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>90</td>\n",
       "      <td>42</td>\n",
       "      <td>43</td>\n",
       "      <td>20.879744</td>\n",
       "      <td>82.002744</td>\n",
       "      <td>6.502985</td>\n",
       "      <td>202.935536</td>\n",
       "      <td>rice</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>85</td>\n",
       "      <td>58</td>\n",
       "      <td>41</td>\n",
       "      <td>21.770462</td>\n",
       "      <td>80.319644</td>\n",
       "      <td>7.038096</td>\n",
       "      <td>226.655537</td>\n",
       "      <td>rice</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>60</td>\n",
       "      <td>55</td>\n",
       "      <td>44</td>\n",
       "      <td>23.004459</td>\n",
       "      <td>82.320763</td>\n",
       "      <td>7.840207</td>\n",
       "      <td>263.964248</td>\n",
       "      <td>rice</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>74</td>\n",
       "      <td>35</td>\n",
       "      <td>40</td>\n",
       "      <td>26.491096</td>\n",
       "      <td>80.158363</td>\n",
       "      <td>6.980401</td>\n",
       "      <td>242.864034</td>\n",
       "      <td>rice</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>78</td>\n",
       "      <td>42</td>\n",
       "      <td>42</td>\n",
       "      <td>20.130175</td>\n",
       "      <td>81.604873</td>\n",
       "      <td>7.628473</td>\n",
       "      <td>262.717340</td>\n",
       "      <td>rice</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    N   P   K  temperature   humidity        ph    rainfall label\n",
       "0  90  42  43    20.879744  82.002744  6.502985  202.935536  rice\n",
       "1  85  58  41    21.770462  80.319644  7.038096  226.655537  rice\n",
       "2  60  55  44    23.004459  82.320763  7.840207  263.964248  rice\n",
       "3  74  35  40    26.491096  80.158363  6.980401  242.864034  rice\n",
       "4  78  42  42    20.130175  81.604873  7.628473  262.717340  rice"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "N              0\n",
       "P              0\n",
       "K              0\n",
       "temperature    0\n",
       "humidity       0\n",
       "ph             0\n",
       "rainfall       0\n",
       "label          0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "mothbeans      100\n",
       "muskmelon      100\n",
       "papaya         100\n",
       "lentil         100\n",
       "coconut        100\n",
       "apple          100\n",
       "watermelon     100\n",
       "chickpea       100\n",
       "coffee         100\n",
       "orange         100\n",
       "mungbean       100\n",
       "kidneybeans    100\n",
       "maize          100\n",
       "mango          100\n",
       "jute           100\n",
       "banana         100\n",
       "grapes         100\n",
       "rice           100\n",
       "cotton         100\n",
       "pomegranate    100\n",
       "pigeonpeas     100\n",
       "blackgram      100\n",
       "Name: label, dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#now lets check the cross present in the dataset \n",
    "data['label'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'data' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-22-e4fc246900ba>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Average ratio of the nitrogen in the soil:{0:.2f}\"\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'N'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmean\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Average ratio of the phosphorous in the soil:{0:.2f}\"\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'P'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmean\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Average ratio of the potassium in the soil:{0:.2f}\"\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'K'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmean\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Average temperature in celsius:{0:.2f}\"\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'temperature'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmean\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Average relative humidity in % :{0:.2f}\"\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'humidity'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmean\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'data' is not defined"
     ]
    }
   ],
   "source": [
    "print(\"Average ratio of the nitrogen in the soil:{0:.2f}\".format(data['N'].mean()))\n",
    "print(\"Average ratio of the phosphorous in the soil:{0:.2f}\".format(data['P'].mean()))\n",
    "print(\"Average ratio of the potassium in the soil:{0:.2f}\".format(data['K'].mean()))\n",
    "print(\"Average temperature in celsius:{0:.2f}\".format(data['temperature'].mean()))\n",
    "print(\"Average relative humidity in % :{0:.2f}\".format(data['humidity'].mean()))\n",
    "print(\"Average ph value of the soil  :{0:.2f}\".format(data['ph'].mean()))\n",
    "print(\"Average rainfall in mm :{0:.2f}\".format(data['rainfall'].mean()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8156c4f9c49d413cb195a8e78dc9c772",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "interactive(children=(Dropdown(description='crops', options=('mothbeans', 'muskmelon', 'papaya', 'lentil', 'co…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ".....................................\n",
      "Statistics for Nitrogen\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'x' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-22-9e58687341e4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Statistics for Nitrogen\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 11\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Minimum Nitrigen required :\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'N'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     12\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Average Nitrogen required :\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'N'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmean\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'x' is not defined"
     ]
    }
   ],
   "source": [
    "#statistics for each crop\n",
    "@interact\n",
    "\n",
    "def summary(crops =list (data[ 'label'].value_counts().index)):\n",
    "    x = data[data['label'] == crops]\n",
    "\n",
    "print(\".....................................\")\n",
    "\n",
    "print(\"Statistics for Nitrogen\")\n",
    "\n",
    "print(\"Minimum Nitrigen required :\", x['N'].min())\n",
    "\n",
    "print(\"Average Nitrogen required :\", x['N'].mean())\n",
    "\n",
    "print(\"Maximum Nitrogen required :\", x['N'].max())\n",
    "print(\".........................\")\n",
    "\n",
    "\n",
    "print(\"Statistics for Phosphorous\")\n",
    "\n",
    "\n",
    "print(\"Minimum Phosphorous required :\", x['P'].min())\n",
    "\n",
    "print(\"Average Phosphorous required :\", x['P'].mean()) \n",
    "print(\"Maximum Phosphorous required \", x['P'].max())\n",
    "\n",
    "print(\"Statistics for Potassium\")\n",
    "\n",
    "print(\"Minimum Potassium required :\", x['K'].min())\n",
    "\n",
    "print(\"Average Potassium required :\", x['K'].mean())\n",
    "print(\"Maximum Potassium required :\", x['K'].max())\n",
    "\n",
    "print(\"............................\")\n",
    "\n",
    "print(\"Statistics for Temperature\")\n",
    "\n",
    "\n",
    "\n",
    "print(\"Minimum Temperature required: (0:.2f)\". format (x['temperature'].min()))\n",
    "print(\"Average Temperature required: (0:.2f)\". format (x['temperature'].mean())) \n",
    "print(\"Maximum Temperature required: (0:.2f}\" .format(x['temperature'].max()))\n",
    "print(\"...................................\")\n",
    "print(\"Statistics for Humidity\")\n",
    "\n",
    "print(\"Minimun Humidity required: (0:2)\".format (x['humidity'].min())) \n",
    "print(\"Average Humidity required (8.2f)\".format(x['humidity'].mean()))\n",
    "\n",
    "print(\"Maximum Humidity required: (0.2f)\".format(x['humidity'].max()))\n",
    "\n",
    "print(\"------------\")\n",
    "print(\"Statistics for PH\")\n",
    "\n",
    "print(\"Minimun PH required (8.2f)\". format(x['ph'].min())) \n",
    "print(\"Average PH required (0:2)\" .format(x[ 'ph'].mean()))\n",
    "\n",
    "print(\"Maximun PH required (8.2f)\" .format(x[ 'ph'].max()))\n",
    "\n",
    "print(\"Statistics for Reinfall\")\n",
    "\n",
    "print(\"Minimum Rainfall required (0.2f) \".format(x['rainfall' ].min()))\n",
    "print(\"Average Rainfall required (0.2f)\".format(x['rainfall' ].mean()))\n",
    "\n",
    "print(\"Maximum Rainfall required (0:2)\".format(x['rainfall' ].max()))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "42d5096f0479479d8bdecded8a9b94ac",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "interactive(children=(Dropdown(description='condition', options=('N', 'P', 'K', 'Temprature', 'ph', 'humidity'…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Lets compare the Average Requirement for each crops with average  conditions\n",
    "\n",
    "@interact\n",
    "def compare(condition =['N','P','K','Temprature','ph','humidity','rainfall']):\n",
    "    print(\"Avrage Value for\", conditions, \"is{0:.2f}\".format(data[conditions].mean()))\n",
    "    print(\"-------------------------------------------\")\n",
    "    print(\"Rice : {0:.2f}\".format(data[data['label'] == 'rice'][conditions].mean()))\n",
    "    print(\"Black Grams : {0:.2f}\".format(data[data['label'] == 'blackgram'][conditions].mean()))\n",
    "    print(\"Banana : {0:.2f}\".format(data[data['label'] == 'banana'][conditions].mean()))\n",
    "    print(\"jute : {0:.2f}\".format(data[data['label'] == 'jute'][conditions].mean()))\n",
    "    print(\"Cocount : {0:.2f}\".format(data[data['label'] == 'coconut'][conditions].mean()))\n",
    "    print(\"Apple : {0:.2f}\".format(data[data['label'] == 'apple'][conditions].mean()))\n",
    "    print(\"papaya : {0:.2f}\".format(data[data['label'] == 'papaya'][conditions].mean()))\n",
    "    print(\"Muskmelon : {0:.2f}\".format(data[data['label'] == 'muskmelon'][conditions].mean()))\n",
    "    print(\"Graps : {0:.2f}\".format(data[data['label'] == 'graps'][conditions].mean()))\n",
    "    print(\"Watermelon : {0:.2f}\".format(data[data['label'] == 'watermelon'][conditions].mean()))\n",
    "    print(\"Kidney Beans : {0:.2f}\".format(data[data['label'] == 'kidneybeans'][conditions].mean()))\n",
    "    print(\"Mung Beans : {0:.2f}\".format(data[data['label'] == 'mungbean'][conditions].mean()))\n",
    "    print(\"Oranges : {0:.2f}\".format(data[data['label'] == 'oranges'][conditions].mean()))\n",
    "    print(\"Chick peas : {0:.2f}\".format(data[data['label'] == 'chickpeas'][conditions].mean()))\n",
    "    print(\"Lentils : {0:.2f}\".format(data[data['label'] == 'lentils'][conditions].mean()))\n",
    "    print(\"Cotton : {0:.2f}\".format(data[data['label'] == 'cotton'][conditions].mean()))\n",
    "    print(\"Maize : {0:.2f}\".format(data[data['label'] == 'Maize'][conditions].mean()))\n",
    "    print(\"Moth Beans : {0:.2f}\".format(data[data['label'] == 'mothbeans'][conditions].mean()))\n",
    "    print(\"Pigeon peas : {0:.2f}\".format(data[data['label'] == 'pigeonpeas'][conditions].mean()))\n",
    "    print(\"Mango : {0:.2f}\".format(data[data['label'] == 'mango'][conditions].mean()))\n",
    "    print(\"pomegranates : {0:.2f}\".format(data[data['label'] == 'pomegranate'][conditions].mean()))\n",
    "    print(\"Coffee : {0:.2f}\".format(data[data['label'] == 'coffee'][conditions].mean()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "cd546de57f3c496db08572f74fe8ee85",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "interactive(children=(Dropdown(description='conditions', options=('N', 'P', 'k', ' temprature', 'ph', 'humidit…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# lets makes this functions more Intutive\n",
    "\n",
    "\n",
    "@interact\n",
    "def compare(conditions = ['N','P','k',' temprature','ph','humidity','rainfall']):\n",
    "    print(\"crpos which require grater than average\", conditions)\n",
    "    print(data[data[conditions]> data[conditional].mean()]['label'].unique())\n",
    "    print(\"--------------------------------------------------\")\n",
    "    print(\"crops which require less than average\",condition,'\\n')\n",
    "    print(data[data[conditions]<= data[conditions].mean()]['lebel'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Some Interesting Patterns\n",
      "-------------------------\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'data' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-c517ec8452ac>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Some Interesting Patterns\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"-------------------------\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Crops which require very high ratio of Nitrogen content in soil:\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'N'\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m>\u001b[0m \u001b[1;36m120\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'label'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0munique\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Crops which require very high ratio of Phosphorous content in soil:\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'P'\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m>\u001b[0m \u001b[1;36m100\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'label'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0munique\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Crops which require very high ratio of Potassium content in soil:\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'K'\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m>\u001b[0m \u001b[1;36m200\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'label'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0munique\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'data' is not defined"
     ]
    }
   ],
   "source": [
    "#lets find out some interesting facts\n",
    "print(\"Some Interesting Patterns\")\n",
    "print(\"-------------------------\")\n",
    "print(\"Crops which require very high ratio of Nitrogen content in soil:\",data[data['N'] > 120]['label'].unique())\n",
    "print(\"Crops which require very high ratio of Phosphorous content in soil:\",data[data['P'] > 100]['label'].unique())\n",
    "print(\"Crops which require very high ratio of Potassium content in soil:\",data[data['K'] > 200]['label'].unique())\n",
    "print(\"Crops which require very high Rainfall:\",data[data['rainfall'] > 200]['label'].unique())\n",
    "print(\"Crops which require very low Temperature:\",data[data['temperature'] < 10]['label'].unique())\n",
    "print(\"Crops which require very high Temperature:\",data[data['temperature'] > 40]['label'].unique())\n",
    "print(\"Crops which require very low Humidity:\",data[data['humidity'] < 20]['label'].unique())\n",
    "print(\"Crops which require very low pH:\",data[data['ph'] < 4]['label'].unique())\n",
    "print(\"Crops which require very high pH:\",data[data['ph'] > 9]['label'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'data' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-6-8f49fd196042>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msubplot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0msns\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhistplot\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'K'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mcolor\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'darkblue'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mxlabel\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Ratio of Potassium'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mfontsize\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgrid\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'data' is not defined"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.subplot(2,4,3)\n",
    "sns.histplot (data['K'],color='darkblue')\n",
    "plt.xlabel('Ratio of Potassium',fontsize=12)\n",
    "plt.grid()\n",
    "\n",
    "plt.subplot(2,4,4)\n",
    "sns.histplot (data['temperature'],color='black')\n",
    "plt.xlabel('Temperature',fontsize=12)\n",
    "plt.grid()\n",
    "\n",
    "plt.subplot(2,4,5)\n",
    "sns.histplot(data['rainfall'],color='grey')\n",
    "plt.xlabel('Rainfall',fontsize=12)\n",
    "plt.grid()\n",
    "\n",
    "plt.subplot(2,4,6)\n",
    "sns.histplot(data['humidity'],color='lightgreen')\n",
    "plt.xlabel('humidity',fontsize=12)\n",
    "plt.grid()\n",
    "\n",
    "plt.subplot(2,4,7)\n",
    "sns.histplot(data['ph'],color='darkgreen')\n",
    "plt.xlabel('pH Level',fontsize=12)\n",
    "plt.grid()\n",
    "\n",
    "plt.suptitle('Distribution for agricultural conditions',fontsize = 20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Summer Crops\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'data' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-7-af9091eab701>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Summer Crops\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'temperature'\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m>\u001b[0m\u001b[1;36m30\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m&\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'humidity'\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m>\u001b[0m \u001b[1;36m50\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'label'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0munique\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"----------------------------------\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Winter Crops\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'data' is not defined"
     ]
    }
   ],
   "source": [
    "### Lets understand which crops can only be grown in Summer Season, Winter Season and Rainy Season\n",
    "\n",
    "print(\"Summer Crops\")\n",
    "print(data[(data['temperature'] >30) & (data['humidity'] > 50)]['label'].unique())\n",
    "print(\"----------------------------------\")\n",
    "print(\"Winter Crops\")\n",
    "print(data[(data['temperature'] <20) & (data['humidity'] > 30)]['label'].unique())\n",
    "print(\"----------------------------------\")\n",
    "print(\"Rainy Crops\")\n",
    "print(data[(data['temperature'] >200) & (data['humidity'] > 30)]['label'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'data' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-8-b53dd0dd0227>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m# removing the labels column\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[0mx\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdrop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'label'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;31m# selecting all the values of the data\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'data' is not defined"
     ]
    }
   ],
   "source": [
    "from sklearn.cluster import KMeans\n",
    "\n",
    "# removing the labels column\n",
    "x = data.drop(['label'], axis=1)\n",
    "\n",
    "# selecting all the values of the data\n",
    "x=x.values\n",
    "\n",
    "# checking the shape\n",
    "print(x.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'x' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-9-5686f93b5046>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m11\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m     \u001b[0mkm\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mKMeans\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn_clusters\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mi\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0minit\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'k-means++'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmax_iter\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m300\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mn_init\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m10\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrandom_state\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m     \u001b[0mkm\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      9\u001b[0m     \u001b[0mwcss\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkm\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0minertia_\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'x' is not defined"
     ]
    }
   ],
   "source": [
    "# Lets determine the Optimum Number of Clusters within the Dataset\n",
    "\n",
    "plt.rcParams['figure.figsize'] = (10,4)\n",
    "\n",
    "wcss = []\n",
    "for i in range(1, 11):\n",
    "    km = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)\n",
    "    km.fit(x)\n",
    "    wcss.append(km.inertia_)\n",
    "    \n",
    "# Lets plot the Results\n",
    "plt.plot(range(1, 11), wcss)\n",
    "plt.title('The Elbow Method', fontsize = 20)\n",
    "plt.xlabel('No. of Clusters')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'x' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-13-b0d6cb9f0b6c>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Lets implement the K Means algorithm to perform Clustering analysis\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mkm\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mKMeans\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mn_clusters\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0minit\u001b[0m\u001b[1;33m=\u001b[0m \u001b[1;34m'k-means++'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmax_iter\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m300\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mn_init\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m18\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrandom_state\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0my_means\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mkm\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfit_predict\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;31m# Lets find out the Results\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'x' is not defined"
     ]
    }
   ],
   "source": [
    "# Lets implement the K Means algorithm to perform Clustering analysis\n",
    "km = KMeans (n_clusters = 4, init= 'k-means++', max_iter = 300, n_init = 18, random_state = 0)\n",
    "y_means = km.fit_predict(x)\n",
    "\n",
    "# Lets find out the Results\n",
    "\n",
    "a = data[ 'label']\n",
    "\n",
    "y_means= pd.DataFrame(y_means) \n",
    "z = pd.concat([y_means, a], axis = 1)\n",
    "\n",
    "z = z. rename (columns={0: 'cluster'})\n",
    "\n",
    "# Lets check the Clusters of each Crops\n",
    "\n",
    "print(\"Lets check the Results After Applying the K Means Clustering Analysis \\n\")\n",
    "print(\"Crops in First Cluster:\", z[z['cluster'] == 0]['label'].unique())\n",
    "\n",
    "print(\"---------------------------------------------------------------- \")\n",
    "print(\"Crops in Second Cluster:\", z[z['cluster'] == 1]['label'].unique())\n",
    "print(\"-----------------------------------------------------------------\")\n",
    "print(\"Crops in Third Cluster:\", z[z['cluster'] == 2]['label'].unique())\n",
    "print(\"------------------------------------------------------------------\")\n",
    "\n",
    "print(\"Crops in Forth Cluster:\", z[z['cluster'] == 3]['label' ].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'data' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-14-c72aadd5d129>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Lets split the Dataset for Predictive Modelling\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0my\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'label'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mx\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdrop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'label'\u001b[0m \u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0maxis\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'data' is not defined"
     ]
    }
   ],
   "source": [
    "# Lets split the Dataset for Predictive Modelling\n",
    "\n",
    "y = data['label']\n",
    "\n",
    "x = data.drop(['label' ], axis = 1)\n",
    "\n",
    "print(\"Shape of x:\", x.shape) \n",
    "print(\"Shape of y:\", y.shape)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'x' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-16-0f6566988517>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmodel_selection\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mtrain_test_split\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[0mx_train\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mx_test\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my_train\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my_test\u001b[0m \u001b[1;33m=\u001b[0m\u001b[0mtrain_test_split\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtest_size\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m8.2\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrandom_state\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"The Shape of x train:\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mx_train\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mshape\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'x' is not defined"
     ]
    }
   ],
   "source": [
    "# Lets create Training and Testing Sets for Validation of Results\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "x_train, x_test, y_train, y_test =train_test_split(x, y, test_size = 8.2, random_state = 0)\n",
    "\n",
    "print(\"The Shape of x train:\", x_train.shape)\n",
    "\n",
    "print(\"The Shape of x test:\", x_test. shape)\n",
    "\n",
    "print(\"The Shape of y train:\", y_train.shape)\n",
    "\n",
    "print(\"The Shape of y test: \", y_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'x_train' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-17-f5e185433a80>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mmodel\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mLogisticRegression\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m \u001b[0mmodel\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx_train\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my_train\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      8\u001b[0m \u001b[0my_pred\u001b[0m\u001b[1;33m=\u001b[0m \u001b[0mmodel\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpredict\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx_test\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'x_train' is not defined"
     ]
    }
   ],
   "source": [
    "# Lets create a Predictive Model\n",
    "\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "\n",
    "model = LogisticRegression()\n",
    "\n",
    "model.fit(x_train, y_train)\n",
    "y_pred= model.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'y_test' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-18-cbafc46702b0>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrcParams\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'figure.figsize'\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m10\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m \u001b[0mcm\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mconfusion_matrix\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my_test\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my_pred\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      8\u001b[0m \u001b[0msns\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mheatmap\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcm\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mannot\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcmap\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'Wistia'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtitle\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Confusion Matrix for Logistic Regression'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfontsize\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m15\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'y_test' is not defined"
     ]
    }
   ],
   "source": [
    "# Lets evaluate the Model Performance\n",
    "from sklearn.metrics import confusion_matrix\n",
    "\n",
    "# Lets print the Confusion matrix first\n",
    "\n",
    "plt.rcParams['figure.figsize'] = (10, 10) \n",
    "cm = confusion_matrix(y_test, y_pred) \n",
    "sns.heatmap(cm, annot = True, cmap = 'Wistia') \n",
    "plt.title('Confusion Matrix for Logistic Regression', fontsize = 15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'classification_report' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-19-c0fbd3c4f40e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Lets print the Classification Report also\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mcr\u001b[0m\u001b[1;33m=\u001b[0m \u001b[0mclassification_report\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0my_test\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my_pred\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'classification_report' is not defined"
     ]
    }
   ],
   "source": [
    "# Lets print the Classification Report also \n",
    "cr= classification_report (y_test, y_pred)\n",
    "print(cr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'data' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-20-304fa4ce4ebd>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdata\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhead\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'data' is not defined"
     ]
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-21-7e70fc34dd02>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-21-7e70fc34dd02>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    prediction model.predict((np.array([[90,\u001b[0m\n\u001b[1;37m               ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "prediction model.predict((np.array([[90,\n",
    "                                     40,\n",
    "                                     20,\n",
    "                                     80,\n",
    "                                     7,\n",
    "                                     200]])))\n",
    "\n",
    "print(\"The Suggested Crop for Given Climatic Condition is:\" prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}