# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           libplasma
Version:        6.5.5
Release:        %autorelease
Summary:        Plasma library and runtime components based upon KF6 and Qt6
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/libplasma
#!RemoteAsset
Source:         https://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.10.0
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(wayland-client) >= 1.9
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-xfixes)

%description
Plasma library and runtime components based upon KF6 and Qt6

%package        devel
Summary:        Plasma library and runtime components
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Package) >= %{kf6_version}
Requires:       cmake(KF6WindowSystem) >= %{kf6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}
Requires:       cmake(Qt6Quick) >= %{qt6_version}
Conflicts:      plasma-framework-devel

%description    devel
Plasma library and runtime components based upon KF6 and Qt6

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%license LICENSES/*.txt
%doc README.md
%{_kf6_debugdir}/plasma-framework.categories
%{_kf6_debugdir}/plasma-framework.renamecategories
%{_kf6_libdir}/libPlasma.so.*
%{_kf6_libdir}/libPlasmaQuick.so.*
%{_kf6_plugindir}/kf6/kirigami/
%{_kf6_plugindir}/kf6/packagestructure/
%{_kf6_qmldir}/org/kde/kirigami/
%{_kf6_qmldir}/org/kde/plasma/
%{_datadir}/plasma/desktoptheme/

%files devel
%doc %{_kf6_qchdir}/Plasma.*
%{_kf6_cmakedir}/Plasma/
%{_kf6_cmakedir}/PlasmaQuick/
%{_includedir}/Plasma/
%{_includedir}/PlasmaQuick/
%{_kf6_libdir}/libPlasma.so
%{_kf6_libdir}/libPlasmaQuick.so
%{_kf6_sharedir}/kdevappwizard/

%files doc
%{_kf6_qchdir}/*.qch
%{_kf6_qchdir}/*.tags

%changelog
%autochangelog
