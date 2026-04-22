# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname IPython

Name:           python-ipython
Version:        9.10.0
Release:        %autorelease
Summary:        An enhanced interactive Python shell
License:        BSD-3-Clause
URL:            https://ipython.org
#!RemoteAsset:  sha256:cd9e656be97618a0676d058134cd44e6dc7012c0e5cb36a9ce96a8c904adaf77
Source0:        https://files.pythonhosted.org/packages/source/i/ipython/ipython-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Skip import tests and some other modules that are not needed for the package
BuildOption(check):  -e "IPython.testing.*" -e "IPython.sphinxext.*" -e "IPython.external.*" -e "IPython.terminal.pt_inputhooks.*"
# These modules was moved to a separate package
BuildOption(check):  -e "IPython.utils.jsonutil" -e "IPython.utils.eventful"
BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(parso)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
IPython provides a rich toolkit to help you make the most out of using Python interactively.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/ipython
%{_bindir}/ipython3
%{_mandir}/man1/ipython.1.gz

%changelog
%autochangelog
