# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           onnxruntime
Version:        1.30.0
Release:        %autorelease
Summary:        A cross-platform inferencing and training accelerator
License:        MIT AND Apache-2.0 AND BSL-1.0 AND BSD-3-Clause
URL:            https://github.com/microsoft/onnxruntime
#!RemoteAsset:  sha256:f6681ecbddf53898adf0cc9e8e9e84657485b84d2eca3c8aa353de6d7dd417ef
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# actually, both cmake and pyproject are used to build this project
BuildSystem:    cmake

BuildOption(conf):  -Donnxruntime_BUILD_BENCHMARKS=OFF
BuildOption(conf):  -Donnxruntime_BUILD_SHARED_LIB=ON
BuildOption(conf):  -Donnxruntime_BUILD_UNIT_TESTS=ON
BuildOption(conf):  -Donnxruntime_ENABLE_PYTHON=ON
BuildOption(conf):  -Donnxruntime_ENABLE_ABSEIL=ON
BuildOption(conf):  -Donnxruntime_USE_FULL_PROTOBUF=OFF
BuildOption(conf):  -Donnxruntime_USE_NEURAL_SPEED=OFF
BuildOption(conf):  -Donnxruntime_USE_PREINSTALLED_EIGEN=ON
BuildOption(conf):  -Deigen_SOURCE_PATH=%{_includedir}/eigen3
BuildOption(conf):  -S cmake
BuildOption(conf):  -DCMAKE_INSTALL_LIBDIR=%{_lib}
BuildOption(conf):  -DCMAKE_INSTALL_INCLUDEDIR=include
BuildOption(conf):  -Donnxruntime_ENABLE_CPUINFO=ON
BuildOption(conf):  -Donnxruntime_INSTALL_UNIT_TESTS=OFF
# FIXME: Avoid build failures with gcc >= 15.
%ifarch riscv64
BuildOption(conf):  -DCMAKE_CXX_FLAGS="-Wno-error=uninitialized -Wno-error=sfinae-incomplete -Wno-error=maybe-uninitialized -Wno-error=array-bounds"
%else
BuildOption(conf):  -DCMAKE_CXX_FLAGS="-Wno-error=uninitialized -Wno-error=sfinae-incomplete -Wno-error=maybe-uninitialized"
%endif
BuildOption(conf):  -DCMAKE_C_FLAGS="-Wno-error=uninitialized"

BuildRequires:  cmake
BuildRequires:  gcc-c++
# Use ONNX 1.22 through ONNX Runtime's upstream FetchContent find-package path.
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
BuildRequires:  patch

%patchlist
# Don't install test binaries to system directories
0001-don-t-install-tests.patch
# Use the system FlatBuffers package and provide the target name expected upstream
0002-system-flatbuffers.patch
# Use system protobuf library instead of bundled version
0003-system-protobuf.patch
# Use the system SafeInt headers instead of downloading the bundled source
0004-system-safeint.patch
# Add version suffix to libonnxruntime_providers_shared.so for proper library versioning
0005-versioned-onnxruntime_providers_shared.patch
# Use system date and mp11 libraries instead of bundled versions
0006-system-date-and-mp11.patch
# Use system cpuinfo library instead of bundled version
0007-system-cpuinfo.patch
# Disable locale-dependent tests that may fail in build environments
0008-disable-locale-tests.patch
# Prevent CMake from downloading dependencies during build
0009-disable-downloading-dependencies.patch
# Use the system Eigen3 package instead of FetchContent
0010-system-eigen3.patch

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

%check -p
# These tests compare exact std::default_random_engine sequences, which are implementation-specific.
export GTEST_FILTER='-SamplingTest.Gpt2Sampling_CPU:Random.MultinomialGoodCase:Random.MultinomialDefaultDType'

%files
%doc ThirdPartyNotices.txt
%license LICENSE
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
