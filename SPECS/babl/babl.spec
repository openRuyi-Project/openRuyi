# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           babl
Version:        0.1.124
Release:        %autorelease
Summary:        A dynamic, any to any, pixel format conversion library
License:        LGPL-3.0-or-later AND GPL-3.0-or-later
URL:            https://www.gimp.org
VCS:            git:https://gitlab.gnome.org/GNOME/babl.git
#!RemoteAsset:  sha256:1b0d544ab6f409f2b1b5f677226272d1e8c6d373f2f453ee870bfc7e5dd4f1b1
Source0:        https://download.gimp.org/babl/0.1/babl-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gi-docgen
BuildRequires:  vala
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(lcms2) >= 2.8

%description
Babl is a dynamic, any to any, pixel format conversion library. It
provides conversions between the myriad of buffer types images can be
stored in. Babl doesn't only help with existing pixel formats, but also
facilitates creation of new and uncommon ones.

%package        devel
Summary:        Headers for developing programs that will use babl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the libraries and header files needed for
developing with babl.

%package        doc
Summary:        Documentation for babl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    doc
This package contains the documentation for babl.

%files
%doc AUTHORS NEWS
%license docs/COPYING*
%{_bindir}/babl
%{_libdir}/libbabl-0.1.so.0*
%{_libdir}/babl-0.1/
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Babl-0.1.typelib

%files devel
%{_includedir}/babl-0.1/
%{_libdir}/libbabl-0.1.so
%{_libdir}/pkgconfig/babl-0.1.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Babl-0.1.gir
%{_datadir}/vala/

%files doc
%{_docdir}/babl-0.1/*

%changelog
%autochangelog
