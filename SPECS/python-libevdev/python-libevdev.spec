# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname libevdev

Name:           python-%{srcname}
Version:        0.13.1
Release:        %autorelease
Summary:        Python bindings to the libevdev evdev device wrapper library
License:        MIT
URL:            https://gitlab.freedesktop.org/libevdev/python-libevdev
#!RemoteAsset
Source:         https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-hatchling
BuildRequires:  pkgconfig(libevdev)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
%{name} provides the Python bindings to the libevdev evdev device
wrapper library. These bindings provide a pythonic API to access evdev
devices and create uinput devices.

%generate_buildrequires
%pyproject_buildrequires

%check
%pytest -v

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
