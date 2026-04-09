# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libaccounts-glib
Version:        1.27
Release:        %autorelease
Summary:        Accounts framework for Linux and POSIX based platforms
License:        LGPL-2.0-or-later
URL:            https://gitlab.com/accounts-sso/libaccounts-glib
#!RemoteAsset:  sha256:a8407a5897a2e425ea1aa955ecf88485dd2fd417919de275b27c781a5d0637a5
Source0:        https://gitlab.com/accounts-sso/libaccounts-glib/-/archive/VERSION_%{version}/libaccounts-glib-VERSION_%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(python3)
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(check)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%install -a
# create data directories
mkdir -p %{buildroot}%{_datadir}/accounts/{applications,providers,services,service_types}

%check
# skip tests in the build env.

%files
%license COPYING
%doc README.md NEWS
%{_bindir}/ag-backup
%{_bindir}/ag-tool
%{_libdir}/libaccounts-glib.so.0
%{_libdir}/libaccounts-glib.so.%{version}
%{_libdir}/girepository-1.0/Accounts-1.0.typelib
%dir %{_datadir}/xml/accounts/schema/dtd
%{_datadir}/xml/accounts/schema/dtd/accounts-*.dtd
%dir %{_datadir}/xml/
%dir %{_datadir}/xml/accounts/
%dir %{_datadir}/xml/accounts/schema/
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/applications/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%dir %{_datadir}/accounts/service_types/

%files devel
%{_includedir}/libaccounts-glib/
%{_libdir}/libaccounts-glib.so
%{_libdir}/pkgconfig/libaccounts-glib.pc
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/gettext/its/accounts-*.{its,loc}
%{_datadir}/gir-1.0/Accounts-1.0.gir
%{_datadir}/vala/vapi/libaccounts-glib.deps
%{_datadir}/vala/vapi/libaccounts-glib.vapi
%doc %{_datadir}/gtk-doc/html/libaccounts-glib/

%changelog
%autochangelog
