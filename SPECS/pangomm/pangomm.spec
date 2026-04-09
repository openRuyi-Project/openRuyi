# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pangomm
Version:        2.46.4
Release:        %autorelease
Summary:        C++ interface for Pango
License:        LGPL-2.1-or-later AND GPL-2.0-only
URL:            https://gitlab.gnome.org/GNOME/pangomm
#!RemoteAsset:  sha256:b92016661526424de4b9377f1512f59781f41fb16c9c0267d6133ba1cd68db22
Source0:        https://download.gnome.org/sources/pangomm/2.46/pangomm-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dbuild-documentation=false

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(cairomm-1.0) >= 1.2.2
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.48.0
BuildRequires:  pkgconfig(pangocairo) >= 1.45.1

%description
pangomm provides a C++ interface to the Pango library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libpangomm-*.so.*

%files devel
%{_includedir}/pangomm-*/
%{_libdir}/libpangomm-*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/pangomm-*/

%changelog
%autochangelog
