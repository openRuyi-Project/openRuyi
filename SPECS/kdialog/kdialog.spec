# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.19.0
%define qt6_version 6.9.0

Name:           kdialog
Version:        25.12.3
Release:        %autorelease
Summary:        KDE version of xdialog
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kdialog
VCS:            git:https://invent.kde.org/utilities/kdialog
#!RemoteAsset:  sha256:fee5a3d52394916a7adca76eaea471cdd5137b0d27b2ef2936cf100981105ea1
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  pkgconfig(x11)

%description
KDialog can be used to show nice dialog boxes from shell scripts.

%install -a

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license COPYING*
%doc README.md
%{_kf6_applicationsdir}/org.kde.kdialog.desktop
%{_kf6_appstreamdir}/org.kde.kdialog.metainfo.xml
%{_kf6_bindir}/kdialog
%{_kf6_bindir}/kdialog_progress_helper
%{_kf6_dbusinterfacesdir}/org.kde.kdialog.ProgressDialog.xml

%changelog
%autochangelog
