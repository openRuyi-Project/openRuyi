# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname python-dateutil

Name:           python-%{srcname}
Version:        2.9.0.post0
Release:        %autorelease
Summary:        Powerful extensions to the standard datetime module
License:        (Apache-2.0 AND BSD-3-Clause) OR BSD-3-Clause
URL:            https://github.com/dateutil/dateutil
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset:  sha256:37dd54208da7e1cd875388217d5e00ebd4179249f90fb72437e91a35459a0ad3
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l dateutil
# ImportError: cannot import name 'winreg' from 'six.moves' (unknown location)
BuildOption(check):  -e dateutil.tz.win
BuildOption(check):  -e dateutil.tzwin

# Otherwise will nothing provides python3dist(setuptools-scm) < 8~~
Patch0:         0001-relax-setuptools_scm-requires.patch
# Fix sphinx import path
Patch1:         0002-fix-sphinx-import.patch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       tzdata

%description
The dateutil module provides powerful extensions to the standard datetime
module available in Python.

%prep -a
# Convert NEWS file to UTF-8
iconv --from=ISO-8859-1 --to=UTF-8 NEWS > NEWS.new
mv NEWS.new NEWS

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc NEWS README.rst
#doc docs/_build/html
%license LICENSE

%changelog
%autochangelog
