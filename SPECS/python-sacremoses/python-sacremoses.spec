# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sacremoses

Name:           python-%{srcname}
Version:        0.1.1
Release:        %autorelease
Summary:        Python port of Moses tokenizer, truecaser and normalizer
License:        MIT
URL:            https://github.com/hplt-project/sacremoses
#!RemoteAsset:  sha256:b6fd5d3a766b02154ed80b962ddca91e1fd25629c0978c7efba21ebccf663934
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# Not Implemented
BuildOption(check):  -e sacremoses.sent_tokenize

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python port of Moses tokenizer, truecaser and normalizer.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/sacremoses

%changelog
%autochangelog
