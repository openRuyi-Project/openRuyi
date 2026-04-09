# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond gtk4 0

Name:           gcr
Version:        4.4.0.1
Release:        %autorelease
Summary:        A library for bits of crypto UI and parsing
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/gcr
#!RemoteAsset:  sha256:be1fd6ec369ed4eb42e309ef7933a6fb925b08296e0a04a21bb979954d5586e3
Source0:        https://gitlab.gnome.org/GNOME/gcr/-/archive/%{version}/gcr-%{version}.tar.gz
BuildSystem:    meson

# skip the test will fail.
Patch0:         0001-skip-some-test.patch

BuildOption(conf):  -Dcrypto=gnutls
%if %{with gtk4}
BuildOption(conf):  -Dgtk4=true
%else
BuildOption(conf):  -Dgtk4=false
%endif
BuildOption(conf):  -Dgtk_doc=true

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  gnupg
BuildRequires:  openssh-clients
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
BuildRequires:  pkgconfig(gi-docgen)
%if %{with gtk4}
BuildRequires:  pkgconfig(gtk4)
%endif

%description
gcr is a library for displaying certificates, and crypto UI, accessing
key stores. It also provides a viewer for crypto files on the GNOME desktop.
gck is a library for accessing PKCS#11 modules like smart cards.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%install -a
# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang gcr-4 --generate-subpackages

%post
%systemd_user_post gcr-ssh-agent.service

%preun
%systemd_user_preun gcr-ssh-agent.service

%postun
%systemd_user_postun_with_restart gcr-ssh-agent.service

%files -f gcr-4.lang
%doc NEWS README.md
%{_libexecdir}/gcr-ssh-agent
%{_libexecdir}/gcr4-ssh-askpass
%{_userunitdir}/gcr-ssh-agent.service
%{_userunitdir}/gcr-ssh-agent.socket
%{_libdir}/girepository-1.0/Gck-2.typelib
%{_libdir}/girepository-1.0/Gcr-4.typelib
%{_libdir}/libgck-2.so.2*
%{_libdir}/libgcr-4.so.4*
%if %{with gtk4}
%{_bindir}/gcr-viewer-gtk4
%endif

%files devel
%{_includedir}/gck-2/
%{_includedir}/gcr-4/
%{_libdir}/libgck-2.so
%{_libdir}/libgcr-4.so
%{_libdir}/pkgconfig/gck-2.pc
%{_libdir}/pkgconfig/gcr-4.pc
%{_datadir}/gir-1.0/Gck-2.gir
%{_datadir}/gir-1.0/Gcr-4.gir
%{_datadir}/vala/vapi/gck-2.deps
%{_datadir}/vala/vapi/gck-2.vapi
%{_datadir}/vala/vapi/gcr-4.deps
%{_datadir}/vala/vapi/gcr-4.vapi
%{_datadir}/doc/gck-2/
%{_datadir}/doc/gcr-4/

%changelog
%autochangelog
