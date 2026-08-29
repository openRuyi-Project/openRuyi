# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname python-louvain

Name:           python-%{srcname}
Version:        0.16
Release:        %autorelease
Summary:        Louvain algorithm for community detection
License:        BSD-3-Clause
URL:            https://github.com/taynaud/python-louvain
#!RemoteAsset:  sha256:b7ba2df5002fd28d3ee789a49532baad11fe648e4f2117cf0798e7520a1da56b
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  community

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
python-louvain is a Python library for community detection using the
Louvain algorithm. It provides the 'community' module which implements
the Louvain method for identifying communities in large networks.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/community

%changelog
%autochangelog
