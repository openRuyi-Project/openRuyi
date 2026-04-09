# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dbus-python
Version:        1.4.0
Release:        %autorelease
Summary:        D-Bus Python Bindings (metapackage)
License:        MIT
URL:            https://www.freedesktop.org/wiki/Software/DBusBindings/
VCS:            git:https://gitlab.freedesktop.org/dbus/dbus-python.git
#!RemoteAsset
Source:         https://dbus.freedesktop.org/releases/dbus-python/dbus-python-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  gcc
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  python3-devel
BuildRequires:  python3-pygobject

%description
D-Bus python bindings for use with python programs.
This is a metapackage that requires the main Python 3 package.

%package     -n python-dbus
Summary:        D-Bus bindings for Python 3
Provides:       python3-dbus
%python_provide python3-dbus

%description -n python-dbus
This package contains the D-Bus bindings for Python 3.

%package        devel
Summary:        Libraries and headers for dbus-python

%description    devel
This package contains the header files and static libraries needed for
hooking up custom mainloops to the D-Bus Python bindings.

%files
%doc NEWS
%license COPYING

%files -n python-dbus
%{python3_sitearch}/dbus/
%{python3_sitearch}/*.so

%files devel
%doc README ChangeLog doc/API_CHANGES.txt doc/tutorial.txt
%{_includedir}/dbus-1.0/dbus/dbus-python.h
%{_libdir}/pkgconfig/dbus-python.pc

%changelog
%autochangelog
