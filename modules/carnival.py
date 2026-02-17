
# All the functions defined under this class returns boolean value
class Verify:
    # True If all elements in container are Integers False otherwise
    # If floatAsInt is True, then floats are treated as Integers
    def isall_int(c, floatAsInt = True) -> bool:
        for i in c:
            if type(i) is int:
                continue
            
            elif type(i) is float:
                if floatAsInt == True:
                    continue
                else:
                    return False
            
            else:
                return False
        return True

 
    # True If all elements in List are string False otherwise
    def isall_str(s) -> bool:
        for i in s:
            if type(i) is str:
                continue
            else:
                return False
        return True 
    

        
    def isall_bool(b) -> bool:
        for i in b:
            if type(i) is bool:
                continue
            else:
                return False
        return True


    # True If all elements in container are Float False otherwise
    # If intAsFloat is True, then integers are treated as floats
    def isall_float(c, intAsFloat = True) -> bool:
        for i in c:
            if type(i) is float:
                continue
            
            elif type(i) is int:
                if intAsFloat == True:
                    continue
                else:
                    return False
                
            else:
                return False
        return True
        
        
    # Return True If Spaces In String
    def is_space(s) -> bool:
        if type(s) is not str:
            raise TypeError(f"parameter must be a string not {type(s)}")
        
        for i in s:
            if i==" ":
                return True
            else:
                continue
        return False


# Under this class, In functions, The arguments must be string and returns an updated string
class Update_str:
        
    # Parameter must be a string otherwise a TypeError is raised
    # Removes Everything except alphabets
    # If parameter preserve_space is True, then it won't removes spaces
    def stay_str(s , preserve_space = True) -> str:
        if type(s) is not str:
            raise TypeError("Argument must be a string")
        
        ss = ""	
        for i in s:
            if i.isalpha():
                ss += i
                
            elif i == " ":
                if preserve_space == True:
                    ss += i
                else:
                    continue
                
            else:
                continue	
        return ss


    # Parameter must be a string otherwise a TypeError is raised
    # Removes Everything except Numbers
    # If parameter preserve_space is True, then it won't removes spaces
    def stay_int(n, preserve_space = True) -> str:
        if type(n) is not str:
            raise TypeError("Argument must be a string")
        
        si = ""	
        for i in n:
            if i.isnumeric():
                si += i
                
            elif i == " ":
                if preserve_space == True:
                    si += i
                else:
                    continue
                
            else:
                continue	
        return si	


    # Removes The Space In String And Joins The Characters
    def drop_space(s) -> str:
        if type(s) is not str:
            raise TypeError(f"parameter must be a string not {type(s)}")
        
        new_str = ""
        for i in s:
            if i==" ":
                continue
            else:
                new_str += i
        return new_str



# Parameter must be Iterable and returns int value
class Count:
        
    # Counts The Number Of String In Iterables and Return Int value
    def count_str(c) -> int:
        if type(c) is str or type(c) is int or type(c) is float:
            raise TypeError(f"parameter must not be a {type(c)}")
        
        number = 0
        for i in c:
            if type(i) is str:
                number += 1
            else:
                continue
        return int(number)


    # Counts The Number Of Integer Values In Iterables and Return Int value
    def count_int(c) -> int:
        if type(c) is str or type(c) is int or type(c) is float:
            raise TypeError(f"parameter must not be a {type(c)}")
        
        number = 0
        for i in c:
            if type(i) is int:
                number += 1
            else:
                continue
        return int(number)


    # Counts The Number Of Float Values In Iterables and Return Int value
    def count_float(c) -> int:
        if type(c) is str or type(c) is int or type(c) is float:
            raise TypeError(f"parameter must not be a {type(c)}")
        
        number = 0
        for i in c:
            if type(i) is float:
                number += 1
            else:
                continue
        return int(number)



class Update_iter:
        
    # Removes Negative Integers, If string present as an element in iterable object ignores it
    def drop_neg_int(c) -> list:
        if type(c) is str or type(c) is int or type(c) is float:
            raise TypeError("parameter must not be a string")
        
        pos = []
        for i in c:
            if type(i) is str or i < 0:
                continue
            else:
                pos.append(i)	
        return pos


    # Removes Positive Integers, If string present as an element in iterable object ignores it
    def drop_pos_int(c) -> list:
        if type(c) is str or type(c) is int or type(c) is float:
            raise TypeError("parameter must not be a string")
        
        neg = []
        for i in c:
            if type(i) is str or i > 0:
                continue
            else:
                neg.append(i)		
        return neg


# This class is for dict work
class DictWork:      
    # this function is created in aim of accessing an element from dict's value of type: list, tuple, or set 
    def selectSingle(f : dict , k: dict.keys, index: int):
        ls = f.__getitem__(k)
        return ls[index]
            

    # this function is created in aim of accessing an element from dict's value of type: list, tuple, or set
    # If iterate is True, then never use this function in print() it has None Return type
    # If iterate is False(default) It has return type
    def selectAll(f: dict, k: dict.keys, iterate:bool = False):
        if iterate == False:
            ls = [i for i in f[k]]
            return ls
        else:
            for i in f[k]:
                print(i)

    
    # iterate keys and values in a formated way defaults add a design '|' in between key and value
    # if dict is empty gives a ValueError
    def show(d, design='|') -> None:
        if type(d) is not dict:
            raise TypeError(f"parameter must be a { type({}) }")

        allKeysLength = [ len(n) for n in d.keys() ] 
        
        if allKeysLength == []:
            raise ValueError("dict cannot be Empty!")
        
        longestLength = max(allKeysLength)

        # formatting for better visibility
        for k, v in zip(d.keys(), d.values()):
            print(f'{k.ljust(longestLength)} {design} {v}')


class Restricted:

    # prom is a prompt to user
    # mess is an error message when user input unexpected
    def only_alpha(prom= "Enter : ", mess= "No Numbers!\n"):
        while True:
            try:
                letter= input(prom)
                if not letter.isalpha():
                    raise ValueError
                return letter
            except:
                print(mess)

    
    # Same as only_alpha() but this function takes two additional parameters 
    # restrict(user must input what developer ask and default is 'yes'.)
    # res_mess( or restrict_message, if user not input restrict)
    def onlySingle_alpha(prom= "Enter : ", mess= "No Numbers!\n", restrict= 'yes', res_mess= "No!\n"):
        while True:
            try:
                letter= input(prom)
                if not letter.isalpha():
                    raise ValueError
                try:
                    if letter.isalpha():
                        if letter == restrict:
                            return letter
                        else:
                            raise ValueError
                except:
                    print(res_mess)

            except:
                print(mess)


    # prom is a prompt to user
    # mess is an error message when user input unexpected
    def only_int(prom= "Enter : ", mess= "No Letters!\n"):
        while True:
            try:
                number= input(prom)
                if not number.isnumeric():
                    raise ValueError
                return int(number)
            except:
                print(mess)

    
    # Same as only_int() but this function takes two additional parameters 
    # restrict(user must input what developer ask and default is 1. Careful! Use quotation around number or it may considered as res_mess)
    # res_mess( or restrict_message, if user not input restrict)
    def onlySingle_int(prom= "Enter : ", mess= "No Letters!\n", restrict= '1', res_mess= "No!\n"):
        while True:
            try:
                number= input(prom)
                if not number.isnumeric():
                    raise ValueError
                try:
                    if number.isnumeric():
                        if number == restrict:
                            return int(number)
                        else:
                            raise ValueError
                except:
                    print(res_mess)

            except:
                print(mess)


if __name__ == '__main__':
    a = Restricted.onlySingle_alpha(prom="Enter a Number : ",mess= "No Numbers\n", res_mess= "Not This\n")
    print(a)


"""
TODO : Documentation
TODO : Add More Regular functions
"""

    
