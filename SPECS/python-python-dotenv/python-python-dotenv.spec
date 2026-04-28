# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname python-dotenv

Name:           python-python-dotenv
Version:        1.1.1
Release:        %autorelease
License:        BSD-3-Clause
URL:            https://saurabh-kumar.com/python-dotenv/
Summary:        Setup environment variables according to .env files
#!RemoteAsset:  sha256:a8a6399716257f45be6a007360200409fce5cda2661e3dec71d23dc15f6189ab
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/python_dotenv-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l dotenv +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
This package provides the @code{python-dotenv} Python module to read
key-value pairs from a @code{.env} file and set them as environment variables.

%pyproject_extras_subpkg -n python%{python3_pkgversion}-dotenv cli

%prep -a
sed -i -e '/ipython/d' requirements.txt tox.ini

%generate_buildrequires
%pyproject_buildrequires

# No check
%check

%files -f %{pyproject_files}
%doc README*
%{_bindir}/dotenv

%changelog
%autochangelog
