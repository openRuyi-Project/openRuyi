# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libcerror
Version:        20240413
Release:        %autorelease
Summary:        Library for cross-platform C error functions
License:        LGPL-3.0-or-later
URL:            https://github.com/libyal/libcerror
#!RemoteAsset
Source0:        %{url}/releases/download/%{version}/%{name}-beta-%{version}.tar.gz
#!RemoteAsset
Source1:        %{url}/releases/download/%{version}/%{name}-beta-%{version}.tar.gz.asc
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc
BuildRequires:  doxygen

%description
libcerror is a library for cross-platform C error functions.

This package is part of the libyal library collection and is used by
other libraries in the collection.

%package        devel
Summary:        Development files for libcerror, a C error library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libcerror is a library for cross-platform C error functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcerror.

%files
%license COPYING.LESSER
%{_libdir}/libcerror.so.1*

%files devel
%{_includedir}/libcerror*
%{_libdir}/libcerror.so
%{_libdir}/pkgconfig/libcerror.pc
%{_mandir}/man3/libcerror.3*

%changelog
%autochangelog
