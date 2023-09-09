'''
  PROGRAM : DES Encryption and descryption
  Programmed By : Aswanth V C
'''
import sys
class DES:
    # INITIAL PERMUTATION BOX
    IP = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    # INVERSE PERMUTATION BOX (FINAL)
    FP = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]
    # EXPANSION BOX (32 BIT -> 48 BIT)
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
    # S BOX (6BIT -> 4 BIT)
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
    # PERMUTAION BOX FOR SHUFFLING 32 BIT (48 BIT -> 32BIT)
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
    #  PERMUTATION BOX FOR KEY GENERATION (64 BIT -> 56 BIT)
    PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]
    # SHIFT TABLE (HOW MUCH TIME WANT TO BE LEFT SHIFTED FOR KEY GENERATION)
    SHIFT_TABLE = [1, 1, 2, 2,
               2, 2, 2, 2,
               1, 2, 2, 2,
               2, 2, 2, 1]
    # PERMUTATION BOX FOR KEY GENERATION (56 BIT -> 48 BIT)
    PC_2 = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]
    text = None # THE ORIGINAL TEXT GIVEN
    bin_text = "" # THE TEXT IN BINARY (ALL TEXT)
    key = None # THE KEY IN BINARY
    grped = [] # THE TOTAL TEXT CONVERTED INTO GROUPS OF 64 BIT

    # APPLY DES ENCRYPTION TO THE GIVEN TEXT USING THE KEY
      # ACCEPT THE TEXT AND KEY, ALSO THE VERBOSE FLAG TO ENABLE PRINTING
    def encrypt(self,text=None,key=None,verbose=True):
      if text == None or key == None:raise ValueError("None value provided")
      self.text = text
      if len(key) != 8:raise ValueError("Expected 8 Character Key")
      self.key = self.string_to_binary(key) # GET THE BINARY OF THE 64 BIT KEY
      self.bin_text = self.string_to_binary(text) # GET THE BINARY OF THE TEXT
      if verbose:
        print(f"TEXT : {self.print_hex_data(self.bin_text,False)}")
        print(f"KEY : {self.print_hex_data(self.key,False)}")
      self.grped = self.split_to(self.bin_text,64) # SPLIT TO GROUPS OF 64 BITS
      cipher_bin = "" # VARIABLE TO STORE FINAL RESULT
      keys = self.get_round_keys(self.key) # GET THE ROUND KEYS 48 BIT
      for i in self.grped:
        after_ip = self.permute(i,self.IP) # APPLY INITIAL PERMUTAION BOX
        if verbose:
          print("After IP : ",end="")
          self.print_hex_data(after_ip)
        cur = after_ip
        for i in range(16):
          cur = self.feistel_round(cur,keys[i]) # DO THE FEISTEL ROUND WITH THE KEY
          if verbose:print(f"Round {i+1} {self.print_hex_data(cur[0:32],False)} {self.print_hex_data(cur[32:64],False)} {self.print_hex_data(keys[i],False)}")
        l = cur[:32]
        r = cur[32:64]
        cur =r+l
        cur = self.permute(cur,self.FP) # APPLY INVERSE INITIAL PERMUTAION
        cipher_bin += cur
      if verbose:print(f"CIPHER TEXT : {self.print_hex_data(cipher_bin,False)}")
      return cipher_bin,self.print_hex_data(cipher_bin,False) # RETURN THE BINARY CIPHER TEXT AND HEX CIPHER TEXT
    # KEY SCHEDULING FOR GENERATING THE ROUND KEYS
      # ACCEPT THE 64 BIT KEY RETURNS A LIST OF 48 BIT KEYS
    def get_round_keys(self,key):
      if len(key)!= 64:raise ValueError("Expected 64 bit key")
      p_key = "".join([key[self.PC_1[i] - 1] for i in range(len(self.PC_1))]) # CONVERT 64 BIT TO 56 BIT AND PERMUTE
      l = p_key[:28]
      r = p_key[28:]
      keys = []
      for i in range(16):
        l = self.shift_left(l,self.SHIFT_TABLE[i]) # SHIFT TO LEFT BY THE GIVEN TIMES
        r = self.shift_left(r,self.SHIFT_TABLE[i]) # SHIFT TO LEFT BY THE GIVEN TIMES
        k = l + r
        key = "".join([k[self.PC_2[i] - 1] for i in range(len(self.PC_2))]) # APPLY PC2 PERMUTAION 56 BIT TO 48 BIT
        keys.append(key)
      return keys
    # CONVERTS INT INTO BITS
      # ACCEPTS THE INT VALUE AND THE LENGTH OF THE BINARY STRING (PADDED WITH 0)
    def int_to_bits(self,val,n):
      k = bin(val).lstrip("0b")
      if len(k)  != n:
        k = "0" * (n - len(k)) + k
      return k
    # APPLY FIESTEL ROUND
      # ACCEPT THE TEXT AND THE KEY AND RETURN THE NEXT LEFT+RIGHT
    def feistel_round(self,text,key):
      if len(key) != 48:raise ValueError("Expected 48 bit key")
      if len(text) != 64:raise ValueError("Expected 64 bits")
      left = text[:32]
      right = text[32:]
      res_left = right
      after_f = self.des_f_function(right,key) # DO THE DES F FUNCTION
      res_right = self.bitwise_xor(after_f,left) # XOR LEFT AND RESULT FROM DES_F_FUNCTION
      return res_left + res_right
    # THE DES F FUNCTION  
      # ACCEPT TEXT AT THE RIGHT SIDE AND THE ROUND KEY (48BIT)
    def des_f_function(self,right,key):
      if len(key)!= 48:raise ValueError("Expected 48 bit key")
      if len(right)!= 32:raise ValueError("Expected 32 bits")
      exp_right = self.permute(right,self.E_BOX) # EXPANSION BOX (32 BIT -> 48 BIT)
      xor_right = self.bitwise_xor(exp_right,key) # XOR RESULT FROM EXPANSION BOX AND KEY(48 BIT)
      splitted = [xor_right[6*i:6*i+6] for i in range(8)] # SPLIT THE TEXT INTO 8 PEACES OF 6 BIT EACH
      res_32 = []
      for i in range(8):
        # APPLY S_BOX FOR EACH
        res_32.append(self.s_box(splitted[i],self.S_BOX[i]))
      after_perm = self.permute("".join(res_32),self.P_BOX) # APPLY THE PERMUTAION BOX TO THE F FUNCTION
      return after_perm
    # APPLY THE GIVEN PERRMUTAION BOX TO THE TEXT
    def permute(self,text,box):return "".join([text[box[i] - 1] for i in range(len(box))])
    # APPLY INVERSE OF GIVEN PERRMUTAION BOX TO THE TEXT
    def inverse_permute(self,text,box):return "".join([text[i - 1] for i in box])
    # APPLY GIVEN S BOX TO GIVEN TEXT
      # ACCEPT THE TEXT AND THE S BOX
    def s_box(self,text,s_box):
      if len(text)!= 6:raise ValueError("Expected 6 bits")
      row = int(text[0]+text[5],2) # GET THE ROW INDEX (0-4)
      column = int(text[1]+text[2]+text[3]+text[4],2) # GET THE COLUMN INDEX (0-15)
      binary = bin(s_box[row][column]).lstrip("0b") # GET THE CORRESPONDING SBOX VALUE
      if len(binary) != 4:
        binary = "0"*(4-len(binary))+binary # PADD WITH 0
      return binary
    # SPLIT A GIVEN TEXT TO GROUP OF N NUMBERS. THE STRING WANT TO BE ABLE TO GROUP IN THAT LENGTH
    def split_to(self,text,n):
      if type(text) != str and type(text) != bytes:raise ValueError("Expected bytes or string as text")
      if type(n) != int:raise ValueError("Expected int as n")
      grp = []
      for i in range(int(len(text)/n) if len(text)%n == 0 else int(len(text)/n + 1)):
        if len(text[i*n:]) < n:
          text = text[:i*n] + ('0' * (n-len(text[i*n:]))) + text[i*n:]
        grp.append(text[i*n:i*n+n])
      return grp
    # CONVERT A STRING(UTF-8) TO A STRING REPRESENTATING THE BINARY VALUES(8BIT)
    def string_to_binary(self,text):
      if type(text) != str:
        raise ValueError("Expected String as value")
      str_bytes = ""
      for i in bytes(text,"utf-8"):
        tmp = bin(i).lstrip("0b")
        if len(tmp) < 8:tmp = '0'*(8-len(tmp)) + tmp
        str_bytes += tmp
      return str_bytes
    # CONVERT THE STRING OF BINARY VALUES INTO A STRING OF CORRESPONDING VALUES(UTF-8)
    def binary_to_string(self,string):
      if type(string) != bytes and type(string) != str:
        raise ValueError("Expected bytes as input")
      str_text = ""
      for i in range(int(len(string)/8)):
        str_text+=chr(int(string[i*8:i*8+8],2))
      return str_text
    # PRINT DATA IN HEX, IF M IS TRUE IT WILL RETURN THE VALUE INSTEAD OF PRINITING, IF X REMOVE THE 0X FROM BEGGINING
    def print_hex_data(self,text,m=True,x=True):
      if m:print(hex(int(text,2)).upper().lstrip("0X" if x else ""))
      else:return hex(int(text,2)).upper().lstrip("0X" if x else "")
    # PRINT  A DATA IN THE GIVEN M,N MATRIX FORMAT
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
    # XOR OPERATION ON INDIVIDUAL BITS
    def bitwise_xor(self,a, b):
        result = ""
        for i in range(len(a)):
            if a[i] == b[i]:
                result += '0'
            else:
                result += '1'
        return result
    # SHIFT THE BITS TO LEFT BY THE GIVEN COUNT
    def shift_left(self,k, nth_shifts):
      s = ""
      for i in range(nth_shifts):
        for j in range(1, len(k)):
          s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
      return k
    # Decrypt THE MESSAGE
      # ACCEPT TEXT, KEY AND HEX_TEXT 
    def decrypt(self,text=None,key=None,hex_text=None,verbose=True):
      if hex_text != None and text == None:
        text = bin(int(hex_text,16)).lstrip("0b")
        if len(text)%64 != 0:text = ('0' * (64 - len(text)%64)) + text
      if text == None or key is None:raise ValueError("None value provided")
      self.key = self.string_to_binary(key) # TO BINARY KEY
      if verbose:
        print(f"CIPHER TEXT : {text}")
        print(f"KEY : {self.print_hex_data(self.key,False)}")
      self.grped = self.split_to(text,64) # GROUP INTO 64 BITS
      cipher_bin = ""
      keys = self.get_round_keys(self.key) # GET THE ROUND KEYS
      for i in self.grped:
        after_ip = self.inverse_permute(i,self.IP) # PERMUTE
        if verbose:print(f"After IP : {self.print_hex_data(after_ip,False)}")
        l = after_ip[:32]
        r = after_ip[32:]
        cur = after_ip
        for i in range(16):
          cur = self.feistel_round(cur,keys[15-i]) # APPLY FIESTEL ROUNDS USE THE KEYS IN INVERSE
          if verbose: print(f"Round {i+1} {self.print_hex_data(cur[0:32],False)} {self.print_hex_data(cur[32:64],False)} {self.print_hex_data(keys[15-i],False)}")
        l = cur[:32]
        r = cur[32:64]
        cur =r+l
        cur = self.inverse_permute(cur,self.FP) # INVERSE PERMUTE FP
        cipher_bin += cur
      if verbose:print(f"TEXT : {self.binary_to_string(cipher_bin)}")
      return cipher_bin,self.binary_to_string(cipher_bin)

if __name__ == "__main__":
  verbose = False
  binary = False
  key = None
  plain = None
  cipher = None
  for arg in sys.argv[1:]:
    if arg == "-h" or arg == "--help":
      print("Usage : python3 des.py -k <KEY> [-e <PLAIN TEXT> / -d <CIPHER TEXT>]\n\t-v or --verbose : show verbose\n\t-b or --binary : use binary values")
      exit()
    elif arg == "-k" or arg == "--key":
      key = sys.argv[sys.argv.index(arg)+1]
    elif arg == "-e" or arg == "--encrypt":
      plain = sys.argv[sys.argv.index(arg)+1]
    elif arg == "-d" or arg == "--decrypt":
      cipher = sys.argv[sys.argv.index(arg)+1]
    elif arg == "-v" or arg == "--verbose":
      verbose = True
    elif arg == "-b" or arg == "--binary":
      binary = True
  if key == None or cipher == None and plain == None:
    print("Expected plain text (-e) or cipher text (-d) and key (-k)")
    exit()
  des = DES()
  if cipher == None and plain != None:
    print("Encrypting :",plain)
    ci,ci_hex = des.encrypt(text=plain,key=key,verbose=verbose)
    if binary:print(f"Cipher Text : {ci}")
    else:print(f"Cipher Text Hex : {ci_hex}")
  else:
    print("Decrypting :",cipher)
    if binary:txt = des.decrypt(text=cipher,key=key,verbose=verbose)
    else:txt = des.decrypt(hex_text=cipher,key=key,verbose=verbose)
    print(f"Message is : {txt[1]}")