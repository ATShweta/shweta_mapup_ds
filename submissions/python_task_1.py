######################Q1$$$$$$$$$$##########################
import pandas as pd

def generate_car_matrix():

    df = pd.read_csv('datasets/dataset-1.csv')


    car_matrix = df.pivot(index='id_1', columns='id_2', values='car')


    car_matrix = car_matrix.fillna(0)

    return car_matrix

# file_path = 'datasets/dataset-1.csv'
result_car_matrix = generate_car_matrix()

# print(result_car_matrix)










##################################################Question 2#######################################

import pandas as pd

def get_type_count():
    df = pd.read_csv('datasets\dataset-1.csv')
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')], labels=['low', 'medium', 'high'], right=False)
    type_count = df['car_type'].value_counts().to_dict()
    type_count = dict(sorted(type_count.items()))
    return type_count


# file_path = 'datasets\dataset-1.csv'
# result_type_count = get_type_count(file_path)
# print(result_type_count)

# ##################################################Question 3###########################################

import pandas as pd

def get_bus_indexes():
    df = pd.read_csv('datasets\dataset-1.csv')
    mean_bus = df['bus'].mean()
    bus_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()
    bus_indexes.sort()
    return bus_indexes


# file_path = 'datasets\dataset-1.csv'
# result_bus_indexes = get_bus_indexes(file_path)
# print(result_bus_indexes)

# ##################################################Question 4###########################################

import pandas as pd

def filter_routes():
    df = pd.read_csv('datasets\dataset-1.csv')
    route_avg_truck = df.groupby('route')['truck'].mean()
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    selected_routes.sort()
    return selected_routes


# file_path = 'datasets\dataset-1.csv'
# result_filtered_routes = filter_routes(file_path)
# print(result_filtered_routes)

# ##################################################Question 5###########################################


import pandas as pd

def multiply_matrix(result_car_matrix):
    modified_matrix = result_car_matrix.copy()
    modified_matrix = modified_matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    modified_matrix = modified_matrix.round(1)
    return modified_matrix



# modified_result = multiply_matrix(result_car_matrix)
# print(modified_result)

# ##################################################Question 6###########################################


import pandas as pd

def check_time_completeness(df):
    df['start_datetime'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end_datetime'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])
    df['duration'] = df['end_datetime'] - df['start_datetime']
    result_series = df.groupby(['id', 'id_2']).apply(
        lambda group: (
            group['duration'].min() < pd.Timedelta(days=1) and
            group['start_datetime'].min().time() == pd.Timestamp('00:00:00').time() and
            group['end_datetime'].max().time() == pd.Timestamp('23:59:59').time() and
            set(group['start_datetime'].dt.dayofweek.unique()) == set(range(7))
        )
    )

    return result_series


# df = pd.read_csv('datasets\dataset-2.csv')
# result = check_time_completeness(df)
# print(result)