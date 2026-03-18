# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname multiprocess

Name:           python-%{srcname}
Version:        0.70.19
Release:        %autorelease
Summary:        Better multiprocessing and multithreading in Python
License:        BSD-3-Clause
URL:            https://github.com/uqfoundation/multiprocess
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  multiprocess

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(dill)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
multiprocess is a fork of multiprocessing that uses dill instead of pickle,
enabling the transfer of more complex objects between processes.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%{?autochangelog}
