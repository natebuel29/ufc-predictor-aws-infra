#!/usr/bin/env python3

import aws_cdk as cdk

from ufc_predictor_aws_infra.ufc_predictor_aws_infra_stack import UfcPredictorAwsInfraStack


app = cdk.App()
UfcPredictorAwsInfraStack(app, "ufc-predictor-aws-infra")

app.synth()
