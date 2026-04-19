# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname model-hosting-container-standards
%global pypi_name model_hosting_container_standards

Name:           python-%{srcname}
Version:        0.1.14
Release:        %autorelease
Summary:        Python toolkit for standardized model hosting container implementations
License:        Apache-2.0
URL:            https://pypi.org/project/model-hosting-container-standards/
#!RemoteAsset:  sha256:b6cf4c46d88ce6acd6e543a578bb88ffd55d1179a7c09c22e61ae1d8a567c564
Source0: https://files.pythonhosted.org/packages/source/m/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install):  -L %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides: python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A standardized Python framework for seamless integration between ML frameworks
(TensorRT-LLM, vLLM) and Amazon SageMaker hosting. It simplifies model deployment
by providing a unified handler system, flexible configuration, and framework
agnostic compatibility.

%generate_buildrequires
%pyproject_buildrequires

echo "Apache-2.0" > LICENSE
%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/generate-supervisor-config
%{_bindir}/standard-supervisor

%changelog
%autochangelog
