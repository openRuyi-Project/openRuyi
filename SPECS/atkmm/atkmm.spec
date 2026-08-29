# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           atkmm
Version:        2.28.4
Release:        %autorelease
Summary:        C++ interface for the ATK library
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/atkmm
#!RemoteAsset:  sha256:0a142a8128f83c001efb8014ee463e9a766054ef84686af953135e04d28fdab3
Source0:        https://download.gnome.org/sources/atkmm/2.28/atkmm-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dbuild-documentation=false

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.46.2

%description
atkmm provides a C++ interface for the ATK library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libatkmm-*.so.*

%files devel
%{_includedir}/atkmm-*/
%{_libdir}/libatkmm-*.so
%{_libdir}/pkgconfig/atkmm-1.6.pc
%{_libdir}/atkmm-*/

%changelog
%{?autochangelog}
