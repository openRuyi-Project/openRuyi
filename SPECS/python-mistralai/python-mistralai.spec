# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mistralai

Name:           python-%{srcname}
Version:        2.4.2
Release:        %autorelease
Summary:        Python Client SDK for the Mistral AI API
License:        Apache-2.0
URL:            https://github.com/mistralai/client-python
#!RemoteAsset:  sha256:7896ffa763e0be1ec05e5b436d2c21ae089e4b5438cda9033dcd1b25bc3021a2
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Backport to relax opentelemetry semantic conventions upper bound
Patch2000:      2000-relax-opentelemetry-semantic-conventions-upper-bound.patch

BuildOption(install):  mistralai
# Exclude _s3 storage backend: aioboto3 pins aiobotocore==2.25.1 which
# requires botocore<1.40.62, incompatible with main (1.42.89)
BuildOption(check):  -e 'mistralai.extra.workflows.encoding.storage._s3'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(authlib)
BuildRequires:  python3dist(azure-storage-blob)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(eval-type-backport)
BuildRequires:  python3dist(gcloud-aio-storage)
BuildRequires:  python3dist(google-auth)
BuildRequires:  python3dist(griffe)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(jsonpath-python)
BuildRequires:  python3dist(mcp)
BuildRequires:  python3dist(opentelemetry-api)
BuildRequires:  python3dist(opentelemetry-sdk)
BuildRequires:  python3dist(opentelemetry-semantic-conventions)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(pydantic-core)
BuildRequires:  python3dist(pydantic-settings)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(typing-inspection)
BuildRequires:  python3dist(websockets)
BuildRequires:  python3dist(hatchling)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The official Python client SDK for the Mistral AI API, providing access to
Mistral's language models for chat, embeddings, and other AI capabilities.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
