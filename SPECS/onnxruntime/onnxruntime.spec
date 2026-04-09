# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           onnxruntime
Version:        1.24.1
Release:        %autorelease
Summary:        A cross-platform inferencing and training accelerator
License:        MIT AND Apache-2.0 AND BSL-1.0 AND BSD-3-Clause
URL:            https://github.com/microsoft/onnxruntime
#!RemoteAsset:  sha256:65bc043f5c1f386fc3e04aa2efdab91ac53f5195d4f78fc7e22eb0fe9caeadc6
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# actually, both cmake and pyproject are used to build this project
BuildSystem:    cmake

BuildOption(conf):  -Donnxruntime_BUILD_BENCHMARKS=OFF
BuildOption(conf):  -Donnxruntime_BUILD_SHARED_LIB=ON
BuildOption(conf):  -Donnxruntime_BUILD_UNIT_TESTS=ON
BuildOption(conf):  -Donnxruntime_ENABLE_PYTHON=ON
BuildOption(conf):  -Donnxruntime_ENABLE_ABSEIL=ON
BuildOption(conf):  -Donnxruntime_ENABLE_ABSEIL=ON
BuildOption(conf):  -Donnxruntime_USE_FULL_PROTOBUF=ON
BuildOption(conf):  -Donnxruntime_USE_NEURAL_SPEED=OFF
BuildOption(conf):  -Donnxruntime_USE_PREINSTALLED_EIGEN=ON
BuildOption(conf):  -Deigen_SOURCE_PATH=%{_includedir}/eigen3
BuildOption(conf):  -S cmake
BuildOption(conf):  -DCMAKE_INSTALL_LIBDIR=%{_lib}
BuildOption(conf):  -DCMAKE_INSTALL_INCLUDEDIR=include
BuildOption(conf):  -Donnxruntime_ENABLE_CPUINFO=ON
BuildOption(conf):  -Donnxruntime_INSTALL_UNIT_TESTS=OFF
# disable Werror uninitialized to avoid build failures
BuildOption(conf):  -DCMAKE_CXX_FLAGS="-Wno-error=uninitialized"
BuildOption(conf):  -DCMAKE_C_FLAGS="-Wno-error=uninitialized"

BuildRequires:  cmake
BuildRequires:  gcc-c++
# this package does not provide pkgconfig
BuildRequires:  onnx-devel
# this package does not ship with a single all-in-one pkgconfig
BuildRequires:  abseil-cpp-devel
# this package does not provide pkgconfig
BuildRequires:  boost-devel
BuildRequires:  bzip2
BuildRequires:  pkgconfig(libcpuinfo)
BuildRequires:  pkgconfig(date)
BuildRequires:  pkgconfig(flatbuffers)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  cmake(Microsoft.GSL)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
BuildRequires:  pkgconfig(re2)
BuildRequires:  safeint
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  python3dist(pybind11)
BuildRequires:  dlpack

%patchlist
# Don't install test binaries to system directories
0001-don-t-install-tests.patch
# Use system flatbuffers library instead of bundled version
0002-system-flatbuffers.patch
# Use system protobuf library instead of bundled version
0003-system-protobuf.patch
# Use system onnx library instead of bundled version
0004-system-onnx.patch
# Use system SafeInt library instead of bundled version
0005-system-safeint.patch
# Add version suffix to libonnxruntime_providers_shared.so for proper library versioning
0006-versioned-onnxruntime_providers_shared.patch
# Suppress GCC false positive warnings that cause build failures
0007-gcc-false-positives.patch
# Disable PyTorch-related tests that require PyTorch installation
0008-disable-pytorch-tests.patch
# Use system date and mp11 libraries instead of bundled versions
0009-system-date-and-mp11.patch
# Use system cpuinfo library instead of bundled version
0010-system-cpuinfo.patch
# Fix compatibility issues between ONNX and ONNX Runtime
0011-onnx-onnxruntime-fix.patch
# Use system Python instead of downloading Python during build
0012-system-python.patch
# Disable locale-dependent tests that may fail in build environments
0013-disable-locale-tests.patch
# Prevent CMake from downloading dependencies during build
0014-disable-downloading-dependencies.patch
# Use system Eigen3 library instead of bundled version
0015-system-eigen3.patch
# Disable additional tests that are not suitable for package builds
0016-disable-tests.patch
# Ignore deprecated Thrust library warnings in CUDA code
0017-onnxruntime-ignore-deprecated-thrust-warnings.patch
# Add ROCm compatibility: CUBLAS_GEMM_DEFAULT_TENSOR_OP is not supported in ROCm
0018-onnxruntime-rocm-no-CUBLAS_GEMM_DEFAULT_TENSOR_OP-su.patch

%description
%{name} is a cross-platform inferencing and training accelerator compatible
with many popular ML/DNN frameworks, including PyTorch, TensorFlow/Keras,
scikit-learn, and more.

%package        devel
Summary:        The development part of the %{name} package
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
The development part of the %{name} package

%package     -n python-%{name}
Summary:        %{summary}
Requires:       %{name}%{_isa} = %{version}-%{release}

Provides:       python3-%{name}
%python_provide python3-%{name}

%description -n python-onnxruntime
Python bindings for the %{name} package

%build -p
# Re-compile flatbuffers schemas with the system flatc
%{__python3} onnxruntime/core/flatbuffers/schema/compile_schema.py --flatc %{_bindir}/flatc
%{__python3} onnxruntime/lora/adapter_format/compile_schema.py --flatc %{_bindir}/flatc

%build -a
cp -R ./%{__cmake_builddir}/onnxruntime/* ./onnxruntime
cp ./%{__cmake_builddir}/requirements.txt ./requirements.txt
%pyproject_wheel

%install -a
mkdir -p "%{buildroot}/%{_docdir}/"
cp --preserve=timestamps -r "./docs/" "%{buildroot}/%{_docdir}/%{name}"
%pyproject_install
%pyproject_save_files onnxruntime

ln -s "../../../../libonnxruntime_providers_shared.so.%{version}" "%{buildroot}/%{python3_sitearch}/onnxruntime/capi/libonnxruntime_providers_shared.so"

%files
%license LICENSE
%doc ThirdPartyNotices.txt
%{_libdir}/libonnxruntime.so.%{version}
%{_libdir}/libonnxruntime_providers_shared.so.%{version}

%files devel
%{_docdir}/%{name}
%dir %{_includedir}/onnxruntime/
%{_includedir}/onnxruntime/*
%{_libdir}/libonnxruntime.so*
%{_libdir}/libonnxruntime_providers_shared.so
%{_libdir}/pkgconfig/libonnxruntime.pc
%{_libdir}/cmake/onnxruntime/*

%files -n python-%{name} -f %{pyproject_files}
%{_bindir}/onnxruntime_test
%{python3_sitearch}/onnxruntime/capi/libonnxruntime_providers_shared.so

%changelog
%autochangelog
