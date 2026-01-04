import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

Gpu = 0
Gpu_T = 4
St_Eng = False
Ws_Size = 0
Lk_Fmt = False

Lt_D2k = False
Model_RIFE = 40
Sc_Mode = 1
Fps_Num = 2
T_Tta = False
Ext_Proc = True

Lt_Hd = False
Model_ESRGAN = 5005
H_Pre = 720

try:
    ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
    clip = k7f.RIFE_NV(clip, lt_d2k=Lt_D2k, model=Model_RIFE, sc_mode=Sc_Mode, fps_num=Fps_Num, t_tta=T_Tta, ext_proc=Ext_Proc, gpu=Gpu, gpu_t=Gpu_T, st_eng=St_Eng, ws_size=Ws_Size)
    clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
    clip = k7f.ESRGAN_NV(clip, lt_hd=Lt_Hd, model=Model_ESRGAN, scale=4 if Model_ESRGAN == 2 else 2, gpu=Gpu, gpu_t=Gpu_T, st_eng=St_Eng, ws_size=Ws_Size)

    clip.set_output()
except Exception:
    pass