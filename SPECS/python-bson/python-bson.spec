# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname bson

Name:           python-%{srcname}
Version:        0.5.10
Release:        %autorelease
Summary:        BSON codec for Python
License:        BSD-3-Clause AND Apache-2.0
URL:            http://github.com/py-bson/bson
#!RemoteAsset:  sha256:d6511b2ab051139a9123c184de1a04227262173ad593429d21e443d6462d6590
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:7f99199909304c0a94ac1d758ad4d19f7cee8285c8f1d0c7a81c7fdffa6950eb
Source1:        https://raw.githubusercontent.com/py-bson/bson/refs/tags/0.5.8/LICENSE
#!RemoteAsset:  sha256:c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4
Source2:        https://raw.githubusercontent.com/py-bson/bson/refs/tags/0.5.8/LICENSE_APACHE
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Independent BSON codec for Python that doesn't depend on MongoDB.

%prep -a
cp %{SOURCE1} LICENSE
cp %{SOURCE2} LICENSE_APACHE

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE LICENSE_APACHE

%changelog
%autochangelog
