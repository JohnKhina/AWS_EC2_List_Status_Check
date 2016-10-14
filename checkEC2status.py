import boto3

session = boto3.Session(profile_name='default')
ec2 = session.resource('ec2', region_name='ap-southeast-2')
d = ec2.meta.client.describe_instance_status()['InstanceStatuses']


def check_ec2():
    instanceList = {}
    for instance in d:
        for k, v in instance.items():
            instanceList.update(instance)
        instanceStatus = instanceList['SystemStatus']
        if instanceStatus['Status'] == 'ok':
            print('Instance: {} is ok'.format(instanceList['InstanceId']))
        elif instanceStatus['Status'] == 'impaired':
            print('Instance: {} is impaired'.format(instanceList['InstanceId']))
        elif instanceStatus['Status'] == 'initializing':
            print('Instance: {} is initializing'.format(instanceList['InstanceId']))
        elif instanceStatus['Status'] == 'insufficient-data':
            print('Instance: {} is insufficient-data'.format(instanceList['InstanceId']))
        elif instanceStatus['Status'] == 'not-applicable':
            print('Instance: {} is not-applicable'.format(instanceList['InstanceId']))


if __name__ == "__main__":
    check_ec2()
