import pandas as pd
import numpy as np
import time


def filter_time():
    """
    Ask user to choose the year or stage of the Worldcup competition

    Returns:
    years(int) - The year from which the championchip was held
    stage(str) - The chosen stage in the competition (Groups, semi-finals, finals ...)
    """
    while True:
        try:
            yeart = int(input("Enter the year of any WC or enter zero (0) the select all: "))
            years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 0]
            if yeart not in years:
                print("You've entered an unknown year, try angain")
                continue
            break
        except:
            print("Opps ):\nThis is not a valid recommanded date")
    
    while True:
        try:
            stage = input("Enter any competion stage of your choice or type 'all' to get all the stages at once: ")
            stages = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G', 'Group H', 'Preliminary round', 'First round',
            'Round 16', 'Quarter-finals', 'Semi-finals', 'Play-off for third place', 'Final', 'all']
            if stage not in stages:
                print("Your entered stage is not recognized, try a better one: ")
                continue
            break
        except:
            print("OPPS ) :>\nThis is not a valid record")

    print("*"*100)
    print()
    return yeart, stage


def load_datas(yeart, stage):
    """
    Load data from a specific FIFA Worldcup year, or filter a tournment in a specific Stage
    
    Args:
    year(int) - A Specific Worldcup year / all years
    stage(str) - A filted competition stage (fina, Quater-finas, ...)
    """
    df = pd.read_csv('datasets/WorldCupMatches.csv')
    df = df.iloc[:, :11]
    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df['year'] = pd.DatetimeIndex(df['Datetime']).year
    if yeart != 0:
        years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014]
        #yeart = years.index(yeart) + 1
        df = df[df['year'] == yeart]
    
    #df['Stage'] = pd.Strindex(df['Stage'])
    if stage != 'all':
        stages = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G', 'Group H', 'Preliminary round', 'First round', 'Round 16', 'Quarter-finals', 'Semi-finals', 'Play-off for third place', 'Final']
        #stage = stages.index(stage) + 1
        df = df[df['Stage'] == stage]
    
    return df

def rw_data(df):
    """
    Display the first 5 row of the data
    Args:
    df - This is the pandas data frame variable name that we have
    choice - this is a yes or no based on our decision 
    """
    choice = str(input("Would you like to display the raw data 'yes' or 'no': ").lower())
    while True:
        if choice == 'yes':
            print(df.head(5))
            break
        else:
            print("Thank you!")
            break
print("*"*100)
print("\n")

def score_stat(df):
    """Display the statiscs of goal score in competition"""
    h_score_home = df['H.Team Goals'].max() 
    h_score_away = df['A.Team Goals'].max()
    for  highest in h_score_home, h_score_away:
        if h_score_home > h_score_away:
            highest == h_score_home
        elif h_score_home < h_score_away:
            highest = h_score_away
        else:
            higest = h_score_away
    print("\n\nThe highest score is {} goals".format(highest))
    print("\nThe highest goal score in home team is {} goals and away team is {} goals".format(h_score_home, h_score_away))
    
    print("*"*100)
    print("\n")
def main():
    while True:
        yeart, stage = filter_time()
        df = load_datas(yeart, stage)

        rw_data(df)
        score_stat(df)

        restart = input("Would you like to restart? 'yes' or 'no'= ")
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

