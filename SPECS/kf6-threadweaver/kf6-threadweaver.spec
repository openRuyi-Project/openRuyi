# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname threadweaver
# Full KF6 version (e.g. 6.28.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-threadweaver
Version:        6.28.0
Release:        %autorelease
Summary:        KDE Helper for multithreaded programming
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/threadweaver.git
#!RemoteAsset:  sha256:ab4a7e1a2ff4ee9e3ebb73097fb93beda6857f08d1c4ab7d15af17c383ffaf7e
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
ThreadWeaver is a helper for multithreaded programming. It uses a job-based
interface to queue tasks and execute them in an efficient way.

You simply divide the workload into jobs, state the dependencies between jobs
and ThreadWeaver will work out the most efficient way of dividing the work
between threads within a set of resource limits.

%package        devel
Summary:        KDE Helper for multithreaded programming
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description    devel
Development files for the KF6 ThreadWeaver library.

%files
%doc README.md
%license LICENSES/*
%{_kf6_libdir}/libKF6ThreadWeaver.so.*

%files devel
%{_kf6_cmakedir}/KF6ThreadWeaver/
%{_kf6_includedir}/ThreadWeaver/
%{_kf6_libdir}/libKF6ThreadWeaver.so

%changelog
%autochangelog
