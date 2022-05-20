import numpy as np, cv2


def print_matInFo(name,image):
    if image.dtype == 'uint8':   mat_type = "CV_8U"
    elif image.dtype == 'int8': mat_type = "CV_8S"
    elif image.dtype == 'uint16':   mat_type = "CV_16U"
    elif image.dtype == 'int16':    mat_type = "CV_16S"
    elif image.dtype == 'float32':  mat_type = "CV_32F"
    elif image.dtype == 'float64':  mat_type = "CV_64F"
    nchannel = 3 if image.ndim == 3 else 1

    print("%12s: depth(%s), channels(%s) -> mat_type(%sC%d)"
          % (name,image.dtype,nchannel,mat_type,nchannel))
def put_string(frame,text,pt,value, color =(120,200,90)):
    text += str(value)
    shade = (pt[0]+2, pt[1]+2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,text,shade,font,0.7,(0,0,0),2)
    cv2.putText(frame, text, pt, font, 0.7, (120, 200, 90), 2)

def contain(p,shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

def time_cheak(func, image, size, title):
    start_time = time.perf_counter()
    ret_img = func(image,size)
    elapsed = (time.perf_counter() - start_time) * 1000
    print("%s elapesd time = %0.02f ms" % (title, elapsed))
    return ret_img