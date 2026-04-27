# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname paddlepaddle

Name:           python-%{srcname}
Version:        3.3.0
Release:        %autorelease
Summary:        Deep learning framework for machine learning
License:        Apache-2.0
URL:            https://www.paddlepaddle.org.cn/
VCS:            git:https://github.com/PaddlePaddle/Paddle
# PyPI 3.3.0 publishes wheels only (no sdist), so Source0 uses upstream tag tarball.
#!RemoteAsset:  git+https://github.com/PaddlePaddle/Paddle.git#cbf3469113cd76b7d5f4cba7b8d7d5f55d9e9911
#!CreateArchive
Source0:        %{srcname}-%{version}.tar.gz
#!RemoteAsset:  git+https://github.com/protocolbuffers/protobuf.git#f0dc78d7e6e331b8c6bb2d5283e06aa26883ca7c
#!CreateArchive
Source1:        submodule-01-protobuf.tar.gz
#!RemoteAsset:  git+https://gitlab.mpcdf.mpg.de/mtr/pocketfft.git#ea778e37710c07723435b1be58235996d1d43a5a
#!CreateArchive
Source2:        submodule-02-pocketfft.tar.gz
#!RemoteAsset:  git+https://github.com/gflags/gflags.git#e171aa2d15ed9eb17054558e0b3a6a413bb01067
#!CreateArchive
Source3:        submodule-03-gflags.tar.gz
#!RemoteAsset:  git+https://github.com/ziyoujiyi/gloo.git#8b6b61dfa0dca02b226a01262bfcf0484382048f
#!CreateArchive
Source4:        submodule-04-gloo.tar.gz
#!RemoteAsset:  git+https://github.com/dmlc/dlpack.git#93c8f2a3c774b84af6f652b1992c48164fae60fc
#!CreateArchive
Source5:        submodule-05-dlpack.tar.gz
#!RemoteAsset:  git+https://github.com/JuliaStrings/utf8proc.git#3203baa7374d67132384e2830b2183c92351bffc
#!CreateArchive
Source6:        submodule-06-utf8proc.tar.gz
#!RemoteAsset:  git+https://github.com/baidu-research/warp-ctc.git#bdc2b4550453e0ef2d3b5190f9c6103a84eff184
#!CreateArchive
Source7:        submodule-07-warpctc.tar.gz
#!RemoteAsset:  git+https://github.com/PaddlePaddle/warp-transducer.git#7ea6bfe748779c245a0fcaa5dd9383826273eff2
#!CreateArchive
Source8:        submodule-08-warprnnt.tar.gz
#!RemoteAsset:  git+https://github.com/Cyan4973/xxHash.git#7cc9639699f64b750c0b82333dced9ea77e8436e
#!CreateArchive
Source9:        submodule-09-xxhash.tar.gz
#!RemoteAsset:  git+https://github.com/pybind/pybind11.git#a2e59f0e7065404b44dfe92a28aca47ba1378dc4
#!CreateArchive
Source10:        submodule-10-pybind.tar.gz
#!RemoteAsset:  git+https://github.com/progschj/ThreadPool.git#9a42ec1329f259a5f4881a291db1dcb8f2ad9040
#!CreateArchive
Source11:        submodule-11-threadpool.tar.gz
#!RemoteAsset:  git+https://github.com/madler/zlib.git#51b7f2abdade71cd9bb0e7a373ef2610ec6f9daf
#!CreateArchive
Source12:        submodule-12-zlib.tar.gz
#!RemoteAsset:  git+https://github.com/google/glog.git#96a2f23dca4cc7180821ca5f32e526314395d26a
#!CreateArchive
Source13:        submodule-13-glog.tar.gz
#!RemoteAsset:  git+https://gitlab.com/libeigen/eigen.git#f612df273689a19d25b45ca4f8269463207c4fee
#!CreateArchive
Source14:        submodule-14-eigen3.tar.gz
#!RemoteAsset:  git+https://github.com/NVIDIA/cub.git#48b555897ee66bcd057a521ed39d62b7688c7d59
#!CreateArchive
Source15:        submodule-15-cub.tar.gz
#!RemoteAsset:  git+https://github.com/NVIDIA/cutlass.git#eefa171318b79cbe2e78514d4cce5cd0fe919d0c
#!CreateArchive
Source16:        submodule-16-cutlass.tar.gz
#!RemoteAsset:  git+https://github.com/herumi/xbyak.git#4ca0434b4e78c05e3f3e68bda70e8713668e87d3
#!CreateArchive
Source17:        submodule-17-xbyak.tar.gz
#!RemoteAsset:  git+https://github.com/oneapi-src/oneDNN.git#28d696724426b943e2f4a0e607f90cdc19aedaf6
#!CreateArchive
Source18:        submodule-18-onednn.tar.gz
#!RemoteAsset:  git+https://github.com/PaddlePaddle/flash-attention.git#196115f865fc7f18a7ab55f32510415a788cb85d
#!CreateArchive
Source19:        submodule-19-flashattn.tar.gz
#!RemoteAsset:  git+https://github.com/google/googletest.git#2fe3bd994b3189899d93f1d5a881e725e046fdc2
#!CreateArchive
Source20:        submodule-20-gtest.tar.gz
#!RemoteAsset:  git+https://github.com/xianyi/OpenBLAS.git#5f36f18148603facb6c3540e673610d6b24cbfbb
#!CreateArchive
Source21:        submodule-21-openblas.tar.gz
#!RemoteAsset:  git+https://github.com/Thunderbrook/rocksdb.git#9e18bf0e273b081de54ef1227e6f1db9e02a472a
#!CreateArchive
Source22:        submodule-22-rocksdb.tar.gz
#!RemoteAsset:  git+https://github.com/NVIDIA/jitify.git#57de649139c866eb83acacfe50c92ad7c6278776
#!CreateArchive
Source23:        submodule-23-jitify.tar.gz
#!RemoteAsset:  git+https://github.com/NVIDIA/cccl.git#1f6e4bcae0fbf1bbed87f88544d8d2161c490fc1
#!CreateArchive
Source24:        submodule-24-cccl.tar.gz
#!RemoteAsset:  git+https://github.com/weidai11/cryptopp.git#9dcc26c58213abb8351fbb1b2a7a1d2c667366e4
#!CreateArchive
Source25:        submodule-25-cryptopp.tar.gz
#!RemoteAsset:  git+https://github.com/noloader/cryptopp-cmake.git#6d0666c457fbbf6f81819fd2b80f0cb5b6646593
#!CreateArchive
Source26:        submodule-26-cryptopp-cmake.tar.gz
#!RemoteAsset:  git+https://github.com/nlohmann/json.git#199dea11b17c533721b26249e2dcaee6ca1d51d3
#!CreateArchive
Source27:        submodule-27-nlohmann_json.tar.gz
#!RemoteAsset:  git+https://github.com/jbeder/yaml-cpp.git#1d8ca1f35eb3a9c9142462b28282a848e5d29a91
#!CreateArchive
Source28:        submodule-28-yaml-cpp.tar.gz
#!RemoteAsset:  git+https://github.com/openvinotoolkit/openvino.git#07ecdf07d2974410dc1d67d9fa2d3433dcab7865
#!CreateArchive
Source29:        submodule-29-openvino.tar.gz
#!RemoteAsset:  git+https://github.com/FlagOpen/FlagCX.git#7c469f4af991bf0f64b8f76d66f8e307a5eaea3f
#!CreateArchive
Source30:        submodule-30-flagcx.tar.gz
#!RemoteAsset:  git+https://github.com/libuv/libuv.git#2e7c07f4d10c1b391a7138471c49f4aae3c47d8d
#!CreateArchive
Source31:        submodule-31-libuv.tar.gz
#!RemoteAsset:  sha256:fc53cd6a459df80e0a261cee3035c3feb724f41efebc103398d84a1844e41665
Source32:        https://paddlepaddledeps.bj.bcebos.com/lapack_lnx_v3.10.0.20210628.tar.gz#/lapack_lnx_v3.10.0.20210628.tar.gz
#!RemoteAsset:  sha256:8b190a13cc21be6030363d119b3a8e0830dd8601902900fa0c05d1129d55b5ab
Source33:        https://paddlepaddledeps.bj.bcebos.com/csrmm_mklml_lnx_2019.0.5.tgz#/csrmm_mklml_lnx_2019.0.5.tgz
BuildSystem:    pyproject

# Avoid importing build-only modules during metadata generation (egg_info/dist_info).
Patch0:         0001-setup.py-short-circuit-metadata-phase-without-env_di.patch
# Replace third_party git checkout/apply flows with deterministic local patching.
Patch1:         0002-cmake-external-remove-git-checkout-from-third-party-patches.patch
# Disable x86 intrinsic include path on riscv64.
Patch2:         0003-phi-search_compute-disable-x86-intrinsics-on-riscv.patch

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  patchelf
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(pybind11-stubgen)
BuildRequires:  python3dist(numpy) >= 1.21
BuildRequires:  python3dist(protobuf) >= 3.20.2
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(safetensors) >= 0.6.0
BuildRequires:  python3dist(opt-einsum) >= 3.3

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PaddlePaddle is a deep learning framework that supports model development,
training, and inference.

%prep
%autosetup -p1 -n Paddle-%{version}

# Populate git submodules from RemoteAsset archives
mkdir -p third_party/protobuf
tar -C third_party/protobuf --strip-components=1 -xf %{SOURCE1}

mkdir -p third_party/pocketfft
tar -C third_party/pocketfft --strip-components=1 -xf %{SOURCE2}

mkdir -p third_party/gflags
tar -C third_party/gflags --strip-components=1 -xf %{SOURCE3}

mkdir -p third_party/gloo
tar -C third_party/gloo --strip-components=1 -xf %{SOURCE4}
# GCC 15 needs fixed-width integer includes in core headers.
grep -q '^#include <cstdint>$' third_party/gloo/gloo/types.h || \
  sed -i '1i #include <cstdint>' third_party/gloo/gloo/types.h

grep -q '^#include <cstdint>$' paddle/common/enforce.h || \
  sed -i '1i #include <cstdint>' paddle/common/enforce.h
grep -q '^#include <cstdint>$' paddle/phi/kernels/strings/unicode.h || \
  sed -i '1i #include <cstdint>' paddle/phi/kernels/strings/unicode.h
grep -q '^#include <cstdint>$' paddle/fluid/inference/api/paddle_api.h || \
  sed -i '1i #include <cstdint>' paddle/fluid/inference/api/paddle_api.h

mkdir -p third_party/dlpack
tar -C third_party/dlpack --strip-components=1 -xf %{SOURCE5}

mkdir -p third_party/utf8proc
tar -C third_party/utf8proc --strip-components=1 -xf %{SOURCE6}

mkdir -p third_party/warpctc
tar -C third_party/warpctc --strip-components=1 -xf %{SOURCE7}

mkdir -p third_party/warprnnt
tar -C third_party/warprnnt --strip-components=1 -xf %{SOURCE8}

mkdir -p third_party/xxhash
tar -C third_party/xxhash --strip-components=1 -xf %{SOURCE9}

mkdir -p third_party/pybind
tar -C third_party/pybind --strip-components=1 -xf %{SOURCE10}

mkdir -p third_party/threadpool
tar -C third_party/threadpool --strip-components=1 -xf %{SOURCE11}

mkdir -p third_party/zlib
tar -C third_party/zlib --strip-components=1 -xf %{SOURCE12}

mkdir -p third_party/glog
tar -C third_party/glog --strip-components=1 -xf %{SOURCE13}

mkdir -p third_party/eigen3
tar -C third_party/eigen3 --strip-components=1 -xf %{SOURCE14}

mkdir -p third_party/cub
tar -C third_party/cub --strip-components=1 -xf %{SOURCE15}

mkdir -p third_party/cutlass
tar -C third_party/cutlass --strip-components=1 -xf %{SOURCE16}

mkdir -p third_party/xbyak
tar -C third_party/xbyak --strip-components=1 -xf %{SOURCE17}

mkdir -p third_party/onednn
tar -C third_party/onednn --strip-components=1 -xf %{SOURCE18}

mkdir -p third_party/flashattn
tar -C third_party/flashattn --strip-components=1 -xf %{SOURCE19}

mkdir -p third_party/gtest
tar -C third_party/gtest --strip-components=1 -xf %{SOURCE20}

mkdir -p third_party/openblas
tar -C third_party/openblas --strip-components=1 -xf %{SOURCE21}

mkdir -p third_party/rocksdb
tar -C third_party/rocksdb --strip-components=1 -xf %{SOURCE22}

mkdir -p third_party/jitify
tar -C third_party/jitify --strip-components=1 -xf %{SOURCE23}

mkdir -p third_party/cccl
tar -C third_party/cccl --strip-components=1 -xf %{SOURCE24}

mkdir -p third_party/cryptopp
tar -C third_party/cryptopp --strip-components=1 -xf %{SOURCE25}

mkdir -p third_party/cryptopp-cmake
tar -C third_party/cryptopp-cmake --strip-components=1 -xf %{SOURCE26}

mkdir -p third_party/nlohmann_json
tar -C third_party/nlohmann_json --strip-components=1 -xf %{SOURCE27}

mkdir -p third_party/yaml-cpp
tar -C third_party/yaml-cpp --strip-components=1 -xf %{SOURCE28}
# yaml-cpp at pinned revision misses fixed-width integer includes with newer toolchains.
sed -i '1i #include <cstdint>' third_party/yaml-cpp/src/emitterutils.cpp

mkdir -p third_party/openvino
tar -C third_party/openvino --strip-components=1 -xf %{SOURCE29}

mkdir -p third_party/flagcx
tar -C third_party/flagcx --strip-components=1 -xf %{SOURCE30}

mkdir -p third_party/libuv
tar -C third_party/libuv --strip-components=1 -xf %{SOURCE31}

# Preseed upstream CMake external downloads for offline builds.
# lapack archive is needed on all arches to avoid network download during configure.
mkdir -p third_party/lapack/Linux
cp %{SOURCE32} third_party/lapack/Linux/lapack_lnx_v3.10.0.20210628.tar.gz

# mklml bundle is x86-only in openRuyi.
%ifarch x86_64
mkdir -p third_party/mklml/Linux
cp %{SOURCE33} third_party/mklml/Linux/csrmm_mklml_lnx_2019.0.5.tgz
%endif

# openRuyi riscv64 toolchain does not support -m64; strip it from upstream flags.
%ifarch riscv64
sed -i 's/[[:space:]]-m64//g' cmake/flags.cmake
%endif

# RISC-V must not enable x86 SSE denormal intrinsics path.
%ifarch riscv64
sed -i 's/!defined(PADDLE_WITH_RISCV)/!defined(__riscv)/g' paddle/phi/core/platform/denormal.cc
if ! grep -q '__riscv' paddle/phi/core/platform/denormal.cc; then
  sed -i 's/!defined(PADDLE_WITH_LOONGARCH)/!defined(PADDLE_WITH_LOONGARCH) \&\& !defined(__riscv)/' paddle/phi/core/platform/denormal.cc
fi
%endif

%build
export PY_VERSION=%{python3_version}
export PADDLE_VERSION=%{version}
export WITH_MKL=OFF
export WITH_SYSTEM_BLAS=ON
export OPENBLAS_ROOT=%{_prefix}
export CMAKE_INSTALL_PREFIX=$PWD/build/paddle-cmake-install
export SKIP_STUB_GEN=1
# riscv64 currently fails in link phase with "ld terminated with signal 11".
# Force bfd linker path and reduce linker memory pressure for huge shared libs.
%ifarch riscv64
export CFLAGS="${CFLAGS:+${CFLAGS} }-fuse-ld=bfd"
# Reduce C++ compile-time memory pressure on riscv64 workers.
export CXXFLAGS="${CXXFLAGS:+${CXXFLAGS} }-fuse-ld=bfd -fno-var-tracking-assignments"
export LDFLAGS="${LDFLAGS:+${LDFLAGS} }-fuse-ld=bfd -Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
export CMAKE_BUILD_PARALLEL_LEVEL=2
%endif
%pyproject_wheel

%install
export PY_VERSION=%{python3_version}
%pyproject_install
# Do not ship bundled runtime libs; use system-provided BLAS/libgfortran stack.
rm -f %{buildroot}%{python3_sitearch}/paddle/libs/libgfortran.so*
rm -f %{buildroot}%{python3_sitearch}/paddle/libs/libquadmath.so*
rm -f %{buildroot}%{python3_sitearch}/paddle/libs/libblas.so*
rm -f %{buildroot}%{python3_sitearch}/paddle/libs/liblapack.so*
%ifarch riscv64
# Guardrail: fail fast if any x86_64 shared objects are still present.
if [ -d %{buildroot}%{python3_sitearch}/paddle/libs ]; then
  if find %{buildroot}%{python3_sitearch}/paddle/libs -maxdepth 1 -type f -name '*.so*' -exec file -L {} + | grep -q 'x86-64'; then
    echo "ERROR: x86_64 ELF detected in riscv64 package payload:" >&2
    find %{buildroot}%{python3_sitearch}/paddle/libs -maxdepth 1 -type f -name '*.so*' -exec file -L {} + | grep 'x86-64' >&2
    exit 1
  fi
fi
%endif
rm -f %{buildroot}%{python3_sitearch}/_foo*.so
%pyproject_save_files -l paddle
# Keep file manifest aligned after removing bundled runtime libs.
sed -i \
  -e '\|/paddle/libs/libgfortran\.so|d' \
  -e '\|/paddle/libs/libquadmath\.so|d' \
  -e '\|/paddle/libs/libblas\.so|d' \
  -e '\|/paddle/libs/liblapack\.so|d' \
  %{pyproject_files}

%check
# Skip test execution due heavy runtime and hardware-dependent test requirements.

%files -f %{pyproject_files}
%{_bindir}/paddle
%doc README.md
%license LICENSE

%changelog
%autochangelog
