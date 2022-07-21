from tecton import batch_feature_view, FilteredSource, Aggregation
from entities import user
from demo_data import demo_data_batch
from datetime import datetime, timedelta

@batch_feature_view(
    sources=[FilteredSource(demo_data_batch)],
    entities=[user],
    mode='spark_sql',
    aggregation_interval=timedelta(days=1),
    aggregations=[
        Aggregation(column='transaction', function='var_samp', time_window=timedelta(days=1)),
        Aggregation(column='transaction', function='var_pop', time_window=timedelta(days=1)),
        Aggregation(column='transaction', function='stddev_samp', time_window=timedelta(days=1)),
        Aggregation(column='transaction', function='stddev_pop', time_window=timedelta(days=1)),
    ],
    online=True,
    offline=True,
    feature_start_time=datetime(2022, 5, 1),
    tags={'release': 'production'},
    owner='matt@tecton.ai',
    description='User transaction variance and standard deviation over a time window, updated daily.'
)
def user_last_transaction_stddev_var(transactions):
    return f'''
        SELECT
            user_id,
            transaction,
            timestamp
        FROM
            {transactions}
        '''
