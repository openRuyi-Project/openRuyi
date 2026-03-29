# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           qtkeychain
Version:        0.15.0
Release:        %autorelease
Summary:        A password store library for Qt6
License:        BSD-3-Clause
URL:            https://github.com/frankosterfeld/qtkeychain
#!RemoteAsset:  sha256:f4254dc8f0933b06d90672d683eab08ef770acd8336e44dfa030ce041dc2ca22
Source0:        https://github.com/frankosterfeld/qtkeychain/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_WITH_QT6:BOOL=ON
BuildOption(conf):  -DECM_MKSPECS_INSTALL_DIR=%{_qt6_archdatadir}/mkspecs/modules

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  qt6-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  qt6-linguist
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)

%description
The qt6keychain library allows you to store passwords easily and securely.
It provides a platform-independent API to access the OS-specific password
stores (Keychain on Mac, Secret Service API/KWallet on Linux, Credential
Manager on Windows).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libsecret-1)
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6DBus)

%description    devel
This package contains development files for qt6keychain.

%install -a
# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages --with-qt

%check
# "Cannot autolaunch D-Bus without X11 $DISPLAY"
# skip tests as the build env no display.

%files -f %{name}.lang
%license COPYING
%{_libdir}/libqt6keychain.so.*
%dir %{_datadir}/qt6keychain
%dir %{_datadir}/qt6keychain/translations

%files devel
%{_includedir}/qt6keychain/
%{_libdir}/cmake/Qt6Keychain/
%{_libdir}/libqt6keychain.so
%{_qt6_archdatadir}/mkspecs/modules/qt_Qt6Keychain.pri

%changelog
%autochangelog
