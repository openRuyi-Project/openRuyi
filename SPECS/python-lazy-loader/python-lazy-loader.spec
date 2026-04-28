# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname lazy-loader
%global pypi_name lazy_loader

Name:           python-%{srcname}
Version:        0.5
Release:        %autorelease
Summary:        Populate library namespace without incurring immediate import costs
License:        BSD-3-Clause
URL:            https://github.com/scientific-python/lazy-loader
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install): %{pypi_name}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
lazy-loader makes it easy to load subpackages and functions on demand.

Motivation:
• Allow subpackages to be made visible to users without incurring import costs.
• Allow external libraries to be imported only when used, improving import
  times.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
