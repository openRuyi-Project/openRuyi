# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ftfy

Name:           python-%{srcname}
Version:        6.3.1
Release:        %autorelease
Summary:        Fixes mojibake and other glitches in Unicode text, after the fact
License:        Apache-2.0
URL:            https://github.com/rspeer/python-ftfy
#!RemoteAsset:  sha256:9b3c3d90f84fb267fe64d375a07b7f8912d817cf86009ae134aa03e1819506ec
Source:         https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(wcwidth)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
ftfy fixes mojibake and other glitches in Unicode text, after the fact.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{_bindir}/ftfy

%changelog
%autochangelog
