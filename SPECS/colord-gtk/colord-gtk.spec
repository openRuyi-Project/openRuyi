# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond gtk4 0
%bcond doc 0
# the tests need dispaly.
%bcond tests 0

Name:           colord-gtk
Version:        0.3.1
Release:        %autorelease
Summary:        GTK+ 3 support library for colord
License:        LGPL-2.1-or-later
URL:            https://gitlab.freedesktop.org/colord/colord-gtk
#!RemoteAsset
Source0:        http://www.freedesktop.org/software/colord/releases/colord-gtk-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dgtk2=false
BuildOption(conf):  -Dman=false
%if %{with doc}
BuildOption(conf):  -Ddocs=true
%else
BuildOption(conf):  -Ddocs=false
%endif
%if %{with tests}
BuildOption(conf):  -Dtests=true
%else
BuildOption(conf):  -Dtests=false
%endif
BuildOption(conf):  -Dvapi=true
%if %{with gtk4}
BuildOption(conf):  -Dgtk4=true
%else
BuildOption(conf):  -Dgtk4=false
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext >= 0.19.8
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(lcms2) >= 2.2
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  vala
%if %{with gtk4}
BuildRequires:  gtk4-devel
%endif
%if %{with doc}
BuildRequires:  gtk-doc
BuildRequires:  docbook-xsl
%endif

%description
colord-gtk is a support library for colord and provides additional
functionality that requires GTK+.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Files for development with %{name}.

%install -a
# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%license COPYING
%doc README AUTHORS NEWS
%{_bindir}/cd-convert
%{_libdir}/libcolord-gtk.so.*
%{_libdir}/girepository-1.0/ColordGtk-1.0.typelib
%if %{with gtk4}
%{_libdir}/libcolord-gtk4.so.*
%endif

%files devel
%{_libdir}/libcolord-gtk.so
%{_libdir}/pkgconfig/colord-gtk.pc
%{_includedir}/colord-1/colord-gtk.h
%dir %{_includedir}/colord-1/colord-gtk
%{_includedir}/colord-1/colord-gtk/*.h
%{_datadir}/gir-1.0/ColordGtk-1.0.gir
%{_datadir}/vala/vapi/colord-gtk.vapi
%{_datadir}/vala/vapi/colord-gtk.deps
%if %{with doc}
%{_datadir}/gtk-doc/html/colord-gtk
%endif
%if %{with gtk4}
%{_libdir}/libcolord-gtk4.so
%{_libdir}/pkgconfig/colord-gtk4.pc
%endif

%changelog
%autochangelog
