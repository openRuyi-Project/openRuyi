# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kitemviews
# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kitemviews
Version:        6.27.0
Release:        %autorelease
Summary:        Set of item views extending the Qt model-view framework
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kitemviews
#!RemoteAsset:  sha256:7a286f147144714aa9e8f567dd5a0638a8fb81df97a34a0112f725b72aa36979
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
KItemViews includes a set of views, which can be used with item models. It
includes views for categorizing lists and to add search filters to flat and
hierarchical lists.

%package        devel
Summary:        Set of item views extending the Qt model-view framework
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
KItemViews includes a set of views, which can be used with item models. It
includes views for categorizing lists and to add search filters to flat and
hierarchical lists. Development files.

%install -a
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kitemviews.categories
%{_kf6_libdir}/libKF6ItemViews.so.*

%files devel
%{_kf6_includedir}/KItemViews/
%{_kf6_cmakedir}/KF6ItemViews/
%{_kf6_libdir}/libKF6ItemViews.so
%{_kf6_plugindir}/designer/kitemviews6widgets.so

%changelog
%autochangelog
