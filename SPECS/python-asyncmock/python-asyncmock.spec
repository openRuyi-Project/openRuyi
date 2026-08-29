# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname asyncmock

Name:           python-%{srcname}
Version:        0.4.2
Release:        %autorelease
Summary:        Extension to the standard mock framework to support async
License:        BSD-3-Clause
URL:            https://github.com/timsavage/asyncmock
VCS:            git:https://github.com/timsavage/asyncmock.git
#!RemoteAsset:  sha256:c251889d542e98fe5f7ece2b5b8643b7d62b50a5657d34a4cbce8a1d5170d750
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
# The sdist on PyPI does not ship the license file, fetch it from upstream git
#!RemoteAsset:  sha256:b38c7751e59cac2e781088399f7cff523f40e76ed0fc11b331866af7d37bbe97
Source1:        https://raw.githubusercontent.com/timsavage/asyncmock/702bc65c8f1930578df0f53a08af160cba28f623/LICENSE
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Extension to the standard mock framework to provide support for mocking
asynchronous coroutines, built on top of the mock library.

%generate_buildrequires
%pyproject_buildrequires

%prep -a
# pytest-runner is deprecated and only needed for the removed test runner integration
sed -i '/pytest-runner/d' setup.cfg
cp %{SOURCE1} LICENSE

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
