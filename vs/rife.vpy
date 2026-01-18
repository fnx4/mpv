import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

core.num_threads = k7f.vs_thd_dft
clip = video_in

H_Pre = 1440
Model = 46
Fps_Num = 3
Fps_Den = 1
Sc_Mode = 1
Gpu = 0
Gpu_T = 4
Ws_Size = 0
Lk_Fmt = False

try:
    ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
    clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
    clip = k7f.RIFE_NV(clip, model=Model, int8_qnt=False, turbo=True, fps_in=container_fps, fps_num=Fps_Num, fps_den=Fps_Den, sc_mode=Sc_Mode, gpu=Gpu, gpu_t=Gpu_T, ws_size=Ws_Size)

    clip.set_output()
except:
    pass