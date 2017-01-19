class HashTable:
    def __init__(self,s):                                                       
        self.size=s
        self.table=[[] for i in range (0,self.size)]        #using list of lists for collision resolution
        
    def hash_function(self,key):                            #hash function for integer key
        return key % self.size

    def hash_function_string(self,key):                     #hash function for string key
        sum=0
        for i in range (0,len(key)):
            sum+=(((i+1)*ord(key[i])))                      #multiple by (i+1) to have diffrent hash values for anagrams
        return sum % self.size

    def insert(self,key,val):
        if isinstance(key,int):
            self.table[self.hash_function(key)].append((key,val))
        elif isinstance(key,str):
            self.table[self.hash_function_string(key)].append((key,val))
            
    def find_val(self,key):
        if isinstance(key,int):
            h=self.hash_function(key)
        elif isinstance(key,str):
            h=self.hash_function_string(key)
        for i in range (0,len(self.table[h])):
            if self.table[h][i][0]==key:
                return self.table[h][i][1]
    def isin(self,key):
        if isinstance(key,int):
            h=self.hash_function(key)
        elif isinstance(key,str):
            h=self.hash_function_string(key)
        for i in range (0,len(self.table[h])):
            if self.table[h][i][0]==key:
                return True
        return False


if __name__=="__main__":
    t=HashTable(11)
    t.insert(5,44)
    t.insert(44,"apple")
    t.insert(55,"orange")
    t.insert(66,"strawberry")
    t.insert("awesome",55)
    print("44 is in table: "+ str(t.isin(44)))
    print("89 is in table: "+ str(t.isin(89)))
    print("'awesome' is in table: "+ str(t.isin("awesome")))
    print("The value of awesome is "+str(t.find_val("awesome")))
    print("The value of 66 is "+str(t.find_val(66)))
    print(t.table)
