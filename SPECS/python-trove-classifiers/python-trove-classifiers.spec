# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname trove_classifiers

Name:           python-trove-classifiers
Version:        2025.8.26.11
Release:        %autorelease
Summary:        Canonical source for classifiers on PyPI (pypi.org)
License:        Apache-2.0
URL:            https://github.com/pypa/trove-classifiers
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset:  sha256:e73efff317c492a7990092f9c12676c705bf6cfe40a258a93f63f4b4c9941432
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Drop dependency on calver which is not packaged
# This patch is rebased version of upstream PR:
# https://github.com/pypa/trove-classifiers/pull/126/commits/809156bb35852bcaa1c753e0165f1814f2bcedf6
Patch0:          0001-Move-to-PEP-621-declarative-metadata.patch

BuildOption(install):  trove_classifiers

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-trove-classifiers = %{version}-%{release}
%python_provide python3-trove-classifiers

%description
Canonical source for classifiers on PyPI.
Classifiers categorize projects per PEP 301. Use this package to validate
classifiers in packages for PyPI upload or download.

%prep -a
# Replace @@VERSION@@ with %%version
sed -i 's/@@VERSION@@/%{version}/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.*
%{_bindir}/trove-classifiers

%changelog
%autochangelog
