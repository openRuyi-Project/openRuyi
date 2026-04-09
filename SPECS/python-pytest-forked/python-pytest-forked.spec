# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-forked

Name:           python-%{srcname}
Version:        1.6.0
Release:        %autorelease
Summary:        py.test plugin for running tests in isolated forked subprocesses
License:        MIT
URL:            https://github.com/pytest-dev/pytest-forked
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install): pytest_forked

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
The pytest-forked plugin extends py.test by adding an option to run tests in
isolated forked subprocesses. This is useful if you have tests involving C or
C++ libraries that might crash the process. To use the plugin, simply use the
--forked argument when invoking py.test.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc example/boxed.txt README.rst
%license LICENSE

%changelog
%autochangelog
