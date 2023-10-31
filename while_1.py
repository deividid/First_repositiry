suma = 0

while True:
  upload = input()
  if upload == "NoMoreMoney":

      break
  new_upload = float(upload)
  if new_upload < 0:
      print(f"Invalid operation!")

      break

  else:
      print(f"Increase: {new_upload: .2f}")
      suma += new_upload

print(f"Total: {suma: .2f}")









