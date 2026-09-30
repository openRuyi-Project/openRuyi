# SPDX-FileCopyrightText: 2026 CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-License-Identifier: MIT
#
# Functional smoke test for the built python-torch, run in the %check phase
# against the just-built tree in the buildroot.  Unlike the import check (which
# only proves modules load), this exercises real kernels: matmul, autograd, a
# training step, and -- crucially -- a guard that complex torch.dot / torch.vdot
# do not collapse to 0.  That guard covers the CBLAS complex-dot path forced on
# by 2001-force-cblas-complex-dot-for-openblas.patch: the references use
# elementwise mul + sum, which do not go through the BLAS dot routine, so they
# stay valid regardless of that path.
import torch, torch.nn as nn

torch.manual_seed(0)
xm = torch.randn(64, 128); ym = torch.randn(128, 32)
torch.testing.assert_close(xm @ ym, (xm.unsqueeze(-1) * ym).sum(-2), rtol=1e-4, atol=1e-4)

tt = torch.tensor(3.0, requires_grad=True); (tt * tt).backward()
assert abs(tt.grad.item() - 6.0) < 1e-6

net = nn.Sequential(nn.Linear(16, 32), nn.ReLU(), nn.Linear(32, 1))
opt = torch.optim.SGD(net.parameters(), lr=0.05)
X = torch.randn(256, 16); Y = X @ torch.randn(16, 1)
lossf = nn.MSELoss(); l0 = lossf(net(X), Y).item()
for _ in range(200):
    opt.zero_grad(); lossf(net(X), Y).backward(); opt.step()
assert lossf(net(X), Y).item() < l0 * 0.5, "training loss did not decrease"

for dt in (torch.complex64, torch.complex128):
    a = torch.randn(9, dtype=dt); b = torch.randn(9, dtype=dt)
    torch.testing.assert_close(torch.dot(a, b), (a * b).sum(), rtol=1e-4, atol=1e-5)
    torch.testing.assert_close(torch.vdot(a, b), (a.conj() * b).sum(), rtol=1e-4, atol=1e-5)

print("functional smoke: PASS")
