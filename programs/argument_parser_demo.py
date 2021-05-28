import  argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="testing")
    parser.add_argument('-s',"--test",default="Hello",help="enter hello",required=False)
    temp = parser.parse_args()
    print(parser)
    print(getattr(temp,'test'))