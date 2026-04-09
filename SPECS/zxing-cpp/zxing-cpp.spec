# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           zxing-cpp
Version:        3.0.2
Release:        %autorelease
Summary:        C++ port of the ZXing barcode image processing library
License:        Apache-2.0 AND MIT
URL:            https://github.com/zxing-cpp/zxing-cpp/
#!RemoteAsset:  sha256:e957f13e2ad4e31badb3d9af3f6ba8999a3ca3c9cc4d6bafc98032f9cce1a090
Source:         https://github.com/zxing-cpp/zxing-cpp/releases/download/v%{version}/zxing-cpp-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DZXING_WRITERS=OFF

BuildRequires:  cmake
BuildRequires:  pkgconfig(stb)

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
Provides:       python3-%{name} = %{version}-%{release}
%python_provide python3-%{name}
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  chrpath
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-%{name}
The python-%{name} package contains Python bindings for the %{name} barcode library.

%prep -a
sed -r -i 's@(COMMAND )python@\1%{python3}@' wrappers/python/CMakeLists.txt
sed -i '1i set(ZXING_WRITERS OFF CACHE BOOL "" FORCE)' wrappers/python/CMakeLists.txt
sed -r -i '/cmake/d' wrappers/python/pyproject.toml

%build -a
pushd wrappers/python
%pyproject_wheel
popd

%install -a
pushd wrappers/python
%pyproject_install
chrpath --delete %{buildroot}%{python3_sitearch}/zxingcpp.*.so
%pyproject_save_files zxingcpp
popd

# No image file, test not executed.
%check

%files
%license LICENSE
%{_libdir}/libZXing.so.*
%{_bindir}/ZXingReader

%files devel
%doc README.md
%{_includedir}/ZXing/
%{_libdir}/libZXing.so
%{_libdir}/cmake/ZXing/
%{_libdir}/pkgconfig/zxing.pc

%files -n python-zxing-cpp -f %{pyproject_files}

%changelog
%autochangelog
