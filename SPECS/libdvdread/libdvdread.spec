# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libdvdread
Version:        7.0.1
Release:        %autorelease
Summary:        Library for Reading DVD Video Images
License:        GPL-2.0-or-later
URL:            https://code.videolan.org/videolan/libdvdread
#!RemoteAsset
Source:         https://download.videolan.org/videolan/libdvdread/%{version}/libdvdread-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Ddefault_library=shared

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libdvdcss)

%description
This package contains shared libraries for accessing DVD images.
This is a metapackage that requires the runtime library.

%package        devel
Summary:        Development files for libdvdread
Requires:       glibc-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and libraries for developing
applications that use the libdvdread library.

%files
%license COPYING
%doc AUTHORS NEWS README.md COPYING TODO
%{_libdir}/libdvdread.so.8*

%files devel
%{_includedir}/dvdread
%{_libdir}/libdvdread.so
%{_libdir}/pkgconfig/dvdread.pc

%changelog
%autochangelog
