# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname datasets

Name:           python-datasets
Version:        4.8.5
Release:        %autorelease
Summary:        Library for accessing and sharing machine learning datasets
License:        MIT
URL:            https://pypi.org/project/datasets/
VCS:            git:https://github.com/huggingface/datasets
#!RemoteAsset:  sha256:0f0c1c3d56ffff2c93b2f4c63c95bac94f3d7e8621aea2a2a576275233bba772
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# NOTE: When updating datasets, please check this URL:
# https://github.com/huggingface/datasets/issues/7326
Patch2000:      2000-Relax-fsspec-version-requirements.patch

BuildOption(install):  -l %{srcname} +auto
BuildOption(check):  -e datasets.io.spark -e 'datasets.packaged_modules.spark*'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(dill) >= 0.3
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(fsspec) >= 2023.1.0
BuildRequires:  python3dist(fsspec[http]) >= 2023.1.0
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(huggingface-hub) >= 0.25
BuildRequires:  python3dist(multiprocess)
BuildRequires:  python3dist(numpy) >= 1.17
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pyarrow) >= 21
BuildRequires:  python3dist(pyyaml) >= 5.1
BuildRequires:  python3dist(requests) >= 2.32.2
BuildRequires:  python3dist(tqdm) >= 4.66.3
BuildRequires:  python3dist(xxhash)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Datasets is a library for easily accessing and sharing datasets for machine
learning, with efficient processing and support for common benchmark tasks.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
