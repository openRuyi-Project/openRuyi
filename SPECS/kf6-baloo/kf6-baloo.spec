# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname baloo
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-baloo
Version:        6.22.0
Release:        %autorelease
Summary:        Framework for searching and managing metadata
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/baloo.git
#!RemoteAsset:  sha256:57b2ac1ae953d499b7364125fe3e7aa5857fb532456ecf0bda2635e875a66d2a
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  attr-devel
BuildRequires:  lmdb-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{_kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{_kf6_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{_kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{_kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{_kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
Baloo is a framework for searching and managing metadata.

%package        file
Summary:        Filesearch components for Baloo Framework
Requires:       qt6-qtbase
Conflicts:      baloo5-file

%description    file
Baloo is a framework for searching and managing metadata. This
package contains filesearch components.

%package        kioslaves
Summary:        KIO slave components for Baloo Framework
Requires:       kf6-kded

%description    kioslaves
Baloo is a framework for searching and managing metadata. This
package contains KIO slave components.

%package        tools
Summary:        Aditional components for Baloo Framework

%description    tools
Baloo is a framework for searching and managing metadata. This
package contains aditional command line utilities.

%package        devel
Summary:        Development package for baloo6
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       lmdb-devel
Requires:       cmake(KF6CoreAddons) >= %{_kf6_version}
Requires:       cmake(KF6FileMetaData) >= %{_kf6_version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description    devel
Baloo is a framework for searching and managing metadata. This
package contains aditional command line utilities. Development files.

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%post file
%systemd_user_post kde-baloo.service

%preun file
%systemd_user_preun kde-baloo.service

%postun file
%systemd_user_postun kde-baloo.service

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_libdir}/libKF6Baloo.so.*
%{_kf6_libdir}/libKF6BalooEngine.so.*
%{_kf6_qmldir}/org/kde/baloo/

%files file
%{_kf6_bindir}/balooctl6
%{_kf6_configdir}/autostart/baloo_file.desktop
%{_kf6_debugdir}/baloo.categories
%{_kf6_debugdir}/baloo.renamecategories
%{_kf6_libexecdir}/baloo_file
%{_kf6_libexecdir}/baloo_file_extractor
%{_userunitdir}/kde-baloo.service

%files kioslaves
%{_kf6_plugindir}/kf6/kded/baloosearchmodule.so
%{_kf6_plugindir}/kf6/kio/baloosearch.so
%{_kf6_plugindir}/kf6/kio/tags.so
%{_kf6_plugindir}/kf6/kio/timeline.so

%files tools
%{_kf6_bindir}/baloosearch6
%{_kf6_bindir}/balooshow6

%files devel
%{_kf6_includedir}/Baloo/
%{_kf6_cmakedir}/KF6Baloo/
%{_kf6_libdir}/libKF6Baloo.so
%{_kf6_pkgconfigdir}/KF6Baloo.pc
%{_kf6_sharedir}/dbus-1/interfaces/*.xml

%changelog
%autochangelog
