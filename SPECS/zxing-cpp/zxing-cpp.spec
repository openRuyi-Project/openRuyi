# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           zxing-cpp
Version:        3.2.0
Release:        %autorelease
Summary:        C++ port of the ZXing barcode image processing library
License:        Apache-2.0 AND BSD-3-Clause AND MIT
URL:            https://github.com/zxing-cpp/zxing-cpp/
#!RemoteAsset:  sha256:eacc2495f452be751d9dd453f4d6cccd0e9a40131e002bcf54d2580ce5c19ad8
Source:         https://github.com/zxing-cpp/zxing-cpp/releases/download/v%{version}/zxing-cpp-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DZXING_WRITERS=BOTH
BuildOption(conf):  -DZXING_DEPENDENCIES=LOCAL

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(stb)

Provides:       bundled(zint) = 2.16.0
Provides:       bundled(zueci) = 1.0.1

%description
ZXing-C++ ("zebra crossing") is an open-source,
multi-format linear/matrix barcode image processing library implemented in C++.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n python-%{name}
Summary:        Python bindings for the %{name} barcode library
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(nanobind)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(scikit-build-core)
BuildRequires:  python3dist(wheel)
Provides:       python3-%{name} = %{version}-%{release}
Provides:       python3-%{name}%{?_isa} = %{version}-%{release}
%python_provide python3-%{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-%{name}
The python-%{name} package contains Python bindings for the %{name} barcode library.

%build -a
pushd wrappers/python
export SKBUILD_CMAKE_ARGS="-DZXING_WRITERS=BOTH;-DZXING_DEPENDENCIES=LOCAL;-DCMAKE_PREFIX_PATH=$(%{python3} -m nanobind --cmake_dir)"
%pyproject_wheel
popd

%install -a
pushd wrappers/python
%pyproject_install
%pyproject_save_files zxingcpp
popd

%files
%license LICENSE
%{_libdir}/libZXing.so.*
%{_bindir}/ZXingReader
%{_bindir}/ZXingWriter

%files devel
%doc README.md
%{_includedir}/ZXing/
%{_libdir}/libZXing.so
%{_libdir}/cmake/ZXing/
%{_libdir}/pkgconfig/zxing.pc

%files -n python-zxing-cpp -f %{pyproject_files}

%changelog
%autochangelog
