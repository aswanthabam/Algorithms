# DES (Data Encryption Standard)

### Description

DES is a classic encryption algorithm that operates on fixed-size blocks of data (64 bits) using a secret key (56 bits). It employs a Feistel network structure, which involves multiple rounds of substitution, permutation, and XOR operations to transform plaintext into ciphertext. DES has been widely used for decades, but its small key size makes it vulnerable to brute-force attacks, leading to its eventual replacement by more secure encryption standards like AES (Advanced Encryption Standard). Despite its weaknesses, DES played a pivotal role in the development of modern cryptography and encryption standards.

- Implemented using `python`

### Options

- **-e or --encrypt** : Specify message to encrypt
- **-d or --decrypt** : Specify cipher text to decrypt
- **-b or --binary** : Give the output as binary when encrypting, accept as input while decrypting
- **-k or --key** : to specify 8 character key
- **-v or --verbose** : show verbose including the rounds

### Usage

#### Encryption

A message can be encrypted like below. we use **8 character (UTF-8)** key to encrypt a message. This 8 bit key is converted into 64 bit binary value.

```bash
python3 DES.py -e <MESSAGE> -k <KEY>
```

##### Example

```bash
python3 DES.py -e "This is a secret message to NASA" -k "mykey123"
```

###### Output

```bash
Encrypting : This is a secret message to NASA
Cipher Text Hex : 4CA38F9F77A6435E5BC1CA2BBC8834624762BE696E23EFC86D07A9B24DABB15E
```

#### Decryption

A message can be decrypted like below. we use **8 character (UTF-8)** key to decrypt a message. This 8 bit key is converted into 64 bit binary value. we can give cipher text in either binary or hexadecimal (use -b)

```bash
python3 DES.py -d <CIPHER_TEXT> -k <KEY>
```

##### Example

```bash
python3 DES.py -d "4CA38F9F77A6435E5BC1CA2BBC8834624762BE696E23EFC86D07A9B24DABB15E" -k "mykey123"
```

_Output_

```
Decrypting : 4CA38F9F77A6435E5BC1CA2BBC8834624762BE696E23EFC86D07A9B24DABB15E
Message is : This is a secret message to NASA
```

Thank You :)
