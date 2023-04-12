from dataclasses import dataclass

@dataclass
class CompresedData:
    list_for_dict = []
    list_in_conetent = []
    list_in_code = []
    list_in_address = []
    

class LZ77():
    def __init__(self) -> None:
        self.dictionary: dict = {}
        self.address: int = 1
        self.iterator: int= 0
        
    def save_data(self,data,code,address) -> None:
        CompresedData.list_in_address.append(address)
        CompresedData.list_in_code.append(code)
        CompresedData.list_in_conetent.append(data)
                
    
    def compressed(self, data: str) -> CompresedData:
        while (self.iterator < len(data)):
            from_dict_to_array = str(list(self.dictionary.keys()))
            CompresedData.list_for_dict.append(from_dict_to_array[1:-1])
            
            if (data[self.iterator] in self.dictionary) == False:
                self.dictionary[data[self.iterator]] = self.address
                code = '<0, ' + data[self.iterator] + '>'
                self.save_data(self.address,code,data[self.iterator])
                
            
            else:
                temp_data = data[self.iterator]
                
                while True:
                    self.iterator = self.iterator + 1
                    
                    if (((temp_data in self.dictionary) == True) and (self.iterator > (len(data)-1))):
                        code = '<' + str(self.dictionary[temp_data]) + ', #' + '>'
                        self.save_data(self.address,code,temp_data)
                        break
                    
                    temp_data = temp_data + data[self.iterator]
                    
                    
                    if (temp_data in self.dictionary) == False:
                        self.dictionary[temp_data] = self.address
                        code = '<' + str(self.dictionary[temp_data[:-1]]) + ', ' + temp_data[-1] + '>'
                        self.save_data(self.address,code,temp_data)
                        break
            
            self.address = self.address + 1
            self.iterator = self.iterator + 1
        print(self.iterator)

