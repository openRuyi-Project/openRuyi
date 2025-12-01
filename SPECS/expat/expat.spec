# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global unversion 2_7_1

Name:           expat
Version:        2.7.1
Release:        %autorelease
Summary:        XML Parser Toolkit
License:        MIT
URL:            https://libexpat.github.io
#!RemoteAsset
Source0:        https://github.com/libexpat/libexpat/releases/download/R_%{unversion}/expat-%{version}.tar.xz
#!RemoteAsset
Source1:        https://github.com/libexpat/libexpat/releases/download/R_%{unversion}/expat-%{version}.tar.xz.asc
# https://www.gentoo.org/inside-gentoo/developers/index.html#sping
# https://github.com/libexpat/libexpat/issues/537#issuecomment-1003796884
#!RemoteAsset
Source4:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3176ef7db2367f1fca4f306b1f9b0e909af37285#/expat.keyring
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
Requires:       expat%{?_isa} = %{version}-%{release}

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
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h
%{_libdir}/cmake/expat-%{version}
%exclude %{_libdir}/libexpat.la

%changelog
%{?autochangelog}
