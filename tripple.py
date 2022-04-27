###
# Triple Data Format
# Copyright Bluebotlaboratories 2022
# I literally ported Maths to strings
# It dum lol
#
#
#
# TODO
# [DONE]    Add addition
# [DONE]    Add subtraction
# [DONE]    Add multiplication
# [TODO]    Add division
###
from copy import copy

class triple():
    def __init__(self, value: str):
        self.value = value

    def subtract(self, value: str):
        if (self.value[0] == "-" and value[0] != "-"):
            self.value = self.internalAdd(self.value[1:], value, 0)
            
            if (self.value[0] == "-"):
                self.value = self.value[1:]
            elif (self.value != "0"):
                self.value = "-" + self.value
                
        elif (self.value[0] == "-" and value[0] == "-"):
            self.value = "-" + self.internalSubtract(self.value[1:], value[1:], 0)
        elif (self.value[0] != "-" and value[0] == "-"):
            self.value = self.internalAdd(self.value, value[1:], 0)
        else:
            self.value = self.internalSubtract(self.value, value, 0)
            
        return self.value
    
    def getNextTen(self, startValue: str, iteration):
        listStart = []
        for char in startValue:
            listStart.append(char)
                    
        #number = startValue[len(startValue)-(iteration+1)]
        numberTwo = int(startValue[len(startValue)-(iteration+2)])
        if (numberTwo > 0):
            listStart[len(startValue)-(iteration+2)] = str(numberTwo - 1)
            result = listStart
        else:
            listStart[len(startValue)-(iteration+2)] = '9'
            startValue = ''.join(listStart)
            result = self.getNextTen(startValue, iteration+1)

        return (''.join(result))

    def internalSubtract(self, startValue: str, changeValue: str, iteration, negative = False):
        if (len(changeValue) > len(startValue)):
            negative = True
            listStart = []
            for char in changeValue:
                listStart.append(char)

            listChange = []
            for char in startValue:
                listChange.append(char)
        else:
            listStart = []
            for char in startValue:
                listStart.append(char)

            listChange = []
            for char in changeValue:
                listChange.append(char)

        if (len(listChange) - (iteration+1) < 0):
            listChange.insert(0, "0")

        if (len(listStart) - (iteration+1) < 0):
            listStart.insert(0, "0")

        startInt = int(listStart[len(listStart) - (iteration+1)])
        changeInt = int(listChange[len(listChange) - (iteration+1)])

        if (changeInt > startInt):
            newNumber = self.getNextTen(''.join(listStart), iteration)
            listStart = []
            for char in newNumber:
                listStart.append(char)
            
            result = str((startInt+10)-changeInt)
        else:
            result = str(startInt-changeInt)
                
        listStart[len(listStart) - (iteration+1)] = result
        finalResult = ''.join(listStart)
        
        if (iteration == len(listChange)-1):
            finalResultTmp = finalResult[:-1].lstrip('0')
            finalResult = finalResultTmp + finalResult[-1]
            if (negative):
                finalResult = "-" + finalResult
        else:
            finalResult = self.internalSubtract(finalResult, ''.join(listChange), iteration+1, negative)

        return finalResult

    def add(self, value: str):
        if (self.value[0] == "-" and value[0] != "-"):
            self.value = self.internalSubtract(self.value[1:], value, 0)
            
            if (self.value[0] == "-"):
                self.value = self.value[1:]
            elif (self.value != "0"):
                self.value = "-" + self.value
            
        elif (self.value[0] == "-" and value[0] == "-"):
            self.value = "-" + self.internalAdd(self.value[1:], value[1:], 0)
        elif (self.value[0] != "-" and value[0] == "-"):
            self.value = self.internalSubtract(self.value, value[1:], 0)
        else:
            self.value = self.internalAdd(self.value, value, 0)
            
        return self.value

    def internalAdd(self, startValue: str, changeValue: str, iteration, carry = 0):
        if (len(changeValue) > len(startValue)):
            listStart = []
            for char in changeValue:
                listStart.append(char)

            listChange = []
            for char in startValue:
                listChange.append(char)
        else:
            listStart = []
            for char in startValue:
                listStart.append(char)

            listChange = []
            for char in changeValue:
                listChange.append(char)

        if (len(listChange) - (iteration+1) < 0):
            listChange.insert(0, "0")

        if (len(listStart) - (iteration+1) < 0):
            listStart.insert(0, "0")

        carry = int(carry)


        startInt = int(listStart[len(listStart) - (iteration+1)])
        changeInt = int(listChange[len(listChange) - (iteration+1)])

        result = str(startInt+changeInt+carry)
        carry = 0
        
        if (len(result) > 1):
            carry = result[0]

        listStart[len(listStart) - (iteration+1)] = result[-1]
        
        finalResult = ''.join(listStart)

        if (iteration == len(listChange)-1 and (carry == 0 or carry == None)):
            pass
        else:
            finalResult = self.internalAdd(finalResult, ''.join(listChange), iteration+1, carry)
        
        return finalResult

    def multiply(self, value: str):
        count = "1"

        if (len(value) > len(self.value)):
            tmpValue = value
            tmpSelf = self.value

            self.value = tmpValue
            value = tmpSelf
        
        if ((value[0] == "-" and self.value[0] != "-") or (value[0] != "-" and self.value[0] == "-")):
            negative = True
        else:
            negative = False

        if (self.value[0] == "-"):
            self.value = self.value[1:]

        ogValue = self.value

        if (value[0] == "-"):
            value = value[1:]
            
        while count != value:
            self.value = self.internalAdd(self.value, ogValue, 0)
            count = self.internalAdd(count, "1", 0)

        if negative:
            self.value = "-" + self.value
            
        return self.value


    
trp = triple("-4")
print(trp.value)
print("+40")
trp.add("40")
print(trp.value)
print("\n\n*3")
trp.multiply("3")
print(trp.value)
print("\n\n-10")
trp.subtract("-10")
print(trp.value)
