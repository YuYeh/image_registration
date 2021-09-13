import os
import shutil
import subprocess

ICG_PATH = 'ICG/'
FA_PATH = 'FA/'

EDDPICP_PATH = 'EDDBICP/' 
SAVE_PATH = 'output/'

def do_eddbicp(img_dir = FA_PATH,icg_dir = ICG_PATH,eddpicp_path = EDDPICP_PATH,save_dir = SAVE_PATH):
    
    folder_dir = os.listdir(img_dir)
    for folder in folder_dir:
        if os.path.isdir(icg_dir+ folder):
            if not os.path.isdir(os.path.join(save_dir,folder,'imgs')):
                os.makedirs(os.path.join(save_dir,folder,'imgs'))      
            print('=' * 38, 'Move file start!', '=' * 38)
            print(f'Moved BVN.png to {eddpicp_path}')
            #  把ICG ground truth和的影像移動到eddbicp code資料夾內
            shutil.copyfile(icg_dir+ folder + '/BVN.png', eddpicp_path + 'BVN.png')
            shutil.copyfile(icg_dir+ folder + '/PCV.png', eddpicp_path + 'PCV.png')
            
            #  把FA(ICG)五個時間點的影像移動到eddbicp code資料夾內
            file_dir = sorted(os.listdir(img_dir + folder),key = lambda i:len(i))
            for name in file_dir:
                print(f'Moved {name} to {eddpicp_path}')
                shutil.copyfile(img_dir + folder + '/' + name, eddpicp_path + name)
            print('=' * 39, 'Move file end!', '=' * 39)
            
            print('=' * 32, 'ED_DBICP Starting(GT to FA)!', '=' * 32)

            # 創建/複寫 do_eddbicp.bat (影像命名: folder_i.png, i=1~5)
            fp = open("do_eddbicp.bat","w")
            fp.write("cd EDDBICP\n")
            fp.write(f"for /l %%i in (1,1,5) do ed_dbicp.exe BVN.png  {folder}_%%i.png -model 2 -xform_as_to -gm\n")
            fp.write(f"for /l %%i in (1,1,5) do ed_dbicp.exe PCV.png xto_BVN_to_{folder}_%%i.png  -model 2 -xform_as_to -gm\n")
            fp.close()
            
            
            print("Overwriting do_eddbicp.bat")
            
            # 執行do_eddbicp.bat
            print('=' * 37, 'ED_DBICP Starting!', '=' * 37)
            print(os.popen('do_eddbicp.bat').read())
            print('=' * 38, 'ED_DBICP Ending!', '=' * 38, '\n')
            
            #  把套合過的FA(ICG)第一個時間點的影像移動到segmentation_gt資料夾(如果有套合成功,也就是有產生檔案的話)
            print('=' * 34, 'Move result files start!', '=' * 34)
            
            count = 0
            for name in file_dir:    
                bvn_fn = f'xto_BVN_to_{name}'
                pcv_fn = f'xto_PCV_to_{bvn_fn}'
                if os.path.isfile(eddpicp_path + bvn_fn):
                    print(f'  Moved {bvn_fn} to {SAVE_PATH + folder}')
                    print(f'Renamed {bvn_fn} to {name.split(".")[0]}_BVN.png')
                    try:
                        os.rename(eddpicp_path + bvn_fn, os.path.join(SAVE_PATH,folder,f'imgs/{name.split(".")[0]}_BVN.png'))
                    except FileExistsError:
                        print(f'{name.split(".")[0]}_BVN.png is exist')
                    count += 1
                else:
                    print(f'File {bvn_fn} does not exist!\n')
                if os.path.isfile(eddpicp_path + pcv_fn):
                    print(f'  Moved {pcv_fn} to {SAVE_PATH + folder}')
                    print(f'Renamed {pcv_fn} to {name.split(".")[0]}_PCV.png\n')
                    try:
                        os.rename(eddpicp_path + pcv_fn, os.path.join(SAVE_PATH,folder,f'imgs/{name.split(".")[0]}_PCV.png'))
                    except FileExistsError:
                        print(f'{name.split(".")[0]}_PCV.png is exist')
                    count += 1
                else:
                    print(f'File {pcv_fn} does not exist!\n')
                    
            print('=' * 35, 'Move result files end!', '=' * 35, '\n')

            
            if count < 10:
                os.rename(SAVE_PATH + folder, SAVE_PATH + folder + '(套合失敗)')
                
        else:
            print(f'Folder {folder} does not exist!\n')
    

def main():
    do_eddbicp()
       
if __name__ =='__main__':
    main()