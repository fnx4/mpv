### rife v4 #! https://github.com/hooke007/MPV_lazy/blob/main/portable_config/vs/rife_std.vpy

import vapoursynth as vs
from vapoursynth import core

input = video_in
colorlv = input.get_frame(0).props._ColorRange
fmt_fin = input.format.id

FPS_num = 2
FPS_den = 1
GPU = 0
GPU_t = 2

if container_fps > 32 :
	raise Exception("EX_STD_1")

cut0 = core.misc.SCDetect(clip=input, threshold=0.2)

cut1 = cut0.resize.Bilinear(format=vs.RGBS, matrix_in_s="709")
cut2 = core.rife.RIFE(clip=cut1, model=9, factor_num=FPS_num, factor_den=FPS_den, gpu_id=GPU, gpu_thread=GPU_t, sc=True, skip=True, skip_threshold=60.0)

output = cut2.resize.Bilinear(format=fmt_fin, matrix_s="709", range=1 if colorlv==0 else None)

output.set_output()
