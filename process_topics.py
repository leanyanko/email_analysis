import pandas as pd

from io import StringIO

import string

def topic(s):
    if isinstance(s, float) or len(s) < 2 or "), (" not in s:
        return ""
    arr = s.split("), (")
    tmp = arr[0].split(',')
    text = tmp[0][3:len(tmp[0]) - 1]
    num = tmp[1][1:len(tmp[1]) - 1]
    # print(num)
    return text

def num(s):
    if isinstance(s, float) or len(s) < 2 or "), (" not in s:
        return ""
    arr = s.split("), (")
    tmp = arr[0].split(',')
    num = tmp[1][1:len(tmp[1]) - 1]
    # print(num)
    return num

def main():
    with open('tuples.csv', 'r') as csvfile:
        data = csvfile.read()
        df = pd.read_csv(StringIO(data))

    df["main_topic"] = df["topics"].apply(topic)
    df["probability"] = df["topics"].apply(num)
    f = open('main_topic.csv', 'w')
    f.write(df.to_csv())
    f.close()
    print("done")

main()