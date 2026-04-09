# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           onnx
Version:        1.20.1
Release:        %autorelease
Summary:        Open standard for machine learning interoperability
License:        Apache-2.0
URL:            https://github.com/onnx/onnx
#!RemoteAsset:  sha256:9bcd6473c689b1ac3aeba8df572891756e01c1a151ae788df5cbc7a4499e5db5
Source:         https://github.com/onnx/onnx/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

# Build shared libraries instead of static
Patch0:         0001-Build-shared-libraries.patch
# Add onnxruntime_fix.h for compatibility with onnxruntime
Patch1:         0002-Add-onnxruntime-fix.patch

BuildOption(conf):  -DBUILD_ONNX_PYTHON=ON
BuildOption(conf):  -DPYTHON_EXECUTABLE=%{__python3}
BuildOption(conf):  -DPY_EXT_SUFFIX=%{python3_ext_suffix}
BuildOption(conf):  -DPY_SITEARCH=%{python3_sitearch}

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pybind11)
BuildRequires:  pkgconfig(pybind11)
BuildRequires:  python3dist(nanobind)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(protobuf)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(ml-dtypes)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  pyproject-rpm-macros

%description
%{name} provides an open source format for AI models, both deep learning and
traditional ML. It defines an extensible computation graph model, as well as
definitions of built-in operators and standard data types.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%package     -n python-onnx
Summary:        Python 3 bindings for %{name}
Provides:       python3-onnx
%python_provide python3-onnx

%description -n python-onnx
Python 3 bindings for %{name}.

%generate_buildrequires
%pyproject_buildrequires requirements-reference.txt

%build -a
export CMAKE_ARGS="-Dnanobind_DIR=%{python3_sitelib}/nanobind/cmake \
-DONNX_USE_LITE_PROTO=OFF \
-DONNX_USE_PROTOBUF_SHARED_LIBS=ON \
-DCMAKE_SKIP_RPATH=ON"

%pyproject_wheel

%install -a
%pyproject_install
%pyproject_save_files onnx

install -p "./onnx/"*.proto -t "%{buildroot}/%{_includedir}/onnx/"

%check
# TODO: skip tests as some deps we don't have yet.
# export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}

%files
%{_libdir}/libonnx.so.*
%{_libdir}/libonnx_proto.so.*

%files devel
%{_libdir}/libonnx.so
%{_libdir}/libonnx_proto.so
%{_libdir}/cmake/ONNX
%{_includedir}/onnx/

%files -n python-onnx -f %{pyproject_files}
%{_bindir}/backend-test-tools
%{_bindir}/check-model
%{_bindir}/check-node

%changelog
%autochangelog
