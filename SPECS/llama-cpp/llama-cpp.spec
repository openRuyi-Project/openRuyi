# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# CPU is the default flavor
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "rocm"
%bcond rocm 1
%bcond vulkan 0
%elif "%{flavor}" == "vulkan"
%bcond rocm 0
%bcond vulkan 1
%else
%bcond rocm 0
%bcond vulkan 0
%endif

%global build_number 10448
# Private libraries should not expose public ABI
# The libllama* is CLI tools
# The libggml-* entries are dlopen()ed backend plugins under %%{_libdir}/ggml
%global __provides_exclude ^(libllama-.*-impl|libggml-cpu.*|libggml-hip|libggml-vulkan)\\.so
%global __requires_exclude ^libllama-.*-impl\\.so
# Exclude network/model-related, maintainer-only, and GGML_BACKEND_DL-incompatible tests
%global ctest_exclude_common (test-tokenizers-ggml-vocabs|test-download-model|test-thread-safety|test-state-restore-fragmented|test-recurrent-state-rollback|test-save-load-state|test-quant-type-selection|test-gguf-model-data|test-arg-parser|test-jinja-py|test-backend-ops|test-llama-archs|test-generate-models|test-recurrent-state-rollback-nemotron-h)
%if %{with rocm} || %{with vulkan}
# GPU flavors exclude test-opt because package is built with no GPU device
%global ctest_exclude ^(%{ctest_exclude_common}|test-opt)$
%else
%global ctest_exclude ^%{ctest_exclude_common}$
%endif

%global llvm_maj_ver 22

%if %{with rocm}
Name:           llama-cpp-rocm
%elif %{with vulkan}
Name:           llama-cpp-vulkan
%else
Name:           llama-cpp
%endif
Version:        b%{build_number}
Release:        %autorelease
Summary:        LLM inference in C/C++
License:        MIT AND Apache-2.0 AND Unlicense
URL:            https://github.com/ggml-org/llama.cpp
VCS:            git:https://github.com/ggml-org/llama.cpp.git
#!RemoteAsset:  sha256:85791799efe44625718640e3dcedb6112a132018e38e61e43190b1ff37ade355
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

%if %{with rocm}
# llama.cpp/ggml produces unstable output in riscv64 ROCm with default batch size
Patch2000:      2000-limit-rocm-batch-size.patch
%endif

BuildOption(prep):  -n llama.cpp-%{version}
BuildOption(conf):  -G Ninja
BuildOption(conf):  -DLLAMA_BUILD_NUMBER=%{build_number}
# Source0 is an archive without .git; preserve the verified release tag commit
BuildOption(conf):  -DLLAMA_BUILD_COMMIT=ad1de39e0708e3ced9c71bb3c82d93a2c046a73f
BuildOption(conf):  -DLLAMA_BUILD_EXAMPLES=OFF
BuildOption(conf):  -DLLAMA_TESTS_INSTALL=OFF
# Building the Web UI downloads frontend assets
BuildOption(conf):  -DLLAMA_BUILD_UI=OFF
BuildOption(conf):  -DLLAMA_USE_PREBUILT_UI=OFF
BuildOption(conf):  -DGGML_NATIVE=OFF
BuildOption(conf):  -DGGML_BACKEND_DL=ON
BuildOption(conf):  -DGGML_BACKEND_DIR=%{_libdir}/ggml
%ifarch x86_64
BuildOption(conf):  -DGGML_CPU_ALL_VARIANTS=ON
%endif
%if %{with rocm}
BuildOption(conf):  -DGGML_HIP=ON
BuildOption(conf):  -DCMAKE_HIP_COMPILER=%{rocmllvm_bindir}/clang++
BuildOption(conf):  -DAMDGPU_TARGETS=%{rocm_gpu_list_default}
%endif
%if %{with vulkan}
BuildOption(conf):  -DGGML_VULKAN=ON
%endif
BuildOption(check):  --exclude-regex '%{ctest_exclude}'

BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig(openssl)
%if %{with rocm}
BuildRequires:  clang(major) = %{llvm_maj_ver}
BuildRequires:  clang-devel(major) = %{llvm_maj_ver}
BuildRequires:  clang%{llvm_maj_ver}-tools-extra
BuildRequires:  libomp%{llvm_maj_ver}-devel
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hipblas)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  cmake(rocblas)
BuildRequires:  compiler-rt(major) = %{llvm_maj_ver}
BuildRequires:  hipcc
BuildRequires:  lld(major) = %{llvm_maj_ver}
BuildRequires:  llvm-devel(major) = %{llvm_maj_ver}
BuildRequires:  rocm-llvm-macros
%else
BuildRequires:  libomp-devel
%endif
%if %{with vulkan}
BuildRequires:  cmake(VulkanLoader)
BuildRequires:  pkgconfig(SPIRV-Headers)
BuildRequires:  shaderc
%endif

# For multimodel AI
Suggests:       ffmpeg
%if %{without rocm}
%if %{without vulkan}
Provides:       llama-cpp-cpu
Conflicts:      llama-cpp-rocm
Conflicts:      llama-cpp-vulkan
%else
Conflicts:      llama-cpp
Conflicts:      llama-cpp-rocm
%endif
%else
Conflicts:      llama-cpp
Conflicts:      llama-cpp-vulkan
%endif

%description
llama.cpp provides performant inference for large language models in plain
C/C++. This package includes command-line tools, a server, and shared libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{without rocm}
%if %{without vulkan}
Provides:       llama-cpp-devel = %{version}-%{release}
%endif
%endif

%description    devel
Headers, shared-library links, pkg-config metadata, and CMake package files for
developing applications against llama.cpp and ggml.

%check -a
# Smoke-test the newly built CLI
LD_LIBRARY_PATH=%{_vpath_builddir}/bin %{_vpath_builddir}/bin/llama-cli --version

%files
%doc README.md
%license LICENSE licenses/LICENSE-jsonhpp vendor/cpp-httplib/LICENSE
%{_bindir}/llama*
%{_libdir}/ggml/
%{_libdir}/libggml*.so.*
%{_libdir}/libllama-*-impl.so
%{_libdir}/libllama*.so.*
%{_libdir}/libmtmd.so.*

%files devel
%{_includedir}/ggml*.h
%{_includedir}/gguf.h
%{_includedir}/llama*.h
%{_includedir}/mtmd*.h
%{_libdir}/cmake/ggml/
%{_libdir}/cmake/llama/
%{_libdir}/libggml*.so
%{_libdir}/libllama.so
%{_libdir}/libllama-common.so
%{_libdir}/libmtmd.so
%{_libdir}/pkgconfig/llama.pc

%changelog
%autochangelog
