# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global gitdate 20231216
%global commit0 05e79ebbbf3784a87f72b7be571070125c10dfe3
%global shortcommit %(c=%{commit0}; echo ${c:0:7})

Name:           accounts-qml-module
Version:        0.7+git%{gitdate}.%{shortcommit}
Release:        %autorelease
Summary:        QML bindings for libaccounts-qt + libsignon-qt (Qt6)
License:        LGPL-2.1-only
URL:            https://gitlab.com/accounts-sso/accounts-qml-module
#!RemoteAsset:  sha256:1a53a6d8a3a56694244bc24bdab844d91420483744822d08ae8517ff7df84763
Source:         https://gitlab.com/accounts-sso/accounts-qml-module/-/archive/%{commit0}/%{name}-%{commit0}.tar.gz
BuildSystem:    autotools

BuildOption(install):  INSTALL_ROOT=%{buildroot}

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  cmake(AccountsQt6)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(SignOnQt6)
BuildRequires:  qt6-doctools

%description
This QML module provides an API to manage the user's online accounts and get
their authentication data. It's a tiny wrapper around the Qt-based APIs of
libaccounts-qt and libsignon-qt.

%conf
# No configure.

%build
%{qmake6} \
  CONFIG+=release \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir}

%install -a
# Delete test executable
rm %{buildroot}%{_bindir}/tst_plugin

%check
# LD_LIBRARY_PATH=mock: xvfb-run -a dbus-test-runner -m 120 -t ./tst_plugin
# some deps we don't have yet.

%files
%license COPYING
%doc README.md
%{_qt6_qmldir}/SSO/
%doc %{_datadir}/accounts-qml-module/

%changelog
%autochangelog
