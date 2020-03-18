def print_accuracy():
    """
    This function compares the results from the dev predictions and dev output to evaluate the
    performance of a model
    :return:
    """
    for i in range(1, 9):
        dev_output = []
        search_engine_output = []
        with open("dev_output/{}.out".format(i), "r") as file:
            reader = file.readlines()
            for line in reader:
                dev_output.append(line.rstrip("\n"))
        with open("dev_predictions/{}.out".format(i), "r") as file:
            reader = file.readlines()
            for line in reader:
                parsed_line = line.rstrip("\n").split(" ")
                search_engine_output.append(parsed_line[0])
        if len(search_engine_output) == 0:
            print("Search Engine has failed on Query {}".format(i))
        else:
            search_engine_output = search_engine_output[: len(dev_output)]
            score = 0
            for url in search_engine_output:
                if url in dev_output:
                    score += 1
            print(
                "For Query {} the Accuracy Score is {}%".format(
                    i, "{0:.2f}".format(score / len(dev_output) * 100)
                )
            )


if __name__ == "__main__":
    print_accuracy()