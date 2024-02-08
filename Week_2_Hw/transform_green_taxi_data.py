if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    # Counting Rows with 0 passengers
    print(f"Rows with out 0 passengers: {data['passenger_count'].fillna(0).isin([0]).sum()}")
    
    #Counting rows where trip distance <= 0
    print(f"Rows with trip distance <= 0: {data['trip_distance'].le(0).sum()}")
    

    #Creating the only date column from datetime
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # Apply both conditions to filter the data
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # Assuming 'data' is your DataFrame with columns in camel case
    data.columns = (data.columns
                .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                .str.lower()
             )




    return  data



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0,'There are rides with zero passengers'
    assert output['trip_distance'].le(0).sum() == 0, 'There are rides with non-positive trip distances'
    
    
    # Check if 'vendor_id' is not null
    assert output['vendor_id'].notnull().all(), 'There are null values in vendor_id'
    # Check if 'vendor_id' contains only integer values
    assert 'vendor_id' in output.columns, 'vendor_id column is missing in the DataFrame'
