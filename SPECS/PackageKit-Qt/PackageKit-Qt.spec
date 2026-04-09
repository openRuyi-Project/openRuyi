# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           PackageKit-Qt
Version:        1.1.4
Release:        %autorelease
Summary:        Qt 6 bindings for PackageKit
License:        LGPL-2.1-or-later
URL:            https://github.com/PackageKit/PackageKit-Qt
#!RemoteAsset:  sha256:bbb8398d0f98c46e2ed7fd3ce526d4f7fc8476f5a449e89269f01b1bc751c4ad
Source0:        https://github.com/PackageKit/PackageKit-Qt/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_WITH_QT6:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(packagekit-glib2)
BuildRequires:  qt6-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  pkgconfig

%description
PackageKit is a system designed to make installing and updating software
on your computer easier. This package provides Qt 6 bindings.

%package        devel
Summary:        Development files for PackageKit-Qt6
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for PackageKit-Qt6.

%files
%license COPYING
%doc NEWS AUTHORS README.md
%{_libdir}/libpackagekitqt6.so.*

%files devel
%doc TODO MAINTAINERS
%{_includedir}/PackageKitQt/PackageKit/
%{_libdir}/libpackagekitqt6.so
%{_libdir}/cmake/packagekitqt6/
%{_libdir}/pkgconfig/packagekitqt6.pc

%changelog
%autochangelog
