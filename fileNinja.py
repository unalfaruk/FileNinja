import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser(description="File Splitter/Joinner")
subparser = parser.add_subparsers(dest="operation")

parser_join = subparser.add_parser("join", help="To join files...")
parser_join.add_argument("input_directory", help="The directory path containing chunks")
parser_join.add_argument("output_file",help="The file (path) to be created by joining chunks (default = inside of input_directory )")

parser_split = subparser.add_parser("split", help="To split a file into chunks...")
parser_split.add_argument("input_file", help="The file (path) to split")
parser_split.add_argument("output_directory", help="The directory path to store chunks created (default = the path of input_file )")
parser_split.add_argument("chunk_size", type=int, default=10, help="Set chunk size (default = 10 Mb)")

def Split(inputFile=None,outputDir=None,chunk=10):

    if chunk == None:
        chunk = 10
    
    if outputDir == None:
        outputDir = inputFile+"_DIR"
        
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
        
    try:        
        with open(inputFile,"rb") as file:
            counter=0
            while 1:            
                part = file.read(1024*1024*int(chunk))
                
                if not part:
                    break
                
                with open (os.path.join(outputDir, str(counter)),"wb+") as io:
                    io.write(part)

                counter = counter + 1
                #print("Encoded successfully! The output file location is:",args.output)
            print("Splitted successfully!")
            return outputDir, counter
    except Exception as e:        
        print(e)
        return False
		
def Join(inputDir=None,outputFile=None):

    if outputFile == None or outputFile=="":
        outputFile = os.path.join(inputDir, Path(inputDir).name)
    
    try:
        with open(outputFile,"wb+") as io:
            counter=0
            while 1:
                tmpFileToRead = os.path.join(inputDir,str(counter))
                counter=counter+1;
                
                if not os.path.exists(tmpFileToRead):
                    break

                with open (tmpFileToRead,"rb") as file:
                    part = file.read()
                
                io.write(part)
                #print("Encoded successfully! The output file location is:",args.output)
        print("Joinned successfully!")
        return outputFile
    except Exception as e:
        print(e)
        return False
        
def main():
    #opening()
    if args.operation == "split":
        Split(args.input_file,args.output_directory,args.chunk_size)
    if args.operation == "join":
        Join(args.input_directory,args.output_file)
       
if __name__ == '__main__':
    args = parser.parse_args()
    main()