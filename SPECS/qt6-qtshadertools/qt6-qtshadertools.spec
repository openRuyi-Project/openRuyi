# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtshadertools
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtshadertools
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - Qt Shader Tools module builds on the SPIR-V Open Source Ecosystem
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtshadertools
#!RemoteAsset
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  pkgconfig(xkbcommon) >= 0.4.1

%description
Qt Shader Tools module builds on the SPIR-V Open Source Ecosystem.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       spirv-tools

%description    devel
Development files for %{name}.

%install -a
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt6_bindir}
for i in * ; do
  case "${i}" in
    qsb)
      ln -v ${i} %{buildroot}%{_bindir}/${i}-qt6
      ;;
    *)
      ln -v ${i} %{buildroot}%{_bindir}/${i}
      ;;
  esac
done
popd

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
%license LICENSES/*
%{_qt6_libdir}/libQt6ShaderTools.so.6*
%{_bindir}/qsb-qt6
%{_qt6_bindir}/qsb
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_qt6_includedir}/QtShaderTools/
%{_qt6_libdir}/libQt6ShaderTools.so
%{_qt6_libdir}/libQt6ShaderTools.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtShaderToolsTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6ShaderTools/
%{_qt6_libdir}/cmake/Qt6ShaderToolsPrivate/
%{_qt6_libdir}/cmake/Qt6ShaderToolsTools/
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}//modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6ShaderTools.pc

%changelog
%autochangelog
