# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>
%global upstream_name sglang

# Upstream pyproject_cpu.toml requires torch==2.14.0, torchvision==0.29.0,
# triton==3.8.0, timm==1.0.16, xgrammar==0.2.7, llguidance>=1.7.6,<2.0.0, and
# mistral_common>=1.11.5.  This distribution ships torch, torchvision, and
# triton from the PyTorch stack it builds, and the grammar and tokenizer
# libraries at the versions owned by their upstream recipes.  %prep rewrites
# those requirements down to the versions that actually exist here; every
# lower pin below is a recorded deviation from the upstream requirement.
%global torch_full_version 2.13.0
%global torchvision_full_version 0.28.0
%global triton_full_version 3.7.1
%global timm_full_version 1.0.28

# pythondistdeps drops trailing zero components from distribution capabilities,
# so an exact pin on 2.13.0 has to be written as 2.13.
%global torch_cap_version 2.13
%global torchaudio_cap_version 2.11
%global torchvision_cap_version 0.28
%global torchcodec_cap_version 0.12

%global transformers_version 5.12.1
%global xgrammar_version 0.2.1
%global llguidance_min_version 1.7.5
%global mistral_common_min_version 1.11.3

# Keep the CUDA conditionals for a future provider-backed flavor.  This source
# package intentionally has no multibuild entry until a CUDA Torch provider is
# available; the default build must resolve to the CPU dependency closure.
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "cuda"
%{error:CUDA SGLang flavor is reserved and is not supported by this SPEC}
%endif
%if "%{flavor}" == "rocm"
%{error:ROCm SGLang flavor is reserved and is not supported by this SPEC}
%endif
%ifarch riscv64
%global llvm_maj_ver 22
%global toolchain clang
%global llvm_bindir %{_libdir}/llvm%{llvm_maj_ver}/bin
%endif

# Select the upstream platform metadata for each build flavor.
%if "%{flavor}" == "cuda"
%bcond cuda 1
%else
%bcond cuda 0
%endif

# Keep the ROCm flavor unbuildable even when a caller enables it directly
# instead of selecting BUILD_FLAVOR=rocm.
%if "%{flavor}" == "rocm"
%bcond rocm 1
%else
%bcond rocm 0
%endif

# Keep the reserved CUDA flavor unbuildable even when a caller overrides the
# bcond directly instead of selecting BUILD_FLAVOR=cuda.
%if %{with cuda}
%{error:CUDA SGLang flavor is reserved and is not supported by this SPEC}
%endif
%if %{with rocm}
%{error:ROCm SGLang flavor is reserved and is not supported by this SPEC}
%endif

%if %{with cuda}
%global srcname sglang
Name:           python-sglang-cuda
%else
%global srcname sglang-cpu
Name:           python-sglang
%endif
Version:        0.5.21
Release:        %autorelease
Summary:        Fast serving framework for large language and vision-language models
License:        Apache-2.0
URL:            https://github.com/sgl-project/sglang
VCS:            git:https://github.com/sgl-project/sglang.git
#!RemoteAsset:  sha256:c44951b7871dac61262fc04e9fca628175758a97fa5f603c522b31dc31b94249
Source0:        https://github.com/sgl-project/sglang/archive/refs/tags/v%{version}.tar.gz#/%{upstream_name}-%{version}.tar.gz
Source1:        sglang-launcher
Source2:        sglang-python-launcher
Source3:        sglang-cpu-engine-smoke.py
BuildSystem:    pyproject
%if %{without cuda}
# The upstream x86_64 metadata requests python3dist(intel-openmp), which this
# repository does not provide, and the CPU closure is validated only on
# RISC-V.  Keep x86_64 out until a real provider and target validation exist.
ExclusiveArch:  riscv64
%else
# CUDA toolkit currently provides Linux host support for these architectures.
ExclusiveArch:  x86_64 aarch64
%endif

BuildOption(prep):  -n %{upstream_name}-%{version}
BuildOption(install):  sglang
%if %{with cuda}
# The CUDA flavor is intentionally dormant until a CUDA Torch provider is
# added.
Conflicts:      python-sglang
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(torch) = %{torch_cap_version}
Requires:       python3dist(torch) = %{torch_cap_version}
%else
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(torch) = %{torch_cap_version}
BuildRequires:  python3dist(torchaudio) = %{torchaudio_cap_version}
BuildRequires:  python3dist(torchvision) = %{torchvision_cap_version}
BuildRequires:  python3dist(triton) = %{triton_full_version}
BuildRequires:  python3dist(sglang-kernel-cpu) = 0.4.7
BuildRequires:  python3dist(mistral-common) >= %{mistral_common_min_version}
BuildRequires:  python3dist(transformers) = %{transformers_version}
BuildRequires:  python3dist(xgrammar) = %{xgrammar_version}
BuildRequires:  python3dist(llguidance) >= %{llguidance_min_version}
BuildRequires:  python3dist(llguidance) < 2
%ifnarch aarch64 armv7hl
# pyproject_cpu.toml excludes torchcodec on Linux ARM (aarch64, arm64, armv7l).
BuildRequires:  python3dist(torchcodec) = %{torchcodec_cap_version}
%endif
%endif

%if %{without cuda}
Requires:       python3dist(torch) = %{torch_cap_version}
Requires:       python3dist(torchaudio) = %{torchaudio_cap_version}
Requires:       python3dist(torchvision) = %{torchvision_cap_version}
Requires:       python3dist(triton) = %{triton_full_version}
# The upstream CPU installation also builds the separate AOT kernel project.
Requires:       python3dist(sglang-kernel-cpu) = 0.4.7
# SGLang's CPU metadata imports Mistral tokenizer utilities at runtime.
Requires:       python3dist(mistral-common) >= %{mistral_common_min_version}
Requires:       python3dist(transformers) = %{transformers_version}
Requires:       python3dist(xgrammar) = %{xgrammar_version}
Requires:       python3dist(llguidance) >= %{llguidance_min_version}
Requires:       python3dist(llguidance) < 2
%ifnarch aarch64 armv7hl
Requires:       python3dist(torchcodec) = %{torchcodec_cap_version}
%endif
%endif

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%patchlist
# RISC-V torch-native runtime fallback and capability-gated unsupported AOT operators.
2002-riscv64-cpu-runtime-fallback.patch

%description
SGLang is a fast serving framework for large language models and vision-language
models.
%if %{with cuda}
This package provides the CUDA backend.
%else
This package provides the CPU backend.
%endif

%prep -a
cp README.md LICENSE python/
%if %{without cuda}
cp python/pyproject_cpu.toml python/pyproject.toml
# The source archive has no Git metadata.  Use a static project version for
# setuptools' wheel metadata so offline builds do not fall back to 0.0.0.
sed -i -e 's/^dynamic = \["version"\]/version = "%{version}"/' \
    python/pyproject.toml
sed -i \
    -e 's/"blobfile==3.0.0"/"blobfile>=3.2.0,<4"/' \
    -e 's/"openai==2.6.1"/"openai>=2.40.0,<3"/' \
    -e 's/"openai-harmony==0.0.4"/"openai-harmony>=0.0.8,<0.1"/' \
    -e 's/"torch==2.14.0"/"torch==%{torch_full_version}"/' \
    -e 's/"torchvision==0.29.0"/"torchvision==%{torchvision_full_version}"/' \
    -e 's/"triton==3.8.0"/"triton==%{triton_full_version}"/' \
    -e 's/"timm==1.0.16"/"timm==%{timm_full_version}"/' \
    -e 's/"xgrammar==0.2.7"/"xgrammar==%{xgrammar_version}"/' \
    -e 's/"llguidance>=1.7.6,<2.0.0"/"llguidance>=%{llguidance_min_version},<2.0.0"/' \
    -e 's/"mistral_common>=1.11.5"/"mistral_common>=%{mistral_common_min_version}"/' \
    python/pyproject.toml
# py-spy is only ever invoked as a subprocess by the crash-dump helper; no
# module imports it, so a missing profiler cannot break inference.  Its Rust
# dependency chain also needs macOS-only crates that the Linux system cargo
# registry does not carry, so it is not available here.  Drop the requirement
# rather than pin the whole stack on an unbuildable package.
sed -i -e '/^  "py-spy",$/d' python/pyproject.toml
%ifarch riscv64
sed -i '/intel-openmp.*platform_machine.*x86_64/d' python/pyproject.toml
%endif
%endif

%generate_buildrequires
cd python
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_SGLANG_CPU='%{version}'
%if %{without cuda}
export SGLANG_BUILD_RUST_EXTS=none
%endif
# The dependency closure is declared above; resolve the build backend only.
%pyproject_buildrequires -R

%build -p
cd python
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_SGLANG_CPU='%{version}'
%if %{without cuda}
# The CPU metadata has no Rust build requirement.  Keep this explicit so a
# future setup.py change cannot silently pull GPU/Rust extensions into RISC-V.
export SGLANG_BUILD_RUST_EXTS=none
%endif
%ifarch riscv64
# Select LLVM for native extensions. Cross-build sysroots are supplied externally.
export PATH="%{llvm_bindir}:$PATH"
export CC="%{llvm_bindir}/clang"
export CXX="%{llvm_bindir}/clang++"
export LD="%{llvm_bindir}/ld.lld"
export AR="%{llvm_bindir}/llvm-ar"
export RANLIB="%{llvm_bindir}/llvm-ranlib"
export CFLAGS="%{build_cflags} --target=%{_target_platform}"
export CXXFLAGS="%{build_cxxflags} --target=%{_target_platform}"
export LDFLAGS="-fuse-ld=lld --target=%{_target_platform} %{build_ldflags}"
%endif

%install -p
cd python

%install -a
# The declarative pass installs the wheel and records the module list from
# python/.  Relocate the upstream console entry point out of _bindir so the
# wrapper below can drop inherited Python and loader settings before starting
# the server.
mkdir -p %{buildroot}%{_libexecdir}/sglang
mv %{buildroot}%{_bindir}/sglang %{buildroot}%{_libexecdir}/sglang/sglang
install -Dpm0755 %{SOURCE1} %{buildroot}%{_bindir}/sglang
install -Dpm0755 %{SOURCE2} %{buildroot}%{_bindir}/sglang-python
%if %{without cuda}
install -Dpm0755 %{SOURCE3} %{buildroot}%{_libexecdir}/sglang/sglang-cpu-engine-smoke.py
%endif
sed -i \
  -e 's|@LIBEXEC@|%{_libexecdir}/sglang|g' \
  -e 's|@PYTHON3@|%{_bindir}/python3|g' \
  %{buildroot}%{_bindir}/sglang %{buildroot}%{_bindir}/sglang-python

%check
# The launchers are shell scripts that must stay syntactically valid.
for launcher in "%{buildroot}%{_bindir}/sglang" \
  "%{buildroot}%{_bindir}/sglang-python"; do
  bash -n "$launcher"
done
# sglang imports its whole runtime closure at load time, and those packages are
# runtime Requires rather than build dependencies.  Verify the installed
# distribution metadata and the prepped requirement pins instead of importing
# the package; the offline engine smoke test in sglang-cpu-engine-smoke.py is
# run manually against an installed system.
export PYTHONPATH="%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}"
%{python3} - <<'PY'
import importlib.metadata

for name in ("sglang-cpu", "sglang"):
    try:
        version = importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        continue
    assert version == "%{version}", (name, version)
    break
else:
    raise SystemExit("no sglang distribution metadata was installed")
PY
cd %{_builddir}/%{upstream_name}-%{version}/python
# Every pin that %prep rewrote has to name a version this distribution builds.
%{python3} - <<'PY'
import re
from pathlib import Path

text = Path("pyproject.toml").read_text(encoding="utf-8")
expected = {
    "torch": "==%{torch_full_version}",
    "torchvision": "==%{torchvision_full_version}",
    "triton": "==%{triton_full_version}",
    "timm": "==%{timm_full_version}",
    "xgrammar": "==%{xgrammar_version}",
}
for name, pin in expected.items():
    assert f'"{name}{pin}"' in text, f"{name} pin was not rewritten to {pin}"
for fragment in (
    '"llguidance>=%{llguidance_min_version},<2.0.0"',
    '"mistral_common>=%{mistral_common_min_version}"',
):
    assert fragment in text, f"missing rewritten requirement {fragment}"
assert not re.search(r'"(torch|torchvision|triton)==(2\.14\.0|0\.29\.0|3\.8\.0)"', text)
PY

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/sglang
%{_bindir}/sglang-python
# The wheel's console entry point is relocated into libexec and is invoked by
# the public wrapper above.
%{_libexecdir}/sglang/sglang
%if %{without cuda}
%{_libexecdir}/sglang/sglang-cpu-engine-smoke.py
%endif

%changelog
%autochangelog
