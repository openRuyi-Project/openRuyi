# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libdvdcss
Version:        1.5.0
Release:        %autorelease
Summary:        Library for Reading DVD Video Images
License:        GPL-2.0-or-later
URL:            https://code.videolan.org/videolan/libdvdcss
#!RemoteAsset
Source:         http://download.videolan.org/videolan/libdvdcss/%{version}/libdvdcss-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Ddefault_library=shared

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)

%description
This package contains shared libraries for accessing DVD images.
This is a metapackage that requires the runtime library.

%package        devel
Summary:        Development files for libdvdcss
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and libraries for developing
applications that use the libdvdcss library.

%files
%license COPYING
%doc %{_docdir}/libdvdcss
%{_libdir}/libdvdcss.so.*

%files devel
%{_includedir}/dvdcss
%{_libdir}/libdvdcss.so
%{_libdir}/pkgconfig/libdvdcss.pc

%changelog
%autochangelog
