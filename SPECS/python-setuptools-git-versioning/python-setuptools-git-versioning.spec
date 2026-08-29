# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname setuptools-git-versioning
%global pypi_name setuptools_git_versioning

Name:           python-%{srcname}
Version:        3.0.1
Release:        %autorelease
Summary:        Dynamic versioning based on git tags for setuptools
License:        MIT
URL:            https://github.com/setuptoolsuptools/setuptools-git-versioning
#!RemoteAsset:  sha256:c8a599bacf163b5d215552b5701faf5480ffc4d65426a5711a010b802e1590eb
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
setuptools-git-versioning is a setuptools plugin for dynamic versioning
based on git tags. It allows you to automatically set the version of your
Python package based on git tags, without having to manually update the
version in your code.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/setuptools-git-versioning

%changelog
%autochangelog
