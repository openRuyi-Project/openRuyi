# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rawpy

Name:           python-%{srcname}
Version:        0.27.0
Release:        %autorelease
Summary:        RAW image processing for Python, a wrapper for libraw
License:        MIT
URL:            https://github.com/letmaik/rawpy
#!RemoteAsset:  sha256:45251e46c1d891a62919a4ac200a9828f825e3c59f89cea2f1daee0900ff15ec
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l rawpy
# skip tests: No module named 'skimage' (circular dependency)
BuildOption(check):  -e 'rawpy.enhance'

BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
rawpy is an easy-to-use Python wrapper for the LibRaw library. It
provides a simple interface to read and process RAW images.

%prep -a
# cmake is not python distributions
sed -i '/"cmake",/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build -p
export RAWPY_USE_SYSTEM_LIBRAW=1

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
