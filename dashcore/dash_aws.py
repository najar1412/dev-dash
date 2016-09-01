import boto3
from random import choice

"""Tools for spinning up a render manager and nodes on AWS"""

# TODO: Cleanup, test
# TODO: IMP tagging on new nodes.
# TODO: Figure out attaching/mapping render storage to nodes
# TODO: Test networking between manager and nodes.
# TODO: See how much control over windows server 2012 settings i have after
# creation... incase ip's etc need to be updated on manager stop/terminate
# TODO: How does aws know to make nodes on us-east-1b? The 'b' part hasnt been
# hardcoded anywhere?

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
availability_zone = 'us-east-1b'

def mk_manager(key='vh-rf-key', ami='ami-ab4024bc', secgroup=['sg-94c29def']):
    """make new instance
    key = str, public key name,
    ami = str, name of amazon machine image
    """
    # Helper - Number gen for node name
    num_list = [x for x in range(1, 9999)]
    num = choice(num_list)
    # Create Node, options
    node = ec2.create_instances(
        ImageId=ami,
        MinCount=1,
        MaxCount=1,
        KeyName=key,
        SecurityGroupIds=secgroup,
        InstanceType='t2.small',
        Placement={
            'AvailabilityZone': availability_zone
            }
        )
    # Add tags to new node.
    ec2.create_tags(
        Resources=[
            str(node[0].id),
        ],
        Tags=[
                {
                'Key': 'Name',
                'Value': 'vh_manager_{}'.format(num)
                },
            ]
        )


def mk_node(key='vh-rf-key', ami='ami-cf7e1ad8', secgroup=['sg-94c29def']):
    """make new instance
    key = str, public key name,
    ami = str, name of amazon machine image
    """
    # Helper - Number gen for node name
    num_list = [x for x in range(1, 9999)]
    num = choice(num_list)
    # Create Node, options
    node = ec2.create_instances(
        ImageId=ami,
        MinCount=1,
        MaxCount=1,
        KeyName=key,
        SecurityGroupIds=secgroup,
        InstanceType='m4.2xlarge',
        Placement={
            'AvailabilityZone': availability_zone
            }
    )
    # Add tags to new node.
    ec2.create_tags(
        Resources=[
            str(node[0].id),
        ],
        Tags=[
                {
                'Key': 'Name',
                'Value': 'node_{}'.format(num)
                },
            ]
        )


def list_instance():
    nodes = {}
    for x in ec2.instances.all():

        if x.tags is None:
            nodes['No Name'] = x
        else:
            nodes[x.tags[0]['Value']] = {
                'ids': x.id,
                'status': x.state['Name'],
                'pubip': x.public_ip_address,
                'pdns': x.public_dns_name
            }

    return nodes


def term_instance(instance):
    """AUG: Must be list
    """
    id_list = []
    if type(instance) == []:
        ec2.instances.filter(InstanceIds=instance).terminate()
    else:
        id_list.append(instance)
        ec2.instances.filter(InstanceIds=id_list).terminate()


def stop_instance(instance):
    """AUG: Must be list
    """
    id_list = []
    if type(instance) == type(list):
        ec2.instances.filter(InstanceIds=instance).stop()
    else:
        id_list.append(instance)
        ec2.instances.filter(InstanceIds=id_list).stop()

def start_instance(instance):
    """AUG: Must be list
    """
    id_list = []
    if type(instance) == type(list):
        ec2.instances.filter(InstanceIds=instance).start()
    else:
        id_list.append(instance)
        ec2.instances.filter(InstanceIds=id_list).start()
