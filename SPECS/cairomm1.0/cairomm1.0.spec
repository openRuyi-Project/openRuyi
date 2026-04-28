# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cairomm1.0
Version:        1.14.5
Release:        %autorelease
Summary:        C++ API for the cairo graphics library
License:        LGPL-2.0-or-later
URL:            https://gitlab.freedesktop.org/cairo/cairomm
#!RemoteAsset:  sha256:70136203540c884e89ce1c9edfb6369b9953937f6cd596d97c78c9758a5d48db
Source0:        https://www.cairographics.org/releases/cairomm-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(fontconfig)

%description
This library provides a C++ interface to cairo.
The API/ABI version series is %{apiver}.

%package        devel
Summary:        Development files for cairomm
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The cairomm-devel package contains libraries and header files for developing
applications that use cairomm.

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libcairomm-*.so.*

%files devel
%{_includedir}/cairomm-*/
%{_libdir}/libcairomm-*.so
%{_libdir}/pkgconfig/cairomm-1.0.pc
%{_libdir}/pkgconfig/cairomm-ft-1.0.pc
%{_libdir}/pkgconfig/cairomm-pdf-1.0.pc
%{_libdir}/pkgconfig/cairomm-png-1.0.pc
%{_libdir}/pkgconfig/cairomm-ps-1.0.pc
%{_libdir}/pkgconfig/cairomm-svg-1.0.pc
%{_libdir}/pkgconfig/cairomm-xlib-1.0.pc
%{_libdir}/pkgconfig/cairomm-xlib-xrender-1.0.pc
%{_libdir}/cairomm-*/

%changelog
%{?autochangelog}
