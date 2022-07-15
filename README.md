# cryptography-decoder
Summer 2022 CECS0912 Intro to Cryptography
Prompt:
Encryption:

The first step is to change the letter of plaintext to its corresponding letter according to the following key:
A=Z
B=R
C=I
D=B
E=U
F=O
G=A
H=S
I=L
J=J
K=D
L=C
M=X
N=Y
O=F
P=G
Q=H
R=M
S=E
T=Q
U=N
V=T
W=K
X=W
Y=P
Z=V
Next, make each letter the number that corresponds with its substituted letter ex: A=Z=26
Then, you would change the number into factor pair that contains the highest prime factor of the number ex: Y=P; P=16; 16=2(highest prime factor)*8
note: both numbers do not have to be prime, it is the factor pair that includes the highest prime factor of the number
Next, write that as the code (2*13=213) 
Each letter will be three digits (2*1=021)
to avoid patterns, numbers can be in any order in each group.
Decryption: 

Multiply each set of three numbers (ignoring zero if it is in the front) and making sure they are broken in a way that makes the answer less than 26
make sure that the two numbers you multiplied include the highest prime factor of their product
Convert the resulting numbers into their corresponding letters
Use the key to find the plaintext letter of the alphabet.
 

Ciphertext Examples:

1) 021023028032027012043022073038028033023012037

2) 171119034051034015035027055

3)021023011015132113037033072117037

4) 191032111213113037028023027

5) 051027038083037131054213033132171034023055

Solutions:

1. DOYOUDIKEMYCODE(DOYOULIKEMYCODE)
2. THISISFUN
3. DOGSARECUTE
4. HOWAREYOU
5. SUMMERVACATION
