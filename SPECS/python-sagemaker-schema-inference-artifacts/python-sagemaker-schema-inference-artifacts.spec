# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sagemaker-schema-inference-artifacts
%global pypi_name sagemaker_schema_inference_artifacts

Name:           python-%{srcname}
Version:        0.0.4
Release:        %autorelease
Summary:        SageMaker Schema Inference Artifacts is an open source library
License:        Apache-2.0
URL:            https://pypi.org/project/sagemaker-schema-inference-artifacts/
#!RemoteAsset:  sha256:af0de2f64449a4a41eba59ae09ec77534d6694dab921dbd17d9db0913ccba466
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
SageMaker Schema Inference Artifacts is an open source library.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
