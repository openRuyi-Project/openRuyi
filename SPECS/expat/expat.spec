# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global unversion 2_8_1

Name:           expat
Version:        2.8.1
Release:        %autorelease
Summary:        XML Parser Toolkit
License:        MIT
URL:            https://libexpat.github.io
VCS:            git:https://github.com/libexpat/libexpat
#!RemoteAsset:  sha256:10b195ee78160a908388180a8fe3603d4e9a12f4755fbf5f3816b23a9d750da0
Source0:        https://github.com/libexpat/libexpat/releases/download/R_%{unversion}/expat-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --without-docbook
BuildOption(conf):  --disable-static

BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig

%description
Expat is an XML parser library written in C. It is a stream-oriented
parser in which an application registers handlers for things the
parser might find in the XML document (like start tags).

%package        devel
Summary:        Development files for expat, an XML parser toolkit
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Expat is an XML parser library written in C. It is a stream-oriented
parser in which an application registers handlers for things the
parser might find in the XML document (like start tags).

This package contains the development headers for the library found
in libexpat.

%files
%license COPYING
%{_bindir}/*
%{_libdir}/libexpat.so.1
%{_libdir}/libexpat.so.1.*
%{_mandir}/*/*
%{_datadir}/doc/*

%files devel
%doc doc/reference.html doc/*.css examples/*.c
%{_libdir}/libexpat.so
%{_libdir}/pkgconfig/expat.pc
%{_includedir}/*.h
%{_libdir}/cmake/expat-%{version}
%exclude %{_libdir}/libexpat.la

%changelog
%autochangelog
