# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname unidic

Name:           python-%{srcname}
Version:        1.1.0
Release:        %autorelease
Summary:        UniDic packaged for Python
License:        MIT
URL:            https://github.com/polm/unidic-py
#!RemoteAsset:  sha256:0ab91c05de342c84d2a6314901fd3afb9061ecd7534dd4a0431dccbb87d921b7
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This is a version of UniDic packaged for use
with pip.

%prep -a
sed -i 's/wasabi>=0\.6\.0,<1\.0\.0/wasabi>=0.6.0/g' setup.cfg
sed -i 's/wasabi<1\.0\.0,>=0\.6\.0/wasabi>=0.6.0/g' unidic.egg-info/requires.txt

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog
