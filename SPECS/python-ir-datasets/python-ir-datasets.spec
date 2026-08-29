# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ir-datasets
%global pypi_name ir_datasets

Name:           python-%{srcname}
Version:        0.5.11
Release:        %autorelease
Summary:        Common interface to IR ranking datasets
License:        MIT
URL:            https://github.com/allenai/ir_datasets
#!RemoteAsset:  sha256:06c90af634ae5063c813286b35065debca1a974d26e136403d899f3ecd7ad463
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} examples test -L
# examples.* need external data files not available at build time.
BuildOption(check):  -e 'examples.*'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(inscriptis)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(trec-car-tools)
BuildRequires:  python3dist(lz4)
BuildRequires:  python3dist(warc3-wet)
BuildRequires:  python3dist(warc3-wet-clueweb09)
BuildRequires:  python3dist(zlib-state)
BuildRequires:  python3dist(ijson)
BuildRequires:  python3dist(unlzw3)
BuildRequires:  python3dist(pyarrow)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
ir-datasets provides a common Python interface to many information retrieval
ranking benchmarks and training datasets.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/ir_datasets

%changelog
%autochangelog
