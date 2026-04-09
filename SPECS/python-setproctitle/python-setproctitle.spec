# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname setproctitle

Name:           python-%{srcname}
Version:        1.1.10
Release:        %autorelease
Summary:        Python module to customize a process title
License:        BSD-3-Clause
URL:            http://pypi.python.org/pypi/setproctitle
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Python module allowing a process to change its title as displayed by
system tool such as ps and top.
It's useful in multiprocess systems, allowing to identify tasks each forked
process is busy with. This technique has been used by PostgreSQL and OpenSSH.
It's based on PostgreSQL implementation which has proven to be portable.

%generate_buildrequires
%pyproject_buildrequires

%build -p
export CFLAGS="%{optflags} -std=gnu89"

%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
# This test script is too old (it also has Python 2 syntax).
# As long as the import is successful, it means that the C
# extension module is compiled without errors.
%{__python3} -c "import setproctitle; setproctitle.setproctitle('test-title'); print('Import and basic call: OK')"

%files
%doc README.rst COPYRIGHT
# For arch-specific packages: sitearch
%{python3_sitearch}/%{srcname}*.so
%{python3_sitearch}/%{srcname}*.dist-info

%changelog
%autochangelog
