import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

H_Pre = 1440
Lt_D2k = False
Model = 40
Sc_Mode = 1
Fps_Num = 3
T_Tta = False
Ext_Proc = True
Gpu = 0
Gpu_T = 4
St_Eng = False
Ws_Size = 0
Lk_Fmt = False

try:
    ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
    clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
    clip = k7f.RIFE_NV(clip, lt_d2k=Lt_D2k, model=Model, sc_mode=Sc_Mode, fps_num=Fps_Num, t_tta=T_Tta, ext_proc=Ext_Proc, gpu=Gpu, gpu_t=Gpu_T, st_eng=St_Eng, ws_size=Ws_Size)

    clip.set_output()
except:
    pass
