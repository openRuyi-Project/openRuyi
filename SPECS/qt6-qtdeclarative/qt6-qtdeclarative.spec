# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtdeclarative
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qtdeclarative
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - QtDeclarative component
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtdeclarative
#!RemoteAsset:  sha256:4fb4efb894e0b96288543505d69794d684bcfbe4940ce181d3e6817bda54843e
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
BuildSystem:    cmake

## upstream patches
# https://codereview.qt-project.org/c/qt/qtdeclarative/+/678924
Patch0:         qtdeclarative-quickshapes-make-module-public.patch

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtlanguageserver-devel >= %{version}
BuildRequires:  pkgconfig(Qt6ShaderTools) >= %{version}
BuildRequires:  pkgconfig(Qt6Svg) >= %{version}
BuildRequires:  python3
BuildRequires:  pkgconfig(xkbcommon) >= 0.4.1

%description
Qt Declarative (QML and Quick) module provides a declarative framework
for building highly dynamic, custom user interfaces.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Core)
Provides:       qt6-quickcontrols2-devel = %{version}-%{release}
Provides:       %{name}-private-devel = %{version}-%{release}

%description    devel
Development files for %{name}.

%package        static
Summary:        Static library files for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
Static library files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       qt6-quickcontrols2-examples = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%install -a
find %{buildroot}%{_qt6_libdir} -type f -name "*.o" -delete -print
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt6_bindir}
for i in * ; do
  case "${i}" in
    qmlcachegen|qmlleasing|qmlformat|qmleasing|qmlimportscanner|qmllint| \
    qmlpreview|qmlscene|qmltestrunner|qmltyperegistrar|qmlplugindump| \
    qmlprofiler|qml|qmlbundle|qmlmin|qmltime)
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
  rm -fv "$(basename ${prl_file} .prl).la"
  sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
done
popd

%files
%license LICENSES/LGPL*
%{_qt6_libdir}/libQt6Labs*.so.6*
%{_qt6_libdir}/libQt6Qml.so.6*
%{_qt6_libdir}/libQt6QmlCompiler.so.*
%{_qt6_libdir}/libQt6QmlCore.so.6*
%{_qt6_libdir}/libQt6QmlLocalStorage.so.6*
%{_qt6_libdir}/libQt6QmlMeta.so.6*
%{_qt6_libdir}/libQt6QmlModels.so.6*
%{_qt6_libdir}/libQt6QmlNetwork.so.6*
%{_qt6_libdir}/libQt6QmlWorkerScript.so.6*
%{_qt6_libdir}/libQt6QmlXmlListModel.so.6*
%{_qt6_libdir}/libQt6Quick.so.6*
%{_qt6_libdir}/libQt6QuickControls2*.so.6*
%{_qt6_libdir}/libQt6QuickDialogs2*.so.6*
%{_qt6_libdir}/libQt6QuickEffects.so.6*
%{_qt6_libdir}/libQt6QuickLayouts.so.6*
%{_qt6_libdir}/libQt6QuickParticles.so.6*
%{_qt6_libdir}/libQt6QuickShapes.so.6*
%{_qt6_libdir}/libQt6QuickShapesDesignHelpers.so.6*
%{_qt6_libdir}/libQt6QuickTemplates2.so.6*
%{_qt6_libdir}/libQt6QuickTest.so.6*
%{_qt6_libdir}/libQt6QuickVectorImage*.so.6*
%{_qt6_libdir}/libQt6QuickWidgets.so.6*
%{_qt6_pluginsdir}/qmltooling/
%{_qt6_pluginsdir}/qmllint/
%{_qt6_pluginsdir}/qmlls/
%{_qt6_qmldir}/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx

%files devel
%{_bindir}/qml*
%{_bindir}/svgtoqml
%{_qt6_bindir}/qml*
%{_qt6_bindir}/svgtoqml
%{_qt6_libexecdir}/qml*
%{_qt6_includedir}/QtLabs*/
%{_qt6_includedir}/QtQml*/
%{_qt6_includedir}/QtQuick*/
%{_qt6_libdir}/libQt6Labs*.prl
%{_qt6_libdir}/libQt6Labs*.so
%{_qt6_libdir}/libQt6Qml*.prl
%{_qt6_libdir}/libQt6Qml*.so
%{_qt6_libdir}/libQt6Quick*.prl
%{_qt6_libdir}/libQt6Quick*.so
%{_qt6_libdir}/cmake/Qt6*/
%{_qt6_mkspecsdir}/features/*.prf
%{_qt6_descriptionsdir}/*.json
%{_qt6_metatypesdir}/*.json
%{_qt6_mkspecsdir}/modules/qt_lib_*.pri
%{_qt6_libdir}/pkgconfig/Qt6LabsAnimation.pc
%{_qt6_libdir}/pkgconfig/Qt6LabsFolderListModel.pc
%{_qt6_libdir}/pkgconfig/Qt6LabsPlatform.pc
%{_qt6_libdir}/pkgconfig/Qt6LabsQmlModels.pc
%{_qt6_libdir}/pkgconfig/Qt6LabsSettings.pc
%{_qt6_libdir}/pkgconfig/Qt6LabsSharedImage.pc
%{_qt6_libdir}/pkgconfig/Qt6LabsSynchronizer.pc
%{_qt6_libdir}/pkgconfig/Qt6LabsWavefrontMesh.pc
%{_qt6_libdir}/pkgconfig/Qt6Qml.pc
%{_qt6_libdir}/pkgconfig/Qt6QmlCompiler.pc
%{_qt6_libdir}/pkgconfig/Qt6QmlCore.pc
%{_qt6_libdir}/pkgconfig/Qt6QmlIntegration.pc
%{_qt6_libdir}/pkgconfig/Qt6QmlLocalStorage.pc
%{_qt6_libdir}/pkgconfig/Qt6QmlMeta.pc
%{_qt6_libdir}/pkgconfig/Qt6QmlModels.pc
%{_qt6_libdir}/pkgconfig/Qt6QmlNetwork.pc
%{_qt6_libdir}/pkgconfig/Qt6QmlWorkerScript.pc
%{_qt6_libdir}/pkgconfig/Qt6QmlXmlListModel.pc
%{_qt6_libdir}/pkgconfig/Qt6Quick.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickControls2.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickControls2Basic.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickControls2BasicStyleImpl.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickControls2FluentWinUI3StyleImpl.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickControls2Fusion.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickControls2FusionStyleImpl.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickControls2Imagine.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickControls2ImagineStyleImpl.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickControls2Impl.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickControls2Material.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickControls2MaterialStyleImpl.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickControls2Universal.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickControls2UniversalStyleImpl.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickDialogs2.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickDialogs2QuickImpl.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickDialogs2Utils.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickEffects.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickLayouts.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickShapes.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickTemplates2.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickTest.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickVectorImage.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickVectorImageHelpers.pc
%{_qt6_libdir}/pkgconfig/Qt6QuickWidgets.pc

%files static
%{_qt6_libdir}/*.a
%{_qt6_libdir}/*.prl
%{_qt6_includedir}/QtPacketProtocol/

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
