# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pydbus

Name:           python-%{srcname}
Version:        0.6.0
Release:        %autorelease
Summary:        Pythonic DBus library
License:        LGPL-2.0-or-later
URL:            https://github.com/LEW21/pydbus
#!RemoteAsset:  sha256:4207162eff54223822c185da06c1ba8a34137a9602f3da5a528eedf3f78d0f2c
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The pydbus module provides pythonic DBUS bindings.
It is based on PyGI, the Python GObject Introspection bindings,
which is the recommended way to use GLib from Python.

%generate_buildrequires
%pyproject_buildrequires

# No module named 'gi'
%check

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
