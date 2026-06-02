# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname bokeh-sampledata
%global pypi_name bokeh_sampledata

Name:           python-%{srcname}
Version:        2025.0
Release:        %autorelease
Summary:        Sample datasets for Bokeh examples
License:        BSD-3-Clause
URL:            https://github.com/bokeh/bokeh_sampledata
#!RemoteAsset:  sha256:6b874af5b878e70f16133695ac07e15de38642fa9fadfdf723f7d42333967af4
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(icalendar)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
Requires:       python3dist(pandas)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Sample datasets for Bokeh examples.

%prep -a
sed -i 's/^dynamic = \["version"\]/version = "%{version}"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
