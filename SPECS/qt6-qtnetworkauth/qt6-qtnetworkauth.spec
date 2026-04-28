# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtnetworkauth
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtnetworkauth
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - NetworkAuth component
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtnetworkauth
#!RemoteAsset:  sha256:1435eb598172d888d7d1795a297c7623f7d8f3afe010c8f40c5aa100abcf380d
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(xkbcommon) >= 0.4.1

%description
Qt Network Auth provides support for OAuth-based authorization methods.

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
%license LICENSES/GPL*
%{_qt6_libdir}/libQt6NetworkAuth.so.6*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_includedir}/QtNetworkAuth/
%{_qt6_libdir}/libQt6NetworkAuth.so
%{_qt6_libdir}/libQt6NetworkAuth.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtNetworkAuthTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6NetworkAuth/
%{_qt6_libdir}/cmake/Qt6NetworkAuthPrivate/
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_networkauth*.pri
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/pkgconfig/Qt6NetworkAuth.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
