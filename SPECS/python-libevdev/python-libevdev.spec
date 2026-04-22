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
#!RemoteAsset:  sha256:dc3369cd1401767b9ecb1117cd6b73faba9038e3bd9e1695a710a9e9d9415e8d
Source:         https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hatchling)
BuildRequires:  pkgconfig(libevdev)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
%{name} provides the Python bindings to the libevdev evdev device
wrapper library. These bindings provide a pythonic API to access evdev
devices and create uinput devices.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest -v

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
