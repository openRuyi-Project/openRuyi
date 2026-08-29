# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname paddlepaddle

# Base package is CPU-only. ONNX Runtime integration is left as an explicit
# opt-in path for future backend work.
%bcond onnxruntime 0
# ROCm support is an explicit opt-in because the full Paddle ROCm dependency stack
# is not packaged in openRuyi yet.
%bcond rocm 0

Name:           python-%{srcname}
Version:        3.3.1
Release:        %autorelease
Summary:        Deep learning framework for machine learning
License:        Apache-2.0
URL:            https://www.paddlepaddle.org.cn/
VCS:            git:https://github.com/PaddlePaddle/Paddle
# PyPI 3.3.1 publishes wheels only (no sdist), so Source0 uses upstream tag tarball.
#!RemoteAsset:  sha256:c3ffd836335fc4f95ffd990b1556cef5d1c39fcfd0bdca46f02e799a3ec870aa
Source0:        https://github.com/PaddlePaddle/Paddle/archive/refs/tags/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l paddle
# APY pass helper modules use non-package-local imports and are not public
# runtime entry points for this CPU-only baseline package.
BuildOption(check):  -e 'paddle.apy.matmul_pass.index_drr_pass_util'
BuildOption(check):  -e 'paddle.apy.matmul_pass.index_program_translator_util'
BuildOption(check):  -e 'paddle.apy.matmul_pass.kernel_arg_id_util'
BuildOption(check):  -e 'paddle.apy.matmul_pass.low_level_ir_code_gen_ctx_util'
BuildOption(check):  -e 'paddle.apy.matmul_pass.matmul_epilogue_pass'
BuildOption(check):  -e 'paddle.apy.matmul_pass.matmul_variadic_ptn'
BuildOption(check):  -e 'paddle.apy.matmul_pass.matmul_variadic_tpl'
BuildOption(check):  -e 'paddle.apy.matmul_pass.op_compute_translator_util'
BuildOption(check):  -e 'paddle.apy.matmul_pass.op_conversion_drr_pass'
BuildOption(check):  -e 'paddle.apy.matmul_pass.op_index_translator_util'
BuildOption(check):  -e 'paddle.apy.matmul_pass.program_translator_util'
BuildOption(check):  -e 'paddle.apy.matmul_pass.topo_drr_pass'
BuildOption(check):  -e 'paddle.apy.matmul_pass.umprime'
BuildOption(check):  -e 'paddle.apy.sys.ap'
# These distributed/optional internals require unavailable optional services or
# conflict with the system protobuf runtime during isolated import checks.
BuildOption(check):  -e 'paddle.base.proto.distributed_strategy_pb2'
BuildOption(check):  -e 'paddle.distributed.auto_tuner.recorder'
BuildOption(check):  -e 'paddle.distributed.launch.utils.etcd_client'
BuildOption(check):  -e 'paddle.distributed.transpiler.geo_sgd_transpiler'
# paddle.libs contains native shared libraries, not Python extension modules.
BuildOption(check):  -e 'paddle.libs.libcommon'
BuildOption(check):  -e 'paddle.libs.libphi'
BuildOption(check):  -e 'paddle.libs.libphi_core'

BuildRequires:  abseil-cpp-devel
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  patchelf
BuildRequires:  cpp-threadpool-devel
BuildRequires:  dlpack
BuildRequires:  eigen3
BuildRequires:  glog-devel
BuildRequires:  pocketfft-devel
BuildRequires:  sleef-devel
BuildRequires:  pkgconfig(gflags)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(openblas)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3dist(pybind11)
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
BuildRequires:  warp-ctc-devel
BuildRequires:  warp-transducer-devel
%if %{with onnxruntime}
BuildRequires:  onnxruntime-devel
BuildRequires:  paddle2onnx-devel
%endif

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%patchlist
# Avoid importing build-only modules during metadata generation (egg_info/dist_info).
2000-setup.py-short-circuit-metadata-phase-without-env_di.patch
# Replace third_party git checkout/apply flows with deterministic local patching.
2001-cmake-external-remove-git-checkout-from-third-party-patches.patch
# Disable x86 intrinsic include path on riscv64.
2002-phi-search_compute-disable-x86-intrinsics-on-riscv.patch
# Use distribution-provided protobuf, ONNX Runtime, and Paddle2ONNX.
2003-use-system-protobuf-onnxruntime-paddle2onnx.patch
# Use distribution-provided third-party dependencies instead of Paddle vendored
# external projects.
2004-use-system-third-party-dependencies.patch
# Fix system protobuf/glog integration and GCC 16 SSE macro handling.
2005-use-system-protobuf-glog-and-fix-sse2-restore.patch
# Fix build issues exposed by system pocketfft and Eigen 5.
2006-fix-system-pocketfft-and-eigen5-build.patch
# Fix more Eigen 5 issues with Paddle custom scalar types.
2007-fix-eigen5-custom-scalar-type-build.patch
# Disable x86 CPUID probing on riscv64.
2008-disable-x86-cpuid-on-riscv.patch
# Match system glog failure writer callback signature.
2009-fix-system-glog-failure-writer-signature.patch
# Use system SLEEF scalar symbol names available on both x86_64 and riscv64.
2010-use-generic-system-sleef-scalar-symbols.patch
# Match system glog LogMessageVoidify namespace.
2011-fix-system-glog-logmessagevoidify-namespace.patch
# Do not feed system utf8proc shared library to static archive merge.
2012-keep-system-utf8proc-out-of-static-inference-archive.patch
# Use system utf8proc include path for inference distribution packaging.
2013-use-system-utf8proc-include-in-inference-dist.patch
# Use system yaml-cpp include path for inference distribution packaging.
2014-use-system-yaml-cpp-include-in-inference-dist.patch
# Preserve system protobuf's Abseil link dependency.
2015-link-system-abseil-from-protobuf-targets.patch

%description
PaddlePaddle is a deep learning framework that supports model development,
training, and inference.

%prep
%autosetup -p1 -n Paddle-%{version}

# GCC 15 needs fixed-width integer includes in core headers.
grep -q '^#include <cstdint>$' paddle/common/enforce.h || \
  sed -i '1i #include <cstdint>' paddle/common/enforce.h
grep -q '^#include <cstdint>$' paddle/phi/kernels/strings/unicode.h || \
  sed -i '1i #include <cstdint>' paddle/phi/kernels/strings/unicode.h
grep -q '^#include <cstdint>$' paddle/fluid/inference/api/paddle_api.h || \
  sed -i '1i #include <cstdint>' paddle/fluid/inference/api/paddle_api.h

# openRuyi riscv64 toolchain does not support -m64; strip it from upstream flags.
%ifarch riscv64
sed -i 's/[[:space:]]-m64//g' cmake/flags.cmake
%endif

# openRuyi uses lib64 on 64-bit architectures; make Paddle's OpenBLAS finder
# use the system package instead of falling back to bundled OpenBLAS.
sed -i 's|${OPENBLAS_ROOT}/lib |${OPENBLAS_ROOT}/%{_lib} ${OPENBLAS_ROOT}/lib |' cmake/cblas.cmake

# RISC-V must not enable x86 SSE denormal intrinsics path.
%ifarch riscv64
sed -i 's/!defined(PADDLE_WITH_RISCV)/!defined(__riscv)/g' paddle/phi/core/platform/denormal.cc
if ! grep -q '__riscv' paddle/phi/core/platform/denormal.cc; then
  sed -i 's/!defined(PADDLE_WITH_LOONGARCH)/!defined(PADDLE_WITH_LOONGARCH) \&\& !defined(__riscv)/' paddle/phi/core/platform/denormal.cc
fi
%endif

%build
# Paddle's setup.py forwards WITH_* and CMAKE_* environment variables to CMake.
export PY_VERSION=%{python3_version}
export PADDLE_VERSION=%{version}
# Use system protobuf instead of Paddle's bundled third-party copy.
export PROTOBUF_ROOT=%{_prefix}
# Build the baseline CPU-only package first; accelerator backends can be added
# as explicit build conditions later.
export WITH_GPU=OFF
export WITH_MKL=OFF
export WITH_XPU=OFF
export WITH_DISTRIBUTE=OFF
# Do not build Paddle's upstream unit-test matrix; %check keeps the installed
# module import smoke test.
export WITH_TESTING=OFF
# Paddle's C++ test targets default to ON and are not part of the runtime RPM.
export WITH_CPP_TEST=OFF
# Prefer system OpenBLAS and system third-party packages over vendored sources.
export WITH_SYSTEM_BLAS=ON
export WITH_SYSTEM_THIRD_PARTY=ON
# Disable optional subsystems that are not packaged/enabled in this CPU build.
export WITH_ONEDNN=OFF
export WITH_OPENVINO=OFF
export WITH_CINN=OFF
export WITH_XBYAK=OFF
export WITH_CRYPTO=OFF
%if %{with onnxruntime}
# When enabled, use system ONNX Runtime/Paddle2ONNX instead of bundled binaries.
export WITH_ONNXRUNTIME=ON
export WITH_SYSTEM_ONNXRUNTIME=ON
export WITH_SYSTEM_PADDLE2ONNX=ON
%else
export WITH_ONNXRUNTIME=OFF
%endif
%if %{with rocm}
# Use the distro ROCm prefix when the optional ROCm build is enabled.
export WITH_ROCM=ON
export ROCM_PATH=%{_prefix}
%else
export WITH_ROCM=OFF
%endif
export OPENBLAS_ROOT=%{_prefix}
export CMAKE_INSTALL_PREFIX=$PWD/build/paddle-cmake-install
# Stub generation is not needed for building the binary runtime package.
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
if [ -d %{buildroot}%{python3_sitearch}/paddle/libs ]; then
  unexpected_libs="$(find %{buildroot}%{python3_sitearch}/paddle/libs -maxdepth 1 -type f \( \
    -name 'libwarpctc.so*' -o \
    -name 'libwarprnnt.so*' -o \
    -name 'libgfortran.so*' -o \
    -name 'libquadmath.so*' -o \
    -name 'libblas.so*' -o \
    -name 'liblapack.so*' \
  \) -print)"
  if [ -n "$unexpected_libs" ]; then
    echo "ERROR: system third-party runtime libraries were copied into paddle.libs:" >&2
    echo "$unexpected_libs" >&2
    exit 1
  fi
fi
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

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/paddle

%changelog
%autochangelog
