# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond docs 0
%bcond tests 1

Name:           libpkgmanifest
Version:        0.5.9
Release:        %autorelease
Summary:        Library for working with RPM manifests
License:        LGPL-2.1-or-later
URL:            https://github.com/rpm-software-management/libpkgmanifest
#!RemoteAsset
Source0:        https://github.com/rpm-software-management/libpkgmanifest/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DWITH_CODE_COVERAGE=OFF
BuildOption(conf):  -DVERSION_MAJOR=0
BuildOption(conf):  -DVERSION_MINOR=5
BuildOption(conf):  -DVERSION_PATCH=9
BuildOption(conf):  -DWITH_PYTHON=ON
%if %{with docs}
BuildOption(conf):  -DWITH_DOCS=ON
%else
BuildOption(conf):  -DWITH_DOCS=OFF
%endif
%if %{with tests}
BuildOption(conf):  -DWITH_TESTS=ON
%else
BuildOption(conf):  -DWITH_TESTS=OFF
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(python3)
BuildRequires:  swig
%if %{with tests}
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
%endif
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  python3-sphinx
%endif

%description
%{name} is a C++ library for parsing and generating RPM manifests.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%package     -n python-%{name}
Summary:        Python bindings for the %{name} library
Provides:       python3-%{name} = %{version}-%{release}
%python_provide python3-%{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-%{name}
Python bindings for the %{name} library.

%files
%license LICENSE
%doc README.md
%{_libdir}/libpkgmanifest.so.*

%files devel
%doc docs/design
%{_includedir}/libpkgmanifest/
%{_libdir}/libpkgmanifest.so
%{_libdir}/pkgconfig/libpkgmanifest.pc

%files -n python-libpkgmanifest
%{python3_sitearch}/libpkgmanifest/
%{python3_sitearch}/libpkgmanifest-*.dist-info/

%changelog
%autochangelog
