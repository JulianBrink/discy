import os
import pandas as pd

### rawdata preprocessing
def read_csv() -> pd.DataFrame:
    file = '../data/scorecards/UDisc Scorecards.csv'
    rawdata = pd.read_csv(file)
    return rawdata

def clear_custom(rawdata: pd.DataFrame) -> pd.DataFrame:
    return rawdata.loc[rawdata.loc[:,'LayoutName']!='Custom',:]

def clear_unfinished(rawdata: pd.DataFrame) -> pd.DataFrame:
    for i in range(6, rawdata.columns.size):
        #print(f"Zero Values on Hole {i-5}")
        #print(rawdata.loc[rawdata.loc[:,rawdata.columns[i]]==0,:])
        #print('*'*50)
        rawdata = rawdata.loc[rawdata.loc[:,rawdata.columns[i]]!=0,:]
    return rawdata

def clear_lowpar(rawdata: pd.DataFrame) -> pd.DataFrame:
    for i in range(6, rawdata.columns.size):
        matchme = rawdata.loc[(rawdata.iloc[:,0]=='Par')
                          &(rawdata.loc[:,rawdata.columns[i]]<3),:].iloc[:,[1,2,3]]
        if len(matchme.index) > 0:
            filter_ = rawdata.loc[((rawdata.iloc[:,1]==matchme.values[0][0])
                                    &(rawdata.iloc[:,2]==matchme.values[0][1])
                                    &(rawdata.iloc[:,3]==matchme.values[0][2])),:]

            rawdata.drop(index=filter_.index, inplace=True)
        else:
            continue
    return rawdata


### pardata branch
def create_pardata (rawdata: pd.DataFrame) -> pd.DataFrame:
    pardata = rawdata[rawdata['PlayerName'] == 'Par']

    old_new = pardata.groupby(by=list(pardata.columns[[1,2,4]])).agg(oldest=(pardata.columns[3],'min'),
                                                       newest=(pardata.columns[3],'max'))

    pardata.drop_duplicates(subset=[pardata.columns[1],
                                    pardata.columns[2],
                                    pardata.columns[4]], 
                            inplace=True, ignore_index=False)
    pardata = pardata.sort_values(by=list(pardata.columns[[1,2,4]])).drop(columns=pardata.columns[[0,3,5]])
    pardata.reset_index(inplace=True, drop=True)
    pardata.insert(loc=2, column='Oldest', value=pd.Series(old_new['oldest'].values))
    pardata.insert(loc=3, column='Newest', value=pd.Series(old_new['newest'].values))
    return pardata

def add_HoleCount(pardata: pd.DataFrame) -> pd.DataFrame:
    pardata.insert(loc=4, column='HoleCount', value=pardata.loc[:,pardata.columns[5:]].count(axis='columns'))
    return pardata

def clear_spaces(pardata: pd.DataFrame) -> pd.DataFrame:
    pardata.iloc[:,0] = pardata.iloc[:,0].apply(lambda x: x.strip())
    pardata.iloc[:,1] = pardata.iloc[:,1].apply(lambda x: x.strip())
    return pardata


### scoredata branch
def create_scoredata(rawdata: pd.DataFrame) -> pd.DataFrame:
    scoredata = rawdata[rawdata['PlayerName'] != 'Par']
    return scoredata

def add_Teamsize(scoredata: pd.DataFrame) -> pd.DataFrame:
    scoredata.insert(loc=4, column='TeamSize', value=scoredata['PlayerName'].apply(lambda x: len(x.split('+'))))
    scoredata.drop(columns='+/-', inplace=True)
    return scoredata




### bundled functions
def create_df_pardata():
    pardata =  clear_spaces(
        add_HoleCount(
            create_pardata(
                clear_lowpar(
                    clear_unfinished(
                        clear_custom(
                            read_csv()))))))
    return pardata

def create_df_scoredata():
    scoredata =  add_Teamsize(
            create_scoredata(
                clear_lowpar(
                    clear_unfinished(
                        clear_custom(
                            read_csv())))))
    return scoredata

def delete_csv():
    file = '../data/scorecards/UDisc Scorecards.csv'
    if os.path.exists(file):
        os.remove(file)








# =============================================================================
# 
#     #Löschen der erstellten Dataframes und Listen aus dem Zwischenspeicher
#     #Ob das sinnvoll ist ist fraglich ....
#     rawdata = None
#     scoredata = None
#     pardata = None
#     data = None
#     templist = None
#     teamsize = None
#     i = None
#     
# =============================================================================
# =============================================================================
#     #Löschen der csv Datei.
#     if os.path.exists(file):
#         os.remove(file)
#         # Print the statement once the file is deleted  
#         print("The file: {} is deleted!".format(file))
#     else:
#         print("The file: {} does not exist!".format(file))
#     file = None
# =============================================================================
