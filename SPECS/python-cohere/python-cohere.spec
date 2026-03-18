# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cohere

Name:           python-%{srcname}
Version:        5.20.7
Release:        %autorelease
Summary:        Python Library for Accessing the Cohere API
License:        MIT
URL:            https://github.com/cohere-ai/cohere-python
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/cohere-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(fastavro)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(pydantic-core)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(tokenizers)
BuildRequires:  python3dist(types-requests)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
The Cohere Python SDK allows access to Cohere models across many different
platforms: the cohere platform, AWS (Bedrock, Sagemaker), Azure, GCP and
Oracle OCI.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%{?autochangelog}
