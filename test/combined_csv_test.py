import os

import unittest
import pandas as pd
import shutil

from src.main import EngineeringTest
from pandas.util.testing import assert_frame_equal


class CombinedCSV_testing(unittest.TestCase):
    
    def setUp(self):
        self.not_exists_path="/test_csv/not_exist"
        self.empty_path='/test_csv/empty'
        if not os.path.exists(self.empty_path):
            os.makedirs(self.empty_path)
        self.path_without_csv="/test_csv/no_contain_csv"
        if not os.path.exists(self.path_without_csv):
            os.makedirs(self.path_without_csv)
        file = self.path_without_csv + '/test.txt'
        open(file, 'a').close()
        self.path_with_csv="/test_csv/csv"
        if not os.path.exists(self.path_with_csv):
            os.makedirs(self.path_with_csv)
        file = self.path_with_csv + '/test.csv'
        open(file, 'a').close()
        file = self.path_with_csv + '/xyz 2.csv'
        open(file, 'a').close()

    def create_combined_test_folder(self):
        self.path_for_combined= "/test_csv/combined"
        if not os.path.exists(self.path_for_combined):
            os.makedirs(self.path_for_combined)
        test_data_1 = pd.DataFrame([['4.4.4.4', '2', '0'], ['4.4.4.4', '5', '100']], columns=['Source IP', 'Count', 'Events per Second'])
        test_data_1.to_csv(self.path_for_combined + '/asia1.csv', index = False)
        test_data_2 = pd.DataFrame([['4.4.4.4', '6', '0'], ['4.4.4.2', '5', '10']], columns=['Source IP', 'Count', 'Events per Second'])
        test_data_2.to_csv(self.path_for_combined + '/asia2.csv', index = False)
        test_data_3 = pd.DataFrame([['4.4.4.4', '6', '0'], ['4.4.4.2', '5', '10']], columns=['Source IP', 'Count', 'Events per Second'])
        test_data_3.to_csv(self.path_for_combined + '/na.csv', index = False)

    def test_location_doesnt_exists(self):
        self.assertFalse(EngineeringTest()._check_path(self.not_exists_path))

    def test_file_data_traverses_combine_dataframe(self):
        self.create_combined_test_folder()
        files = EngineeringTest()._get_all_csv_files(self.path_for_combined)
        df = EngineeringTest().file_data_traverses(files)
        EngineeringTest().generate_combined_csv(df)
        test_dataframe_data = pd.DataFrame({"Source IP": ["4.4.4.4", "4.4.4.2"], "Environment": ["asia", "asia"]})
        dataframe=pd.read_csv(self.path_for_combined + "/Output" +"/combined.csv" ,index_col=None)
        assert_frame_equal(test_dataframe_data, dataframe)

        



    