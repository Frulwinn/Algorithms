#!/usr/bin/python

import argparse

#set prices in list
prices = [50, 100, 20, 80]

def find_max_profit(prices):
  #get current index

  #loop through the list
  
  #subtract current index from next element to find max profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))