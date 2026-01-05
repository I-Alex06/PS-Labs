import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy.datasets import ascent, face
from scipy.fft import dctn, idctn
X = ascent()
X2 = face()
Q_jpeg = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
          [12, 12, 14, 19, 26, 28, 60, 55],
          [14, 13, 16, 24, 40, 57, 69, 56],
          [14, 17, 22, 29, 51, 87, 80, 62],
          [18, 22, 37, 56, 68, 109, 103, 77],
          [24, 35, 55, 64, 81, 104, 113, 92],
          [49, 64, 78, 87, 103, 121, 120, 101],
          [72, 92, 95, 98, 112, 100, 103, 99]])
def ex1(img=X,q=Q_jpeg,show=True,mse_calc=False):
    #1)
    new_rows = 8 - img.shape[0] % 8
    new_cols = 8 - img.shape[1] % 8
    if new_rows == 8:
        new_rows = 0
    if new_cols ==8:
        new_cols = 0
    x_pad = np.pad(img,((0,new_rows),(0,new_cols)), mode='edge')

    x_jpeg = np.zeros(x_pad.shape)
    y_nnz = 0
    y_jpeg_nnz = 0

    # Encoding
    for i in range(0, x_pad.shape[0],8):
        for j in range(0, x_pad.shape[1],8):
            x = x_pad[i:i+8, j:j+8]
            y = dctn(x,norm='ortho')
            y_jpeg = q*np.round(y/q)

            # Decoding
            x_jpeg_block = idctn(y_jpeg,norm='ortho')

            # Results
            x_jpeg[i:i+8, j:j+8] = x_jpeg_block
            y_nnz += np.count_nonzero(y)
            y_jpeg_nnz += np.count_nonzero(y_jpeg)

    x_jpeg = x_jpeg[:img.shape[0], :img.shape[1]]

    if show:
        plt.subplot(121).imshow(img, cmap=plt.cm.gray)
        plt.title('Original')
        plt.subplot(122).imshow(x_jpeg, cmap=plt.cm.gray)
        plt.title('JPEG')
        plt.show()

        print('\n\nEX1)\n\nComponente în frecvență:' + str(y_nnz) + 
            '\nComponente în frecvență după cuantizare: ' + str(y_jpeg_nnz))
    if mse_calc:
        mse=np.mean((img - x_jpeg)**2)
        return mse


def rgb2ycbcr(x):
    trans_matrix = np.array([[0.299,0.587,0.114],
                             [-0.168736,-0.331264,0.5],
                             [0.5,-0.418688,-0.081312]])
    ycbcr=x.dot(trans_matrix.T)
    ycbcr[:,:,[1,2]]+=128
    return np.clip(ycbcr,0,255)

def ycbcr2rgb(y):
    x=y.copy()
    x[:,:,[1,2]]-=128
    trans_matrix = np.array([[1,0,1.402],
                             [1,-0.344136,-0.714136],
                             [1,1.772,0]])
    rgb=x.dot(trans_matrix.T)
    return np.clip(rgb,0,255)

def procces_channel(channel,q=Q_jpeg):
    new_rows = 8 - channel.shape[0] % 8
    new_cols = 8 - channel.shape[1] % 8
    if new_rows == 8:
        new_rows = 0
    if new_cols ==8:
        new_cols = 0
    x_pad = np.pad(channel,((0,new_rows),(0,new_cols)), mode='edge')

    x_jpeg = np.zeros(x_pad.shape)
    y_nnz = 0
    y_jpeg_nnz = 0

    # Encoding
    for i in range(0, x_pad.shape[0],8):
        for j in range(0, x_pad.shape[1],8):
            x = x_pad[i:i+8, j:j+8]
            y = dctn(x,norm='ortho')
            y_jpeg = q*np.round(y/q)

            # Decoding
            x_jpeg_block = idctn(y_jpeg,norm='ortho')

            # Results
            x_jpeg[i:i+8, j:j+8] = x_jpeg_block
            y_nnz += np.count_nonzero(y)
            y_jpeg_nnz += np.count_nonzero(y_jpeg)

    x_jpeg = x_jpeg[:channel.shape[0], :channel.shape[1]]
    
    return x_jpeg, y_nnz, y_jpeg_nnz

def ex2(img=X2,q=Q_jpeg,show=True,mse_calc=False):
    #2)
    x2_ycbcr = rgb2ycbcr(img)
    y_channel, y_nnz_y, y_jpeg_nnz_y = procces_channel(x2_ycbcr[:,:,0],q)
    cb_channel, y_nnz_cb, y_jpeg_nnz_cb = procces_channel(x2_ycbcr[:,:,1],q)
    cr_channel, y_nnz_cr, y_jpeg_nnz_cr = procces_channel(x2_ycbcr[:,:,2],q)

    x2_ycbcr_jpeg = np.stack((y_channel, cb_channel, cr_channel), axis=2)
    x2_rgb_jpeg= ycbcr2rgb(x2_ycbcr_jpeg).astype(np.uint8)

    if show:
        plt.subplot(121).imshow(X2)
        plt.title('Original')
        plt.subplot(122).imshow(x2_rgb_jpeg)
        plt.title('JPEG')
        plt.show()

        print('\n\n\nEX2)\n\nY:\n   Componente în frecvență:' + str(y_nnz_y) + 
            '\n   Componente în frecvență după cuantizare: ' + str(y_jpeg_nnz_y))
        print('Cb:\n   Componente în frecvență:' + str(y_nnz_cb) + 
            '\n   Componente în frecvență după cuantizare: ' + str(y_jpeg_nnz_cb))
        print('Cr:\n   Componente în frecvență:' + str(y_nnz_cr) + 
            '\n   Componente în frecvență după cuantizare: ' + str(y_jpeg_nnz_cr))
        print('Total:\n   Componente în frecvență:' + str(y_nnz_y+y_nnz_cb+y_nnz_cr) + 
            '\n   Componente în frecvență după cuantizare: ' + str(y_jpeg_nnz_y+y_jpeg_nnz_cb+y_jpeg_nnz_cr))
    if mse_calc:
        mse=np.mean((img - x2_rgb_jpeg)**2)
        return mse

def ex3(target_mse,img=X2,color=None):
    print("\n\n\nEX3)\n\n")
    if color is None:
        if len(img.shape)==2:
            color=False
        elif len(img.shape)==3:
            color=True
        else:
            print("Error: img must be 2D or 3D np array")
            return -1
    tol=target_mse*0.01
    q_scale1=1.0
    if color == True:
        func=ex2
    elif color == False:
        func=ex1
    mse1=func(img,Q_jpeg*q_scale1,show=False,mse_calc=True)
    mse2=mse1
    q_scale2=q_scale1
    if mse2>target_mse:
        while mse2>target_mse:
            q_scale1=q_scale2
            q_scale2/=2
            mse1=mse2
            mse2=func(img,Q_jpeg*q_scale2,show=False,mse_calc=True)
            if q_scale2<0.001:
                print("Q scale too small")
                break
    elif mse2<target_mse:
        while mse2<target_mse:
            q_scale1=q_scale2
            q_scale2*=2
            mse1=mse2
            mse2=func(img,Q_jpeg*q_scale2,show=False,mse_calc=True)
            if q_scale2>10000:
                print("Q scale too big")
                break
    else:
        func(img,Q_jpeg*q_scale1)
        print("MSE found: ", mse1," Target MSE: ", target_mse, " Q scale: ", q_scale1)
        return
    q_min=np.min([q_scale1,q_scale2])
    q_max=np.max([q_scale1,q_scale2])
    mse_min=np.min([mse1,mse2])
    mse_max=np.max([mse1,mse2])
    mse1=mse_min
    mse2=mse_max
    mse=np.min([mse1,mse2])
    q_scale=q_min
    while(mse2 - mse1)>tol:
        q_mid=(q_min+q_max)/2
        mse_mid=func(img,Q_jpeg*q_mid,show=False,mse_calc=True)
        if mse_mid<target_mse:
            q_min=q_mid
            mse1=mse_mid
        elif mse_mid>target_mse:
            q_max=q_mid
            mse2=mse_mid
    if mse2<target_mse:
        mse=mse2
        q_scale=q_max
    elif mse1<target_mse:
        mse=mse1
        q_scale=q_min
    func(img,Q_jpeg*q_scale)
    print("MSE found: ", mse," Target MSE: ", target_mse, " Q scale: ", q_scale)



ex1()
ex2()
#TOLERANTA E 1% DIN TINTA, SE POATE MODIFICA
#PT COLOR SE MISCA MAI INCET DAR TOT GASESTE(NU SE BLOCHEAZA)
ex3(80)
ex3(300) #Q scale prea mare
ex3(3)
#PT MONO E MAI RAPID
ex3(6,X)
ex3(200,X)
ex3(0.0005,X) #Q scale prea mic
