def processData(input):
    if input == 1:
       print('1')
       return
    lucky = 1;
    # Starting the counter with 2
    count = 2
    # Expecting to loop twice the input to get definite results.
    while ( count <= 2*input):
        # Convert the number to str to find the index
        temp = str(count)
        if temp.find("4") == -1 and temp.find("13") == -1:
            lucky = lucky + 1
        if lucky == input:
            print(count)
            return
        count = count + 1
if __name__ == "__main__":
   # Given input example is 15, you can modify to rewrite to any input or raw_input
    processData(15)
