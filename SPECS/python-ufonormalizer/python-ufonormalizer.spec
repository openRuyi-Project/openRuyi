# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ufonormalizer

Name:           python-%{srcname}
Version:        0.6.3
Release:        %autorelease
Summary:        Script to normalize the XML and other data inside of a UFO
License:        BSD-3-Clause
URL:            https://github.com/unified-font-object/ufoNormalizer
#!RemoteAsset:  sha256:c3271097aba9d290594b75c2b432cf681088b74fe3eb334ca4319324e2bddd4e
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Provides a standard formatting so that there are meaningful diffs in version control rather than formatting noise.

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Run the upstream UFO normalization fixtures against the installed Python module.
PYTHONPATH=%{buildroot}%{python3_sitelib} %{python3} -m unittest discover -s tests -p test_ufonormalizer.py

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/ufonormalizer

%changelog
%autochangelog
