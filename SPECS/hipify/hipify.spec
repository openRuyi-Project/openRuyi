# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global rocm_release 7.1
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

# This is a clang tool so best to build with clang
%global toolchain clang

Name:           hipify
Version:        %{rocm_version}
Release:        %autorelease
Summary:        Convert CUDA to HIP
License:        MIT
URL:            https://github.com/ROCm/HIPIFY
#!RemoteAsset
Source0:        %{url}/archive/rocm-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf): -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/clang++
BuildOption(conf): -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/clang
BuildOption(conf): -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/..

Patch0:         0001-prepare-hipify-cmake.patch
Patch1:         0002-clang21-compatibility-fix.patch

BuildRequires:  chrpath
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  clang-tools-extra
BuildRequires:  clang-tools-extra-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  lld
BuildRequires:  lld-devel
BuildRequires:  llvm
BuildRequires:  llvm-devel
BuildRequires:  llvm-static
BuildRequires:  perl
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rocm-llvm-macros


%description
HIPIFY is a set of tools to translate CUDA source code into portable
HIP C++ automatically.

%check
echo "void f(int *a, const cudaDeviceProp *b) { cudaChooseDevice(a,b); }" > b.cu
echo "void f(int *a, const hipDeviceProp_t *b) { hipChooseDevice(a,b); }" > e.hip
./bin/hipify-perl b.cu -o t.hip
diff e.hip t.hip

%install -a
rm -rf %{buildroot}/usr/hip
# Fix executable perm:
chmod a+x %{buildroot}%{_bindir}/*
# Fix script shebang (Fedora doesn't allow using "env"):
sed -i 's|\(/usr/bin/\)env perl|\1perl|' %{buildroot}%{_bindir}//hipify-perl

# Fix
# /usr/bin/hipify-clang: error while loading shared libraries: libclang-cpp.so.19.0git
chrpath %{buildroot}%{_bindir}/hipify-clang -r %rocmllvm_libdir

rm -rf %{buildroot}%{_includedir}

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/hipify-clang
%{_bindir}/hipify-perl
%{_libexecdir}/hipify

%changelog
%autochangelog
