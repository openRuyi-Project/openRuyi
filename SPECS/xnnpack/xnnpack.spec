# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit0 312eb7e13554ce75d02c5cb27357555f1368f2d1
%global date0 20260211
%global shortcommit0 312eb7e

%global upstream_name XNNPACK

# This project is not well behaved so build in source
%global __cmake_in_source_build 1
# No debug info
%global debug_package %{nil}

Name:           xnnpack
Version:        0+git%{date0}.%{shortcommit0}
Release:        %autorelease
Summary:        High-efficiency floating-point neural network inference operators
License:        BSD-3-Clause
URL:            https://github.com/google/%{upstream_name}
#!RemoteAsset:  sha256:45bbffbc193a1823f979731139cb5fb43076ae85759e63fb31ed928ddbc73bcb
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildSystem:    cmake

# https://github.com/google/XNNPACK/pull/6144
Patch0:         0001-Fix-cmake-for-pthread-and-cpuinfo-with-USE_SYSTEM_LI.patch

BuildOption(conf):  -G Ninja
BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DCMAKE_C_FLAGS=-fPIC
BuildOption(conf):  -DCMAKE_CXX_FLAGS=-fPIC
BuildOption(conf):  -DXNNPACK_BUILD_BENCHMARKS=OFF
BuildOption(conf):  -DXNNPACK_BUILD_LIBRARY=ON
BuildOption(conf):  -DXNNPACK_BUILD_TESTS=OFF
BuildOption(conf):  -DXNNPACK_ENABLE_KLEIDIAI=OFF
BuildOption(conf):  -DXNNPACK_USE_SYSTEM_LIBS=ON
BuildOption(conf):  -DXNNPACK_LIBRARY_TYPE=shared

BuildRequires:  cmake
BuildRequires:  fp16-devel
BuildRequires:  fxdiv-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ninja
BuildRequires:  pkgconfig(libcpuinfo)
# Since 20241217, google uses branched pthreadpool
BuildRequires:  pthreadpool-devel
BuildRequires:  python

%description
XNNPACK is a highly optimized solution for neural network inference on ARM,
x86, WebAssembly, and RISC-V platforms. XNNPACK is not intended for direct
use by deep learning practitioners and researchers; instead it provides
low-level performance primitives for accelerating high-level machine learning
frameworks, such as TensorFlow Lite, TensorFlow.js, PyTorch, ONNX Runtime,
and MediaPipe.

%package        devel
Summary:        Headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}

%prep -a
# version of the *.so
echo "SET_TARGET_PROPERTIES(XNNPACK PROPERTIES SOVERSION \"24.08.14\")" >> CMakeLists.txt

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 644 include/xnnpack.h %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
strip libXNNPACK.so.24.08.14
install -p -m 755 libXNNPACK.so.24.08.14 %{buildroot}%{_libdir}
cd %{buildroot}%{_libdir}
ln -s libXNNPACK.so.24.08.14 libXNNPACK.so

%files
%license LICENSE
%{_libdir}/libXNNPACK.so.*

%files devel
%doc README.md
%{_includedir}/xnnpack.h
%{_libdir}/libXNNPACK.so

%changelog
%autochangelog
