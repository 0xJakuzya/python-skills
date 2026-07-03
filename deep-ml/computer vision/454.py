import numpy as np

def compute_video_generation_fps(
    num_chunks: int,
    chunk_frames: int,
    denoising_steps: int,
    time_per_step_ms: float,
    context_encoding_ms: float = 0.0,
    realtime_fps_threshold: float = 24.0
) -> dict:
    """
    Calculate end-to-end FPS for an autoregressive video generation pipeline.

    Args:
        num_chunks: Number of video chunks to generate.
        chunk_frames: Frames per chunk.
        denoising_steps: Diffusion denoising steps per chunk.
        time_per_step_ms: Milliseconds per denoising step.
        context_encoding_ms: Extra overhead per chunk for history encoding (ms).
        realtime_fps_threshold: FPS at or above which generation is real-time.

    Returns:
        Dictionary with keys: total_frames, total_time_ms, total_time_s,
        fps, time_per_chunk_ms, is_realtime.
    """
    result = {}

    is_realtime = False

    total_frames = chunk_frames * num_chunks
    time_per_chunk_ms = time_per_step_ms * denoising_steps + context_encoding_ms
    total_time_ms = time_per_chunk_ms * num_chunks
    total_time_s = round(total_time_ms * 10**(-3) , 2)
    fps = total_frames / total_time_s
    
    if fps >= realtime_fps_threshold:
        is_realtime = True

    result.update(
        total_frames=total_frames,
        total_time_ms=total_time_ms,
        total_time_s=total_time_s,
        fps=round(fps, 2), 
        time_per_chunk_ms=time_per_chunk_ms, 
        is_realtime=is_realtime,
    )

    return result

print(compute_video_generation_fps(5, 24, 3, 50.0, context_encoding_ms=10.0))