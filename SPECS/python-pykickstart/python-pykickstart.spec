# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pykickstart

Name:           python-%{srcname}
Version:        3.69
Release:        %autorelease
Summary:        Python module for manipulating kickstart files
License:        GPL-2.0-only
URL:            http://fedoraproject.org/wiki/pykickstart
VCS:            git:https://github.com/pykickstart/pykickstart.git
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  PYTHON=%{__python3}
BuildOption(install):  PYTHON=%{__python3} DESTDIR=%{buildroot}

BuildRequires:  make
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(pytest-cov)

Provides:       python3-%{srcname}
Provides:       python3-%{srcname}%{?_isa}
%python_provide python3-%{srcname}

%description
Python utilities for manipulating kickstart files.

# No configure
%conf

%install -a
# TODO: Avoid illegal package names
rm -rf %{buildroot}%{python3_sitelib}/pykickstart/locale/*@*
rm -rf %{buildroot}%{python3_sitelib}/pykickstart/locale/en_GB/
%find_lang %{srcname} --generate-subpackages

# TODO: Currently our python don't provide readline module
# and this is a mistake
%check
make PYTHON=%{__python3} test-no-coverage ||:

%files
%license COPYING
%doc README.rst
%doc data/kickstart.vim
%doc docs/2to3
%doc docs/programmers-guide
%doc docs/kickstart-docs.txt
%{_bindir}/ksvalidator
%{_bindir}/ksflatten
%{_bindir}/ksverdiff
%{_bindir}/ksshell
%{_mandir}/man1/ksflatten.1.gz
%{_mandir}/man1/ksshell.1.gz
%{_mandir}/man1/ksvalidator.1.gz
%{_mandir}/man1/ksverdiff.1.gz
%{python3_sitelib}/pykickstart
%{python3_sitelib}/pykickstart-%{version}.dist-info

%changelog
%{?autochangelog}
