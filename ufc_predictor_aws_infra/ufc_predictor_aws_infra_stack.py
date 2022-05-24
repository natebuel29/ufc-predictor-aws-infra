from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_ec2 as ec2,
)


class UfcPredictorAwsInfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self,"ufc-predictor-vpc")
        
        security_group = ec2.SecurityGroup(self,"ufc-predictor-rds-SG",vpc=vpc)
        
