import os
import pandas as pd
from glob import glob

#path to the folders and end of file to remove to get episodes name
def tsv_to_df(path, end):

    base_path = path
    tsv_files = sorted(glob(os.path.join(base_path, '**', '*.tsv'), recursive=True))
    all_data = []

    for file in tsv_files:

        df = pd.read_csv(file, sep='\t')

        # Extract episode name from filename
        episode = os.path.basename(file).replace( end, '')
        df['episode'] = episode

        all_data.append(df)

    # Combine all data into one dataframe for maxpeak
    df_final = pd.concat(all_data, ignore_index=True)

    return df_final

def tsv_to_df2(path):

    base_path = path
    tsv_files = sorted(glob(os.path.join(base_path, '**', '*.tsv'), recursive=True))
    all_data = []

    for file in tsv_files:

        df = pd.read_csv(file, sep='\t')


        all_data.append(df)

    # Combine all data into one dataframe for maxpeak
    df_final = pd.concat(all_data, ignore_index=True)

    return df_final
