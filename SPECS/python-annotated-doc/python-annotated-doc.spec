# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname annotated-doc
%global pkgname annotated_doc

Name:           python-%{srcname}
Version:        0.0.4
Release:        %autorelease
Summary:        Document parameters, class attributes, return types, and variables inline, with Annotated
License:        MIT
URL:            https://github.com/fastapi/annotated-doc
#!RemoteAsset:  sha256:fbcda96e87e9c92ad167c2e53839e57503ecfda18804ea28102353485033faa4
Source0:        https://files.pythonhosted.org/packages/source/a/annotated-doc/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install):  -l %{pkgname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Document parameters, class attributes, return types, and variables inline, with Annotated.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{pkgname}-%{version}

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
