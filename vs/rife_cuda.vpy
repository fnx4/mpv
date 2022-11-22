### rife v4 #! https://github.com/hooke007/MPV_lazy/blob/main/portable_config/vs/rife_cuda.vpy

import vapoursynth as vs
from vapoursynth import core
import math
from vsmlrt import RIFE, RIFEModel, Backend

input = video_in
colorlv = input.get_frame(0).props._ColorRange
fmt_fin = input.format.id

L_FHD = False
FPS_num = 3
GPU = 0
GPU_t = 4

if container_fps > 32 :
	raise Exception("EX_CUDA_1")
if not L_FHD and (input.width * input.height > 2073600) :
	raise Exception("EX_CUDA_2")

w_tmp = math.ceil(input.width / 32) * 32 - input.width
h_tmp = math.ceil(input.height / 32) * 32 - input.height

cut0 = core.misc.SCDetect(clip=input, threshold=0.2)

cut1 = cut0.resize.Bilinear(format=vs.RGBS, matrix_in_s="709")
cut2 = cut1.std.AddBorders(right=w_tmp, bottom=h_tmp)
cut3 = RIFE(clip=cut2, multi=FPS_num, model=RIFEModel.v4_6, backend=Backend.TRT(fp16=True, device_id=GPU, use_cuda_graph=True, num_streams=GPU_t))
fin = cut3.std.Crop(right=w_tmp, bottom=h_tmp)

output = fin.resize.Bilinear(format=fmt_fin, matrix_s="709", range=1 if colorlv==0 else None)
output.set_output()
