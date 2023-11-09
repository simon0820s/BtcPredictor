from utils.analyze import graph
from utils.model import useModel
import argparse

def main():
  print("====init====")
  
  #Arguments
  parser = argparse.ArgumentParser(description='main script')
  parser.add_argument('do', choices=['graph', 'useModel'], help='function to use')
  
  args = parser.parse_args()
  
  if args.do == 'graph':
    graph()
    
  if args.do == 'useModel':
    useModel()

if __name__ == '__main__':
  main()