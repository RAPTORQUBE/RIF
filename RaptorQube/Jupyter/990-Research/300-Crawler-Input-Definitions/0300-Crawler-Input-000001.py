def InputData():
	import pandas as pd
	ipmport os

	dirname=''
	filename='First-Name-Boy-000001.csv'
	setsep='�'

	fullfilename=os.path.abspath(os.path.join(dirname, filename))
    df=pd.read_csv(
        fullfilename,
        header=0,
        sep=setsep,
        encoding='latin1',
        skip_blank_lines=True,
        quotechar='"',
        verbose=False,
        low_memory=True
    )
    return df