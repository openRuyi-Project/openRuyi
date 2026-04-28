# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtconnectivity
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtconnectivity
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - Connectivity components
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtconnectivity
#!RemoteAsset:  sha256:7baefd3a90c73820e33ddc59ded8c018e233d14d23eaa4eadbf332b5ac2154ff
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(xkbcommon) >= 0.4.1
BuildRequires:  pkgconfig(openssl)

%description
Qt Connectivity provides classes and functions to access Bluetooth and NFC
hardware.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Network)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%install -a
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

%files
%license LICENSES/GPL* LICENSES/LGPL*
%{_qt6_libexecdir}/sdpscanner
%{_qt6_libdir}/libQt6Bluetooth.so.6*
%{_qt6_libdir}/libQt6Nfc.so.6*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_includedir}/QtBluetooth/
%{_qt6_includedir}/QtConnectivity/
%{_qt6_includedir}/QtNfc/
%{_qt6_libdir}/libQt6Bluetooth.so
%{_qt6_libdir}/libQt6Bluetooth.prl
%{_qt6_libdir}/libQt6Nfc.so
%{_qt6_libdir}/libQt6Nfc.prl
%{_qt6_libdir}/cmake/Qt6Bluetooth/
%{_qt6_libdir}/cmake/Qt6BluetoothPrivate/
%{_qt6_libdir}/cmake/Qt6Connectivity/
%{_qt6_libdir}/cmake/Qt6Nfc/
%{_qt6_libdir}/cmake/Qt6NfcPrivate/
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/pkgconfig/Qt6Bluetooth.pc
%{_qt6_libdir}/pkgconfig/Qt6Nfc.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
