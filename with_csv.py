def read_csv():
    with open('E:/data.csv') as file:
        keys_csv = file.readline().strip().split(',')
        # print(keys_csv)
        values_csv = [line.strip().split(',') for line in file.readlines()]
        # print(values_csv)
        data_csv = []
        for value_csv in values_csv:
            result = dict(zip(keys_csv, value_csv))
            data_csv.append(result)
        return data_csv

