def non_random(file):
    with open(file, "r") as file:
        numbers = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        count = 0
        for x in file.read():
            try:
                numbers[int(x)] += 1
                count += 1
            except:
                pass

        chi_test = 0
        oi = count / 6
        for key in numbers:
            chi_test += ((numbers[key] - oi)**2)/numbers[key]
        if chi_test > 11:
            print("nenahodna data")
        else:
            print("nahodna data")
        print("hodnota chi kvadratu:", chi_test)
        print("\n\n\n")



non_random("random_data/random1.txt")
non_random("random_data/random2.txt")
non_random("random_data/random3.txt")
non_random("random_data/random4.txt")
non_random("random_data/random5.txt")
non_random("random_data/random6.txt")
non_random("random_data/random7.txt")