region = "us-east-1"

terraform_lambda= {
    name = "Override_Name"
    runtime = "python3.9"
    handler = "override.lambda_handler"
}



#this is taken as refference from below githublink and below medium link
#https://github.com/batuhan-bulut/terraform-aws-lambda/blob/main/terraform/terraform.tfvars
#https://bulutbatuhan.medium.com/how-to-deploy-lambda-function-on-aws-using-terraform-16f7f1fa930f

#Refer this link if you have any other doubts for clratification for creating lambda fucntion using terraform
#https://medium.com/@sutrapusharan/automating-aws-lambda-function-deployment-with-terraform-a-step-by-step-guide-19dfe64663c2
