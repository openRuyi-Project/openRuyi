# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>

"""Run deterministic smoke checks against the built sgl_kernel extension."""

import multiprocessing
import os
import time
import traceback
from pathlib import Path

import torch
import sgl_kernel  # noqa: F401  # Registers torch.ops.sgl_kernel.


def _tp2_rank(rank, port):
    try:
        os.environ["LOCAL_SIZE"] = "2"
        os.environ["MASTER_ADDR"] = "127.0.0.1"
        os.environ["MASTER_PORT"] = str(port)
        ops = torch.ops.sgl_kernel
        ops.initialize(2, rank)
        cases = (("float32", torch.float32), ("float16", torch.float16))
        if hasattr(torch, "bfloat16"):
            cases += (("bfloat16", torch.bfloat16),)
        # Include small, chunk-boundary, and non-divisible tail sizes.
        for _, dtype in cases:
            for size in (1, 7, 4095, 4096, 4097, 100003):
                for iteration in range(3):
                    values = torch.arange(size, dtype=torch.float32).mul_(0.125)
                    data = values.add((rank + 1) * 64.0 + iteration * 0.25).to(dtype)
                    peer = values.add((2 - rank) * 64.0 + iteration * 0.25).to(dtype)
                    expected = (data.float() + peer.float()).to(dtype).float()
                    ops.shm_allreduce(data, 0)
                    torch.testing.assert_close(
                        data.float(), expected, rtol=1.0e-5, atol=1.0e-5
                    )
    except BaseException:
        traceback.print_exc()
        raise


def _run_tp2():
    timeout = int(os.environ.get("SGLANG_KERNEL_SMOKE_TIMEOUT", "90"))
    if timeout <= 0:
        raise ValueError("SGLANG_KERNEL_SMOKE_TIMEOUT must be a positive integer")
    port = 20000 + (os.getpid() % 30000)
    addr = "127.0.0.1"
    prefix = f"deepspeed_allreduce_buffer_{os.getuid()}_{addr}_{port}_"
    paths = [Path("/dev/shm") / f"{prefix}{rank}" for rank in range(2)]
    for path in paths:
        path.unlink(missing_ok=True)
    context = multiprocessing.get_context("spawn")
    processes = [context.Process(target=_tp2_rank, args=(rank, port)) for rank in range(2)]
    try:
        for process in processes:
            process.start()
        deadline = time.monotonic() + timeout
        for process in processes:
            process.join(max(0.0, deadline - time.monotonic()))
        if any(process.is_alive() for process in processes):
            for process in processes:
                if process.is_alive():
                    process.terminate()
            for process in processes:
                process.join(10)
            raise RuntimeError("TP=2 smoke test timed out")
        failed = [process.exitcode for process in processes if process.exitcode != 0]
        if failed:
            raise RuntimeError(f"TP=2 smoke test failed with exit codes {failed}")
    finally:
        for process in processes:
            if process.is_alive():
                process.terminate()
                process.join(10)
        for path in paths:
            path.unlink(missing_ok=True)


def main():
    ops = torch.ops.sgl_kernel
    required = ("rmsnorm_cpu", "silu_and_mul_cpu", "initialize", "shm_allreduce")
    missing = [name for name in required if not hasattr(ops, name)]
    if missing:
        raise RuntimeError(f"sgl_kernel is missing required CPU operators: {missing}")

    # Upstream dispatches these kernels only for Half and BFloat16. Compare
    # both formats with float32 reference calculations and format tolerances.
    for dtype, tolerance in ((torch.float16, 1.0e-3), (torch.bfloat16, 1.0e-2)):
        x = torch.tensor([[-1.0, 2.0, -3.0, 4.0]], dtype=dtype)
        weight = torch.tensor([0.5, 1.0, 1.5, 2.0], dtype=dtype)
        eps = 1.0e-5
        got_norm = ops.rmsnorm_cpu(x, weight, eps)
        ref_x = x.float()
        ref_norm = ref_x * torch.rsqrt(ref_x.square().mean(dim=-1, keepdim=True) + eps)
        ref_norm = ref_norm * weight.float()
        torch.testing.assert_close(
            got_norm.float(), ref_norm, rtol=tolerance, atol=tolerance
        )

        gate_up = torch.tensor(
            [[-1.0, 2.0, -3.0, 4.0, 2.0, -3.0, 4.0, 5.0]], dtype=dtype
        )
        got_silu = ops.silu_and_mul_cpu(gate_up)
        split = gate_up.shape[-1] // 2
        ref_input = gate_up.float()
        ref_silu = torch.nn.functional.silu(ref_input[..., :split]) * ref_input[..., split:]
        torch.testing.assert_close(
            got_silu.float(), ref_silu, rtol=tolerance, atol=tolerance
        )

    _run_tp2()
    print(f"sgl_kernel CPU smoke passed with torch {torch.__version__}")


if __name__ == "__main__":
    main()
