
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display_html
from itertools import chain,cycle


# Print all dataframe function
def print_all_dataframe(rows, columns):

    """
    Set the number of rows and columns printed of pandas dataframe when executing print (dataframe).
    :param rows: longitude of first place
    :param columns: longitude of second place
    """
    
    if columns == False or rows == False:
        pd.reset_option('all')
    if columns == True:
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None) 
    if rows == True:
        pd.set_option('display.max_rows', None)
        
        
# Print more than one dataframe in the same line
def display_side_by_side(*args, titles=cycle([''])):

    """
    Print multiple pandas dataframes in the same line.
    :param args: pandas dataframes to print.
    :param titles: titles to print above the pandas dataframes (optional).
    """
    
    html_str=''
    for df,title in zip(args, chain(titles,cycle(['</br>'])) ):
        html_str+='<th style="text-align:center"><td style="vertical-align:top">'
        html_str+=f'<h2 style="text-align: center;">{title}</h2>'
        html_str+=df.to_html().replace('table','table style="display:inline"')
        html_str+='</td></th>'
    display_html(html_str,raw=True)        
        
        
# Descriptive statistics
def sdescribe (df, column, decimals):

    """
    Calculate the descriptive statistics of a numeric variable in a pandas dataframe. Note that kurtosis follows Pearson's definition (normal ==> 3.0).
    :param df: a pandas dataframe containing the data.
    :param column: the name of the column containing the quantitative data.
    :param decimals: the number of decimals to print.   
    :return: descriptive statistics of the variable, including count, mean, standard deviation (std), minimum (min), P25%, P50%, P75%, maximum (max), skewness (skew), and kurtosis (kurt).
    """
   
    d1= df.describe()[[column]]
    d2= pd.DataFrame(data={column:[skew(df[column], nan_policy='omit'), kurtosis(df[column], nan_policy='omit', fisher=False)]}, index=['skew', 'kurt'])
    d= pd.concat([d1,d2], axis=0).transpose()
    return round(d, decimals)
    
    
# Frequency tables with absolute and relative frequencies

def freqtab (df, column, decimals):

    """
    Calculate the descriptive statistics of a qualitative variable in a pandas dataframe.
    :param df: a pandas dataframe containing the data.
    :param column: the name of the column containing the qualitative data.
    :param decimals: the number of decimals to print.   
    :return: frequency table of a qualitative variable, including total count and percentage.
    """
    
    df2= df.copy()
    
    if str(df2[column].dtypes) == 'category':
        df2[column]= df2[column].cat.add_categories('NA')
        table= pd.crosstab(index=df2[column].fillna('NA'), columns='count', dropna=False)
    elif str(df2[column].dtypes) != 'category':
        table= pd.crosstab(index=df2[column].fillna('NA'), columns='count', dropna=False)

    table.rename(columns={'count':'count (n)'}, inplace=True)
    table['percentage (%)']= [float(round((value/sum(table['count (n)'].values.tolist())*100),decimals)) for value in table['count (n)'].values.tolist()]
    total= pd.DataFrame(data=[[sum(table['count (n)'].values.tolist()), sum(table['percentage (%)'].values.tolist())]], columns=table.columns.to_list(), index=['TOTAL'])
    table= pd.concat([table,total], axis=0)
    table= table.rename_axis(column, axis=1)

    return table
    
    
# Barplots and boxplots with NA values

def plot(df, x_axis, axis, kind, hue=None):

    """
    Plotting barplots and boxplots of qualitative variables in a pandas dataframe including NAs.
    :param df: a pandas dataframe containing the data.
    :param x_axis: the name of the column containing the data to plot.
    :param axis: axis of a matplotlib subplots figure where the figure is going to be plotted.
    :param kind: the kind of plot, including 'bars' or 'box'
    :param hue: a variable to divide the graph distribution. Default None.
    :return: the plot.
    """
    
    df2= df.copy()
    
    if str(df2[x_axis].dtypes) == 'category':
        df2[x_axis]= df2[x_axis].cat.add_categories('NA').fillna('NA')
    elif str(df2[x_axis].dtypes) != 'category':
        values= []
        for value in df2[x_axis].tolist():
            if np.isnan(value):
                value= 'NA'
            elif ~np.isnan(value):
                try:
                    value= str(int(value))
                except:
                    value=value
            values.append(value)  
        df2[x_axis]= values

    if kind == 'bars':
        if str(df2[x_axis].dtypes) == 'category':
            sns.countplot(data=df2, x=x_axis, hue=hue, ax=axis)
        elif str(df2[x_axis].dtypes) != 'category':
            order= np.unique(values).tolist()
            if 'NA' in order:
                order.remove('NA')
                order.sort(key=int)
                order.append('NA')
            elif 'NA' not in order:
                order.sort(key=int)
            sns.countplot(data=df2, x=x_axis, hue=hue, order=order, ax=axis)
    elif kind == 'box':
        sns.boxplot(data=df2, x=x_axis, y=hue, color='#77DD77', ax=axis)
		
