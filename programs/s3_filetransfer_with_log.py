import logging
import boto3
import os
import sys
import traceback

class aws_opertion:
    def __init__(self):
        self.logger = "aws_opertion"
        self.logger.setLevel(logging.DEBUG)

        self.format = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

        self.file_handler = logging.FileHandler("awsopertion.log")
        self.file_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(self.format)

        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(logging.DEBUG)
        self.stream_handler.setFormatter(self.format)

        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stream_handler)

        self.s3 = boto3.client("s3")
    @property
    def logger(self):
        return self._logger
    @logger.setter
    def logger(self,name):
        self._logger = logging.getLogger("aws_opertion")
    def add_file_s3(self,file_name,bucket,destination):
        if os.path.exists(file_name):
            logger.info("uploading file to s3")
            self.s3.upload_file(file_name,bucket,destination)
            logger.info("succefully uploaded file to se")
            return 1
        else:
            logger.error("path does't exist")
            raise Exception("file does't exist")

    def list_files(self,bucket,dir):
        logger.info(f"dir is {dir}")
        s3_fetched_file_names = []
        file_list = self.s3.list_objects(Bucket=bucket,Prefix=dir)['Contents'] if len(self.s3.list_objects(Bucket=bucket,Prefix=dir)['Contents'])>0 else []
        if len(file_list)>0:
            for s3_object in file_list:
                s3_fetched_file_names.append(s3_object['Key'])
            return s3_fetched_file_names
        else:
            logger.info("bucket is empty")
            return []
    def delete_file(self,file_name,bucket):
        try:
            flag = self.s3.delete_object(Bucket=bucket,Key=file_name)
            logger.info(f"sucefully deleted file {file_name}")
        except:
            raise Exception("exception during deleting file")
    def download_files(self,download_location,bucket,download_file):
        print(os.path.dirname(download_location))
        if not os.path.isdir(os.path.dirname(download_location)):
            os.mkdir(os.path.dirname(download_location))
        try:
            download_location = download_location + download_file.split('/')[-1]
            self.s3.download_file(Bucket = bucket,Filename = download_location,Key = download_file)
            logger.info("succefully downloaded the file")
        except :
            logger.exception(traceback.print_exc())


aws = aws_opertion()
logger = aws.logger


if __name__ == "__main__":
    logger.info("aws operation started")
    bucket = "dai-wiley-lake-data"
    download_location = "C:\\Users\\shankar.dengi\\Downloads\\PythonProjectGit\\programs\\"
    dir = 'stage/linkedin/t_s_linkedin_accounts/'
    while True:
        print("1)file upload to s3")
        print("2)list files from s3")
        print("3)delete files from s3")
        print("4)download files from s3")
        print("5)Exit")
        ch = int(input("\nEnter you choice:"))
        if ch == 1:
            logger.info("insert operation selected")
            try:
                aws.add_file_s3("test_file.txt",bucket,f"{dir}test_file.txt")
            except:
                logger.exception(traceback.print_exc())
        elif ch== 2:
            logger.info("listing files from bucket")
            files = aws.list_files(bucket,dir)
            logger.info(files)
        elif ch == 3:
            logger.info("deleting file from bucket")
            try:
                logger.info(aws.list_files(bucket,dir))
                file_name = input("\n\nEnter Filename to delte:")
                aws.delete_file(file_name,bucket)
            except:
                logger.exception(traceback.print_exc())
        elif ch ==4:
            logger.info(f"downloading files at :{download_location}")
            logger.info(aws.list_files(bucket,dir))
            download_file = input("Enter file name to download:")
            aws.download_files(download_location,bucket,download_file)
        elif ch==5:
            logger.info("Exiting from aws opertion")
            break
