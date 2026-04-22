# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname marshmallow

Name:           python-%{srcname}
Version:        4.2.1
Release:        %autorelease
Summary:        A lightweight library for converting complex objects to and from simple Python datatypes
License:        MIT
URL:            https://marshmallow.readthedocs.io/
VCS:            git:https://github.com/marshmallow-code/marshmallow/
#!RemoteAsset:  sha256:4d1d66189c8d279ca73a6b0599d74117e5f8a3830b5cd766b75c2bb08e3464e7
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(flit-core)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(ordered-set)
BuildRequires:  python3dist(simplejson)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Marshmallow is a framework-agnostic library for converting complex datatypes,
such as objects, to and from primitive Python datatypes.

Marshmallow schemas can be used to:
* Validate input data.
* Deserialize input data to app-level objects.
* Serialize app-level objects to primitive Python types.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.rst README.rst

%changelog
%autochangelog
