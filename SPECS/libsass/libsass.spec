# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libsass
Version:        3.6.6
Release:        %autorelease
Summary:        C/C++ port of the Sass CSS precompiler
License:        MIT AND BSL-1.0
URL:            https://github.com/sass/libsass
#!RemoteAsset:  sha256:11f0bb3709a4f20285507419d7618f3877a425c0131ea8df40fe6196129df15d
Source0:        https://github.com/sass/libsass/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

%description
Libsass is a C/C++ port of the Sass CSS precompiler. The original version was
written in Ruby, but this version is meant for efficiency and portability.

This library strives to be light, simple, and easy to build and integrate with
a variety of platforms and languages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%conf -p
export LIBSASS_VERSION=%{version}
autoreconf -fiv

%files
%license LICENSE
%doc Readme.md SECURITY.md
%{_libdir}/libsass.so.*

%files devel
%{_includedir}/sass.h
%{_includedir}/sass2scss.h
%{_includedir}/sass/
%{_libdir}/libsass.so
%{_libdir}/pkgconfig/libsass.pc

%changelog
%autochangelog
