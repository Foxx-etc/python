

class Verify:
    """
    All the functions defined under this class returns boolean value
    """
    
    def isall_int(c, floatAsInt = True) -> bool:
        """
        True If all elements in container are Integers False otherwise
        If floatAsInt is True, then floats are treated as Integers
        """

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


        
    
    def isall_str(s) -> bool:
        """
        True If all elements in List are string False otherwise
        """
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



    
    def isall_float(c, intAsFloat = True) -> bool:
        """
        True If all elements in container are Float False otherwise
        If intAsFloat is True, then integers are treated as floats
        """
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
        
        
    
    def is_space(s) -> bool:
        """
        Return True If Spaces In String
        """
        if type(s) is not str:
            raise TypeError(f"parameter must be a string not {type(s)}")
        
        for i in s:
            if i==" ":
                return True
            else:
                continue
        return False


class UpdateStr:
    """
    Under this class, In functions, The arguments must be string and returns an updated string
    """
        
    
    def stay_str(s , preserve_space = True) -> str:
        """
        Parameter must be a string otherwise a TypeError is raised
        Removes Everything except alphabets
        If parameter preserve_space is True, then it won't removes spaces
        """
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


    
    def stay_int(n, preserve_space = True) -> str:
        """
        Parameter must be a string otherwise a TypeError is raised
        Removes Everything except Numbers
        If parameter preserve_space is True, then it won't removes spaces
        """
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


    
    def drop_space(s) -> str:
        """
        Removes The Space In String And Joins The Characters
        """
        if type(s) is not str:
            raise TypeError(f"parameter must be a string not {type(s)}")
        
        new_str = ""
        for i in s:
            if i==" ":
                continue
            else:
                new_str += i
        return new_str



class Count:
    """
    Parameter must be Iterable and returns int value
    """
        
    
    def count_str(c) -> int:
        """
        Counts The Number Of String In Iterables and Return Int value
        """
        if type(c) is str or type(c) is int or type(c) is float:
            raise TypeError(f"parameter must not be a {type(c)}")
        
        number = 0
        for i in c:
            if type(i) is str:
                number += 1
            else:
                continue
        return int(number)



    def count_int(c) -> int:
        """
        Counts The Number Of Integer Values In Iterables and Return Int value
        """
        if type(c) is str or type(c) is int or type(c) is float:
            raise TypeError(f"parameter must not be a {type(c)}")
        
        number = 0
        for i in c:
            if type(i) is int:
                number += 1
            else:
                continue
        return int(number)


    def count_float(c) -> int:
        """
        Counts The Number Of Float Values In Iterables and Return Int value
        """
        if type(c) is str or type(c) is int or type(c) is float:
            raise TypeError(f"parameter must not be a {type(c)}")
        
        number = 0
        for i in c:
            if type(i) is float:
                number += 1
            else:
                continue
        return int(number)



class UpdateIter:
        
    def drop_neg_int(c) -> list:
        """
        Removes Negative Integers, If string present as an element in iterable object ignores it
        """
        if type(c) is str or type(c) is int or type(c) is float:
            raise TypeError("parameter must not be a string")
        
        pos = []
        for i in c:
            if type(i) is str or i < 0:
                continue
            else:
                pos.append(i)	
        return pos
    
    
    def drop_pos_int(c) -> list:
        """
        Removes Positive Integers, If string present as an element in iterable object ignores it
        """
        if type(c) is str or type(c) is int or type(c) is float:
            raise TypeError("parameter must not be a string")
        
        neg = []
        for i in c:
            if type(i) is str or i > 0:
                continue
            else:
                neg.append(i)		
        return neg



class DictWork:
    """This class is for dict work"""     

    
    def selectSingle(f : dict , k: dict.keys, index: int):
        """this function is created in aim of accessing an element from dict's value of type: list, tuple, or set"""
        ls = f.__getitem__(k)
        return ls[index]
            

    
    def selectAll(f: dict, k: dict.keys, iterate:bool = False):
        """
        this function is created in aim of accessing an element from dict's value of type: list, tuple, or set
        If iterate is True, then never use this function in print() it has None Return type
        If iterate is False(default) It has return type
        """
        if iterate == False:
            ls = [i for i in f[k]]
            return ls
        else:
            for i in f[k]:
                print(i)


    
    def show(d, design='|' , intToStr = True):
        """
        iterate keys and values in a formated way defaults add a design '|' in between key and value
        if dict is empty gives a ValueError.
        For Design Purpose, We have to measure length of keys so TypeError if key is type 'int'. Default is set to True to convert int to str to measure length.
        """
        if type(d) is not dict:
            raise TypeError(f"parameter must be a { type({}) }")

        # for design purpose, type 'int' has no length we may raise TypeError
        allKeysLength = []
        for n in d.keys():
            if type(n) is not str:
                if intToStr == True:
                    allKeysLength.append(len(str(n)))
                else:
                    raise TypeError(f"key cannot be of type 'int' or 'float'")
                
            else:
                allKeysLength.append(len(n))
        

        if allKeysLength == []:
            raise ValueError("dict cannot be Empty!")
        
        longestLength = max(allKeysLength)

        # formatting for better visibility
        for k, v in zip(d.keys(), d.values()):
            print( f'{str(k).ljust(longestLength)} {design} {v}' )
        return ""


class Restricted:

    def only_alpha(prom= "Enter : ", mess= "No Numbers!\n"):
        """"
        prom is a prompt to user
        mess is an error message when user input unexpected
        """
        while True:
            try:
                letter= input(prom)
                if not letter.isalpha():
                    raise ValueError
                return letter
            except:
                print(mess)
    


  
    def onlySingle_alpha(prom= "Enter : ", mess= "No Numbers!\n", restrict= 'yes', res_mess= "No!\n"):
        """"
        Same as only_alpha() but this function takes two additional parameters

        restrict(user must input what developer ask and default is 'yes'.)
        res_mess( or restrict_message, if user not input restrict)
        """
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



    
    def only_int(prom= "Enter : ", mess= "No Letters!\n"):
        """
        prom is a prompt to user
        mess is an error message when user input unexpected
        """
        while True:
            try:
                number= input(prom)
                if not number.isnumeric():
                    raise ValueError
                return int(number)
            except:
                print(mess)

    
    
    def onlySingle_int(prom= "Enter : ", mess= "No Letters!\n", restrict= '1', res_mess= "No!\n"):
        """
        Same as only_int() but this function takes two additional parameters 
        
        restrict(user must input what developer ask and default is 1. Careful! Use quotation around number or it may considered as res_mess)
        res_mess( or restrict_message, if user not input restrict)
        """
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

    u={
        5 : 1,
        8 : 0,
        424222: "df"
    }
