import math

#-------------------------------------------------------------------------
#find r using relation -->  2 ^ r >= m + r + 1 
def calcRedundantBits(m):
     for i in range(m):
          if(2**i >= m + i + 1):
               return i
#-------------------------------------------------------------------------
#find positions of redundunt bits and put 0 in their place 
def posRedundantBits(data, r):
     m=len(data)
     mes=''
     c,k=0,1

     for i in range(1,m+r+1):
          
          if(2**c==i):
               mes+='0'
               c+=1

          else:
               mes+=data[-1*k]
               k+=1
     
     return mes[::-1]
#-------------------------------------------------------------------------
#ُencode
def Encode():
     data = input("Enter the data to be transmitted: ")
     m = len(data)
     r = calcRedundantBits(m)
     arr = posRedundantBits(data, r)
     n = len(arr)

     #i is used to find position of parity bit in code
     for i in range(r):
          val = 0

          #j is used to find position of bit to be checked
          for j in range(1, n + 1):
               if(j & (2**i) == (2**i)):
                    val = val ^ int(arr[-1 * j])

          # (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n)
          arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
     print ("The encoded message is : ",end="")
     return arr
#-------------------------------------------------------------------------
#decode
def decoding():
     codeWord = input("Enter the codeword : ")   
     n = len(codeWord)
     j=0
     message=""

     for i in range(1 , n+1):
          if(i == 2**j):
               j+=1  
          else:
               message+=codeWord[-1*i]

     return message[::-1]
#-------------------------------------------------------------------------
# error detection and correction
def detectError():
     Data = input("Enter the codeword : ")   
     n=len(Data)
     r = int(math.log2(n))+ 1
     res=0
     for i in range(r):
          val=0
          for j in range(1,n+1):
               
               if(j & (2**i) == (2**i)):
                    val^=int(Data[-1 * j])

          res+=val*(2**i)

     if(res==0):
          print("There is no error in the received message.")
          ans = Data
     else:
          print ("The position of error is " ,res ," from right")
          print ("The correct decode is : ",end="")
          ans = Data[:n-res] + str(1 ^ int(Data[n-res])) + Data[n-res+1:]

     return ans
#-------------------------------------------------------------------------
def main():
     c='y'
     while(c=='y'):
          print("---------------------------------------------------------")
          print("|             H  e   l   l   o    In                    |")
          print("|       Encoding    and    Decoding    checker          |")
          print("|            Using Hamming Code Algorithm               |")
          print("---------------------------------------------------------")
          print("\n")
          print("****************** M    E   N   U ******************")
          print(" 1) Encode   ")
          print(" 2) Decode   ")
          print(" 3) Error detection and Correction")
          
          x=input("Enter Number Of Transaction You Want: ")
          L = [Encode, decoding, detectError]
          try:
               x = int(x)
               ans = L[x-1]()
               print(ans)
          except:
               print("Sorry! No number match :(")

          c=input("Do you want to continue?y/n.\n")

main()