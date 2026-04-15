# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname PyQt6
%global pypi_name pyqt6

Name:           python-PyQt6
Version:        6.10.1
Release:        %autorelease
Summary:        PyQt6 is Python bindings for Qt6
License:        GPL-3.0-only
URL:            http://www.riverbankcomputing.com/software/pyqt/
#!RemoteAsset:  sha256:d733a6c712c0b7a7b99e4ad59b211ea25a5d1b9d1131e47a1f50b5e524266e57
Source0:        https://pypi.python.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
Source1:        macros.pyqt6
BuildSystem:    autotools

BuildOption(build):  -C build
BuildOption(install):  INSTALL_ROOT=%{buildroot} -C build

BuildRequires:  qt6-macros
BuildRequires:  make
BuildRequires:  chrpath
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-python)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6SerialPort)
BuildRequires:  pkgconfig(Qt6SerialBus)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Positioning)
BuildRequires:  pkgconfig(Qt6Sensors)
BuildRequires:  pkgconfig(Qt6WebChannel)
BuildRequires:  pkgconfig(Qt6WebSockets)
BuildRequires:  pkgconfig(Qt6Quick3D)
BuildRequires:  pkgconfig(Qt6RemoteObjects)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-PyQt-builder
BuildRequires:  python3dist(dbus-python)
BuildRequires:  python3dist(sip)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
Provides:       PyQt6 = %{version}-%{release}

Requires:       %{name}-rpm-macros = %{version}-%{release}

%description
PyQt6 is Python bindings for Qt6.

%package        rpm-macros
Summary:        RPM macros %{name}
BuildArch:      noarch

%description    rpm-macros
RPM macros for PyQt6.

%package        devel
Summary:        Development files for python3-PyQt6
Requires:       python3-PyQt6 = %{version}-%{release}
Requires:       pkgconfig(Qt6Core)
Provides:       python3-PyQt6-devel
%python_provide python3-PyQt6-devel

%description    devel
Development files for python3-PyQt6.

# No configure.
%conf

%build -p
sip-build \
  --no-make \
  --qt-shared \
  --confirm-license \
  --qmake=%{__qt6_qmake} \
  --api-dir=%{_qt6_datadir}/qsci/api/python \
  --verbose \
  --dbus=%{_includedir}/dbus-1.0/ \
  --pep484-pyi \
  --qmake-setting 'QMAKE_CFLAGS_RELEASE="%{build_cflags}"' \
  --qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%{build_cxxflags} `pkg-config --cflags dbus-python` -DQT_NO_INT128"' \
  --qmake-setting 'QMAKE_LFLAGS_RELEASE="%{build_ldflags}"'

%install -a
# Explicitly byte compile as the automagic byte compilation doesn't work for
# /app prefix in flatpak builds
%py_byte_compile %{__python3} %{buildroot}%{python3_sitearch}/PyQt6

# rpm macros
install -p -m644 -D %{SOURCE1} \
  %{buildroot}%{_rpmmacrodir}/macros.pyqt6
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch:}}%{version}-%{release}|g" \
  %{buildroot}%{_rpmmacrodir}/macros.pyqt6

%check
# No tests.

%files
%doc NEWS
%license LICENSE
%dir %{python3_sitearch}/PyQt6/
%{python3_sitearch}/PyQt6/QtMultimedia.*
%{python3_sitearch}/PyQt6/QtMultimediaWidgets.*
%{python3_sitearch}/PyQt6/QtPositioning.*
%{python3_sitearch}/PyQt6/QtQml.*
%{python3_sitearch}/PyQt6/QtQuick.*
%{python3_sitearch}/PyQt6/QtQuickWidgets.*
%{python3_sitearch}/PyQt6/QtSensors.*
%{python3_sitearch}/PyQt6/QtSerialPort.*
%{python3_sitearch}/PyQt6/QtSvg.*
%{python3_sitearch}/PyQt6/QtSvgWidgets.*
%{python3_sitearch}/PyQt6/QtWebChannel.*
%{python3_sitearch}/PyQt6/QtWebSockets.*
%{python3_sitearch}/PyQt6/QtOpenGLWidgets.*
%{python3_sitearch}/PyQt6/QtQuick3D.*
%{python3_sitearch}/PyQt6/QtRemoteObjects.*
%{python3_sitearch}/PyQt6/QtSpatialAudio.*
%{python3_sitearch}/pyqt6-*.dist-info
%{python3_sitearch}/PyQt6/__pycache__/__init__.*
%{python3_sitearch}/PyQt6/__init__.py*
%{python3_sitearch}/PyQt6/QtCore.*
%{python3_sitearch}/PyQt6/QtDBus.*
%{python3_sitearch}/PyQt6/QtGui.*
%{python3_sitearch}/PyQt6/QtNetwork.*
%{python3_sitearch}/PyQt6/QtOpenGL.*
%{python3_sitearch}/PyQt6/QtPrintSupport.*
%{python3_sitearch}/PyQt6/QtSql.*
%{python3_sitearch}/PyQt6/QtTest.*
%{python3_sitearch}/PyQt6/QtWidgets.*
%{python3_sitearch}/PyQt6/QtXml.*
%{python3_sitearch}/dbus/mainloop/pyqt6.abi3.so
# plugins
%{_qt6_pluginsdir}/PyQt6/
%{python3_sitearch}/PyQt6/uic/
%{python3_sitearch}/PyQt6/lupdate/
%{_bindir}/pylupdate6
%{_bindir}/pyuic6
%{python3_sitearch}/PyQt6/py.typed
%{python3_sitearch}/PyQt6/sip.pyi
%doc examples/
%dir %{_qt6_datadir}/qsci/
%dir %{_qt6_datadir}/qsci/api/
%dir %{_qt6_datadir}/qsci/api/python/
%doc %{_qt6_datadir}/qsci/api/python/PyQt6.api

%files rpm-macros
%{_rpmmacrodir}/macros.pyqt6

%files devel
%{python3_sitearch}/PyQt6/bindings/

%changelog
%autochangelog
