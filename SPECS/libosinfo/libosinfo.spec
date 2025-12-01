# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libosinfo
Version:        1.12.0
Release:        %autorelease
Summary:        A library for managing OS information for virtualization
License:        LGPL-2.1-or-later
URL:            https://libosinfo.org/
VCS:            git:https://gitlab.com/libosinfo/libosinfo
#!RemoteAsset
Source:         https://releases.pagure.org/libosinfo/libosinfo-%{version}.tar.xz
Patch:          0001-libosinfo-libxml2-2.14.patch
BuildSystem:    meson

BuildOption(conf): -Denable-gtk-doc=false
BuildOption(conf): -Denable-tests=true
BuildOption(conf): -Denable-introspection=enabled
BuildOption(conf): -Denable-vala=enabled

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glib-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  hwdata
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  osinfo-db
BuildRequires:  vala
Requires:       hwdata osinfo-db osinfo-db-tools

%description
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

%package        devel
Summary:        Development files for the libosinfo library
Requires:       %{name}%{?_isa} = %{version}
Requires:       pkgconfig
Requires:       glib-devel

%description devel
This package contains the libraries, header files, and documentation needed to
develop applications that use the libosinfo library.

%install -a
# Avoid illegal package names
rm -rf %{buildroot}%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files
%license COPYING.LIB
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/osinfo-detect
%{_bindir}/osinfo-query
%{_bindir}/osinfo-install-script
%{_mandir}/man1/osinfo-detect.1*
%{_mandir}/man1/osinfo-query.1*
%{_mandir}/man1/osinfo-install-script.1*
%{_libdir}/libosinfo-1.0.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Libosinfo-1.0.typelib

%files devel
%{_libdir}/libosinfo-1.0.so
%dir %{_includedir}/libosinfo-1.0/
%dir %{_includedir}/libosinfo-1.0/osinfo/
%{_includedir}/libosinfo-1.0/osinfo/*.h
%{_libdir}/pkgconfig/libosinfo-1.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Libosinfo-1.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libosinfo-1.0.deps
%{_datadir}/vala/vapi/libosinfo-1.0.vapi

%changelog
%{?autochangelog}
