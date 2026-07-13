# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kdesu
# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kdesu
Version:        6.27.0
Release:        %autorelease
Summary:        User interface for running shell commands with root privileges
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kdesu.git
#!RemoteAsset:  sha256:a8a0c5103cb43dc62952aab76bb7e576e8643dbb31672e2ac2988279ab571700
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6Pty) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(x11)

%description
libkdesu provides functionality for building GUI front ends for
(password asking) console mode programs. For example, kdesu and
kdessh use it to interface with su and ssh respectively.

%package        devel
Summary:        User interface for running shell commands with root privileges
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Pty) >= %{_kf6_version}

%description    devel
libkdesu provides functionality for building GUI front ends for
(password asking) console mode programs. For example, kdesu and
kdessh use it to interface with su and ssh respectively.
Development files.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --all-name --generate-subpackages

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_debugdir}/ksu.categories
%{_kf6_libexecdir}/kdesu_stub
%{_kf6_libexecdir}/kdesud
%{_kf6_libdir}/libKF6Su.so.*

%files devel
%{_kf6_cmakedir}/KF6Su/
%{_kf6_includedir}/KDESu/
%{_kf6_libdir}/libKF6Su.so

%changelog
%autochangelog
