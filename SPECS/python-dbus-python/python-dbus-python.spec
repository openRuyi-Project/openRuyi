# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname dbus-python

Name:           python-dbus-python
Version:        1.4.0
Release:        %autorelease
Summary:        D-Bus Python Bindings
License:        MIT
URL:            https://www.freedesktop.org/wiki/Software/DBusBindings/
VCS:            git:https://gitlab.freedesktop.org/dbus/dbus-python.git
#!RemoteAsset:  sha256:c36b28f10ffcc8f1f798aca973bcc132f91f33eb9b6b8904381b4077766043d5
Source:         https://dbus.freedesktop.org/releases/dbus-python/dbus-python-%{version}.tar.xz
# Originally we need the meson BuildSystem
# But we can't generate python3dist(dbus-python) with meson, so we switch to pyproject BuildSystem - 251
BuildSystem:    pyproject

BuildOption(install):  dbus

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  patchelf
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pygobject)
BuildRequires:  python3dist(meson-python)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)

# For compatibility
Provides:       dbus-python
# Pypi name is dbus-python
Provides:       python3-dbus-python = %{version}-%{release}
Provides:       python3-dbus-python%{?_isa} = %{version}-%{release}
%python_provide python3-dbus-python

%description
D-Bus python bindings for use with python programs.
This is a metapackage that requires the main Python 3 package.

%package        devel
Summary:        Libraries and headers for dbus-python

%description    devel
This package contains the header files and static libraries needed for
hooking up custom mainloops to the D-Bus Python bindings.

%prep -a
# Remove ninja and patchelf from build-system.requires in pyproject.toml
# They are provided by system packages, not Python distributions
sed -i -e "/^ *'ninja'/d" -e "/^ *'patchelf'/d" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -p

%conf -a
%meson

%build -a
%meson_build

%install -a
%meson_install
# Remove duplicate header/pkgconfig installed by pyproject into site-packages
find %{buildroot}%{python3_sitearch} -name dbus-python.h -delete
find %{buildroot}%{python3_sitearch} -name dbus-python.pc -delete
find %{buildroot}%{python3_sitearch} -name '.dbus_python.mesonpy.libs' -type d -exec rm -rf {} +
# Remove duplicate header installed by pyproject under python include dir
find %{buildroot}%{_prefix}/include -path '*/dbus_python/*' -delete
find %{buildroot}%{_prefix}/include -name 'dbus_python' -type d -exec rm -rf {} +

%files -f %{pyproject_files}
%doc NEWS
%license COPYING
%{python3_sitearch}/*.so

%files devel
%doc README ChangeLog doc/API_CHANGES.txt doc/tutorial.txt
%{_includedir}/dbus-1.0/dbus/dbus-python.h
%{_libdir}/pkgconfig/dbus-python.pc

%changelog
%autochangelog
