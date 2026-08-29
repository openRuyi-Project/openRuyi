# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: kenlig <qiming.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hatch_nodejs_version

Name:           python-hatch-nodejs-version
Version:        0.4.0
Release:        %autorelease
Summary:        Hatch plugin for versioning and metadata from package.json
License:        MIT
URL:            https://github.com/jupyterlab/hatch-nodejs-version
#!RemoteAsset:  sha256:2428ea398dd053f019d2b7ac949dd6b690ca8e826b6d433ad13c5b6c475ae91b
Source:         https://github.com/jupyterlab/hatch-nodejs-version/releases/download/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
hatch-nodejs-version provides Hatch plugins that read Python packaging metadata
and versions from a Node.js package.json file. It includes both a version
source plugin and a metadata hook plugin for projects that bridge Python and
Node.js build metadata.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE.txt

%changelog
%autochangelog
