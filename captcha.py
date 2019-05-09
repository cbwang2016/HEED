import numpy as np
import pickle
import gzip

with open('captcha_kernels.pickle.gz','rb') as f:
    kernels=pickle.loads(gzip.decompress(f.read()))
sorted_kernels=list(sorted(kernels.items(),reverse=True,key=lambda x:x[1].sum()))

def check_kernel(kern,img):
    if kern.shape[1]<=img.shape[1]:
        img=img[:,:kern.shape[1]]
    else:
        kern=kern[:,:img.shape[1]]
    return np.all((img&kern)==kern)

def _detect(img,recognized,xpos):
    if recognized==4:
        return '',0
    
    ma_prio=-999
    best_txt=''
    for txt,kern in sorted_kernels:
        for offset in range(0,5):
            if check_kernel(kern,img[:,xpos+offset:]):
                cur_prio=kern.sum()
                nxt_txt,next_prio=_detect(img,recognized+1,xpos+offset+kern.shape[1]-3)
                if next_prio+cur_prio>ma_prio:
                    ma_prio=next_prio+cur_prio
                    best_txt=txt+nxt_txt
    
    return best_txt,ma_prio

def recognize(img:np.ndarray):
    assert img.shape==(22,58) and img.dtype==np.uint8
    return _detect((img<80)[:,4:],0,0)[0]

#import cv2
#ii=cv2.imread(f'data_raw/m2mL===bTJtTA==.jpg',0)
#print(detect(ii))