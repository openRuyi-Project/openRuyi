# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nodeenv

Name:           python-%{srcname}
Version:        1.10.0
Release:        %autorelease
Summary:        Node.js virtual environment builder
License:        BSD-3-Clause
URL:            https://github.com/ekalinin/nodeenv
#!RemoteAsset:  sha256:996c191ad80897d076bdfba80a41994c2b47c68e224c542b48feba42ba00f8bb
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Node.js virtual environment builder.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%doc README.ru.rst
%doc CHANGES
%license LICENSE
%{_bindir}/nodeenv

%changelog
%autochangelog
