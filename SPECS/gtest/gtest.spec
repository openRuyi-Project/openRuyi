# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gtest
Version:        1.17.0
Release:        %autorelease
Summary:        Google C++ testing framework
License:        BSD-3-Clause and Apache-2.0
URL:            https://github.com/google/googletest
#!RemoteAsset
Source:         https://github.com/google/googletest/releases/download/v%{version}/googletest-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DPYTHON_EXECUTABLE=%{__python3}
BuildOption(conf):  -Dgtest_build_tests=ON

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(python3)

%description
This package is Google C++ testing framework,It can be compiled for
a variety of platforms.Google Test is a unit testing library for
the C++ programming language, based on the xUnit architecture,
allowing unit-testing of C sources as well as C++ with minimal source modification.

%package        devel
Summary:        Gtest development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmock%{?_isa} = %{version}-%{release}

%description    devel
This package is libraries and head files for google testing framework.

%package     -n gmock
Summary:        Google framework for writing and using C++ mock classes
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n gmock
The package is Google's framework for writing and using C++ mock classes.
It can help you derive better designs of your system and write better tests.
Gmock is a suite of testing tools developed by Google.
It is often used in combination with GTest.

%package     -n gmock-devel
Summary:        Gmock development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n gmock-devel
The package is libraries and head files for google mocking framework.

%prep
%autosetup -p1 -n googletest-%{version}

%files
%license LICENSE
%{_libdir}/libgtest*.%{version}

%files -n gtest-devel
%doc CONTRIBUTORS README.md
%doc docs/
%{_includedir}/gtest/
%{_libdir}/libgtest*.so
%{_libdir}/cmake/GTest/
%{_libdir}/pkgconfig/gtest*

%files -n gmock
%license LICENSE
%{_libdir}/libgmock*.%{version}

%files -n gmock-devel
%doc CONTRIBUTORS README.md
%doc docs/
%{_includedir}/gmock/
%{_libdir}/libgmock*.so
%{_libdir}/pkgconfig/gmock*

%changelog
%autochangelog
