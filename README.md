# Booking.com_hackerrank
#Problem 1 : packNumbers
Given an array of integers, pack neighbouring numbers that are the same as below:

For example, this

packNumbers([9, 9, 1, 5, 5, 5, 9])
should return

["9:2", 1, "5:3", 9]



# Problem 2 :
You and a friend are at one of the tallest hotels in the world. In the elevator up from the lobby, you notice that the sequence of floor numbers is , , , , , , , , , , , , , and so on. After a while, you realize that the hotel's floor numbering is lucky: no floors contain the numbers  or . This means there are no , , , or  floors; however, there are  and  floors.

The hotel wants to build a second tower without going through the hassle of numbering floors manually. Can you come up with an algorithm that, when given a "real" (i.e., non-lucky or sequential) floor number, will return the corresponding floor number associated with the lucky numbering system (i.e., not containing any 's or 's)?

Complete the processData function in your editor. It has one parameter: an integer, , denoting a "real" floor number. It must convert  to a lucky floor number and print the converted number.

Input Format

Stub code in the editor below reads a real floor number, , from stdin and passes it to the processData function.

Constraints

Output Format

Using the console.log command, print the lucky floor number.

Sample Input

12
Sample Output

15
Explanation

Given , we need to find the corresponding lucky floor number. The following chart shows the first twelve real and lucky floor numbers:

Real:   1  2  3  4  5  6  7  8  9  10  11  12
Lucky:  1  2  3  5  6  7  8  9  10 11  12  15
Because  is the twelfth lucky floor number, we print  on a new line.
