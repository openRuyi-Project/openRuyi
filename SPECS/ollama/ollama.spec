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
%define llama_cpp_commit 391fac16460f15233a7740550d858ac96df3419d

# Ollama bundles some ggml libs
# They should be kept private and the scans of these files should be disabled
%global __provides_exclude lib.*\\.so(\\..*)?
%global __requires_exclude libggml-.*\\.so(\\..*)?

Name:           ollama
Version:        0.34.2
Release:        %autorelease
Summary:        Get up and running with OpenAI gpt-oss, DeepSeek-R1, Gemma 3 and other models.
License:        MIT
URL:            https://ollama.com/
VCS:            git:https://github.com/ollama/ollama
#!RemoteAsset:  sha256:3fb06dc496f321749423792066f299205c433b815540c1f23f18368540401640
Source0:        https://github.com/ollama/ollama/archive/refs/tags/v%{version}.tar.gz
Source1:        ollama.service
Source2:        ollama.sysusers
#!RemoteAsset:  sha256:82977400c28b7486f90126a5592c9ff585f9b2ae0a3be2c9ab77464e5eef78cc
Source3:        https://github.com/ggml-org/llama.cpp/archive/%{llama_cpp_commit}.tar.gz#/llama.cpp-%{llama_cpp_commit}.tar.gz
BuildSystem:    golang

Patch2000:      2000-stabilize-codex-app-request-count-test.patch

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  go >= 1.26.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/agnivade/levenshtein)
BuildRequires:  go(github.com/charmbracelet/bubbletea)
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/containerd/console)
BuildRequires:  go(github.com/emirpasic/gods/v2)
BuildRequires:  go(github.com/gin-contrib/cors)
BuildRequires:  go(github.com/gin-gonic/gin)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/ledongthuc/pdf)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/mattn/go-sqlite3)
BuildRequires:  go(github.com/olekukonko/tablewriter) < 1.0.0
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/pkg/browser)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tkrajina/typescriptify-golang-structs)
BuildRequires:  go(github.com/tree-sitter/go-tree-sitter)
BuildRequires:  go(github.com/tree-sitter/tree-sitter-cpp)
BuildRequires:  go(github.com/wk8/go-ordered-map/v2)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/image)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  ninja
BuildRequires:  systemd-rpm-macros
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

# These private, unversioned llama.cpp helper libraries are shipped in this
# package.  The private-library filter above intentionally suppresses their
# automatic Provides, so declare the exact capabilities required by the
# packaged helper executables.
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

# Ollama use a mix build of cmake and go.
# Ollama binary built by go will use dlopen to load *.so built by cmake.
# Building order of go/cmake is not important.
%build -a
%if %{with rocm}
# Ollama's ROCm preset uses the retired -parallel-jobs spelling. LLVM 22
# provides the equivalent --offload-jobs option for parallel device builds.
%endif
%cmake \
    -G Ninja \
    -W no-dev \
    -DOLLAMA_VERSION=%{version} \
    -DFETCHCONTENT_SOURCE_DIR_LLAMA_CPP=%{_builddir}/llama.cpp-%{llama_cpp_commit} \
    -DCMAKE_INSTALL_LIBDIR:PATH=lib \
    -DCMAKE_INSTALL_FULL_LIBDIR:PATH=/usr/lib \
    -DLIB_INSTALL_DIR:PATH=/usr/lib \
    -DLIB_SUFFIX= \
%if %{with rocm}
    -DOLLAMA_LLAMA_BACKENDS=rocm_v7_2 \
    -DCMAKE_HIP_COMPILER=%{rocmllvm_bindir}/clang++ \
    -DCMAKE_HIP_FLAGS=--offload-jobs=4 \
    -DAMDGPU_TARGETS=%{rocm_gpu_list_default}
%endif
%cmake_build

%install
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
