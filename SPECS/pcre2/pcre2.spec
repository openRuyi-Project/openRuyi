# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:          pcre2
Version:       10.45
Release:       %autorelease
Summary:       A library for Perl-compatible regular expressions
License:       BSD-3-Clause WITH PCRE2-exception
URL:           https://pcre2project.github.io/pcre2/
#!RemoteAsset
Source0:       https://github.com/PCRE2Project/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2

BuildSystem:   autotools

BuildOption(conf): --enable-jit
BuildOption(conf): --enable-pcre2-16
BuildOption(conf): --enable-pcre2-32
BuildOption(conf): --enable-pcre2grep-libbz2
BuildOption(conf): --enable-pcre2grep-libz
BuildOption(conf): --enable-pcre2test-libreadline
BuildOption(conf): --enable-unicode


BuildRequires:  make, gcc-c++, autoconf, automake, libtool
BuildRequires:  bzip2-devel, readline-devel
BuildRequires:  pkgconfig(zlib)


%description
PCRE2 is a re-working of the original PCRE library to provide a new API.
This package contains the runtime libraries (8-bit, 16-bit, 32-bit, and POSIX)
and the `pcre2grep` and `pcre2test` command-line tools.
Requires:      bzip2-libs, readline, zlib
# Provides all the different library sonames.
Provides:      libpcre2-8.so.0%{?_isa}
Provides:      libpcre2-16.so.0%{?_isa}
Provides:      libpcre2-32.so.0%{?_isa}
Provides:      libpcre2-posix.so.3%{?_isa}

# The `-devel` package for developers.
%package devel
Summary:       Development files for pcre2
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains header files, development libraries, and API documentation
for compiling applications that use the PCRE2 library.

%conf -p
autoreconf -fiv

%install -a
rm -f %{buildroot}%{_libdir}/*.la

%files
%license LICENCE.md
%doc AUTHORS.md ChangeLog NEWS README
# All runtime libraries are in the main package.
%{_libdir}/libpcre2-8.so.0*
%{_libdir}/libpcre2-16.so.0*
%{_libdir}/libpcre2-32.so.0*
%{_libdir}/libpcre2-posix.so.3*
# All CLI tools are in the main package.
%{_bindir}/pcre2grep
%{_bindir}/pcre2test
# Man pages for the tools.
%{_mandir}/man1/*

%files devel
%doc %{_docdir}/pcre2/
# Header file.
%{_includedir}/*.h
# Development symlinks.
%{_libdir}/*.so
# Static libraries.
%{_libdir}/*.a
# Pkg-config files.
%{_libdir}/pkgconfig/*.pc
# Man page for the pcre2-config script.
%{_mandir}/man1/pcre2-config.1.gz
# API documentation.
%{_mandir}/man3/*
# The pcre2-config script is a development tool.
%{_bindir}/pcre2-config

%changelog
%{?autochangelog}
