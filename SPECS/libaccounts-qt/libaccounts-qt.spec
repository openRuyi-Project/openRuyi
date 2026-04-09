# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libaccounts-qt
Version:        1.17
Release:        %autorelease
Summary:        Accounts framework Qt6 bindings
License:        LGPL-2.1-only
URL:            https://gitlab.com/accounts-sso/libaccounts-qt
#!RemoteAsset:  sha256:6ed3e976133962c1c88f6c66928ba0d0a17a570843577d31e783dc891659e5d8
Source0:        https://gitlab.com/accounts-sso/libaccounts-qt/-/archive/VERSION_%{version}/libaccounts-qt-VERSION_%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install):  INSTALL_ROOT=%{buildroot}

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  doxygen
BuildRequires:  cmake(Qt6Test)
BuildRequires:  qt6-macros

%description
Accounts framework Qt6 bindings.

%package        devel
Summary:        Development files for libaccounts-qt6
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel

%description    devel
Development files for libaccounts-qt6.

%conf
# No configure.

%build
%{qmake6} \
    QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release \
    LIBDIR=%{_libdir} \
    accounts-qt.pro

%install -a
mkdir -p %{buildroot}%{_datadir}/accounts/{providers,services}
rm -rfv %{buildroot}%{_datadir}/libaccounts-qt-tests
rm -fv %{buildroot}%{_bindir}/accountstest

%check
# skip tests in the build env,as no dbus in it.

%files
%license COPYING
%{_libdir}/libaccounts-qt6.so.1*
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/

%files devel
%{_libdir}/libaccounts-qt6.so
%{_includedir}/accounts-qt6/
%{_libdir}/pkgconfig/accounts-qt6.pc
%{_libdir}/cmake/AccountsQt6/
%{_docdir}/accounts-qt

%changelog
%autochangelog
