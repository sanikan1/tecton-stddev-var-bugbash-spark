from tecton import FeatureService
from transactions import user_transaction_stddev_var

fraud_detection_feature_service = FeatureService(
    name='fraud_detection_feature_service',
    features=[
        user_transaction_stddev_var
    ]
)
