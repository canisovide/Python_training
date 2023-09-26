def test_composable(mot, sequence):
    mot_list = list(mot)
    print(mot_list)
    occurence = [mot.count(i) for i in mot_list]
    print(occurence)
    for i in range(len(mot)):
        if mot.find(mot_list[i]) == 1:
            print(mot_list[i])
            print(sequence.count(mot_list[i]))
            if occurence[i] <= sequence.count(mot_list[i]):

                return "Le mot {} n'est pas composable par {} .".format(mot, sequence)

    return "Le mot {} est composable par {} .".format(mot, sequence)


print(test_composable('coucou', 'uocuoceokzefhu'))
