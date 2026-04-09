# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libdisplay-info
Version:        0.2.0
Release:        %autorelease
Summary:        EDID and DisplayID library
License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/libdisplay-info
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/emersion/libdisplay-info/-/archive/%{version}/libdisplay-info-%{version}.tar.bz2
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(hwdata)

%description
libdisplay-info is an EDID and DisplayID library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license LICENSE
%doc README.md
%{_libdir}/libdisplay-info.so.*
%{_bindir}/di-edid-decode

%files devel
%{_includedir}/libdisplay-info/
%{_libdir}/libdisplay-info.so
%{_libdir}/pkgconfig/libdisplay-info.pc

%changelog
%autochangelog
