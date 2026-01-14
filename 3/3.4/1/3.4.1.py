import csv

file_name = "3/3.4/1/Crimes.csv"
atribute = "Primary Type"
year = 2015

def get_year(date: str) -> int:
    """_summary_

    Args:
        date (str): _description_

    Returns:
        int: year

    Example:
    >>> date = "10/01/2002 12:47:08 PM"
    >>> get_year(date)
    2002
    """
    result = date.split("/")[2][:4]
    return int(result)
    
   
def task(file_name):
    with open(file_name) as f:
        reader = csv.reader(f)
        header = reader.__next__()
        dic = {}

        for row in reader:
            current_date = row[header.index("Date")]
            current_year = get_year(current_date)
            if current_year == year:
                val_atribute = row[header.index(atribute)]
                dic[val_atribute] = dic.setdefault(val_atribute, 0) + 1
       
    return max(dic, key=dic.get)


def main():
    result = task(file_name)
    print(result)




def tests():
    import doctest
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    # tests()
    main()
