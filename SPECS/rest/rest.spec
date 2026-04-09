# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0
%bcond tests 0

Name:           rest
Version:        0.10.2
Release:        %autorelease
Summary:        A library for access to RESTful web services
License:        LGPL-2.1-only
URL:            https://gitlab.gnome.org/GNOME/librest
#!RemoteAsset
Source0:        https://download.gnome.org/sources/librest/0.10/librest-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dsoup2=false
BuildOption(conf):  -Dexamples=false

%if %{with doc}
BuildOption(conf):  -Dgtk_doc=true
%else
BuildOption(conf):  -Dgtk_doc=false
%endif

%if %{with tests}
BuildOption(conf):  -Dtests=true
%else
BuildOption(conf):  -Dtests=false
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
%if %{with doc}
BuildRequires:  pkgconfig(gi-docgen)
%endif

%description
This library was designed to make it easier to access web services that
claim to be "RESTful".

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Files for development with %{name}.

%files
%license COPYING
%doc AUTHORS README.md
%{_libdir}/librest-1.0.so.0*
%{_libdir}/librest-extras-1.0.so.0*
%{_libdir}/girepository-1.0/Rest-1.0.typelib
%{_libdir}/girepository-1.0/RestExtras-1.0.typelib

%files devel
%{_includedir}/rest-1.0/
%{_libdir}/pkgconfig/rest-1.0.pc
%{_libdir}/pkgconfig/rest-extras-1.0.pc
%{_libdir}/librest-1.0.so
%{_libdir}/librest-extras-1.0.so
%{_datadir}/gir-1.0/Rest-1.0.gir
%{_datadir}/gir-1.0/RestExtras-1.0.gir
%if %{with doc}
%{_datadir}/doc/librest-1.0/
%endif

%changelog
%autochangelog
