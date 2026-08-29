# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname matplotlib-inline
%global pypi_name matplotlib_inline

Name:           python-%{srcname}
Version:        0.2.2
Release:        %autorelease
Summary:        Inline Matplotlib backend for Jupyter
License:        BSD-3-Clause
URL:            https://github.com/ipython/matplotlib-inline
#!RemoteAsset:  sha256:72f3fe8fce36b70d4a5b612f899090cd0401deddc4ea90e1572b9f4bfb058c79
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(parso)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides support for matplotlib to
display figures directly inline in the Jupyter notebook
and related clients, as shown below.

%generate_buildrequires
%pyproject_buildrequires

# We don't have python-matplotlib
%check

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
