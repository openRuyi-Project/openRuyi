# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# first two digits of version
%global release_version 0.21

Name:           libsecret
Version:        %{release_version}.7
Release:        %autorelease
Summary:        Library for storing and retrieving passwords and other secrets
License:        LGPL-2.1-or-later AND Apache-2.0 AND (GPL-2.0-or-later OR TGPPL-1.0) AND LicenseRef-openRuyi-Public-Domain
URL:            https://wiki.gnome.org/Projects/Libsecret
VCS:            git:https://gitlab.gnome.org/GNOME/libsecret
#!RemoteAsset
Source:         https://download.gnome.org/sources/%{name}/%{release_version}/%{name}-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  vala
BuildRequires:  libxslt
BuildRequires:  docbook-xsl
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(gi-docgen)

%description
libsecret is a library for storing and retrieving passwords and other secrets.
It communicates with the "Secret Service" using DBus. gnome-keyring and
KSecretService are both implementations of a Secret Service.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%install -a
%find_lang libsecret

# TODO: Broken check also no distro is checking it - 251
%check

%files -f libsecret.lang
%license COPYING
%doc NEWS README.md
%{_bindir}/secret-tool
%{_libdir}/libsecret-1.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Secret-1.typelib
%{_mandir}/man1/secret-tool.1*
%{_datadir}/bash-completion/completions/secret-tool

%files devel
%license COPYING
%{_includedir}/libsecret-1/
%{_libdir}/libsecret-1.so
%{_libdir}/pkgconfig/libsecret-1.pc
%{_libdir}/pkgconfig/libsecret-unstable.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Secret-1.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libsecret-1.deps
%{_datadir}/vala/vapi/libsecret-1.vapi
%doc %{_docdir}/libsecret-1/

%changelog
%autochangelog
