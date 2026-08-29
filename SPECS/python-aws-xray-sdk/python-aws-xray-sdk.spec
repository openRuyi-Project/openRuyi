# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aws-xray-sdk
%global pypi_name aws_xray_sdk

Name:           python-%{srcname}
Version:        2.15.0
Release:        %autorelease
Summary:        AWS X-Ray SDK for Python
License:        Apache-2.0
URL:            https://github.com/aws/aws-xray-sdk-python
#!RemoteAsset:  sha256:794381b96e835314345068ae1dd3b9120bd8b4e21295066c37e8814dbb341365
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}
# No module named 'bson'
BuildOption(check):  -e 'aws_xray_sdk.ext.pymongo'
BuildOption(check):  -e 'aws_xray_sdk.ext.pymongo.patch'
# No module named 'flask_sqlalchemy'
# incompatible with openRuyi's flask 3.x
BuildOption(check):  -e 'aws_xray_sdk.ext.flask_sqlalchemy.query'
# No module named 'mysql.connector'
# mysql-connector-python uses non-standard cpydist build system
BuildOption(check):  -e 'aws_xray_sdk.ext.mysql'
BuildOption(check):  -e 'aws_xray_sdk.ext.mysql.patch'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(aiobotocore)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(botocore)
BuildRequires:  python3dist(bottle)
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pg8000)
BuildRequires:  python3dist(pymongo)
BuildRequires:  python3dist(pymysql)
BuildRequires:  python3dist(pynamodb)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(wrapt)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The AWS X-Ray SDK for Python (the SDK) enables Python developers to record
and emit information from within their applications to the AWS X-Ray service.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
