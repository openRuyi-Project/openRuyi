# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname moto

Name:           python-%{srcname}
Version:        5.2.1
Release:        %autorelease
Summary:        A library that allows you to easily mock out tests based on AWS infrastructure
License:        Apache-2.0
URL:            https://github.com/getmoto/moto
#!RemoteAsset:  sha256:ccb2f3e1dfa82e50e054bda98b0be708d244d2668364dcc1d45e8d3de6091bde
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# No module named 'openapi_spec_validator'
BuildOption(check):  -e 'moto.apigateway*'
BuildOption(check):  -e 'moto.cloudformation*'
# No module named 'localstack'
BuildOption(check):  -e 'moto.firehose*'
BuildOption(check):  -e 'moto.stepfunctions.parser*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(antlr4-python3-runtime)
BuildRequires:  python3dist(aws-xray-sdk)
BuildRequires:  python3dist(boto3)
BuildRequires:  python3dist(botocore)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(flask-cors)
BuildRequires:  python3dist(joserfc)
BuildRequires:  python3dist(jsonpath-ng)
BuildRequires:  python3dist(python-multipart)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyparsing)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(responses)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(werkzeug)
BuildRequires:  python3dist(xmltodict)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Moto is a library that allows you to easily mock out tests based on
AWS infrastructure.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/moto_proxy
%{_bindir}/moto_server

%changelog
%autochangelog
