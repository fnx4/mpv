import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

core.num_threads = k7f.vs_thd_dft
clip = video_in

H_Pre = 720
Model = "the_database_AnimeJaNaiV3L2_sharp_HD_x2_fp16_op17.onnx" # https://github.com/hooke007/dotfiles/releases/download/onnx_models/the_database_AnimeJaNaiV3L2_sharp_HD_x2_fp16_op17.onnx
Fp16_Qnt = True
Gpu = 0
Gpu_T = 4
St_Eng = False
Res_Opt = [1280, 720]
Res_Max = [1920, 1200]
Ws_Size = 0
H_Max = 1440
Lk_Fmt = False

try:
    ret = k7f.FMT_CTRL(clip, h_max=1200, h_ret=True)
    clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
    clip = k7f.UAI_NV_TRT(clip, crc=False, model_pth=Model, opt_lv=3, cuda_opt=[0, 0, 0], int8_qnt=False, fp16_qnt=Fp16_Qnt, gpu=Gpu, gpu_t=Gpu_T, st_eng=St_Eng, res_opt=Res_Opt, res_max=Res_Max, ws_size=Ws_Size)
    clip = k7f.FMT_CTRL(clip, h_max=H_Max, fmt_pix=1 if Lk_Fmt else 0)

    clip.set_output()
except:
    pass