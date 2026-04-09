# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:          pcre2
Version:       10.45
Release:       %autorelease
Summary:       A library for Perl-compatible regular expressions
License:       BSD-3-Clause WITH PCRE2-exception
URL:           https://pcre2project.github.io/pcre2/
VCS:           git:https://github.com/PCRE2Project/pcre2.git
#!RemoteAsset
Source0:       https://github.com/PCRE2Project/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildSystem:   autotools

BuildOption(conf):  --enable-jit
BuildOption(conf):  --enable-pcre2-16
BuildOption(conf):  --enable-pcre2-32
BuildOption(conf):  --enable-pcre2grep-libbz2
BuildOption(conf):  --enable-pcre2grep-libz
BuildOption(conf):  --enable-pcre2test-libreadline
BuildOption(conf):  --enable-unicode

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib)

%description
PCRE2 is a re-working of the original PCRE library to provide a new API.
This package contains the runtime libraries (8-bit, 16-bit, 32-bit, and POSIX)
and the `pcre2grep` and `pcre2test` command-line tools.

%package        devel
Summary:        Development files for pcre2
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains header files, development libraries, and API documentation
for compiling applications that use the PCRE2 library.

%conf -p
autoreconf -fiv

%files
%license LICENCE.md
%doc AUTHORS.md ChangeLog NEWS README
%{_libdir}/libpcre2-8.so.0*
%{_libdir}/libpcre2-16.so.0*
%{_libdir}/libpcre2-32.so.0*
%{_libdir}/libpcre2-posix.so.3*
%{_bindir}/pcre2grep
%{_bindir}/pcre2test
%{_mandir}/man1/*

%files devel
%doc %{_docdir}/pcre2/
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/pcre2-config.1.gz
%{_mandir}/man3/*
%{_bindir}/pcre2-config

%changelog
%autochangelog
