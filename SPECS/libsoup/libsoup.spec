# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libsoup
Version:        3.6.5
Release:        %autorelease
Summary:        An HTTP library implementation in C
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/libsoup
VCS:            git:https://gitlab.gnome.org/GNOME/libsoup
#!RemoteAsset
Source:         https://download.gnome.org/sources/libsoup/3.6/libsoup-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf): -Ddocs=enabled
BuildOption(conf): -Dautobahn=disabled
BuildOption(conf): -Dsysprof=disabled
BuildOption(conf): -Dntlm=disabled

BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gi-docgen >= 2021.1
BuildRequires:  krb5-devel
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  glib-networking >= 2.70.0
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libpsl)
BuildRequires:  pkgconfig(sqlite3)

Recommends:     glib-networking >= 2.70.0

%description
Libsoup is an HTTP library implementation in C. It uses the Glib main loop and
is designed to work well with GTK applications.

%package        devel
Summary:        Header files and documentation for the Soup library
Requires:       %{name} = %{version}

%description devel
This package contains the header files, libraries, and developer documentation
needed to develop applications that use the libsoup library.

%install -a
install -m 644 -D tests/libsoup.supp %{buildroot}%{_datadir}/libsoup-3.0/libsoup.supp

# Avoid illegal package names
rm -rf %{buildroot}%{_datadir}/locale/*@*
rm -rf %{buildroot}%{_datadir}/locale/en_GB/LC_MESSAGES
%find_lang libsoup-3.0 --generate-subpackages

%files
%license COPYING
%doc README NEWS AUTHORS
%{_libdir}/libsoup-3.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Soup-3.0.typelib

%files devel
%{_includedir}/libsoup-3.0
%{_libdir}/libsoup-3.0.so
%{_libdir}/pkgconfig/libsoup-3.0.pc
%dir %{_datadir}/libsoup-3.0
%{_datadir}/libsoup-3.0/libsoup.supp
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Soup-3.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libsoup-3.0.deps
%{_datadir}/vala/vapi/libsoup-3.0.vapi
%{_docdir}/libsoup-3.0/

%changelog
%{?autochangelog}
