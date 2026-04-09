# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname iniconfig

Name:           python-%{srcname}
Version:        2.1.0
Release:        %autorelease
Summary:        Brain-dead simple parsing of ini files
License:        MIT
URL:            http://github.com/RonnyPfannschmidt/iniconfig
#!RemoteAsset
Source0:        %{url}/archive/v%{version}/iniconfig-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pluggy
BuildRequires:  python3-hatch-vcs
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-hatchling
BuildRequires:  python3-packaging
BuildRequires:  python3-pip
BuildRequires:  expat

%description
iniconfig is a small and simple INI-file parser module
having a unique set of features:

* tested against Python2.4 across to Python3.2, Jython, PyPy
* maintains order of sections and entries
* supports multi-line values with or without line-continuations
* supports "#" comments everywhere
* raises errors with proper line-numbers
* no bells and whistles like automatic substitutions
* iniconfig raises an Error if two sections have the same name.

%package     -n python3-iniconfig
Summary:        %{summary}

%description -n python3-iniconfig
iniconfig is a small and simple INI-file parser module
having a unique set of features:

* tested against Python2.4 across to Python3.2, Jython, PyPy
* maintains order of sections and entries
* supports multi-line values with or without line-continuations
* supports "#" comments everywhere
* raises errors with proper line-numbers
* no bells and whistles like automatic substitutions
* iniconfig raises an Error if two sections have the same name.

%prep
%autosetup -p1 -n iniconfig-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l iniconfig

%files -n python3-iniconfig -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
