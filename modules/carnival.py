

class Verify:
    """
    All the functions defined under this class returns boolean value

    The constructor must be an iterable..
    """
    def __init__(self, iterable):
        self.iterable = iterable

    def isint(self, floatAsInt=True) -> bool:
        """
        True If all elements in container are Integers False otherwise
        If floatAsInt is True, then floats are treated as Integers
        """
        for i in self.iterable:
            if isinstance(i,int):
                continue
            
            elif isinstance(i, float):
                if floatAsInt == True:
                    continue
                else:
                    return False
            
            else:
                return False
        return True

    
    def isstr(self) -> bool:
        """
        True If all elements in List are string False otherwise
        """
        for i in self.iterable:
            if isinstance(i, str):
                continue
            else:
                return False
        return True 
    
  
    def isbool(self) -> bool:
        for i in self.iterable:
            if isinstance(i, bool):
                continue
            else:
                return False
        return True


    def isfloat(self, intAsFloat = False) -> bool:
        """
        True If all elements in container are Float False otherwise
        If intAsFloat is True, then integers are treated as floats
        """
        for i in self.iterable:
            if isinstance(i, float):
                continue
            
            elif isinstance(i, int):
                if intAsFloat:
                    continue
                else:
                    return False
                
            else:
                return False
        return True
        
        
    def isspace(self) -> bool:
        """
        Return True If Spaces In String
        """
        if isinstance(i, str):
            raise TypeError(f"parameter must be a string not {type(s)}")
        
        for i in self.iterable:
            if i==" ":
                return True
            else:
                continue
        return False

    def isnewline(self) -> bool:
        if len(self.iterable) == 0:
            return True
        return False


class UpdateStr:
    """
    Under this class, In functions, The arguments must be string and returns an updated string
    """
    
    def __init__(self, string):
        if not isinstance(string, str):
            raise TypeError("argument must be a string")
        self.string = string

    def staystr(self , preserve_space=True) -> str:
        """
        Parameter must be a string otherwise a TypeError is raised
        Removes Everything except alphabets
        parameter: preserve_space is True, won't removing spaces. If False, all the whitespace charachter are removed. 
        """
        ss = ""	
        for i in self.string:
            if i.isalpha():
                ss += i
                
            elif i.isspace():
                if preserve_space:
                    ss += i
                else:
                    continue
                
            else:
                continue	
        return ss

   
    def stayint(self, preserve_space=True) -> str:
        """
        Parameter must be a string otherwise a TypeError is raised
        Removes Everything except Numbers
        parameter: preserve_space is True, then it won't removing spaces
        """   
        si = ""	
        for i in self.string:
            if i.isnumeric():
                si += i
                
            elif i.isspace():
                if preserve_space:
                    si += i
                else:
                    continue
                
            else:
                continue	
        return si	

 
    def dropspace(self) -> str:
        """
        Removes The Space In String And Joins The Characters
        """      
        new_str = ""
        for i in self.string:
            if i.isspace():
                continue
            else:
                new_str += i
        return new_str


class Count:
    """
    Parameter must be Iterable and returns int value
    """
    def __init__(self, iterable):
        if isinstance(iterable, (str,int,float)):
            raise TypeError(f"parameter must not be: str, int, or float")
        self.iterable = iterable

    def count_str(self) -> int:
        """
        Counts The Number Of String In Iterables and Return Int value
        """
        
        number = 0
        for i in self.iterable:
            if type(i) is str:
                number += 1
            else:
                continue
        return int(number)


    def count_int(self) -> int:
        """
        Counts The Number Of Integer Values In Iterables and Return Int value
        """
        number = 0
        for i in self.iterable:
            if type(i) is int:
                number += 1
            else:
                continue
        return int(number)


    def count_float(self) -> int:
        """
        Counts The Number Of Float Values In Iterables and Return Int value
        """
        
        number = 0
        for i in self.iterable:
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
        if isinstance(c, (str,int,float)):
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
        if isinstance(c, (str,int,float)):
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

    def __init__(self, dictionary):
        if not isinstance(dictionary, dict):
            raise TypeError('argument accepts <class dict>')
        self.dictionary = dictionary

    def selectSingle(self, key: dict.keys, index: int):
        """This function is created in an aim of accessing an element of dictionary's 'value' of type: list, tuple, or set"""
        iterable = self.dictionary[key]
        return iterable[index]
            
    
    def selectAll(self, k: dict.keys, iterate: bool=False):
        """
        this function is created in aim of accessing an element from dict's value of type: list, tuple, or set
        parameter: iterate=True, then never use this function in print() statment it returns None.
        """
        if not iterate:
            ls = [i for i in self.dictionary[k]]
            return ls
        else:
            for i in self.dictionary[k]:
                print(i)

    
    def show(self, design='|' , intToStr=True) -> None:
        """
        iterate keys and values in a formated way defaults add a design '|' in between key and value
        if dict is empty gives a ValueError.
        For Design Purpose, We have to measure length of keys so TypeError if key is type 'int'. Default is set to True to convert int to str to measure length.
        """
        
        # Empty returns False
        if not self.dictionary:
            raise ValueError("dict cannot be Empty!")

        # for design purpose, type 'int' has no length we may raise TypeError
        allKeysLength = []
        for n in self.dictionary.keys():
            if not isinstance(n, str):
                if intToStr:
                    allKeysLength.append(len(str(n)))
                else:
                    raise TypeError(f"key cannot be of type: int or float")      
            else:
                allKeysLength.append(len(n))
               
        maxlen = max(allKeysLength)

        # formatting for better visibility
        for (k, v) in zip(self.dictionary.keys(), self.dictionary.values()):
            print(f'{str(k).ljust(maxlen)} {design} {v}')
        return None


    def getkey(self, value):
        """If Raised A KeyError, Then In Default dict, The Key Is Overriden By Value, So Does Here The Same"""   
        inv_di = {}
        for (k,v) in zip(self.dictionary.keys(), self.dictionary.values()):
            inv_di[v] = k

        return inv_di[value]


class Restricted:

    def allalpha(prompt="Enter : ", error_mess="No Numbers!\n"):
        """"
        parameter: prompt: is a prompt
        parameter: error_mess: is an error message when user input unexpected
        """
        while True:
            try:
                letter= input(prompt)
                if not letter.isalpha():
                    raise ValueError
                return letter
            except:
                print(error_mess)
    

    def singlealpha(prompt="Enter : ", error_mess="No Numbers!\n", expect='yes', expect_mess="No!\n"):
        """"
        Same as Restricted.allalpha() but this function takes two additional parameters,

        parameter: expect: user must input what developer expects and default is 'yes'.
        parameter: expect_mess: if user not input what developer expect
        """
        while True:
            try:
                letter= input(prompt)
                if not letter.isalpha():
                    raise ValueError
                try:
                    if letter.isalpha():
                        if letter == expect:
                            return letter
                        else:
                            raise ValueError
                except ValueError:
                    print(expect_mess)

            except:
                print(error_mess)

 
    def allint(prompt="Enter : ", error_mess="No Letters!\n"):
        """
        parameter: prom is a prompt
        parameter: mess is an error message when user input unexpected

        return value is int
        """
        while True:
            try:
                number= input(prompt)
                if not number.isnumeric():
                    raise ValueError
                return int(number)
            except:
                print(error_mess)

      
    def singleint(prompt="Enter : ", error_mess="No Letters!\n", expect=1, expect_mess="No!\n"):
        """
        Same as Restricted.allint() but this function takes two additional parameters,
        
        parameter: expect: user must input what developer expects, default is 1. Careful! Use quotation for parameter expect, it employees str.isnumeric() then convert to class int.
        parameter: expect_mess: if user not input what developer expects
        """
        while True:
            try:
                number= input(prompt)
                if not number.isnumeric():
                    raise ValueError
                try:
                    if number.isnumeric():
                        if number == expect:
                            return int(number)
                        else:
                            raise ValueError
                except ValueError:
                    print(expect_mess)

            except:
                print(error_mess)



if __name__ == '__main__':
    b = ('fd',6, 8.5, 33.3, 'w', 'sdfs89f')
    a = UpdateStr(b[5]).staystr()
    print(a)
