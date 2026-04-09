# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Sakura286 <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond rocm 1

%define _name           ollama
%define go_import_path  github.com/ollama/ollama

# Ollama bundles some ggml libs
# They should be kept private and the scans of these files should be disabled
%global __provides_exclude lib.*\\.so(\\..*)?
%global __requires_exclude libggml-.*\\.so(\\..*)?

Name:           ollama
Version:        0.13.5
Release:        %autorelease
Summary:        Get up and running with OpenAI gpt-oss, DeepSeek-R1, Gemma 3 and other models.
License:        MIT
URL:            https://ollama.com/
VCS:            git:https://github.com/ollama/ollama
#!RemoteAsset
Source0:        https://github.com/ollama/ollama/archive/refs/tags/v%{version}.tar.gz
Source1:        ollama.service
Source2:        ollama.sysusers
BuildSystem:    golang

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/agnivade/levenshtein)
BuildRequires:  go(github.com/containerd/console)
BuildRequires:  go(github.com/d4l3k/go-bfloat16)
BuildRequires:  go(github.com/dlclark/regexp2)
BuildRequires:  go(github.com/emirpasic/gods/v2)
BuildRequires:  go(github.com/gin-contrib/cors)
BuildRequires:  go(github.com/gin-gonic/gin)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/nlpodyssey/gopickle)
BuildRequires:  go(github.com/olekukonko/tablewriter) < 1.0.0
BuildRequires:  go(github.com/pdevine/tensor)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/x448/float16)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/image)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(gonum.org/v1/gonum)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  ninja
BuildRequires:  systemd-rpm-macros
%if %{with rocm}
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(Clang)
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hipblas)
BuildRequires:  cmake(hsa-runtime64)
BuildRequires:  cmake(LLD)
BuildRequires:  cmake(LLVM)
BuildRequires:  cmake(rocblas)
BuildRequires:  cmake(rocsolver)
BuildRequires:  pkgconfig(libdrm_amdgpu)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(numa)
BuildRequires:  rocm-llvm-macros
BuildRequires:  rocminfo
BuildRequires:  clang-tools-extra-devel
BuildRequires:  compiler-rt
BuildRequires:  hipcc
%endif

%{?systemd_requires}
%if %{with rocm}
Requires:       hipblas
Requires:       rocblas
%endif

%patchlist
# Ollama vendors ggml code, but it does not sync riscv64 code by default
# Manually sync riscv64 code here
0001-ollama-0.14.2_add-riscv.patch
# Ollama put ggml-cpu code(cpp) inside 'ollama' binary file(go)
0002-go-riscv64.patch
# Golang buildsystem on openRuyi use GO11MODULE=off, makes
# httpmuxgo121=1, which is deprecated in newer version of go
# Without this patch, ollama cannot provide even the basic http functions
# https://github.com/jkroepke/openvpn-auth-oauth2/pull/706
0003-disable-httpmuxgo121-on-newer-version-of-go.patch
# This patch breaks dlopen of ollama, temporarily disable it
# Install ollama to /usr/lib as workaround
# 0004-use-lib64-instead-of-lib.patch
# GGML_CPU_ALL_VARIANTS only supports x86_64
0005-disable-cpu-variants.patch
# Llama.cpp(ggml) on riscv64's ROCm frequently produce nonsense
# Give parameter '-b 8 -ub 8' can stabilize it
0006-limit-batch-size-to-stabilize.patch

%description
Ollama is an open-source platform designed to run large language models locally.
It allows users to generate text, assist with coding, and create content privately
and securely on their own devices.

%prep -a
# Remove bundled dependencies
rm -rf llama/llama.cpp/vendor

# Ollama use a mix build of cmake and go.
# Ollama binary built by go will use dlopen to load *.so built by cmake.
# Building order of go/cmake is not important.
%build -a
%cmake \
    -G Ninja \
    -W no-dev \
    -DCMAKE_INSTALL_LIBDIR:PATH=lib \
    -DCMAKE_INSTALL_FULL_LIBDIR:PATH=/usr/lib \
    -DLIB_INSTALL_DIR:PATH=/usr/lib \
    -DLIB_SUFFIX= \
%if %{with rocm}
    -DCMAKE_HIP_COMPILER=%{rocmllvm_bindir}/clang++ \
    -DAMDGPU_TARGETS=%{rocm_gpu_list_default}
%endif
%cmake_build

%install
%buildsystem_golang_install
%cmake_install
# Remove bundled contents
rm -rvf %{buildroot}%{_bindir}/lib* \
    %{buildroot}%{_exec_prefix}/lib/ollama/libamd*  \
    %{buildroot}%{_exec_prefix}/lib/ollama/libdrm*  \
    %{buildroot}%{_exec_prefix}/lib/ollama/libelf*  \
    %{buildroot}%{_exec_prefix}/lib/ollama/libhip*  \
    %{buildroot}%{_exec_prefix}/lib/ollama/libhsa*  \
    %{buildroot}%{_exec_prefix}/lib/ollama/libnuma* \
    %{buildroot}%{_exec_prefix}/lib/ollama/libroc*  \
    %{buildroot}%{_exec_prefix}/lib/ollama/libroc*  \
    %{buildroot}%{_exec_prefix}/lib/ollama/rocblas/

install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/ollama.service
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/ollama.conf
# home dir
mkdir -p %{buildroot}%{_var}/lib/ollama

%pre
%sysusers_create_package ollama %{SOURCE2}

%preun
%systemd_preun ollama.service

%post
%systemd_post ollama.service

%postun
%systemd_postun_with_restart ollama.service

%files
%license LICENSE*
%doc README*
%dir %{_exec_prefix}/lib/ollama
%attr(0755,ollama,ollama) %dir %{_var}/lib/ollama/
%{_bindir}/ollama
%{_exec_prefix}/lib/ollama/*
%{_unitdir}/ollama.service
%{_sysusersdir}/ollama.conf

%changelog
%autochangelog
