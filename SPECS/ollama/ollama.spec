# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Sakura286 <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond rocm 1

%define _name           ollama
%define go_import_path  github.com/ollama/ollama
%define _vpath_srcdir %{_builddir}/go/src/%{go_import_path}
%define llama_cpp_commit f174553e1621c6a22a64e7bfcbb58d3a5c49e6fb

# Ollama bundles some ggml libs
# They should be kept private and the scans of these files should be disabled
%global __provides_exclude lib.*\\.so(\\..*)?
%global __requires_exclude libggml-.*\\.so(\\..*)?

Name:           ollama
Version:        0.40.7
Release:        %autorelease
Summary:        Run large language models locally
License:        MIT
URL:            https://ollama.com/
VCS:            git:https://github.com/ollama/ollama
#!RemoteAsset:  sha256:9db79f02285556ace3f724c1609e6fbf3d17a9812049400f22567ced591b2c16
Source0:        https://github.com/ollama/ollama/archive/refs/tags/v%{version}.tar.gz
Source1:        ollama.service
Source2:        ollama.sysusers
#!RemoteAsset:  sha256:1bafb9a13f3c6f7a6bdf6cac3d5ef3789c661a0753ed743e62686837dcef16ed
Source3:        https://github.com/ggml-org/llama.cpp/archive/%{llama_cpp_commit}.tar.gz#/llama.cpp-%{llama_cpp_commit}.tar.gz
BuildSystem:    cmake

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(conf):  -G Ninja
BuildOption(conf):  -DOLLAMA_VERSION=%{version}
BuildOption(conf):  -DFETCHCONTENT_SOURCE_DIR_LLAMA_CPP=%{_builddir}/llama.cpp-%{llama_cpp_commit}
BuildOption(conf):  -DOLLAMA_LIB_DIR=lib/ollama
%if %{with rocm}
BuildOption(conf):  -DOLLAMA_LLAMA_BACKENDS=rocm_v7_2
BuildOption(conf):  -DCMAKE_HIP_COMPILER=%{rocmllvm_bindir}/clang++
BuildOption(conf):  -DCMAKE_HIP_FLAGS=--offload-jobs=4
BuildOption(conf):  -DAMDGPU_TARGETS=%{rocm_gpu_list_default}
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  go >= 1.26.0
BuildRequires:  go-rpm-macros
BuildRequires:  ninja
BuildRequires:  systemd-rpm-macros
BuildRequires:  go(github.com/agnivade/levenshtein)
BuildRequires:  go(github.com/charmbracelet/bubbletea)
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/containerd/console)
BuildRequires:  go(github.com/d4l3k/go-bfloat16)
BuildRequires:  go(github.com/emirpasic/gods/v2)
BuildRequires:  go(github.com/gin-contrib/cors)
BuildRequires:  go(github.com/gin-gonic/gin)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/mattn/go-sqlite3)
BuildRequires:  go(github.com/olekukonko/tablewriter) <= 0.0.5
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/pkg/browser)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tree-sitter/go-tree-sitter)
BuildRequires:  go(github.com/tree-sitter/tree-sitter-cpp)
BuildRequires:  go(github.com/wk8/go-ordered-map/v2)
BuildRequires:  go(github.com/x448/float16)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/image)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/yaml.v3)
%if %{with rocm}
BuildRequires:  cmake(amd_comgr)
BuildRequires:  cmake(Clang)
BuildRequires:  cmake(hip)
BuildRequires:  cmake(hipblas)
BuildRequires:  cmake(hsa-runtime64)
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

Provides:       libllama-quantize-impl.so()(64bit)
Provides:       libllama-server-impl.so()(64bit)

%{?systemd_requires}
%if %{with rocm}
Requires:       hipblas
Requires:       rocblas
%endif

%description
Ollama is an open-source platform designed to run large language models locally.
It allows users to generate text, assist with coding, and create content privately
and securely on their own devices.

%prep -a
%go_prep
tar -xzf %{SOURCE3} -C %{_builddir}
# Use the compatibility patch and idempotent patch driver shipped by Ollama.
# This prepares the explicit local llama.cpp source exactly as the upstream
# FetchContent path does, without accessing the network during the build.
pushd %{_builddir}/llama.cpp-%{llama_cpp_commit}
cmake \
    -DPATCH_DIR=%{_builddir}/%{_name}-%{version}/llama/compat \
    -DPATCH_LABEL=llama/compat \
    -P %{_builddir}/%{_name}-%{version}/cmake/apply-git-patches.cmake
popd

%conf -p
%go_common
export GOFLAGS="-trimpath -buildmode=pie"
export GOPROXY=off
export GOTOOLCHAIN=local
export GOCACHE=%{_builddir}/go-build-cache

%build -p
%go_common
export GOFLAGS="-trimpath -buildmode=pie"
export GOPROXY=off
export GOTOOLCHAIN=local
export GOCACHE=%{_builddir}/go-build-cache

%install -a
# Use distribution ROCm libraries instead of the runtime copies in upstream payloads.
for backend in %{buildroot}%{_exec_prefix}/lib/ollama %{buildroot}%{_exec_prefix}/lib/ollama/rocm*; do
    rm -f "$backend"/libamd* "$backend"/libdrm* "$backend"/libelf* \
        "$backend"/libhip* "$backend"/libhsa* "$backend"/libnuma* "$backend"/libroc*
    rm -rf "$backend"/rocblas
done
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/ollama.service
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/ollama.conf
# home dir
mkdir -p %{buildroot}%{_var}/lib/ollama

%check
%go_common
cd %{_builddir}/go/src/%{go_import_path}
# Tokenizer fixtures are located through runtime.Caller in the test binary.
unset GOFLAGS
export GOPROXY=off
export GOTOOLCHAIN=local
export GOCACHE=%{_builddir}/go-build-cache
go test -short -timeout=20m ./...

%pre
%sysusers_create_package ollama %{SOURCE2}

%preun
%systemd_preun ollama.service

%post
%systemd_post ollama.service

%postun
%systemd_postun_with_restart ollama.service

%files
%doc README*
%license LICENSE*
%dir %{_exec_prefix}/lib/ollama
%attr(0755,ollama,ollama) %dir %{_var}/lib/ollama/
%{_bindir}/ollama
%{_exec_prefix}/lib/ollama/*
%{_unitdir}/ollama.service
%{_sysusersdir}/ollama.conf

%changelog
%autochangelog
