# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           calamares
Version:        3.4.2
Release:        %autorelease
Summary:        Installer from a live CD/DVD/USB to disk
License:        BSD-2-Clause
URL:            https://calamares.io/
VCS:            git:https://codeberg.org/Calamares/calamares.git
#!RemoteAsset:  sha256:733bbbb00dc9f84874bd5c22960952f317ea2537565431179fa2152b2fbfdccc
Source0:        https://codeberg.org/Calamares/calamares/releases/download/v%{version}/%{name}-%{version}.tar.gz
# TODO: Use KDE BuildSystem in the future

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig(libparted)
BuildRequires:  pkgconfig(libxcrypt)
BuildRequires:  cmake(Qt6Core)
# For "/usr/lib64/qt6/bin/lconvert"
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(polkit-qt6-1)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(KF6CoreAddons)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  cmake(AppStreamQt)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(KPMcore)

# Can we shrink these dependencies? - 251
Requires:       coreutils
Requires:       util-linux
Requires:       NetworkManager
Requires:       dracut
Requires:       grub
Requires:       e2fsprogs
Requires:       dosfstools
Requires:       ntfs-3g
Requires:       gawk
Requires:       systemd
Requires:       rsync
Requires:       shadow
Requires:       dnf
# If we don't have kdesu then we need polkit. - 251
Requires:       polkit
Requires:       hicolor-icon-theme

%description
Calamares is a distribution-independent installer framework, designed to install
from a live CD/DVD/USB environment to a hard disk. It includes a graphical
installation program based on Qt 6.

%package        devel
Summary:        Development files for calamares
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and libraries needed to develop
applications that use the calamares installer framework.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%{cmake_kf6} -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
             -DBUILD_TESTING:BOOL=OFF \
             -DWITH_PYBIND11:BOOL=OFF \
             -DWITH_QT6:BOOL=ON
%cmake_build

%install
%cmake_install

# Should we split the python bindings into a separate package? - 251
# TODO: Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang calamares-python --generate-subpackages

%files -f calamares-python.lang
%doc AUTHORS
%license LICENSES/*
%{_bindir}/calamares
%dir %{_datadir}/calamares/
%dir %{_datadir}/calamares/branding/
%{_datadir}/calamares/branding/default/*
%{_datadir}/calamares/qml/*
%{_datadir}/applications/calamares.desktop
%{_datadir}/icons/hicolor/scalable/apps/calamares.svg
%{_mandir}/man8/calamares.8*
# polkit
%{_datadir}/polkit-1/actions/io.calamares.calamares.policy
# libs
%{_libdir}/libcalamares.so.*
%{_libdir}/libcalamaresui.so.*
%{_libdir}/calamares/
# interactiveterminal
#{_datadir}/calamares/modules/interactiveterminal.conf
#{_libdir}/calamares/modules/interactiveterminal/
# plasmalnf
#{_datadir}/calamares/modules/plasmalnf.conf
#{_libdir}/calamares/modules/plasmalnf/

%files devel
%{_includedir}/libcalamares/
%{_libdir}/libcalamares.so
%{_libdir}/libcalamaresui.so
%{_libdir}/cmake/Calamares/

%changelog
%autochangelog
