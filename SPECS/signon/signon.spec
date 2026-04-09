# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           signon
Version:        8.61
Release:        %autorelease
Summary:        Accounts framework for Linux and POSIX based platforms
License:        LGPL-2.1-only
URL:            https://gitlab.com/accounts-sso/signond
#!RemoteAsset:  sha256:3dd57c25e1bf1583b2cb857f96831e38e73d40264ff66ca43e63bb7233f76828
Source0:        https://gitlab.com/accounts-sso/signond/-/archive/VERSION_%{version}/signond-VERSION_%{version}.tar.gz
BuildSystem:    autotools

# enable Qt6 from upstream.
Patch0:         0001-Add-Qt6-support.patch
# disable build of static library
Patch1:         0002-disbale-static-build.patch

BuildOption(install):  INSTALL_ROOT=%{buildroot}

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  qt6-macros
BuildRequires:  doxygen
BuildRequires:  graphviz

Requires:       dbus

%description
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%conf
# No configure.

%build
%{qmake6} PREFIX=%{_prefix} LIBDIR=%{_libdir}

%check
# skip tests in the build env as it needs dbus.

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/signond.conf
%{_bindir}/signond
%{_bindir}/signonpluginprocess
%{_libdir}/libsignon-extension.so.1*
%{_libdir}/libsignon-plugins-common.so.1*
%{_libdir}/libsignon-plugins.so.1*
%{_libdir}/signon/
%{_datadir}/dbus-1/services/*.service
%{_libdir}/libsignon-qt6.so.1*

%files devel
%{_includedir}/signon-extension/
%{_includedir}/signon-plugins/
%{_includedir}/signond/
%{_includedir}/signon-qt6/
%{_libdir}/libsignon-extension.so
%{_libdir}/libsignon-plugins-common.so
%{_libdir}/libsignon-plugins.so
%{_libdir}/libsignon-qt6.so
%{_libdir}/pkgconfig/SignOnExtension.pc
%{_libdir}/pkgconfig/signon-plugins-common.pc
%{_libdir}/pkgconfig/signon-plugins.pc
%{_libdir}/pkgconfig/signond.pc
%{_libdir}/pkgconfig/libsignon-qt6.pc
%{_libdir}/cmake/SignOnQt6/
%{_docdir}/signon/
%{_docdir}/libsignon-qt/
%{_docdir}/signon-plugins/
%{_docdir}/signon-plugins-dev/

%changelog
%autochangelog
