# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname flask-restful

Name:           python-%{srcname}
Version:        0.3.10
Release:        %autorelease
Summary:        Simple framework for creating REST APIs
License:        BSD-3-Clause
URL:            https://github.com/flask-restful/flask-restful
# This is messed up upstream... - 251
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/Flask-RESTful-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  flask_restful

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
# Tests
BuildRequires:  python3dist(pycryptodome)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Flask-RESTful provides the building blocks for creating a REST API.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%{?autochangelog}
