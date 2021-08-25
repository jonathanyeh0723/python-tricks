from subpackage1 import moduleX


if __name__ == "__main__":
    jonathan = moduleX.Cat('jonathan', 35)
    print(vars(jonathan))
    print(jonathan.speak())
