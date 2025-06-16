## friends_pack

# Description

This package contains two modules, friendsTSV and boolean friends plotter.

# friendsTSV

This module contains 2 functions that do basically the same thing.

**tsv to df** : this function takes the base path of the dataset and the ending of the name of
the file (i.e the dataset name)

this function loads all tsv and concatenates them into a pandas dataframe. This also adds
an episode column (i.e the episode comes from the name of the file hence why we removed the 
ending of the filename.)

**tsv to df 2**: does the same thing as the first function but doesn<t create an episode
column. This function is useful for datasets already containing the episode column

# boolean friends plotter

This module contains one function.

**boolean true plotter**: This function is useful for dataset with columns containing
booleans. This function counts and plots a distribution of the segments that are labelled as
True. This function takes 4 arguments, the dataframe you want to use, the columns you want,
the title of the plot, the name of the x, and the name of the y.
