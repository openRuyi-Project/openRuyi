# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ocifs

Name:           python-%{srcname}
Version:        1.3.4
Release:        %autorelease
Summary:        Fsspec interface for Oracle Cloud Object Storage
License:        UPL-1.0
URL:            https://github.com/oracle/ocifs
#!RemoteAsset:  sha256:52658665366210924eca61716ad3fce3c3cdf772c0e95d47fd378db7f969c6f4
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto
BuildOption(check):    -e %{srcname}.tests -e '%{srcname}.tests.*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(flit-core) >= 3.8
BuildRequires:  python3dist(fsspec) >= 0.8.7
BuildRequires:  python3dist(oci) > 2.43.1
BuildRequires:  python3dist(requests)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Ocifs provides an fsspec-compatible filesystem for Oracle Cloud
Infrastructure Object Storage.

%generate_buildrequires
%pyproject_buildrequires

%install -a
# The upstream wheel includes its integration tests in the runtime package.
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/tests
sed -i '\#/%{srcname}/tests#d' %{pyproject_files}

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
