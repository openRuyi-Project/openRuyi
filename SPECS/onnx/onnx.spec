# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           onnx
Version:        1.22.0
Release:        %autorelease
Summary:        Open standard for machine learning interoperability
License:        Apache-2.0
URL:            https://github.com/onnx/onnx
#!RemoteAsset:  sha256:70bb8b25cf31ea9b1d9f94baacfdc8c4fa27a760f9a10f5d93881bc9eede5fbc
Source0:        https://github.com/onnx/onnx/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

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
Requires:       abseil-cpp-devel
Requires:       protobuf-devel

%description    devel
Development files for %{name}.

%package     -n python-onnx
Summary:        Python 3 bindings for %{name}
Provides:       python3-onnx
%python_provide python3-onnx

%description -n python-onnx
Python 3 bindings for %{name}.

%prep -a
# Upstream pins the minimum tested protobuf release for isolated PyPI builds.
# The runtime metadata supports newer protobuf versions, as provided by openRuyi.
sed -i 's/"protobuf==4.25.1"/"protobuf>=4.25.1"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build -a
export CMAKE_ARGS="-Dnanobind_DIR=%{python3_sitelib}/nanobind/cmake \
-DONNX_USE_LITE_PROTO=ON \
-DONNX_USE_PROTOBUF_SHARED_LIBS=ON \
-DCMAKE_SKIP_RPATH=ON"

# Build the official static C++ targets separately for consumers that use ONNX
# internals.  The Python wheel's private build directory is intentionally
# ephemeral and cannot be used as a packaged artifact source.
%{__cmake} -S . -B onnx-static-build \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DCMAKE_INSTALL_INCLUDEDIR=include \
  -DBUILD_SHARED_LIBS=OFF \
  -DONNX_BUILD_PYTHON=OFF \
  -DONNX_USE_LITE_PROTO=ON \
  -DONNX_USE_PROTOBUF_SHARED_LIBS=ON \
  -DONNX_ML=ON
%{__cmake} --build onnx-static-build --target onnx onnx_proto --parallel %{_smp_build_ncpus}

%pyproject_wheel

%install -a
%pyproject_install
%pyproject_save_files onnx

# Install the official static build's archives, headers and generated CMake
# targets for consumers such as ONNX Runtime.  The shared libraries from the
# Python build remain available as the runtime ABI.
%{__cmake} --install onnx-static-build --prefix "%{buildroot}%{_prefix}"
install -pm 0644 onnx/*.proto onnx/*.proto3 \
  "%{buildroot}%{_includedir}/onnx/"

%check
# TODO: skip tests as some deps we don't have yet.
# export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}

%files
%{_libdir}/libonnx.so
%{_libdir}/libonnx_proto.so

%files devel
%{_libdir}/cmake/ONNX
%{_includedir}/onnx/
%{_libdir}/libonnx.a
%{_libdir}/libonnx_proto.a

%files -n python-onnx -f %{pyproject_files}
%{_bindir}/backend-test-tools
%{_bindir}/check-model
%{_bindir}/check-node

%changelog
%autochangelog
