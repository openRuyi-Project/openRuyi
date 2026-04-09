# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libdvdnav
Version:        7.0.0
Release:        %autorelease
Summary:        DVD Navigation Library
License:        GPL-2.0-or-later
URL:            https://code.videolan.org/videolan/libdvdnav
#!RemoteAsset
Source:         https://download.videolan.org/pub/videolan/libdvdnav/7.0.0/libdvdnav-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Ddefault_library=shared

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dvdread)

%description
This library contains functions to display DVD video menus.
This is a metapackage that requires the runtime library.

%package        devel
Summary:        Development files for libdvdnav
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and libraries needed to develop
applications that use the libdvdnav library.

%install -a
rm -r %{buildroot}%{_datadir}/doc/libdvdnav/

%files
%license COPYING
%doc AUTHORS ChangeLog TODO
%{_libdir}/libdvdnav.so.4*

%files devel
%{_includedir}/dvdnav
%{_libdir}/libdvdnav.so
%{_libdir}/pkgconfig/dvdnav.pc

%changelog
%autochangelog
