# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sagemaker-serve
%global pypi_name sagemaker_serve

Name:           python-%{srcname}
Version:        1.26.0
Release:        %autorelease
Summary:        Amazon SageMaker Python SDK for SageMaker Server
License:        Apache-2.0
URL:            https://sagemaker.readthedocs.io/en/stable/
VCS:            git:https://github.com/aws/sagemaker-python-sdk.git
#!RemoteAsset:  sha256:a4140f101420a21bf8826b02c10cc8f5fb4ee4e3adb44491e5dbfe9c42033303
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l sagemaker
# Inference entry points require deployed models or Triton's backend runtime.
BuildOption(check):  -e sagemaker.serve.model_server.multi_model_server.inference
BuildOption(check):  -e sagemaker.serve.model_server.smd.custom_execution_inference
BuildOption(check):  -e sagemaker.serve.model_server.tensorflow_serving.inference
BuildOption(check):  -e sagemaker.serve.model_server.torchserve.inference
BuildOption(check):  -e sagemaker.serve.model_server.torchserve.xgboost_inference
BuildOption(check):  -e sagemaker.serve.model_server.triton.model
# This maintenance script reads image configuration relative to its working directory.
BuildOption(check):  -e sagemaker.serve.validations.parse_registry_accounts

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(docker)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       python3dist(docker)

%description
Amazon SageMaker Python SDK for SageMaker Server.

%prep -a
sed -i '/mlflow/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%install -a
rm -f %{buildroot}%{python3_sitelib}/sagemaker/__init__.py
rm -f %{buildroot}%{python3_sitelib}/sagemaker/__pycache__/__init__.*
sed -i '\|/sagemaker/__init__.py|d' %{pyproject_files}
sed -i '\|/sagemaker/__pycache__/__init__|d' %{pyproject_files}

# SDK initialization needs a region; instance metadata is unavailable during builds.
%check -p
export AWS_DEFAULT_REGION=us-east-1
export AWS_EC2_METADATA_DISABLED=true

%check -a
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -c 'from sagemaker.serve import ModelBuilder'

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
