# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0
%bcond tests 0

Name:           tinysparql
Version:        3.10.1
Release:        %autorelease
Summary:        Desktop-neutral metadata database and search tool
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/tinysparql/
#!RemoteAsset
Source0:        https://download.gnome.org/sources/tinysparql/3.10/tinysparql-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dunicode_support=icu
BuildOption(conf):  -Dsystemd_user_services_dir=%{_userunitdir}
BuildOption(conf):  -Davahi=disabled
%if %{without libstemmer}
BuildOption(conf):  -Dstemmer=disabled
%endif

%if %{with doc}
BuildOption(conf):  -Ddocs=true
BuildOption(conf):  -Dman=true
%else
BuildOption(conf):  -Ddocs=false
BuildOption(conf):  -Dman=false
%endif

%if %{with tests}
BuildOption(conf):  -Dtests=true
%else
BuildOption(conf):  -Dtests=false
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)

%if %{with libstemmer}
BuildRequires:  libstemmer-devel
%endif

%if %{with doc}
BuildRequires:  asciidoc
BuildRequires:  gi-docgen
%endif

Provides:       tracker = %{version}-%{release}

%description
Tinysparql is a powerful desktop-neutral first class object database,
tag/metadata database and search tool.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with doc}
%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains the documentation for %{name}.
%endif

%install -a
# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/en_GB/
%find_lang tinysparql3 --generate-subpackages

%check
# just skip the tests,as the env is not ready.

%post
%systemd_user_post tinysparql-xdg-portal-3.service

%preun
%systemd_user_preun tinysparql-xdg-portal-3.service

%postun
%systemd_user_postun_with_restart tinysparql-xdg-portal-3.service

%files
%license COPYING COPYING.GPL
%doc AUTHORS NEWS README.md
%{_bindir}/tinysparql
%{_libexecdir}/tinysparql-sql
%{_libexecdir}/tinysparql-xdg-portal-3
%{_datadir}/dbus-1/services/org.freedesktop.portal.Tracker.service
%{_userunitdir}/tinysparql-xdg-portal-3.service
%{_datadir}/bash-completion/completions/tinysparql
%{_libdir}/girepository-1.0/Tracker-3.0.typelib
%{_libdir}/girepository-1.0/Tsparql-3.0.typelib
%{_libdir}/libtinysparql-3.0.so.0*
%{_libdir}/libtracker-sparql-3.0.so.0*
%{_libdir}/tinysparql-3.0/
%if %{with doc}
%{_mandir}/man1/tinysparql*.1*
%endif

%files devel
%license COPYING COPYING.LGPL
%{_includedir}/tinysparql-3.0/
%{_libdir}/libtinysparql-3.0.so
%{_libdir}/libtracker-sparql-3.0.so
%{_libdir}/pkgconfig/tinysparql-3.0.pc
%{_libdir}/pkgconfig/tracker-sparql-3.0.pc
%{_datadir}/gir-1.0/Tracker-3.0.gir
%{_datadir}/gir-1.0/Tsparql-3.0.gir
%{_datadir}/vala/vapi/tinysparql-3.0.deps
%{_datadir}/vala/vapi/tinysparql-3.0.vapi
%{_datadir}/vala/vapi/tracker-sparql-3.0.deps
%{_datadir}/vala/vapi/tracker-sparql-3.0.vapi

%if %{with doc}
%files doc
%license docs/reference/COPYING
%{_docdir}/Tsparql-3.0/
%endif

%changelog
%{?autochangelog}
