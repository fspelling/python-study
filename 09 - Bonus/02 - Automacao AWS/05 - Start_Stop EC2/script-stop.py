import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    for region in regions:
        print("Region:", region)

        ec2 = boto3.resource('ec2', region_name=region)
        
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}]
        )

        for instance in instances:
            instance.start()
            print('Started instance: ', instance.id)