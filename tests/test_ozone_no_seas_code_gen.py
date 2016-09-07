import pandas as pd
import numpy as np
import AutoForecast as autof
import Bench.TS_datasets as tsds
import TS_CodeGen_Objects as tscodegen

#get_ipython().magic('matplotlib inline')

b1 = tsds.load_ozone()
df = b1.mPastData

#df.tail(10)
#df[:-10].tail()
#df[:-10:-1]
#df.describe()



H = b1.mHorizon;

N = df.shape[0];
for n in range(N,  N+1 , 10):
    df1 = df.head(n).copy();
    lAutoF = autof.cAutoForecast()
    lAutoF
    lAutoF.mOptions.mEnableSeasonals = False;
    lAutoF.mOptions.mDebugCycles = True;
    lAutoF.mOptions.mCycle_Criterion_Threshold = 20000;
    lAutoF.train(df1 , b1.mTimeVar , b1.mSignalVar, H);
    lAutoF.getModelInfo();
    lAutoF.mSignalDecomposition.mBestTransformation.mTimeInfo.mResolution
    lCodeGenerator = tscodegen.cDecompositionCodeGenObject();
    lSQL = lCodeGenerator.testGeneration(lAutoF);