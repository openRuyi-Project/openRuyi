# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lxqt-menu-data
Version:        2.4.0
Release:        %autorelease
Summary:        Menu files for LXQt Panel, Configuration Center and PCManFM-Qt
License:        LGPL-2.1-or-later
URL:            https://github.com/lxqt/lxqt-menu-data
VCS:            git:https://github.com/lxqt/lxqt-menu-data.git
#!RemoteAsset:  sha256:3487e47562dc19e63358a50c81e51cd0cf1a020397943cadd8db35daeb4866cc
Source0:        https://github.com/lxqt/lxqt-menu-data/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(lxqt2-build-tools) >= 2.4.0
BuildRequires:  perl

%description
Freedesktop.org compliant menu files for LXQt Panel, Configuration Center
and PCManFM-Qt/libfm-qt.

%package        devel
Summary:        CMake files for lxqt-menu-data
Requires:       %{name} = %{version}-%{release}

%description    devel
This package provides CMake files for projects that use lxqt-menu-data
as a build-time dependency.

%files
%doc CHANGELOG README.md
%license LICENSE
%dir %{_sysconfdir}/xdg/menus
%config(noreplace) %{_sysconfdir}/xdg/menus/lxqt-*.menu
%dir %{_datadir}/desktop-directories
%{_datadir}/desktop-directories/lxqt-*.directory

%files devel
%{_datadir}/cmake/lxqt-menu-data/

%changelog
%autochangelog
