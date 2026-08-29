# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname flask-restful
%global pypi_name Flask-RESTful

Name:           python-%{srcname}
Version:        0.3.10
Release:        %autorelease
Summary:        Simple framework for creating REST APIs
License:        BSD-3-Clause
URL:            https://github.com/flask-restful/flask-restful
#!RemoteAsset:  sha256:fe4af2ef0027df8f9b4f797aba20c5566801b6ade995ac63b588abf1a59cec37
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  flask_restful

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
# Tests
BuildRequires:  python3dist(pycryptodome)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Flask-RESTful provides the building blocks for creating a REST API.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
