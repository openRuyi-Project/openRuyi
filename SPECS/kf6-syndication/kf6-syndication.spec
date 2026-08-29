# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname syndication
# Full KF6 version (e.g. 6.28.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-syndication
Version:        6.28.0
Release:        %autorelease
Summary:        RSS/Atom parsing library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/syndication.git
#!RemoteAsset:  sha256:24db750155b69e3f858997cad0655a2f230f85d587c1063166113bc7690fd7b8
Source:         https://download.kde.org/stable/frameworks/6.28/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
KF6Syndication is an RSS/Atom parsing library by KDE, which
also provides an API to fetch feeds from the network.

%package        devel
Summary:        RSS/Atom parsing library - development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
KF6Syndication is an RSS/Atom parsing library, which
also provides an API to fetch feeds from the network. This
package contains development headers.

%files
%doc README.md
%license LICENSES/*
%{_kf6_debugdir}/syndication.categories
%{_kf6_debugdir}/syndication.renamecategories
%{_kf6_libdir}/libKF6Syndication.so.*

%files devel
%{_kf6_cmakedir}/KF6Syndication/
%{_kf6_includedir}/Syndication/
%{_kf6_libdir}/libKF6Syndication.so

%changelog
%autochangelog
