# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname kguiaddons

# Full KF6 version (e.g. 6.22.0)
# %%{!?_kf6_version: %%global _kf6_version %%{version}}
%global _kf6_version 6.22.0

Name:           kf6-kguiaddons
Version:        6.22.0
Release:        %autorelease
Summary:        Utilities for graphical user interfaces
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/kguiaddons
#!RemoteAsset
Source:         https://download.kde.org/stable/frameworks/6.22/%{rname}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-private-devel >= %{qt6_version}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  pkgconfig(wayland-client) >= 1.15
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

# https://community.kde.org/Plasma/Plasma_6#Coinstallability
Provides:       kguiaddons = %{version}-%{release}
Obsoletes:      kguiaddons < %{version}-%{release}

%description
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input.

%package        imports
Summary:        QtQuick bindings for utilities for graphical user interfaces
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    imports
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input. This package provides QtQuick
bindings to use these GUI addons with QML and QtQuick applications.

%package        devel
Summary:        Utilities for graphical user interfaces: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input. Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 \
  -DBUILD_PYTHON_BINDINGS=OFF

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/google-maps-geo-handler.desktop
%{_kf6_applicationsdir}/openstreetmap-geo-handler.desktop
%{_kf6_applicationsdir}/wheelmap-geo-handler.desktop
%{_kf6_bindir}/kde-geo-uri-handler
%{_kf6_debugdir}/kguiaddons.categories
%{_kf6_libdir}/libKF6GuiAddons.so.*

%files imports
%{_kf6_qmldir}/org/kde/guiaddons/

%files devel
%{_kf6_cmakedir}/KF6GuiAddons/
%{_kf6_includedir}/KGuiAddons/
%{_kf6_libdir}/libKF6GuiAddons.so
%{_kf6_pkgconfigdir}/KF6GuiAddons.pc

%changelog
%autochangelog
