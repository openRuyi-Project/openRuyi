# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname email-validator
%global pypi_name email_validator

Name:           python-%{srcname}
Version:        2.3.0
Release:        %autorelease
Summary:        Robust email address syntax and deliverability validation library
License:        Unlicense
URL:            https://github.com/JoshData/python-email-validator
VCS:            git:https://github.com/JoshData/python-email-validator.git
#!RemoteAsset:  sha256:9fc05c37f2f6cf439ff414f8fc46d917929974a82244c20eb10231ba60c54426
Source0:        https://files.pythonhosted.org/packages/source/e/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}
BuildOption(check):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(dnspython) >= 2
BuildRequires:  python3dist(idna) >= 2
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
email-validator validates email address syntax and optionally checks domain
deliverability using DNS. It supports internationalized domain names and
normalized address output.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/email_validator

%changelog
%autochangelog
