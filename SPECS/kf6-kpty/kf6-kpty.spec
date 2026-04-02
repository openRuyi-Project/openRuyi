# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kpty
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kpty
Version:        6.22.0
Release:        %autorelease
Summary:        Primitives to interface with pseudo terminal devices
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kpty.git
#!RemoteAsset:  sha256:e974ae36e609d1fb485782139f8c6aa260fcee8f651da3dd0d175dad1c0b9663
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
This library provides primitives to interface with pseudo terminal devices
as well as a KProcess derived class for running child processes and
communicating with them using a pty.

%package        devel
Summary:        Development files for kpty, a pseudo terminal device interface
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description    devel
This library provides primitives to interface with pseudo terminal devices
as well as a KProcess derived class for running child processes and
communicating with them using a pty.

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_debugdir}/kpty.categories
%{_kf6_libdir}/libKF6Pty.so.*

%files devel
%{_kf6_includedir}/KPty/
%{_kf6_cmakedir}/KF6Pty/
%{_kf6_libdir}/libKF6Pty.so

%changelog
%autochangelog
