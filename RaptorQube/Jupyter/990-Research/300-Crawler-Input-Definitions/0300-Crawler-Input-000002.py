def InputData():
	import pandas as pd
	ipmport os

	dirname='../../../../100-DL/100-Raw-Zone/0100-External/100-Golden-Source/000005-Data-Source-F/'
	filename=''
	setsep='\t'

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