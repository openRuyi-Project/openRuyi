# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ipython_pygments_lexers

Name:           python-ipython-pygments-lexers
Version:        1.1.1
Release:        %autorelease
Summary:        Defines a variety of Pygments lexers for highlighting IPython code.
License:        BSD-3-Clause
URL:            https://github.com/ipython/ipython-pygments-lexers
#!RemoteAsset:  sha256:09c0138009e56b6854f9535736f4171d855c8c08a563a0dcd8022f78355c7e81
Source0:        https://files.pythonhosted.org/packages/source/i/ipython-pygments-lexers/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(parso)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
A Pygments plugin for IPython code & console sessions.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%{?autochangelog}
