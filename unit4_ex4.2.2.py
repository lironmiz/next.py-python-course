# exercise 4.2.2 from unit 4
'''
Write a function called parse_ranges defined like this:

def parse_ranges(ranges_string):
The function accepts as a parameter a string called ranges_string that represents ranges of numbers, and returns a generator that produces all the numbers in these ranges.

An example of running the parse_ranges function:

print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))
[1, 2, 4, 8, 9, 10]
[0, 4, 5, 6, 7, 8, 20, 21, 43, 44, 45]
Pay attention in the example to how the string of number ranges is written: a number indicating the beginning of a range, a dash, a number indicating the end of a range, a comma, and so on).

Guidelines:

Realize the generator using a generator expression.
You can divide the task into two separate operations by implementing two generators. Write the solution using the generator piping process.
First hint
It is actually a pipeline of generators consisting of two generators, each of which is responsible for a different operation:
The first generator in the chain is responsible for processing the string passed as input, and producing for us each time a data structure whose members each represent two members that are a range of numbers.

First hint
It is actually a pipeline of generators consisting of two generators, each of which is responsible for a different operation:
The first generator in the chain is responsible for processing the string passed as input, and producing for us each time a data structure whose members each represent two members that are a range of numbers.

For example, for the string "1-2,4-4,8-10", the generator will produce:
In the first iteration ['2' ,'1']
In the second iteration ['4' ,'4']
In the third iteration ['10','8']
Note, we chose to use a list, but you can use any data structure you want.
The second generator will use the values produced by the first generator as its input and will return each time all the numbers in the range.


Second hint
For the second generator, you can use the following basic code template, and convert it to a generator:
for start, stop in first_generator:
     for num in range(int(start), int(stop)+1):
     
'''

def parse_ranges(ranges_string):
    def get_ranges():
        for range_str in ranges_string.split(','):
            start, stop = range_str.split('-')
            yield int(start), int(stop)
            
    def generate_numbers():
        for start, stop in get_ranges():
            for num in range(start, stop+1):
                yield num

    return generate_numbers()

print(list(parse_ranges("1-2,4-4,8-10")))

print(list(parse_ranges("0-0,4-8,20-21,43-45")))
