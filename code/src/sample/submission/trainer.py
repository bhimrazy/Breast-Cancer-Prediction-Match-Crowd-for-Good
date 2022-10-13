import pandas as pd
import sys
import pickle
from sklearn.neighbors import KNeighborsClassifier
import warnings
warnings.filterwarnings('ignore')

def main():
    
    if len(sys.argv) < 2 or len(sys.argv[1]) == 0:
        print("Training input file is missing.")
        return 1
    
    if len(sys.argv) < 3 or len(sys.argv[2]) == 0:
        print("Training output file is missing.")
        return 1
    
    print('Training started.')
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    train_data = pd.read_csv(input_file)

    train_data = train_data.drop_duplicates()
    train_data = train_data.reset_index(drop = True)
    y_train = train_data['cancer']
    x_train = train_data.iloc[:,1:11]

    model = KNeighborsClassifier()
    model.fit(x_train, y_train)

    with open(output_file, "wb") as file:
        pickle.dump(model, file)

    print('Training finished.')

    return 0

if __name__ == "__main__":
    main()
