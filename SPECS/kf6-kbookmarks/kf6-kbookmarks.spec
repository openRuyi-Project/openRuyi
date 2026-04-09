# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kbookmarks
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kbookmarks
Version:        6.22.0
Release:        %autorelease
Summary:        Framework for manipulating bookmarks in XBEL format
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kbookmarks
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
This is a framework for accessing and manipulating bookmarks using
the XBEL format.

%package        devel
Summary:        Development files for kbookmarks, a XBEL format bookmark manipulation framework
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6WidgetsAddons) >= %{_kf6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Requires:       cmake(Qt6Xml) >= %{qt6_version}

%description    devel
Development files for kbookmarks, a framework for accessing and
manipulating bookmarks using the XBEL format

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name}6 --with-qt --all-name --generate-subpackages

%files -f %{name}6.lang
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kbookmarks.categories
%{_kf6_debugdir}/kbookmarks.renamecategories
%{_kf6_debugdir}/kbookmarkswidgets.categories
%{_kf6_libdir}/libKF6Bookmarks.so.*
%{_kf6_libdir}/libKF6BookmarksWidgets.so.*

%files devel
%{_kf6_libdir}/libKF6Bookmarks.so
%{_kf6_libdir}/libKF6BookmarksWidgets.so
%{_kf6_cmakedir}/KF6Bookmarks/
%{_kf6_includedir}/KBookmarks/
%{_kf6_includedir}/KBookmarksWidgets/

%changelog
%autochangelog
