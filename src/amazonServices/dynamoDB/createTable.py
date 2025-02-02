import boto3
import sys

def check_args():
    if len(sys.argv) == 2:
        return 1
    else:
        return 0

def create_table(tableName):
    DDB = boto3.resource('dynamodb', region_name='AWS_REGION')
    params = {
        'TableName': str(tableName),
        'KeySchema': [
            {'AttributeName': 'course_name', 'KeyType': 'HASH'}
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'course_name', 'AttributeType': 'S'}
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    }
    table = DDB.create_table(**params)
    table.wait_until_exists()
    print ("Done")

if __name__ == '__main__':
    #checks that the correct argument is given when file is run
    if check_args() and "-courses" in sys.argv[1]:
        tableName = sys.argv[1]
        create_table(tableName)
    else:
        print("Usage: python3 createTable.py <name-courses>")
        exit()
    
