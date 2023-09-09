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
    E_BOX = [
      32,  1,  2,  3,  4,  5,
      4,  5,  6,  7,  8,  9,
      8,  9, 10, 11, 12, 13,
      12, 13, 14, 15, 16, 17,
      16, 17, 18, 19, 20, 21,
      20, 21, 22, 23, 24, 25,
      24, 25, 26, 27, 28, 29,
      28, 29, 30, 31, 32,  1
    ]
    S_BOX = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

            [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

            [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

            [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

            [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

            [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

            [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

            [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
    P_BOX = [
        16,  7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2,  8, 24, 14,
        32, 27,  3,  9,
        19, 13, 30,  6,
        22, 11,  4, 25
    ]
    PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]
    SHIFT_TABLE = [1, 1, 2, 2,
               2, 2, 2, 2,
               1, 2, 2, 2,
               2, 2, 2, 1]
    PC_2 = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]

    text = None # the original text given
    bin_text = "" # the text in binary (all text)
    key = None # the key in binary
    grped = [] # the total text converted into groups of 64 bit

    CUR_TEXT = ""
    CUR_MATRIX = ""
    def __init__(self):
        pass
    # Apply DES encryption to the given text using the key
    def encrypt(self,text,key):
      self.text = text
      if len(key) != 8:raise ValueError("Expected 8 Character Key")
      self.key = self.string_to_binary(key)
      # print(f" - Text : {text}")
      # print(f" - Key : {key} (converted to {len(self.key)} bit)")
      self.bin_text = self.string_to_binary(text)
      print(f"TEXT : {self.print_hex_data(self.bin_text,False)}")
      # print(f"    - Binary equivalent of length: {len(self.bin_text)}")
      # print(f"    - HEX : ",end="")
      # self.print_hex_data(self.bin_text)
      self.grped = self.split_to(self.bin_text,64)
      # print(f"    - Splited the text into '{len(self.grped)}' group of 64 bits")
      cipher_bin = ""
      for i in self.grped:
        after_ip = self.initial_permutation(i)
        print("After IP : ",end="")
        self.print_hex_data(after_ip)
        cur = after_ip
        keys = self.get_round_keys(self.key)
        for i in range(16):
          # print("  - Text : ",end="")
          # self.print_hex_data(cur)
          # print("  - Key : ",end="")
          # self.print_hex_data(keys[i])
          cur = self.feistel_round(cur,keys[i])
          print(f"Round {i+1} {self.print_hex_data(cur[0:32],False)} {self.print_hex_data(cur[32:64],False)} {self.print_hex_data(keys[i],False)}")
          # print(f"  - After Fiestel round : ",end="")
          # self.print_hex_data(cur)
        l = cur[:32]
        r = cur[32:64]
        cur =r+l
        cur = self.final_permutation(cur)
        cipher_bin += cur
      print(f"CIPHER TEXT : {self.print_hex_data(cipher_bin,False)}")
        # print(f"KEY : ",end="")
        # self.print_hex_data(self.key)
        # print("OUT : ",end="")
        # self.print_hex_data(cur)
        # print(f"KEY (BIN) : {self.key}")
        # print(f"OUT (BIN) : {cur}")
        
        # self.print_matrix_data(cur)
        # after_fp = self.final_permutation(after_ip)
    # Key Scheduling
    def get_round_keys(self,key):
      if len(key)!= 64:raise ValueError("Expected 64 bit key")
      # self.print_matrix_data(key)
      # n_key = ""
      # for i in range(8):
      #   n_key += key[i*8:i*8+7]
      #   print(key[i*8:i*8+7])
      # key = n_key
      # print("Key geneation")
      p_key = "".join([key[self.PC_1[i] - 1] for i in range(len(self.PC_1))])
      # print(f"  - After Permutation {len(p_key)} : ",end ="")
      # self.print_hex_data(p_key)
      l = p_key[:28]
      r = p_key[28:]
      keys = []
      for i in range(16):
        # l = self.int_to_bits(int(l,2) << self.SHIFT_TABLE[i],28)
        # r = self.int_to_bits(int(r,2) << self.SHIFT_TABLE[i],28)
        l = self.shift_left(l,self.SHIFT_TABLE[i])
        r = self.shift_left(r,self.SHIFT_TABLE[i])
        k = l + r
        key = "".join([k[self.PC_2[i] - 1] for i in range(len(self.PC_2))])
        keys.append(key)
      return keys
    # COnverts int to bits
    def int_to_bits(self,val,n):
      k = bin(val).lstrip("0b")
      if len(k)  != n:
        k = "0" * (n - len(k)) + k
      return k
    def feistel_round(self,text,key):
      if len(key) != 48:raise ValueError("Expected 48 bit key")
      if len(text) != 64:raise ValueError("Expected 64 bits")
      left = text[:32]
      right = text[32:]
      res_left = right
      after_f = self.des_f_function(right,key)
      res_right = self.bitwise_xor(after_f,left)
      return res_left + res_right
    def des_f_function(self,right,key):
      if len(key)!= 48:raise ValueError("Expected 48 bit key")
      if len(right)!= 32:raise ValueError("Expected 32 bits")
      # print("DES f Function ..")
      # print(f"  - RIght {len(right)}: ",end="")
      # self.print_hex_data(right)
      exp_right = self.e_box(right)
      # print(f"  - Expanded RIght {len(exp_right)}: ",end="")
      # self.print_hex_data(exp_right)
      xor_right = self.bitwise_xor(exp_right,key)
      # print(f"  - After XOR {len(xor_right)}: ",end="")
      # self.print_hex_data(exp_right)
      b_size = int(len(xor_right)/8)
      splitted = [xor_right[b_size*i:b_size*i+b_size] for i in range(8)]
      # print("Splitted to 8: ",splitted)
      res_32 = []
      for i in range(8):
        # apply s_box for each
        res_32.append(self.s_box(splitted[i],self.S_BOX[i]))
      # print("After SBOX: ",res_32)
      after_perm = self.p_box("".join(res_32))
      # print(f"  - After P_BOX {len(after_perm)}: ",end="")
      # self.print_hex_data(after_perm)
      return after_perm
    # Apply P_box to given text
    def p_box(self,text):
      if len(text) != 32:raise ValueError("Expected 32 bits")
      return "".join([text[self.P_BOX[i] - 1] for i in range(len(self.P_BOX))])
    # Apply given s box to given text
    def s_box(self,text,s_box):
      if len(text)!= 6:raise ValueError("Expected 6 bits")
      row = int(text[0]+text[5],2)
      column = int(text[1]+text[2]+text[3]+text[4],2)
      binary = bin(s_box[row][column]).lstrip("0b")
      if len(binary) != 4:
        binary = "0"*(4-len(binary))+binary
      return binary

    # Apply e box to the given text
    def e_box(self,text):
      if len(text)!= 32:raise ValueError("Expected 32 bits")
      return "".join([text[self.E_BOX[i] - 1] for i in range(48)])
    # split a given text to group of n numbers. the string want to be able to group in that length
    def split_to(self,text,n):
      if type(text) != str and type(text) != bytes:raise ValueError("Expected bytes or string as text")
      if type(n) != int:raise ValueError("Expected int as n")
      # if len(text) % n != 0:raise ValueError(f"The values cant be grouped in to the length {n}")
      grp = []
      for i in range(int(len(text)/n) if len(text)%n == 0 else int(len(text)/n + 1)):
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
    # Apply initail permutation and give back a string
    def initial_permutation(self,text):
        matr = [[text[i-1] for i in ip_row] for ip_row in self.IP]
        txt = "".join(["".join(i) for i in matr])
        return txt
    # Apply final permuation and gives back the text
    def final_permutation(self,text):
      if type(text) != str:raise ValueError("Expected a string")
      res = ""
      for row in range(8):
        for clmn in range(8):
          res += text[self.FP[row][clmn] - 1]
      return res
    # Print data in hex
    def print_hex_data(self,text,m=True,x=True):
      if m:print(hex(int(text,2)).upper().lstrip("0X" if x else ""))
      else:return hex(int(text,2)).upper().lstrip("0X" if x else "")
    # Print  a data in the given m,n matrix format
    def print_matrix_data(self,matrix,m=8,n=8):
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
    
    # XOR operation on individual bits
    def bitwise_xor(self,a, b):
        result = ""
        for i in range(len(a)):
            if a[i] == b[i]:
                result += '0'
            else:
                result += '1'
        return result
    def shift_left(self,k, nth_shifts):
      s = ""
      for i in range(nth_shifts):
        for j in range(1, len(k)):
          s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
      return k

key = "abcdefgh"
des = DES()
des.encrypt("Hi Im Aswanth V C, Im sending this very secret message $1+",key)

