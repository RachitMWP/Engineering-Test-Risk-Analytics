import os
import sys

import pandas as pd
import glob



class EngineeringTest():        

    def _get_all_csv_files(self, DIR_PATH):
        '''
        Get the list of file in directory and return the list of csv files

        '''
        
        os.chdir(DIR_PATH)
        extension = 'csv'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
        return all_filenames


    def generate_combined_csv(self , df):
        """
            Generating the csv and Saves the dataframe as csv in specific directory
        """
        outdir = './Output'
        if not os.path.exists(outdir):
            os.mkdir(outdir)
        df.to_csv( "Output/combined.csv", index=False, encoding='utf-8', columns= ['Source IP', 'Environment'])

    def file_data_traverses(self, files):

        """
        concatenate the dataframe together
        Returns:
            _type_: A single concatenated dataframe
        """

        dfs = []
        for filename in files:
            sample_df = pd.read_csv(filename)
            file_str = ''.join((x for x in filename.split('.')[0] if not x.isdigit()))
            sample_df['Environment'] = file_str
            dfs.append(sample_df)
            df = pd.concat(dfs, axis=0, ignore_index=True)
        df.drop_duplicates(subset=['Source IP'], inplace=True)
        return df

if __name__ == "__main__":
    DIR_PATH  = input("Enter the Folder Location \n")
    Obj = EngineeringTest()
    try :
        files_csv = Obj._get_all_csv_files(DIR_PATH)
        dataframes = Obj.file_data_traverses(files_csv)
        Obj.generate_combined_csv(dataframes)
        print("Script Running Succesfully")
    except Exception as e:
        print("Something went wrong \n {}" .format(str(e)))