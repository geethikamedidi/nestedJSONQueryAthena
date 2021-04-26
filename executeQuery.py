import boto3
import time

athena = boto3.client('athena')

with open("query3.txt") as q:
    query = q.read()
    params = {
        'region': 'us-west-2',
        'database': 'nestedJsondb',
        'bucket': 'clis3',
        'path': 'output2/',
        'query': query
    }

    response_query_execution_id = athena.start_query_execution(QueryString=params['query'],
                                                               QueryExecutionContext={'Database': params['database']},
                                                               ResultConfiguration={
                                                                   'OutputLocation': 's3://' + params['bucket'] + '/' +
                                                                                     params[
                                                                                         'path']})
    query_execution_details = athena.get_query_execution(
        QueryExecutionId=response_query_execution_id['QueryExecutionId'])
    print("query_execution_details: " + str(query_execution_details))

    status = "RUNNING"
    maxIterations = 10
    while maxIterations > 0:
        maxIterations = maxIterations - 1
        query_execution_details = athena.get_query_execution(
            QueryExecutionId=response_query_execution_id['QueryExecutionId'])
        status = query_execution_details['QueryExecution']['Status']['State']
        print("Status of the query execution: " + status)
        if (status == 'FAILED') | (status == 'CANCELLED'):
            print("Status of the query execution: " + status)
        elif status == 'SUCCEEDED':
            location = query_execution_details['QueryExecution']['ResultConfiguration']['OutputLocation']
            print("location of the result of the query execution: " + location)
            response_query_result = athena.get_query_results(
                QueryExecutionId=response_query_execution_id['QueryExecutionId'])
            result_set = response_query_result['ResultSet']
            print("ResultSet----------" + str(result_set))
            print("Success!!!")
            exit()
        else:
            time.sleep(1)
