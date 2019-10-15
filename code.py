# --------------
#Code starts here
def reverse(number):
    reverse = 0
    while number:
        reverse = reverse*10 + number%10
        number = number//10
    return reverse

def palindrome(num):
    result = 0
    if num == num%10:
        result = num + 1
    elif num == reverse(num):
        result = num
        #print("Already palindrome")
    else:
        while True:
            num = num + 1
            if num == reverse(num):
                #print("next palindrome: " + str(num))
                result = num
                break
       
    return result

palindrome(121)


        




# --------------
#Code starts here
def a_scramble(str_1,str_2):
    str_1 = str_1.replace(" ", "")
    str_2 = str_2.replace(" ", "")
    str_1 = str_1.upper()
    str_2 = str_2.upper()
    str_1_len = len(str_1)
    str_2_len = len(str_2)
   
    count = 0
    for x in str_2:
        if x in str_1:
            if str_1.count(x) >= str_2.count(x):
                count = count + 1
    if count == str_2_len:
        return True
    else:
        return False
            
        
output1 = a_scramble("Tom Marvolo Riddle","Voldemort")
print(output1)
output2 = a_scramble("ticket","chat")
print(output2)
output3 = a_scramble("baby shower","shows")
print(output3)


# --------------
#Code starts here
def fib_list(num):
    
     final = ''
     first = 1
     last = 1
     count = 0
     while count < 100:
        #final = str(first) + str(last)
        nth = first + last
        first = last
        last = nth
        final = str(first) + final
        
        count += 1
     
     return final
    
#fib_list()
def check_fib(num):
    lst = fib_list(num)
    if str(num) in str(lst):
        return True
    else:
        return False
    
    

check_fib(456)
check_fib(987)



# --------------
#Code starts here
def compress(word):
    i = 0 
    final = ""
    word = word.replace(" ", "")
    word = word.lower()
    print(len(word))
    while i <= len(word)-1:
        
        count = 1
        
        if i != len(word)-1:
            while word[i] == word[i+1]:
                
                i += 1
                count = count + 1

                if i+1 == len(word):
                   
                    break
                
        
        final = final + word[i]+str(count)
        i = i+1
    return final
      
    
    
        
            
    
new_str = compress('ssggtts')
print(new_str) 




# --------------
#Code starts here
def k_distinct(string ,k):
    string = string.replace(" ","")
    string = string.lower()
    string = set(string)
    print(string)
    if len(string) == k:
        return True
    else:
        return False

k_distinct('Falafel',5)


