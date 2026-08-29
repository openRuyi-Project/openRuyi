# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kitemmodels
# Full KF6 version (e.g. 6.28.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kitemmodels
Version:        6.28.0
Release:        %autorelease
Summary:        Set of item models extending the Qt model-view framework
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kitemmodels.git
#!RemoteAsset:  sha256:e03c5dbfc97fa298de9be58bfeb686518a52ae1236389fbc2436ff84165e7e2b
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
KItemModels provides a set of item models extending the Qt model-view framework.

%package        devel
Summary:        Set of item models extending the Qt model-view framework
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
KItemModels provides a set of item models extending the Qt model-view framework.
Development files.

%files
%license LICENSES/*
%{_kf6_libdir}/libKF6ItemModels.so.*
%{_kf6_debugdir}/kitemmodels.categories
%{_kf6_debugdir}/kitemmodels.renamecategories
%{_kf6_qmldir}/org/kde/kitemmodels/

%files devel
%{_kf6_cmakedir}/KF6ItemModels/
%{_kf6_includedir}/KItemModels/
%{_kf6_libdir}/libKF6ItemModels.so

%changelog
%autochangelog
