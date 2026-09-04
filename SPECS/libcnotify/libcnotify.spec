# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libcnotify
Version:        20260703
Release:        %autorelease
Summary:        Library for cross-platform C notification functions
License:        LGPL-3.0-or-later
URL:            https://github.com/libyal/libcnotify
#!RemoteAsset:  sha256:9cbc0301ab2c7ea393b40f6a793339d08b18907acda247dded4146f10b5b1077
Source0:        %{url}/releases/download/%{version}/libcnotify-beta-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20240413

%description
libcnotify is a library for cross-platform C notification functions.

This package is  part of the libyal library collection.

%package        devel
Summary:        Development files for libcnotify, a C notify library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libcnotify is a library for cross-platform C notification functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcnotify.

%files
%license COPYING.LESSER
%{_libdir}/libcnotify.so.1*

%files devel
%{_includedir}/libcnotify*
%{_libdir}/libcnotify.so
%{_libdir}/pkgconfig/libcnotify.pc
%{_mandir}/man3/libcnotify.3*

%changelog
%autochangelog
