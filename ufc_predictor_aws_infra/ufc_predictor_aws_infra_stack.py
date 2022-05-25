from unicodedata import name
from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
    RemovalPolicy,
    aws_iam as iam,
    aws_ec2 as ec2,
    aws_rds as rds,
)


class UfcPredictorAwsInfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "ufc-predictor-vpc", cidr='10.0.0.0/16',
                      max_azs=3,
                      subnet_configuration=[ec2.SubnetConfiguration(
                          subnet_type=ec2.SubnetType.PUBLIC,
                          name="UfcPredictorPublicSubnet"
                      )])

        sg = ec2.SecurityGroup(
            self, "ufc-predictor-rds-SG", vpc=vpc)

        sg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(3306))

        db = rds.DatabaseInstance(self, 'ufcfightpredictortest', vpc=vpc,
                                  vpc_subnets=ec2.SubnetSelection(
                                      subnet_type=ec2.SubnetType.PUBLIC
                                  ),
                                  engine=rds.DatabaseInstanceEngine.mysql(
                                      version=rds.MysqlEngineVersion.VER_8_0_19),
                                  instance_type=ec2.InstanceType.of(
                                      ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
                                  credentials=rds.Credentials.from_generated_secret(
                                      "mysqlAdmin"),
                                  multi_az=False,
                                  allocated_storage=100,
                                  max_allocated_storage=105,
                                  allow_major_version_upgrade=False,
                                  auto_minor_version_upgrade=True,
                                  backup_retention=Duration.days(0),
                                  delete_automated_backups=True,
                                  removal_policy=RemovalPolicy.DESTROY,
                                  deletion_protection=False,
                                  database_name="thisisatest",
                                  publicly_accessible=True,
                                  security_groups=[sg])

        CfnOutput(self, 'TestDBEndpoint',
                  value=db.instance_endpoint.hostname)

        CfnOutput(self, 'test-secret', value=db.secret.secret_name)
