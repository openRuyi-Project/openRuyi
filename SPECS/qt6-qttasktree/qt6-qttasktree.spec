# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qttasktree
%define short_version 6.12

Name:           qt6-qttasktree
Version:        6.12.0
Release:        %autorelease
Summary:        Asynchronous task composition for Qt
License:        LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
URL:            https://doc.qt.io/qt-6/qttasktree-index.html
VCS:            git:https://code.qt.io/qt/qttasktree.git
#!RemoteAsset:  sha256:d28cac0d1fc2d87fbc8fd70d4f956a79b2d37a039df2766e9ff0f69635596b5e
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -GNinja
BuildOption(conf):  -DQT_BUILD_TESTS=ON
BuildOption(conf):  -DQT_BUILD_EXAMPLES=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES=ON

BuildRequires:  cmake >= 3.25
BuildRequires:  ninja
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  qt6-qtbase-private-devel >= %{version}
BuildRequires:  pkgconfig(Qt6Core) >= %{version}
BuildRequires:  pkgconfig(Qt6Test) >= %{version}
BuildRequires:  pkgconfig(Qt6Widgets) >= %{version}
BuildRequires:  pkgconfig(Qt6Concurrent) >= %{version}
BuildRequires:  pkgconfig(Qt6Network) >= %{version}

%description
Qt TaskTree composes asynchronous operations into sequential or parallel
task groups. It provides process, network and concurrent task adapters.
The Qt 6.12 API is a technology preview.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%package        examples
License:        BSD-3-Clause
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%files
%license LICENSES/LGPL-3.0-only.txt LICENSES/GPL-2.0-only.txt LICENSES/GPL-3.0-only.txt
%{_qt6_libdir}/libQt6TaskTree.so.6*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{version}.spdx

%files devel
%{_qt6_libdir}/libQt6TaskTree.so
%{_qt6_libdir}/libQt6TaskTree.prl
%{_qt6_includedir}/QtTaskTree/
%{_qt6_libdir}/cmake/Qt6TaskTree/
%{_qt6_libdir}/pkgconfig/Qt6TaskTree.pc
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json

%files examples
%license LICENSES/BSD-3-Clause.txt
%{_qt6_examplesdir}/

%changelog
%autochangelog
