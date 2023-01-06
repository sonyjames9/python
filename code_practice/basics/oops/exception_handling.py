class ZeroDenominatorError(Exception):
  pass


while True:
  try:
    n = input('Enter the numerator : ')
    numer = int(n)
    n = input('Enter the denominator : ')
    denom = int(n)
    if denom == 0:
      raise ZeroDenominatorError("Denominator should not be zero")

    val = numer/denom

  except NameError:
    print("Name not defined")
  except ValueError:
    print("Numerator and Denominator should be integers")
  except ZeroDivisionError:
    print("Numerator cannot be divided by zero")
  except ZeroDenominatorError:
    print("Denominator should not be zero")
  except:
    print("exception raised")

  else:
      print(val)
      break
  finally:
    print(numer)
    print(denom)
    print('Will be executed all the time')
