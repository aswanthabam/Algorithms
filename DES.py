class DES:
    IP = [
        [58, 50, 42, 34, 26, 18, 10, 2],
        [60, 52, 44, 36, 28, 20, 12, 4],
        [62, 54, 46, 38, 30, 22, 14, 6],
        [64, 56, 48, 40, 32, 24, 16, 8],
        [57, 49, 41, 33, 25, 17, 9, 1],
        [59, 51, 43, 35, 27, 19, 11, 3],
        [61, 53, 45, 37, 29, 21, 13, 5],
        [63, 55, 47, 39, 31, 23, 15, 7]
    ]
    FP = [
        [40, 8, 48, 16, 56, 24, 64, 32],
        [39, 7, 47, 15, 55, 23, 63, 31],
        [38, 6, 46, 14, 54, 22, 62, 30],
        [37, 5, 45, 13, 53, 21, 61, 29],
        [36, 4, 44, 12, 52, 20, 60, 28],
        [35, 3, 43, 11, 51, 19, 59, 27],
        [34, 2, 42, 10, 50, 18, 58, 26],
        [33, 1, 41, 9, 49, 17, 57, 25]
    ]
    cur_matrix = None
    cur_text = None
    text = None
    bin_text = ""
    grped = []
    def __init__(self,text):
        self.text = text
        print(f"Text : {text}")
        self.bin_text = self.string_to_binary(text)
        print(f"Binary equivalent of length: {len(self.bin_text)}")
        self.grped = self.split_to(self.bin_text,64)
        print(f"Splited the text into '{len(self.grped)}' group of 64 bits")
        print(self.binary_to_string(self.grped[0]))
        for i in self.grped[:1]:
          print("Before permutations: ")
          self.print_matrix_data(i,8,8)
          perm = self.initial_permutation(i)
          print(f"After IP (Result): ")
          self.print_matrix_data(perm)
          
          fperm = self.final_permutation(perm)
          print(f"After FP (Result): ")
          self.print_matrix_data(fperm,8,8)
          print(f"equivalent : {self.binary_to_string(fperm)}")
    # split a given text to group of n numbers. the string want to be able to group in that length
    def split_to(self,text,n):
      if type(text) != str and type(text) != bytes:raise ValueError("Expected bytes or string as text")
      if type(n) != int:raise ValueError("Expected int as n")
      # if len(text) % n != 0:raise ValueError(f"The values cant be grouped in to the length {n}")
      grp = []
      for i in range(int(len(text)/n) if len(text)%n == n else int(len(text)/n + 1)):
        if len(text[i*n:]) < n:
          text = text[:i*n] + ('0' * (n-len(text[i*n:]))) + text[i*n:]
        grp.append(text[i*n:i*n+n])
      return grp
    # Convert a string(utf-8) to a string representating the binary values(8bit)
    def string_to_binary(self,text):
      if type(text) != str:
        raise ValueError("Expected String as value")
      str_bytes = ""
      for i in bytes(text,"utf-8"):
        tmp = bin(i).lstrip("0b")
        if len(tmp) < 8:tmp = '0'*(8-len(tmp)) + tmp
        str_bytes += tmp
        #print(tmp)
      return str_bytes
    # convert the string of binary values into a string of corresponding values(utf-8)
    def binary_to_string(self,string):
      if type(string) != bytes and type(string) != str:
        raise ValueError("Expected bytes as input")
      str_text = ""
      for i in range(int(len(string)/8)):
        str_text+=chr(int(string[i*8:i*8+8],2))
      return str_text
    def initial_permutation(self,text):
        self.cur_matrix = [[text[i-1] for i in ip_row] for ip_row in self.IP]
        self.cur_text = "".join(["".join(i) for i in self.cur_matrix])
        return self.cur_matrix
    def final_permutation(self,matrix):
      if type(matrix) != list:raise ValueError("Expected a list of list ,matrix")
      res = []
      for row in range(8):
        m = []
        for clmn in range(8):
          m.append(matrix[int((self.FP[row][clmn] - 1)/8)][self.FP[row][clmn] % 8])
        res.append(m)
      return "".join(["".join(i) for i in res])
    def print_matrix_data(self,matrix,m=None,n=None):
      if type(matrix) == list:
        for row in matrix:
          print("|",end=" ")
          for elem in row:
            print(elem, end=" ")
          print("|")
      elif type(matrix) == str:
        if m == None or n == None:raise ValueError("Give m,n for string")
        if m*n != len(matrix):raise ValueError("Expected string doesnt match length")
        for row in range(m):
          print("|",end=" ")
          for clmn in range(n):
            print(matrix[row*m+clmn], end=" ")
          print("|")
    
des = DES("Hi Im Aswanth V C, Im sending this very secret message $1+")

