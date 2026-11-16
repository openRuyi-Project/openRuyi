# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>
%global srcname torchcodec

# TorchCodec is packaged only for the validated SGLang CPU provider.  CUDA and
# ROCm flavors are reserved until matching providers and target validation are
# available; keep them from silently resolving to the CPU dependency.
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "cuda"
%bcond cuda 1
%else
%bcond cuda 0
%endif
%if "%{flavor}" == "rocm"
%bcond rocm 1
%else
%bcond rocm 0
%endif

# Keep reserved accelerator flavors unbuildable when a caller enables a bcond
# directly instead of selecting the corresponding BUILD_FLAVOR.
%if %{with cuda}
%{error:CUDA SGLang TorchCodec flavor is reserved and is not supported by this SPEC}
%endif
%if %{with rocm}
%{error:ROCm SGLang TorchCodec flavor is reserved and is not supported by this SPEC}
%endif

# pythondistdeps drops trailing zero components from distribution capabilities,
# so an exact pin on 2.13.0 has to be written as 2.13.
%global torch_cap_version 2.13

%ifarch riscv64
%global llvm_maj_ver 22
%global toolchain clang
%global llvm_bindir %{_libdir}/llvm%{llvm_maj_ver}/bin
%endif

Name:           python-%{srcname}
Version:        0.12.0
Release:        %autorelease
Summary:        PyTorch video decoding and encoding library
License:        BSD-3-Clause
URL:            https://github.com/meta-pytorch/torchcodec
VCS:            git:https://github.com/meta-pytorch/torchcodec.git
#!RemoteAsset:  sha256:f0cc21c1f99439cff30eb43080e9bc8e43c6b9505b4f327cb42ee132075bcec4
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject
# The CPU Torch/SGLang closure is currently validated only on RISC-V.
ExclusiveArch:  riscv64

BuildOption(install):  -l %{srcname}

%ifarch riscv64
BuildOption(build):  -Ccmake.define.CMAKE_C_COMPILER=%{llvm_bindir}/clang
BuildOption(build):  -Ccmake.define.CMAKE_CXX_COMPILER=%{llvm_bindir}/clang++
BuildOption(build):  -Ccmake.define.CMAKE_C_COMPILER_TARGET:STRING=%{_target_platform}
BuildOption(build):  -Ccmake.define.CMAKE_CXX_COMPILER_TARGET:STRING=%{_target_platform}
%if "%{_host_cpu}" != "%{_target_cpu}"
BuildOption(build):  -Ccmake.define.CMAKE_SYSTEM_NAME=Linux
BuildOption(build):  -Ccmake.define.CMAKE_SYSTEM_PROCESSOR=riscv64
%endif
%endif

BuildRequires:  cmake
BuildRequires:  patchelf
%ifarch riscv64
BuildRequires:  clang
BuildRequires:  clang(major) = %{llvm_maj_ver}
BuildRequires:  compiler-rt(major) = %{llvm_maj_ver}
BuildRequires:  lld(major) = %{llvm_maj_ver}
BuildRequires:  llvm(major) = %{llvm_maj_ver}
BuildRequires:  libstdc++-devel
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  ffmpeg-devel%{?_isa} >= 4
BuildRequires:  ffmpeg-devel%{?_isa} < 9
# Upstream expects fmt to be bundled in PyTorch's include directory and builds
# it in header-only mode.  This distribution's PyTorch does not install those
# headers, so the library must come from the system copy instead.
BuildRequires:  fmt-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(python3)
BuildRequires:  file
BuildRequires:  pkgconfig(pybind11)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python-rpm-macros
# TorchCodec includes PyTorch headers, so it builds against the runtime rather
# than a pinned release.  Torch installs its CMake package files in -devel.
BuildRequires:  python-torch-devel
BuildRequires:  python3dist(torch) = %{torch_cap_version}
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Requires:       ffmpeg%{?_isa} >= 4
Requires:       ffmpeg%{?_isa} < 9
Requires:       python3dist(torch) = %{torch_cap_version}

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3dist(torchcodec) = %{version}
%python_provide python3-%{srcname}

%description
TorchCodec provides PyTorch bindings for decoding and encoding audio and video
with the system FFmpeg libraries.

%prep
%setup -q -n %{srcname}-%{version}
# Upstream's version.txt carries a pre-release suffix ("0.12.0a0") that does not
# match the release version this package ships.  Pin it so the installed
# distribution metadata and the RPM EVR agree, otherwise the automatic
# python3.*dist(torchcodec) capability disagrees with the explicit Provides.
echo '%{version}' > version.txt

%generate_buildrequires
%pyproject_buildrequires -R

%build -p
# The build links to the system FFmpeg package instead of downloading or
# bundling an FFmpeg build.  TorchCodec asks downstream distributors to make
# this licensing decision explicitly when producing a wheel.
export I_CONFIRM_THIS_IS_NOT_A_LICENSE_VIOLATION=1
export ENABLE_CUDA=0
export TORCHCODEC_DISABLE_COMPILE_WARNING_AS_ERROR=ON
%ifarch riscv64
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

%install -a
# The extension resolves torch's shared libraries in the same site-packages
# tree at runtime. Record relative entries so the module is found without
# depending on a loader cache entry for an installed environment.
for so in $(find %{buildroot}%{python3_sitearch} -type f -name '*.so*'); do
  if file "$so" | grep -q 'ELF'; then
    patchelf --set-rpath '$ORIGIN:$ORIGIN/../torch/lib' "$so"
  fi
done

# The bundled libtorchcodec_* objects are internal backend libraries that the
# package loads with ctypes; they export no PyInit_ symbol and must not be
# imported as extension modules.
%check
%pyproject_check_import -e 'torchcodec.libtorchcodec_*'
PYTHONPATH="%{buildroot}%{python3_sitearch}:" \
%{python3} - <<'PY'
from torchcodec._core import get_ffmpeg_library_versions

versions = get_ffmpeg_library_versions()
assert versions["ffmpeg_version"]
PY

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
