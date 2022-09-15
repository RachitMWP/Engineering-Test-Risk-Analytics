import os

import unittest
import pandas as pd

from src.main import EngineeringTest

DIR_PATH  = "Engineering Test Files"
TEST_DIR  = 'test' 


class CombinedCSV_testing(unittest.TestCase):

    def test_file_data_traverses_column(self):
        temporary_df = pd.DataFrame({"Source IP": ["0.0.0.0","0.0.0.111"], "Environment": ["NA Prod", "Asia prod"]})
        obj = EngineeringTest()
        files_csv = obj._get_all_csv_files('Engineering Test Files')
        main_df = obj.file_data_traverses(files_csv)
        self.assertTrue(tuple(temporary_df.columns), tuple(main_df.columns))
        self.assertIsNotNone(main_df['Source IP'].values[1])
        self.assertIsNotNone(main_df['Environment'].values[1])

        



    