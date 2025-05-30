from datetime import datetime
import boto3


def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']] for region in ec2_client.describe_regions()['Regions']

    for region in regions:
        print(f'Instances in EC2 Region {region}:')

        ec2 = boto3.resource('ec2', region_name=region)

        instances = ec2.instances.filter(
            Filters=[
                {'Name': 'Backup', 'Values': ['True']}
            ]
        )

        timestamp = datetime.utcnow().replace(microsecond=0).isoformat()

        for i in instances.all():
            for v in i.volumes.all():
                desc_snapshoot = 'Backup of instance {i.id}, volume {v.id}, created {timestamp}'
                print(desc_snapshoot)

                snapshot = v.create_snapshot(Description=desc_snapshoot)
                print("Created snapshot:", snapshot.id)