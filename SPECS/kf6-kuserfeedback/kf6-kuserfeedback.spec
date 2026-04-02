# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kuserfeedback
# Full KF6 version (e.g. 6.22.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-kuserfeedback
Version:        6.22.0
Release:        %autorelease
Summary:        Framework for collecting feedback from application users
License:        MIT
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kuserfeedback.git
#!RemoteAsset:  sha256:10e2db5703649bfd377121ea2daf629dae8cc082d0457488a04238d55d9e8b87
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DQT_MAJOR_VERSION:STRING=6
BuildOption(conf):  -DENABLE_DOCS:BOOL=FALSE
BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  bison
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  flex
BuildRequires:  cmake(Qt6Charts) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
KUserFeedback is a framework which allows applications to collect user
telemetry and feedback surveys. It is designed to be compliant with the
KDE Telemetry Policy, which forbids the usage of unique identification.

%package        server
Summary:        Server component of kf6-kuserfeedback
Requires:       (php-sqlite or php-mysql or php-pgsql)
Requires:       kf6-kuserfeedback >= %{version}
Requires:       php

%description    server
KUserFeedback is a framework which allows applications to collect user
telemetry and feedback surveys. This package provides a server component
used to collect telemetry and feedback.

%package        devel
Summary:        Development files for kf6-kuserfeedback
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for kf6-kuserfeedback, a framework for collecting feedback from
application users via telemetry and targeted surveys.

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

mkdir -p %{buildroot}%{_kf6_sharedir}/php/
cp -r src/server %{buildroot}%{_kf6_sharedir}/php/kuserfeedback6
# CMakeLists.txt is not needed there and will trigger a rpmlint warning
rm %{buildroot}%{_kf6_sharedir}/php/kuserfeedback6/CMakeLists.txt

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/org_kde_UserFeedback.categories
%{_kf6_libdir}/libKF6UserFeedbackCore.so.*
%{_kf6_libdir}/libKF6UserFeedbackWidgets.so.*
%dir %{_kf6_qmldir}/org/kde/userfeedback
%{_kf6_qmldir}/org/kde/userfeedback/

%files server
%doc composer.json
%doc INSTALL README.md
%dir %{_kf6_sharedir}/php
%{_kf6_sharedir}/php/kuserfeedback6/

%files devel
%dir %{_kf6_includedir}/KUserFeedback
%{_kf6_includedir}/KUserFeedback/kuserfeedback_version.h
%{_kf6_includedir}/KUserFeedbackCore/
%{_kf6_includedir}/KUserFeedbackWidgets/
%{_kf6_cmakedir}/KF6UserFeedback/
%{_kf6_libdir}/libKF6UserFeedbackCore.so
%{_kf6_libdir}/libKF6UserFeedbackWidgets.so
%{_kf6_mkspecsdir}/qt_KF6UserFeedbackCore.pri
%{_kf6_mkspecsdir}/qt_KF6UserFeedbackWidgets.pri

%changelog
%autochangelog
