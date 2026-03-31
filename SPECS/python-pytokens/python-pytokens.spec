# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: kenlig <qiming.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytokens

Name:           python-pytokens
Version:        0.4.1
Release:        %autorelease
Summary:        Fast spec-compliant Python tokenizer for older Python versions
License:        MIT
URL:            https://pypi.org/project/pytokens/
VCS:            git:https://github.com/tusharsadhwani/pytokens
#!RemoteAsset:  sha256:292052fe80923aae2260c073f822ceba21f3872ced9a68bb7953b348e561179a
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:	pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pytokens is a fast, spec-compliant Python tokenizer that backports newer
tokenizer behavior to older Python runtimes.

%generate_buildrequires -p
export PYTOKENS_USE_MYPYC=0

%build -p
export PYTOKENS_USE_MYPYC=0

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
