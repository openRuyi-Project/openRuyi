# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global pypi_name pyside6
%global camel_name PySide6
%global qt6ver 6.10.1

Name:           python-%{pypi_name}
Version:        6.10.1
Release:        %autorelease
Summary:        Python bindings for the Qt 6 cross-platform application and UI framework
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://wiki.qt.io/Qt_for_Python
VCS:            git:https://github.com/qtproject/pyside-pyside-setup
#!RemoteAsset:  sha256:fd54f40853d61dfd845dbb40d4f89fbd63df5ed341b3d9a2c77bb5c947a0a838
Source0:        https://download.qt.io/official_releases/QtForPython/%{pypi_name}/%{camel_name}-%{qt6ver}-src/pyside-setup-everywhere-src-%{version}.tar.xz
BuildSystem:    cmake

# Revert header installation paths to use standard system include directories.
Patch0:         0001-Revert-Modify-headers-installation-for-CMake-builds.patch
# Unconditionally link against Python libraries on all platforms.
Patch1:         0002-Always-link-to-python-libraries.patch
# Install CMake configuration files and binaries to standard system locations.
Patch2:         0003-Fix-installation.patch

BuildOption(conf):  -DCMAKE_BUILD_TYPE=Release
BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DBUILD_DOCS=OFF
BuildOption(conf):  -DNO_QT_TOOLS=yes
BuildOption(conf):  -DCMAKE_SKIP_INSTALL_RPATH=ON
BuildOption(conf):  -DCMAKE_BUILD_RPATH_USE_ORIGIN=ON
BuildOption(conf):  -DFORCE_LIMITED_API=no

BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  clang-devel
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(packaging)
BuildRequires:  qt6-macros
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6MultimediaWidgets)
BuildRequires:  pkgconfig(Qt6Positioning)
BuildRequires:  cmake(Qt6Location)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  cmake(Qt6Nfc)
BuildRequires:  cmake(Qt6Quick3D)
BuildRequires:  cmake(Qt6Scxml)
BuildRequires:  cmake(Qt6Sensors)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6SerialBus)
BuildRequires:  cmake(Qt6StateMachine)
BuildRequires:  cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6SpatialAudio)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6DataVisualization)
BuildRequires:  cmake(Qt6Graphs)
BuildRequires:  cmake(Qt6GraphsWidgets)
BuildRequires:  cmake(Qt6Bluetooth)
BuildRequires:  cmake(Qt6WebChannel)
# we don't have yet.
# BuildRequires:  cmake(Qt6WebEngineCore)
# BuildRequires:  cmake(Qt6WebEngineWidgets)
# BuildRequires:  cmake(Qt6WebEngineQuick)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6HttpServer)
BuildRequires:  cmake(Qt63DCore)
BuildRequires:  cmake(Qt63DRender)
BuildRequires:  cmake(Qt63DInput)
BuildRequires:  cmake(Qt63DLogic)
BuildRequires:  cmake(Qt63DAnimation)
BuildRequires:  cmake(Qt63DExtras)
BuildRequires:  cmake(Qt6RemoteObjects)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  qt6-designer

Provides:       python3-%{pypi_name} = %{version}-%{release}
Provides:       python3-%{pypi_name}%{?_isa} = %{version}-%{release}
%python_provide python3-%{pypi_name}

%description
PySide6 is the official Python module from the Qt for Python project, which
provides access to the complete Qt 6+ framework.

%package     -n python-%{pypi_name}-devel
Summary:        Development files related to %{name}
Requires:       pyside6-tools
Requires:       shiboken6
Provides:       python3-%{pypi_name}-devel = %{version}-%{release}
Provides:       python3-%{pypi_name}-devel%{?_isa} = %{version}-%{release}
%description -n python-%{pypi_name}-devel
Development files for PySide6.

%package     -n pyside6-tools
Summary:        PySide6 tools for the Qt 6 framework
Requires:       python-%{pypi_name}

%description -n pyside6-tools
PySide6 tools.

%package     -n shiboken6
Summary:        Python / C++ bindings generator for %camel_name

%description -n shiboken6
Shiboken binding generator.

%package     -n python-shiboken6
Summary:        Python / C++ bindings libraries for %camel_name
Provides:       python3-shiboken6 = %{version}-%{release}
Provides:       python3-shiboken6%{?_isa} = %{version}-%{release}
%python_provide python3-shiboken6

%description -n python-shiboken6
Shiboken Python libraries.

%package     -n python-shiboken6-devel
Summary:        Python / C++ bindings helper module for %camel_name
Requires:       shiboken6
Requires:       python-shiboken6
Provides:       python3-shiboken6-devel = %{version}-%{release}
Provides:       python3-shiboken6-devel%{?_isa} = %{version}-%{release}

%description -n python-shiboken6-devel
Shiboken development files.

%prep -a
sed -i 's#${base}/../shiboken6/##' sources/pyside6/CMakeLists.txt

%build -p
# fix can't find stddef.h
CLANG_INC=$(ls -d /usr/lib/clang/*/include | head -n 1)
echo "Injecting CPATH=$CLANG_INC into shiboken_wrapper.sh"
find . -name "shiboken_wrapper.sh" -exec sed -i "2i export CPATH=\"$CLANG_INC:\$CPATH\"" {} +

export PYTHONPATH="$PWD/%{_vpath_builddir}/sources:$PYTHONPATH"

%install -a
cp -r %{_vpath_builddir}/sources/shiboken6/shibokenmodule/{*.py,*.txt} sources/shiboken6/shibokenmodule/
cp -r %{_vpath_builddir}/sources/pyside6/PySide6/*.py sources/pyside6/PySide6/

%{__python3} setup.py --qtpaths=/usr/%{_lib}/qt6/bin/qtpaths install_scripts --install-dir=%{buildroot}%{_bindir}

for name in PySide6 shiboken6 shiboken6_generator; do
  mkdir -p %{buildroot}%{python3_sitearch}/$name-%{version}-py%{python3_version}.egg-info
  cp -p $name.egg-info/{PKG-INFO,top_level.txt} \
        %{buildroot}%{python3_sitearch}/$name-%{version}-py%{python3_version}.egg-info/
  if [ -f $name.egg-info/entry_points.txt ]; then
    cp -p $name.egg-info/entry_points.txt %{buildroot}%{python3_sitearch}/$name-%{version}-py%{python3_version}.egg-info/
  fi
done

# Add symlinks for tools used by pyside_tool.py
mkdir -p %{buildroot}%{python3_sitelib}/%{camel_name}/Qt/libexec
ln -sfr %{_qt6_libexecdir}/{qmlcachegen,qmlimportscanner,qmltyperegistrar,rcc,uic} %{buildroot}%{python3_sitelib}/%{camel_name}/Qt/libexec/
ln -sfr %{_qt6_bindir}/{assistant,balsam,balsamui,designer,linguist,lrelease,lupdate,qmlformat,qmllint,qmlls,qsb} %{buildroot}%{python3_sitelib}/%{camel_name}/

# Create scripts folders (this basically replicates prepare_packages() in build_scripts/main.py)
mkdir -p %{buildroot}%{python3_sitelib}/%{camel_name}/scripts
mv %{buildroot}%{_bindir}/{android_deploy.py,deploy_lib,deploy.py,metaobjectdump.py,project_lib,project.py,pyside_tool.py,qml.py,qtpy2cpp_lib,qtpy2cpp.py,requirements-android.txt} %{buildroot}%{python3_sitelib}/%{camel_name}/scripts
mkdir -p %{buildroot}%{python3_sitelib}/shiboken6_generator/scripts
mv %{buildroot}%{_bindir}/shiboken_tool.py %{buildroot}%{python3_sitelib}/shiboken6_generator/scripts

# Fix CMake config files to use correct absolute paths (OpenSUSE solution)
# The upstream build is designed for wheel installation with relative paths,
# but for system installation we need absolute paths
sed -i 's#/typesystems#/share/PySide6/typesystems#g' %{buildroot}%{_libdir}/cmake/PySide6/*.cmake
sed -i 's#/glue#/share/PySide6/glue#g' %{buildroot}%{_libdir}/cmake/PySide6/*.cmake

# Fix all Python shebangs recursively
# -p preserves timestamps
# -n prevents creating ~backup files
# -i specifies the interpreter for the shebang
# Need to list files that do not match ^[a-zA-Z0-9_]+\.py$ explicitly!
%py3_shebang_fix %{buildroot}%{python3_sitelib}/%{camel_name}/scripts
%py3_shebang_fix %{buildroot}%{python3_sitelib}/shiboken6_generator/scripts

%check
export LD_LIBRARY_PATH="%{buildroot}%{_libdir}"
%py3_check_import PySide6
%py3_check_import shiboken6

%files
%license LICENSES/*
%{_libdir}/libpyside6*.so.6*
%{python3_sitelib}/PySide6/
%{python3_sitearch}/PySide6-%{version}-py%{python3_version}.egg-info/

%files -n python-pyside6-devel
%{_datadir}/PySide6/
%{_includedir}/PySide6/
%{_libdir}/libpyside6*.so
%{_libdir}/libpyside6remoteobjects.a
%{_libdir}/cmake/PySide6*
%{_libdir}/pkgconfig/pyside6.pc

%files -n pyside6-tools
%{_bindir}/pyside*
%{_libdir}/qt6/plugins/designer/libPySidePlugin.so

%files -n shiboken6
%{_libdir}/cmake/Shiboken6Tools/*

%files -n python-shiboken6
%{_libdir}/libshiboken6*.so.6*
%{python3_sitelib}/shiboken6/
%{python3_sitearch}/shiboken6-%{version}-py%{python3_version}.egg-info/

%files -n python-shiboken6-devel
%{_bindir}/shiboken6*
%{_includedir}/shiboken6/
%{_libdir}/cmake/Shiboken6/
%{_libdir}/libshiboken6*.so
%{_libdir}/pkgconfig/shiboken6.pc
%{python3_sitelib}/shiboken6_generator/
%{python3_sitearch}/shiboken6_generator-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
