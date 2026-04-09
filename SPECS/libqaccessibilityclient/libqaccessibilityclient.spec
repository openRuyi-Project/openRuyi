# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libqaccessibilityclient
Version:        0.6.0
Release:        %autorelease
Summary:        Accessibilty tools helper library, used e.g. by screen readers
License:        LGPL-2.1-or-later
URL:            https://invent.kde.org/libraries/libqaccessibilityclient
#!RemoteAsset:  sha256:4c50c448622dc9c5041ed10da7d87b3e4e71ccb49d4831a849211d423c5f5d33
Source0:        https://download.kde.org/Attic/libqaccessibilityclient/libqaccessibilityclient-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_WITH_QT6:BOOL=TRUE
BuildOption(conf):  -DBUILD_TESTING:BOOL=TRUE
BuildOption(conf):  -DCMAKE_SKIP_RPATH:BOOL=TRUE
BuildOption(conf):  -DQt6_FOUND=TRUE

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)

%description
This library is used when writing accessibility clients such as screen readers.

%package        devel
Summary:        Development files for libqaccessibilityclient
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for libqaccessibilityclient-qt6.

%check
# skip tests in the build env.

%files
%license LICENSES/*
%{_datadir}/qlogging-categories6/libqaccessibilityclient.categories
%{_libdir}/libqaccessibilityclient-qt6.so.*
%{_bindir}/dumper

%files devel
%doc README.md
%{_includedir}/QAccessibilityClient6/
%{_libdir}/libqaccessibilityclient-qt6.so
%{_libdir}/cmake/QAccessibilityClient6/

%changelog
%autochangelog
