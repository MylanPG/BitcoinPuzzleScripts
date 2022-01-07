# BitcoinPuzzleScripts
Scripts to help solve the Bitcoin Puzzle

These scripts were written to try to solve Bitcoin Puzzle #64. They can be adjusted to solve any of the remaining puzzles with ease.

Each script is tweaked, but essentially does the same thing. It takes private keys and converts them into a public key and then subsequently into a RIPEMD-160.

This RIPEMD-160 string is compared to the RIPEMD-160 of the known Bitcoin Address.

If a key is found, it will print to found.txt

In the original script, I also included the ability to email if the key is found. This requires the yagmail module (pip3 install yagmail)

Due to having to turn off the security on your gmail account and inserting password into this script, it is smart to make a new account that will only be used for this purpose.

This will email you whatever is found, as well as the found.txt file.

Steps to add email notifications:

```
Import yagmail

 if VAR == "{RIPEMD-160 STR}":
  print(pk, pk3, p2)
  print(pk, pk3, p2, file=open("found.txt", "a"))
  receiver = "{your email}"
  body = (pk, pk3)
  filename = "found.txt"


  yag = yagmail.SMTP('{second gmail}', '{password}')
  yag.send(
        to=receiver,
        subject="found",
        contents=body,
        attachments = filename,)
  break
  ```
 
To find out more about the Bitcoin Puzzle Challenge, visit:
https://privatekeys.pw/puzzles/bitcoin-puzzle-tx
  
If you wish to find the RIPEMD-160 of a Bitcoin Address, you can check that here:
https://gobittest.appspot.com/Address
