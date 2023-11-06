import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

H_Pre = 720
Lt_Hd = False
Model = 5006
Gpu = 0
Gpu_T = 4
St_Eng = False
Ws_Size = 0
H_Max = 1440
Lk_Fmt = False

ret = k7f.FMT_CTRL(clip, h_max=1200, h_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.ESRGAN_NV(clip, lt_hd=Lt_Hd, model=Model, scale=4 if Model==2 else 2, gpu=Gpu, gpu_t=Gpu_T, st_eng=St_Eng, ws_size=Ws_Size)
clip = k7f.FMT_CTRL(clip, h_max=H_Max, fmt_pix=1 if Lk_Fmt else 0)

clip.set_output()
