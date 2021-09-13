cd F:\Ophthalmic\segmentation\code\EDDBICP
for /l %%i in (1,1,5) do ed_dbicp.exe BVN.png  0142_05_%%i.png -model 2 -xform_as_to -gm
for /l %%i in (1,1,5) do ed_dbicp.exe PCV.png xto_BVN_to_0142_05_%%i.png  -model 2 -xform_as_to -gm
