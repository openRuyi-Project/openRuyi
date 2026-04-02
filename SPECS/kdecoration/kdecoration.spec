# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

%global sover 6
%global private_sover 2

Name:           kdecoration
Version:        6.5.5
Release:        %autorelease
Summary:        KDE's window decorations library
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/kdecoration.git
#!RemoteAsset:  sha256:dc217bc6374f07a427b6d78de677b1878e9af47352c6addeb89426211b53681a
Source:         https://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
Plugin based library to create window decorations.

%package        devel
Summary:        KDE's window decorations library (development package)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Gui)

%description    devel
Development files belonging to kdecoration,
plugin based library to create window decorations.

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_libdir}/libkdecorations3.so.%{sover}
%{_kf6_libdir}/libkdecorations3.so.*
%{_kf6_libdir}/libkdecorations3private.so.%{private_sover}
%{_kf6_libdir}/libkdecorations3private.so.*

%files devel
%{_includedir}/KDecoration3/
%{_kf6_cmakedir}/KDecoration3/
%{_kf6_includedir}/kdecoration3_version.h
%{_kf6_libdir}/libkdecorations3.so
%{_kf6_libdir}/libkdecorations3private.so

%changelog
%autochangelog
