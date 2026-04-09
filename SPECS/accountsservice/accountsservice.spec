# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0

Name:           accountsservice
Version:        23.13.9
Release:        %autorelease
Summary:        D-Bus interfaces for querying and manipulating user account information
License:        GPL-3.0-or-later
URL:            https://www.freedesktop.org/wiki/Software/AccountsService/
VCS:            git:https://gitlab.freedesktop.org/accountsservice/accountsservice.git
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/accountsservice/accountsservice/-/archive/%{version}/accountsservice-%{version}.tar.gz
BuildSystem:    meson

# add forward declaration to fix compiler error.
Patch0:         0001-mocklibc-Fix-compiler-warning.patch
# Fixes compiler warning by adding ACT_USER_MANAGER_NEW_SESSION_STATE_UNLOADED
# to the switch default case.
Patch1:         0002-user-manager-Fix-another-compiler-warning.patch
# Replaces crypt() with crypt_rn() for thread safety and zeroizes memory buffers.
Patch2:         0003-act-user-Use-the-reentrant-interfaces-of-crypt-gens.patch

BuildOption(conf):  -Dadmin_group=wheel
%if %{with doc}
BuildOption(conf):  -Dgtk_doc=true
%else
BuildOption(conf):  -Dgtk_doc=false
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  vala
BuildRequires:  pkgconfig(libxcrypt)
BuildRequires:  systemd-rpm-macros

%if %{with doc}
BuildRequires:  gtk-doc
%endif

Requires:       polkit
Requires:       shadow
%{?systemd_requires}

%description
The accountsservice project provides a set of D-Bus interfaces for
querying and manipulating user account information.

%package        devel
Summary:        Development files for accountsservice-libs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The accountsservice-devel package contains headers and other
files needed to build applications that use accountsservice-libs.

%install -a
mkdir -p %{buildroot}%{_datadir}/accountsservice/interfaces/

# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang accounts-service --generate-subpackages

%post
%systemd_post accounts-daemon.service

%preun
%systemd_preun accounts-daemon.service

%postun
%systemd_postun accounts-daemon.service

%files -f accounts-service.lang
%license COPYING
%doc README.md AUTHORS
%{_libexecdir}/accounts-daemon
%dir %{_datadir}/accountsservice/
%dir %{_datadir}/accountsservice/interfaces/
%{_datadir}/accountsservice/user-templates/
%{_datadir}/dbus-1/interfaces/org.freedesktop.Accounts.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Accounts.User.xml
%{_datadir}/dbus-1/system.d/org.freedesktop.Accounts.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.Accounts.service
%{_datadir}/polkit-1/actions/org.freedesktop.accounts.policy
%dir %{_localstatedir}/lib/AccountsService/
%dir %{_localstatedir}/lib/AccountsService/users/
%dir %{_localstatedir}/lib/AccountsService/icons/
%{_unitdir}/accounts-daemon.service
%{_libdir}/libaccountsservice.so.*
%{_libdir}/girepository-1.0/AccountsService-1.0.typelib

%files devel
%{_includedir}/accountsservice-1.0
%{_libdir}/libaccountsservice.so
%{_libdir}/pkgconfig/accountsservice.pc
%{_datadir}/gir-1.0/AccountsService-1.0.gir
%{_datadir}/vala/vapi/accountsservice.*
%if %{with doc}
%{_datadir}/gtk-doc/html/libaccountsservice
%endif

%changelog
%autochangelog
