from NumberStats import NumberStats


def main():
    a = NumberStats()
    a.add_number(10)
    a.add_number(20)
    a.add_number(23) 
    a.add_number(-203)
    a.add_number(345)
    
    print(a.average())
    print(a.min,a.max)


if __name__ == "__main__":
    main()
