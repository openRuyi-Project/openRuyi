# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sagemaker-core
%global pypi_name sagemaker_core

Name:           python-%{srcname}
Version:        2.8.0
Release:        %autorelease
Summary:        A library for training and deploying machine learning models on Amazon SageMaker
License:        Apache-2.0
URL:            https://sagemaker.readthedocs.io/en/stable/
VCS:            git:https://github.com/aws/sagemaker-python-sdk.git
#!RemoteAsset:  sha256:7f695da4538c9548fb42ad51f27db0039cd65f21b97c90075904f0257df4f265
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l sagemaker

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The SDK designed to provide an object-oriented
interface for interacting with Amazon SageMaker resources.
It offers full parity with SageMaker APIs, allowing developers
to leverage all SageMaker capabilities directly through the SDK.
sagemaker-core introduces features such as dedicated resource classes,
resource chaining, auto code completion, comprehensive documentation and
type hints to enhance the developer experience as well as productivity.

%prep -a
sed -i 's/importlib-metadata<7.0,>=1.4.0/importlib-metadata>=1.4.0/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
