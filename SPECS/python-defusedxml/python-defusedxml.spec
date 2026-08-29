# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname defusedxml

Name:           python-%{srcname}
Version:        0.7.1
Release:        %autorelease
Summary:        XML bomb protection for Python standard library modules
License:        PSF-2.0
URL:            https://github.com/tiran/defusedxml
#!RemoteAsset:  sha256:1bb3032db185915b62d7c6209c5a8792be6a32ab2fedacc84e01b52c51aa3e69
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l defusedxml

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
defusedxml provides safer replacements for Python standard library XML
parsers that protect applications from common XML attacks.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.txt
%license LICENSE

%changelog
%autochangelog
