# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname id

Name:           python-%{srcname}
Version:        1.6.1
Release:        %autorelease
Summary:        Tool for generating OIDC identities
License:        Apache-2.0
URL:            https://github.com/di/id
VCS:            git:https://github.com/di/id.git
#!RemoteAsset:  sha256:d0732d624fb46fd4e7bc4e5152f00214450953b9e772c182c1c22964def1a069
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(flit-core)
BuildRequires:  python3dist(urllib3) >= 2

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
id provides a small client for requesting OpenID Connect identity tokens from
supported continuous integration and workload identity environments.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
