# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sagemaker-mlops
%global pypi_name sagemaker_mlops

Name:           python-%{srcname}
Version:        1.26.0
Release:        %autorelease
Summary:        A library for MLOps on Amazon SageMaker
License:        Apache-2.0
URL:            https://sagemaker.readthedocs.io/en/stable/
VCS:            git:https://github.com/aws/sagemaker-python-sdk.git
#!RemoteAsset:  sha256:045a26a0873a3f124d6d7479c893f91ffa75ad5d2df173056a78931596197c53
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l sagemaker
# Feature Processor imports require the optional feature-processor PySpark extra.
BuildOption(check):  -e 'sagemaker.mlops.feature_store.feature_processor*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The sagemaker-mlops package provides high-level orchestration
capabilities for Amazon SageMaker workflows, including pipeline
definitions, step implementations, and model building utilities.

%install -a
rm -f %{buildroot}%{python3_sitelib}/sagemaker/__init__.py
rm -f %{buildroot}%{python3_sitelib}/sagemaker/__pycache__/__init__.*
sed -i '\|/sagemaker/__init__.py|d' %{pyproject_files}
sed -i '\|/sagemaker/__pycache__/__init__|d' %{pyproject_files}

%generate_buildrequires
%pyproject_buildrequires

# SDK initialization needs a region; instance metadata is unavailable during builds.
%check -p
export AWS_DEFAULT_REGION=us-east-1
export AWS_EC2_METADATA_DISABLED=true

%check -a
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -c 'from sagemaker.mlops.workflow.pipeline import Pipeline'

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
