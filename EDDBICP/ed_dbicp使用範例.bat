REM ed_dbicp.exe img8.png img1.png  -model 2 -xform_as_to -gm


REM for /l %%i in (1,1,5) do ed_dbicp.exe %%i.png  0141_03_5.png -model 2 -xform_as_to -gm

REM ed_dbicp.exe PCV.png 0101_03_2.png  -model 2 -xform_as_to -gm
REM ed_dbicp.exe 1.png 0101_11_4.png  -model 2 -xform_as_to -gm

ed_dbicp.exe PCV.png xto_1_to_0101_11_4.png  -model 2 -xform_as_to -gm
ed_dbicp.exe BVN.png xto_PCV_to_xto_3_to_0101_11_4.png  -model 2 -xform_as_to -gm

REM ed_dbicp.exe BVN.png xto_1_to_0101_11_4.png  -model 2 -xform_as_to -gm
REM ed_dbicp.exe PCV.png xto_BVN_to_xto_1_to_0101_11_4.png  -model 2 -xform_as_to -gm




REM ed_dbicp.exe BVN.png 0101_03_1.png  -model 2 -xform_as_to -gm
REM ed_dbicp.exe PCV.png 0101_03_1.png  -model 2 -xform_as_to -gm

REM ed_dbicp.exe BVN.png xto_PCV_to_0101_03_1.png  -model 2 -xform_as_to -gm
REM ed_dbicp.exe PCV.png xto_BVN_to_0101_03_1.png  -model 2 -xform_as_to -gm


REM for /l %%i in (1,1,5) do ed_dbicp.exe PCV.png  xto_BVN_to_xto_2_to_0121_03_%%i.png -model 2 -xform_as_to -gm