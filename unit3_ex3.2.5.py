# exercise 3.2.5 from unit 3
 '''
 Write a function called read_file defined as follows:

def read_file(file_name):
The function accepts as a parameter a string representing the name of a file. If the file exists, the function reads its contents and returns a string representing the contents of the file wrapped in the following output:

An example of running the read_file function for an existing file:

print(read_file("one_lined_file.txt"))
__CONTENT_START__
This is the content from the file!
__CONTENT_END__
If the file does not exist, the function will return a string detailing it as follows.

An example of running the read_file function for a file that does not exist:

print(read_file("file_does_not_exist.txt"))
__CONTENT_START__
__NO_SUCH_FILE__
__CONTENT_END__
Guidelines:

For testing purposes, pass to the function as arguments:
File name that does not exist.
An existing file name with - place it in the folder from which you run the code.
Use: try, except, else, finally and open.
'''
  
  def read_file(file_name):
    try:
        with open(file_name) as f:
            content = f.read()
    except FileNotFoundError:
        content = "__NO_SUCH_FILE__"
    finally:
        return "__CONTENT_START__\n" + content + "\n__CONTENT_END__"

# Test the function with a file that does not exist
print(read_file("file_does_not_exist.txt"))

# Test the function with an existing file
print(read_file("one_lined_file.txt"))

  
  
