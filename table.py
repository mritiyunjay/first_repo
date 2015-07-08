#!/usr/bin/python
class table:
	def print_table(self, input):
		for i in range(1, 11):
			print input*i

if __name__ == "__main__":
	#create table instance
	tb = table()
	tb.print_table(3)
			
