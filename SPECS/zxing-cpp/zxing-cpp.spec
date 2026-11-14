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

BuildOption(conf):  -DZXING_WRITERS=OLD
BuildOption(conf):  -DZXING_DEPENDENCIES=LOCAL

BuildRequires:  cmake
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(stb)

Provides:       %{name}(qr-writer) = %{version}-%{release}

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
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(opencv)
BuildRequires:  python3dist(pillow)
BuildRequires:  chrpath
Provides:       python3-%{name} = %{version}-%{release}
Provides:       python3-%{name}%{?_isa} = %{version}-%{release}
%python_provide python3-%{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-%{name}
The python-%{name} package contains Python bindings for the %{name} barcode library.

%prep -a
sed -r -i 's@(COMMAND )python@\1%{python3}@' wrappers/python/CMakeLists.txt
sed -i '1i set(ZXING_WRITERS OLD CACHE STRING "" FORCE)' wrappers/python/CMakeLists.txt
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

# Upstream's unit-test configuration exposes private symbols for its test binary.
%check
%cmake -B build-tests -DBUILD_SHARED_LIBS=OFF -DZXING_DEPENDENCIES=LOCAL -DZXING_EXAMPLES=OFF -DZXING_UNIT_TESTS=ON -DZXING_WRITERS=OLD
cmake --build build-tests --target UnitTest --parallel %{_smp_build_ncpus}
ctest --test-dir build-tests --output-on-failure -R '^UnitTest$'
# Exercise the installed Python binding with upstream barcode round-trip tests.
PYTHONPATH=%{buildroot}%{python3_sitearch} %{python3} wrappers/python/test.py -v

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
