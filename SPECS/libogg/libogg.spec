# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libogg
Version:        1.3.6
Release:        %autorelease
Summary:        The Ogg bitstream file format library
License:        BSD-3-Clause
URL:            https://github.com/xiph/ogg
#!RemoteAsset
Source:         https://downloads.xiph.org/releases/ogg/libogg-%{version}.tar.xz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make

%description
Libogg is a library for manipulating Ogg bitstream file formats. It supports
both creating Ogg bitstreams and extracting packets from them.

%package        devel
Summary:        Development files and documentation for libogg
Requires:       %{name}%{?_isa} = %{version}
Requires:       pkgconfig
Requires:       automake

%description devel
This package contains the header files, libraries, documentation, and other
files needed to develop applications that use the libogg library.

%install -a
install -d -m 755 %{buildroot}%{_datadir}/aclocal
cp -pr ogg.m4 %{buildroot}%{_datadir}/aclocal/

%files
%license COPYING
%doc AUTHORS CHANGES README.md
%{_libdir}/libogg.so.0*

%files devel
%doc %{_docdir}/ogg
%{_includedir}/ogg/
%{_libdir}/libogg.so
%{_libdir}/pkgconfig/ogg.pc
%{_datadir}/aclocal/ogg.m4
%{_libdir}/cmake/Ogg/

%changelog
%{?autochangelog}
