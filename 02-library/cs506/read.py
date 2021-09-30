import re
def read_csv(csv_file_path):
    """
    read in csv dataset assuming there is no header 
    :param dataset_path: the string path to the dataset file
    :return: dataset as a numpy array
    """
    # open the file to read and MUST HAVE ENCODING otherwise there is a charmap issue 
    f = open(csv_file_path, "r", encoding="utf8")
    
    # readlines (assume no header)
    lines = f.readlines()
    
    # initialize an empty dataset and read line by line 
    dataset = []

    for line in lines:
        # use regex to split the line by a comma only when the comma is preceded by an even number of quotes
        # attr = re.split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', line)
        attr = line.split(sep=",")
        attr_processed = [elem[1:-1] \
                    if (elem[0] == '"' and elem[-1] == '"') or (elem[0] == "'" and elem[-1] == "'") \
                    else int(elem) for elem in attr]
        
        # so append the split list but everything is maintained as strings 
        dataset.append(attr_processed)
    
    # close the file 
    f.close()
    
    #  return the numpy array of the dataset with only the longitude, latitude, and price
    return dataset