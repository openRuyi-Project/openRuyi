# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ipdb

Name:           python-%{srcname}
Version:        0.13.13
Release:        %autorelease
Summary:        IPython-enabled pdb
License:        BSD-3-Clause
URL:            https://github.com/gotcha/ipdb
#!RemoteAsset:  sha256:e3ac6018ef05126d442af680aad863006ec19d02290561ac88b8b1c0b0cfc726
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(parso)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(ipython)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
ipdb exports functions to access the IPython debugger,
which features tab completion, syntax highlighting, better tracebacks,
better introspection with the same interface as the pdb module.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license COPYING.txt
%{_bindir}/ipdb3

%changelog
%autochangelog
