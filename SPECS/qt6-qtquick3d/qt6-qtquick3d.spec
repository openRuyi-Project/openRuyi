# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtquick3d
%define real_version 6.10.1
%define short_version 6.10

%bcond system_assimp 0
%bcond system_openxr 0

Name:           qt6-qtquick3d
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - Quick3D Libraries and utilities
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtquick3d
#!RemoteAsset:  sha256:17d40272becef0dab71b60333bcf0c23d1d25dcf1df16ee9bf0daa7e4de403e6
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON
%if %{with system_assimp}
BuildOption(conf):  -DFEATURE_system_assimp=ON
%else
BuildOption(conf):  -DFEATURE_system_assimp=OFF
%endif
%if %{with system_openxr}
BuildOption(conf):  -DFEATURE_system_openxr=ON
%else
BuildOption(conf):  -DFEATURE_system_openxr=OFF
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  qt6-qtbase-static >= %{version}
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  qt6-qtdeclarative-static
BuildRequires:  pkgconfig(Qt6QuickTimeline)
BuildRequires:  pkgconfig(Qt6ShaderTools)
%if %{with system_assimp}
BuildRequires:  pkgconfig(assimp) >= 5.0.0
%endif
%if %{with system_openxr}
BuildRequires:  pkgconfig(openxr)
%endif

%description
The Qt 6 Quick3D library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Gui)
Requires:       qt6-qtquick3d
Requires:       pkgconfig(Qt6Quick)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%install -a
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt6_bindir}
for i in * ; do
  case "${i}" in
    balsam|meshdebug|shadergen|balsamui|instancer|materialeditor|shapegen|lightmapviewer)
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
%license LICENSES/GPL*
%{_qt6_libdir}/libQt6Quick3D.so.6*
%{_qt6_libdir}/libQt6Quick3DAssetImport.so.6*
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.so.6*
%{_qt6_libdir}/libQt6Quick3DUtils.so.6*
%{_qt6_libdir}/libQt6Quick3DIblBaker.so.6*
%{_qt6_libdir}/libQt6Quick3DParticles.so.6*
%{_qt6_libdir}/libQt6Quick3DAssetUtils.so.6*
%{_qt6_libdir}/libQt6Quick3DEffects.so.6*
%{_qt6_libdir}/libQt6Quick3DHelpers.so.6*
%{_qt6_libdir}/libQt6Quick3DHelpersImpl.so.6*
%{_qt6_libdir}/libQt6Quick3DParticleEffects.so.6*
%{_qt6_libdir}/libQt6Quick3DGlslParser.so.6*
%{_qt6_libdir}/libQt6Quick3DXr.so.6*
%{_qt6_qmldir}/QtQuick3D/
%{_qt6_pluginsdir}/assetimporters/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_bindir}/balsam-qt6
%{_bindir}/meshdebug-qt6
%{_bindir}/shadergen-qt6
%{_bindir}/balsamui-qt6
%{_bindir}/instancer-qt6
%{_bindir}/materialeditor-qt6
%{_bindir}/shapegen-qt6
%{_bindir}/lightmapviewer-qt6
%{_qt6_bindir}/balsam
%{_qt6_bindir}/meshdebug
%{_qt6_bindir}/shadergen
%{_qt6_bindir}/balsamui
%{_qt6_bindir}/instancer
%{_qt6_bindir}/materialeditor
%{_qt6_bindir}/shapegen
%{_qt6_bindir}/lightmapviewer
%{_qt6_includedir}/QtQuick3D*/
%ifarch x86_64
%dir %{_qt6_libdir}/cmake/Qt6BundledEmbree/
%{_qt6_libdir}/cmake/Qt6BundledEmbree/*.cmake
%{_qt6_libdir}/libQt6BundledEmbree.a
%endif
%if %{without system_openxr}
%dir %{_qt6_libdir}/cmake/Qt6BundledOpenXR/
%{_qt6_libdir}/cmake/Qt6BundledOpenXR/*.cmake
%{_qt6_libdir}/libQt6BundledOpenXR.a
%endif
%{_qt6_libdir}/cmake/Qt6Quick3D*/
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/*.cmake
%{_qt6_libdir}/libQt6Quick3D*.prl
%{_qt6_libdir}/libQt6Quick3D*.so
%{_qt6_pluginsdir}/qmltooling/libqmldbg_quick3dprofiler.so
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6Quick3D.pc
%{_qt6_libdir}/pkgconfig/Qt6Quick3DAssetImport.pc
%{_qt6_libdir}/pkgconfig/Qt6Quick3DAssetUtils.pc
%{_qt6_libdir}/pkgconfig/Qt6Quick3DEffects.pc
%{_qt6_libdir}/pkgconfig/Qt6Quick3DHelpers.pc
%{_qt6_libdir}/pkgconfig/Qt6Quick3DHelpersImpl.pc
%{_qt6_libdir}/pkgconfig/Qt6Quick3DIblBaker.pc
%{_qt6_libdir}/pkgconfig/Qt6Quick3DParticleEffects.pc
%{_qt6_libdir}/pkgconfig/Qt6Quick3DParticles.pc
%{_qt6_libdir}/pkgconfig/Qt6Quick3DRuntimeRender.pc
%{_qt6_libdir}/pkgconfig/Qt6Quick3DUtils.pc
%{_qt6_libdir}/pkgconfig/Qt6Quick3DXr.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
