# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gtkmm3
Version:        3.24.10
Release:        %autorelease
Summary:        C++ interface for the GTK+ library
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gtkmm
#!RemoteAsset:  sha256:7ab7e2266808716e26c39924ace1fb46da86c17ef39d989624c42314b32b5a76
Source0:        https://download.gnome.org/sources/gtkmm/3.24/gtkmm-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dbuild-documentation=false

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(atkmm-1.6) >= 2.24.2
BuildRequires:  pkgconfig(cairomm-1.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.35.5
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.54.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(pangomm-1.4) >= 2.38.2

%description
gtkmm is the official C++ interface for the popular GUI library GTK+.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%check
# skip tests as there is no display.

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libgdkmm-*.so.1*
%{_libdir}/libgtkmm-*.so.1*

%files devel
%{_includedir}/gtkmm-*/
%{_includedir}/gdkmm-*/
%{_libdir}/libgdkmm-*.so
%{_libdir}/libgtkmm-*.so
%{_libdir}/gtkmm-*/
%{_libdir}/gdkmm-*/
%{_libdir}/pkgconfig/gdkmm-3.0.pc
%{_libdir}/pkgconfig/gtkmm-3.0.pc

%changelog
%{?autochangelog}
