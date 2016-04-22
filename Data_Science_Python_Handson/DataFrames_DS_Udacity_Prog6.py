__author__ = 'Anubhav'

import numpy
from pandas import DataFrame, Series
import pandas as pd


def numpy_dot():
    '''
    Imagine a point system in which each country is awarded 4 points for each
    gold medal,  2 points for each silver medal, and one point for each
    bronze medal.

    Using the numpy.dot function, create a new dataframe called
    'olympic_points_df' that includes:
        a) a column called 'country_name' with the country name
        b) a column called 'points' with the total number of points the country
           earned at the Sochi olympics.

    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    points_gold = [4]
    points_silver = [2]
    points_bronze = [1]
    odf = {'countries' : Series(countries),
           'gold' : Series(gold),
           'silver' : Series(silver),
           'bronze' : Series(bronze)}
    # YOUR CODE HERE
    print numpy.dot(numpy.array(gold),4)
    print numpy.dot(numpy.array(silver),2)
    print numpy.dot(numpy.array(bronze),1)
    df =  pd.DataFrame(odf)
    gold_points = [x*4 for x in gold]
    silver_points = [x*2 for x in silver]
    bronze_points = [x*1 for x in bronze]
    common_points = {'gold_p' : Series(gold_points),
                     'silver_p' : Series(silver_points),
                     'bronze_p' : Series(bronze_points)
                    }

   # print df['gold']*4 + df['silver']*2 + df['bronze']*1
    #print gold_points
    #print silver_points
    #print bronze_points

    cdf = pd.DataFrame(common_points)

    print cdf['bronze_p'][0]
    print cdf['gold_p'][0]
    print cdf['silver_p'][0]
    print cdf['bronze_p'][0], cdf['gold_p'][0],  cdf['silver_p'][0]

    final_frame = {
            'country_name' : Series(countries),
            'total_points' : Series(cdf['bronze_p'] + cdf['gold_p'] + cdf['silver_p'])
    }

    fdf = pd.DataFrame(final_frame)

    print fdf

numpy_dot()