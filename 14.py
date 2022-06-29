# Write a program to find how many times substring “Hi” appears in the given string.
def countSubstring(str1, str2):
     
    n1 = len(str1);
    n2 = len(str2);
     

    if (n1 == 0 or n1 < n2):
        return 0;
    if (str1[0 : n2] == str2):
        return countSubstring(str1[1:],
                             str2) + 1;
 

    return countSubstring(str1[1:],
                         str2);

if __name__ == '__main__':
     
    str1 = "geeksforgeeks";
    str2 = "geeks";
    print(countSubstring(str1, str2));
 
    str1 = "aaaaa";
    str2 = "aaa";
    print(countSubstring(str1, str2));
