# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>
%global srcname sglang-kernel-cpu
%global toolchain clang
%global version_upstream 0.5.21

# The upstream AOT metadata pins torch==2.14.0.  This distribution builds
# torch 2.13.0, so %prep rewrites that requirement down; the pin below is the
# recorded deviation from the upstream requirement.
%global torch_full_version 2.13.0
# pythondistdeps drops trailing zero components from distribution capabilities,
# so an exact pin on 2.13.0 has to be written as 2.13.
%global torch_cap_version 2.13

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "cuda"
%bcond cuda 1
%{error:CUDA SGLang CPU kernel flavor is reserved and is not supported by this SPEC}
%else
%bcond cuda 0
%endif
%if "%{flavor}" == "rocm"
%bcond rocm 1
%{error:ROCm SGLang CPU kernel flavor is reserved and is not supported by this SPEC}
%else
%bcond rocm 0
%endif
%if %{with cuda}
%{error:CUDA SGLang CPU kernel flavor is reserved and is not supported by this SPEC}
%endif
%if %{with rocm}
%{error:ROCm SGLang CPU kernel flavor is reserved and is not supported by this SPEC}
%endif
%ifarch riscv64
%global llvm_maj_ver 22
%global llvm_bindir %{_libdir}/llvm%{llvm_maj_ver}/bin
%endif

Name:           python-%{srcname}
Version:        0.4.7
Release:        %autorelease
Summary:        CPU kernel library for SGLang
License:        Apache-2.0
URL:            https://github.com/sgl-project/sglang/tree/v0.5.21/python/sglang/kernels/aot
VCS:            git:https://github.com/sgl-project/sglang.git
#!RemoteAsset:  sha256:c44951b7871dac61262fc04e9fca628175758a97fa5f603c522b31dc31b94249
Source0:        https://github.com/sgl-project/sglang/archive/refs/tags/v%{version_upstream}.tar.gz#/sglang-%{version_upstream}.tar.gz
Source1:        sglang-kernel-cpu-smoke.py
BuildSystem:    pyproject
# The CPU kernel is currently validated only as part of the RISC-V SGLang
# closure.  Do not publish an x86_64 provider while the corresponding SGLang
# CPU metadata still requires unavailable intel-openmp capability.
ExclusiveArch:  riscv64
Conflicts:      python-sglang-kernel

BuildOption(prep):  -n sglang-%{version_upstream}
BuildOption(install):  sgl_kernel
# flash_attn and rotary_embedding need a live device runtime.
BuildOption(check):  -e sgl_kernel.flash_attn
BuildOption(check):  -e sgl_kernel.testing.rotary_embedding

%ifarch riscv64
%if "%{openruyi_riscv_arch}" == "-march=rva23u64"
%global sglang_cpu_march rva23u64
%else
%global sglang_cpu_march rva20u64
%endif
# Keep CMake's compiler driver and target triple aligned with the LLVM 22
# toolchain used for the RISC-V package build.
BuildOption(build):  -Ccmake.define.CMAKE_C_COMPILER=%{llvm_bindir}/clang
BuildOption(build):  -Ccmake.define.CMAKE_CXX_COMPILER=%{llvm_bindir}/clang++
BuildOption(build):  -Ccmake.define.CMAKE_C_COMPILER_TARGET:STRING=%{_target_platform}
BuildOption(build):  -Ccmake.define.CMAKE_CXX_COMPILER_TARGET:STRING=%{_target_platform}
%if "%{_host_cpu}" != "%{_target_cpu}"
BuildOption(build):  -Ccmake.define.CMAKE_SYSTEM_NAME=Linux
BuildOption(build):  -Ccmake.define.CMAKE_SYSTEM_PROCESSOR=riscv64
%endif
%endif

BuildRequires:  cmake >= 3.18
BuildRequires:  cmake(concurrentqueue)
BuildRequires:  clang
BuildRequires:  file
BuildRequires:  patchelf
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(python3)
# Caffe2/public/protobuf.cmake in Torch's CMake package resolves protobuf with
# find_package(Protobuf CONFIG), so the CMake package files this package ships
# are needed even though the kernels never include a protobuf header directly.
BuildRequires:  protobuf-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python-rpm-macros
# The distribution ships scikit-build-core 1.1.1, which satisfies the
# upstream >= 0.10 floor and the >= 1.0.2 pin used by python-pyvex.
BuildRequires:  python3dist(scikit-build-core) >= 0.10
BuildRequires:  python3dist(torch) = %{torch_cap_version}
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(ninja) >= 1.5
# Torch installs its CMake package files in the -devel subpackage.
BuildRequires:  python-torch-devel

%ifarch riscv64
BuildRequires:  clang(major) = %{llvm_maj_ver}
BuildRequires:  compiler-rt(major) = %{llvm_maj_ver}
BuildRequires:  libomp-devel(major) = %{llvm_maj_ver}
BuildRequires:  lld(major) = %{llvm_maj_ver}
BuildRequires:  llvm(major) = %{llvm_maj_ver}
%endif

Requires:       python3dist(torch) = %{torch_cap_version}

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}
# Keep both the provider name and the upstream project capability.  The
# upstream CPU metadata still requires sglang-kernel, while the RISC-V package
# name identifies the isolated provider as sglang-kernel-cpu.
Provides:       python3dist(sglang-kernel) = %{version}

%patchlist
# RISC-V source selection and explicit cross-target ISA handling.
2000-riscv64-cpu-target-selection.patch
# Portable scalar shared-memory collectives and acquire/release state hand-off.
2001-riscv64-port-cpu-shm-collectives.patch

%description
SGLang Kernel CPU provides the CPU AOT extension used by the SGLang inference
engine. It uses the upstream CPU build configuration from SGLang 0.5.21.

%prep -a
cd python/sglang/kernels/aot
cp pyproject_cpu.toml pyproject.toml
sed -i -e 's/"torch==2.14.0"/"torch==%{torch_full_version}"/' pyproject.toml

%generate_buildrequires
cd python/sglang/kernels/aot
# The dependency closure is declared above; resolve the build backend only.
%pyproject_buildrequires -R

%build -p
cd python/sglang/kernels/aot
# scikit-build-core discovers CMake and Ninja by probing them with a hardcoded
# five-second timeout; under a saturated build queue that probe is starved and
# metadata generation aborts with CMakeNotFoundError.  Name the programs and
# bound the job count so the probe cannot time out.
export CMAKE_MAKE_PROGRAM=%{_bindir}/ninja
export CMAKE_BUILD_PARALLEL_LEVEL=%{?_smp_build_ncpus}%{!?_smp_build_ncpus:2}
%ifarch riscv64
export PATH="%{llvm_bindir}:$PATH"
export CC="%{llvm_bindir}/clang"
export CXX="%{llvm_bindir}/clang++"
export LD="%{llvm_bindir}/ld.lld"
export AR="%{llvm_bindir}/llvm-ar"
export RANLIB="%{llvm_bindir}/llvm-ranlib"
export CMAKE_ARGS="-DSGLANG_CPU_TARGET_ARCH=riscv64 -DSGLANG_CPU_MARCH=%{sglang_cpu_march}"
export CFLAGS="%{build_cflags} --target=%{_target_platform}"
export CXXFLAGS="%{build_cxxflags} --target=%{_target_platform}"
export LDFLAGS="-fuse-ld=lld --target=%{_target_platform} %{build_ldflags}"
%endif

%install -p
cd python/sglang/kernels/aot

%install -a
install -Dpm0755 %{SOURCE1} %{buildroot}%{_libexecdir}/sglang/sglang-kernel-cpu-smoke.py
# The extension loads torch's shared libraries from the sibling torch package
# at runtime, so record relative entries instead of a private library path.
for so in $(find %{buildroot}%{python3_sitearch} -type f -name '*.so*'); do
  if file "$so" | grep -q 'ELF'; then
    patchelf --set-rpath '$ORIGIN:$ORIGIN/../torch/lib' "$so"
  fi
done

%check -a
cd %{buildroot}
# Torch is a build dependency of this recipe, so the built extension can be
# imported straight out of the buildroot.  The smoke script validates
# registration, two-rank reduction, and synchronization with the native
# shared-memory implementation.
PYTHONPATH="%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}" \
LOCAL_SIZE=1 MASTER_ADDR=127.0.0.1 MASTER_PORT=29599 \
  %{python3} "%{buildroot}%{_libexecdir}/sglang/sglang-kernel-cpu-smoke.py"

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_libexecdir}/sglang/sglang-kernel-cpu-smoke.py

%changelog
%autochangelog
