import pandas as pd
import sys
import pickle
import warnings
warnings.filterwarnings('ignore')

def main():
    
    if len(sys.argv) < 2 or len(sys.argv[1]) == 0:
        print("Testing input file is missing.")
        return 1
    
    if len(sys.argv) < 3 or len(sys.argv[2]) == 0:
        print("Testing output file is missing.")
        return 1
    
    print('Testing started.')

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    model_file = sys.argv[3]

    test_data = pd.read_csv(input_file)

    test_data = test_data.drop_duplicates()
    test_data = test_data.reset_index(drop = True)
    ids = test_data['id']
    x_test = test_data.iloc[:,1:11]

    with open(model_file, "rb") as file:
        model = pickle.load(file)

    pred = model.predict(x_test)

    submission_data = pd.DataFrame({'id': ids, 'prediction': pred})

    submission_data.to_csv(output_file, index=False)

    print('Testing finished.')

    return 0

if __name__ == "__main__":
    main()
