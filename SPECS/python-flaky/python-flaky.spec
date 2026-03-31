# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname flaky

Name:           python-%{srcname}
Version:        3.8.1
Release:        %autorelease
Summary:        Plugin for pytest that automatically reruns flaky tests
License:        Apache-2.0
URL:            https://github.com/box/flaky
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
# Tests
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Flaky is a plugin for pytest that automatically reruns flaky
tests. Ideally, tests reliably pass or fail, but sometimes test fixtures must
rely on components that aren't 100% reliable. With flaky, instead of removing
those tests or marking them to @skip, they can be automatically retried.

%generate_buildrequires
%pyproject_buildrequires

%check
# adapted from upstream's tox.ini
%pytest -v -k 'example and not options' --doctest-modules test/test_pytest/
%pytest -v -k 'example and not options' test/test_pytest/
%pytest -v -p no:flaky test/test_pytest/test_flaky_pytest_plugin.py
%pytest -v --force-flaky --max-runs 2 test/test_pytest/test_pytest_options_example.py

%files -f %{pyproject_files}
%doc README.rst

%changelog
%{?autochangelog}
