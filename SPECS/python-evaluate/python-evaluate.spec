# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname evaluate

Name:           python-%{srcname}
Version:        0.4.6
Release:        %autorelease
Summary:        Library for evaluating machine learning models and datasets
License:        Apache-2.0
URL:            https://pypi.org/project/evaluate/
VCS:            git:https://github.com/huggingface/evaluate
#!RemoteAsset:  sha256:e07036ca12b3c24331f83ab787f21cc2dbf3631813a1631e63e40897c69a3f21
Source0:        https://files.pythonhosted.org/packages/source/e/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# Disable check imports huggingface_hub.Repository,matplotlib
BuildOption(check):  -e evaluate.commands.evaluate_cli
BuildOption(check):  -e evaluate.visualization

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(datasets) >= 2.0.0
BuildRequires:  python3dist(dill)
BuildRequires:  python3dist(fsspec) >= 2021.05.0
BuildRequires:  python3dist(fsspec[http]) >= 2021.05.0
BuildRequires:  python3dist(huggingface-hub) >= 0.7.0
BuildRequires:  python3dist(multiprocess)
BuildRequires:  python3dist(numpy) >= 1.17
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyarrow)
BuildRequires:  python3dist(requests) >= 2.19.0
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tqdm) >= 4.62.1
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(xxhash)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       python3dist(pyarrow)
Requires:       python3dist(typing-extensions)

%description
Evaluate provides tools to load, compute, and compare evaluation modules for
machine learning models and datasets, including metrics, comparisons, and
measurements shared through the Hugging Face Hub.

%generate_buildrequires
%pyproject_buildrequires

%install -a
# evaluate-cli targets still imports huggingface_hub.Repository API
rm -f %{buildroot}%{_bindir}/evaluate-cli

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
