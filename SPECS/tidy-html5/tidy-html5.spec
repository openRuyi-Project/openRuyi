# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tidy-html5
Version:        5.8.0
Release:        %autorelease
Summary:        HTML syntax checker and reformatter
License:        W3C
URL:            https://github.com/htacg/tidy-html5
#!RemoteAsset
Source:         https://github.com/htacg/tidy-html5/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_SHARED_LIB:BOOL=ON
BuildOption(conf):  -DBUILD_STATIC_LIB:BOOL=OFF
BuildOption(conf):  -DTIDY_CONSOLE_SHARED:BOOL=ON
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libxslt

%description
Tidy is a console application which corrects and cleans up HTML and XML
documents by fixing markup errors and upgrading legacy code to modern
standards.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%install -a
find %{buildroot} -type f -name "*.a" -delete -print

%files
%license README/LICENSE.md
%doc README.md
%{_bindir}/tidy
%{_mandir}/man1/tidy.1*
%{_libdir}/libtidy.so.5*

%files devel
%{_includedir}/*.h
%{_libdir}/libtidy.so
%{_libdir}/pkgconfig/tidy.pc

%changelog
%{?autochangelog}
