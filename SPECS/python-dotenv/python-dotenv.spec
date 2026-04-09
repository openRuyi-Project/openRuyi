# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname python-dotenv

Name:           python-dotenv
Version:        1.1.1
Release:        %autorelease
License:        BSD-3-Clause
URL:            https://saurabh-kumar.com/python-dotenv/
Summary:        Setup environment variables according to .env files
Provides:       python3-dotenv
%python_provide python3-dotenv
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/python_dotenv-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildSystem:    pyproject
BuildOption(install): -l dotenv +auto
%description
This package provides the @code{python-dotenv} Python module to read
key-value pairs from a @code{.env} file and set them as environment variables.


%prep -a
sed -i -e '/ipython/d' requirements.txt tox.ini

%generate_buildrequires
%pyproject_buildrequires


%check


%pyproject_extras_subpkg -n python%{python3_pkgversion}-dotenv cli
%{_bindir}/dotenv

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
