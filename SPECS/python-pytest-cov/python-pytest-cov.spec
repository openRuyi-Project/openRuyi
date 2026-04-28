# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-cov
%global pypi_name pytest_cov

Name:           python-%{srcname}
Version:        7.0.0
Release:        %autorelease
Summary:        Pytest plugin for measuring coverage.
License:        GPL-2.0-only
URL:            https://github.com/pytest-dev/pytest-cov
#!RemoteAsset:  sha256:33c97eda2e049a0c5298e91f519302a1334c26ac65c1a483d6206fd458361af1
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
This plugin produces coverage reports. Compared to just using coverage run this
plugin does some extras:

  • Subprocess support: you can fork or run stuff in a subprocess and will get
    covered without any fuss.
  • Xdist support: you can use all of pytest-xdist’s features and still get
    coverage.
  • Consistent pytest behavior. If you run coverage run -m pytest you will have
    slightly different sys.path (CWD will be in it, unlike when running
    pytest).

All features offered by the coverage package should work, either through
pytest-cov’s command line options or through coverage’s config file.

# Disable tests
%generate_buildrequires
%pyproject_buildrequires -r -x testing

%check

%files -f %{pyproject_files}
%license LICENSE
%doc *.rst

%changelog
%autochangelog
