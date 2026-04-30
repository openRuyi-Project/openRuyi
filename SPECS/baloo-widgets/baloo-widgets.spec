# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.19.0
%define qt6_version 6.9.0

Name:           baloo-widgets
Version:        25.12.3
Release:        %autorelease
Summary:        Framework for searching and managing metadata
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/libraries/baloo-widgets.git
#!RemoteAsset:  sha256:0b03fc0adfeda46deeb53fb5e22bb9108715ebc1d8f5b19ca4e5c2216332c711
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Baloo) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
Baloo is a framework for searching and managing metada

%package        devel
Summary:        Development package for baloo-widgets
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6KIO) >= %{kf6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description    devel
Development package for baloo-widgets

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/baloo_filemetadata_temp_extractor
%{_kf6_debugdir}/baloo-widgets.categories
%{_kf6_libdir}/libKF6BalooWidgets.so.*
%dir %{_kf6_plugindir}/kf6/propertiesdialog
%{_kf6_plugindir}/kf6/propertiesdialog/baloofilepropertiesplugin.so
%dir %{_kf6_plugindir}/kf6/kfileitemaction
%{_kf6_plugindir}/kf6/kfileitemaction/tagsfileitemaction.so

%files devel
%{_kf6_cmakedir}/KF6BalooWidgets/
%{_kf6_includedir}/BalooWidgets/
%{_kf6_libdir}/libKF6BalooWidgets.so

%changelog
%autochangelog
