# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qttools
%define real_version 6.10.1
%define short_version 6.10

Name:           qt6-qttools
Version:        6.10.1
Release:        %autorelease
Summary:        Qt6 - QtTool components
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io
#!RemoteAsset:  sha256:8148408380ffea03101a26305c812b612ea30dbc07121e58707601522404d49b
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}/submodules/%{qt_module}-everywhere-src-%{real_version}.tar.xz
Source1:        assistant.desktop
Source2:        designer.desktop
Source3:        linguist.desktop
Source4:        qdbusviewer.desktop
BuildSystem:    cmake

# some install dir is error.
Patch0:         0001-fix-install-dir.patch

BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(Qt6Core) >= %{version}
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-static >= %{version}
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}
BuildRequires:  qt6-qtdeclarative-static >= %{version}
BuildRequires:  clang-devel
BuildRequires:  llvm-devel
BuildRequires:  libzstd-devel

%description
Qt Tools contains a set of applications to help with development.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Core)

%description    devel
Development files for %{name}.

%package     -n qt6-assistant
Summary:        Documentation browser for Qt6
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n qt6-assistant
Documentation browser for Qt6.

%package     -n qt6-designer
Summary:        Design GUIs for Qt6 applications
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n qt6-designer
Design GUIs for Qt6 applications.

%package     -n qt6-linguist
Summary:        Qt6 Linguist Tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n qt6-linguist
Tools to add translations to Qt6 applications.

%package     -n qt6-qdbusviewer
Summary:        D-Bus debugger and viewer
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n qt6-qdbusviewer
D-Bus debugger and viewer.

%package     -n qt6-doctools
Summary:        Qt6 doc tools package

%description -n qt6-doctools
Qt6 doc tools package.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%install -a
desktop-file-install --dir=%{buildroot}%{_datadir}/applications --vendor="qt6" %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4}
install -m644 -p -D src/assistant/assistant/images/assistant.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/assistant-qt6.png
install -m644 -p -D src/assistant/assistant/images/assistant-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/assistant-qt6.png
install -m644 -p -D src/designer/src/designer/images/designer.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/designer-qt6.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/qdbusviewer-qt6.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/qdbusviewer-qt6.png
# linguist icons
for icon in src/linguist/linguist/images/icons/linguist-*-32.png ; do
  size=$(echo $(basename ${icon}) | cut -d- -f2)
  install -p -m644 -D ${icon} %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/linguist-qt6.png
done

mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt6_bindir}
for i in * ; do
  case "${i}" in
   assistant|designer|lconvert|linguist|lrelease|lupdate|pixeltool| \
   qcollectiongenerator|qdbus|qdbusviewer|qhelpconverter|qhelpgenerator| \
   qtplugininfo|qdistancefieldgenerator|qdoc|qtdiag)
      ln -v ${i} %{buildroot}%{_bindir}/${i}-qt6
      ln -sv ${i} ${i}-qt6
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
%{_qt6_archdatadir}/sbom/%{qt_module}-%{real_version}.spdx
%{_bindir}/qdbus-qt6
%{_qt6_bindir}/qdbus
%{_qt6_bindir}/qdbus-qt6
%{_qt6_libdir}/libQt6UiTools.so.6*
%{_qt6_libdir}/libQt6Designer.so.6*
%dir %{_qt6_libdir}/cmake/Qt6Designer/
%{_qt6_pluginsdir}/designer/*
%{_qt6_libdir}/libQt6DesignerComponents.so.6*
%{_qt6_libdir}/libQt6Help.so.6*
%{_qt6_libdir}/libQt6Designer*.prl
%{_qt6_libdir}/libQt6Help.prl
%{_qt6_libdir}/libQt6UiTools.prl

%files -n qt6-assistant
%{_bindir}/assistant-qt6
%{_qt6_bindir}/assistant*
%{_datadir}/applications/*assistant.desktop
%{_datadir}/icons/hicolor/*/apps/assistant*.*

%files -n qt6-doctools
%{_bindir}/qdoc*
%{_qt6_bindir}/qdoc*
%{_bindir}/qdistancefieldgenerator*
%{_qt6_bindir}/qdistancefieldgenerator*
%{_qt6_libexecdir}/qhelpgenerator*
%{_qt6_libexecdir}/qtattributionsscanner*

%files -n qt6-designer
%{_bindir}/designer*
%{_qt6_bindir}/designer*
%{_datadir}/applications/*designer.desktop
%{_datadir}/icons/hicolor/*/apps/designer*.*

%files -n qt6-linguist
%{_bindir}/linguist*
%{_qt6_bindir}/linguist*
%{_datadir}/qt6/phrasebooks/*.qph
%{_datadir}/applications/*linguist.desktop
%{_datadir}/icons/hicolor/*/apps/linguist*.*
%{_bindir}/lconvert*
%{_bindir}/lrelease*
%{_bindir}/lupdate*
%{_qt6_bindir}/lconvert*
%{_qt6_bindir}/lrelease*
%{_qt6_bindir}/lupdate*
%{_qt6_libexecdir}/lprodump*
%{_qt6_libexecdir}/lrelease*
%{_qt6_libexecdir}/lupdate*

%files -n qt6-qdbusviewer
%{_bindir}/qdbusviewer*
%{_qt6_bindir}/qdbusviewer*
%{_datadir}/applications/*qdbusviewer.desktop
%{_datadir}/icons/hicolor/*/apps/qdbusviewer*.*

%files devel
%{_bindir}/pixeltool*
%{_bindir}/qtdiag*
%{_bindir}/qtplugininfo*
%{_qt6_bindir}/pixeltool*
%{_qt6_bindir}/qtdiag*
%{_qt6_bindir}/qtplugininfo*
%{_qt6_includedir}/QtQDoc*/
%{_qt6_includedir}/QtDesigner/
%{_qt6_includedir}/QtDesignerComponents/
%{_qt6_includedir}/QtHelp/
%{_qt6_includedir}/QtUiPlugin/
%{_qt6_includedir}/QtUiTools/
%{_qt6_includedir}/QtTools/
%{_qt6_libdir}/libQt6Designer*.so
%{_qt6_libdir}/libQt6Help.so
%{_qt6_libdir}/libQt6UiTools.so
%{_qt6_libdir}/cmake/Qt6*/
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6Designer.pc
%{_qt6_libdir}/pkgconfig/Qt6Help.pc
%{_qt6_libdir}/pkgconfig/Qt6Linguist.pc
%{_qt6_libdir}/pkgconfig/Qt6UiPlugin.pc
%{_qt6_libdir}/pkgconfig/Qt6UiTools.pc

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
