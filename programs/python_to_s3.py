import boto3
import os


s3 = boto3.client("s3")
# lists = s3.list_objects(Bucket="dai-wiley-lake-data",Prefix ='stage/linkedin/t_s_linkedin_accounts/')
# dicts = lists['Contents']
# for i in dicts:
#     print(i)
# print(os.getcwd())
# s3.download_file(Filename = "C:\\Users\\shankar.dengi\\Downloads\\PythonProjectGit\\programs\\downloads_ssm.josn",Bucket = "dai-wiley-lake-data",Key = "/stage/linkedin/t_s_linkedin_accounts/Stream_Report_2021-05-19T1223_x4rw9Y.json")
temp = s3.delete_object(Bucket="dai-wiley-lake-data",Key="stage/linkedin/t_s_linkedin_accounts/test_file.txt")
print(temp)


#temp = s3.upload_file("test_file.txt","dai-wiley-lake-data","/stage/linkedin/t_s_linkedin_accounts/")
print(dir(s3))
#print(temp)
#strings = open("test_file.txt",'r')
#print(strings.read())

#s3.upload_file

